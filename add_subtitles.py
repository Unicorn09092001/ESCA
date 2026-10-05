#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
add_subtitles.py — Công cụ tự động tạo và gắn phụ đề cho video kênh Cúspide Silenciosa.

TÍNH NĂNG:
  1. Nhận diện giọng nói tiếng Tây Ban Nha chính xác bằng faster-whisper.
  2. Tự động căn chỉnh (alignment) với file script.txt để đảm bảo 100% đúng chính tả, dấu câu Tây Ban Nha.
  3. Chia cụm từ giật nhịp 3-5 từ (High-Retention Rhythmic Chunks) chuẩn YouTube.
  4. Hiển thị kiểu Karaoke Highlight: từ đang đọc phát sáng theo màu nhận diện của Playlist.
  5. Xuất video hardsub siêu tốc với phần cứng Apple Silicon (h264_videotoolbox) + libass.
  6. Xuất đầy đủ file phụ đề mềm (.srt, .vtt, .ass) để tải lên YouTube Studio.

CÁCH DÙNG:
  # 1. Chạy cho 1 project cụ thể (tự động nhận diện video, audio, script và màu playlist):
  python3 add_subtitles.py --project "01_Disciplina y Habitos/project_03_rutina_matutina_perfecta_20260904"

  # 2. Xem trước nhanh 10 giây đầu (render chỉ mất 2-3s):
  python3 add_subtitles.py --project "01_Disciplina y Habitos/project_03_rutina_matutina_perfecta_20260904" --preview 10

  # 3. Xuất 1 frame ảnh xem trước bố cục phụ đề:
  python3 add_subtitles.py --project "01_Disciplina y Habitos/project_03_rutina_matutina_perfecta_20260904" --preview-frame 5.0

  # 4. Chạy trên 1 file video bất kỳ:
  python3 add_subtitles.py --video "path/to/video.mp4" --script "path/to/script.txt"

  # 5. Chạy hàng loạt tất cả project trong một playlist:
  python3 add_subtitles.py --playlist "01_Disciplina y Habitos"
"""

import os
import sys
import argparse
import json
import tempfile
from tools.config import (
    WORKSPACE_ROOT,
    detect_playlist_accent,
    hex_to_ass,
    DEFAULT_MIN_WORDS,
    DEFAULT_MAX_WORDS,
    DEFAULT_ALIGNMENT,
    DEFAULT_MARGIN_V
)
from tools.transcriber import (
    find_project_audio_and_script,
    extract_audio_from_video,
    transcribe_audio
)
from tools.ass_generator import (
    generate_ass_script,
    save_ass_file
)
from tools.srt_generator import (
    generate_srt_content,
    generate_vtt_content,
    parse_srt_file
)
from tools.video_renderer import (
    burn_subtitles_to_video,
    embed_soft_subtitles,
    extract_preview_frame
)
from tools.video_assembler import (
    assemble_video_from_images,
    get_project_title
)
from tools.xoa_watermark import clean_project

def process_single(
    video_path,
    audio_path=None,
    script_path=None,
    tv_path=None,
    srt_path=None,
    output_video_path=None,
    output_dir=None,
    style="karaoke",
    font_name="Anton",
    font_size=82,
    uppercase=False,
    min_words=DEFAULT_MIN_WORDS,
    max_words=DEFAULT_MAX_WORDS,
    accent_hex=None,
    preview_sec=None,
    preview_frame_sec=None,
    soft_subs=False,
    only_subs=False,
    whisper_model="base",
    force_transcribe=False,
    rebuild_video=False,
    **kwargs
):
    print("=" * 80)
    print(f"🎬 BẮT ĐẦU XỬ LÝ: {os.path.basename(video_path)}")
    print("=" * 80)

    if not os.path.isfile(video_path):
        print(f"❌ Không tìm thấy file video: {video_path}")
        return False

    video_dir = os.path.dirname(os.path.abspath(video_path))
    if not output_dir:
        output_dir = os.path.join(video_dir, "subtitles")
    os.makedirs(output_dir, exist_ok=True)

    base_name = os.path.splitext(os.path.basename(video_path))[0]
    
    # Detect accent color from path
    if accent_hex:
        accent_ass = hex_to_ass(accent_hex)
        print(f"🎨 Màu nhấn tùy chỉnh: {accent_hex}")
    else:
        playlist_info = detect_playlist_accent(video_path)
        accent_ass = playlist_info["ass"]
        print(f"🎨 Nhận diện Playlist: {playlist_info['name']} (Mã màu: {playlist_info['hex']})")

    # Step 1: Obtain word tokens with timestamps
    words = []
    words_cache_file = os.path.join(output_dir, f"{base_name}_words.json")
    if not force_transcribe and os.path.isfile(words_cache_file):
        print(f"⚡ Sử dụng dữ liệu phiên âm đã lưu: {words_cache_file}")
        with open(words_cache_file, "r", encoding="utf-8") as f:
            words = json.load(f)
    elif srt_path and os.path.isfile(srt_path):
        print(f"📄 Sử dụng file SRT có sẵn: {srt_path}")
        words = parse_srt_file(srt_path)
    else:
        # Determine audio
        temp_audio = None
        if not audio_path or not os.path.isfile(audio_path):
            print("🔊 Không có audio riêng, đang tách âm thanh trực tiếp từ video...")
            temp_audio = os.path.join(output_dir, f"{base_name}_extracted.mp3")
            extract_audio_from_video(video_path, temp_audio)
            audio_to_use = temp_audio
        else:
            audio_to_use = audio_path

        words = transcribe_audio(
            audio_path=audio_to_use,
            script_path=script_path,
            model_size=whisper_model,
            language="es"
        )
        if words:
            with open(words_cache_file, "w", encoding="utf-8") as f:
                json.dump(words, f, ensure_ascii=False, indent=2)

        if temp_audio and os.path.isfile(temp_audio):
            try:
                os.remove(temp_audio)
            except Exception:
                pass

    if not words:
        print("❌ Không trích xuất được từ nào từ âm thanh!")
        return False

    # Step 2: Generate Subtitle Files (.ass, .srt, .vtt)
    ass_path = os.path.join(output_dir, f"{base_name}.ass")
    srt_out_path = os.path.join(output_dir, f"{base_name}.srt")
    vtt_out_path = os.path.join(output_dir, f"{base_name}.vtt")

    print(f"📝 Đang tạo phụ đề ASS (Style: {style}, Font: {font_name}, Cụm: {min_words}-{max_words} từ)...")
    if tv_path and os.path.isfile(tv_path):
        print(f"🎞️  Đồng bộ phụ đề với từng khung hình theo: {os.path.basename(tv_path)}")
    ass_content = generate_ass_script(
        words=words,
        tv_path=tv_path,
        accent_color_ass=accent_ass,
        style=style,
        font_name=font_name,
        font_size=font_size,
        uppercase=uppercase,
        min_words=min_words,
        max_words=max_words,
        margin_v=DEFAULT_MARGIN_V,
        alignment=DEFAULT_ALIGNMENT
    )
    save_ass_file(ass_content, ass_path)

    srt_content = generate_srt_content(words, tv_path=tv_path, min_words=min_words, max_words=max_words)
    with open(srt_out_path, "w", encoding="utf-8") as f:
        f.write(srt_content)

    vtt_content = generate_vtt_content(words, tv_path=tv_path, min_words=min_words, max_words=max_words)
    with open(vtt_out_path, "w", encoding="utf-8") as f:
        f.write(vtt_content)

    print(f"💾 Đã lưu file ASS: {ass_path}")
    print(f"💾 Đã lưu file SRT (YouTube CC): {srt_out_path}")
    print(f"💾 Đã lưu file VTT: {vtt_out_path}")

    # If preview frame requested
    if preview_frame_sec is not None:
        frame_img_path = os.path.join(output_dir, f"{base_name}_frame_{preview_frame_sec}s.jpg")
        print(f"🖼️  Đang trích xuất frame ảnh tại {preview_frame_sec}s...")
        extract_preview_frame(video_path, ass_path, frame_img_path, timestamp_sec=preview_frame_sec)
        print(f"✅ Ảnh xem trước: {frame_img_path}")

    if only_subs:
        print("🏁 Đã tạo xong toàn bộ phụ đề (Chế độ --only-subs).")
        return True

    # Step 3: Render Subtitled Video
    if preview_sec:
        out_video = os.path.join(video_dir, f"{base_name}_preview_{preview_sec}s.mp4")
    elif output_video_path:
        out_video = output_video_path
    else:
        out_video = os.path.join(video_dir, f"{base_name}_subtitled.mp4")

    if soft_subs:
        embed_soft_subtitles(video_path, srt_out_path, out_video)
    else:
        burn_subtitles_to_video(
            video_path=video_path,
            ass_path=ass_path,
            output_path=out_video,
            preview_sec=preview_sec
        )

    print(f"🎉 HOÀN TẤT: {out_video}\n")
    return True

def process_project(project_dir, **kwargs):
    """Processes a project directory automatically discovering assets and building video if needed."""
    abs_project = os.path.abspath(project_dir)
    if not os.path.isdir(abs_project):
        print(f"❌ Không tìm thấy thư mục project: {project_dir}")
        return False

    video_path, audio_path, script_path, tv_path = find_project_audio_and_script(abs_project)
    images_dir = os.path.join(abs_project, "images")

    rebuild_video = kwargs.get("rebuild_video", False)
    if (not video_path or rebuild_video) and os.path.isdir(images_dir) and audio_path and tv_path:
        title = get_project_title(abs_project)
        target_video_path = os.path.join(abs_project, f"{title}.mp4")

        print(f"📁 Project: {os.path.basename(abs_project)}")
        print(f"   🖼️  Tìm thấy thư mục ảnh: {os.path.basename(images_dir)} (Đánh số 1, 2, 3...)")
        print(f"   🔊 Audio : {os.path.basename(audio_path)}")
        print(f"   🎞️ Visuals: {os.path.basename(tv_path)}")
        print(f"🚀 Tự động kích hoạt module ghép ảnh thành video: {os.path.basename(target_video_path)} ...")

        # Step 1: Ensure transcription words are available for timeline alignment
        output_dir = kwargs.get("output_dir") or os.path.join(abs_project, "subtitles")
        os.makedirs(output_dir, exist_ok=True)
        words_cache_file = os.path.join(output_dir, f"{title}_words.json")

        words = []
        if not kwargs.get("force_transcribe") and os.path.isfile(words_cache_file):
            print(f"⚡ Sử dụng dữ liệu phiên âm đã lưu: {words_cache_file}")
            with open(words_cache_file, "r", encoding="utf-8") as f:
                words = json.load(f)
        else:
            words = transcribe_audio(
                audio_path=audio_path,
                script_path=script_path,
                model_size=kwargs.get("whisper_model", "base"),
                language="es"
            )
            if words:
                with open(words_cache_file, "w", encoding="utf-8") as f:
                    json.dump(words, f, ensure_ascii=False, indent=2)

        if not words:
            print("❌ Không trích xuất được từ nào từ âm thanh!")
            return False

        # Step 2: Strip the Gemini watermark (images_clean/ + thumbnail/*_clean), then assemble
        clean_images_dir = clean_project(abs_project)
        assemble_video_from_images(
            images_dir=clean_images_dir,
            audio_path=audio_path,
            words=words,
            tv_path=tv_path,
            output_video_path=target_video_path,
            preview_sec=None,  # Always assemble full base video so it persists cleanly
            use_videotoolbox=True
        )
        video_path = target_video_path

    if not video_path:
        print(f"❌ Không tìm thấy file .mp4 nào và không đủ dữ liệu (images + audio + visuals) để tự động ghép trong: {project_dir}")
        return False

    print(f"📁 Project: {os.path.basename(abs_project)}")
    print(f"   🎥 Video : {os.path.basename(video_path)}")
    print(f"   🔊 Audio : {os.path.basename(audio_path) if audio_path else 'Tách từ video'}")
    print(f"   📜 Script: {os.path.basename(script_path) if script_path else 'Không có (Dùng Whisper thuần)'}")
    print(f"   🎞️ Visuals: {os.path.basename(tv_path) if tv_path else 'Không có (Dùng ngắt câu thuần)'}")

    return process_single(
        video_path=video_path,
        audio_path=audio_path,
        script_path=script_path,
        tv_path=tv_path,
        **kwargs
    )

def process_playlist(playlist_dir, **kwargs):
    """Processes all project_* folders inside a playlist directory."""
    abs_playlist = os.path.abspath(playlist_dir)
    if not os.path.isdir(abs_playlist):
        print(f"❌ Không tìm thấy thư mục playlist: {playlist_dir}")
        return False

    subdirs = sorted([
        os.path.join(abs_playlist, d) for d in os.listdir(abs_playlist)
        if os.path.isdir(os.path.join(abs_playlist, d)) and "project" in d.lower()
    ])

    if not subdirs:
        print(f"⚠️  Không tìm thấy project_* nào trong playlist: {playlist_dir}")
        return False

    print(f"📋 Tìm thấy {len(subdirs)} project trong playlist. Bắt đầu xử lý...")
    success_count = 0
    for p in subdirs:
        try:
            ok = process_project(p, **kwargs)
            if ok:
                success_count += 1
        except Exception as e:
            print(f"❌ Lỗi khi xử lý {p}: {e}")

    print(f"🏁 Hoàn thành playlist! Đã xử lý thành công {success_count}/{len(subdirs)} projects.")
    return True

def main():
    parser = argparse.ArgumentParser(description="Tool tự động gắn phụ đề video kênh Cúspide Silenciosa")
    
    # Target selection
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--project", "-p", help="Đường dẫn tới thư mục project (vd: '01_Disciplina y Habitos/project_03_...')")
    group.add_argument("--video", "-v", help="Đường dẫn tới file video .mp4 đơn lẻ")
    group.add_argument("--playlist", help="Đường dẫn tới thư mục playlist để chạy hàng loạt (vd: '01_Disciplina y Habitos')")

    # Options
    parser.add_argument("--audio", "-a", help="Đường dẫn file âm thanh (nếu chạy --video)")
    parser.add_argument("--script", "-s", help="Đường dẫn file script.txt để căn chỉnh chính tả")
    parser.add_argument("--tv", help="Đường dẫn file transcript_and_visuals.txt để đồng bộ từng khung hình")
    parser.add_argument("--srt", help="Sử dụng file .srt có sẵn thay vì chạy Whisper")
    parser.add_argument("--out", "-o", help="Đường dẫn file video đầu ra (tùy chọn)")
    parser.add_argument("--rebuild-video", action="store_true", help="Bắt buộc ghép lại video từ ảnh gốc kể cả khi đã có video .mp4")

    # Styling
    parser.add_argument("--style", choices=["karaoke", "minimalist_dark", "box_pill"], default="karaoke",
                        help="Phong cách phụ đề: karaoke (mặc định), minimalist_dark, box_pill")
    parser.add_argument("--font", default="Anton", help="Tên Font chữ (mặc định: Anton, hoặc Inter, Arial)")
    parser.add_argument("--size", type=int, default=82, help="Kích thước font chữ (mặc định: 82, tối ưu cho mobile)")
    parser.add_argument("--accent", help="Mã màu HEX cho từ nhấn (vd: #FF5A36, mặc định tự nhận theo playlist)")
    parser.add_argument("--uppercase", action="store_true", help="Viết HOA toàn bộ phụ đề (chuẩn YouTube retention)")
    parser.add_argument("--min-words", type=int, default=2, help="Số từ tối thiểu mỗi cụm (mặc định: 2)")
    parser.add_argument("--max-words", type=int, default=4, help="Số từ tối đa mỗi cụm (mặc định: 4, chuẩn 3-5 từ giật nhịp)")

    # Testing & output modes
    parser.add_argument("--preview", type=int, help="Chế độ render thử nghiệm: chỉ render N giây đầu (vd: --preview 10)")
    parser.add_argument("--preview-frame", type=float, help="Chỉ trích xuất 1 ảnh frame xem trước tại giây thứ N (vd: --preview-frame 5.0)")
    parser.add_argument("--soft", action="store_true", help="Gắn softsub track vào MP4 thay vì burn hardsub (xong ngay lập tức)")
    parser.add_argument("--only-subs", action="store_true", help="Chỉ tạo file phụ đề (.ass, .srt, .vtt) mà không render video")
    parser.add_argument("--force-transcribe", action="store_true", help="Bắt buộc chạy lại Whisper bỏ qua cache")
    parser.add_argument("--model", default="base", choices=["tiny", "base", "small", "medium"], help="Mô hình whisper (mặc định: base)")

    args = parser.parse_args()

    common_kwargs = dict(
        style=args.style,
        font_name=args.font,
        font_size=args.size,
        uppercase=args.uppercase,
        min_words=args.min_words,
        max_words=args.max_words,
        accent_hex=args.accent,
        preview_sec=args.preview,
        preview_frame_sec=args.preview_frame,
        soft_subs=args.soft,
        only_subs=args.only_subs,
        whisper_model=args.model,
        force_transcribe=args.force_transcribe,
        rebuild_video=args.rebuild_video
    )

    if args.project:
        process_project(args.project, output_video_path=args.out, **common_kwargs)
    elif args.video:
        process_single(
            video_path=args.video,
            audio_path=args.audio,
            script_path=args.script,
            tv_path=args.tv,
            srt_path=args.srt,
            output_video_path=args.out,
            **common_kwargs
        )
    elif args.playlist:
        process_playlist(args.playlist, **common_kwargs)

if __name__ == "__main__":
    main()

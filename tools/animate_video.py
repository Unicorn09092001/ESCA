#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
animate_video.py — Bản "motion graphics" của render_video.py: thay vì ảnh tĩnh + zoom, mỗi khung
được dựng lại 30 lần/giây từ các lớp SVG của draw_frames.build_layers() với chuyển động kiểu GSAP:

  • nhân vật chính hiện trước, các lớp còn lại bật ra lần lượt (stagger, ease-out-back, trồi lên)
  • vật nhấn #8B6CFF đập nhịp nhẹ (scale + quầng sáng) sau khi xuất hiện
  • nhân vật "thở" (nhấp nhô 3px), chuỗi 7 chấm hiện từng chấm, hạt sáng bay lên
  • camera trôi chậm 1.00↔1.04, mỗi cảnh mở bằng fade 0.25s
Sau đó ghép giọng đọc + burn phụ đề karaoke (dùng lại build_ass/chunks_of của render_video.py).

Cách dùng:
  python3 tools/animate_video.py --project "05_Autoconocimiento/project_28_..." --audio voz_gonzalo.mp3 \
      --title 7_senales_autosabotaje_motion [--preview 20] [--workers 4]
"""
import argparse
import json
import math
import os
import re
import subprocess
import sys
from multiprocessing import Pool

import cairosvg

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from projectkit import load_scenes  # noqa: E402
from render_video import build_ass, build_srt, chunks_of, hex_to_ass  # noqa: E402
from sticklib import svg_doc  # noqa: E402

FPS = 30
APPEAR = 0.5  # thời lượng hiệu ứng xuất hiện của một lớp
GHOST_DASH = 'stroke-dasharray="16 13"'

_layers_cache = {}
_scenes = None


def _init_worker(project):
    global _scenes
    _scenes = load_scenes(project)


def ease_out_back(x, k=1.6):
    x = min(max(x, 0.0), 1.0)
    return 1 + (k + 1) * (x - 1) ** 3 + k * (x - 1) ** 2


def ease_out(x):
    x = min(max(x, 0.0), 1.0)
    return 1 - (1 - x) ** 3


def layers_for(n, shot):
    key = (n, shot)
    if key not in _layers_cache:
        _layers_cache[key] = _scenes.build_layers(n, shot)
    return _layers_cache[key]


def schedule(layers, dur):
    """Thời điểm xuất hiện từng lớp: nhân vật chính t=0, phần còn lại lần lượt."""
    main = [i for i, l in enumerate(layers) if "data-fig" in l and GHOST_DASH not in l]
    rest = [i for i in range(len(layers)) if i not in main]
    t0 = {i: 0.0 for i in main}
    span = max(min(dur * 0.45, 2.4), 0.3)
    step = min(0.38, span / max(len(rest), 1))
    for k, i in enumerate(rest):
        t0[i] = 0.12 + k * step
    return t0


def animate_layer(svg, t, appear_t, seed):
    lt = t - appear_t
    if lt < 0:
        return ""
    p = ease_out_back(lt / APPEAR)
    op = ease_out(lt / (APPEAR * 0.8))
    dy = (1 - p) * 26

    def acc_sub(m):
        cx, cy = map(float, m.group(1).split(","))
        sc = 0.55 + 0.45 * p
        if lt > APPEAR:
            sc *= 1 + 0.035 * math.sin(2 * math.pi * (lt - APPEAR) / 2.2)
        return f'transform="translate({cx:.1f},{cy:.1f}) scale({sc:.4f}) translate({-cx:.1f},{-cy:.1f})"'

    def fig_sub(m):
        x, y, s = map(float, m.group(1).split(","))
        bob = 3.0 * s * math.sin(2 * math.pi * t / 3.2 + x / 300)
        breathe = 1 + 0.006 * math.sin(2 * math.pi * t / 3.2 + x / 300)
        return (f'transform="translate({x:.1f},{y + bob:.1f}) scale(1,{breathe:.4f}) translate({-x:.1f},{-y:.1f})"')

    def dot_sub(m):
        i = int(m.group(1))
        o = ease_out((lt - i * 0.14) / 0.35)
        return f'opacity="{max(o, 0):.3f}"'

    svg = re.sub(r'data-acc="([^"]+)"', acc_sub, svg)
    svg = re.sub(r'data-fig="([^"]+)"', fig_sub, svg)
    svg = re.sub(r'data-dot="(\d+)"', dot_sub, svg)
    svg = svg.replace('data-drift="1"', f'transform="translate(0,{-14 * lt:.1f})"')
    return f'<g opacity="{op:.3f}" transform="translate(0,{dy:.1f})">{svg}</g>'


def render_frame(args):
    n, shot, t, dur = args
    layers = layers_for(n, shot)
    t0 = schedule(layers, dur)
    body = "".join(animate_layer(l, t, t0[i], i) for i, l in enumerate(layers))
    z = 1.0 + 0.04 * (t / max(dur, 0.1)) if n % 2 else 1.04 - 0.04 * (t / max(dur, 0.1))
    fade = max(0.0, 1 - t / 0.25)
    cam = f'<g transform="translate(960,540) scale({z:.4f}) translate(-960,-540)">{body}</g>'
    cover = f'<rect width="1920" height="1080" fill="#000" opacity="{fade:.3f}"/>' if fade > 0 else ""
    return cairosvg.svg2png(bytestring=svg_doc(cam + cover).encode("utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", required=True)
    ap.add_argument("--audio", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--accent", help="Ghi đè màu nhấn (mặc định theo youtube_metadata.txt)")
    ap.add_argument("--fonts", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "fonts"))
    ap.add_argument("--preview", type=float)
    ap.add_argument("--workers", type=int, default=os.cpu_count())
    args = ap.parse_args()

    proj = os.path.abspath(args.project)
    _init_worker(proj)
    accent = _scenes.META["accent"]
    frames = json.load(open(os.path.join(proj, "subtitles", "timeline.json"), encoding="utf-8"))
    audio = os.path.join(proj, args.audio)
    sub_dir = os.path.join(proj, "subtitles")
    chunks = chunks_of(frames)
    ass_path = os.path.join(sub_dir, f"{args.title}.ass")
    open(ass_path, "w", encoding="utf-8").write(build_ass(chunks, hex_to_ass(args.accent or accent)))
    open(os.path.join(sub_dir, f"{args.title}.srt"), "w", encoding="utf-8").write(build_srt(chunks))

    limit = args.preview or frames[-1]["end"]
    jobs = []
    for i, fr in enumerate(frames, 1):
        f0, f1 = round(fr["start"] * FPS), round(min(fr["end"], limit) * FPS)
        dur = fr["end"] - fr["start"]
        for f in range(f0, f1):
            jobs.append((i, fr.get("shot", "MEDIUM SHOT"), (f - f0) / FPS, dur))
        if fr["end"] >= limit:
            break
    print(f"🎞️  Dựng {len(jobs)} khung hình ({len(jobs) / FPS:.1f}s) với {args.workers} tiến trình...")

    out_name = f"{args.title}_preview_{int(limit)}s.mp4" if args.preview else f"{args.title}.mp4"
    out_path = os.path.join(proj, out_name)
    ass_esc = ass_path.replace("\\", "/").replace(":", "\\:").replace("'", "\\'")
    vf = f"subtitles='{ass_esc}':fontsdir='{os.path.abspath(args.fonts)}',format=yuv420p"
    cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
           "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "png", "-i", "-", "-i", audio,
           "-map", "0:v", "-map", "1:a", "-vf", vf, "-c:v", "libx264", "-preset", "medium", "-crf", "20",
           "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-movflags", "+faststart", "-shortest", out_path]
    ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    with Pool(args.workers, initializer=_init_worker, initargs=(proj,)) as pool:
        for k, png in enumerate(pool.imap(render_frame, jobs, chunksize=8), 1):
            ff.stdin.write(png)
            if k % 300 == 0:
                print(f"   {k}/{len(jobs)}", flush=True)
    ff.stdin.close()
    if ff.wait() != 0:
        raise SystemExit("ffmpeg lỗi")
    print(f"🎉 HOÀN TẤT: {out_path}")


if __name__ == "__main__":
    main()

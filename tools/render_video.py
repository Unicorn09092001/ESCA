#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
render_video.py — Ghép ảnh từng Frame + giọng đọc + phụ đề karaoke thành video 1080p30.

Đầu vào (trong thư mục project):
  images/img_NNN.png, subtitles/timeline.json (từ align_frames.py), <audio>.mp3
Đầu ra:
  subtitles/<title>.ass / .srt   — phụ đề karaoke (burn) + phụ đề YouTube CC
  <title>.mp4                    — video hoàn chỉnh đã gắn phụ đề

Cách dùng:
  python3 tools/render_video.py --project "05_Autoconocimiento/project_28_..." --audio voz_gonzalo.mp3 \
      --title "7_senales_autosabotaje" --accent "#8B6CFF"
"""
import argparse
import json
import os
import re
import subprocess
import tempfile

FPS = 30
PUNCT_END = re.compile(r"[,.;:?!…]$|[—–]$")


def hex_to_ass(h):
    h = h.lstrip("#")
    return f"&H00{h[4:6]}{h[2:4]}{h[0:2]}&".upper()


def ts_ass(t):
    cs = int(round(t * 100))
    return f"{cs // 360000}:{cs // 6000 % 60:02d}:{cs // 100 % 60:02d}.{cs % 100:02d}"


def ts_srt(t):
    ms = int(round(t * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def merge_dashes(words):
    out = []
    for w in words:
        if w["word"] in ("—", "–", "-") and out:
            out[-1] = dict(out[-1], word=out[-1]["word"] + " —", end=w["end"])
        else:
            out.append(dict(w))
    return out


def chunks_of(frames, min_words=2, max_words=4):
    """Cụm 2–4 từ giật nhịp, ngắt ở dấu câu; không vượt ranh giới Frame."""
    res = []
    for fr in frames:
        ws = merge_dashes(fr["words"])
        cur = []
        for i, w in enumerate(ws):
            cur.append(w)
            rest = len(ws) - i - 1
            if (len(cur) >= max_words or (len(cur) >= min_words and PUNCT_END.search(w["word"]))) \
                    and rest != 1:
                res.append(cur)
                cur = []
        if cur:
            if res and len(cur) == 1 and res[-1][-1]["end"] >= fr["start"] and len(res[-1]) < max_words \
                    and res[-1][0]["start"] >= fr["start"]:
                res[-1].extend(cur)
            else:
                res.append(cur)
    return res


def esc(t):
    return t.replace("{", "(").replace("}", ")")


def build_ass(chunks, accent_ass, font="Anton", size=82, margin_v=70):
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Karaoke,{font},{size},&H00F0F5F5,&H00F0F5F5,&H00000000,&H96000000,0,0,0,0,100,100,1,0,1,5,2,2,80,80,{margin_v},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    ev = []
    for ch in chunks:
        for i, w in enumerate(ch):
            st = w["start"]
            en = ch[i + 1]["start"] if i + 1 < len(ch) else w["end"]
            if en - st < 0.04:
                continue
            parts = []
            for j, x in enumerate(ch):
                t = esc(x["word"])
                parts.append(f"{{\\c{accent_ass}}}{t}{{\\c&H00F0F5F5&}}" if j == i else t)
            ev.append(f"Dialogue: 0,{ts_ass(st)},{ts_ass(en)},Karaoke,,0,0,0,,{' '.join(parts)}")
    return head + "\n".join(ev) + "\n"


def build_srt(chunks):
    out = []
    for n, ch in enumerate(chunks, 1):
        out.append(f"{n}\n{ts_srt(ch[0]['start'])} --> {ts_srt(ch[-1]['end'])}\n{' '.join(w['word'] for w in ch)}\n")
    return "\n".join(out)


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(r.stderr[-3000:])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", required=True)
    ap.add_argument("--audio", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--accent", default="#8B6CFF")
    ap.add_argument("--fonts", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "fonts"))
    ap.add_argument("--preview", type=float, help="Chỉ render N giây đầu")
    args = ap.parse_args()

    proj = os.path.abspath(args.project)
    frames = json.load(open(os.path.join(proj, "subtitles", "timeline.json"), encoding="utf-8"))
    audio = os.path.join(proj, args.audio)
    sub_dir = os.path.join(proj, "subtitles")

    chunks = chunks_of(frames)
    ass_path = os.path.join(sub_dir, f"{args.title}.ass")
    open(ass_path, "w", encoding="utf-8").write(build_ass(chunks, hex_to_ass(args.accent)))
    open(os.path.join(sub_dir, f"{args.title}.srt"), "w", encoding="utf-8").write(build_srt(chunks))
    print(f"📝 Phụ đề: {len(chunks)} cụm → {ass_path}")

    limit = args.preview or frames[-1]["end"]
    tmp = tempfile.mkdtemp(prefix="render_")
    clips = []
    for i, fr in enumerate(frames, 1):
        if fr["start"] >= limit:
            break
        f0 = round(fr["start"] * FPS)
        f1 = round(min(fr["end"], limit) * FPS)
        n = max(f1 - f0, 1)
        img = os.path.join(proj, "images", f"img_{i:03d}.png")
        out = os.path.join(tmp, f"c{i:03d}.mp4")
        z0, z1 = (1.0, 1.06) if i % 2 else (1.06, 1.0)
        zexpr = f"{z0}+({z1}-{z0})*on/{n}"
        vf = (f"scale=2304:1296,zoompan=z='{zexpr}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080:fps={FPS},"
              f"fade=t=in:st=0:d=0.25,format=yuv420p")
        run(["ffmpeg", "-y", "-hide_banner", "-loop", "1", "-framerate", str(FPS), "-i", img, "-frames:v", str(n),
             "-vf", vf, "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-r", str(FPS), out])
        clips.append(out)
        print(f"\r🎞️  Clip {i}/{len(frames)}", end="", flush=True)
    print()
    lst = os.path.join(tmp, "list.txt")
    open(lst, "w").write("".join(f"file '{c}'\n" for c in clips))
    base = os.path.join(tmp, "base.mp4")
    run(["ffmpeg", "-y", "-hide_banner", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", base])

    out_name = f"{args.title}_preview_{int(limit)}s.mp4" if args.preview else f"{args.title}.mp4"
    out_path = os.path.join(proj, out_name)
    fonts = os.path.abspath(args.fonts)
    ass_esc = ass_path.replace("\\", "/").replace(":", "\\:").replace("'", "\\'")
    vf = f"subtitles='{ass_esc}':fontsdir='{fonts}'"
    cmd = ["ffmpeg", "-y", "-hide_banner", "-i", base, "-i", audio, "-map", "0:v", "-map", "1:a",
           "-vf", vf, "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-movflags", "+faststart", "-shortest"]
    if args.preview:
        cmd += ["-t", str(limit)]
    run(cmd + [out_path])
    print(f"🎉 HOÀN TẤT: {out_path}")


if __name__ == "__main__":
    main()

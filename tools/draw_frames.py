#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
draw_frames.py — Vẽ ảnh tĩnh từng Frame (images/img_NNN.png) bằng code, theo [VISUAL DESCRIPTION] +
[STYLE RULES] của transcript_and_visuals.txt (người que nét trắng ấm, nền #0B0B0C, 1 vật nhấn màu playlist).
Kịch bản hình nằm ở <project>/scenes.py (build_layers(n, shot)); màu nhấn đọc từ youtube_metadata.txt.

Cách dùng:
  python3 tools/draw_frames.py --project "05_Autoconocimiento/project_28_7_senales_autosabotaje"
  python3 tools/draw_frames.py --project ... --only 1,5,12      # vẽ lại vài khung
"""
import argparse
import json
import os
import sys

import cairosvg

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from projectkit import load_scenes  # noqa: E402
from scenekit import finalize_static  # noqa: E402
from sticklib import svg_doc  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", required=True)
    ap.add_argument("--only", help="Danh sách số khung, vd 1,5,12")
    args = ap.parse_args()
    scenes = load_scenes(args.project)
    tl = json.load(open(os.path.join(args.project, "subtitles", "timeline.json"), encoding="utf-8"))
    out_dir = os.path.join(args.project, "images")
    os.makedirs(out_dir, exist_ok=True)
    only = {int(x) for x in args.only.split(",")} if args.only else None
    for i, fr in enumerate(tl, 1):
        if only and i not in only:
            continue
        svg = finalize_static(svg_doc("".join(scenes.build_layers(i, fr.get("shot", "MEDIUM SHOT")))))
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=os.path.join(out_dir, f"img_{i:03d}.png"))
    print(f"✅ Đã vẽ {len(only) if only else len(tl)} khung → {out_dir}")


if __name__ == "__main__":
    main()

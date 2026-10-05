#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_thumbnails.py — Thumbnail 1280x720 theo 2 bố cục trong youtube_metadata.txt:
  Mẫu B: triptych 3 khung  ·  Mẫu C: lưới 6 khung (2x3)
Nội dung từng khung lấy từ thumb_b()/thumb_c() trong <project>/scenes.py; headline + từ nhấn + màu
playlist đọc từ youtube_metadata.txt. Nhân vật vẽ theo phong cách người que của kênh (không dùng ảnh AI).

Cách dùng:
  python3 tools/make_thumbnails.py --project "01_Disciplina y Habitos/project_14_..."
"""
import argparse
import os
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from projectkit import load_scenes  # noqa: E402
from thumbkit import headline, render  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", required=True)
    args = ap.parse_args()
    scenes = load_scenes(args.project)
    meta = scenes.META
    out = os.path.join(args.project, "thumbnail")
    os.makedirs(out, exist_ok=True)
    for name, fn in (("thumbnail_B_triptych.png", scenes.thumb_b), ("thumbnail_C_grid.png", scenes.thumb_c)):
        img, ratio = headline(render("".join(fn())), meta["headline"], meta["accent_word"])
        img.save(os.path.join(out, name))
        img.resize((160, 90), Image.LANCZOS).save(os.path.join(out, name.replace(".png", "_160x90.png")))
        print(f"✅ {name}  (khối chữ ≈ {ratio * 100:.0f}% chiều cao ảnh)")


if __name__ == "__main__":
    main()

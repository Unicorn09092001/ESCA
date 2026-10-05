#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_chapters.py — Thay timestamp ƯỚC TÍNH trong youtube_metadata.txt bằng timestamp THẬT:
tên chương lấy theo thứ tự từ mục CHAPTERS của metadata, thời điểm = Frame đầu tiên của mỗi ESCENA
trong subtitles/timeline.json. Ghi ra <project>/chapters.txt.

Cách dùng:
  python3 tools/make_chapters.py --project "01_Disciplina y Habitos/project_14_..."
"""
import argparse
import json
import os
import re


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", required=True)
    args = ap.parse_args()
    meta = open(os.path.join(args.project, "youtube_metadata.txt"), encoding="utf-8").read()
    sec = meta[meta.find("CHAPTERS"):]
    names = re.findall(r"^\d+:\d{2}\s+(.+)$", sec, flags=re.M)
    tl = json.load(open(os.path.join(args.project, "subtitles", "timeline.json"), encoding="utf-8"))
    starts, seen = [], set()
    for f in tl:
        sc = f["id"].split("_")[0]
        if sc not in seen:
            seen.add(sc)
            starts.append(0.0 if not starts else f["start"])
    if len(names) != len(starts):
        print(f"⚠️  Metadata có {len(names)} chương, timeline có {len(starts)} cảnh — ghép theo thứ tự tối đa.")
    lines = [f"{int(t // 60)}:{int(t % 60):02d} {n}" for t, n in zip(starts, names)]
    txt = ("CHAPTERS — timestamp THẬT (căn theo audio, xem subtitles/timeline.json)\n\n"
           + "\n".join(lines) + "\n")
    open(os.path.join(args.project, "chapters.txt"), "w", encoding="utf-8").write(txt)
    print(txt)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
align_frames.py — Căn thời gian từng Frame (transcript_and_visuals.txt) theo audio,
không cần Whisper: dò khoảng lặng bằng ffmpeg silencedetect rồi dùng quy hoạch động
chọn các khoảng lặng làm ranh giới Frame sao cho tốc độ đọc mỗi Frame sát tốc độ trung bình.
Thời gian từng từ trong Frame được chia theo tỉ lệ ký tự trên các đoạn có tiếng.

Xuất: <project>/subtitles/timeline.json
  [{"id": "S01_F001", "scene": "...", "es": "...", "visual": "...", "start": s, "end": s,
    "words": [{"word": "...", "start": s, "end": s}, ...]}, ...]

Cách dùng:
  python3 tools/align_frames.py --project "05_Autoconocimiento/project_28_..." --audio voz_gonzalo.mp3
"""
import argparse
import json
import os
import re
import subprocess


def parse_frames(tv_path):
    frames, scene = [], ""
    cur = None
    lines = open(tv_path, encoding="utf-8").read().splitlines()
    i = 0
    while i < len(lines):
        ln = lines[i]
        m = re.match(r"^## ESCENA \d+: (.*)$", ln)
        if m:
            scene = m.group(1).strip()
        m = re.match(r"^\[FRAME ID\]: (\S+)", ln)
        if m:
            cur = {"id": m.group(1), "scene": scene}
            frames.append(cur)
        if cur is not None:
            if ln.startswith("[SHOT TYPE]:"):
                cur["shot"] = ln.split(":", 1)[1].strip()
            elif ln.startswith("[ES]:"):
                cur["es"] = ln.split(":", 1)[1].strip()
            elif ln.startswith("[VISUAL DESCRIPTION]:"):
                cur["visual"] = lines[i + 1].strip()
        i += 1
    return frames


def detect_silences(audio, noise_db=-33, min_dur=0.07):
    out = subprocess.run(
        ["ffmpeg", "-hide_banner", "-i", audio, "-af",
         f"silencedetect=noise={noise_db}dB:d={min_dur}", "-f", "null", "-"],
        capture_output=True, text=True).stderr
    starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", out)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", out)]
    dur = float(re.search(r"Duration: (\d+):(\d+):([\d.]+)", out).groups()[2]) + \
        60 * float(re.search(r"Duration: (\d+):(\d+):([\d.]+)", out).groups()[1])
    sil = list(zip(starts, ends + [dur] * (len(starts) - len(ends))))
    return sil, dur


def weight(text):
    # Ký tự có tiếng + phạt cho dấu câu (người đọc ngắt nghỉ)
    letters = len(re.sub(r"[^\wáéíóúñü]", "", text, flags=re.I))
    pauses = len(re.findall(r"[.,:;—?!]", text))
    return letters + 6 * pauses


def align(frames, sil, dur):
    """Quy hoạch động theo đoạn: mỗi Frame là một khoảng giữa hai khoảng lặng; chi phí =
    (log(thời lượng có tiếng / thời lượng kỳ vọng))^2 — kỳ vọng = trọng số ký tự × tốc độ đọc
    trung bình — trừ điểm thưởng cho khoảng lặng ranh giới dài (thường là dấu câu)."""
    import math
    speech_start = sil[0][1] if sil and sil[0][0] < 0.05 else 0.0
    speech_end = sil[-1][0] if sil and sil[-1][1] >= dur - 0.05 else dur
    inner = [s for s in sil if s[0] > speech_start + 0.1 and s[1] < speech_end - 0.1]
    # điểm cắt: 0 = đầu bài, 1..m = khoảng lặng, m+1 = cuối bài
    cuts = [(speech_start, speech_start)] + inner + [(speech_end, speech_end)]
    m = len(cuts)
    # thời lượng có tiếng tích luỹ tới đầu mỗi điểm cắt
    def speech_between(a, b):
        t = cuts[b][0] - cuts[a][1]
        for k in range(a + 1, b):
            t -= cuts[k][1] - cuts[k][0]
        return max(t, 0.05)
    w = [weight(f["es"]) for f in frames]
    n = len(frames)
    rate = speech_between(0, m - 1) / sum(w)
    INF = float("inf")
    cost = [[INF] * m for _ in range(n + 1)]
    back = [[-1] * m for _ in range(n + 1)]
    cost[0][0] = 0.0
    ends = ["sent" if re.search(r"[.?!…][\"”»']?$", f["es"].strip()) else "other" for f in frames]
    for i in range(1, n + 1):
        exp = w[i - 1] * rate
        for b in range(i, m):
            if i == n and b != m - 1:
                continue
            if b == m - 1:
                bonus = 0.0
            else:
                gap = cuts[b][1] - cuts[b][0]
                bonus = 0.6 * min(gap, 1.0)
                # edge-tts: hết câu (. ? !) ngắt ~1.2s, dấu phẩy ~0.3s, giữa câu không ngắt
                if ends[i - 1] == "sent" and gap < 0.8:
                    bonus -= 0.8
                elif ends[i - 1] != "sent" and gap > 0.9:
                    bonus -= 0.8
            best, arg = INF, -1
            for a in range(i - 1, b):
                if cost[i - 1][a] == INF:
                    continue
                d = speech_between(a, b)
                if d > 4 * exp + 3:
                    continue
                c = cost[i - 1][a] + math.log(d / exp) ** 2 - bonus
                if c < best:
                    best, arg = c, a
            cost[i][b], back[i][b] = best, arg
    idx, b = [], m - 1
    for i in range(n, 0, -1):
        idx.append(b)
        b = back[i][b]
    idx.reverse()  # điểm cắt kết thúc của từng Frame
    mids = [(a + b) / 2 for a, b in cuts]
    edges = [0.0] + [mids[k] for k in idx[:-1]] + [dur]
    for f, a, b in zip(frames, edges[:-1], edges[1:]):
        f["start"], f["end"] = round(a, 3), round(b, 3)
        f["words"] = word_times(f["es"], a, b, sil)
    return frames


def word_times(text, a, b, sil):
    # Các đoạn có tiếng trong [a, b]
    segs, t = [], a
    for s0, s1 in sil:
        if s1 <= a or s0 >= b:
            continue
        if s0 > t:
            segs.append((t, s0))
        t = max(t, s1)
    if t < b:
        segs.append((t, b))
    segs = [s for s in segs if s[1] - s[0] > 0.05] or [(a, b)]
    toks = text.split()
    ws = [max(1, len(re.sub(r"[^\wáéíóúñü]", "", x, flags=re.I))) for x in toks]
    total_w, total_t = sum(ws), sum(s1 - s0 for s0, s1 in segs)

    def to_time(frac):
        target = frac * total_t
        for s0, s1 in segs:
            if target <= s1 - s0:
                return s0 + target
            target -= s1 - s0
        return segs[-1][1]

    out, acc = [], 0
    for tok, x in zip(toks, ws):
        st = to_time(acc / total_w)
        acc += x
        en = to_time(acc / total_w)
        out.append({"word": tok, "start": round(st, 3), "end": round(en, 3)})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", required=True)
    ap.add_argument("--audio", required=True)
    args = ap.parse_args()
    tv = os.path.join(args.project, "transcript_and_visuals.txt")
    audio = os.path.join(args.project, args.audio)
    frames = parse_frames(tv)
    sil, dur = detect_silences(audio)
    frames = align(frames, sil, dur)
    out = os.path.join(args.project, "subtitles", "timeline.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(frames, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"✅ {len(frames)} frames · audio {dur:.1f}s · {len(sil)} khoảng lặng → {out}")
    for f in frames:
        print(f"{f['id']}  {f['start']:7.2f}–{f['end']:7.2f}  ({f['end'] - f['start']:4.1f}s)  {f['es'][:60]}")


if __name__ == "__main__":
    main()

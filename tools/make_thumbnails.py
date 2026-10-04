#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_thumbnails.py — Thumbnail 1280x720 cho project 28 theo 2 bố cục trong youtube_metadata.txt:
  Mẫu B: triptych 3 khung (mỗi khung một hành vi, tông nền khác nhau)
  Mẫu C: lưới 6 khung (2 hàng x 3 cột)
Headline chung "7 SEÑALES OCULTAS" (OCULTAS màu nhấn), font Anton, scrim tối, huy hiệu đỉnh núi góc trái.
Nhân vật vẽ theo phong cách người que của kênh (không dùng ảnh AI).

Cách dùng:
  python3 tools/make_thumbnails.py --project "05_Autoconocimiento/project_28_7_senales_autosabotaje"
"""
import argparse
import io
import os
import sys

import cairosvg
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sticklib import ACC, BG, INK, acc, desk, dim, figure, glow, ico, icon, place, svg_doc  # noqa: E402

TW, TH = 1280, 720
FONT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "fonts", "Anton-Regular.ttf")


def panel_bg(x, y, w, h, tint, op=0.22):
    gid = f"pg{int(x)}{int(y)}"
    return (f'<defs><radialGradient id="{gid}" cx=".5" cy=".38" r=".8"><stop offset="0" stop-color="{tint}" stop-opacity="{op}"/>'
            f'<stop offset="1" stop-color="{tint}" stop-opacity="0"/></radialGradient></defs>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#0B0B0C"/><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#{gid})"/>')


def badge():
    return (f'<circle cx="64" cy="64" r="40" fill="#151517" stroke="{INK}" stroke-width="3" opacity=".95"/>'
            f'<path d="M38,82 L58,48 L68,62 L76,52 L92,82 Z" fill="{INK}"/>'
            f'<path d="M52,58 L58,48 L64,57 L60,55 Z" fill="#151517"/>')


def render(svg_body):
    png = cairosvg.svg2png(bytestring=svg_doc(svg_body, TW, TH, vignette=False).encode())
    return Image.open(io.BytesIO(png)).convert("RGB")


def headline(img, lines=(("7 SEÑALES", INK), ("OCULTAS", ACC)), size=104, gap=4, bottom=34):
    """Hai dòng chữ, tổng chiều cao khối ≈ 31-33% ảnh, căn đáy, trên scrim gradient tối."""
    W, Hh = img.size
    font = ImageFont.truetype(FONT, size)
    probe = ImageDraw.Draw(img)
    hs = [probe.textbbox((0, 0), t, font=font) for t, _ in lines]
    block_h = sum(bb[3] - bb[1] for bb in hs) + (gap + 14) * (len(lines) - 1)
    top = Hh - bottom - block_h
    scrim = Image.new("RGBA", img.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(scrim)
    for i in range(Hh - top + 60):
        a = int(min(1, i / 120) * 215)
        sd.line([(0, top - 60 + i), (W, top - 60 + i)], fill=(5, 5, 6, a))
    img = Image.alpha_composite(img.convert("RGBA"), scrim)
    d = ImageDraw.Draw(img)
    y = top
    for text, col in lines:
        bb = d.textbbox((0, 0), text, font=font)
        w, h = bb[2] - bb[0], bb[3] - bb[1]
        x = (W - w) // 2 - bb[0]
        d.text((x, y - bb[1]), text, font=font, fill=col, stroke_width=4, stroke_fill="#000000")
        y += h + gap + 14
    return img.convert("RGB"), block_h / Hh


def thumb_b():
    pw = TW / 3
    b = []
    tints = ("#3B6CFF", "#FFB46B", ACC)
    for i, t in enumerate(tints):
        b.append(panel_bg(i * pw, 0, pw, TH, t, .26 if i < 2 else .3))
    # 1: đứng trước laptop dự án quan trọng nhưng chần chừ, tay lơ lửng
    b += [desk(250, 395, 300), ico("laptop", 300, 345, 120), glow(300, 330, 90, "W", 1)]
    b += [figure(140, 520, .95, "reach", "uneasy", look=6)[0]]
    # 2: gạt đi lời khen, nhìn sang chỗ khác
    b += [ico("star", 640 + 120, 150, 70, INK, .6), ico("bubble", 640 + 110, 160, 150, INK, .55)]
    b += [figure(640 - 30, 540, 1.0, "dismiss", "avoid", look=-7)[0]]
    # 3: cạnh bức ghép gần xong, còn đúng 1 mảnh (màu nhấn)
    b += [place(1080, 300, 200, icon("puzzle", INK, 6, gap=ACC)), glow(1140, 240, 70, "A", 1)]
    b += [figure(940, 540, 1.0, "stand", "avoid", look=-6)[0]]
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 3}" y="0" width="6" height="{TH}" fill="#000"/>')
    b.append(badge())
    img = render("".join(b))
    return headline(img)


def thumb_c():
    pw, ph = TW / 3, TH / 2
    b = []
    tints = ("#3B6CFF", "#FF6B6B", "#FFB46B", "#5AC8C8", ACC, "#FFD9A0")
    for i, t in enumerate(tints):
        b.append(panel_bg((i % 3) * pw, (i // 3) * ph, pw, ph, t, .24))
    s = .68
    # 1 procrastina lo importante
    b += [ico("laptop", 300, 250, 85), figure(130, 330, s, "sit_away", "distracted", look=-6)[0]]
    # 2 busca razones para fallar
    b += [ico("door", 760, 200, 170, INK, .55, w=6), figure(560, 330, s, "head_shake", "defensive", look=6)[0]]
    # 3 minimiza logros
    b += [ico("bubble", 1150, 110, 80, INK, .55), figure(1010, 330, s, "dismiss", "avoid", look=-6)[0]]
    # 4 rodeado de lo que confirma dudas
    for x in (60, 360):
        b += [figure(x, 690, .5, "stand", op=.28, ghost=True)[0]]
    b += [figure(213, 690, s, "stand", "sad")[0]]
    # 5 todo al 90% — puzzle sin una pieza, sin personaje
    b += [place(640, 540, 200, icon("puzzle", INK, 6, gap=ACC)), glow(700, 480, 70, "A", 1)]
    # 6 cierre: brazos cruzados, espejo detrás
    b += [glow(1066, 520, 150, "warm", 1), ico("mirror", 1130, 500, 200, INK, .35), figure(1040, 690, s, "cross", "determined")[0]]
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 1.5}" y="0" width="3" height="{TH}" fill="{BG}"/>')
    b.append(f'<rect x="0" y="{ph - 1.5}" width="{TW}" height="3" fill="{BG}"/>')
    b.append(badge())
    img = render("".join(b))
    return headline(img)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", required=True)
    args = ap.parse_args()
    out = os.path.join(args.project, "thumbnail")
    os.makedirs(out, exist_ok=True)
    for name, fn in (("thumbnail_B_triptych.png", thumb_b), ("thumbnail_C_grid.png", thumb_c)):
        img, ratio = fn()
        img.save(os.path.join(out, name))
        img.resize((160, 90), Image.LANCZOS).save(os.path.join(out, name.replace(".png", "_160x90.png")))
        print(f"✅ {name}  (khối chữ ≈ {ratio * 100:.0f}% chiều cao ảnh)")


if __name__ == "__main__":
    main()

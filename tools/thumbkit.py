# -*- coding: utf-8 -*-
"""
thumbkit.py — Khối dựng thumbnail 1280x720 dùng chung: nền từng khung, huy hiệu đỉnh núi,
render SVG→PIL và headline 2 dòng (font Anton, từ nhấn màu playlist, khối chữ ≈ 29–34% chiều cao).
"""
import io
import os

import cairosvg
from PIL import Image, ImageDraw, ImageFont

import sticklib as sl

TW, TH = 1280, 720
FONT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "fonts", "Anton-Regular.ttf")


def panel_bg(x, y, w, h, tint, op=0.22):
    gid = f"pg{int(x)}{int(y)}"
    return (f'<defs><radialGradient id="{gid}" cx=".5" cy=".38" r=".8"><stop offset="0" stop-color="{tint}" stop-opacity="{op}"/>'
            f'<stop offset="1" stop-color="{tint}" stop-opacity="0"/></radialGradient></defs>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#0B0B0C"/><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#{gid})"/>')


def badge():
    return (f'<circle cx="64" cy="64" r="40" fill="#151517" stroke="{sl.INK}" stroke-width="3" opacity=".95"/>'
            f'<path d="M38,82 L58,48 L68,62 L76,52 L92,82 Z" fill="{sl.INK}"/>'
            f'<path d="M52,58 L58,48 L64,57 L60,55 Z" fill="#151517"/>')


def render(svg_body):
    png = cairosvg.svg2png(bytestring=sl.svg_doc(svg_body, TW, TH, vignette=False).encode())
    return Image.open(io.BytesIO(png)).convert("RGB")


def split_lines(words, font, draw):
    """Chia headline thành 2 dòng sao cho dòng dài nhất ngắn nhất."""
    best = None
    for k in range(1, len(words)):
        ws = [draw.textlength(" ".join(words[:k]), font=font), draw.textlength(" ".join(words[k:]), font=font)]
        if best is None or max(ws) < best[0]:
            best = (max(ws), [words[:k], words[k:]])
    return best[1] if best else [words]


def headline(img, text, accent_word, size=116, gap=18, bottom=34, max_w=1180):
    W, Hh = img.size
    probe = ImageDraw.Draw(img)
    words = text.split()
    font = ImageFont.truetype(FONT, size)
    lines = split_lines(words, font, probe)
    while max(probe.textlength(" ".join(l), font=font) for l in lines) > max_w and size > 60:
        size -= 4
        font = ImageFont.truetype(FONT, size)
        lines = split_lines(words, font, probe)
    asc, desc = font.getbbox("ÑA")[1], font.getbbox("A")[3]
    line_h = desc - font.getbbox("A")[1]
    block_h = line_h * len(lines) + gap * (len(lines) - 1)
    top = Hh - bottom - block_h
    scrim = Image.new("RGBA", img.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(scrim)
    for i in range(Hh - top + 60):
        sd.line([(0, top - 60 + i), (W, top - 60 + i)], fill=(5, 5, 6, int(min(1, i / 120) * 215)))
    img = Image.alpha_composite(img.convert("RGBA"), scrim)
    d = ImageDraw.Draw(img)
    space = d.textlength(" ", font=font)
    y = top
    for ln in lines:
        total = sum(d.textlength(w, font=font) for w in ln) + space * (len(ln) - 1)
        x = (W - total) / 2
        for w in ln:
            col = sl.ACC if w.upper() == accent_word.upper() else sl.INK
            d.text((x, y - font.getbbox("A")[1]), w, font=font, fill=col, stroke_width=4, stroke_fill="#000000")
            x += d.textlength(w, font=font) + space
        y += line_h + gap
    return img.convert("RGB"), block_h / Hh

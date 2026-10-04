# -*- coding: utf-8 -*-
"""
scenekit.py — Các khối dựng cảnh dùng chung cho mọi project (cân, vòng người mờ, tảng đá...).
File scenes.py của từng project chỉ cần:  from scenekit import *  rồi định nghĩa build_layers(n, shot).
"""
import math

import sticklib as sl
from sticklib import *  # noqa: F401,F403
from sticklib import INK, figure, glow, ico, icon, place

FLOOR = 905


def scale_with(cx, cy, size, tilt, left=None, right=None, color=INK, op=1.0, glow_it=False):
    """Cân thăng bằng + vật trên hai đĩa. left/right = (tên icon, màu, cỡ, op)."""
    out = []
    if glow_it:
        out.append(glow(cx, cy, size * 1.1, "A", 0.6))
    out.append(place(cx, cy, size, icon("scale", color, 7, tilt=tilt), op))
    k = size / 100
    a = math.radians(tilt)
    for side, item in ((-1, left), (1, right)):
        if not item:
            continue
        px = cx + side * 60 * math.cos(a) * k
        py = cy + (-40 + side * 60 * math.sin(a)) * k + 16 * k
        for j, (name, col, sz, o) in enumerate(item if isinstance(item, list) else [item]):
            off = (j - (len(item) - 1) / 2) * sz * 0.8 if isinstance(item, list) else 0
            if col == sl.ACC:
                out.append(glow(px + off, py - sz * 0.45, sz * 1.2, "A", o))
            out.append(place(px + off, py - sz * 0.45, sz, icon(name, col, 7), o))
    return "".join(out)


def ghost_ring(cx, cy, rx, ry, n=6, s=0.62, op=0.22, skip_front=True, bubbles=False):
    out = []
    for i in range(n):
        a = math.radians(90 + 360 * i / n + 30)
        x, y = cx + rx * math.cos(a), cy + ry * math.sin(a)
        if skip_front and abs(x - cx) < 60 and y > cy:
            continue
        out.append(figure(x, y, s, "explain_l" if x > cx else "explain", op=op, ghost=True)[0])
        if bubbles:
            out.append(ico("thought", x + (40 if x < cx else -40), y - 330 * s, 60, INK, op + 0.05, inner=True))
    return "".join(out)


def boulder_on(anch, size, op=1.0, dx=0):
    """Tảng đá đè lên vai/đầu (vẽ TRƯỚC nhân vật để tay đỡ nằm trên)."""
    tx, ty = anch["top"]
    bottom = min(ty - 6, anch["lhand"][1] + 6, anch["rhand"][1] + 6)
    return ico("boulder", tx + dx, bottom - size * 0.30, size, INK, op)


def mirror(svg, x):
    """Lật ngang một khối SVG quanh trục dọc x (vd: người ngồi đối diện)."""
    return f'<g transform="translate({2 * x:.1f},0) scale(-1,1)">{svg}</g>'


def dots_row(x0, x1, y, n=5, size=14, lit=None, op=1.0):
    out = []
    for i in range(n):
        x = x0 + (x1 - x0) * i / (n - 1)
        on = lit is None or i < lit
        o = op if on else op * 0.35
        out.append(f'<g data-dot="{i}">' + glow(x, y, size * 3.2, "A", o)
                   + f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{size}" fill="{sl.ACC}" opacity="{o}"/></g>')
    return "".join(out)


def nodes(cx, cy, r, n=9, seed=5, color=None, w=4, op=1.0):
    """Mạng kết nối nhỏ (nơ-ron mới) phủ lên icon não."""
    import random
    rnd = random.Random(seed)
    color = color or sl.ACC
    pts = [(cx + rnd.uniform(-r, r), cy + rnd.uniform(-r * .7, r * .7)) for _ in range(n)]
    out = []
    for i, p in enumerate(pts):
        q = pts[(i * 3 + 1) % n]
        out.append(f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="{color}" stroke-width="{w}" stroke-linecap="round" opacity="{op * .8}"/>')
    for p in pts:
        out.append(f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{w * 1.6}" fill="{color}" opacity="{op}"/>')
    return "".join(out)


def table(x, y, wdt=380, op=1.0):
    return (f'<g opacity="{op}"><line x1="{x - wdt / 2}" y1="{y}" x2="{x + wdt / 2}" y2="{y}" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>'
            f'<line x1="{x}" y1="{y}" x2="{x}" y2="{FLOOR}" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>'
            f'<line x1="{x - 60}" y1="{FLOOR}" x2="{x + 60}" y2="{FLOOR}" stroke="{INK}" stroke-width="7" stroke-linecap="round"/></g>')


def bed(x0, x1, y, op=1.0):
    return (f'<g opacity="{op}"><rect x="{x0}" y="{y}" width="{x1 - x0}" height="46" rx="10" fill="none" stroke="{INK}" stroke-width="8"/>'
            f'<line x1="{x0}" y1="{y - 60}" x2="{x0}" y2="{FLOOR}" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>'
            f'<line x1="{x1}" y1="{y + 20}" x2="{x1}" y2="{FLOOR}" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>'
            f'<rect x="{x1 - 150}" y="{y - 34}" width="120" height="36" rx="16" fill="none" stroke="{INK}" stroke-width="7"/></g>')


def timeline(x0, y0, x1, y1, ticks=2, color=None, w=6, op=1.0):
    color = color or sl.ACC
    out = [f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" stroke="{color}" stroke-width="{w}" stroke-linecap="round" opacity="{op}"/>']
    for i in range(1, ticks + 1):
        t = i / (ticks + 1)
        x, y = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
        out.append(f'<line x1="{x:.1f}" y1="{y - 22:.1f}" x2="{x:.1f}" y2="{y + 22:.1f}" stroke="{color}" stroke-width="{w}" stroke-linecap="round" opacity="{op}"/>')
    if color == sl.ACC:
        out.insert(0, glow((x0 + x1) / 2, (y0 + y1) / 2, abs(x1 - x0) * .45, "A", op * .5))
    return "".join(out)


# ------------------------------------------------------------------ domino
def domino_tile(x, y, h, color=None, op=1.0, label=None, glow_it=False):
    """Quân domino đứng, đáy giữa tại (x, y). label = tên icon nhỏ vẽ trên mặt quân."""
    color = color or INK
    w = h * 0.46
    out = []
    if glow_it:
        out.append(glow(x, y - h / 2, h * 0.9, "A", op))
    out.append(f'<rect x="{x - w / 2:.1f}" y="{y - h:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{w * .14:.1f}" '
               f'fill="{sl.BG}" stroke="{color}" stroke-width="{max(4, h * .045):.1f}" opacity="{op}"/>')
    out.append(f'<line x1="{x - w * .32:.1f}" y1="{y - h / 2:.1f}" x2="{x + w * .32:.1f}" y2="{y - h / 2:.1f}" '
               f'stroke="{color}" stroke-width="{max(3, h * .03):.1f}" stroke-linecap="round" opacity="{op}"/>')
    if label:
        out.append(place(x, y - h * .75, w * .62, icon(label, color, 7), op))
        out.append(f'<circle cx="{x:.1f}" cy="{y - h * .25:.1f}" r="{h * .045:.1f}" fill="{color}" opacity="{op}"/>')
    else:
        for dy in (.75, .25):
            out.append(f'<circle cx="{x:.1f}" cy="{y - h * dy:.1f}" r="{h * .05:.1f}" fill="{color}" opacity="{op}"/>')
    return "".join(out)


def domino_row(x0, x1, y, n=10, h=180, fall=None, first_acc=True, labels=None, op=1.0, fade=0.0,
               shrink=0.0, start=0.35, step=0.16):
    """Hàng domino. fall: None (đứng) | "anim" (đổ dây chuyền trong video; ảnh tĩnh = đã đổ) | "done" (đã đổ).
    fade: độ mờ dần về cuối hàng; shrink: thu nhỏ dần (phối cảnh xa)."""
    out = []
    xs = [x0 + (x1 - x0) * i / max(n - 1, 1) for i in range(n)]
    for i, x in enumerate(xs):
        k = i / max(n - 1, 1)
        hi = h * (1 - shrink * k)
        yi = y - (h - hi) * .9 * (1 if shrink else 0)
        oi = op * (1 - fade * k)
        acc_tile = first_acc and i == 0
        col = sl.ACC if acc_tile else INK
        lab = labels[i] if labels and i < len(labels) else None
        tile = domino_tile(x, yi, hi, col, oi, lab, glow_it=acc_tile)
        if fall:
            gap = (xs[i + 1] - x) if i + 1 < n else hi
            w = hi * .46
            ang = 82 if i == n - 1 else min(80, math.degrees(math.asin(max(0.05, min(1, (gap - w * .5) / hi)))) + 4)
            mode = "done" if fall == "done" else f"{start + i * step:.2f}"
            tile = f'<g data-fall="{ang:.1f},{x + w / 2:.1f},{yi:.1f},{mode}">{tile}</g>'
        out.append(tile)
    return "".join(out)


def jumble(cx, cy, n=20, h=90, seed=7, op=.7):
    """Cụm domino lộn xộn (nhiều thói quen cùng lúc, không quân nào đổ gọn)."""
    import random
    rnd = random.Random(seed)
    out = []
    for i in range(n):
        x, yy = cx + rnd.uniform(-330, 330), cy + rnd.uniform(-60, 120)
        out.append(f'<g transform="rotate({rnd.uniform(-35, 35):.1f} {x:.1f} {yy:.1f})">'
                   + domino_tile(x, yy, h * rnd.uniform(.7, 1.15), INK, op * rnd.uniform(.5, 1)) + "</g>")
    return "".join(out)


def marker(num, x, y, size=170, color=None):
    """Số đánh dấu module ("1".."4") — vòng tròn + chữ số Anton."""
    color = color or INK
    return (f'<circle cx="{x}" cy="{y}" r="{size * .62:.0f}" fill="none" stroke="{color}" stroke-width="7" opacity=".9"/>'
            f'<text x="{x}" y="{y + size * .36:.0f}" font-family="Anton" font-size="{size:.0f}" fill="{color}" '
            f'text-anchor="middle">{num}</text>')


def finalize_static(svg):
    """Ảnh tĩnh/thumbnail: domino "anim" hiển thị ở trạng thái đã đổ."""
    import re

    def sub(m):
        ang, px, py, _ = m.group(1).split(",")
        return f'transform="rotate({ang} {px} {py})"'
    return re.sub(r'data-fall="([^"]+)"', sub, svg)

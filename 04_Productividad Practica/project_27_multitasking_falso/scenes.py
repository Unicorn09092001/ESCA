# -*- coding: utf-8 -*-
"""
scenes.py — Kịch bản hình của project 27 "Por Qué el Multitasking Te Hace Más Lento (Ciencia)"
(43 khung + 2 thumbnail), bám theo [VISUAL DESCRIPTION] trong transcript_and_visuals.txt.
Màu nhấn #3BA7C9 (04_Productividad Practica).
Mô-típ: các icon việc vây quanh · công tắc bật/tắt liên tục (task switching) để lại "vết cặn" nhỏ chồng
thành đống · cột năng suất 60% vs 100% · đồng hồ "hoạt động" đầy vs "tiến độ thật" thấp · gom việc thành khối.
"""
import random

from scenekit import *  # noqa: F401,F403
from sticklib import *  # noqa: F401,F403  (nạp lại ACC sau khi đã set_accent theo playlist)
from scenekit import FLOOR, desk, marker, timeline
from thumbkit import TH, TW, badge, panel_bg

TASKS = ("bubble", "document", "phone", "envelope", "call", "browser")


def ring_tasks(cx, cy, r, names=TASKS, size=90, op=.7, seq=True, half=False):
    out = []
    for i, nm in enumerate(names):
        a = math.radians(-90 + 360 * i / len(names))
        x, y = cx + r * math.cos(a), cy + r * .8 * math.sin(a)
        g = ico(nm, x, y, size, INK, op)
        if half:
            g += (f'<path d="M{x - size * .55:.0f},{y + size * .55:.0f} A{size * .62:.0f},{size * .62:.0f} 0 0 1 {x + size * .55:.0f},{y + size * .55:.0f}" '
                  f'fill="none" stroke="{INK}" stroke-width="4" opacity=".35" stroke-dasharray="6 8"/>')
        out.append(f'<g data-dot="{i}">{g}</g>' if seq else g)
    return "".join(out)


def residue(cx, cy, n=24, spread=110, seed=7, op=.9, pile=True):
    """Các vết cặn nhỏ sau mỗi lần chuyển việc — chồng thành đống."""
    rr = random.Random(seed)
    out = []
    for i in range(n):
        if pile:
            row = int((math.sqrt(8 * i + 1) - 1) / 2)
            k = i - row * (row + 1) // 2
            x = cx + (k - row / 2) * 26 + rr.uniform(-4, 4)
            y = cy - (8 - row) * 4 + row * 22 - 60
        else:
            x, y = cx + rr.uniform(-spread, spread), cy + rr.uniform(-spread * .4, spread * .4)
        out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rr.uniform(5, 8):.1f}" fill="{ACC}" opacity="{op * rr.uniform(.5, 1):.2f}"/>')
    return f'<g data-acc="{cx},{cy}">' + glow(cx, cy, spread * 1.2, "A", .45) + "".join(out) + "</g>"


def jump_arrow(x0, x1, y, h=120, op=1.0):
    xm = (x0 + x1) / 2
    return (f'<g data-acc="{xm:.0f},{y - h:.0f}">' + glow(xm, y - h * .6, 140, "A", .6)
            + f'<path d="M{x0},{y} Q{xm},{y - h * 2} {x1},{y}" stroke="{ACC}" stroke-width="6" fill="none" opacity="{op}"/>'
            + f'<path d="M{x1},{y} Q{xm},{y + h * 1.4} {x0},{y}" stroke="{ACC}" stroke-width="4" fill="none" opacity="{op * .6:.2f}" stroke-dasharray="10 10"/>'
            + f'<path d="M{x1 - 26},{y - 20} L{x1},{y} L{x1 - 30},{y + 6}" fill="none" stroke="{ACC}" stroke-width="6" stroke-linejoin="round"/></g>')


def bar(x, y_base, h_full, frac, w=150, lit=False, label=None):
    col = ACC if lit else INK
    out = (f'<rect x="{x - w / 2}" y="{y_base - h_full}" width="{w}" height="{h_full}" rx="10" fill="none" stroke="{INK}" stroke-width="3" opacity=".25" stroke-dasharray="10 8"/>'
           f'<rect x="{x - w / 2}" y="{y_base - h_full * frac:.0f}" width="{w}" height="{h_full * frac:.0f}" rx="10" fill="{col}" fill-opacity="{.35 if lit else .18}" stroke="{col}" stroke-width="5"/>')
    if label:
        out += f'<text x="{x}" y="{y_base + 70}" font-family="Anton" font-size="56" fill="{col}" text-anchor="middle">{label}</text>'
    return (f'<g data-acc="{x},{y_base - h_full * frac / 2:.0f}">' + glow(x, y_base - h_full * frac / 2, w * 1.3, "A", .5) + out + "</g>") if lit else out


def gauge_l(x, y, v, lit, size=220):
    g = ico("gauge", x, y, size, ACC if lit else INK, 1 if lit else .55, value=v)
    return (f'<g data-acc="{x},{y}">' + glow(x, y, size * .9, "A", .7) + g + "</g>") if lit else g


def struck(x, y, size, op=.55):
    return line(x - size * .55, y + size * .45, x + size * .55, y - size * .45, INK, 6, op)


def build_layers(n, shot):
    F = lambda **kw: shot_fig(shot, **kw)  # noqa: E731
    b = []
    # ---------------------------------------------------------------- GANCHO
    if n == 1:
        b += [floor_line(), ring_tasks(960, 470, 420, ("bubble", "document", "phone", "browser", "envelope"), 100, .75),
              chair(950, FLOOR, 1.12), figure(960, FLOOR, 1.12, "sit", "proud", look=0)[0]]
    elif n == 2:
        fig, an = F(x=960, pose="stand", expr="distracted", look=-4)
        b += [fig, ico("bubble", 520, 420, 140, INK, .8), ico("document", 1400, 420, 140, INK, .8), jump_arrow(620, 1300, 330, 90)]
    elif n == 3:
        fig, an = F(x=960, pose="stand", expr="strain")
        hx, hy = an["head"]
        b += [fig] + [f'<g data-acc="{hx + dx},{hy + dy}">' + glow(hx + dx, hy + dy, 110, "A", .5) + ico("browser", hx + dx, hy + dy, 140, INK, .9) + "</g>"
                      for dx, dy in ((-420, 0), (420, 0), (0, -260))]
    elif n == 4:
        b += [floor_line(), ring_tasks(960, 450, 430, TASKS, 90, .6, seq=False), F(x=960, pose="hands_hips", expr="proud")[0]]
    elif n == 5:
        b += [ring_tasks(960, 500, 460, TASKS, 80, .35, seq=False), acc("brain", 960, 500, 300),
              crack(860, 420, 1060, 590, seed=5, color=INK, w=4)]
    # ---------------------------------------------------------------- PROMESA
    elif n == 6:
        b += [acc("brain", 1320, 440, 220), F(x=680, pose="explain", expr="calm", look=6)[0]]
    elif n == 7:
        b += [ico("hourglass", 960, 470, 300, INK, .8), particles(960, 700, 60, 120, 12, seed=7, op=.8)]
    elif n == 8:
        b += [crowd([1300, 1460, 1620], FLOOR, .6, .15, poses=["stride"]), F(x=700, pose="reassure", expr="calm", look=6)[0]]
    # ---------------------------------------------------------------- 1 — El mito (Earl Miller)
    elif n == 9:
        b += [floor_line(), marker(1, 1340, 380, 190), F(x=700, pose="stand", expr="attentive", look=6)[0]]
    elif n == 10:
        b += [ico("campus", 1360, 430, 220, INK, .5), F(x=700, pose="explain", expr="thoughtful", look=6)[0]]
    elif n == 11:
        b += [ico("brain", 960, 520, 340, INK, .9), acc("bubble", 640, 260, 110), acc("document", 1280, 260, 110),
              line(700, 320, 840, 400, INK, 4, .4, "8 8"), line(1220, 320, 1080, 400, INK, 4, .4, "8 8")]
    elif n == 12:
        b += [line(640, 440, 1260, 440, INK, 6, .5), line(640, 560, 1260, 560, INK, 6, .5),
              f'<path d="M1230,410 L1270,440 L1230,470 M1230,530 L1270,560 L1230,590" fill="none" stroke="{INK}" stroke-width="6" opacity=".5"/>',
              struck(960, 500, 520, .7)]
    elif n == 13:
        b += [ico("bubble", 560, 520, 170, INK), ico("document", 1360, 520, 170, INK), jump_arrow(680, 1240, 440, 110)]
    elif n == 14:
        b += [acc("toggle", 820, 500, 260, on=True), ico("toggle", 1180, 500, 260, INK, .35, on=False)]
    elif n == 15:
        b += [acc("toggle", 660, 460, 220, on=True), residue(1260, 620, 21, 140, seed=15)]
    # ---------------------------------------------------------------- 2 — El costo real (David Meyer)
    elif n == 16:
        b += [floor_line(), marker(2, 1240, 360, 180), residue(1560, 780, 28, 140, seed=16), F(x=640, pose="stand", expr="attentive", look=6)[0]]
    elif n == 17:
        b += [acc("document", 1360, 480, 200), F(x=700, pose="explain", expr="thoughtful", look=6)[0]]
    elif n == 18:
        b += [ico("toggle", 640, 500, 200, INK, .8, on=True)]
        b += [gauge_l(1260, 520, .62, True, 300)]
    elif n == 19:
        b += [floor_line(op=.3), bar(960, 820, 520, .6, 200, lit=True, label="60%")]
    elif n == 20:
        b += [bar(760, 820, 520, .6, 180, lit=False, label="60%"), bar(1160, 820, 520, 1.0, 180, lit=True, label="100%")]
    elif n == 21:
        fig, an = F(x=620, pose="dismiss", expr="calm", look=6)
        b += [fig, bar(1340, 860, 520, .6, 180),
              f'<g data-acc="1340,452">' + glow(1340, 452, 170, "A", .6) + f'<rect x="1250" y="340" width="180" height="208" rx="10" fill="none" stroke="{ACC}" stroke-width="6" stroke-dasharray="14 10"/>'
              + f'<text x="1340" y="470" font-family="Anton" font-size="60" fill="{ACC}" text-anchor="middle">40%</text></g>']
    elif n == 22:
        b += [timeline(200, 760, 1720, 760, ticks=8, color=INK, w=4, op=.5), residue(960, 640, 60, 720, seed=22, op=.7, pile=False),
              ico("sun", 260, 600, 70, INK, .4), ico("moon", 1660, 600, 70, INK, .4)]
    # ---------------------------------------------------------------- 3 — Por qué se siente productivo
    elif n == 23:
        b += [floor_line(), marker(3, 1240, 360, 180), F(x=640, pose="stand", expr="satisfied", look=6)[0]]
        b += [ico("check", x, y, 70, INK, .6) for x, y in ((1480, 560), (1600, 660), (1460, 760), (1640, 500))]
    elif n == 24:
        b += [ico("toggle", 760, 500, 220, INK, .9, on=True), acc("spark", 1120, 400, 140), particles(1120, 400, 120, 80, 10, seed=24, op=.6)]
    elif n == 25:
        b += [f'<g data-dot="{i}">' + acc("check", 520 + i * 290, 500, 130) + "</g>" for i in range(4)]
    elif n == 26:
        b += [gauge_l(680, 520, .95, True, 320), gauge_l(1260, 520, .2, False, 320),
              ico("bolt", 680, 760, 60, INK, .5), ico("arrow_up", 1260, 760, 60, INK, .5)]
    elif n == 27:
        b += [gauge_l(560, 560, .95, True, 220), gauge_l(1360, 560, .2, False, 220), ico("brain", 960, 340, 220, INK, .9),
              ico("question", 960, 600, 90, INK, .5), line(860, 420, 680, 470, INK, 3, .3, "6 8"), line(1060, 420, 1240, 470, INK, 3, .3, "6 8")]
    elif n == 28:
        b += [floor_line(), ico("moon", 1650, 200, 80, INK, .5), chair(950, FLOOR, 1.12), figure(960, FLOOR, 1.12, "sit", "resigned", look=0)[0],
              ring_tasks(960, 480, 440, TASKS, 80, .55, seq=False, half=True)]
    elif n == 29:
        b += [timeline(200, 820, 1720, 820, ticks=6, color=INK, w=4, op=.4)]
        b += [ico(nm, 360 + i * 260, 520 + (i % 2) * 60, 100, INK, .5) for i, nm in enumerate(TASKS)]
        b += [f'<path d="M{306 + i * 260},{580 + (i % 2) * 60} A62,62 0 0 1 {414 + i * 260},{580 + (i % 2) * 60}" fill="none" stroke="{ACC}" stroke-width="4" opacity=".5" stroke-dasharray="6 8"/>' for i in range(6)]
    # ---------------------------------------------------------------- 4 — Qué hacer en su lugar
    elif n == 30:
        b += [floor_line(), marker(4, 1240, 360, 180), F(x=640, pose="stand", expr="determined", look=6)[0]]
        b += [ico(nm, 1460 + (i % 3) * 110, 620 + (i // 3) * 120, 70, INK, .45) for i, nm in enumerate(TASKS)]
    elif n == 31:
        b += [ico("door", 1300, 480, 220, INK, .3), ico("xmark", 1300, 480, 160, INK, .5), F(x=700, pose="reassure", expr="calm", look=6)[0]]
    elif n == 32:
        for j, nm in enumerate(("bubble", "document", "call")):
            cx = 560 + j * 400
            b += [f'<g data-dot="{j}">' + f'<rect x="{cx - 150}" y="340" width="300" height="320" rx="24" fill="none" stroke="{ACC if j == 0 else INK}" stroke-width="5" opacity="{1 if j == 0 else .5}"/>'
                  + "".join(ico(nm, cx - 60 + (k % 2) * 120, 430 + (k // 2) * 140, 90, INK, .85) for k in range(4)) + "</g>"]
    elif n == 33:
        b += [timeline(200, 760, 1720, 760, ticks=0, color=INK, w=4, op=.4)]
        for j, nm in enumerate(("envelope", "call", "document")):
            x0 = 280 + j * 500
            blk = (f'<rect x="{x0}" y="560" width="400" height="160" rx="18" fill="{ACC if j == 2 else INK}" fill-opacity="{.2 if j == 2 else .06}" '
                   f'stroke="{ACC if j == 2 else INK}" stroke-width="5" opacity="{1 if j == 2 else .7}"/>'
                   + "".join(ico(nm, x0 + 80 + k * 120, 640, 80, INK, .9) for k in range(3)))
            b += [f'<g data-dot="{j}">{blk}</g>']
    elif n == 34:
        b += [acc("toggle", 960, 500, 260, on=True), f'<path d="M760,700 Q960,760 1160,700" stroke="{INK}" stroke-width="4" fill="none" opacity=".35"/>',
              ico("clock", 960, 260, 90, INK, .4)]
    elif n == 35:
        b += [ico("task", 600, 500, 120, INK, .25), acc("task", 960, 500, 240), ico("check", 1080, 360, 80, ACC), ico("task", 1320, 500, 120, INK, .25)]
    elif n == 36:
        fig, an = F(x=760, pose="walk", expr="serene", look=6)
        b += [floor_line(), fig, ico("boulder", 380, 820, 120, INK, .15), particles(380, 820, 120, 80, 10, seed=36, color=INK, op=.25)]
    elif n == 37:
        b += [glow(960, 500, 420, "A", .35), acc("brain", 960, 500, 340)]
    # ---------------------------------------------------------------- CIERRE
    elif n == 38:
        b += [floor_line(), F(x=960, pose="stand", expr="calm")[0], dust(1500, 760, 260, 160, 18, seed=38, op=.15)]
    elif n == 39:
        b += [ico("brain", 960, 480, 320, INK, .95), f'<circle cx="960" cy="480" r="230" fill="none" stroke="{ACC}" stroke-width="5" opacity=".6"/>',
              glow(960, 480, 300, "A", .35)]
    elif n == 40:
        b += [F(x=640, pose="stand", expr="thoughtful", look=6)[0], residue(1340, 700, 36, 160, seed=40)]
    elif n == 41:
        b += [acc("bubble", 1320, 380, 180), ico("browser", 1560, 600, 90, INK, .4), F(x=700, pose="point_you", expr="warm", look=3)[0]]
    elif n == 42:
        b += [acc("bell", 1340, 420, 150), F(x=760, pose="thumbs", expr="smile")[0]]
    elif n == 43:
        b += [rim(960, 500, 620), F(x=960, pose="stand", expr="serene")[0]]
    else:
        raise ValueError(n)
    return b


def thumb_b():
    """Mẫu B — triptych: alternar entre dos tareas · agrupar tareas · una sola tarea (vật nhấn)."""
    pw = TW / 3
    b = [panel_bg(0, 0, pw, TH, "#7FB8FF", .26), panel_bg(pw, 0, pw, TH, "#FFB46B", .24), panel_bg(2 * pw, 0, pw, TH, "#5AC8A0", .24)]
    b += [figure(pw / 2, 560, .9, "shrug", "strain")[0], ico("bubble", 90, 200, 80, INK, .9), ico("document", pw - 90, 200, 80, INK, .9),
          f'<path d="M130,170 Q{pw / 2},60 {pw - 130},170" stroke="{INK}" stroke-width="5" fill="none" stroke-dasharray="10 8"/>']
    fig, an = figure(pw + 120, 560, .9, "explain", "determined", look=6)
    b += [fig, f'<rect x="{pw + 210}" y="160" width="180" height="200" rx="16" fill="none" stroke="{INK}" stroke-width="5"/>']
    b += [ico("envelope", pw + 255 + (k % 2) * 90, 215 + (k // 2) * 90, 60, INK) for k in range(4)]
    x3 = 2 * pw + pw / 2
    b += [line(x3 - 60, 440, x3 + 190, 440, INK, 7), line(x3 + 160, 440, x3 + 160, 560, INK, 6), acc("task", x3 + 100, 370, 100),
          chair(x3 - 150, 560, .9), figure(x3 - 140, 560, .9, "type", "satisfied", look=5)[0]]
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 3}" y="0" width="6" height="{TH}" fill="#000"/>')
    b.append(badge())
    return b


def thumb_c():
    """Mẫu C — lưới 6 khung."""
    pw, ph = TW / 3, TH / 2
    tints = ("#7FB8FF", "#FF6B6B", "#FFB46B", "#5AC8A0", "#8C7BFF", "#FFD9A0")
    b = [panel_bg((i % 3) * pw, (i // 3) * ph, pw, ph, t, .22) for i, t in enumerate(tints)]
    b += [glow(213, 180, 160, "A", .6), ico("brain", 213, 180, 200, ACC), ico("toggle", 213, 180, 60, INK)]          # 1 mito
    b += [figure(640, 320, .58, "shrug", "strain")[0], ico("bubble", 520, 110, 60, INK), ico("document", 760, 110, 60, INK)]  # 2 costo
    b += [chair(1060, 320, .58), figure(1066, 320, .58, "sit", "resigned")[0]]
    b += [ico(nm, 1066 + 150 * math.cos(math.radians(a)), 160 + 110 * math.sin(math.radians(a)), 50, INK, .6)
          for nm, a in zip(TASKS, range(-190, 20, 40))]                                                               # 3 ocupado
    b += [figure(120, 460, .34, "point", "calm", look=6)[0], acc("task", 260, 420, 80)]                                # 4 una tarea
    b += [f'<rect x="{560 + j * 120}" y="380" width="100" height="90" rx="10" fill="none" stroke="{INK}" stroke-width="3" opacity=".7"/>'
          + ico(nm, 610 + j * 120, 425, 50, INK, .8) for j, nm in enumerate(("envelope", "call"))]                   # 5 agrupar
    b += [figure(1040, 520, .45, "hands_hips", "satisfied")[0], ico("check", 1170, 420, 70, INK)]                     # 6 cierre
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 1.5}" y="0" width="3" height="{TH}" fill="{BG}"/>')
    b.append(f'<rect x="0" y="{ph - 1.5}" width="{TW}" height="3" fill="{BG}"/>')
    b.append(badge())
    return b

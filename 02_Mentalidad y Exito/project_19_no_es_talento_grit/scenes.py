# -*- coding: utf-8 -*-
"""
scenes.py — Kịch bản hình của project 19 "No Es Talento, Es GRIT" (61 khung + 2 thumbnail),
bám theo [VISUAL DESCRIPTION] trong transcript_and_visuals.txt. Màu nhấn #E8A23C (02_Mentalidad y Exito).
Mô-típ: con dốc (West Point "la Bestia"), công thức talento × esfuerzo = habilidad × esfuerzo = logro,
spotlight thiên vị "lo natural", lối đi thẳng nhiều năm vs nhánh rẽ, rào chắn "regla de la cosa difícil".
"""
from scenekit import *  # noqa: F401,F403
from sticklib import *  # noqa: F401,F403  (nạp lại ACC sau khi đã set_accent theo playlist)
from scenekit import FLOOR
from thumbkit import TH, TW, badge, panel_bg

SLOPE = (640, FLOOR, 1820, 300)  # chân dốc → đỉnh dốc


def hill(op=1.0, x0=None, y0=None, x1=None, y1=None, color=None):
    a, b_, c, d = SLOPE
    x0, y0, x1, y1 = x0 or a, y0 or b_, x1 or c, y1 or d
    color = color or INK
    return (f'<path d="M{x0 - 400},{y0} L{x0},{y0} L{x1},{y1} L{x1 + 200},{y1}" fill="none" stroke="{color}" '
            f'stroke-width="7" stroke-linecap="round" stroke-linejoin="round" opacity="{op}"/>')


def on_slope(t):
    """Điểm trên dốc theo tỉ lệ t (0 = chân, 1 = đỉnh) và góc nghiêng."""
    x0, y0, x1, y1 = SLOPE
    ang = math.degrees(math.atan2(y1 - y0, x1 - x0))
    return x0 + (x1 - x0) * t, y0 + (y1 - y0) * t, ang


def flame(x, y, size, op=1.0):
    return acc("flame", x, y, size, op=op)


def op_sign(x, y, kind="x", color=None, size=40):
    color = color or INK
    if kind == "x":
        d = f"M{x - size / 2},{y - size / 2} L{x + size / 2},{y + size / 2} M{x + size / 2},{y - size / 2} L{x - size / 2},{y + size / 2}"
    else:
        d = f"M{x - size / 2},{y - size / 4} L{x + size / 2},{y - size / 4} M{x - size / 2},{y + size / 4} L{x + size / 2},{y + size / 4}"
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="7" stroke-linecap="round" opacity=".7"/>'


def chain(items, y=520, x0=260, x1=1660, size=150, seq=True):
    """Chuỗi công thức: items = [(icon, màu, op), "x" | "=" , ...] — xuất hiện lần lượt (data-dot)."""
    n = len(items)
    out = []
    for i, it in enumerate(items):
        x = x0 + (x1 - x0) * i / (n - 1)
        if isinstance(it, str):
            el = op_sign(x, y, "x" if it == "x" else "=")
        else:
            nm, col, o = it
            el = (glow(x, y, size * .9, "A", o) if col == ACC else "") + place(x, y, size, icon(nm, col, 7), o)
        out.append(f'<g data-dot="{i}">{el}</g>' if seq else el)
    return "".join(out)


def spotlight(x, top=60, bottom=FLOOR, w=260, op=.35):
    return (f'<g data-acc="{x},{(top + bottom) / 2:.0f}"><polygon points="{x - 40},{top} {x + 40},{top} {x + w / 2},{bottom} {x - w / 2},{bottom}" '
            f'fill="{ACC}" opacity="{op}"/></g>')


def formation(cx=960, y0=380, rows=5, cols=11, gap_x=120, gap_y=110, s=.42, op=.22, keep=None):
    out = []
    for r in range(rows):
        for c in range(cols):
            x = cx + (c - (cols - 1) / 2) * gap_x
            y = y0 + r * gap_y + 150
            idx = r * cols + c
            if keep is not None:
                if idx in keep:
                    out.append(figure(x, y, s, "stand", "determined", color=ACC)[0])
                else:
                    out.append(figure(x, y, s, "stand", op=.07, ghost=True)[0])
            else:
                out.append(figure(x, y, s, "stand", op=op, ghost=True)[0])
    return "".join(out)


def build_layers(n, shot):
    F = lambda **kw: shot_fig(shot, **kw)  # noqa: E731
    b = []
    # ---------------------------------------------------------------- EL GANCHO
    if n == 1:
        b += [hill(), line(1820, 300, 1880, 220, INK, 4, .25, "10 10"), line(1820, 300, 1890, 360, INK, 4, .25, "10 10")]
        b += [F(x=460, pose="stand", expr="thoughtful", look=6)[0]]
    elif n == 2:
        for i, (nm, x) in enumerate((("star", 600), ("brain", 960), ("muscle", 1320))):
            b += [ico(nm, x, 460, 170, INK, .55 - i * .17)]
    elif n == 3:
        b += [F(x=960, pose="stand", expr="neutral")[0]]
    elif n == 4:
        fig, an = F(x=960, pose="stand", expr="calm")
        b += [fig, flame(an["top"][0], an["top"][1] - 110, 140)]
    elif n == 5:
        b += [floor_line(), flame(1280, 480, 200), F(x=720, pose="explain", expr="calm", look=6)[0]]
    elif n == 6:
        b += [ico("bulb", 1280, 460, 220, INK, .3), acc("xmark", 1280, 460, 170, w=8), F(x=700, pose="stand", expr="neutral", look=6)[0]]
    elif n == 7:
        x, y, ang = on_slope(.12)
        b += [hill()] + [glow(*on_slope(t)[:2], 30, "A", .9) for t in (.04, .08)]
        b += [figure(x, y, 1.2, "walk", "determined", look=6, tilt=ang * .6)[0]]
    # ---------------------------------------------------------------- MÓDULO 1 — West Point
    elif n == 8:
        b += [glow(960, 200, 600, "W", 1), formation()]
    elif n == 9:
        x0, y0, x1, y1 = 300, FLOOR, 1700, 260
        b += [hill(x0=x0, y0=y0, x1=x1, y1=y1), dust(1000, 600, 900, 300, 90, seed=9, op=.35)]
        ang = math.degrees(math.atan2(y1 - y0, x1 - x0))
        b += [figure(x0 + (x1 - x0) * .42, y0 + (y1 - y0) * .42, 1.4, "hunch", "strain", look=6, tilt=ang * .5)[0]]
    elif n == 10:
        b += [ico("clipboard", 1380, 520, 340, INK, rows=2), F(x=640, pose="stand", expr="thoughtful", look=6)[0]]
    elif n == 11:
        b += [ico("clipboard", 1300, 500, 300, INK, rows=2), acc("gauge", 1300, 640, 110)]
        b += [F(x=640, pose="stand", expr="attentive", look=6)[0]]
    elif n == 12:
        b += [ico("page", 1400, 420, 200, INK, .8, rot=-8), ico("page", 1430, 440, 200, INK, .3, rot=6)]
        b += [F(x=720, pose="stand", expr="attentive", look=6)[0]]
    elif n == 13:
        b += [ico("clipboard", 1300, 480, 300, INK, .25, rows=2), F(x=700, pose="head_shake", expr="neutral", look=6)[0]]
    elif n == 14:
        b += [floor_line(), ico("clipboard", 1600, 440, 200, INK, .2, rows=2), acc("gauge", 1260, 460, 240)]
        b += [F(x=640, pose="stand", expr="calm", look=6)[0]]
    elif n == 15:
        b += [formation(cx=1260, rows=4, cols=8, gap_x=90, gap_y=120, s=.42, keep={3, 12, 21, 30})]
        b += [F(x=480, pose="stand", expr="determined", look=6)[0]]
    elif n == 16:
        x0, y0, x1, y1 = 300, FLOOR, 1700, 260
        b += [hill(x0=x0, y0=y0, x1=x1, y1=y1)]
        for i, t in enumerate((.25, .5, .75)):
            px, py = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
            b += [f'<g data-dot="{i}">' + line(px, py - 20, px, py - 200, INK, 3, .3, "8 8") + ico("page", px, py - 230, 60, INK, .5) + "</g>"]
        ang = math.degrees(math.atan2(y1 - y0, x1 - x0))
        b += [glow(x0 + (x1 - x0) * .55, y0 + (y1 - y0) * .55 - 200, 260, "A", .5),
              figure(x0 + (x1 - x0) * .55, y0 + (y1 - y0) * .55, 1.2, "walk", "determined", look=6, tilt=ang * .5, color=ACC)[0]]
    elif n == 17:
        x0, y0, x1, y1 = 120, FLOOR, 1200, 420
        b += [f'<path d="M{x0},{y0} L{x1},{y1} L1900,{y1}" fill="none" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/>']
        b += [rim(1450, 260, 400), figure(1450, y1, 1.12, "hands_hips", "determined", look=-4)[0]]
    # ---------------------------------------------------------------- MÓDULO 2 — La Fórmula
    elif n == 18:
        b += [acc("book", 1260, 360, 200, progress=0), chain([("star", INK, .4), "x", ("arrow_up", INK, .4), "=", ("gear", INK, .4)], y=760, x0=1000, x1=1560, size=80)]
        b += [F(x=640, pose="explain", expr="thoughtful", look=6)[0]]
    elif n == 19:
        b += [chain([("star", INK, .9), "x", ("arrow_up", ACC, 1), "=", ("gear", INK, .9)], x0=400, x1=1520, size=190)]
    elif n == 20:
        b += [chain([("gear", INK, .9), "x", ("arrow_up", ACC, 1), "=", ("burst", INK, .9)], x0=400, x1=1520, size=190)]
    elif n == 21:
        b += [ico("star", 1080, 300, 110, INK, .3), acc("arrow_up", 1320, 300, 120), acc("arrow_up", 1560, 300, 120)]
        b += [F(x=640, pose="point", expr="attentive", look=6)[0]]
    elif n == 22:
        for x, big in ((700, False), (1220, True)):
            fig, an = figure(x, FLOOR, 1.12, "stand", op=.45, ghost=True)
            tx, ty = an["top"]
            b += [fig, ico("star", tx - 60, ty - 80, 70, INK, .8)]
            b += [acc("arrow_up", tx + 60, ty - 80, 110) if big else ico("arrow_up", tx + 60, ty - 80, 70, INK, .6)]
        b += [floor_line()]
    elif n == 23:
        b += [ico("burst", 660, 540, 150, INK, .6), acc("burst", 1260, 540, 300)]
    elif n == 24:
        b += [floor_line(), acc("burst", 1300, 460, 280), F(x=700, pose="hands_hips", expr="satisfied", look=6)[0]]
    elif n == 25:
        b += [chain([("star", INK, .9), "x", ("arrow_up", ACC, 1), "=", ("gear", INK, .9), "x", ("arrow_up", ACC, 1), "=", ("burst", INK, 1)],
                    x0=180, x1=1740, size=130)]
    elif n == 26:
        b += [ico("star", 1300, 460, 170, INK, .55), F(x=700, pose="explain", expr="thoughtful", look=6)[0]]
    elif n == 27:
        b += [acc("arrow_up", 1240, 440, 240), ico("burst", 1560, 360, 160, INK, .9), F(x=640, pose="stand", expr="calm", look=6)[0]]
    # ---------------------------------------------------------------- MÓDULO 3 — Sesgo de lo Natural
    elif n == 28:
        b += [floor_line(), rim(960, 520, 520), F(x=960, pose="stand", expr="attentive", look=4, tilt=5)[0]]
    elif n == 29:
        b += [ico("campus", 1360, 420, 300, INK, .35), F(x=700, pose="stand", expr="thoughtful", look=6)[0]]
    elif n == 30:
        b += [floor_line(), spotlight(960), figure(960, FLOOR, 1.05, "stand", op=.5, ghost=True)[0], figure(1360, FLOOR, 1.05, "stand", op=.4, ghost=True)[0]]
        b += [F(x=440, pose="stand", expr="thoughtful", look=6)[0]]
    elif n == 31:
        b += [floor_line(), spotlight(760, op=.18)]
        for x in (760, 1160):
            fig, an = figure(x, FLOOR, 1.12, "stand", op=.45, ghost=True)
            b += [fig, ico("burst", x, an["top"][1] - 90, 100, INK, .9)]
    elif n == 32:
        b += [ico("note", 760, 520, 230, INK, .9), ico("note", 1160, 520, 230, INK, .9)]
    elif n == 33:
        b += [ico("note", 760, 560, 230, INK, .9), ico("note", 1160, 560, 230, INK, .9), ico("star", 760, 300, 80, INK, .8), ico("clock", 1160, 300, 80, INK, .8)]
    elif n == 34:
        b += [acc("note", 1120, 560, 220), ico("note", 1460, 560, 220, INK, .5), ico("star", 1120, 320, 70, INK, .8), ico("clock", 1460, 320, 70, INK, .8)]
        b += [F(x=520, pose="stand", expr="satisfied", look=6)[0]]
    elif n == 35:
        b += [ico("note", 1240, 520, 240, INK, .95), ico("note", 1150, 520, 240, INK, .12), ico("note", 1330, 520, 240, INK, .12)]
        b += [F(x=620, pose="head_shake", expr="satisfied", look=6)[0]]
    elif n == 36:
        b += [floor_line(), acc("star", 1300, 420, 200), F(x=720, pose="explain", expr="warm", look=6)[0]]
    elif n == 37:
        b += [ico("star", 1560, 320, 110, INK, .3), acc("clock", 1240, 500, 170), F(x=760, pose="reach", expr="determined", look=6)[0]]
    elif n == 38:
        b += [ico("star", 1460, 300, 160, INK, .25), F(x=760, pose="shrug", expr="calm", look=4)[0]]
    elif n == 39:
        fig, an = F(x=860, pose="walk", expr="determined", look=6)
        b += [floor_line(), fig, acc("clock", an["head"][0] + 260, an["head"][1], 110)]
    # ---------------------------------------------------------------- MÓDULO 4 — Consistencia
    elif n == 40:
        b += [floor_line(), ico("calendar", 1280, 460, 220, INK, .9, crossed=4), F(x=700, pose="stand", expr="neutral", look=6)[0]]
    elif n == 41:
        b += [f'<g data-acc="1100,600">' + glow(1100, 600, 400, "A", .4)
              + f'<line x1="520" y1="860" x2="1840" y2="380" stroke="{ACC}" stroke-width="10" stroke-linecap="round"/></g>']
        for i in range(7):
            t = i / 7
            b += [ico("calendar", 700 + 1100 * t, 700 - 420 * t, 120 * (1 - .55 * t), INK, .7 - .5 * t, crossed=12)]
        b += [figure(440, FLOOR, 1.0, "walk", "determined", look=6)[0]]
    elif n == 42:
        b += [acc("compass", 1380, 420, 230), F(x=760, pose="stand", expr="thoughtful", look=6)[0]]
    elif n == 43:
        b += [ico("bulb", 1300, 460, 180, INK, .25), ico("xmark", 1300, 460, 150, INK, .35), F(x=720, pose="stand", expr="satisfied", look=6)[0]]
    elif n == 44:
        b += [line(160, FLOOR, 1800, FLOOR, ACC, 6, .6), F(x=760, pose="walk", expr="neutral", look=6)[0]]
    elif n == 45:
        b += [f'<rect x="0" y="0" width="1920" height="1080" fill="#000" opacity=".35"/>', ico("compass", 1360, 300, 130, INK, .2)]
        b += [line(160, FLOOR, 1800, FLOOR, ACC, 6, .35), F(x=860, pose="walk", expr="resigned", look=6)[0]]
    elif n == 46:
        b += [line(160, 760, 1800, 760, ACC, 8, .8)]
        for i, (x, y) in enumerate(((1700, 260), (1500, 1000), (1800, 520), (1200, 300))):
            b += [line(700 + i * 200, 760, x, y, INK, 4, .45, "12 10"), ico("star", x, y, 70, INK, .8)]
    elif n == 47:
        b += [line(160, 900, 1800, 900, ACC, 8, .8), figure(1300, 900, .9, "walk", "determined", look=6)[0]]
        for i, (x, y) in enumerate(((560, 260), (900, 200), (1200, 340), (360, 420))):
            b += [line(760, 620, x, y, INK, 3, .3, "10 10"), figure(x, y + 140, .4, "walk", op=.28, ghost=True)[0]]
    # ---------------------------------------------------------------- MÓDULO 5 — La Cosa Difícil
    elif n == 48:
        b += [floor_line(), ico("sofa", 1380, 800, 200, INK, .5), ico("lamp", 1620, 760, 150, INK, .5), glow(1600, 640, 240, "warm", 1)]
        b += [F(x=720, pose="explain", expr="calm", look=6)[0]]
    elif n == 49:
        b += [acc("dumbbell", 960, 540, 260)]
    elif n == 50:
        for x, s_, nm in ((520, 1.3, "book"), (880, 1.0, "note"), (1180, .85, "shoe"), (1440, .7, "dumbbell")):
            fig, an = figure(x, 1080, s_ * 1.6, "reach", op=.35, ghost=True)
            hx, hy = an["rhand"]
            b += [fig, glow(hx + 30, hy, 70, "A", .9), ico(nm, hx + 30, hy, 60 * s_, ACC)]
    elif n == 51:
        for x, nm in ((1060, "book"), (1360, "note"), (1660, "shoe")):
            fig, an = figure(x, FLOOR, .8, "stand", op=.4, ghost=True)
            b += [fig, ico(nm, x, an["top"][1] - 70, 80, INK, .9)]
        b += [floor_line(), F(x=520, pose="explain", expr="warm", look=6)[0]]
    elif n == 52:
        fig, an = figure(820, FLOOR, 1.2, "reach_down", op=.5, ghost=True)
        hx, hy = an["rhand"]
        b += [floor_line(), fig, ico("note", hx + 40, hy + 30, 80, INK, .8)]
        b += [f'<g data-acc="{hx + 110},{hy}">' + glow(hx + 110, hy, 160, "A", .8)
              + line(hx + 110, hy - 140, hx + 110, hy + 140, ACC, 10) + "</g>"]
    elif n == 53:
        for i in range(12):
            x = 340 + i * 110
            b += [ico("page", x, 540, 70, INK, .6)]
            if i in (5, 11):
                b += [acc("check", x, 410, 70)]
    elif n == 54:
        b += [f'<g data-acc="1360,560">' + glow(1360, 560, 260, "A", .6)
              + f'<polyline points="1060,620 1140,500 1220,640 1300,480 1380,620 1460,500 1540,640 1620,520" fill="none" stroke="{ACC}" stroke-width="10" stroke-linejoin="round"/></g>']
        b += [F(x=640, pose="stand", expr="determined", look=6)[0]]
    elif n == 55:
        for i in range(10):
            x = 860 + i * 95
            b += [ico("page", x, 420, 60, INK, .5)]
            if i in (4, 9):
                b += [acc("check", x, 320, 60)]
        b += [F(x=520, pose="point", expr="calm", look=6)[0]]
    elif n == 56:
        b += [floor_line(), f'<polyline points="1000,{FLOOR - 10} 1060,{FLOOR - 90} 1120,{FLOOR - 10} 1180,{FLOOR - 100} 1240,{FLOOR - 10}" fill="none" stroke="{INK}" stroke-width="8" stroke-linejoin="round"/>']
        b += [acc("check", 1650, 300, 70), acc("check", 1780, 300, 70), F(x=820, pose="hands_hips", expr="determined", look=6)[0]]
    # ---------------------------------------------------------------- EL CIERRE
    elif n == 57:
        b += [acc("door", 1400, 560, 420, w=5), F(x=720, pose="stand", expr="calm")[0]]
    elif n == 58:
        b += [f'<path d="M960,180 L560,1000 M960,180 L1360,1000" stroke="{INK}" stroke-width="4" opacity=".25"/>',
              ico("door", 960, 380, 220, INK, .6, w=6), glow(960, 380, 220, "A", .35)]
        b += [figure(960, 980, 1.1, "walk", "determined", look=0)[0]]
    elif n == 59:
        b += [acc("bubble", 1320, 360, 220), F(x=760, pose="point_you", expr="warm", look=3)[0]]
    elif n == 60:
        b += [floor_line(), acc("bell", 1260, 430, 150), F(x=860, pose="thumbs", expr="smile")[0]]
    elif n == 61:
        b += [rim(960, 500, 620), F(x=960, pose="stand", expr="serene")[0]]
    else:
        raise ValueError(n)
    return b


def thumb_b():
    """Mẫu B — triptych: subida día 12 · práctica deliberada con calendario · no abandonar a la mitad (vật nhấn)."""
    pw = TW / 3
    b = [panel_bg(0, 0, pw, TH, "#7FB8FF", .26), panel_bg(pw, 0, pw, TH, "#5AC8C8", .22), panel_bg(2 * pw, 0, pw, TH, "#FF8A6B", .24)]
    b += [f'<path d="M0,600 L420,250" stroke="{INK}" stroke-width="6"/>', figure(200, 433, .9, "hunch", "strain", look=6, tilt=14)[0]]
    b += [desk(pw + 230, 420, 260), ico("calendar", pw + 330, 190, 110, INK, crossed=12), ico("notebook", pw + 230, 395, 60, INK, lit=2),
          chair(pw + 70, 560, .9), figure(pw + 80, 560, .9, "type", "determined", look=5)[0]]
    mid = 2 * pw + pw / 2
    b += [acc("dumbbell", mid + 110, 300, 90, glow_r=120), figure(mid - 60, 560, .95, "hands_hips", "determined", look=6)[0]]
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 3}" y="0" width="6" height="{TH}" fill="#000"/>')
    b.append(badge())
    return b


def thumb_c():
    """Mẫu C — lưới 6 khung."""
    pw, ph = TW / 3, TH / 2
    tints = ("#7FB8FF", "#FFB46B", "#8C7BFF", "#5AC8C8", "#FF8A6B", "#FFD9A0")
    b = [panel_bg((i % 3) * pw, (i // 3) * ph, pw, ph, t, .24) for i, t in enumerate(tints)]
    s = .6
    b += [f'<path d="M150,330 L410,80" stroke="{INK}" stroke-width="5"/>', figure(110, 330, s, "stand", "determined", look=6)[0]]       # 1
    b += [ico("star", 600, 150, 60, INK), op_sign(660, 150, "x", size=24), acc("arrow_up", 720, 150, 60, glow_r=80),
          figure(520, 330, s, "explain", "attentive", look=6)[0]]                                                                 # 2
    b += [spotlight(1160, top=0, bottom=330, w=160, op=.3), figure(1160, 330, s, "cheer", op=.4, ghost=True)[0],
          figure(990, 330, s, "stand", "calm", look=6)[0]]                                                                       # 3
    b += [ico("calendar", 310, 440, 80, INK, crossed=12), figure(150, 690, s, "stand", "determined", look=6)[0]]                # 4
    b += [ico("shoe", 600, 560, 120, INK), ico("calendar", 720, 520, 90, INK, .8, crossed=8)]                                  # 5
    b += [f'<path d="M860,712 L1080,580 L1280,580" stroke="{INK}" stroke-width="5" fill="none"/>', figure(1170, 580, .48, "hands_hips", "serene")[0]]  # 6
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 1.5}" y="0" width="3" height="{TH}" fill="{BG}"/>')
    b.append(f'<rect x="0" y="{ph - 1.5}" width="{TW}" height="3" fill="{BG}"/>')
    b.append(badge())
    return b

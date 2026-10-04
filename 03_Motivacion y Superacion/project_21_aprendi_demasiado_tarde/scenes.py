# -*- coding: utf-8 -*-
"""
scenes.py — Kịch bản hình của project 21 "5 Lecciones de Vida Que Aprendí Demasiado Tarde" (77 khung + 2 thumbnail),
bám theo [VISUAL DESCRIPTION] trong transcript_and_visuals.txt. Màu nhấn #FF3B78 (03_Motivacion y Superacion).
Mô-típ: 5 chấm sáng (5 bài học), vòng lặp lái tự động, ngưỡng cửa + đếm ngược 5-4-3-2-1, vòng ranh giới,
cán cân việc/nghỉ, la bàn chỉ vào trong (locus de control).
"""
from scenekit import *  # noqa: F401,F403
from sticklib import *  # noqa: F401,F403  (nạp lại ACC sau khi đã set_accent theo playlist)
from scenekit import FLOOR, bed, desk
from thumbkit import TH, TW, badge, panel_bg


def dots5(cx, cy, r, a0, a1, size=14, lit=None, hi=None):
    out = dots_arc(cx, cy, r, n=5, a0=a0, a1=a1, size=size, lit=lit)
    if hi is not None:
        a = math.radians(a0 + (a1 - a0) * hi / 4)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        out += f'<g data-acc="{x:.0f},{y:.0f}">' + glow(x, y, size * 6, "A", 1) + f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{size * 1.6}" fill="{ACC}"/></g>'
    return out


def loop_path(cx=960, cy=820, rx=520, ry=110, color=None, op=.6):
    color = color or ACC
    return (f'<g data-acc="{cx},{cy}"><ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{color}" stroke-width="6" '
            f'stroke-dasharray="4 18" stroke-linecap="round" opacity="{op}"/></g>')


def triangle_loop(bend=False):
    pts = {"house": (620, 300), "road": (1300, 300), "schooldesk": (960, 800)}
    out = []
    p = list(pts.values())
    d = f"M{p[0][0]},{p[0][1]} L{p[1][0]},{p[1][1]} L{p[2][0]},{p[2][1]} Z"
    out.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="5" stroke-dasharray="14 12" opacity=".5"/>')
    if bend:
        out.append(f'<g data-acc="1250,560">' + glow(1250, 560, 140, "A", 1)
                   + f'<path d="M1300,300 Q1500,600 960,800" fill="none" stroke="{ACC}" stroke-width="7"/></g>')
    for nm, (x, y) in pts.items():
        out.append(f'<circle cx="{x}" cy="{y}" r="90" fill="{BG}" stroke="{INK}" stroke-width="4" opacity=".8"/>' + ico(nm, x, y, 110, INK))
    return "".join(out)


def threshold(x=1200, op=1.0, glow_op=.5):
    return (glow(x, 560, 300, "A", glow_op) + f'<rect x="{x - 110}" y="250" width="220" height="{FLOOR - 250}" fill="none" stroke="{ACC}" '
            f'stroke-width="7" opacity="{op}"/>')


def countdown(x0=520, x1=1400, y=330, arc=80):
    out = []
    for i, d in enumerate("54321"):
        x = x0 + (x1 - x0) * i / 4
        yy = y - arc * math.sin(math.pi * i / 4)
        out.append(f'<g data-dot="{i}">' + glow(x, yy - 40, 90, "A", .8)
                   + f'<text x="{x}" y="{yy}" font-family="Anton" font-size="130" fill="{ACC}" text-anchor="middle">{d}</text></g>')
    return "".join(out)


def reaching_hands(cx, cy, r=330, n=6, op=.35, size=110):
    out = []
    for i in range(n):
        a = math.radians(360 * i / n + 15)
        x, y = cx + r * math.cos(a), cy + r * .8 * math.sin(a)
        out.append(ico("hand", x, y, size, INK, op, rot=math.degrees(a) - 90))
    return "".join(out)


def boundary(cx, cy, rx=300, ry=420):
    return (f'<g data-acc="{cx},{cy}">' + glow(cx, cy, rx, "A", .35)
            + f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{ACC}" stroke-width="6"/></g>')


def build_layers(n, shot):
    F = lambda **kw: shot_fig(shot, **kw)  # noqa: E731
    b = []
    # ---------------------------------------------------------------- EL GANCHO
    if n == 1:
        b += [floor_line(), ico("book", 1300, 460, 200, INK, .3), F(x=760, pose="stand", expr="calm", look=6)[0]]
    elif n == 2:
        b += [ico("book", 1300, 460, 240, INK, .55, progress=0), dust(1300, 400, 300, 200, 30, seed=2, op=.3)]
        b += [F(x=720, pose="stand", expr="worried", look=6)[0]]
    elif n == 3:
        b += [F(x=760, pose="stand", expr="resigned", look=6)[0], dots5(760, 430, 380, -48, 48)]
    elif n == 4:
        b += [floor_line(), figure(1500, FLOOR, .75, "stand", op=.35, ghost=True)[0], F(x=700, pose="reach", expr="worried", look=6)[0]]
    elif n == 5:
        b += [floor_line(), figure(1500, FLOOR, .75, "walk", op=.3, ghost=True, tilt=-4)[0], F(x=700, pose="shrug", expr="satisfied", look=6)[0]]
    # ---------------------------------------------------------------- LA PROMESA
    elif n == 6:
        b += [floor_line(), chair(940, FLOOR, 1.12), figure(950, FLOOR, 1.12, "sit", "warm", look=4)[0], dots_row(1260, 1700, 400, n=5)]
    elif n == 7:
        b += [ico("brain", 960, 280, 180, INK, .5), dots_row(560, 1360, 720, n=5)]
        b += [line(960, 360, x, 690, INK, 3, .3, "8 8") for x in (560, 760, 960, 1160, 1360)]
    elif n == 8:
        b += [F(x=760, pose="stand", expr="determined", look=6)[0], dots5(760, 430, 380, -48, 48, lit=4, hi=4)]
    elif n == 9:
        b += [dots_row(1040, 1600, 360, n=4, op=.5), acc("star", 1760, 360, 60), F(x=700, pose="stand", expr="warm", look=6)[0]]
    # ---------------------------------------------------------------- L1 — Piloto Automático
    elif n == 10:
        b += [loop_path(), figure(1300, 860, 1.0, "walk", "neutral", look=6)[0]]
    elif n == 11:
        for i, (x, o) in enumerate(((560, .2), (760, .35), (960, 1.0))):
            if o < 1:
                b += [figure(x, FLOOR, 1.12, "think", op=o, ghost=True)[0]]
        b += [floor_line(), F(x=960, pose="think", expr="neutral", look=4)[0]]
    elif n == 12:
        b += [triangle_loop()]
    elif n == 13:
        fig, an = F(x=760, pose="stand", expr="thoughtful", look=6)
        hx, hy = an["head"]
        b += [fig, f'<g data-acc="{hx:.0f},{hy:.0f}">' + glow(hx, hy, 260, "A", .7) + ico("cloud", hx + 120, hy - 140, 160, ACC, .5) + "</g>"]
    elif n == 14:
        b += [acc("toggle", 1340, 460, 200), F(x=720, pose="stand", expr="resigned", look=6)[0]]
    elif n == 15:
        fig, an = F(x=760, pose="stand", expr="attentive", look=6)
        b += [fig, ico("battery", an["head"][0] + 360, an["head"][1], 170, INK, level=.9)]
    elif n == 16:
        b += [ico("battery", 1260, 460, 240, INK, level=.6), crack(1180, 400, 1340, 520, seed=16, w=5)]
        b += [F(x=680, pose="stand", expr="worried", look=6)[0]]
    elif n == 17:
        b += [floor_line(), ico("door", 1100, FLOOR - 160, 320, INK, .4, w=6)]
        b += [F(x=1420, pose="walk", expr="neutral", look=6)[0]]
    elif n == 18:
        b += [floor_line(), acc("hand", 1240, 420, 130, rot=-30), F(x=860, pose="think", expr="determined", look=6)[0]]
    elif n == 19:
        b += [triangle_loop(bend=True)]
    elif n == 20:
        b += [ico("cloud", 1200, 220, 160, INK, .1), F(x=860, pose="stand", expr="surprised", look=6)[0], particles(1120, 260, 300, 200, 30, seed=20, op=.6)]
    elif n == 21:
        b += [floor_line(), F(x=960, pose="walk", expr="uneasy", look=4)[0]]
    elif n == 22:
        b += [scale_with(1360, 560, 340, 24, color=INK, op=.5), acc("toggle", 1240, 360, 60), F(x=720, pose="stand", expr="worried", look=6)[0]]
    elif n == 23:
        b += [loop_path(rx=620, ry=130, op=.9), F(x=960, pose="stand", expr="resigned")[0]]
    # ---------------------------------------------------------------- L2 — Esperar Sentirte Listo
    elif n == 24:
        b += [floor_line(), threshold(1240), F(x=880, pose="stand", expr="worried", look=6)[0]]
    elif n == 25:
        b += [ico("calendar", 360 + i * 70, 320 + i * 40, 160, INK, .15 + i * .1, crossed=6) for i in range(5)]
        b += [floor_line(), threshold(1500, op=.5, glow_op=.2), F(x=1000, pose="hunch", expr="resigned", look=6)[0]]
    elif n == 26:
        fig, an = F(x=760, pose="reach", expr="worried", look=6)
        hx, hy = an["rhand"]
        b += [fig, acc("heart", hx + 280, hy - 60, 110)]
    elif n == 27:
        b += [countdown(), F(x=1560, pose="stand", expr="attentive", look=-6)[0]]
    elif n == 28:
        b += [floor_line(), ico("heart", 1600, 280, 90, INK, .25), threshold(1300, glow_op=.3), F(x=980, pose="walk", expr="determined", look=6)[0]]
    elif n == 29:
        b += [acc("heart", 1380, 360, 200), ico("door", 1180, 700, 400, INK, .5, w=5), F(x=760, pose="walk", expr="surprised", look=6)[0]]
    elif n == 30:
        fig, an = F(x=960, pose="stand", expr="surprised")
        b += [f'<g data-acc="960,560">' + glow(960, 560, 380, "A", .5) + "</g>", fig]
    elif n == 31:
        fig, an = F(x=960, pose="stand", expr="worried")
        b += [glow(960, 560, 620, "A", .7), crack(560, 300, 760, 700, seed=31, w=4), crack(1200, 260, 1420, 760, seed=13, w=4), fig]
    elif n == 32:
        b += [countdown(x0=800, x1=1700, y=300, arc=60), F(x=520, pose="stand", expr="determined", look=6)[0]]
    elif n == 33:
        b += [floor_line(), threshold(960, glow_op=.6), F(x=1060, pose="stride", expr="determined", look=6, tilt=4)[0]]
    elif n == 34:
        b += [F(x=960, pose="stand", expr="defensive")[0]]
    elif n == 35:
        fig, an = F(x=1300, pose="stand", expr="satisfied", look=-4)
        b += [floor_line(), ico("door", 760, FLOOR - 160, 320, INK, .4, w=6), fig, acc("heart", an["head"][0] + 220, an["head"][1], 110)]
    # ---------------------------------------------------------------- L3 — Decir Sí a Todo
    elif n == 36:
        b += [reaching_hands(960, 520, 400, n=7), F(x=960, pose="stand", expr="uneasy")[0]]
    elif n == 37:
        b += [F(x=960, pose="stand", expr="defensive", look=0)[0], reaching_hands(960, 420, 700, n=5, op=.2)]
    elif n == 38:
        b += [reaching_hands(960, 560, 230, n=6, op=.4, size=100), F(x=960, pose="stand", expr="worried")[0]]
    elif n == 39:
        fig, an = F(x=960, pose="carry", expr="strain")
        tx, ty = an["top"]
        b += [ico("task", tx + dx, ty - 70 - k * 70, 90, INK, .8) for k, dx in enumerate((-20, 30, -10))] + [fig]
    elif n == 40:
        b += [ico("bubble", 1380, 380, 240, INK, .5), F(x=760, pose="stand", expr="thoughtful", look=6)[0]]
    elif n == 41:
        b += [ico("bubble", 1360, 400, 260, INK), line(1270, 380, 1450, 380, ACC, 12), glow(1360, 380, 160, "A", .8)]
        b += [F(x=720, pose="stand", expr="calm", look=6)[0]]
    elif n == 42:
        b += [floor_line(), ico("hand", 1240, 420, 160, INK, .55, rot=-90), F(x=900, pose="stand", expr="defensive", look=6)[0]]
    elif n == 43:
        b += [ico("hand", 1280, 420, 320, INK, .4, rot=-90), F(x=720, pose="hunch", expr="resigned", look=6)[0]]
    elif n == 44:
        fig, an = F(x=960, pose="stop", expr="determined")
        b += [boundary(960, 620, 420, 560), fig]
    elif n == 45:
        b += [acc("bolt", 620, 480, 160), line(820, 480, 1000, 480, INK, 3, .3)]
        b += [ico("boulder", 1360, 500, 300, INK, .6), line(1180, 640, 1560, 640, INK, 5, .4, "16 10")]
    elif n == 46:
        b += [floor_line(), reaching_hands(960, 520, 700, n=4, op=.12), F(x=960, pose="stand", expr="neutral")[0]]
    elif n == 47:
        b += [floor_line(), rim(960, 520, 500), F(x=960, pose="stand", expr="serene")[0]]
    # ---------------------------------------------------------------- L4 — El Descanso
    elif n == 48:
        b += [scale_with(1300, 600, 380, 22, left=[("task", INK, 70, .9), ("task", INK, 70, .9), ("task", INK, 70, .9)],
                         right=("bedicon", ACC, 80, 1)), F(x=600, pose="stand", expr="worried", look=6)[0]]
    elif n == 49:
        b += [scale_with(1300, 600, 380, 26, left=[("task", INK, 80, 1), ("task", INK, 80, 1), ("task", INK, 80, 1)],
                         right=("bedicon", ACC, 70, .7)), F(x=640, pose="reach", expr="avoid", look=6)[0]]
    elif n == 50:
        b += [floor_line(), desk(1000, 705, 520)]
        b += [ico("task", 1180 + (k % 2) * 30, 620 - k * 60, 80, INK, .6) for k in range(5)]
        b += [chair(780, FLOOR, 1.12), figure(790, FLOOR, 1.12, "type", "resigned", look=5, tilt=12)[0]]
    elif n == 51:
        b += [acc("book", 1340, 420, 220, progress=0), glow(1340, 380, 220, "warm", 1), F(x=740, pose="stand", expr="thoughtful", look=6)[0]]
    elif n == 52:
        b += [dust(1260, 520, 400, 200, 40, seed=52, op=.4), acc("bedicon", 1260, 540, 220), F(x=680, pose="stand", expr="calm", look=6)[0]]
    elif n == 53:
        b += [floor_line(), rim(960, 520, 500), F(x=960, pose="stand", expr="attentive", look=4, tilt=5)[0]]
    elif n == 54:
        b += [crowd([1180, 1360, 1540, 1720], FLOOR, .75, .2, poses=["cross"]), floor_line(), F(x=660, pose="stand", expr="uneasy", look=6)[0]]
    elif n == 55:
        b += [crowd([1300, 1600], 1080, 1.2, .06, poses=["cross"]), F(x=760, pose="stand", expr="determined", look=6)[0]]
    elif n == 56:
        b += [floor_line(), glow(960, 640, 420, "A", .5), bed(560, 1360, 690, op=.9)]
        b += [figure(700, 682, 1.15, "stand", "serene", tilt=90)[0]]
    elif n == 57:
        b += [floor_line()] + [f'<g data-dot="{i}">' + place(1240 + i * 120, 360, 70, icon("check", ACC, 9)) + "</g>" for i in range(4)]
        b += [F(x=760, pose="cheer", expr="smile")[0]]
    elif n == 58:
        b += [floor_line(), F(x=1100, pose="walk", expr="calm", look=6)[0], figure(760, FLOOR, 1.12, "hunch", op=.08, ghost=True)[0]]
    # ---------------------------------------------------------------- L5 — Nadie Viene a Salvarte
    elif n == 59:
        b += [dots_row(760, 1160, 160, n=5, op=.6), F(x=960, pose="stand", expr="neutral", head_y=None)[0]]
    elif n == 60:
        fig, an = F(x=960, pose="stand", expr="serene")
        b += [glow(960, 600, 520, "A", .4), fig]
    elif n == 61:
        b += [line(1100, 520, 1900, 520, INK, 4, .25), F(x=760, pose="cross", expr="neutral", look=6)[0]]
    elif n == 62:
        b += [ico("dice", 1300, 300, 130, INK, .25), ico("eye", 1600, 460, 140, INK, .2), F(x=640, pose="cross", expr="resigned", look=6)[0]]
    elif n == 63:
        b += [acc("compass", 1380, 420, 220, rot=40), F(x=760, pose="stand", expr="thoughtful", look=6)[0]]
    elif n == 64:
        fig, an = F(x=760, pose="stand", expr="determined", look=6)
        sx, sy = an["sh"]
        b += [fig, acc("compass", sx + 520, sy, 200, rot=-90), line(sx + 400, sy, sx + 60, sy + 40, ACC, 5, .7, "12 10")]
    elif n == 65:
        b += [ico("dice", 1700, 220, 70, INK, .1), ico("eye", 1800, 360, 70, INK, .1)]
        b += [f'<rect x="1180" y="300" width="60" height="605" fill="none" stroke="{INK}" stroke-width="6" stroke-dasharray="16 12" opacity=".5"/>']
        b += [floor_line(), F(x=960, pose="push", expr="strain", look=6, tilt=8)[0]]
    elif n == 66:
        b += [line(160, 560, 1800, 560, INK, 3, .15), floor_line(), F(x=960, pose="cross", expr="resigned")[0]]
    elif n == 67:
        b += [F(x=960, pose="stand", expr="worried", look=-6)[0]]
    elif n == 68:
        b += [acc("compass", 1380, 380, 220, rot=-90), F(x=760, pose="stand", expr="determined", look=6)[0]]
    elif n == 69:
        fig, an = F(x=960, pose="shrug", expr="thoughtful")
        b += [fig] + [acc("gear", x, y - 30, 60) for x, y in (an["lhand"], an["rhand"])]
    elif n == 70:
        b += [floor_line(), dots_row(300, 760, 560, n=5), F(x=1200, pose="walk", expr="calm", look=6)[0]]
    # ---------------------------------------------------------------- EL CIERRE
    elif n == 71:
        b += [F(x=760, pose="stand", expr="calm")[0], dots5(760, 430, 380, -48, 48)]
    elif n == 72:
        b += [F(x=960, pose="explain", expr="satisfied", look=4)[0]]
    elif n == 73:
        b += [F(x=960, pose="point_you", expr="warm")[0]]
    elif n == 74:
        b += [floor_line(), acc("notebook", 1300, 500, 220, lit=3), F(x=720, pose="stand", expr="calm", look=6)[0]]
    elif n == 75:
        b += [acc("bubble", 1320, 360, 220), F(x=760, pose="point_you", expr="warm", look=3)[0]]
    elif n == 76:
        b += [floor_line(), acc("bell", 1260, 430, 150), F(x=860, pose="thumbs", expr="smile")[0]]
    elif n == 77:
        b += [rim(960, 500, 620), F(x=960, pose="stand", expr="serene")[0]]
    else:
        raise ValueError(n)
    return b


def thumb_b():
    """Mẫu B — triptych: cuenta regresiva 5→1 · un "no" calmado · descansar sin culpa (vật nhấn)."""
    pw = TW / 3
    b = [panel_bg(0, 0, pw, TH, "#7FB8FF", .24), panel_bg(pw, 0, pw, TH, "#FFB46B", .26), panel_bg(2 * pw, 0, pw, TH, "#8C7BFF", .24)]
    b += [f'<text x="310" y="250" font-family="Anton" font-size="120" fill="{INK}" text-anchor="middle" opacity=".85">5</text>',
          figure(150, 560, .95, "point", "determined", look=6)[0]]
    b += [figure(pw + 200, 560, .95, "stop", "determined", look=6)[0]]
    mid = 2 * pw + pw / 2
    b += [f'<rect x="{mid - 170}" y="440" width="340" height="40" rx="12" fill="none" stroke="{INK}" stroke-width="7"/>',
          figure(mid - 130, 432, .8, "stand", "serene", tilt=90)[0], acc("moon", mid + 120, 230, 60, glow_r=100)]
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 3}" y="0" width="6" height="{TH}" fill="#000"/>')
    b.append(badge())
    return b


def thumb_c():
    """Mẫu C — lưới 6 khung."""
    pw, ph = TW / 3, TH / 2
    tints = ("#5AC8C8", "#7FB8FF", "#FFB46B", "#8C7BFF", "#FF3B78", "#FFD9A0")
    b = [panel_bg((i % 3) * pw, (i // 3) * ph, pw, ph, t, .22) for i, t in enumerate(tints)]
    s = .62
    b += [figure(213, 330, s, "walk", "confused", look=4)[0]]                                                        # 1 piloto automático
    b += [f'<text x="760" y="160" font-family="Anton" font-size="90" fill="{INK}" text-anchor="middle" opacity=".8">3</text>',
          figure(580, 330, s, "point", "determined", look=6)[0]]                                                     # 2 esperar listo
    b += [figure(1066, 330, s, "stop", "determined", look=6)[0]]                                                     # 3 límites
    b += [line(90, 640, 340, 640, INK, 6), figure(110, 632, .55, "stand", "serene", tilt=90)[0]]                     # 4 descanso
    b += [acc("hourglass", 640, 540, 200)]                                                                           # 5 locus de control
    b += [rim(1066, 540, 200), figure(1066, 690, s, "stand", "determined")[0]]                                       # 6 cierre
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 1.5}" y="0" width="3" height="{TH}" fill="{BG}"/>')
    b.append(f'<rect x="0" y="{ph - 1.5}" width="{TW}" height="3" fill="{BG}"/>')
    b.append(badge())
    return b

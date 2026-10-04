# -*- coding: utf-8 -*-
"""
scenes.py — Kịch bản hình của project 22 "5 Retos Que Muy Pocas Personas Se Atreven a Completar"
(54 khung + 2 thumbnail), bám theo [VISUAL DESCRIPTION] trong transcript_and_visuals.txt.
Màu nhấn #FF3B78 (03_Motivacion y Superacion).
"""
from scenekit import *  # noqa: F401,F403
from sticklib import *  # noqa: F401,F403  (nạp lại ACC sau khi đã set_accent theo playlist)
from scenekit import FLOOR, marker, mirror, table, timeline
from thumbkit import TH, TW, badge, panel_bg


def num_arc(cx, cy, r, a0, a1, size=70, lit=None):
    """5 ô số 1..5 xếp vòng cung (xuất hiện lần lượt)."""
    out = []
    for i in range(5):
        a = math.radians(a0 + (a1 - a0) * i / 4)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        on = lit is None or i < lit
        col = ACC if on else INK
        out.append(f'<g data-dot="{i}">' + (glow(x, y, size * 1.3, "A", .6) if on else "")
                   + f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{size * .55:.0f}" fill="{BG}" stroke="{col}" stroke-width="5"/>'
                   + f'<text x="{x:.0f}" y="{y + size * .3:.0f}" font-family="Anton" font-size="{size * .8:.0f}" fill="{col}" text-anchor="middle">{i + 1}</text></g>')
    return "".join(out)


def big_num(d, x, y, size=180):
    return (f'<g data-acc="{x},{y}">' + glow(x, y, size * 1.2, "A", .6)
            + f'<text x="{x}" y="{y + size * .36:.0f}" font-family="Anton" font-size="{size}" fill="{ACC}" text-anchor="middle">{d}</text></g>')


def doors(cx=960, cy=520, r=520, n=6, closed=0, op=.35):
    out = []
    for i in range(n):
        a = math.radians(-90 + 360 * i / n)
        x, y = cx + r * math.cos(a), cy + r * .7 * math.sin(a)
        o = op * (.35 if i < closed else 1)
        out.append(ico("door", x, y, 130, INK, o, w=6))
        if i < closed:
            out.append(line(x - 34, y, x + 34, y, INK, 6, op))
    return "".join(out)


def wristband(x, y, size=70, on=True):
    col = ACC if on else INK
    return (f'<g data-acc="{x},{y}">' + (glow(x, y, size, "A", .8) if on else "")
            + f'<ellipse cx="{x}" cy="{y}" rx="{size * .5:.0f}" ry="{size * .22:.0f}" fill="none" stroke="{col}" stroke-width="8"/></g>')


def counter(x, y, val, size=110):
    return (f'<rect x="{x - size * .6:.0f}" y="{y - size * .8:.0f}" width="{size * 1.2:.0f}" height="{size:.0f}" rx="14" fill="none" stroke="{INK}" stroke-width="5" opacity=".7"/>'
            f'<text x="{x}" y="{y + size * .05:.0f}" font-family="Anton" font-size="{size * .75:.0f}" fill="{INK}" text-anchor="middle">{val}</text>')


def build_layers(n, shot):
    F = lambda **kw: shot_fig(shot, **kw)  # noqa: E731
    b = []
    # ---------------------------------------------------------------- GANCHO
    if n == 1:
        b += [floor_line(), ico("bubble", 1280, 380, 180, INK, .4), F(x=760, pose="stand", expr="calm", look=6)[0]]
    elif n == 2:
        b += [floor_line(), glow(1320, 520, 300, "A", .5),
              f'<path d="M1100,700 L1320,360 L1540,700 Z" fill="none" stroke="{ACC}" stroke-width="8" stroke-linejoin="round"/>',
              F(x=720, pose="stand", expr="determined", look=6)[0]]
    elif n == 3:
        b += [doors(960, 540, 470, n=6, closed=6), F(x=960, pose="stand", expr="determined")[0]]
    # ---------------------------------------------------------------- PROMESA
    elif n == 4:
        b += [floor_line(), num_arc(1300, 760, 400, 200, 340, size=110), F(x=640, pose="explain", expr="calm", look=6)[0]]
    elif n == 5:
        b += [ico("muscle", 1220, 620, 150, INK, .25, rot=-12), acc("thought", 1440, 360, 200)]
        b += [F(x=700, pose="dismiss", expr="calm", look=6)[0]]
    elif n == 6:
        b += [acc("crutch", 1300, 600, 260, rot=25), line(1180, 600, 1100, 600, INK, 4, .4, "8 8"), F(x=760, pose="stand", expr="uneasy", look=6)[0]]
    elif n == 7:
        b += [floor_line(), num_arc(1300, 760, 400, 200, 340, size=110), F(x=640, pose="explain", expr="warm", look=6)[0]]
    # ---------------------------------------------------------------- RETO 1 — Silencio
    elif n == 8:
        b += [floor_line(), big_num("1", 1360, 420), chair(820, FLOOR, 1.12), figure(830, FLOOR, 1.12, "sit", "calm", look=5)[0]]
    elif n == 9:
        for i, (nm, x, y) in enumerate((("bubble", 1180, 300), ("note", 1440, 440), ("mic", 1220, 640))):
            b += [ico(nm, x, y, 120, INK, .55 - i * .15), ico("xmark", x, y, 90, INK, .3)]
        b += [F(x=700, pose="stand", expr="calm", look=6)[0]]
    elif n == 10:
        b += [F(x=960, pose="stand", expr="uneasy")[0]]
    elif n == 11:
        for nm, x, y in (("car", 360, 300), ("drop", 960, 200), ("shoe", 1560, 300)):
            b += [ico(nm, x, y, 150, INK, .4), ico("wave", x + 110, y - 60, 70, INK, .35)]
        b += [F(x=960, pose="stand", expr="neutral")[0]]
    elif n == 12:
        for nm, x, y in (("car", 420, 380), ("drop", 960, 240), ("shoe", 1500, 380)):
            b += [ico(nm, x, y, 170, INK, .55), ico("wave", x + 120, y - 70, 80, INK, .5)]
        b += [floor_line(), F(x=960, pose="stand", expr="thoughtful")[0]]
    elif n == 13:
        b += [ico("wave", 1360, 420, 220, INK, .35), F(x=760, pose="stand", expr="calm", look=6)[0]]
    elif n == 14:
        fig, an = F(x=960, pose="stand", expr="worried")
        tx, ty = an["top"]
        b += [fig, acc("thought", tx + 120, ty - 130, 260)]
    elif n == 15:
        fig, an = F(x=860, pose="stand", expr="determined", look=5)
        tx, ty = an["top"]
        b += [fig, acc("thought", tx + 360, ty + 60, 300)]
    # ---------------------------------------------------------------- RETO 2 — Soledad
    elif n == 16:
        b += [floor_line(), big_num("2", 1360, 420), f'<rect x="560" y="300" width="760" height="605" fill="none" stroke="{INK}" stroke-width="5" opacity=".35"/>']
        b += [crowd([200, 340, 1620, 1760], FLOOR, .6, .12, poses=["walk"]), F(x=900, pose="stand", expr="calm", look=4)[0]]
    elif n == 17:
        b += [floor_line(), table(1300, 700, 300), ico("phone", 1300, 676, 70, INK, .35, rot=90), F(x=720, pose="stand", expr="calm", look=6)[0]]
    elif n == 18:
        b += [ico("campus", 1400, 400, 260, INK, .4), F(x=760, pose="stand", expr="thoughtful", look=6)[0]]
    elif n == 19:
        b += [timeline(200, 820, 1720, 820, ticks=8, w=5), F(x=960, pose="stand", expr="attentive", look=4)[0]]
    elif n == 20:
        b += [glow(960, 560, 520, "warm", 1)] + [line(x, 220, x, 900, INK, 5, .12) for x in range(560, 1400, 80)]
        b += [F(x=960, pose="stand", expr="serene")[0]]
    elif n == 21:
        fig, an = F(x=860, pose="stand", expr="calm", look=6)
        hx, hy = an["head"]
        d = " ".join(f"Q{hx + 360 + i * 60},{hy - 60 + (40 if i % 2 else -40)} {hx + 380 + i * 60},{hy - 60}" for i in range(6))
        b += [fig, f'<g data-acc="{hx + 520:.0f},{hy - 60:.0f}">' + glow(hx + 520, hy - 60, 260, "A", .5)
              + f'<path d="M{hx + 320},{hy - 60} {d}" fill="none" stroke="{ACC}" stroke-width="6"/></g>']
    elif n == 22:
        b += [floor_line(), ico("hourglass", 1320, 520, 200, INK, .3), F(x=720, pose="explain", expr="calm", look=6)[0]]
    elif n == 23:
        b += [floor_line(), chair(820, FLOOR, 1.12)]
        fig, an = figure(830, FLOOR, 1.12, "sit", "serene", look=5)
        b += [fig, acc("thought", an["top"][0] + 260, an["top"][1] - 60, 200)]
    # ---------------------------------------------------------------- RETO 3 — Sin quejarte
    elif n == 24:
        fig, an = F(x=760, pose="stand", expr="calm", look=6)
        b += [floor_line(), big_num("3", 1360, 420), fig, wristband(*an["rhand"], size=50)]
    elif n == 25:
        fig, an = F(x=760, pose="think", expr="thoughtful", look=6)
        b += [fig, wristband(an["rhand"][0], an["rhand"][1] + 8, size=60), ico("book", 1400, 420, 180, INK, .4)]
    elif n == 26:
        b += [acc("bubble", 1360, 360, 220), ico("cloud", 1360, 350, 90, ACC), F(x=760, pose="stand", expr="surprised", look=6)[0]]
    elif n == 27:
        fig, an = F(x=860, pose="shrug", expr="neutral")
        lx, ly = an["lhand"]
        rx, ry = an["rhand"]
        b += [fig, wristband(lx, ly + 10, 50, on=False), wristband(rx, ry + 10, 50), line(lx + 40, ly - 30, rx - 40, ry - 30, ACC, 4, .7, "10 8")]
        b += [counter(1500, 380, "0")]
    elif n == 28:
        b += [f'<g data-dot="{i}">' + counter(560 + i * 260, 520, v) + "</g>" for i, v in enumerate("1230")]
        b += [line(1340, 450, 1420, 450, ACC, 6, .9)]
    elif n == 29:
        for i, (x, y) in enumerate(((560, 360), (960, 280), (1360, 360), (760, 640), (1160, 640))):
            b += [ico("bubble", x, y, 170, INK, .55), ico("cloud", x, y - 10, 60, ACC if i % 2 == 0 else INK, .9)]
    elif n == 30:
        b += [ico("mask", 1320, 480, 200, INK, .3, rot=-10), F(x=720, pose="dismiss", expr="determined", look=6)[0]]
    elif n == 31:
        b += [f'<g data-acc="760,540"><ellipse cx="760" cy="540" rx="150" ry="70" fill="none" stroke="{ACC}" stroke-width="7" stroke-dasharray="20 12"/></g>']
        b += [line(910, 520, 1300, 360, INK, 5, .6), ico("check", 1380, 330, 120, INK), line(910, 560, 1300, 720, INK, 5, .4), dust(1400, 760, 200, 120, 30, seed=31, op=.4)]
    # ---------------------------------------------------------------- RETO 4 — Ayuno
    elif n == 32:
        b += [floor_line(), big_num("4", 1440, 360), table(1120, 700, 340), ico("plate", 1120, 680, 140, INK, .8)]
        b += [chair(820, FLOOR, 1.12), figure(830, FLOOR, 1.12, "sit", "determined", look=5)[0]]
    elif n == 33:
        b += [acc("firstaid", 1320, 440, 180), F(x=720, pose="stand", expr="calm", look=6)[0]]
    elif n == 34:
        b += [acc("medal", 1360, 420, 200), F(x=760, pose="stand", expr="thoughtful", look=6)[0]]
    elif n == 35:
        b += [acc("cell", 960, 520, 360), particles(960, 520, 300, 220, 30, seed=35, op=.7)]
    elif n == 36:
        b += [ico("cell", 960, 520, 420, INK, .9), particles(960, 520, 360, 260, 40, seed=36, op=.8)]
    elif n == 37:
        b += [ico("plate", 640, 560, 220, INK), line(780, 560, 1080, 560, ACC, 6, .9), acc("cell", 1260, 540, 240)]
    elif n == 38:
        b += [floor_line(), ico("pot", 1320, 640, 150, INK, .25, rot=-10), F(x=720, pose="explain", expr="determined", look=6)[0]]
    elif n == 39:
        b += [timeline(260, 800, 1700, 800, ticks=6, color=INK, w=4, op=.4), ico("pot", 420, 640, 120, INK, .5), ico("pot", 760, 640, 100, INK, .25), ico("pot", 1100, 640, 80, INK, .1)]
    elif n == 40:
        fig, an = F(x=760, pose="reach", expr="strain", look=6)
        hx, hy = an["rhand"]
        b += [fig, acc("cookie", hx + 200, hy, 100), line(hx + 40, hy, hx + 120, hy, INK, 4, .4, "6 8")]
    # ---------------------------------------------------------------- RETO 5 — Decir "No"
    elif n == 41:
        b += [floor_line(), big_num("5", 1360, 420), F(x=760, pose="stop", expr="determined", look=6)[0]]
    elif n == 42:
        b += [ico("envelope", 1300, 340, 140, INK, .7), ico("hand", 1500, 600, 130, INK, .6, rot=-90)]
        b += [acc("warning", 1380, 260, 50), acc("warning", 1580, 520, 50), F(x=700, pose="stand", expr="uneasy", look=6)[0]]
    elif n == 43:
        fig, an = F(x=860, pose="stand", expr="resigned", look=6)
        b += [fig, ico("task", an["sh"][0] + 240, an["sh"][1] + 40, 140, INK, .8), line(an["sh"][0] + 40, an["sh"][1] + 40, an["sh"][0] + 170, an["sh"][1] + 40, INK, 3, .5)]
    elif n == 44:
        b += [acc("check", 1320, 460, 200), F(x=720, pose="stand", expr="neutral", look=6)[0]]
    elif n == 45:
        b += [ico("task", 1440, 520, 200, INK, .25), acc("check", 1200, 460, 200), F(x=640, pose="stand", expr="neutral", look=6)[0]]
    elif n == 46:
        b += [acc("check", 560, 520, 180)] + [ico(nm, 960 + i * 260, 520, 150, INK, .35) for i, nm in enumerate(("clock", "bolt", "task"))]
    elif n == 47:
        b += [ico("cloud", 1360, 480, 160, INK, .2), F(x=760, pose="dismiss", expr="warm", look=6)[0]]
    elif n == 48:
        b += [ico("check", 1520, 260, 100, INK, .2), acc("compass", 1340, 460, 220, rot=-30), F(x=720, pose="stand", expr="determined", look=6)[0]]
    # ---------------------------------------------------------------- CIERRE
    elif n == 49:
        b += [floor_line(), num_arc(960, 610, 430, 210, 330, size=80), F(x=960, pose="stand", expr="determined")[0]]
    elif n == 50:
        b += [doors(960, 540, 470, n=6, closed=6, op=.5), F(x=960, pose="stand", expr="calm")[0]]
    elif n == 51:
        b += [F(x=600, pose="stand", expr="calm", look=6)[0], num_arc(1320, 760, 400, 200, 340, size=110)]
    elif n == 52:
        b += [acc("bubble", 1320, 360, 220), F(x=760, pose="point_you", expr="warm", look=3)[0]]
    elif n == 53:
        b += [floor_line(), acc("bell", 1260, 430, 150), F(x=860, pose="thumbs", expr="smile")[0]]
    elif n == 54:
        b += [rim(960, 500, 620), F(x=960, pose="stand", expr="serene")[0]]
    else:
        raise ValueError(n)
    return b


def thumb_b():
    """Mẫu B — triptych: silencio en una habitación vacía · cambiar la pulsera de muñeca · ayuno ante un plato vacío (vật nhấn)."""
    pw = TW / 3
    b = [panel_bg(0, 0, pw, TH, "#7FB8FF", .26), panel_bg(pw, 0, pw, TH, "#8C7BFF", .26), panel_bg(2 * pw, 0, pw, TH, "#FFB46B", .24)]
    b += [chair(200, 560, .9), figure(210, 560, .9, "sit", "uneasy", look=5)[0]]
    fig, an = figure(pw + pw / 2, 560, .95, "shrug", "uneasy")
    b += [fig, wristband(an["rhand"][0], an["rhand"][1] + 10, 46)]
    mid = 2 * pw + pw / 2
    b += [line(mid - 10, 420, mid + 190, 420, INK, 7), line(mid + 90, 420, mid + 90, 560, INK, 6), acc("plate", mid + 90, 400, 80, glow_r=100),
          chair(mid - 120, 560, .9), figure(mid - 110, 560, .9, "sit", "determined", look=5)[0]]
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 3}" y="0" width="6" height="{TH}" fill="#000"/>')
    b.append(badge())
    return b


def thumb_c():
    """Mẫu C — lưới 6 khung."""
    pw, ph = TW / 3, TH / 2
    tints = ("#7FB8FF", "#5AC8C8", "#8C7BFF", "#FFB46B", "#FF6B6B", "#FFD9A0")
    b = [panel_bg((i % 3) * pw, (i // 3) * ph, pw, ph, t, .22) for i, t in enumerate(tints)]
    s = .62
    b += [ico("wave", 213, 180, 160, INK, .6)]                                                                # 1 silencio
    b += [f'<rect x="490" y="70" width="300" height="250" fill="none" stroke="{INK}" stroke-width="4" opacity=".4"/>',
          chair(630, 320, .58), figure(640, 320, .58, "sit", "calm", look=5)[0]]                               # 2 soledad
    b += [line(980, 190, 1180, 190, INK, 24, .9), wristband(1080, 190, 90)]                                   # 3 pulsera
    b += [ico("plate", 300, 600, 100, INK, .8), figure(150, 690, s, "stand", "calm", look=6)[0]]              # 4 ayuno
    b += [figure(640, 458, .34, "stop", "determined", look=6)[0]]                                               # 5 decir no
    b += [f'<path d="M920,700 L1066,520 L1212,700" fill="none" stroke="{INK}" stroke-width="5"/>', figure(1066, 520, .45, "hands_hips", "satisfied")[0]]  # 6
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 1.5}" y="0" width="3" height="{TH}" fill="{BG}"/>')
    b.append(f'<rect x="0" y="{ph - 1.5}" width="{TW}" height="3" fill="{BG}"/>')
    b.append(badge())
    return b

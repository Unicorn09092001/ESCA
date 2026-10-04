# -*- coding: utf-8 -*-
"""
scenes.py — Kịch bản hình của project 25 "Detox Digital de 7 Días: Recupera Tu Cerebro del Scroll"
(45 khung + 2 thumbnail), bám theo [VISUAL DESCRIPTION] trong transcript_and_visuals.txt.
Màu nhấn #3BA7C9 (04_Productividad Practica).
Mô-típ: dải lịch 7 ô (tắt → ngày 1-2 nhấp nháy cam căng thẳng → ngày 5-7 sáng xanh ổn định) ·
bánh răng thiết kế sau màn hình · móc câu trong não · ngã ba đường · đường cong trũng rồi đi lên.
"""
from scenekit import *  # noqa: F401,F403
from sticklib import *  # noqa: F401,F403  (nạp lại ACC sau khi đã set_accent theo playlist)
from scenekit import FLOOR, bed, table
from thumbkit import TH, TW, badge, panel_bg

WARM = "#E8743B"   # ô ngày 1-2 "căng thẳng" (theo mô tả red-orange), dùng rất tiết chế


def tile(x, y, d, state="off", w=110, op=1.0, dot=None):
    """Một ô lịch ngày d. state: off · strain · dim · on."""
    h = w * 1.2
    col = {"off": INK, "strain": WARM, "dim": "#8FA9B5", "on": ACC}[state]
    o = {"off": .25, "strain": 1, "dim": .55, "on": 1}[state] * op
    out = ""
    if state == "on":
        out += glow(x, y, w * 1.1, "A", .7 * op)
    if state == "strain":
        out += f'<g opacity="{op}">' + "".join(
            f'<path d="M{x + (w * .7) * math.cos(math.radians(a)):.0f},{y + (h * .62) * math.sin(math.radians(a)):.0f} '
            f'l{10 * math.cos(math.radians(a + 40)):.0f},{10 * math.sin(math.radians(a + 40)):.0f} '
            f'l{10 * math.cos(math.radians(a - 40)):.0f},{10 * math.sin(math.radians(a - 40)):.0f}" '
            f'fill="none" stroke="{WARM}" stroke-width="3"/>' for a in range(0, 360, 45)) + "</g>"
    out += (f'<g opacity="{o:.2f}"><rect x="{x - w / 2:.0f}" y="{y - h / 2:.0f}" width="{w:.0f}" height="{h:.0f}" rx="12" fill="{BG}" stroke="{col}" stroke-width="5"/>'
            f'<line x1="{x - w / 2:.0f}" y1="{y - h / 2 + h * .26:.0f}" x2="{x + w / 2:.0f}" y2="{y - h / 2 + h * .26:.0f}" stroke="{col}" stroke-width="4"/>'
            f'<text x="{x:.0f}" y="{y + h * .32:.0f}" font-family="Anton" font-size="{w * .55:.0f}" fill="{col}" text-anchor="middle">{d}</text></g>')
    if state == "on":
        out = f'<g data-acc="{x:.0f},{y:.0f}">{out}</g>'
    if dot is not None:
        out = f'<g data-dot="{dot}">{out}</g>'
    return out


def strip(x0, x1, y, states, w=110, op=1.0, seq=False):
    n = len(states)
    return "".join(tile(x0 + (x1 - x0) * i / max(n - 1, 1), y, i + 1, st, w, op, dot=i if seq else None) for i, st in enumerate(states))


def gear_phone(x, y, size=200, glow_on=True):
    out = ico("phone", x, y, size, INK)
    g = ico("gear", x, y, size * .42, ACC)
    return out + (f'<g data-acc="{x},{y}">' + glow(x, y, size * .5, "A", .7) + g + "</g>" if glow_on else g)


def fork(cx=960, y0=905, back_lit=True, op=1.0):
    """Ngã ba: nhánh trái quay về điện thoại sáng, nhánh phải đi tiếp mờ."""
    return (
            f'<g opacity="{op}"><path d="M{cx},{y0} L{cx},{y0 - 160}" stroke="{INK}" stroke-width="6" fill="none" opacity=".6"/>'
            f'<path d="M{cx},{y0 - 160} Q{cx - 220},{y0 - 230} {cx - 460},{y0 - 380}" stroke="{INK}" stroke-width="6" fill="none" opacity=".7"/>'
            f'<path d="M{cx},{y0 - 160} Q{cx + 220},{y0 - 230} {cx + 460},{y0 - 380}" stroke="{INK}" stroke-width="5" fill="none" opacity=".2" stroke-dasharray="14 12"/></g>'
            + f'<g data-acc="{cx},{y0 - 160}">' + glow(cx, y0 - 160, 110, "A", .9) + f'<circle cx="{cx}" cy="{y0 - 160}" r="14" fill="{ACC}"/></g>'
            + (glow(cx - 470, y0 - 420, 120, "W", .6) if back_lit else "") + ico("phone", cx - 470, y0 - 420, 110, INK, .95 if back_lit else .5))


def dip_curve(x0=300, x1=1620, y=560, depth=220, op=.8, color=None, rise=True):
    color = color or INK
    xm = (x0 + x1) / 2
    end_y = y - 120 if rise else y
    return (f'<path d="M{x0},{y} C{x0 + 300},{y} {xm - 260},{y + depth} {xm},{y + depth} S{x1 - 300},{end_y} {x1},{end_y}" '
            f'fill="none" stroke="{color}" stroke-width="6" opacity="{op}" stroke-linecap="round"/>')


def pulse(x, y, size=60, strong=False):
    r = size * (1.6 if strong else 1)
    return (f'<g data-acc="{x:.0f},{y:.0f}">' + glow(x, y, r * 1.6, "A", .9)
            + f'<path d="M{x - r:.0f},{y:.0f} L{x - r * .4:.0f},{y:.0f} L{x - r * .2:.0f},{y - r * .6:.0f} L{x + r * .1:.0f},{y + r * .6:.0f} '
              f'L{x + r * .3:.0f},{y:.0f} L{x + r:.0f},{y:.0f}" fill="none" stroke="{ACC}" stroke-width="{6 if strong else 5}" stroke-linejoin="round"/></g>')


def build_layers(n, shot):
    F = lambda **kw: shot_fig(shot, **kw)  # noqa: E731
    b = []
    S7 = ["off"] * 7
    # ---------------------------------------------------------------- GANCHO
    if n == 1:
        b += [line(820, 760, 1700, 760, INK, 7, .6), glow(1090, 700, 120, "A", .35), ico("phone", 1090, 712, 130, INK, .9, rot=90)]
        fig, an = figure(560, 1250, 2.6, "reach", "attentive", look=6)
        b += [fig]
    elif n == 2:
        fig, an = F(x=760, pose="hunch", expr="distracted", look=5)
        hx, hy = an["rhand"]
        b += [fig, gear_phone(hx + 20, hy - 40, 140)]
    elif n == 3:
        b += [floor_line(), strip(560, 1640, 420, S7, 105, seq=True), F(x=330, pose="stand", expr="thoughtful", look=6)[0]]
    elif n == 4:
        fig, an = F(x=960, pose="stand", expr="attentive")
        tx, ty = an["top"]
        b += [fig, acc("brain", tx, ty - 120, 160)]
        b += [line(tx + math.cos(a) * 120, ty - 120 + math.sin(a) * 100, tx + math.cos(a) * 190, ty - 120 + math.sin(a) * 150, ACC, 4, .6)
              for a in (math.radians(d) for d in (200, 240, 300, 340))]
    elif n == 5:
        b += [floor_line(), strip(520, 1680, 380, ["strain", "strain", "off", "off", "off", "off", "on"], 100),
              F(x=760, pose="walk", expr="determined", look=6)[0]]
    # ---------------------------------------------------------------- M1 — Días 1 y 2 (Adam Alter)
    elif n == 6:
        b += [tile(820, 500, 1, "strain", 190), tile(1100, 500, 2, "strain", 190)]
    elif n == 7:
        b += [ico("campus", 1560, 300, 160, INK, .25), acc("book", 1260, 500, 230, progress=0), F(x=680, pose="explain", expr="calm", look=6)[0]]
    elif n == 8:
        b += [gear_phone(960, 500, 420)]
    elif n == 9:
        b += [ico("slot", 560, 500, 260, INK), ico("phone", 1360, 500, 260, INK), ico("gear", 1360, 500, 90, INK, .8)]
        b += [f'<g data-acc="960,500">' + glow(960, 500, 200, "A", .8) + f'<g data-flow="1"><line x1="720" y1="500" x2="1220" y2="500" stroke="{ACC}" stroke-width="7" stroke-dasharray="8 20" stroke-linecap="round"/></g></g>']
    elif n == 10:
        fig, an = F(x=760, pose="hunch", expr="attentive", look=6)
        hx, hy = an["rhand"]
        b += [fig, ico("phone", hx + 14, hy - 20, 90, INK), f'<rect x="1160" y="260" width="140" height="110" rx="14" fill="none" stroke="{INK}" stroke-width="5" opacity=".3"/>',
              acc("star", 1560, 315, 110), ico("question", 1430, 320, 90, INK, .6)]
    elif n == 11:
        b += [ico("brain", 960, 480, 420, INK, .9), acc("hook", 1060, 420, 170)]
    elif n == 12:
        for i, o in enumerate((.2, .4, 1.0)):
            fig, an = F(x=760 + i * 60, pose="reach", expr="distracted", look=6, op=o)
            b += [fig]
        b += [table(1340, 760, 320), ico("phone", 1340, 738, 70, INK, .8, rot=90)]
        b += [line(1000, 500 + i * 40, 1120, 500 + i * 40, INK, 3, .3) for i in range(3)]
    elif n == 13:
        b += [strip(1300, 1700, 230, ["strain", "strain"], 90)]
        fig, an = F(x=760, pose="stand", expr="uneasy", look=6)
        b += [fig, pulse(an["rhand"][0] + 40, an["rhand"][1], 50)]
    elif n == 14:
        b += [floor_line(), strip(1300, 1700, 330, ["strain", "strain"], 110, op=.7), F(x=820, pose="stand", expr="determined")[0]]
    elif n == 15:
        b += [floor_line(), f'<g data-acc="1360,430">' + glow(1360, 430, 330, "A", .5) + ico("gear", 1360, 430, 440, ACC, .8) + "</g>",
              ico("phone", 1360, 700, 110, INK), F(x=640, pose="stand", expr="realize", look=6)[0]]
    # ---------------------------------------------------------------- M2 — Días 3 y 4
    elif n == 16:
        b += [tile(820, 470, 3, "dim", 190), tile(1100, 470, 4, "dim", 190), ico("arrow", 960, 760, 110, INK, .6, rot=90)]
    elif n == 17:
        b += [fork(1100), F(x=1100, pose="stand", expr="uneasy", look=0, floor=FLOOR)[0]] if shot != "CLOSE-UP" else [fork(1100)]
    elif n == 18:
        fig, an = F(x=960, pose="stand", expr="resigned")
        hx, hy = an["head"]
        b += [fig] + [ico("burst", hx + dx, hy + dy, 70, INK, .5) for dx, dy in ((-260, -120), (250, -140), (-280, 120), (270, 100))]
    elif n == 19:
        fig, an = F(x=760, pose="stand", expr="uneasy", look=6)
        b += [fig, pulse(an["rhand"][0] + 60, an["rhand"][1], 60, strong=True), ico("phone", 1460, 560, 120, INK, .6)]
    elif n == 20:
        b += [dip_curve(260, 1660, 420, 260), tile(890, 680, 3, "dim", 80), tile(1030, 680, 4, "dim", 80),
              f'<path d="M1500,360 L1640,300" stroke="{ACC}" stroke-width="6" stroke-dasharray="10 12"/>']
    elif n == 21:
        b += [dip_curve(300, 1620, 640, 150, .25)]
        b += [f'<g data-dot="{i}">' + ico(nm, 640 + i * 320, 380, 150, INK, .75 - i * .22) + "</g>" for i, nm in enumerate(("star", "bell", "heart"))]
    elif n == 22:
        b += [f'<ellipse cx="960" cy="500" rx="{220 + i * 70}" ry="{180 + i * 56}" fill="none" stroke="{INK}" stroke-width="3" opacity="{.35 - i * .07:.2f}"/>' for i in range(4)]
        b += [acc("brain", 960, 500, 300)]
    elif n == 23:
        b += [fork(1100, back_lit=True), F(x=820, pose="walk", expr="resigned", look=4)[0]]
    elif n == 24:
        b += [f'<path d="M300,880 Q900,700 1500,420" stroke="{INK}" stroke-width="5" fill="none" opacity=".2" stroke-dasharray="14 12"/>',
              strip(1440, 1720, 330, ["off", "off", "off"], 70, op=.6)]
        b += [dust(1500, 400, 400, 200, 20, seed=24, op=.15)]
    # ---------------------------------------------------------------- M3 — Días 5, 6, 7 (Melissa Hunt)
    elif n == 25:
        b += [tile(700 + i * 260, 480, 5 + i, "on", 180) for i in range(3)]
    elif n == 26:
        b += [ico("bank", 1600, 290, 150, INK, .25), acc("document", 1260, 500, 220), F(x=680, pose="explain", expr="calm", look=6)[0]]
    elif n == 27:
        b += [ico("clock", 620, 480, 280, INK),
              f'<g data-acc="620,480">' + glow(620, 480, 200, "A", .7) + f'<path d="M620,480 L620,{480 - 100} A100,100 0 0 1 {620 + 100},480 Z" fill="{ACC}" opacity=".55"/></g>']
        b += [f'<g data-dot="{i}">' + ico("calendar", 1080 + i * 220, 480, 140, INK, .6) + f'<text x="{1080 + i * 220}" y="600" font-family="Anton" font-size="50" fill="{INK}" opacity=".6" text-anchor="middle">{i + 1}</text></g>'
              for i in range(3)]
    elif n == 28:
        for j, (nm, x) in enumerate((("person", 640), ("cloud", 1280))):
            b += [ico(nm, x - 200, 300, 110, INK, .6)]
            b += [f'<rect x="{x - 130 + i * 90}" y="{760 - v}" width="60" height="{v}" rx="6" fill="none" stroke="{INK}" stroke-width="4" opacity=".6"/>'
                  for i, v in enumerate((360, 290, 210, 140))]
            b += [f'<g data-acc="{x + 50},{450}">' + f'<path d="M{x - 110},{380} L{x + 230},{620}" stroke="{ACC}" stroke-width="7" stroke-linecap="round"/>'
                  + f'<path d="M{x + 200},{580} L{x + 236},{626} L{x + 180},{628}" fill="none" stroke="{ACC}" stroke-width="7" stroke-linejoin="round"/></g>']
    elif n == 29:
        b += [line(220, 820, 1700, 820, INK, 4, .4), line(660, 300, 660, 840, INK, 3, .3, "8 10")]
        b += [f'<path d="M220,460 L1700,460" stroke="{INK}" stroke-width="6" opacity=".4"/>',
              f'<g data-acc="1200,600">' + glow(1300, 650, 220, "A", .6) + f'<path d="M220,470 L660,500 Q900,560 1200,650 L1700,720" stroke="{ACC}" stroke-width="7" fill="none" stroke-linecap="round"/></g>']
    elif n == 30:
        b += [strip(420, 960, 400, ["on"] * 7, 64)]
        b += ["".join(tile(300 + 60 * (i % 21), 680, "", "dim", 46, .7) for i in range(21))]
        b += [f'<path d="M1180,360 C1380,360 1500,320 1700,220" stroke="{INK}" stroke-width="4" fill="none" opacity=".35"/>',
              f'<circle cx="1360" cy="350" r="14" fill="{ACC}"/>', f'<circle cx="1690" cy="226" r="10" fill="{INK}" opacity=".5"/>']
    elif n == 31:
        b += [ico("brain", 840, 480, 400, INK, .9), f'<g data-acc="1240,600">' + glow(1240, 600, 200, "A", .5) + ico("hook", 1250, 640, 150, ACC, .8, rot=30) + "</g>",
              line(1020, 470, 1140, 560, INK, 3, .3, "6 10")]
    elif n == 32:
        fig, an = F(x=880, pose="stand", expr="serene", look=6)
        hx, hy = an["head"]
        b += [fig, f'<g data-acc="{hx + 500:.0f},{hy:.0f}">' + glow(hx + 520, hy, 160, "A", .6)
              + f'<line x1="{hx + 120:.0f}" y1="{hy:.0f}" x2="{hx + 700:.0f}" y2="{hy:.0f}" stroke="{ACC}" stroke-width="5" stroke-dasharray="4 16" stroke-linecap="round"/></g>',
              ico("phone", 1720, 920, 80, INK, .35, rot=90)]
    # ---------------------------------------------------------------- M4 — Qué hacer en su lugar
    elif n == 33:
        b += [strip(400, 1520, 560, ["on"] * 7, 120)]
        b += [ico(nm, 400 + 1120 * i / 6, 360, 70, INK, .4) for i, nm in enumerate(("shoe", "call", "book", "shoe", "call", "book", "lamp"))]
    elif n == 34:
        b += [floor_line(), table(1300, 760, 340), ico("phone", 1300, 738, 70, INK, .8, rot=90), F(x=760, pose="stand", expr="calm", look=6)[0]]
    elif n == 35:
        b += [ico("phone", 620, 500, 200, INK, .2), arrow_r(760, 860, 500) if False else line(740, 500, 840, 500, INK, 3, .3, "6 10"),
              f'<rect x="880" y="330" width="200" height="340" rx="30" fill="none" stroke="{INK}" stroke-width="5" stroke-dasharray="16 12" opacity=".7"/>',
              acc("clipboard", 1180, 380, 150, rows=2), f'<path d="M1110,420 Q1040,460 1000,480" stroke="{ACC}" stroke-width="4" fill="none" stroke-dasharray="8 10"/>']
    elif n == 36:
        b += [floor_line(), line(960, 260, 960, 880, INK, 3, .15)]
        b += [figure(500, FLOOR, 1.0, "walk", "serene", look=6)[0], ico("signpost", 200, 760, 120, INK, .35)]
        fig, an = figure(1400, FLOOR, 1.0, "stand", "smile", look=5)
        b += [fig, acc("call", an["head"][0] + 70, an["head"][1] + 10, 80)]
    elif n == 37:
        b += [bed(380, 1100, 820), table(1350, 820, 260), acc("book", 1310, 780, 110, progress=0),
              ico("phone", 1430, 805, 56, INK, .5, rot=90), ico("lamp", 1450, 640, 150, INK, .8), glow(1450, 640, 260, "warm", .9)]
    elif n == 38:
        b += [strip(380, 1340, 480, ["on"] * 7, 110), tile(1600, 480, 8, "off", 110, .6), line(1420, 480, 1520, 480, INK, 3, .3, "6 10")]
    elif n == 39:
        b += [F(x=760, pose="stand", expr="calm", look=6)[0]]
        b += [ico(nm, x, y, s, INK, o) for nm, x, y, s, o in (("star", 1240, 440, 110, .6), ("hand", 1420, 320, 100, .45), ("star", 1580, 210, 80, .3), ("hand", 1720, 130, 60, .18))]
        b += [particles(1460, 300, 400, 300, 16, seed=39, color=INK, op=.3)]
    elif n == 40:
        b += [floor_line(), table(1300, 760, 340), f'<g data-acc="1300,560">' + glow(1300, 560, 260, "A", .5) + ico("gear", 1300, 560, 260, ACC, .5) + "</g>",
              glow(1300, 730, 90, "W", .8), ico("phone", 1300, 738, 70, INK, 1, rot=90), F(x=620, pose="stand", expr="attentive", look=6)[0]]
    # ---------------------------------------------------------------- CIERRE
    elif n == 41:
        b += [floor_line(), strip(780, 1700, 430, ["on"] * 7, 110), F(x=440, pose="stand", expr="calm", look=6)[0]]
    elif n == 42:
        b += [ico("brain", 960, 580, 340, INK, .9), acc("compass", 960, 280, 140)]
    elif n == 43:
        b += [strip(1100, 1700, 760, ["on"] * 7, 60, op=.5), acc("bubble", 1320, 380, 180), F(x=640, pose="point_you", expr="warm", look=3)[0]]
    elif n == 44:
        b += [floor_line(), F(x=860, pose="stand", expr="serene")[0], acc("bell", 1620, 200, 90), acc("hand", 1780, 200, 80)]
    elif n == 45:
        b += [floor_line(), strip(300, 1000, 300, ["on"] * 7, 70, op=.45), table(1440, 760, 300), ico("phone", 1440, 738, 70, INK, .5, rot=90),
              F(x=900, pose="walk", expr="serene", look=-6)[0]]
    else:
        raise ValueError(n)
    return b


def thumb_b():
    """Mẫu B — triptych: caminar sin teléfono · llamada real · libro físico junto a la cama (vật nhấn)."""
    pw = TW / 3
    b = [panel_bg(0, 0, pw, TH, "#5AC8A0", .24), panel_bg(pw, 0, pw, TH, "#FFB46B", .24), panel_bg(2 * pw, 0, pw, TH, "#8C7BFF", .24)]
    b += [figure(pw / 2, 560, .95, "walk", "serene", look=6)[0], ico("sun", pw / 2 + 120, 140, 70, INK, .5)]
    fig, an = figure(pw + pw / 2, 560, .95, "stand", "smile", look=5)
    b += [fig, ico("call", an["head"][0] + 70, an["head"][1] + 10, 70, INK)]
    x3 = 2 * pw + pw / 2
    fig, an = figure(x3 - 60, 560, .95, "sit", "calm", look=6)
    b += [chair(x3 - 70, 560, .95), fig, acc("book", an["rhand"][0] + 40, an["rhand"][1] - 30, 90, progress=0),
          table(x3 + 150, 560, 110), ico("phone", x3 + 150, 548, 36, INK, .5, rot=90),
          glow(x3 + 160, 340, 160, "warm", .8), ico("lamp", x3 + 160, 360, 90, INK, .8)]
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 3}" y="0" width="6" height="{TH}" fill="#000"/>')
    b.append(badge())
    return b


def thumb_c():
    """Mẫu C — lưới 6 khung."""
    pw, ph = TW / 3, TH / 2
    tints = ("#FFB46B", "#FF6B6B", "#7FB8FF", "#5AC8A0", "#8C7BFF", "#FFD9A0")
    b = [panel_bg((i % 3) * pw, (i // 3) * ph, pw, ph, t, .22) for i, t in enumerate(tints)]
    b += [glow(213, 180, 150, "A", .7), ico("slot", 213, 180, 170, ACC)]                                           # 1 diseño del enganche
    fig, an = figure(600, 320, .58, "hunch", "uneasy", look=5)
    b += [fig, ico("phone", an["rhand"][0] + 8, an["rhand"][1] - 14, 46, INK), pulse(an["rhand"][0] + 60, an["rhand"][1] - 50, 26)]  # 2 impulso
    b += [chair(990, 320, .58), figure(1000, 320, .58, "sit", "resigned", look=5)[0], ico("phone", 1150, 300, 40, INK, .5, rot=90)]  # 3 caída
    b += [figure(120, 460, .34, "stand", "calm", look=6)[0], acc("book", 260, 410, 70, progress=0)]                   # 4 cambio real
    b += [ico("road", 560, 420, 80, INK, .7), ico("book", 720, 420, 70, INK, .7, progress=0)]                         # 5 qué hacer
    b += [ico("sun", 1200, 410, 60, INK, .5), figure(1070, 500, .4, "hands_hips", "satisfied")[0]]                    # 6 cierre
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 1.5}" y="0" width="3" height="{TH}" fill="{BG}"/>')
    b.append(f'<rect x="0" y="{ph - 1.5}" width="{TW}" height="3" fill="{BG}"/>')
    b.append(badge())
    return b

# -*- coding: utf-8 -*-
"""
scenes.py — Kịch bản hình của project 16 "Tu Entorno Decide Antes Que Tu Fuerza de Voluntad"
(35 khung + 2 thumbnail), bám theo [VISUAL DESCRIPTION] trong transcript_and_visuals.txt.
Màu nhấn #FF5A36 (01_Disciplina y Habitos).
"""
from scenekit import *  # noqa: F401,F403
from sticklib import *  # noqa: F401,F403  (nạp lại ACC sau khi đã set_accent theo playlist)
from scenekit import FLOOR, mirror, table, timeline
from thumbkit import TH, TW, badge, panel_bg


def shelf(cx, cy, w=560, rows=3, gap=150, op=1.0, color=None):
    """Kệ đơn giản: khung + các tầng ngang. Trả về (svg, danh sách y của mặt từng tầng)."""
    color = color or INK
    top = cy - gap * rows / 2
    out = [f'<g opacity="{op}">',
           f'<line x1="{cx - w / 2}" y1="{top - 20}" x2="{cx - w / 2}" y2="{top + gap * rows}" stroke="{color}" stroke-width="8" stroke-linecap="round"/>',
           f'<line x1="{cx + w / 2}" y1="{top - 20}" x2="{cx + w / 2}" y2="{top + gap * rows}" stroke="{color}" stroke-width="8" stroke-linecap="round"/>']
    ys = []
    for r in range(rows):
        y = top + gap * (r + 1)
        ys.append(y)
        out.append(f'<line x1="{cx - w / 2}" y1="{y}" x2="{cx + w / 2}" y2="{y}" stroke="{color}" stroke-width="8" stroke-linecap="round"/>')
    out.append("</g>")
    return "".join(out), ys


def tension(x, y, r=260, n=10, op=.6):
    """Các vạch căng thẳng quanh nhân vật."""
    out = []
    for i in range(n):
        a = math.radians(360 * i / n + 12)
        x0, y0 = x + r * math.cos(a), y + r * .9 * math.sin(a)
        x1, y1 = x + (r + 40) * math.cos(a), y + (r + 40) * .9 * math.sin(a)
        out.append(line(x0, y0, x1, y1, INK, 5, op))
    return "".join(out)


def theater(cx, cy, w=900, op=1.0, glow_screen=True):
    out = [f'<g opacity="{op}">']
    if glow_screen:
        out.append(glow(cx, cy - 200, w * .5, "W", 1))
    out.append(f'<rect x="{cx - w / 2}" y="{cy - 330}" width="{w}" height="250" rx="8" fill="none" stroke="{INK}" stroke-width="7"/>')
    out.append("</g>")
    return "".join(out)


def stocked(cx, ys, items, op=1.0):
    """Đặt icon lên các tầng kệ: items = [(tầng, dx, tên, màu, cỡ, op), ...]."""
    out = []
    for r, dx, nm, col, sz, o in items:
        y = ys[r] - sz * .48
        if col == ACC:
            out.append(acc(nm, cx + dx, y, sz, op=o * op))
        else:
            out.append(ico(nm, cx + dx, y, sz, col, o * op))
    return "".join(out)


def build_layers(n, shot):
    F = lambda **kw: shot_fig(shot, **kw)  # noqa: E731
    b = []
    # ---------------------------------------------------------------- ESCENA 1: EL GANCHO
    if n == 1:
        fig, an = F(x=760, pose="push", expr="strain", look=6, tilt=-6)
        b += [floor_line(), tension(an["head"][0] + 30, an["hip"][1] - 120, 300), fig, acc("cookie", 1300, 560, 170)]
    elif n == 2:
        fig, an = F(x=960, pose="hunch", expr="sad")
        tx, ty = an["top"]
        for i, dx in enumerate((-260, 0, 260)):
            b += [ico("tag", tx + dx, ty - 120, 130, INK, .4), acc("xmark", tx + dx, ty - 120, 100, w=8)]
        b += [fig]
    elif n == 3:
        b += [floor_line(), rim(960, 520, 520), F(x=960, pose="stand", expr="neutral")[0]]
    elif n == 4:
        sh, _ = shelf(380, 560, 340, rows=3, gap=120, op=.25)
        b += [sh, acc("battery", 1360, 400, 180, level=.3), F(x=860, pose="point", expr="determined", look=6)[0]]
    elif n == 5:
        sh, ys = shelf(1240, 560, 620, rows=3, gap=150)
        b += [floor_line(), glow(1240, 540, 460, "A", .8), sh,
              stocked(1240, ys, [(0, -180, "drop", INK, 80, .9), (1, 0, "apple", INK, 90, .9), (2, 180, "books", INK, 90, .9)])]
        b += [figure(520, FLOOR, 1.0, "stand", "calm", look=6)[0]]
    # ---------------------------------------------------------------- ESCENA 2: CAFETERÍA (Thorndike)
    elif n == 6:
        b += [acc("battery", 960, 520, 360, level=.08)]
    elif n == 7:
        b += [acc("hospital", 1260, 400, 220), ico("tray", 1500, 700, 170, INK, .85)]
        b += [F(x=700, pose="explain", expr="calm", look=6)[0]]
    elif n == 8:
        sh, ys = shelf(900, 560, 700, rows=3, gap=160)
        b += [sh, stocked(900, ys, [(0, -220, "soda", INK, 80, .9), (0, -60, "drop", INK, 80, .9), (1, 120, "soda", INK, 80, .9),
                                    (2, -200, "drop", INK, 80, .9), (2, 200, "soda", INK, 80, .9)])]
        b += [acc("hand", 1080, ys[1] - 70, 110, rot=-20), ico("tag", 1500, 420, 130, INK, .6), ico("xmark", 1500, 420, 100, INK, .6)]
    elif n == 9:
        sh, ys = shelf(960, 560, 760, rows=3, gap=160)
        b += [sh, stocked(960, ys, [(0, 0, "drop", ACC, 130, 1), (1, -150, "drop", INK, 80, .7), (1, 150, "drop", INK, 80, .7),
                                    (2, 320, "soda", INK, 60, .25), (2, 250, "soda", INK, 60, .2)])]
    elif n == 10:
        b += [place(760, 480, 300, icon("bars", ACC, 7, vals=(.25, .45, .65, .9))), glow(760, 480, 260, "A", .6)]
        b += [place(1260, 480, 300, icon("bars", INK, 7, vals=(.9, .65, .45, .25))), ico("drop", 760, 230, 70, INK, .8), ico("soda", 1260, 230, 70, INK, .8)]
        b += [ico("page", 860 + i * 70, 820, 60, INK, .45) for i in range(4)]
    elif n == 11:
        b += [floor_line(), ico("megaphone", 760, 520, 230, INK, .35), ico("xmark", 760, 520, 200, INK, .5)]
        b += [place(1320, 560, 240, icon("bars", ACC, 7, vals=(.25, .45, .65, .9))), glow(1320, 560, 200, "A", .6)]
    elif n == 12:
        sh, ys = shelf(1300, 600, 520, rows=2, gap=170)
        b += [floor_line(), sh, stocked(1300, ys, [(0, -120, "drop", ACC, 110, 1), (0, 120, "drop", INK, 80, .7), (1, 160, "soda", INK, 60, .25)])]
        b += [figure(x, FLOOR, .85, "reach", "calm", look=6, op=o)[0] for x, o in ((520, .45), (760, .7), (980, 1.0))]
    # ---------------------------------------------------------------- ESCENA 3: EL HÁBITO AUTOMÁTICO (Wood / Neal)
    elif n == 13:
        b += [ico("theater", 860, 520, 360, INK, .75), acc("popcorn", 1260, 600, 170)]
    elif n == 14:
        b += [ico("campus", 1260, 420, 240, INK, .85), ico("document", 1520, 640, 130, INK, .7)]
        b += [F(x=680, pose="explain", expr="thoughtful", look=6)[0]]
    elif n == 15:
        b += [theater(960, 560, 1100)]
        for x in (560, 760, 1160, 1360):
            b += [figure(x, 960, .8, "sit", "neutral", op=.35, ghost=True)[0]]
        b += [acc("popcorn", 860, 780, 120), ico("popcorn", 1260, 780, 120, INK, .3)]
    elif n == 16:
        b += [theater(960, 560, 1100, op=.6)]
        b += [figure(640, FLOOR, 1.1, "sit", "neutral", look=6)[0], mirror(figure(1280, FLOOR, 1.1, "sit", "neutral", look=6)[0], 1280)]
        b += [ico("popcorn", 820, 700, 110, INK, .35), ico("popcorn", 1100, 700, 110, INK, .9)]
        b += [f'<g data-acc="960,640">' + line(925, 625, 995, 625, ACC, 9) + line(925, 655, 995, 655, ACC, 9) + "</g>"]
    elif n == 17:
        b += [ico("utensils", 640, 520, 260, INK, .3), ico("hand", 1300, 520, 230, INK, .9)]
        b += [line(780, 520, 920, 520, ACC, 8), line(1010, 520, 1150, 520, ACC, 8), crack(930, 470, 1000, 580, seed=17, w=5)]
    elif n == 18:
        b += [theater(960, 560, 1200, op=.5), ico("utensils", 380, 760, 110, INK, .15)]
        b += [acc("wave", 760, 380, 140), acc("moon", 1160, 380, 130)]
        b += [line(780, 460, 920, 680, INK, 4, .5, "10 10"), line(1140, 460, 1000, 680, INK, 4, .5, "10 10"), ico("hand", 960, 770, 150, INK, .9)]
    elif n == 19:
        b += [ico("moon", 500, 560, 170, INK, .9), ico("brain", 960, 260, 150, INK, .25)]
        b += [f'<path d="M560,480 Q960,200 1360,480" fill="none" stroke="{INK}" stroke-width="4" stroke-dasharray="10 12" opacity=".25"/>']
        b += [f'<g data-acc="960,560">' + glow(960, 560, 300, "A", .5) + line(620, 560, 1260, 560, ACC, 10)
              + place(1270, 560, 80, icon("arrow", ACC, 10)) + "</g>", ico("hand", 1460, 560, 170, INK, .9)]
    # ---------------------------------------------------------------- ESCENA 4: QUÉ HACER EN LA PRÁCTICA
    elif n == 20:
        sh, ys = shelf(960, 560, 600, rows=2, gap=200, color=ACC)
        b += [glow(960, 520, 420, "A", .6), sh, ico("apple", 840, ys[1] - 50, 90, INK, .9), ico("cookie", 1120, ys[0] - 45, 80, INK, .4)]
        b += [f'<path d="M1120,{ys[0] - 100} Q1300,{ys[0] + 40} 900,{ys[1] - 120}" fill="none" stroke="{INK}" stroke-width="5" stroke-dasharray="12 10" opacity=".7"/>']
    elif n == 21:
        b += [floor_line(), ico("cookie", 1500, 640, 100, INK, .25), F(x=760, pose="stand", expr="calm", look=6)[0]]
    elif n == 22:
        b += [timeline(260, 760, 1700, 760, ticks=3, color=INK, w=5, op=.5)]
        b += [acc("hand", 520, 560, 130, rot=-20), ico("battery", 520, 380, 120, INK, level=1)]
        b += [ico("cookie", 1440, 600, 110, INK, .35), ico("battery", 1440, 380, 120, INK, .3, level=.15)]
    elif n == 23:
        sh, ys = shelf(1260, 520, 640, rows=3, gap=170)
        b += [floor_line(), sh, ico("books", 1400, ys[0] - 45, 90, INK, .7), ico("cookie", 1440, ys[0] - 40, 70, INK, .3),
              acc("apple", 1160, ys[2] - 50, 110)]
        b += [F(x=620, pose="stand", expr="calm", look=6)[0]]
    elif n == 24:
        b += [f'<rect x="200" y="640" width="560" height="44" rx="10" fill="none" stroke="{INK}" stroke-width="8"/>',
              line(200, 580, 200, 905, INK, 8), line(760, 660, 760, 905, INK, 8), acc("tshirt", 880, 760, 150)]
        b += [line(960, 200, 960, 900, INK, 3, .2), table(1460, 700, 380), ico("drawer", 1460, 790, 170, INK), ico("remote", 1460, 807, 34, INK, .3, rot=90)]
    elif n == 25:
        b += [floor_line()]
        for x in (700, 1220):
            fig, an = figure(x, FLOOR, 1.12, "stand", "neutral", look=4)
            b += [fig, ico("battery", x, an["top"][1] - 80, 110, INK, .8, level=.6)]
    elif n == 26:
        b += [f'<g data-acc="1100,600">' + glow(1100, 600, 420, "A", .5)
              + f'<path d="M560,880 C900,880 1000,520 1520,420" fill="none" stroke="{ACC}" stroke-width="14" stroke-linecap="round"/></g>']
        b += [ico("target", 1600, 400, 150, INK), figure(480, FLOOR, 1.0, "walk", "calm", look=6)[0]]
    # ---------------------------------------------------------------- ESCENA 5: LA TRAMPA
    elif n == 27:
        sh, ys = shelf(960, 540, 600, rows=2, gap=190)
        b += [sh, stocked(960, ys, [(0, -120, "drop", INK, 80, .9), (1, 120, "apple", INK, 90, .9)]), acc("warning", 1310, 360, 110)]
    elif n == 28:
        sh, ys = shelf(760, 540, 520, rows=2, gap=190)
        b += [sh, stocked(760, ys, [(0, -100, "drop", INK, 80, .9), (1, 100, "apple", INK, 90, .9)])]
        b += [ico("calendar", 1360 + i * 90, 400 + i * 20, 120, INK, .25 + i * .15, crossed=4 * (i + 1)) for i in range(3)]
    elif n == 29:
        sh, ys = shelf(960, 560, 700, rows=3, gap=160)
        b += [glow(960, 540, 420, "A", .25), sh, stocked(960, ys, [(0, -200, "drop", INK, 80, .6), (1, 0, "apple", INK, 90, .5), (2, 200, "books", INK, 90, .4)])]
        b += [f'<rect x="580" y="300" width="760" height="520" rx="20" fill="none" stroke="{ACC}" stroke-width="5" stroke-dasharray="20 14" opacity=".35"/>']
    elif n == 30:
        b += [line(320, 640, 680, 640, INK, 8), ico("cookie", 500, 590, 90, INK, .9)]
        b += [f'<rect x="760" y="600" width="380" height="36" rx="10" fill="none" stroke="{INK}" stroke-width="7"/>', ico("phone", 1050, 560, 80, INK, .9, rot=-10)]
        sh, ys = shelf(1520, 560, 360, rows=2, gap=140)
        b += [sh, ico("cookie", 1450, ys[0] - 35, 60, INK, .8), ico("soda", 1580, ys[1] - 35, 60, INK, .8), acc("discount", 1520, 330, 110)]
    elif n == 31:
        sh, ys = shelf(860, 560, 640, rows=3, gap=160)
        b += [sh, stocked(860, ys, [(0, -200, "cookie", INK, 70, .8), (0, 0, "soda", INK, 70, .8), (0, 180, "phone", INK, 60, .7),
                                    (1, -120, "cookie", INK, 70, .7), (1, 160, "discount", INK, 70, .6), (2, -60, "soda", INK, 70, .7), (2, 200, "cookie", INK, 70, .7)])]
        b += [f'<rect x="1360" y="300" width="300" height="300" rx="20" fill="none" stroke="{ACC}" stroke-width="5" stroke-dasharray="14 12"/>', acc("calcheck", 1510, 450, 170)]
    # ---------------------------------------------------------------- ESCENA 6: EL CIERRE
    elif n == 32:
        fig, an = F(x=960, pose="stand", expr="serene")
        b += [floor_line(), fig, acc("battery", 960, an["top"][1] - 110, 150, level=1)]
    elif n == 33:
        b += [acc("bubble", 1320, 360, 220), F(x=760, pose="point_you", expr="warm", look=3)[0]]
    elif n == 34:
        b += [floor_line(), table(1300, 700, 360), acc("cookie", 1300, 650, 90)]
        fig, an = F(x=720, pose="think", expr="thoughtful", look=6)
        b += [fig, ico("thought", an["top"][0] + 230, an["top"][1] - 60, 160, INK, .7, inner=False), ico("cookie", an["top"][0] + 230, an["top"][1] - 66, 50, INK, .7)]
    elif n == 35:
        sh, ys = shelf(1440, 540, 460, rows=3, gap=140, op=.6)
        b += [floor_line(), glow(1440, 520, 360, "W", 1), sh,
              stocked(1440, ys, [(0, -100, "drop", INK, 70, .7), (1, 80, "apple", INK, 80, .7), (2, -60, "books", INK, 80, .7)])]
        b += [F(x=780, pose="stand", expr="serene", look=4)[0], acc("bell", 1720, 170, 90), acc("check", 1600, 170, 80)]
    else:
        raise ValueError(n)
    return b


def thumb_b():
    """Mẫu B — triptych: fruta a la vista / galletas arriba · ropa lista junto a la cama · control remoto al cajón (vật nhấn)."""
    pw = TW / 3
    b = [panel_bg(0, 0, pw, TH, "#FFB46B", .26), panel_bg(pw, 0, pw, TH, "#7FB8FF", .24), panel_bg(2 * pw, 0, pw, TH, "#8C7BFF", .2)]
    # 1: cocina
    b += [line(200, 160, 400, 160, INK, 6), ico("cookie", 330, 125, 60, INK, .45), line(170, 420, 400, 420, INK, 6), ico("apple", 260, 385, 70, INK)]
    b += [figure(110, 560, .9, "reach", "calm", look=6)[0]]
    # 2: ropa junto a la cama
    b += [f'<rect x="{pw + 170}" y="430" width="230" height="36" rx="10" fill="none" stroke="{INK}" stroke-width="7"/>',
          line(pw + 170, 380, pw + 170, 560, INK, 7), line(pw + 400, 450, pw + 400, 560, INK, 7), ico("tshirt", pw + 290, 395, 80, INK)]
    b += [figure(pw + 90, 560, .9, "reach_down", "determined", look=6)[0]]
    # 3: control remoto al cajón — vật nhấn
    mid = 2 * pw + pw / 2
    b += [ico("drawer", mid + 90, 470, 150, INK), acc("remote", mid + 90, 380, 70, glow_r=100)]
    b += [figure(mid - 110, 560, .9, "reach", "satisfied", look=6)[0]]
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 3}" y="0" width="6" height="{TH}" fill="#000"/>')
    b.append(badge())
    return b


def thumb_c():
    """Mẫu C — lưới 6 khung."""
    pw, ph = TW / 3, TH / 2
    tints = ("#5AC8C8", "#8C7BFF", "#FFB46B", "#7FB8FF", "#FF6B6B", "#FFD9A0")
    b = [panel_bg((i % 3) * pw, (i // 3) * ph, pw, ph, t, .24) for i, t in enumerate(tints)]
    s = .66
    sh, ys = shelf(213, 190, 260, rows=2, gap=110)                                        # 1 cafetería
    b += [sh, acc("drop", 170, ys[0] - 38, 70, glow_r=90), ico("soda", 300, ys[1] - 30, 50, INK, .3)]
    b += [ico("theater", 760, 160, 150, INK, .6), ico("popcorn", 760, 270, 70, INK), figure(560, 330, s, "stand", "neutral", look=6)[0]]  # 2
    sh, ys = shelf(1160, 200, 180, rows=2, gap=100)                                       # 3 reorganizar
    b += [sh, ico("apple", 1130, ys[1] - 30, 50, INK), figure(990, 330, s, "reach", "determined", look=6)[0]]
    b += [ico("cookie", 360, 420, 50, INK, .4), figure(150, 690, s, "stand", "calm", look=6)[0]]            # 4 menos disciplina
    sh, ys = shelf(640, 560, 280, rows=2, gap=110)                                        # 5 se degrada
    b += [sh, ico("cookie", 580, ys[0] - 30, 50, INK, .7), ico("discount", 690, ys[1] - 25, 60, INK, .7), ico("soda", 740, ys[0] - 28, 45, INK, .6)]
    sh, ys = shelf(1180, 560, 160, rows=2, gap=100, op=.6)                                # 6 cierre
    b += [sh, ico("drop", 1150, ys[0] - 28, 45, INK, .7), figure(1010, 690, s, "stand", "serene")[0]]
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 1.5}" y="0" width="3" height="{TH}" fill="{BG}"/>')
    b.append(f'<rect x="0" y="{ph - 1.5}" width="{TW}" height="3" fill="{BG}"/>')
    b.append(badge())
    return b

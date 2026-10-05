# -*- coding: utf-8 -*-
"""
scenes.py — Kịch bản hình của project 15 "El Efecto Dominó" (38 khung + 2 thumbnail),
bám theo [VISUAL DESCRIPTION] trong transcript_and_visuals.txt. Màu nhấn #FF5A36 (01_Disciplina y Habitos).
Domino fall="anim" sẽ đổ dây chuyền trong video (animate_video.py); ảnh tĩnh hiển thị trạng thái đã đổ.
"""
from scenekit import *  # noqa: F401,F403
from sticklib import *  # noqa: F401,F403  (nạp lại ACC sau khi đã set_accent theo playlist)
from scenekit import FLOOR, domino_row, domino_tile, dots_row, jumble, marker, timeline
from thumbkit import TH, TW, badge, panel_bg

CANDIDATES = ("shoe", "bedicon", "clock", "notebook")


def single(x, y, h, label=None, op=1.0, wobble=False):
    """Một quân domino nhấn màu, có quầng sáng (đập nhịp như vật nhấn)."""
    t = domino_tile(x, y, h, ACC, op, label, glow_it=True)
    if wobble:
        t = f'<g data-wobble="{x + h * .23:.1f},{y:.1f}">{t}</g>'
    return f'<g data-acc="{x:.1f},{y - h / 2:.1f}">{t}</g>'


def build_layers(n, shot):
    F = lambda **kw: shot_fig(shot, **kw)  # noqa: E731
    b = []
    # ---------------------------------------------------------------- ESCENA 1: EL GANCHO
    if n == 1:
        fig, an = F(x=520, pose="reach", expr="calm", look=6)
        hx = an["rhand"][0]
        b += [floor_line(), fig, domino_row(hx + 50, 1820, FLOOR, n=10, h=200, shrink=.55, fade=.5)]
    elif n == 2:
        b += [floor_line(), domino_row(560, 1860, FLOOR, n=14, h=220, shrink=.7, fade=.85)]
        b += [F(x=300, pose="stand", expr="surprised", look=6)[0]]
    elif n == 3:
        import random
        rnd = random.Random(3)
        icons = ("shoe", "bedicon", "clock", "notebook", "coin", "apple", "target", "book", "phone", "dumbbell")
        for i, nm in enumerate(icons):
            b += [ico(nm, 1250 + rnd.uniform(-260, 330), 400 + rnd.uniform(-230, 260), 70, INK, .22)]
        b += [single(1380, 640, 300)]
        b += [F(x=680, pose="stand", expr="calm", look=6)[0]]
    elif n == 4:
        b += [floor_line(), ico("clover", 1280, 520, 220, INK, .35), acc("xmark", 1280, 520, 190, w=8)]
        b += [F(x=720, pose="stand", expr="neutral", look=6)[0]]
    elif n == 5:
        b += [domino_row(1160, 1820, 1000, n=6, h=200, first_acc=False, op=.35)]
        b += [acc("document", 1400, 380, 200), F(x=720, pose="stand", expr="thoughtful", look=6)[0]]
    # ---------------------------------------------------------------- ESCENA 2: EL HÁBITO CLAVE
    elif n == 6:
        b += [floor_line(), marker("1", 1250, 300), single(1250, FLOOR, 280)]
        b += [F(x=700, pose="explain", expr="calm", look=6)[0]]
    elif n == 7:
        b += [acc("book", 1320, 440, 230, progress=0), F(x=700, pose="explain", expr="thoughtful", look=5)[0]]
    elif n == 8:
        b += [ico("building", 1460, 420, 360, INK, .45), ico("coin", 1460, 180, 90, INK, .2), ico("xmark", 1460, 180, 80, INK, .3)]
        b += [acc("shield", 1460, 330, 120)]
        b += [figure(1080, 1180, 2.0, "stand", op=.45, ghost=True)[0]]
    elif n == 9:
        b += [floor_line(), domino_row(900, 1780, FLOOR, n=9, h=190, first_acc=False, op=.3)]
        b += [single(560, FLOOR, 300, label="clock")]
    elif n == 10:
        b += [floor_line(), domino_row(330, 1700, FLOOR, n=8, h=250, fall="anim", step=.22,
                                       labels=["clock", "bubble", "org", "pair", "bubble", "org", "pair", "coin"])]
    elif n == 11:
        b += [domino_row(160, 1200, 1000, n=10, h=170, fall="done", op=.45)]
        b += [acc("coins", 1500, 420, 200)] + [ico("coin", x, y, 70, ACC, .8) for x, y in ((1330, 300), (1680, 330), (1600, 600), (1380, 620))]
    elif n == 12:
        b += [floor_line(), domino_row(220, 1700, FLOOR, n=16, h=190, fall="anim", step=.12)]
    # ---------------------------------------------------------------- ESCENA 3: POR QUÉ FUNCIONA
    elif n == 13:
        b += [floor_line(), domino_row(950, 1820, FLOOR, n=10, h=170, fall="done", op=.35)]
        b += [marker("2", 1330, 300), F(x=650, pose="explain", expr="calm", look=6)[0]]
    elif n == 14:
        b += [ico("signpost", 1320, 520, 260, INK, .25, rot=-14), F(x=700, pose="dismiss", expr="thoughtful", look=6)[0]]
    elif n == 15:
        b += [line(180, 760, 1760, 760, INK, 4, .3)]
        for i in range(14):
            x = 200 + i * 112
            r = 5 * 1.27 ** i
            b += [f'<g data-dot="{i}">' + glow(x, 760 - r, r * 2.4, "A", .9)
                  + f'<circle cx="{x}" cy="{760 - r:.1f}" r="{r:.1f}" fill="{ACC}"/></g>']
    elif n == 16:
        b += [ico("star", 1280, 560, 90, INK, .5), line(1200, 620, 1360, 620, INK, 6, .4)]
        b += [F(x=700, pose="shrug", expr="neutral", look=6)[0]]
    elif n == 17:
        for i in range(6):
            b += [f'<g data-dot="{i}">' + place(1000 + i * 70, 820, 50, icon("check", INK, 8)) + "</g>"]
        b += [glow(1480, 520, 260, "A", 1), figure(1480, 760, .9, "stand", "determined", color=ACC)[0]]
        b += [F(x=560, pose="explain", expr="calm", look=6)[0]]
    elif n == 18:
        b += [acc("person", 960, 470, 200)]
        for x, y, nm in ((560, 260, "pill"), (1360, 260, "target"), (520, 780, "coin"), (1400, 800, "apple"), (960, 900, "clock")):
            b += [line(960, 470, x, y, INK, 3, .3, "8 10"), ico(nm, x, y, 80, INK, .7)]
    # ---------------------------------------------------------------- ESCENA 4: CÓMO ENCONTRAR EL TUYO
    elif n == 19:
        b += [floor_line(), marker("3", 1320, 280)]
        b += [ico(nm, 1080 + i * 160, 780, 90, INK, .8) for i, nm in enumerate(CANDIDATES)]
        b += [F(x=600, pose="explain", expr="calm", look=6)[0]]
    elif n == 20:
        b += [ico(nm, x, y, 130, INK, .9) for nm, (x, y) in zip(CANDIDATES, ((1180, 330), (1480, 330), (1180, 630), (1480, 630)))]
        b += [F(x=620, pose="explain", expr="attentive", look=6)[0]]
    elif n == 21:
        for i, nm in enumerate(CANDIDATES):
            x = 420 + i * 360
            b += [glow(x, 540, 200, "W", 1), ico(nm, x, 540, 190, INK)]
    elif n == 22:
        b += [floor_line(), ico("question", 1280, 330, 200, INK, .4), acc("xmark", 1280, 330, 170, w=8)]
        b += [ico(nm, 1040 + i * 160, 780, 90, INK, .7) for i, nm in enumerate(CANDIDATES)]
        b += [F(x=600, pose="stand", expr="thoughtful", look=6)[0]]
    elif n == 23:
        fig, an = F(x=640, pose="reach", expr="determined", look=6)
        hx, hy = an["rhand"]
        b += [ico("calendar", 1480, 320, 200, INK, .7, crossed=10), fig, acc("shoe", hx + 90, hy, 130)]
    elif n == 24:
        b += [acc("shoe", 820, 560, 260)]
        for (x, y), nm in zip(((1380, 260), (1520, 560), (1380, 860)), ("moon", "apple", "target")):
            b += [line(940, 560, x, y, INK, 4, .45, "10 10"), glow(x, y, 120, "W", 1), ico(nm, x, y, 130, INK)]
    elif n == 25:
        b += [floor_line(), acc("notebook", 1180, 600, 170)]
        b += [ico(nm, x, y, 100, INK, .18) for nm, (x, y) in zip(("moon", "apple", "target"), ((1480, 350), (1580, 600), (1480, 820)))]
        b += [F(x=640, pose="stand", expr="thoughtful", look=6)[0]]
    # ---------------------------------------------------------------- ESCENA 5: QUÉ NO DEBES ESPERAR
    elif n == 26:
        b += [floor_line(), marker("4", 1300, 300), F(x=700, pose="stand", expr="calm", look=6)[0]]
    elif n == 27:
        b += [floor_line(), single(1260, FLOOR, 300, wobble=True)]
        b += [figure(560, FLOOR, 1.5, "walk", op=.4, ghost=True)[0]]
    elif n == 28:
        b += [jumble(960, 560, n=20, h=150, seed=28)]
    elif n == 29:
        b += [timeline(260, 960, 1700, 960, ticks=8, color=INK, w=4, op=.4)]
        b += [f'<g data-dot="{i}"><circle cx="{330 + i * 170}" cy="960" r="10" fill="{INK}"/></g>' for i in range(8)]
        fig, an = F(x=640, pose="push", expr="calm", look=6)
        b += [single(an["rhand"][0] + 80, FLOOR - 40, 240), fig]
    elif n == 30:
        b += [f'<g opacity=".2">{jumble(560, 620, n=20, h=110, seed=30)}</g>', single(1400, FLOOR, 340)]
    elif n == 31:
        b += [f'<g opacity=".25">{jumble(320, 700, n=14, h=120, seed=31)}</g>', single(1480, 900, 420)]
        b += [F(x=960, pose="stand", expr="determined", look=6)[0]]
    # ---------------------------------------------------------------- ESCENA 6: EL CIERRE
    elif n == 32:
        fig, an = F(x=560, pose="reach", expr="serene", look=6)
        hx = an["rhand"][0]
        b += [floor_line(), fig, domino_row(hx + 50, 1800, FLOOR, n=9, h=190, shrink=.4, fade=.6)]
    elif n == 33:
        b += [timeline(260, 980, 1700, 980, ticks=10, color=INK, w=4, op=.4)]
        b += [f'<g data-dot="{i}">' + place(330 + i * 130, 940, 40, icon("check", INK, 8)) + "</g>" for i in range(11)]
        fig, an = F(x=620, pose="reach", expr="calm", look=6)
        b += [fig, single(an["rhand"][0] + 60, FLOOR - 60, 230)]
    elif n == 34:
        b += [domino_row(1150, 1820, 1000, n=5, h=260, op=.55)]
        b += [F(x=640, pose="stand", expr="serene", look=6)[0]]
    elif n == 35:
        b += [acc("bubble", 1320, 360, 220), F(x=760, pose="point_you", expr="warm", look=3)[0]]
    elif n == 36:
        b += [acc("calendar", 1320, 420, 200, crossed=0), F(x=720, pose="stand", expr="attentive", look=6)[0]]
    elif n == 37:
        b += [floor_line(), acc("bell", 1260, 430, 150), F(x=860, pose="thumbs", expr="smile")[0]]
    elif n == 38:
        b += [floor_line(), domino_row(160, 1760, FLOOR - 10, n=18, h=170, fall="done", op=.6)]
        b += [rim(960, 520, 520), F(x=960, pose="stand", expr="serene")[0]]
    else:
        raise ValueError(n)
    return b


def thumb_b():
    """Mẫu B — triptych: tender la cama · registrar gastos · hora fija para dormir (vật nhấn ở khung 3)."""
    pw = TW / 3
    b = [panel_bg(0, 0, pw, TH, "#7FB8FF", .26), panel_bg(pw, 0, pw, TH, "#FFB46B", .3), panel_bg(2 * pw, 0, pw, TH, "#8C7BFF", .2)]
    # 1: tender la cama
    b += [f'<rect x="150" y="410" width="250" height="40" rx="10" fill="none" stroke="{INK}" stroke-width="7"/>',
          f'<line x1="150" y1="350" x2="150" y2="560" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>',
          f'<line x1="400" y1="430" x2="400" y2="560" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>',
          f'<rect x="170" y="384" width="80" height="26" rx="12" fill="none" stroke="{INK}" stroke-width="6"/>']
    b += [figure(90, 560, .9, "reach_down", "calm", look=6)[0]]
    # 2: anotar gastos
    b += [glow(640 + 90, 330, 160, "warm", 1), desk(640 + 70, 400, 280), ico("notebook", 640 + 60, 375, 80, INK, lit=3),
          ico("coin", 640 + 160, 370, 40, INK, .9), chair(470, 560, .9), figure(480, 560, .9, "type", "determined", look=5)[0]]
    # 3: reloj junto a la cama, hora fija (vật nhấn)
    mid = 2 * pw + pw / 2
    b += [line(mid - 30, 420, mid + 150, 420, INK, 6), line(mid + 120, 420, mid + 120, 560, INK, 6)]
    b += [acc("clock", mid + 70, 370, 70, glow_r=110), ico("lamp", mid + 10, 370, 70, INK, .35)]
    b += [figure(mid - 120, 560, .9, "reach", "determined", look=6)[0]]
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 3}" y="0" width="6" height="{TH}" fill="#000"/>')
    b.append(badge())
    return b


def thumb_c():
    """Mẫu C — lưới 6 khung theo 6 nhịp của video."""
    pw, ph = TW / 3, TH / 2
    tints = ("#FF8A6B", "#7FB8FF", "#FFB46B", "#5AC8C8", "#8C7BFF", "#FFD9A0")
    b = [panel_bg((i % 3) * pw, (i // 3) * ph, pw, ph, t, .24) for i, t in enumerate(tints)]
    s = .66
    b += [single(213, 320, 220)]                                                            # 1 hábito clave
    b += [figure(520, 330, s, "reach", "determined", look=6)[0], domino_row(640, 820, 330, n=4, h=110, first_acc=False)]  # 2
    b += [figure(940, 330, s, "stand", "attentive", look=6)[0],
          domino_row(1060, 1240, 330, n=5, h=100, first_acc=False, fall="anim")]          # 3 (đang đổ)
    b += [figure(110, 690, s, "stand", "attentive", look=6)[0]] + \
         [ico(nm, x, y, 60, INK, .85) for nm, (x, y) in zip(("shoe", "bedicon", "clock"), ((260, 470), (330, 560), (260, 640)))]  # 4
    b += [domino_row(470, 820, 690, n=7, h=110, first_acc=False, fall="done", op=.9)]      # 5 cascada completa
    b += [domino_row(880, 1260, 690, n=7, h=90, first_acc=False, fall="done", op=.45),
          figure(1066, 690, s, "stand", "serene")[0]]                                       # 6 cierre
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 1.5}" y="0" width="3" height="{TH}" fill="{BG}"/>')
    b.append(f'<rect x="0" y="{ph - 1.5}" width="{TW}" height="3" fill="{BG}"/>')
    b.append(badge())
    return b

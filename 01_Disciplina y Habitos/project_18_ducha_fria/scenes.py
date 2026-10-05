# -*- coding: utf-8 -*-
"""
scenes.py — Kịch bản hình của project 18 "Por Qué la Ducha Fría Cambia Tu Disciplina" (33 khung + 2 thumbnail),
bám theo [VISUAL DESCRIPTION] trong transcript_and_visuals.txt. Màu nhấn #FF5A36 (01_Disciplina y Habitos).
Vòi sen dùng data-flow để tia nước chảy trong video.
"""
from scenekit import *  # noqa: F401,F403
from sticklib import *  # noqa: F401,F403  (nạp lại ACC sau khi đã set_accent theo playlist)
from scenekit import FLOOR, shower
from thumbkit import TH, TW, badge, panel_bg


def bar(x, y_base, h, w=90, color=None, op=1.0):
    color = color or INK
    g = glow(x, y_base - h / 2, h * .6, "A", op) if color == ACC else ""
    tag = f'<g data-acc="{x},{y_base - h / 2:.0f}">' if color == ACC else "<g>"
    return tag + g + f'<rect x="{x - w / 2}" y="{y_base - h}" width="{w}" height="{h}" rx="8" fill="{color}" opacity="{op}"/></g>'


def strip(x0, y, n=7, gap=110, size=80, op=.7, marks=None, warn=0, segs=False):
    """Dải lịch n ngày; warn = số ngày đầu có biển cảnh báo (nhấn); segs = mỗi ngày có đoạn lạnh 30s (nhấn)."""
    out = []
    for i in range(n):
        x = x0 + i * gap
        o = op if marks is None or i < marks else op * .25
        out.append(ico("page", x, y, size, INK, o))
        if i < warn:
            out.append(acc("warning", x, y - size * .9, size * .45))
        if segs:
            out.append(f'<g data-dot="{i}"><rect x="{x - size * .35:.0f}" y="{y + size * .62:.0f}" width="{size * .7:.0f}" height="10" rx="5" fill="{INK}" opacity=".35"/>'
                       f'<rect x="{x + size * .15:.0f}" y="{y + size * .62:.0f}" width="{size * .2:.0f}" height="10" rx="5" fill="{ACC}"/></g>')
    return "".join(out)


def build_layers(n, shot):
    F = lambda **kw: shot_fig(shot, **kw)  # noqa: E731
    b = []
    # ---------------------------------------------------------------- EL GANCHO
    if n == 1:
        b += [floor_line(), shower(1420, op=.15), F(x=760, pose="stand", expr="neutral", look=4)[0]]
    elif n == 2:
        b += [glow(820, 470, 300, "W", 1), ico("brain", 820, 470, 280, INK), acc("timer", 1260, 470, 200, progress=.5)]
    elif n == 3:
        b += [floor_line(), rim(960, 520, 520), F(x=960, pose="stand", expr="calm")[0]]
    elif n == 4:
        b += [acc("gear", 1300, 460, 210), F(x=700, pose="explain", expr="determined", look=6)[0]]
    elif n == 5:
        b += [ico("phone", 600, 520, 260, INK, .3), ico("hashtag", 600, 520, 90, INK, .3), ico("arrow", 940, 520, 140, INK, .6)]
        b += [place(1320, 540, 280, icon("bars", ACC, 7, vals=(.3, .55, .8, 1))), glow(1320, 540, 240, "A", .6)]
    # ---------------------------------------------------------------- MÓDULO 1 — Noradrenalina (Sramek)
    elif n == 6:
        b += [acc("bolt", 840, 520, 240), ico("drop", 1120, 520, 180, INK, .9)]
    elif n == 7:
        b += [acc("document", 1180, 360, 170)]
        b += [f'<rect x="1300" y="560" width="300" height="200" rx="14" fill="none" stroke="{INK}" stroke-width="7"/>',
              f'<path d="M1310,610 q35,-18 70,0 t70,0 t70,0 t70,0" fill="none" stroke="{INK}" stroke-width="4" opacity=".6"/>',
              ico("thermo", 1560, 520, 150, INK, .9, level=.2)]
        b += [F(x=680, pose="explain", expr="calm", look=6)[0]]
    elif n == 8:
        for x, lvl, h, col in ((600, .85, 120, INK), (960, .4, 440, ACC), (1320, .15, 380, INK)):
            b += [ico("thermo", x, 860, 130, INK, .85, level=lvl), bar(x, 760, h, color=col, op=1 if col == ACC else .45)]
    elif n == 9:
        b += [ico("timer", 680, 500, 220, INK, .8, progress=.08), bar(1240, 820, 520, w=140, color=ACC)]
    elif n == 10:
        b += [ico("molecule", 820, 520, 240, INK), ico("warning", 1260, 520, 170, INK, .3)]
    elif n == 11:
        b += [acc("molecule", 960, 520, 200)]
        for nm, x, y in (("eye", 480, 260), ("bolt", 1440, 260), ("face", 960, 900)):
            b += [line(960, 520, x, y, ACC, 5, .8), glow(x, y, 110, "W", 1), ico(nm, x, y, 130, INK)]
    elif n == 12:
        b += [ico("timer", 680, 500, 220, INK, .8, progress=.1), bar(1240, 820, 560, w=140, color=ACC)]
    # ---------------------------------------------------------------- MÓDULO 2 — El Ánimo (Shevchuk)
    elif n == 13:
        b += [ico("face", 760, 520, 200, INK, .5, mood=0), ico("arrow", 960, 520, 120, INK, .6), acc("face", 1160, 520, 200, mood=1)]
    elif n == 14:
        b += [acc("journal", 1300, 440, 220), F(x=700, pose="explain", expr="thoughtful", look=6)[0]]
    elif n == 15:
        for i, (x, r) in enumerate(((360, -60), (560, -10), (760, 50))):
            b += [ico("valve", x, 540, 140, INK, .5 + i * .2, rot=r)]
        b += [line(860, 540, 1240, 540, ACC, 6, .9), place(1250, 540, 50, icon("arrow", ACC, 8))]
        b += [ico("face", 1460, 540, 200, INK, mood=.6)]
    elif n == 16:
        b += [acc("nerves", 960, 520, 360), ico("molecule", 560, 520, 150, INK, .8), ico("molecule", 1360, 520, 150, INK, .8)]
    elif n == 17:
        b += [ico("pill", 440, 340, 130, INK), ico("valve", 440, 760, 140, INK)]
        b += [f'<g data-acc="1100,540">' + glow(1100, 540, 300, "A", .4)
              + f'<path d="M540,340 C900,340 1000,520 1300,540" fill="none" stroke="{ACC}" stroke-width="7"/>'
              + f'<path d="M540,760 C900,760 1000,560 1300,540" fill="none" stroke="{ACC}" stroke-width="7"/></g>']
        b += [ico("face", 1440, 540, 210, INK, mood=1)]
    elif n == 18:
        fig, an = F(x=960, pose="hunch", expr="strain")
        b += [shower(960, head_y=an["top"][1] - 120, intense=True), fig]
    elif n == 19:
        b += [floor_line(), acc("nerves", 1260, 470, 260), ico("timer", 1520, 300, 110, INK, .7, progress=.75)]
        b += [F(x=700, pose="stand", expr="attentive", look=6)[0]]
    # ---------------------------------------------------------------- MÓDULO 3 — La Conexión con la Disciplina
    elif n == 20:
        b += [shower(700, head_y=330, floor=760, width=150, op=.9)]
        b += [line(860, 520, 1130, 520, ACC, 8), glow(1000, 520, 200, "A", .6), ico("gear", 1260, 520, 200, INK)]
    elif n == 21:
        b += [floor_line(), ico("thermo", 1760, 520, 120, INK, .18, level=.3), F(x=900, pose="stand", expr="neutral", look=4)[0]]
    elif n == 22:
        b += [acc("valve", 1320, 420, 150), ico("arrow", 560, 470, 120, INK, .35, rot=180)]
        b += [F(x=820, pose="reach", expr="determined", look=6)[0]]
    elif n == 23:
        b += [floor_line(), acc("valve", 1240, 520, 150, rot=95), ico("arrow", 520, 560, 110, INK, .1, rot=180)]
        b += [F(x=820, pose="reach", expr="determined", look=6)[0]]
    elif n == 24:
        b += [acc("gear", 960, 420, 220)]
        for nm, x, y in (("clock", 520, 820), ("document", 960, 860), ("handshake", 1400, 820)):
            b += [line(960, 420, x, y, INK, 4, .45), ico(nm, x, y, 130, INK)]
    # ---------------------------------------------------------------- MÓDULO 4 — Por Qué Abandonan
    elif n == 25:
        b += [strip(630, 560, n=7, gap=110, size=80, warn=3)]
    elif n == 26:
        fig, an = F(x=900, pose="hunch", expr="strain")
        b += [floor_line(), shower(900, head_y=an["top"][1] - 120, intense=True), fig, ico("timer", 1500, 340, 160, INK, .8, progress=1.0), ico("page", 300, 300, 80, INK, .4)]
    elif n == 27:
        b += [acc("burst", 1220, 380, 200), strip(560, 860, n=7, gap=110, size=60, marks=1)]
        b += [F(x=760, pose="step_back", expr="surprised", look=-6, tilt=-8)[0]]
    elif n == 28:
        b += [f'<rect x="360" y="500" width="1200" height="90" rx="45" fill="none" stroke="{INK}" stroke-width="6" opacity=".7"/>',
              f'<rect x="372" y="512" width="1040" height="66" rx="33" fill="{INK}" opacity=".12"/>']
        b += [f'<g data-acc="1480,545">' + glow(1480, 545, 160, "A", .9) + f'<rect x="1420" y="512" width="128" height="66" rx="33" fill="{ACC}"/></g>']
        b += [shower(560, head_y=250, floor=460, width=120, op=.5), shower(1480, head_y=250, floor=460, width=120, op=.9)]
    elif n == 29:
        b += [strip(260, 560, n=14, gap=110, size=70, segs=True)]
    # ---------------------------------------------------------------- EL CIERRE
    elif n == 30:
        b += [ico("tub", 640, 560, 280, INK, .3), ico("xmark", 640, 560, 220, INK, .5), acc("timer", 1300, 520, 220, progress=.5)]
    elif n == 31:
        b += [ico("valve", 1320, 420, 150, INK), acc("timer", 1360, 200, 110, progress=.5)]
        b += [F(x=820, pose="reach", expr="calm", look=6)[0]]
    elif n == 32:
        b += [acc("bubble", 1320, 360, 220), ico("timer", 1560, 560, 110, INK, .6, progress=.5)]
        b += [F(x=760, pose="point_you", expr="warm", look=3)[0]]
    elif n == 33:
        fig, an = F(x=860, pose="stand", expr="calm")
        b += [floor_line(), shower(860, head_y=an["top"][1] - 120), fig, acc("bell", 1700, 170, 90), acc("check", 1580, 170, 80)]
    else:
        raise ValueError(n)
    return b


def thumb_b():
    """Mẫu B — triptych: mirar el temporizador de 30 s · el agua fría golpea · afuera, con energía (vật nhấn)."""
    pw = TW / 3
    b = [panel_bg(0, 0, pw, TH, "#7FB8FF", .26), panel_bg(pw, 0, pw, TH, "#5AC8C8", .24), panel_bg(2 * pw, 0, pw, TH, "#FFD9A0", .3)]
    b += [ico("timer", 310, 260, 150, INK, progress=.5), figure(150, 560, .95, "point", "calm", look=6)[0]]
    fig, an = figure(pw + pw / 2, 560, .95, "hunch", "determined")
    b += [shower(pw + pw / 2, head_y=an["top"][1] - 90, floor=560, width=140, intense=True), fig]
    mid = 2 * pw + pw / 2
    b += [ico("sun", mid + 110, 160, 110, INK, .6), line(2 * pw + 20, 560, TW - 20, 560, INK, 4, .3)]
    b += [acc("bolt", mid + 110, 330, 70, glow_r=110), figure(mid - 60, 560, .95, "hands_hips", "determined", look=6)[0]]
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 3}" y="0" width="6" height="{TH}" fill="#000"/>')
    b.append(badge())
    return b


def thumb_c():
    """Mẫu C — lưới 6 khung."""
    pw, ph = TW / 3, TH / 2
    tints = ("#FF8A6B", "#8C7BFF", "#7FB8FF", "#5AC8C8", "#FFB46B", "#FFD9A0")
    b = [panel_bg((i % 3) * pw, (i // 3) * ph, pw, ph, t, .24) for i, t in enumerate(tints)]
    s = .66
    b += [ico("thermo", 170, 180, 170, INK, level=.15), acc("bolt", 280, 170, 90, glow_r=110)]              # 1 Sramek
    b += [ico("brain", 760, 150, 110, INK, .8), figure(560, 330, s, "stand", "calm", look=6)[0]]              # 2 Shevchuk
    b += [ico("valve", 1170, 180, 90, INK), figure(990, 330, s, "reach", "strain", look=6)[0]]               # 3 decisión incómoda
    fig, an = figure(213, 690, s, "hunch", "determined")
    b += [shower(213, head_y=an["top"][1] - 70, floor=690, width=110, intense=True), fig, ico("bolt", 213, 560, 50, INK, .9)]  # 4
    b += [ico("timer", 640, 540, 200, INK, progress=.5)]                                                     # 5 30 segundos
    b += [rim(1066, 540, 200), figure(1066, 690, s, "stand", "satisfied")[0]]                              # 6 cierre
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 1.5}" y="0" width="3" height="{TH}" fill="{BG}"/>')
    b.append(f'<rect x="0" y="{ph - 1.5}" width="{TW}" height="3" fill="{BG}"/>')
    b.append(badge())
    return b

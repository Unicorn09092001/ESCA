# -*- coding: utf-8 -*-
"""
scenes.py — Kịch bản hình của project 20 "7 Habilidades Que Toda Persona Debe Dominar" (50 khung + 2 thumbnail),
bám theo [VISUAL DESCRIPTION] trong transcript_and_visuals.txt. Màu nhấn #E8A23C (02_Mentalidad y Exito).
"""
from scenekit import *  # noqa: F401,F403
from sticklib import *  # noqa: F401,F403  (nạp lại ACC sau khi đã set_accent theo playlist)
from scenekit import FLOOR, marker, mirror, table, timeline
from thumbkit import TH, TW, badge, panel_bg

SKILLS = ("firstaid", "pot", "pie", "bubble", "wrench", "handshake", "notebook")


def collapsed(x, y=FLOOR - 8, s=1.05, op=.45):
    """Người bất tỉnh (mờ) nằm trên sàn."""
    return figure(x, y, s, "stand", op=op, ghost=True, tilt=-90)[0]


def build_layers(n, shot):
    F = lambda **kw: shot_fig(shot, **kw)  # noqa: E731
    b = []
    # ---------------------------------------------------------------- GANCHO / PROMESA
    if n == 1:
        b += [floor_line(), ico("schooldesk", 1180, 760, 220, INK, .3)]
        import random
        rnd = random.Random(1)
        b += [ico(nm, 1250 + rnd.uniform(-300, 400), 360 + rnd.uniform(-160, 120), 70, INK, .4) for nm in SKILLS]
        b += [F(x=600, pose="stand", expr="neutral", look=6)[0]]
    elif n == 2:
        b += [timeline(240, 720, 1700, 720, ticks=6, color=INK, w=4, op=.45)]
        b += [acc("warning", 520, 590, 80), line(520, 640, 520, 720, ACC, 4, .8, "8 8")]
        b += [ico(nm, 1380 + i * 70, 620 - (i % 2) * 40, 60, INK, .7) for i, nm in enumerate(SKILLS[:4])]
    elif n == 3:
        b += [F(x=720, pose="stand", expr="calm", look=6)[0], dots_arc(720, 430, 380, n=7, a0=-55, a1=55)]
    elif n == 4:
        b += [ico("toolbox", 1060, 560, 380, INK, .85), dots_arc(1060, 640, 300, n=7, a0=200, a1=340)]
    # ---------------------------------------------------------------- H1 — Primeros auxilios
    elif n == 5:
        b += [floor_line(), marker("1", 1320, 300), acc("firstaid", 1320, 650, 160), F(x=700, pose="explain", expr="calm", look=6)[0]]
    elif n == 6:
        b += [floor_line(), collapsed(1440), F(x=860, pose="reach_down", expr="determined", look=6)[0]]
    elif n == 7:
        b += [acc("clock", 1500, 280, 150), collapsed(1200, y=1000, s=1.6, op=.35)]
        b += [F(x=620, pose="push", expr="determined", look=6)[0]]
    elif n == 8:
        b += [floor_line(), collapsed(960, op=.3), crowd([300, 460, 620, 1300, 1460, 1620], FLOOR, .62, .2, poses=["cross", "stand"])]
    elif n == 9:
        b += [timeline(240, 760, 1700, 760, ticks=6, color=INK, w=4, op=.4)]
        b += [f'<g data-acc="430,760"><rect x="250" y="700" width="360" height="120" rx="14" fill="{ACC}" opacity=".3"/></g>', acc("clock", 430, 520, 150)]
    elif n == 10:
        b += [collapsed(1360, y=1020, s=1.6, op=.4), F(x=640, pose="stand", expr="determined", look=6)[0]]
    # ---------------------------------------------------------------- H2 — Cocinar
    elif n == 11:
        b += [floor_line(), marker("2", 1360, 280), desk(1160, 700, 460), ico("pot", 1180, 640, 120, INK)]
        b += [acc("apple", 1340, 655, 60), ico("drop", 1020, 660, 50, INK, .8)]
        b += [F(x=720, pose="reach", expr="calm", look=6)[0]]
    elif n == 12:
        b += [ico("cloche", 1320, 520, 220, INK, .3, rot=-8), F(x=720, pose="dismiss", expr="neutral", look=6)[0]]
    elif n == 13:
        b += [f'<rect x="1100" y="200" width="460" height="560" fill="none" stroke="{INK}" stroke-width="7" opacity=".7"/>',
              line(1100, 380, 1560, 380, INK, 6, .6), line(1100, 570, 1560, 570, INK, 6, .6)]
        b += [acc("apple", 1220, 330, 70), ico("drop", 1420, 335, 60, INK, .7), ico("pot", 1330, 520, 80, INK, .6)]
        b += [F(x=640, pose="stand", expr="thoughtful", look=6)[0]]
    elif n == 14:
        b += [floor_line(), ico("takeout", 1500, 560, 160, INK, .15), desk(1100, 700, 380), acc("pot", 1100, 640, 120)]
        b += [F(x=760, pose="reach", expr="calm", look=6)[0]]
    elif n == 15:
        b += [ico("pot", 1180, 520, 200, INK), ico("coin", 1440, 360, 80, INK, .5), F(x=680, pose="stand", expr="calm", look=6)[0]]
    elif n == 16:
        b += [ico("pot", 1220, 640, 160, INK), acc("battery", 1460, 380, 160, level=.9), F(x=700, pose="stand", expr="satisfied", look=6)[0]]
    # ---------------------------------------------------------------- H3 — Presupuestar 50/30/20
    elif n == 17:
        b += [floor_line(), marker("3", 1360, 280), acc("pie", 1360, 640, 220), F(x=720, pose="explain", expr="calm", look=6)[0]]
    elif n == 18:
        b += [acc("book", 1300, 440, 220, progress=0), F(x=700, pose="explain", expr="thoughtful", look=6)[0]]
    elif n == 19:
        for i, x in enumerate((560, 960, 1360)):
            b += [f'<g data-dot="{i}">' + glow(x, 540, 200, "A", .6) + place(x, 540, 260, icon("pie", INK, 6, hi=i, accent=ACC)) + "</g>"]
    elif n == 20:
        b += [ico("grid", 640, 520, 260, INK, .25, rot=-8), ico("arrow", 960, 520, 120, INK, .6), acc("pie", 1300, 520, 260)]
    elif n == 21:
        b += [acc("pie", 1300, 360, 200)] + [ico("page", 1060 + i * 120, 760, 80, INK, .6) for i in range(5)]
        b += [F(x=620, pose="stand", expr="calm", look=6)[0]]
    # ---------------------------------------------------------------- H4 — Hablar en público
    elif n == 22:
        b += [floor_line(), marker("4", 560, 260), crowd([1260, 1420, 1580, 1740], FLOOR, .7, .25, poses=["stand", "cross"])]
        b += [F(x=820, pose="explain", expr="worried", look=6)[0]]
    elif n == 23:
        fig, an = F(x=860, pose="stand", expr="worried", look=6)
        sx, sy = an["sh"]
        b += [fig, f'<g data-acc="{sx:.0f},{sy + 80:.0f}">' + glow(sx, sy + 80, 120, "A", .9) + place(sx + 4, sy + 80, 70, icon("bolt", ACC, 7)) + "</g>"]
    elif n == 24:
        fig, an = figure(1000, 430 + 328 * 2.35, 2.35, "explain", op=.4, ghost=True)
        sx, sy = an["sh"]
        b += [fig, acc("bolt", sx + 10, sy + 180, 120)]
    elif n == 25:
        fig, an = F(x=860, pose="stand", expr="calm", look=6)
        tx, ty = an["top"]
        b += [floor_line(), fig, ico("cloud", tx + 260, ty + 40, 120, INK, .4), acc("bolt", an["sh"][0], an["sh"][1] + 80, 50, op=.5)]
    elif n == 26:
        d1 = "M260,420 " + " ".join(f"L{260 + i * 40},{420 + (40 if i % 2 else -40)}" for i in range(1, 16))
        d2 = "M260,700 " + " ".join(f"Q{260 + i * 160 - 80},{700 + (60 if i % 2 else -60)} {260 + i * 160},700" for i in range(1, 9))
        b += [f'<path d="{d1}" fill="none" stroke="{INK}" stroke-width="5" opacity=".3"/>',
              f'<g data-acc="960,700">' + glow(960, 700, 300, "A", .5) + f'<path d="{d2}" fill="none" stroke="{ACC}" stroke-width="8"/></g>']
    elif n == 27:
        b += [crowd([1100, 1280, 1640, 1800], 1080, 1.0, .18, poses=["stand"]), glow(1460, 700, 200, "A", .8), figure(1460, 1080, 1.0, "stand", op=.6, ghost=True)[0]]
        b += [F(x=620, pose="explain", expr="calm", look=6)[0]]
    # ---------------------------------------------------------------- H5 — Reparaciones
    elif n == 28:
        fig, an = F(x=760, pose="reach", expr="calm", look=6)
        hx, hy = an["rhand"]
        b += [floor_line(), marker("5", 1360, 280), fig, acc("wrench", hx + 50, hy - 10, 110)]
    elif n == 29:
        b += [acc("pipe", 1300, 440, 260), ico("wrench", 1160, 580, 120, INK, rot=-30), F(x=640, pose="reach", expr="determined", look=6)[0]]
    elif n == 30:
        b += [ico("call", 1320, 440, 200, INK, .2), ico("xmark", 1320, 440, 160, INK, .3), ico("pipe", 1560, 760, 140, INK, .8, drip=False)]
        b += [F(x=640, pose="stand", expr="calm", look=6)[0]]
    elif n == 31:
        b += [floor_line(), ico("pipe", 960, 560, 260, INK, drip=False), ico("coin", 1260, 420, 80, INK, .55)]
    elif n == 32:
        b += [ico("pipe", 1460, 760, 160, INK, .8, drip=False), acc("star", 1360, 360, 160), F(x=680, pose="stand", expr="satisfied", look=6)[0]]
    # ---------------------------------------------------------------- H6 — Negociar (Voss)
    elif n == 33:
        b += [floor_line(), marker("6", 960, 260), table(960, 700, 300), chair(640, FLOOR, 1.12), mirror(chair(1300, FLOOR, 1.12), 1300)]
        b += [mirror(figure(1280, FLOOR, 1.12, "sit", "calm", op=.45, ghost=True)[0], 1280), figure(660, FLOOR, 1.12, "sit", "calm", look=6)[0]]
    elif n == 34:
        b += [acc("badge", 1300, 440, 200), F(x=700, pose="explain", expr="thoughtful", look=6)[0]]
    elif n == 35:
        b += [acc("bubble", 1180, 420, 220), ico("question", 1180, 400, 90, ACC), ico("bubble", 1520, 520, 160, INK, .25), ico("warning", 1520, 500, 70, INK, .25)]
        b += [F(x=620, pose="stand", expr="calm", look=6)[0]]
    elif n == 36:
        b += [floor_line(), table(960, 700, 300), chair(640, FLOOR, 1.12), mirror(chair(1300, FLOOR, 1.12), 1300)]
        b += [mirror(figure(1260, FLOOR, 1.12, "sit", "smile", op=.5, ghost=True, tilt=-6)[0], 1260), figure(660, FLOOR, 1.12, "sit", "calm", look=6)[0]]
        b += [f'<g data-acc="960,400"><path d="M760,420 Q960,320 1160,420" fill="none" stroke="{ACC}" stroke-width="6" stroke-dasharray="14 10"/></g>']
    elif n == 37:
        b += [ico("trophy", 1260, 460, 150, INK, .25, rot=-10), ico("xmark", 1450, 470, 90, INK, .25), F(x=680, pose="dismiss", expr="calm", look=6)[0]]
    elif n == 38:
        b += [acc("handshake", 960, 520, 300), glow(960, 520, 360, "W", .6)]
    # ---------------------------------------------------------------- H7 — Escribir con claridad
    elif n == 39:
        b += [floor_line(), marker("7", 1360, 280), desk(1180, 700, 420), acc("notebook", 1180, 655, 110, lit=3)]
        b += [chair(820, FLOOR, 1.12), figure(830, FLOOR, 1.12, "type", "calm", look=5)[0]]
    elif n == 40:
        b += [ico("document", 640, 520, 300, INK, .35), ico("arrow", 960, 520, 120, INK, .6)]
        b += [f'<g data-dot="{i}">' + glow(1180 + 120, 420 + i * 100, 80, "A", .5) + line(1160, 420 + i * 100, 1440, 420 + i * 100, ACC, 14) + "</g>" for i in range(3)]
    elif n == 41:
        b += [ico("envelope", 760, 520, 220, INK), acc("heart", 1160, 520, 200)]
    elif n == 42:
        b += [floor_line(), acc("envelope", 900, 420, 120), line(1000, 420, 1200, 420, INK, 4, .5, "10 10")]
        b += [figure(1380, FLOOR, 1.12, "reach", "calm", op=.5, ghost=True)[0], F(x=560, pose="stand", expr="calm", look=6)[0]]
    elif n == 43:
        b += [acc("envelope", 860, 520, 220), line(1000, 520, 1240, 520, ACC, 5, .8), ico("question", 1440, 520, 160, INK, .15)]
    # ---------------------------------------------------------------- EL CIERRE
    elif n == 44:
        b += [floor_line(), dots_arc(960, 610, 430, n=7, a0=205, a1=335, size=14), F(x=960, pose="stand", expr="calm")[0]]
    elif n == 45:
        b += [ico("resume", 640, 520, 200, INK, .25), ico("phone", 960, 520, 200, INK, .25), ico("schooldesk", 1280, 540, 200, INK, .25)]
    elif n == 46:
        b += [acc("toolbox", 1380, 460, 260), F(x=720, pose="stand", expr="calm", look=6)[0]]
    elif n == 47:
        b += [floor_line()]
        for i, nm in enumerate(SKILLS):
            a = math.radians(205 + 130 * i / 6)
            x, y = 960 + 470 * math.cos(a), 600 + 430 * math.sin(a)
            b += [f'<g data-dot="{i}">' + glow(x, y, 80, "A", .7) + place(x, y, 80, icon(nm, ACC, 7)) + "</g>"]
        b += [F(x=960, pose="hands_hips", expr="determined")[0]]
    elif n == 48:
        b += [acc("bubble", 1320, 360, 220), F(x=760, pose="point_you", expr="warm", look=3)[0]]
    elif n == 49:
        b += [floor_line(), acc("bell", 1260, 430, 150), F(x=860, pose="thumbs", expr="smile")[0]]
    elif n == 50:
        b += [rim(960, 500, 620), F(x=960, pose="stand", expr="serene")[0]]
    else:
        raise ValueError(n)
    return b


def thumb_b():
    """Mẫu B — triptych: RCP en maniquí · hablar en público con nervios · tachar palabras de una nota (vật nhấn)."""
    pw = TW / 3
    b = [panel_bg(0, 0, pw, TH, "#FF6B6B", .22), panel_bg(pw, 0, pw, TH, "#7FB8FF", .24), panel_bg(2 * pw, 0, pw, TH, "#FFD9A0", .3)]
    b += [line(30, 560, 400, 560, INK, 4, .3), figure(330, 548, .8, "stand", op=.45, ghost=True, tilt=-90)[0],
          figure(150, 560, .95, "reach_down", "determined", look=6)[0]]
    b += [crowd([pw + 330, pw + 400], 560, .5, .3, poses=["stand"]), figure(pw + 160, 560, .95, "explain", "worried", look=6)[0]]
    mid = 2 * pw + pw / 2
    b += [desk(mid + 50, 420, 280), ico("document", mid + 90, 360, 100, INK), line(mid + 60, 345, mid + 120, 345, ACC, 6),
          line(mid + 60, 372, mid + 110, 372, ACC, 6), acc("check", mid + 160, 270, 50, glow_r=80),
          chair(mid - 110, 560, .9), figure(mid - 100, 560, .9, "type", "calm", look=5)[0]]
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 3}" y="0" width="6" height="{TH}" fill="#000"/>')
    b.append(badge())
    return b


def thumb_c():
    """Mẫu C — lưới 6 khung."""
    pw, ph = TW / 3, TH / 2
    tints = ("#FF6B6B", "#FFB46B", "#E8A23C", "#7FB8FF", "#5AC8C8", "#8C7BFF")
    b = [panel_bg((i % 3) * pw, (i // 3) * ph, pw, ph, t, .22) for i, t in enumerate(tints)]
    s = .62
    b += [acc("firstaid", 213, 180, 170)]                                                                    # 1
    b += [desk(700, 250, 200), ico("pot", 720, 205, 70, INK), figure(560, 330, s, "reach", "calm", look=6)[0]]  # 2
    b += [ico("pie", 1170, 170, 150, INK, hi=0, accent=ACC), figure(980, 330, s, "stand", "attentive", look=6)[0]]  # 3
    b += [crowd([330, 390], 690, .4, .3, poses=["stand"]), figure(150, 690, s, "explain", "calm", look=6)[0]]  # 4
    b += [ico("pipe", 640, 520, 160, INK), ico("wrench", 560, 600, 80, INK, rot=-30)]                       # 5
    b += [line(1010, 600, 1130, 600, INK, 5), figure(950, 690, .52, "sit", "calm", look=6)[0],
          mirror(figure(1190, 690, .52, "sit", "calm", op=.45, ghost=True)[0], 1190)]                        # 6
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 1.5}" y="0" width="3" height="{TH}" fill="{BG}"/>')
    b.append(f'<rect x="0" y="{ph - 1.5}" width="{TW}" height="3" fill="{BG}"/>')
    b.append(badge())
    return b

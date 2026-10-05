# -*- coding: utf-8 -*-
"""
scenes.py — Kịch bản hình của project 14 "5 Hábitos Que Cambian Todo" (71 khung + 2 thumbnail),
bám theo [VISUAL DESCRIPTION] trong transcript_and_visuals.txt. Màu nhấn #FF5A36 (01_Disciplina y Habitos).
Được tools/draw_frames.py, tools/animate_video.py và tools/make_thumbnails.py nạp tự động.
"""
from scenekit import *  # noqa: F401,F403
from sticklib import *  # noqa: F401,F403  (nạp lại ACC sau khi đã set_accent theo playlist)
from scenekit import FLOOR, bed, dots_row, mirror, nodes, table, timeline
from thumbkit import TH, TW, badge, panel_bg


def dots5(cx, cy, r, a0, a1, size=14, lit=None):
    return dots_arc(cx, cy, r, n=5, a0=a0, a1=a1, size=size, lit=lit)


def table_scene(x_left=640, x_right=1280, ghost_op=.45, s=1.12, expr="warm"):
    """Hai người ngồi đối diện qua bàn, không có điện thoại."""
    mid = (x_left + x_right) / 2
    out = [floor_line(), table(mid, 700, 360), glow(mid, 640, 120, "warm", 1)]
    out.append(f'<ellipse cx="{mid - 70}" cy="688" rx="46" ry="10" fill="none" stroke="{INK}" stroke-width="5"/>')
    out.append(f'<ellipse cx="{mid + 70}" cy="688" rx="46" ry="10" fill="none" stroke="{INK}" stroke-width="5"/>')
    out.append(chair(x_left - 20, FLOOR, s))
    out.append(mirror(chair(x_right + 20, FLOOR, s), x_right + 20))
    out.append(mirror(figure(x_right, FLOOR, s, "sit", "warm", op=ghost_op, ghost=True)[0], x_right))
    out.append(figure(x_left, FLOOR, s, "sit", expr, look=6)[0])
    return out


def build_layers(n, shot):
    """Danh sách lớp SVG của khung n, theo thứ tự xuất hiện."""
    F = lambda **kw: shot_fig(shot, **kw)  # noqa: E731
    b = []
    # ---------------------------------------------------------------- ESCENA 1: EL GANCHO
    if n == 1:
        b += [floor_line(), ico("page", 1300, 430, 200, INK, .35), F(x=760, pose="stand", expr="neutral", look=6)[0]]
    elif n == 2:
        b += [ico("page", 1320, 400, 190, INK, .14), dust(1320, 400, 300, 260, 70, seed=2, op=.6)]
        b += [F(x=720, pose="dismiss", expr="calm", look=6)[0]]
    elif n == 3:
        b += [F(x=720, pose="stand", expr="calm", look=6)[0], dots5(720, 430, 380, -48, 48)]
    elif n == 4:
        b += [rim(700, 500, 560), dots5(860, 520, 420, -50, 50), F(x=700, pose="explain", expr="thoughtful")[0]]
    # ---------------------------------------------------------------- ESCENA 2: LA PROMESA
    elif n == 5:
        b += [floor_line(), ico("bulb", 1280, 520, 220, INK, .32), acc("xmark", 1280, 520, 180, w=8)]
        b += [F(x=720, pose="stand", expr="neutral", look=6)[0]]
    elif n == 6:
        b += [dots5(1260, 600, 300, 205, 335), ico("books", 1260, 640, 190, INK, .55)]
        b += [F(x=640, pose="explain", expr="calm", look=5)[0]]
    elif n == 7:
        b += [dots_row(980, 1640, 300)]
        for x, nm in ((980, "brain"), (1145, "person"), (1310, "pair"), (1475, "coin")):
            b += [ico(nm, x, 470, 100, INK, .8)]
        b += [F(x=560, pose="explain", expr="calm", look=5)[0]]
    elif n == 8:
        b += [F(x=720, pose="stand", expr="attentive", look=6)[0], dots5(720, 430, 380, -48, 48, lit=1)]
    # ---------------------------------------------------------------- ESCENA 3: HÁBITO 1
    elif n == 9:
        b += [floor_line(), glow(1180, 520, 360, "warm", 1), desk(1120, 705, 520), chair(800, FLOOR, 1.12)]
        b += [ico("lamp", 1300, 610, 150, INK)]
        b += [acc("notebook", 1060, 670, 110, lit=3)]
        b += [figure(810, FLOOR, 1.12, "type", "calm", look=5)[0]]
    elif n == 10:
        b += [F(x=960, pose="hands_hips", expr="thoughtful", tilt=-4)[0]]
    elif n == 11:
        b += [ico("building", 1400, 360, 280, INK, .4), glow(1400, 360, 260, "W", 1)]
        b += [F(x=760, pose="stand", expr="thoughtful", look=5)[0]]
    elif n == 12:
        b += [timeline(900, 320, 1760, 320, ticks=2), F(x=620, pose="point", expr="determined", look=6)[0]]
    elif n == 13:
        b += [ico("calendar", 1260, 330, 200, INK, .7, crossed=12)]
        for i, (x, r) in enumerate(((1080, 50), (1260, 80), (1440, 120))):
            b += [f'<g data-acc="{x},{660}">' + glow(x, 660, r * 1.8, "A", 1) + f'<circle cx="{x}" cy="660" r="{r * .35:.0f}" fill="{ACC}"/></g>']
        b += [F(x=600, pose="stand", expr="calm", look=6)[0]]
    elif n == 14:
        b += [ico("cloud", 960, 130, 300, INK, .1), ico("cloud", 960, 140, 140, INK, .55)]
        b += [F(x=960, pose="stand", expr="serene", head_y=470)[0]]
    elif n == 15:
        b += [floor_line(), bed(560, 1360, 690), acc("timer", 1530, 330, 170, progress=.25)]
        b += [figure(700, 682, 1.15, "stand", "serene", tilt=90)[0]]
    elif n == 16:
        b += [ico("thought", 1260, 330, 240, INK, .45, inner=False), acc("xmark", 1260, 320, 160, w=8)]
        b += [F(x=680, pose="explain", expr="attentive", look=6)[0]]
    elif n == 17:
        b += [ico("thought", 1100, 300, 200, INK, .12, inner=False), acc("gem", 1420, 400, 170)]
        b += [F(x=640, pose="point", expr="calm", look=6)[0]]
    elif n == 18:
        b += [ico("notebook", 960, 560, 760, INK, .9, w=5)]
        b += [line(1000, 470, 1240, 470, INK, 10, .18), line(1000, 560, 1240, 560, INK, 10, .18)]
        b += [f'<g data-acc="1120,650">' + glow(1120, 650, 200, "A", 1) + line(1000, 650, 1240, 650, ACC, 14) + "</g>"]
    elif n == 19:
        fig, an = F(x=720, pose="cheer", expr="proud")
        hx, hy = an["rhand"]
        b += [fig, acc("notebook", hx + 150, hy - 10, 170, lit=3)]
    elif n == 20:
        b += [floor_line(), ico("cloud", 1320, 450, 240, INK, .08), F(x=760, pose="stand", expr="neutral", look=6)[0]]
    elif n == 21:
        b += [acc("gem", 1380, 400, 200), F(x=760, pose="stand", expr="satisfied", look=6)[0]]
    # ---------------------------------------------------------------- ESCENA 4: HÁBITO 2
    elif n == 22:
        b += [floor_line(), chair(780, FLOOR, 1.12), ico("guitar", 1180, 760, 210, INK), ico("book", 1440, 820, 150, INK, .85, progress=.1)]
        b += [figure(790, FLOOR, 1.12, "sit", "attentive", look=6)[0]]
    elif n == 23:
        b += [ico("bubble", 1120, 300, 140, INK, .8), acc("note", 1340, 440, 140), ico("wrench", 1560, 300, 130, INK, .8)]
        b += [F(x=620, pose="explain", expr="attentive", look=6)[0]]
    elif n == 24:
        b += [acc("brain", 1380, 380, 240), F(x=760, pose="stand", expr="thoughtful", look=5)[0]]
    elif n == 25:
        b += [ico("brain", 1260, 420, 320, INK, .9), nodes(1260, 420, 120, seed=25)]
        b += [F(x=600, pose="stand", expr="attentive", look=6)[0]]
    elif n == 26:
        b += [floor_line(), ico("tag", 1650, 760, 110, INK, .14), acc("brain", 1380, 430, 220)]
        b += [figure(900, FLOOR, 1.12, "hands_hips", op=.5, ghost=True)[0]]
    elif n == 27:
        b += [acc("brain", 1300, 470, 250), F(x=640, pose="explain", expr="warm", look=5)[0]]
    elif n == 28:
        for gx, k in ((1130, 3), (1400, 4), (1670, 7)):
            for j in range(k):
                b += [f'<circle cx="{gx - (k - 1) * 13 + j * 26}" cy="830" r="8" fill="{INK}" opacity=".55"/>']
        b += [acc("brain", 1400, 360, 220), F(x=660, pose="stand", expr="calm", look=6)[0]]
    elif n == 29:
        b += [ico("brain", 1380, 300, 210, INK, .22), ico("guitar", 1480, 760, 170, INK, .35), ico("books", 1680, 800, 120, INK, .35)]
        b += [F(x=720, pose="hands_hips", expr="avoid", look=-6)[0]]
    elif n == 30:
        fig, an = F(x=760, pose="reach_down", expr="calm", look=6)
        hx, hy = an["rhand"]
        b += [ico("brain", 1380, 300, 200, INK, .4), ico("guitar", hx + 50, hy + 10, 200, INK, rot=-25), fig]
    elif n == 31:
        fig, an = F(x=700, pose="reach_down", expr="determined", look=6)
        hx, hy = an["rhand"]
        b += [floor_line(), acc("brain", 1400, 380, 220, glow_r=380), ico("guitar", hx + 40, hy, 160, INK, rot=-25), fig]
    elif n == 32:
        b += [ico("brain", 1380, 400, 300, INK, .9), nodes(1380, 400, 115, seed=32, w=5)]
        b += [F(x=720, pose="stand", expr="satisfied", look=6)[0]]
    # ---------------------------------------------------------------- ESCENA 5: HÁBITO 3
    elif n == 33:
        b += [floor_line(), ico("sun", 1500, FLOOR - 30, 330, INK, .5), acc("timer", 1180, 330, 150, progress=.3)]
        b += [F(x=760, pose="stride", expr="determined", look=6, tilt=6)[0]]
    elif n == 34:
        b += [ico("book", 1380, 470, 240, INK, .85, progress=0), acc("flame", 1380, 290, 120)]
        b += [F(x=760, pose="stand", expr="thoughtful", look=5)[0]]
    elif n == 35:
        b += [ico("brain", 1300, 450, 340, INK, .9)]
        b += [f'<g data-acc="1300,450">' + glow(1300, 450, 280, "A", .9) + "".join(
            place(x, y, 50, icon("spark", ACC, 7)) for x, y in ((1190, 360), (1400, 380), (1280, 520), (1420, 520), (1180, 500))) + "</g>"]
    elif n == 36:
        b += [ico("brain", 960, 440, 280, INK, .9), nodes(960, 440, 100, seed=36), particles(960, 440, 1100, 600, 80, seed=36)]
    elif n == 37:
        b += [floor_line(), ico("brain", 1300, 300, 240, INK, .85), glow(1250, 270, 70, "A", 1), glow(1360, 330, 70, "A", 1)]
        b += [nodes(1250, 270, 40, n=5, seed=37), nodes(1360, 330, 40, n=5, seed=73)]
        b += [F(x=620, pose="stride", expr="determined", look=6, tilt=6)[0]]
    elif n == 38:
        b += [floor_line(), rim(960, 520, 560), F(x=960, pose="walk", expr="attentive", look=4)[0]]
    elif n == 39:
        b += [ico("cloud", 1450, 260, 260, INK, .1), ico("cloud", 1450, 270, 120, INK, .55), acc("brain", 1300, 600, 170)]
        b += [F(x=700, pose="stand", expr="warm", look=6)[0]]
    elif n == 40:
        b += [dust(1350, 300, 320, 200, 60, seed=40, op=.4), F(x=760, pose="cheer", expr="smile")[0]]
    elif n == 41:
        b += [floor_line(), acc("sun", 360, FLOOR - 30, 300), ico("gym", 1450, 720, 230, INK, .18), ico("clock", 1650, 340, 150, INK, .18)]
        b += [F(x=820, pose="stride", expr="smile", look=6, tilt=6)[0]]
    elif n == 42:
        b += [acc("timer", 1320, 420, 190, progress=1.0), F(x=700, pose="hands_hips", expr="proud")[0]]
    elif n == 43:
        b += [acc("brain", 1380, 400, 240), place(1460, 320, 60, icon("spark", ACC, 7))]
        b += [F(x=740, pose="stand", expr="satisfied", look=6)[0]]
    # ---------------------------------------------------------------- ESCENA 6: HÁBITO 4
    elif n == 44:
        b += table_scene()
    elif n == 45:
        b += [timeline(1060, 760, 1860, 300, ticks=4, w=5), F(x=700, pose="stand", expr="thoughtful", look=6)[0]]
    elif n == 46:
        b += [timeline(160, 820, 1760, 820, ticks=3, w=5)]
        for k, x in enumerate((360, 760, 1160, 1560)):
            b += [figure(x - 70, 800, .55, "walk", op=.25, ghost=True)[0], figure(x + 70, 800, .55, "walk", op=.25, ghost=True)[0]]
            b += [figure(x, 800, .62, "walk", "calm", color=INK)[0]]
    elif n == 47:
        b += [ico("question", 1130, 420, 260, INK, .55), line(1260, 420, 1380, 420, INK, 6, .5, "12 10")]
        b += [acc("pair", 1500, 420, 150), F(x=600, pose="point", expr="attentive", look=6)[0]]
    elif n == 48:
        b += [floor_line(), ico("trophy", 1100, 520, 150, INK, .45), ico("coins", 1350, 520, 140, INK, .3), ico("briefcase", 1600, 520, 150, INK, .16)]
        b += [F(x=600, pose="stand", expr="neutral", look=6)[0]]
    elif n == 49:
        b += [acc("pair", 1380, 420, 240), F(x=720, pose="stand", expr="serene", look=6)[0]]
    elif n == 50:
        import random
        rnd = random.Random(50)
        for _ in range(22):
            b += [ico("person", rnd.uniform(1000, 1800), rnd.uniform(180, 800), rnd.uniform(40, 70), INK, .25)]
        b += [F(x=580, pose="hands_hips", expr="resigned", look=6)[0]]
    elif n == 51:
        import random
        rnd = random.Random(50)
        b += [floor_line()]
        for _ in range(22):
            b += [ico("person", rnd.uniform(1000, 1800), rnd.uniform(180, 800), rnd.uniform(40, 70), INK, .07)]
        b += [acc("pair", 1350, 540, 260), F(x=640, pose="stand", expr="calm", look=6)[0]]
    elif n == 52:
        fig, an = F(x=720, pose="reach", expr="warm", look=6)
        hx, hy = an["rhand"]
        b += [ico("bubble", 1180, 280, 130, INK, .18), fig, acc("call", hx + 80, hy - 20, 150)]
    elif n == 53:
        b += [glow(960, 600, 300, "warm", 1), line(260, 640, 1660, 640, INK, 10)]
        b += [f'<ellipse cx="760" cy="620" rx="150" ry="28" fill="none" stroke="{INK}" stroke-width="7"/>',
              f'<ellipse cx="1120" cy="620" rx="150" ry="28" fill="none" stroke="{INK}" stroke-width="7"/>']
        b += [ico("phone", 1530, 610, 120, INK, .35, rot=78)]
    elif n == 54:
        b += table_scene(660, 1260, ghost_op=.55, expr="warm")
    elif n == 55:
        b += [timeline(200, 360, 1720, 360, ticks=5, color=INK, w=4, op=.25), glow(960, 600, 320, "A", .7)]
        b += table_scene(640, 1280, ghost_op=.55, expr="serene")
    # ---------------------------------------------------------------- ESCENA 7: HÁBITO 5
    elif n == 56:
        b += [floor_line(), acc("wallet", 1160, 600, 170), F(x=720, pose="stand", expr="satisfied", look=6)[0]]
    elif n == 57:
        b += [ico("stream", 760, 460, 300, INK, .85), ico("bank", 1600, 460, 200, INK, .7)]
        b += [line(880, 500, 1180, 700, INK, 5, .45, "12 10"), acc("coin", 1100, 640, 70), ico("jar", 1260, 760, 210, INK, level=.15)]
    elif n == 58:
        b += [ico("stream", 700, 460, 320, INK, .85), ico("bank", 1500, 460, 220, INK, .6)]
        b += [line(850, 500, 960, 760, ACC, 6, .9, "12 10"), acc("coin", 960, 700, 90)]
    elif n == 59:
        b += [acc("medal", 1300, 420, 180), F(x=700, pose="explain", expr="thoughtful", look=5)[0]]
    elif n == 60:
        b += [acc("page", 1380, 380, 210), ico("arrow", 1380, 640, 130, INK, .7)]
        b += [F(x=740, pose="stand", expr="warm", look=6)[0]]
    elif n == 61:
        b += [floor_line(), ico("jar", 1300, 760, 220, INK, level=.04)]
        b += [figure(800, FLOOR, 1.12, "step_back", op=.5, ghost=True)[0]]
    elif n == 62:
        fig, an = F(x=600, pose="stand", expr="calm", look=6)
        tx, ty = an["top"]
        b += [fig, acc("arrow_up", tx, ty - 90, 110)]
        b += [ico("coin", 900, 480, 70, INK, .8), ico("coin", 1060, 590, 95, INK, .9), ico("jar", 1320, 700, 240, INK, level=.4)]
    elif n == 63:
        b += [floor_line(), ico("page", 1620, 300, 120, INK, .3, rot=-10), ico("page", 1730, 330, 120, INK, .2, rot=8)]
        b += [acc("jar", 1240, 640, 300, level=.9, fill=ACC), F(x=640, pose="stand", expr="satisfied", look=6)[0]]
    elif n == 64:
        b += [ico("bank", 1360, 500, 220, INK, .85), F(x=740, pose="shrug", expr="calm", look=5)[0]]
    elif n == 65:
        b += [acc("jar", 1380, 560, 320, level=1.0, fill=ACC), F(x=720, pose="stand", expr="satisfied", look=6)[0]]
    # ---------------------------------------------------------------- ESCENA 8: EL CIERRE
    elif n == 66:
        b += [F(x=760, pose="stand", expr="determined")[0], dots5(760, 430, 380, -48, 48)]
    elif n == 67:
        b += [ico("page", 1360, 640, 170, INK, .25, rot=-18), F(x=700, pose="dismiss", expr="calm", look=6)[0]]
    elif n == 68:
        b += [floor_line(), rim(960, 520, 600), dots5(960, 610, 430, 210, 330), F(x=960, pose="stand", expr="determined")[0]]
    elif n == 69:
        b += [acc("bubble", 1320, 360, 220), F(x=760, pose="point_you", expr="warm", look=3)[0]]
    elif n == 70:
        b += [floor_line(), acc("bell", 1260, 430, 150), F(x=860, pose="thumbs", expr="smile")[0]]
    elif n == 71:
        b += [rim(960, 500, 620), F(x=960, pose="stand", expr="serene")[0]]
    else:
        raise ValueError(n)
    return b


def thumb_b():
    """Mẫu B — triptych: viết nhật ký dưới đèn · chạy lúc bình minh · bữa ăn không điện thoại."""
    pw = TW / 3
    b = [panel_bg(0, 0, pw, TH, "#FFB46B", .3), panel_bg(pw, 0, pw, TH, "#7FB8FF", .26), panel_bg(2 * pw, 0, pw, TH, ACC, .3)]
    # 1: nhật ký dưới ánh đèn
    b += [glow(300, 300, 200, "warm", 1), desk(250, 400, 300), ico("lamp", 340, 330, 110), ico("notebook", 220, 380, 80, INK, lit=3)]
    b += [chair(90, 560, .9), figure(100, 560, .9, "type", "calm", look=5)[0]]
    # 2: chạy lúc bình minh
    b += [ico("sun", 640 + 110, 470, 200, INK, .55), line(pw + 20, 470, 2 * pw - 20, 470, INK, 4, .3)]
    b += [figure(600, 480, 1.0, "stride", "determined", look=6, tilt=8)[0]]
    # 3: bữa ăn với người đối diện, không điện thoại, 1 vật nhấn
    mid = 2 * pw + pw / 2
    b += [line(mid - 110, 400, mid + 110, 400, INK, 7), line(mid, 400, mid, 560, INK, 6)]
    b += [acc("flame", mid, 370, 40, glow_r=90)]
    b += [figure(mid - 130, 560, .85, "sit", "warm", look=6)[0], mirror(figure(mid + 130, 560, .85, "sit", "warm", op=.45, ghost=True)[0], mid + 130)]
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 3}" y="0" width="6" height="{TH}" fill="#000"/>')
    b.append(badge())
    return b


def thumb_c():
    """Mẫu C — lưới 6 khung: gratitud · aprender · ejercicio · relaciones · ahorro (không người) · cierre."""
    pw, ph = TW / 3, TH / 2
    tints = ("#FFB46B", "#5AC8C8", "#7FB8FF", "#FF8A6B", ACC, "#FFD9A0")
    b = [panel_bg((i % 3) * pw, (i // 3) * ph, pw, ph, t, .26) for i, t in enumerate(tints)]
    s = .66
    b += [glow(300, 200, 120, "warm", 1), ico("lamp", 330, 200, 80), ico("notebook", 250, 280, 60, INK, lit=3)]
    b += [chair(110, 330, s), figure(120, 330, s, "type", "calm", look=5)[0]]
    b += [ico("guitar", 760, 250, 130), figure(590, 330, s, "reach_down", "attentive", look=6)[0]]
    b += [ico("sun", 1150, 300, 130, INK, .5), figure(1020, 330, s, "stride", "determined", look=6, tilt=8)[0]]
    b += [line(213 - 70, 600, 213 + 70, 600, INK, 6), figure(213 - 90, 690, .58, "sit", "warm", look=6)[0],
          mirror(figure(213 + 90, 690, .58, "sit", "warm", op=.45, ghost=True)[0], 213 + 90)]
    b += [ico("jar", 640, 600, 150, INK, level=.5), acc("coin", 640, 470, 50, glow_r=80)]
    b += [ico("sun", 1066, 690, 220, INK, .45), figure(1066, 690, s, "stand", "serene")[0]]
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 1.5}" y="0" width="3" height="{TH}" fill="{BG}"/>')
    b.append(f'<rect x="0" y="{ph - 1.5}" width="{TW}" height="3" fill="{BG}"/>')
    b.append(badge())
    return b

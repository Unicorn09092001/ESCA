# -*- coding: utf-8 -*-
"""
scenes.py — Kịch bản hình của project 28 "7 Señales de Autosabotaje" (66 khung + 2 thumbnail).
Được tools/draw_frames.py, tools/animate_video.py và tools/make_thumbnails.py nạp tự động.
"""
from scenekit import *  # noqa: F401,F403
from sticklib import *  # noqa: F401,F403  (nạp lại ACC sau khi đã set_accent theo playlist)
from scenekit import FLOOR, boulder_on, ghost_ring, scale_with
from thumbkit import TH, TW, badge, panel_bg


def build_layers(n, shot):
    """Danh sách lớp SVG của khung n, theo thứ tự xuất hiện (dùng cho cả ảnh tĩnh và animation)."""
    F = lambda **kw: shot_fig(shot, **kw)  # noqa: E731
    b = []
    if n == 1:
        b += [floor_line(), line(380, FLOOR - 6, 1560, FLOOR - 6, INK, 4, .25, "18 16")]
        b += [acc("star", 1600, 600, 70, w=6)]
        b += [figure(1150, FLOOR, 1.12, "stand", op=.42, ghost=True)[0]]
        b += [F(x=720, pose="stand", expr="uneasy", look=5)[0]]
    elif n == 2:
        b += [glow(1180, 560, 430, "A", .55)]
        b += [dim("cloud", 560, 330, 240, .5), dim("xmark", 560, 330, 190, .7, w=6)]
        b += [dim("horseshoe", 560, 690, 190, .5), dim("xmark", 560, 690, 190, .7, w=6)]
        b += [F(x=1180, pose="stand", expr="confused", look=-4)[0]]
    elif n == 3:
        b += [figure(1420, 430 + 328 * 2.35, 2.35, "stand", op=.35, ghost=True)[0]]
        b += [crack(1300, 180, 1520, 900, seed=4)]
        b += [F(x=720, pose="stand", expr="realize", look=6)[0]]
    elif n == 4:
        b += [floor_line()]
        for i, (x, s) in enumerate(((330, .62), (610, .5), (1330, .5), (1610, .62))):
            b += [figure(x, FLOOR - 40 * (i % 2), s, "stand", "neutral", op=.22)[0],
                  figure(x + 120 * s, FLOOR - 40 * (i % 2), s, "stand", op=.16, ghost=True)[0]]
        b += [figure(1120, FLOOR, 1.5, "stand", op=.35, ghost=True)[0]]
        b += [F(x=880, pose="stand", expr="neutral", look=4)[0]]
    elif n == 5:
        b += [floor_line(), dots_arc(1000, 540, 330, a0=-60, a1=60)]
        b += [F(x=720, pose="explain", expr="calm", look=4)[0]]
    elif n == 6:
        b += [rim(960, 520, 560), F(x=960, pose="reassure", expr="warm")[0]]
    elif n == 7:
        b += [acc("eye", 1380, 330, 190), F(x=780, pose="stand", expr="attentive", look=6)[0]]
    elif n == 8:
        b += [rim(760, 500, 560), dots_arc(820, 560, 380, a0=-55, a1=55, size=15)]
        b += [F(x=760, pose="stand", expr="determined")[0]]
    elif n == 9:
        b += [floor_line(), desk(1120, 705, 560), chair(800, FLOOR, 1.12)]
        b += [ico("envelope", 980, 655, 75, INK, .5)]
        b += [acc("folder", 1260, 640, 120, fill=ACC)]
        b += [figure(810, FLOOR, 1.12, "type", "neutral", look=4)[0]]
    elif n == 10:
        b += [floor_line(), acc("folder", 1340, 640, 160, op=.55, fill=ACC)]
        b += [F(x=720, pose="hands_hips", expr="avoid", look=-6)[0]]
    elif n == 11:
        b += [ico("laptop", 1180, 760, 300)]
        for i, (x, y, o) in enumerate(((1300, 470, .5), (1480, 360, .32), (1650, 260, .18))):
            b += [ico("envelope", x, y, 110 - i * 15, INK, o)]
        b += [F(x=720, pose="type", expr="satisfied", look=5)[0]]
    elif n == 12:
        b += [floor_line(), ico("calendar", 1380, 430, 210, INK, .45, crossed=9)]
        b += [acc("folder", 960, 700, 220, star=True), dust(960, 690, 260, 140, 60, seed=12, op=.55)]
        b += [figure(480, FLOOR, 1.0, "hands_hips", "avoid", look=-6)[0]]
    elif n == 13:
        b += [acc("calendar", 1320, 420, 190, crossed=0)]
        b += [F(x=760, pose="explain", expr="thoughtful")[0]]
    elif n == 14:
        b += [acc("tag", 1380, 400, 220), F(x=760, pose="stand", expr="neutral", look=5)[0]]
    elif n == 15:
        b += [acc("folder", 1320, 560, 240, glow_r=470, fill=ACC)]
        b += [F(x=640, pose="stop", expr="squint", look=5)[0]]
    elif n == 16:
        b += [floor_line(), ico("shield", 940, 640, 230, INK, .9, fill=INK)]
        b += [acc("folder", 1380, 620, 170, fill=ACC)]
        b += [F(x=560, pose="cross", expr="defensive", look=5)[0]]
    elif n == 17:
        b += [ico("bubble", 1240, 300, 190, INK, .55), acc("bubble", 1560, 560, 190)]
        b += [F(x=720, pose="point", expr="calm", look=6)[0]]
    elif n == 18:
        b += [acc("folder", 1360, 560, 180, fill=ACC), F(x=760, pose="point", expr="attentive", look=6)[0]]
    elif n == 19:
        b += [floor_line(), ico("shield", 930, 620, 360, INK, .95, fill=INK)]
        b += [acc("folder", 1440, 560, 210, glow_r=430, fill=ACC)]
        b += [F(x=540, pose="stand", expr="calm", look=5)[0]]
    elif n == 20:
        b += [floor_line(), acc("door", 1450, FLOOR - 160, 320, w=6)]
        b += [dim("moon", 700, 500, 75, .4), dim("battery", 1080, 470, 75, .4), dim("blank", 650, 720, 60, .4)]
        b += [F(x=880, pose="stand", expr="resigned", look=5)[0]]
    elif n == 21:
        b += [floor_line(), acc("door", 1620, FLOOR - 160, 320, op=.5, w=6)]
        b += [ico("bubble", 1120, 300, 150, INK, .8), ico("bubble", 1300, 470, 120, INK, .55)]
        b += [F(x=760, pose="dismiss", expr="calm", look=5)[0]]
    elif n == 22:
        b += [acc("door", 1420, 560, 600, w=5), F(x=640, pose="stand", expr="resigned", look=6)[0]]
    elif n == 23:
        b += [floor_line(), acc("clock", 960, 330, 230)]
        b += [ico("door", 1300, FLOOR - 160, 320, INK, .8, w=6)]
        b += [line(1000, 600, 760, 600, INK, 5, .45, "14 12")]
        b += [F(x=700, pose="stand", expr="neutral", look=5)[0]]
    elif n == 24:
        b += [acc("shield", 960, 590, 640, op=.75, w=4)]
        b += [dim("moon", 740, 470, 60, .35), dim("battery", 1180, 470, 60, .35), dim("blank", 1170, 760, 50, .35)]
        b += [F(x=960, pose="stand", expr="calm")[0]]
    elif n == 25:
        b += [ico("door", 380, 520, 600, INK, .35, w=5)]
        b += [acc("shield", 1330, 520, 330, fill=ACC)]
        b += [figure(900, 430 + 328 * 2.35, 2.35, "stumble", "calm", look=6, tilt=12)[0]]
    elif n == 26:
        b += [figure(960, FLOOR, 1.5, "stand", op=.45, ghost=True)[0]]
        b += [acc("shield", 960, 560, 420, fill=ACC, w=5)]
    elif n == 27:
        b += [floor_line(), ico("door", 650, FLOOR - 160, 320, INK, .7, w=6)]
        b += [acc("star", 1020, 300, 120, fill=ACC)]
        b += [crowd([1420, 1560, 1700], FLOOR, .62, .25, poses=["explain_l", "cheer", "stand"])]
        b += [F(x=1020, pose="cheer", expr="proud")[0]]
    elif n == 28:
        b += [ico("shield", 1600, 720, 190, INK, .35), acc("star", 1330, 330, 230, glow_r=330, fill=ACC)]
        b += [F(x=720, pose="stand", expr="proud", look=5)[0]]
    elif n == 29:
        b += [floor_line(), acc("trophy", 1080, 760, 170)]
        b += [figure(1440, FLOOR, 1.05, "point_l", op=.42, ghost=True)[0]]
        b += [F(x=740, pose="stand", expr="neutral", look=5)[0]]
    elif n == 30:
        b += [ico("trophy", 1260, 620, 260, INK, .14), ico("trophy", 1260, 640, 180, INK, .22)]
        b += [acc("trophy", 1260, 660, 95)]
        b += [ico("bubble", 1040, 290, 120, INK, .7), ico("bubble", 1250, 230, 95, INK, .5)]
        b += [F(x=700, pose="dismiss", expr="uneasy", look=5)[0]]
    elif n == 31:
        b += [ico("calendar", 1360, 320, 210, INK, .5, crossed=12), acc("trophy", 1460, 720, 85)]
        b += [F(x=680, pose="stand", expr="worried", look=6)[0]]
    elif n == 32:
        b += [floor_line(), acc("humble", 1380, 440, 160, w=6)]
        b += [F(x=900, pose="explain", expr="calm")[0]]
    elif n == 33:
        b += [acc("trophy", 1320, 650, 95, op=.6), glow(1320, 650, 60, "A", .4)]
        b += [F(x=760, pose="hands_hips", expr="uneasy", look=-7)[0]]
    elif n == 34:
        b += [ico("trophy", 1310, 600, 290, INK, .12), ico("trophy", 1310, 610, 200, INK, .2)]
        b += [acc("trophy", 1310, 620, 90)]
        b += [line(1110, 620, 1200, 620, INK, 6, .55), line(1510, 620, 1420, 620, INK, 6, .55)]
        b += [F(x=680, pose="push", expr="uneasy", look=5)[0]]
    elif n == 35:
        b += [floor_line(), crowd([1220, 1380, 1540, 1700], FLOOR, .66, .14, poses=["explain_l", "stand"])]
        b += [acc("trophy", 930, 850, 50)]
        b += [F(x=600, pose="stand", expr="resigned", look=5)[0]]
    elif n == 36:
        b += [ghost_ring(960, 780, 600, 140, n=7, s=.66, op=.3, bubbles=True)]
        b += [figure(960, 860, 1.05, "stand", "sad")[0]]
        b += [acc("thought", 1060, 380, 110, inner=True)]
    elif n == 37:
        b += [ghost_ring(960, 900, 660, 110, n=7, s=.55, op=.2)]
        b += [acc("tag", 960, 170, 140)]
        b += [F(x=960, pose="explain", expr="thoughtful")[0]]
    elif n == 38:
        b += [ico("thought", 1380, 230, 270, INK, .55, inner=True)]
        b += [F(x=900, pose="stand", expr="sad", look=5)[0]]
    elif n == 39:
        b += [floor_line(), ghost_ring(1430, 860, 250, 70, n=5, s=.6, op=.28, skip_front=False)]
        b += [line(760, 640, 1120, 640, ACC, 6, .85, "16 14"), place(1140, 640, 50, icon("arrow", ACC, 8))]
        b += [F(x=560, pose="walk", expr="neutral", look=6, tilt=4)[0]]
    elif n == 40:
        b += [scale_with(1260, 600, 360, 20, left=("cloud", INK, 110, .9), right=("gem", ACC, 95, 1))]
        b += [F(x=620, pose="think", expr="thoughtful", look=5)[0]]
    elif n == 41:
        b += [ghost_ring(1440, 1000, 380, 80, n=5, s=.9, op=.18, skip_front=False)]
        b += [F(x=720, pose="stand", expr="realize", look=6)[0]]
    elif n == 42:
        b += [acc("brain", 960, 170, 170)]
        for x in (420, 700, 960, 1220, 1500):
            b += [line(960, 250, x, 560 if x != 960 else 470, INK, 3, .3, "6 10")]
        b += [ghost_ring(960, 900, 620, 90, n=6, s=.6, op=.25)]
        b += [figure(960, 900, 1.0, "stand", "neutral")[0]]
    elif n == 43:
        b += [floor_line(), place(520, 420, 150, icon("puzzle", INK, 6, gap=ACC)), glow(565, 375, 60, "A", .9)]
        b += [ico("book", 1400, 420, 150, INK, .9, progress=.88)]
        b += [ico("boxes", 520, 760, 150, INK, .8), ico("document", 1410, 760, 130, INK, .8)]
        b += [F(x=960, pose="shrug", expr="worried")[0]]
    elif n == 44:
        b += [ico("boxes", 640, 560, 300, INK, .85), ico("book", 1290, 540, 290, INK, .85, progress=.9, bar=ACC)]
        b += [glow(1290, 680, 160, "A", .5)]
    elif n == 45:
        b += [ico("folder", 960, 560, 520, INK, .4, star=False, w=5)]
        b += [acc("document", 960, 560, 220), dust(960, 520, 300, 260, 70, seed=45, op=.6)]
    elif n == 46:
        b += [rim(960, 500, 600), F(x=960, pose="think", expr="thoughtful")[0]]
    elif n == 47:
        b += [glow(1300, 560, 260, "A", .7)]
        b += [place(1300, 560, 270, icon("puzzle", INK, 6))]
        b += [f'<rect x="{1300 - 160}" y="{560 - 160}" width="320" height="320" rx="20" fill="none" stroke="{ACC}" stroke-width="6" stroke-dasharray="20 12"/>']
        b += [F(x=640, pose="explain", expr="satisfied", look=5)[0]]
    elif n == 48:
        b += [place(1340, 520, 320, icon("puzzle", INK, 6, missing=(-1, -1)))]
        b += [crack(1250, 380, 1300, 520, seed=48, w=4), crack(1400, 560, 1460, 680, seed=8, w=4)]
        b += [F(x=640, pose="stand", expr="uneasy", look=6)[0]]
    elif n == 49:
        b += [floor_line(), scale_with(1200, 640, 400, 18)]
        b += [F(x=560, pose="stand", expr="resigned", look=6)[0]]
    elif n == 50:
        b += [scale_with(1220, 600, 380, 18, left=("notes", INK, 130, .75))]
        b += [F(x=560, pose="stand", expr="worried", look=6)[0]]
    elif n == 51:
        b += [scale_with(960, 560, 600, 16,
                         left=[("question", INK, 85, .7), ("crumple", INK, 85, .7), ("raincloud", INK, 85, .7)])]
    elif n == 52:
        b += [floor_line(), scale_with(1200, 640, 420, 20, left=("notes", INK, 120, .6), right=("gem", ACC, 105, 1))]
        b += [F(x=500, pose="stand", expr="sad", look=6)[0]]
    elif n == 53:
        b += [scale_with(1340, 620, 330, 18, op=.4), acc("magnifier", 1020, 300, 120, op=.45)]
        b += [F(x=640, pose="step_back", expr="thoughtful", look=5)[0]]
    elif n == 54:
        b += [scale_with(1360, 560, 420, 18, color=ACC, op=.6, glow_it=True)]
        b += [F(x=700, pose="stand", expr="resigned", look=6)[0]]
    elif n == 55:
        fig, an = F(x=960, pose="carry", expr="sad")
        b += [floor_line(), boulder_on(an, 260), fig]
    elif n == 56:
        fig, an = F(x=760, pose="step_back", expr="defensive", look=6)
        b += [boulder_on(an, 280, .55), acc("hand", 1380, 470, 180, rot=-80), fig]
    elif n == 57:
        fig, an = F(x=680, pose="carry", expr="calm", look=6, head_y=560)
        b += [boulder_on(an, 420, .5)]
        b += [ico("bubble", 1250, 280, 190, INK, .85), ico("bubble", 1520, 470, 160, INK, .6), fig]
    elif n == 58:
        fig, an = F(x=760, pose="carry", expr="conflict", look=6)
        b += [floor_line(), boulder_on(an, 230), acc("hand", 1240, 560, 160, rot=-80), fig]
    elif n == 59:
        fig, an = F(x=760, pose="strain", expr="strain")
        b += [boulder_on(an, 400), acc("hand", 1420, 450, 150, op=.5, rot=-80), fig]
    elif n == 60:
        fig, an = F(x=760, pose="strain", expr="strain", head_y=640)
        b += [boulder_on(an, 620), acc("hand", 1550, 380, 150, op=.22, rot=-80), fig]
    elif n == 61:
        b += [floor_line(), dots_arc(960, 610, 430, a0=205, a1=335, size=14)]
        b += [F(x=960, pose="stand", expr="serene")[0]]
    elif n == 62:
        b += [glow(620, 640, 340, "A", .45), figure(620, FLOOR, .95, "stand", op=.5, ghost=True)[0]]
        b += [F(x=1180, pose="explain_l", expr="calm", look=-5)[0]]
    elif n == 63:
        b += [glow(420, 700, 260, "A", .25), figure(420, 1080, 1.2, "stand", op=.18, ghost=True)[0]]
        b += [F(x=1000, pose="stand", expr="serene", head_y=400)[0]]
    elif n == 64:
        b += [acc("bubble", 1320, 360, 220), F(x=760, pose="point_you", expr="warm", look=3)[0]]
    elif n == 65:
        b += [floor_line(), acc("bell", 1260, 430, 150), F(x=860, pose="thumbs", expr="smile")[0]]
    elif n == 66:
        fig, an = F(x=960, pose="stand", expr="serene")
        b += [rim(960, 500, 600), boulder_on(an, 260, .12), particles(960, 180, 560, 300, 80, seed=66), fig]
    else:
        raise ValueError(n)
    return b


def thumb_b():
    """Mẫu B — triptych 3 khung."""
    pw = TW / 3
    b = []
    tints = ("#3B6CFF", "#FFB46B", ACC)
    for i, t in enumerate(tints):
        b.append(panel_bg(i * pw, 0, pw, TH, t, .26 if i < 2 else .3))
    # 1: đứng trước laptop dự án quan trọng nhưng chần chừ, tay lơ lửng
    b += [desk(250, 395, 300), ico("laptop", 300, 345, 120), glow(300, 330, 90, "W", 1)]
    b += [figure(140, 520, .95, "reach", "uneasy", look=6)[0]]
    # 2: gạt đi lời khen, nhìn sang chỗ khác
    b += [ico("star", 640 + 120, 150, 70, INK, .6), ico("bubble", 640 + 110, 160, 150, INK, .55)]
    b += [figure(640 - 30, 540, 1.0, "dismiss", "avoid", look=-7)[0]]
    # 3: cạnh bức ghép gần xong, còn đúng 1 mảnh (màu nhấn)
    b += [place(1080, 300, 200, icon("puzzle", INK, 6, gap=ACC)), glow(1140, 240, 70, "A", 1)]
    b += [figure(940, 540, 1.0, "stand", "avoid", look=-6)[0]]
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 3}" y="0" width="6" height="{TH}" fill="#000"/>')
    b.append(badge())
    return b


def thumb_c():
    """Mẫu C — lưới 6 khung."""
    pw, ph = TW / 3, TH / 2
    b = []
    tints = ("#3B6CFF", "#FF6B6B", "#FFB46B", "#5AC8C8", ACC, "#FFD9A0")
    for i, t in enumerate(tints):
        b.append(panel_bg((i % 3) * pw, (i // 3) * ph, pw, ph, t, .24))
    s = .68
    # 1 procrastina lo importante
    b += [ico("laptop", 300, 250, 85), figure(130, 330, s, "sit_away", "distracted", look=-6)[0]]
    # 2 busca razones para fallar
    b += [ico("door", 760, 200, 170, INK, .55, w=6), figure(560, 330, s, "head_shake", "defensive", look=6)[0]]
    # 3 minimiza logros
    b += [ico("bubble", 1150, 110, 80, INK, .55), figure(1010, 330, s, "dismiss", "avoid", look=-6)[0]]
    # 4 rodeado de lo que confirma dudas
    for x in (60, 360):
        b += [figure(x, 690, .5, "stand", op=.28, ghost=True)[0]]
    b += [figure(213, 690, s, "stand", "sad")[0]]
    # 5 todo al 90% — puzzle sin una pieza, sin personaje
    b += [place(640, 540, 200, icon("puzzle", INK, 6, gap=ACC)), glow(700, 480, 70, "A", 1)]
    # 6 cierre: brazos cruzados, espejo detrás
    b += [glow(1066, 520, 150, "warm", 1), ico("mirror", 1130, 500, 200, INK, .35), figure(1040, 690, s, "cross", "determined")[0]]
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 1.5}" y="0" width="3" height="{TH}" fill="{BG}"/>')
    b.append(f'<rect x="0" y="{ph - 1.5}" width="{TW}" height="3" fill="{BG}"/>')
    b.append(badge())
    return b

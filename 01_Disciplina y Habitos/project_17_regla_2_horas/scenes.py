# -*- coding: utf-8 -*-
"""
scenes.py — Kịch bản hình của project 17 "La Regla de las 2 Horas" (57 khung + 2 thumbnail),
bám theo [VISUAL DESCRIPTION] trong transcript_and_visuals.txt. Màu nhấn #FF5A36 (01_Disciplina y Habitos).
Mô-típ xuyên suốt: trục ngày (mặt trời → mặt trăng), vùng 2 giờ được bảo vệ, thanh năng lực có giới hạn,
đường sóng hiệu suất đạt đỉnh sớm.
"""
from scenekit import *  # noqa: F401,F403
from sticklib import *  # noqa: F401,F403  (nạp lại ACC sau khi đã set_accent theo playlist)
from scenekit import FLOOR, marker
from thumbkit import TH, TW, badge, panel_bg

X0, X1 = 420, 1680  # trục ngày mặc định


def day_line(y=760, x0=X0, x1=X1, op=1.0, icons=True):
    out = [line(x0, y, x1, y, INK, 6, .55 * op)]
    for i in range(1, 8):
        x = x0 + (x1 - x0) * i / 8
        out.append(line(x, y - 14, x, y + 14, INK, 4, .35 * op))
    if icons:
        out += [ico("sun", x0 - 10, y - 80, 110, INK, .7 * op), ico("moon", x1, y - 80, 80, INK, .7 * op)]
    return "".join(out)


def zone(x0, x1, y=760, h=90, op=1.0, broken=False):
    """Vùng 2 giờ được bảo vệ trên trục ngày (vật nhấn, đập nhịp)."""
    cx = (x0 + x1) / 2
    if broken:
        return (f'<rect x="{x0}" y="{y - h / 2}" width="{x1 - x0}" height="{h}" rx="12" fill="none" stroke="{ACC}" '
                f'stroke-width="5" stroke-dasharray="14 12" opacity=".4"/>' + crack(x0 + 30, y - h / 2, x1 - 30, y + h / 2, seed=43, w=4))
    return (f'<g data-acc="{cx:.0f},{y}">' + glow(cx, y, (x1 - x0) * .9, "A", op)
            + f'<rect x="{x0}" y="{y - h / 2}" width="{x1 - x0}" height="{h}" rx="12" fill="{ACC}" fill-opacity=".35" '
              f'stroke="{ACC}" stroke-width="6" opacity="{op}"/></g>')


def capbar(x0, y, w=620, h=56, fill=.3, cap=True, color=None, op=1.0, ghost_full=False):
    """Thanh năng lực: khung đầy đủ + phần sáng (fill) + vạch giới hạn."""
    color = color or ACC
    out = []
    if ghost_full:
        out.append(f'<rect x="{x0}" y="{y - h / 2}" width="{w}" height="{h}" rx="{h / 2}" fill="{color}" opacity=".12"/>')
    out.append(f'<rect x="{x0}" y="{y - h / 2}" width="{w}" height="{h}" rx="{h / 2}" fill="none" stroke="{INK}" stroke-width="5" opacity="{.55 * op}"/>')
    fw = max(w * fill, h)
    tag = f'<g data-acc="{x0 + fw / 2:.0f},{y}">' if color == ACC else "<g>"
    out.append(tag + (glow(x0 + fw / 2, y, fw * .7, "A", op) if color == ACC else "")
               + f'<rect x="{x0 + 6}" y="{y - h / 2 + 6}" width="{fw - 12}" height="{h - 12}" rx="{h / 2 - 6}" fill="{color}" opacity="{op}"/></g>')
    if cap:
        out.append(line(x0 + fw, y - h, x0 + fw, y + h, INK, 4, .6, "8 8"))
    return "".join(out)


def wave(x0=X0, x1=X1, y=600, amp=230, op=1.0, w=9, color=None):
    """Đường hiệu suất: lên đỉnh sớm sau khi thức dậy, rồi giảm dần đến tối."""
    color = color or ACC
    pk = x0 + (x1 - x0) * .18
    d = (f"M{x0},{y} C{x0 + 80},{y - amp * .6} {pk - 80},{y - amp} {pk},{y - amp} "
         f"C{pk + 160},{y - amp} {x0 + (x1 - x0) * .45},{y - amp * .1} {x0 + (x1 - x0) * .62},{y + amp * .25} "
         f"S{x0 + (x1 - x0) * .85},{y + amp * .2} {x1},{y + amp * .45}")
    g = glow(pk, y - amp, 200, "A", op) if color == ACC else ""
    return (f'<g data-acc="{pk:.0f},{y - amp:.0f}">' + g
            + f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" opacity="{op}"/></g>'), pk, y - amp


DISTRACT = ("phone", "bubble", "bell", "envelope")


def build_layers(n, shot):
    F = lambda **kw: shot_fig(shot, **kw)  # noqa: E731
    b = []
    # ---------------------------------------------------------------- EL GANCHO
    if n == 1:
        b += [floor_line(), F(x=560, pose="stand", expr="satisfied", look=4)[0], acc("check", 560, 300, 110)]
        import random
        rnd = random.Random(1)
        for i in range(8):
            b += [ico(("task", "envelope", "bell", "bubble")[i % 4], 1300 + rnd.uniform(-260, 260), 360 + rnd.uniform(-160, 220), 60, INK, .35)]
        b += [F(x=1300, pose="hunch", expr="sad", look=-4)[0], ico("moon", 1700, 170, 70, INK, .5)]
    elif n == 2:
        for x in (640, 1280):
            fig, an = F(x=x, pose="stand", expr="neutral", look=4 if x < 960 else -4)
            tx, ty = an["top"]
            b += [fig, ico("brain", tx - 60, ty - 70, 80, INK, .6), ico("arrow", tx + 60, ty - 70, 80, INK, .6)]
    elif n == 3:
        b += [acc("shield", 760, 600, 900, op=.4, w=3), F(x=760, pose="stand", expr="determined", look=5)[0]]
    elif n == 4:
        b += [ico("shield", 1180, 520, 560, INK, .5, w=4), zone(1060, 1300, 520, 200)]
        b += [ico("phone", 1650, 300, 80, INK, .3), ico("bubble", 1680, 720, 90, INK, .3), ico("bell", 760, 260, 70, INK, .3)]
        b += [F(x=520, pose="stand", expr="calm", look=6)[0]]
    # ---------------------------------------------------------------- LA PROMESA
    elif n == 5:
        b += [day_line(650, 620, 1760), zone(640, 800, 650), F(x=330, pose="explain", expr="calm", look=6)[0]]
    elif n == 6:
        b += [capbar(1030, 480, 660, fill=.32), F(x=640, pose="explain", expr="thoughtful", look=6)[0]]
    elif n == 7:
        b += [day_line(700, 360, 1600), zone(370, 580, 700, 120)]
        b += [line(1350, 600, 700, 600, INK, 4, .4, "12 10"), place(690, 600, 50, icon("arrow", INK, 8), .5, 180)]
    elif n == 8:
        b += [day_line(760), ico("shield", 600, 640, 380, INK, .35, w=4), zone(470, 730, 760)]
        b += [ico(nm, x, y, 70, INK, .35) for nm, (x, y) in zip(DISTRACT, ((860, 560), (900, 720), (820, 470), (930, 640)))]
        b += [F(x=1460, pose="stand", expr="calm", look=-6)[0]]
    # ---------------------------------------------------------------- MÓDULO 1 — El Límite Real
    elif n == 9:
        b += [floor_line(), marker("1", 1280, 300), F(x=700, pose="explain", expr="attentive", look=6)[0]]
    elif n == 10:
        b += [acc("book", 1300, 440, 230, progress=0), F(x=700, pose="explain", expr="thoughtful", look=5)[0]]
    elif n == 11:
        b += [ico("clock", 960, 520, 420, INK, .3), acc("xmark", 960, 520, 300, w=8)]
    elif n == 12:
        b += [day_line(700), zone(X0, X0 + (X1 - X0) * .22, 700)]
    elif n == 13:
        b += [day_line(700, op=.6), zone(X0, X0 + (X1 - X0) * .22, 700, h=120)]
        b += [glow(X0 + 140, 700, 420, "A", .5)]
    elif n == 14:
        b += [capbar(360, 500, 1200, h=80, fill=.35)]
        b += [f'<path d="M{360 + 1200 * .35},{560} Q{360 + 1200 * .45},{620} {360 + 1200 * .6},{760}" fill="none" stroke="{INK}" stroke-width="6" opacity=".6"/>']
    elif n == 15:
        b += [ico("muscle", 1350, 640, 170, INK, .3, rot=-12), F(x=760, pose="explain", expr="determined", look=6)[0]]
    elif n == 16:
        b += [acc("brain", 900, 480, 260), ico("muscle", 1300, 520, 180, INK, .55)]
    elif n == 17:
        b += [capbar(1180, 420, 520, fill=.32, h=60), F(x=700, pose="stand", expr="realize", look=6)[0]]
    elif n == 18:
        b += [day_line(700, 700, 1760)]
        for x in (760, 1100, 1440):
            b += [f'<rect x="{x}" y="660" width="220" height="80" rx="12" fill="none" stroke="{INK}" stroke-width="4" stroke-dasharray="10 10" opacity=".5"/>']
        b += [acc("question", 1210, 470, 90), F(x=420, pose="point", expr="thoughtful", look=6)[0]]
    # ---------------------------------------------------------------- MÓDULO 2 — Las Primeras 2 Horas
    elif n == 19:
        b += [day_line(820, 760, 1780), marker("2", 1280, 360), F(x=460, pose="explain", expr="calm", look=6)[0]]
    elif n == 20:
        b += [acc("scatter", 1300, 440, 220), F(x=700, pose="explain", expr="thoughtful", look=5)[0]]
    elif n == 21:
        w, _, _ = wave(260, 1660, 640, 300)
        b += [w]
    elif n == 22:
        w, px, py = wave(X0, X1, 640, 260)
        b += [day_line(840, op=.7), w, F(x=1560, pose="point_l", expr="attentive", look=-6)[0]]
    elif n == 23:
        w, px, py = wave(X0, X1, 640, 260)
        b += [day_line(840), w, ico("sun", px, py - 140, 120, INK, .9)]
    elif n == 24:
        w, px, py = wave(200, 1700, 560, 300)
        b += [w, ico("moon", 1720, 820, 110, INK, .9)]
    elif n == 25:
        b += [floor_line(), ico("sofa", 1300, 700, 200, INK, .35), acc("xmark", 1300, 680, 180, w=8)]
        b += [F(x=700, pose="stand", expr="neutral", look=6)[0]]
    elif n == 26:
        b += [capbar(380, 640, 900, fill=.45)]
        for i, (nm, x) in enumerate((("envelope", 460), ("bell", 600), ("signpost", 740))):
            b += [line(x, 600, x, 420, INK, 3, .4, "8 8"), ico(nm, x, 360, 80, INK, .55)]
        b += [ico("task", 1520, 640, 160, INK, .25)]
    elif n == 27:
        b += [capbar(300, 560, 900, h=70, fill=.15), ico("task", 1500, 520, 300, INK, .4)]
    elif n == 28:
        b += [floor_line(), ico("clock", 1340, 640, 160, INK, .25, rot=-10), F(x=760, pose="explain", expr="determined", look=6)[0]]
    elif n == 29:
        w, px, py = wave(X0, 1380, 640, 260)
        b += [w, line(px + 60, py, 1500, py + 40, INK, 4, .6, "12 10"), ico("task", 1600, py + 60, 170, INK)]
    elif n == 30:
        b += [ico("shield", 960, 540, 640, INK, .35, w=4), zone(780, 1140, 540, 240)]
        b += [ico(nm, x, y, 90, INK, .4) for nm, (x, y) in zip(DISTRACT, ((520, 360), (1420, 360), (520, 760), (1420, 760)))]
    # ---------------------------------------------------------------- MÓDULO 3 — Cómo Proteger
    elif n == 31:
        b += [day_line(820, 760, 1780), zone(760, 980, 820), marker("3", 1300, 360), F(x=460, pose="explain", expr="calm", look=6)[0]]
    elif n == 32:
        b += [ico("moon", 1700, 170, 80, INK, .5)]
        for x, y in ((1180, 360), (1480, 360), (1180, 640), (1480, 640)):
            if (x, y) == (1480, 360):
                b += [acc("task", x, y, 120), f'<circle cx="{x}" cy="{y}" r="100" fill="none" stroke="{ACC}" stroke-width="6"/>']
            else:
                b += [ico("task", x, y, 110, INK, .3)]
        b += [F(x=640, pose="point", expr="calm", look=6)[0]]
    elif n == 33:
        import random
        rnd = random.Random(33)
        b += [ico("signpost", 960 + rnd.uniform(-700, 700), 540 + rnd.uniform(-380, 380), rnd.uniform(60, 100), INK, .3) for _ in range(14)]
        b += [figure(960, 430 + 328 * 2.35, 2.35, "hunch", op=.45, ghost=True)[0]]
    elif n == 34:
        b += [floor_line(), desk(420, 705, 360)]
        b += [f'<rect x="1380" y="420" width="380" height="485" fill="none" stroke="{INK}" stroke-width="5" stroke-dasharray="16 12" opacity=".45"/>']
        fig, an = F(x=1020, pose="reach", expr="determined", look=6)
        hx, hy = an["rhand"]
        b += [fig, acc("phone", hx + 50, hy - 10, 90)]
    elif n == 35:
        b += [desk(760, 760, 600), ico("phone", 860, 718, 70, INK, .45, rot=90), capbar(1120, 380, 560, fill=.6)]
        b += [line(900, 690, 1180, 420, INK, 3, .4, "6 8")]
    elif n == 36:
        b += [ico("bubble", 300, 360, 90, INK, .35), ico("bell", 420, 520, 80, INK, .35), ico("envelope", 280, 640, 80, INK, .35)]
        b += [zone(1380, 1700, 720, 200), F(x=900, pose="stand", expr="determined", look=6)[0]]
    elif n == 37:
        b += [acc("bell", 760, 460, 170, op=.6), ico("timer", 1240, 460, 230, INK, .35, progress=.3)]
        b += [line(860, 460, 1080, 460, INK, 4, .4, "10 10")]
    elif n == 38:
        d = "M260,420 L700,420 L760,760 C900,760 1100,640 1300,520 L1700,430"
        b += [f'<g data-acc="760,700">' + glow(760, 700, 260, "A", .7) + f'<path d="{d}" fill="none" stroke="{ACC}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></g>']
        b += [line(260, 860, 1700, 860, INK, 4, .4)]
    elif n == 39:
        b += [ico("browser", 960, 540, 760, INK, .9, w=5, tabs=4)]
        for i in range(1, 4):
            b += [ico("xmark", 960 + (-38 + i * 24) * 7.6, 540 - 37 * 7.6, 60, INK, .6)]  # tab i bị đóng
        b += [acc("task", 960, 600, 200)]
    elif n == 40:
        b += [ico("browser", 960, 540, 760, INK, .9, w=5, tabs=1), acc("task", 960, 600, 220)]
    elif n == 41:
        b += [capbar(560, 540, 800, h=70, fill=.55)]
        for x, y in ((420, 260), (1500, 260), (420, 820), (1500, 820)):
            b += [ico("browser", x, y, 140, INK, .4, tabs=2), line(x, y, 960, 540, INK, 2, .25)]
    elif n == 42:
        b += [capbar(1150, 420, 520, fill=.4, h=60), F(x=700, pose="stand", expr="calm", look=6)[0]]
    # ---------------------------------------------------------------- MÓDULO 4 — Si No las Proteges
    elif n == 43:
        b += [day_line(820, 760, 1780), zone(760, 980, 820, broken=True), marker("4", 1300, 360), F(x=460, pose="stand", expr="worried", look=6)[0]]
    elif n == 44:
        b += [floor_line(), bed(560, 1360, 690)]
        fig, an = figure(700, 682, 1.15, "stand", "neutral", tilt=90)
        b += [fig, acc("phone", 1460, 560, 100)]
        b += [f'<g data-dot="{i}">' + place(1460 + dx, 380 + dy, 70, icon(nm, INK, 7)) + "</g>"
              for i, (nm, dx, dy) in enumerate((("bubble", -150, 0), ("bubble", 0, -60), ("bubble", 150, 0), ("bell", 260, 100)))]
    elif n == 45:
        b += [capbar(300, 540, 1300, h=90, fill=.22, ghost_full=True)]
    elif n == 46:
        import random
        rnd = random.Random(46)
        b += [ico(("signpost", "bell", "envelope", "bubble")[i % 4], 300 + rnd.uniform(0, 1000), 200 + rnd.uniform(0, 640), 70, INK, .3) for i in range(16)]
        b += [ico("task", 1560, 540, 200, INK, .8)]
    elif n == 47:
        b += [day_line(700, 360, 1760)]
        b += [f'<rect x="900" y="640" width="840" height="120" rx="14" fill="{INK}" opacity=".06"/>']
        b += [F(x=360, pose="point", expr="neutral", look=6)[0]]
    elif n == 48:
        b += [capbar(260, 560, 900, h=80, fill=.4)]
        b += [ico(nm, 320 + i * 100, 450, 60, INK, .8) for i, nm in enumerate(("envelope", "bell", "bubble"))]
        b += [ico("task", 1560, 560, 220, INK, .3)]
    elif n == 49:
        b += [floor_line(), ico("brain", 800, 560, 240, INK, .3), ico("task", 1240, 560, 220, INK, .8)]
    elif n == 50:
        b += [day_line(860, 200, 1720, icons=False, op=.6)]
        b += [place(260 + i * 120, 800, 40, icon("check", INK, 8), .45) for i in range(13)]
        b += [F(x=960, pose="hunch", expr="resigned", look=4)[0]]
    elif n == 51:
        b += [ico("task", 1380, 520, 240, INK, .8), ico("moon", 1600, 200, 90, INK, .6), F(x=720, pose="stand", expr="resigned", look=6)[0]]
    # ---------------------------------------------------------------- EL CIERRE
    elif n == 52:
        b += [floor_line(), figure(1380, FLOOR, 1.05, "cross", op=.2, ghost=True)[0], F(x=700, pose="stand", expr="calm", look=4)[0]]
    elif n == 53:
        w, _, _ = wave(820, 1760, 560, 220, op=.8)
        b += [w, F(x=480, pose="stand", expr="calm", look=6)[0]]
    elif n == 54:
        b += [zone(1180, 1600, 640, 220), ico("task", 1390, 600, 160, INK)]
        b += [F(x=720, pose="reach", expr="satisfied", look=6)[0]]
    elif n == 55:
        b += [rim(500, 520, 520), day_line(800, 860, 1780), zone(860, 1080, 800), F(x=500, pose="stand", expr="determined", look=6)[0]]
    elif n == 56:
        b += [floor_line(), acc("bell", 1260, 430, 150), F(x=860, pose="thumbs", expr="smile")[0]]
    elif n == 57:
        b += [rim(960, 500, 620), F(x=960, pose="stand", expr="serene")[0]]
    else:
        raise ValueError(n)
    return b


def thumb_b():
    """Mẫu B — triptych: anotar la tarea la noche anterior · llevar el teléfono a otra habitación · cerrar pestañas (vật nhấn)."""
    pw = TW / 3
    b = [panel_bg(0, 0, pw, TH, "#8C7BFF", .24), panel_bg(pw, 0, pw, TH, "#7FB8FF", .24), panel_bg(2 * pw, 0, pw, TH, "#FFB46B", .3)]
    # 1: nhật ký trên giường, buổi tối
    b += [ico("moon", 340, 120, 60, INK, .6), f'<rect x="120" y="440" width="290" height="36" rx="10" fill="none" stroke="{INK}" stroke-width="7"/>',
          line(120, 390, 120, 560, INK, 7), line(410, 460, 410, 560, INK, 7), ico("notebook", 330, 380, 70, INK, lit=1)]
    b += [figure(230, 450, .75, "type", "calm", look=5)[0]]
    # 2: mang điện thoại sang phòng khác
    b += [f'<rect x="{pw + 250}" y="190" width="150" height="370" fill="none" stroke="{INK}" stroke-width="5" stroke-dasharray="12 10" opacity=".5"/>']
    fig, an = figure(pw + 160, 560, .95, "reach", "determined", look=6)
    b += [fig, ico("phone", an["rhand"][0] + 30, an["rhand"][1], 50, INK)]
    # 3: bàn sạch buổi sáng, đóng tab — vật nhấn
    mid = 2 * pw + pw / 2
    b += [ico("sun", mid + 120, 140, 90, INK, .5), desk(mid + 40, 420, 300), ico("browser", mid + 70, 350, 120, INK, tabs=1), acc("task", mid + 70, 360, 45, glow_r=90)]
    b += [chair(mid - 150, 560, .9), figure(mid - 140, 560, .9, "type", "determined", look=5)[0]]
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 3}" y="0" width="6" height="{TH}" fill="#000"/>')
    b.append(badge())
    return b


def thumb_c():
    """Mẫu C — lưới 6 khung."""
    pw, ph = TW / 3, TH / 2
    tints = ("#FF8A6B", "#FFD9A0", "#7FB8FF", "#5AC8C8", "#8C7BFF", "#FFB46B")
    b = [panel_bg((i % 3) * pw, (i // 3) * ph, pw, ph, t, .24) for i, t in enumerate(tints)]
    s = .66
    b += [acc("hourglass", 213, 180, 200)]                                                       # 1 el límite real
    b += [ico("sun", 760, 250, 110, INK, .5), line(470, 300, 690, 300, INK, 6),
          figure(560, 300, .55, "sit", "attentive", look=6)[0]]                                  # 2 primeras 2 horas
    b += [ico("drawer", 1180, 260, 120, INK), ico("phone", 1180, 160, 50, INK, .8, rot=90),
          figure(990, 330, s, "reach", "determined", look=6)[0]]                                 # 3 protege el bloque
    b += [desk(260, 600, 220), ico("task", 290, 555, 60, INK), chair(110, 690, .66), figure(120, 690, s, "type", "determined", look=5)[0]]  # 4 una tarea
    b += [ico("phone", 640, 540, 220, INK, .8)] + [ico(nm, 640 + dx, 520 + dy, 34, INK, .8)
                                                    for nm, dx, dy in (("bell", -20, -50), ("bubble", 22, -10), ("envelope", -18, 30), ("bell", 20, 60))]  # 5
    b += [ico("hourglass", 1180, 560, 120, INK, .45), figure(1040, 690, s, "stand", "satisfied", look=6)[0]]  # 6 cierre
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 1.5}" y="0" width="3" height="{TH}" fill="{BG}"/>')
    b.append(f'<rect x="0" y="{ph - 1.5}" width="{TW}" height="3" fill="{BG}"/>')
    b.append(badge())
    return b

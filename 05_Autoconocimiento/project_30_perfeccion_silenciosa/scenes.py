# -*- coding: utf-8 -*-
"""
scenes.py — Kịch bản hình của project 30 "¿Por Qué Nunca Sientes Que Es Suficiente? (Perfeccionismo)"
(48 khung + 2 thumbnail), bám theo [VISUAL DESCRIPTION] trong transcript_and_visuals.txt.
Màu nhấn #8B6CFF (05_Autoconocimiento).
Mô-típ: nút thắt căng thẳng phát sáng trong ngực (chỉ mình mình thấy) · 5 chấm vòng cung · cột mốc mục tiêu cứ trôi xa ·
trang trắng không dám bắt đầu · kính lúp soi tài liệu đã xong · 9 lời khen + 1 góp ý · "bản thân lý tưởng" luôn đi trước một bước ·
thước đo dài vô tận cuối cùng có điểm kết.
"""
from scenekit import *  # noqa: F401,F403
from sticklib import *  # noqa: F401,F403  (nạp lại ACC sau khi đã set_accent theo playlist)
from scenekit import FLOOR, desk, marker
from thumbkit import TH, TW, badge, panel_bg


def knot(x, y, size=40, op=1.0):
    """Nút thắt căng thẳng phát sáng trong ngực."""
    s = size
    return (f'<g data-acc="{x:.0f},{y:.0f}">' + glow(x, y, s * 2.2, "A", .7 * op)
            + f'<path d="M{x - s:.0f},{y:.0f} C{x - s:.0f},{y - s:.0f} {x + s * .6:.0f},{y - s:.0f} {x + s * .4:.0f},{y:.0f} '
              f'C{x + s * .2:.0f},{y + s:.0f} {x - s * .8:.0f},{y + s * .6:.0f} {x - s * .3:.0f},{y - s * .2:.0f} '
              f'C{x + s * .2:.0f},{y - s * .9:.0f} {x + s:.0f},{y - s * .2:.0f} {x + s * .8:.0f},{y + s * .5:.0f}" '
              f'fill="none" stroke="{ACC}" stroke-width="4" opacity="{op}" stroke-linecap="round"/></g>')


def fig_knot(F, x, pose="stand", expr="calm", look=0, op=1.0, **kw):
    fig, an = F(x=x, pose=pose, expr=expr, look=look, **kw)
    sx, sy = an["sh"]
    hx, hy = an["hip"]
    return fig + knot((sx + hx) / 2, sy + (hy - sy) * .3, 26 * (hy - sy) / 150, op), an


def dots5(cx, cy, r, a0=200, a1=340, lit=None):
    return dots_arc(cx, cy, r, n=5, a0=a0, a1=a1, size=16, lit=lit)


def flag(x, y, size=90, op=1.0, color=INK):
    return (f'<g opacity="{op}"><line x1="{x}" y1="{y + size * .5:.0f}" x2="{x}" y2="{y - size * .5:.0f}" stroke="{color}" stroke-width="5"/>'
            f'<path d="M{x},{y - size * .5:.0f} L{x + size * .5:.0f},{y - size * .35:.0f} L{x},{y - size * .2:.0f} Z" fill="{color}"/></g>')


def ruler(x0, y, x1, ended=False, op=.8):
    out = [f'<rect x="{x0}" y="{y - 30}" width="{x1 - x0}" height="60" rx="6" fill="none" stroke="{INK}" stroke-width="4" opacity="{op}"/>']
    for i, x in enumerate(range(x0 + 20, x1, 40)):
        out.append(f'<line x1="{x}" y1="{y - 30}" x2="{x}" y2="{y - 30 + (26 if i % 5 == 0 else 14)}" stroke="{INK}" stroke-width="3" opacity="{op}"/>')
    if ended:
        out.append(f'<g data-acc="{x1},{y}">' + glow(x1, y, 120, "A", .9) + f'<line x1="{x1}" y1="{y - 70}" x2="{x1}" y2="{y + 70}" stroke="{ACC}" stroke-width="9" stroke-linecap="round"/></g>')
    else:
        out.append(f'<g data-flow="1"><line x1="{x1 + 10}" y1="{y}" x2="{x1 + 260}" y2="{y}" stroke="{INK}" stroke-width="4" opacity=".4" stroke-dasharray="10 14"/></g>')
    return "".join(out)


def page(x, y, w=200, lit=False, rough=False, op=1.0):
    col = ACC if lit else INK
    h = w * 1.3
    out = f'<rect x="{x - w / 2:.0f}" y="{y - h / 2:.0f}" width="{w:.0f}" height="{h:.0f}" rx="10" fill="{BG}" stroke="{col}" stroke-width="5" opacity="{op}"/>'
    if rough:
        out += "".join(f'<path d="M{x - w * .35:.0f},{y - h * .3 + i * h * .16:.0f} q{w * .1:.0f},-8 {w * .2:.0f},0 t{w * .2:.0f},0 t{w * .2:.0f},0" fill="none" stroke="{INK}" stroke-width="3" opacity="{op * .7:.2f}"/>' for i in range(4))
    return (f'<g data-acc="{x:.0f},{y:.0f}">' + glow(x, y, w * .9, "A", .6) + out + "</g>") if lit else out


def praise_ring(cx, cy, r, crit_scale=1.0, praise_op=.8, show_praise=True):
    out = []
    if show_praise:
        for i in range(9):
            a = math.radians(-90 + 36 * i)
            out.append(ico("star", cx + r * math.cos(a), cy + r * .8 * math.sin(a), 70, INK, praise_op))
    a = math.radians(-90 + 36 * 9)
    x, y = (cx + r * math.cos(a), cy + r * .8 * math.sin(a)) if crit_scale < 1.5 else (cx + 260, cy)
    out.append(acc("xmark", x, y, 60 * crit_scale) if crit_scale > 1 else ico("xmark", x, y, 60, INK, .6))
    return "".join(out)


def build_layers(n, shot):
    F = lambda **kw: shot_fig(shot, **kw)  # noqa: E731
    b = []
    # ---------------------------------------------------------------- GANCHO
    if n == 1:
        b += [floor_line(), ico("trophy", 1080, 640, 160, INK), flag(1620, 560, 110, .35), F(x=700, pose="stand", expr="neutral", look=6)[0]]
    elif n == 2:
        b += [ico("heart", 1260, 380, 110, INK, .3), line(1200, 430, 1320, 330, INK, 5, .5), ico("arrow_up", 1500, 600, 110, INK, .3), line(1440, 650, 1560, 550, INK, 5, .5),
              F(x=680, pose="stand", expr="calm", look=6)[0]]
    elif n == 3:
        f, an = fig_knot(F, 960, "stand", "neutral")
        b += [f]
    elif n == 4:
        f, an = fig_knot(F, 1300, "stand", "calm", look=-5)
        b += [desk(700, 760, 420), ico("document", 600, 720, 70, INK, .6, rot=-12), ico("notes", 760, 726, 60, INK, .5, rot=18), ico("pill", 830, 740, 40, INK, .4), f]
    # ---------------------------------------------------------------- PROMESA
    elif n == 5:
        b += [floor_line(), dots5(1300, 700, 360), F(x=620, pose="explain", expr="calm", look=6)[0]]
    elif n == 6:
        b += [figure(1300, FLOOR, 1.1, "stand", "squint", op=.3, ghost=True)[0], ico("check", 1460, 420, 70, INK, .25),
              F(x=640, pose="dismiss", expr="calm", look=6)[0]]
    elif n == 7:
        f, an = fig_knot(F, 960, "hands_hips", "calm", op=.7)
        b += [floor_line(), f]
    # ---------------------------------------------------------------- SEÑAL 1 — Nunca es suficiente
    elif n == 8:
        b += [floor_line(), marker(1, 1500, 340, 160), acc("trophy", 1180, 640, 160), F(x=760, pose="walk", expr="neutral", look=-6)[0]]
    elif n == 9:
        b += [ico("trophy", 760, 560, 110, INK, .3), acc("task", 1220, 460, 220), line(870, 540, 1080, 480, INK, 4, .4, "8 10")]
    elif n == 10:
        fig, an = F(x=960, pose="stand", expr="neutral")
        b += [glow(960, 520, 520, "warm", .45), fig] + [f'<circle cx="{960 + 330 * math.cos(math.radians(a)):.0f}" cy="{520 + 300 * math.sin(math.radians(a)):.0f}" r="6" fill="#FFD9A0" opacity=".35"/>' for a in range(0, 360, 30)]
    elif n == 11:
        b += [line(1000, 760, 1720, 760, INK, 3, .3), line(1000, 760, 1000, 300, INK, 3, .3),
              f'<g data-acc="1400,520">' + glow(1400, 520, 200, "A", .5) + f'<path d="M1020,720 L1180,680 L1320,600 L1460,520 L1600,400 L1700,330" stroke="{ACC}" stroke-width="7" fill="none" stroke-linejoin="round"/></g>',
              F(x=560, pose="explain", expr="thoughtful", look=6)[0]]
    elif n == 12:
        b += [F(x=960, pose="stand", expr="uneasy")[0]]
        for i, (x, y) in enumerate(((420, FLOOR), (640, FLOOR), (1280, FLOOR), (1500, FLOOR))):
            fig, an = figure(x, y, .8, "stand", "neutral", op=.25, ghost=True)
            b += [fig, ico("thought", an["top"][0], an["top"][1] - 70, 90, INK, .25), ico("star", an["top"][0], an["top"][1] - 74, 30, INK, .3)]
    elif n == 13:
        b += [ico("thought", 1300, 380, 220, INK, .35), ico("question", 1300, 375, 80, INK, .45), F(x=700, pose="stand", expr="realize", look=6)[0]]
    elif n == 14:
        b += [acc("trophy", 640, 560, 180)] + [flag(1100 + i * 220, 520 - i * 40, 100, .45 - i * .12) for i in range(3)]
        b += [line(760, 560, 1060, 540, INK, 3, .3, "6 10")]
    # ---------------------------------------------------------------- SEÑAL 2 — Empezar imperfecto
    elif n == 15:
        fig, an = F(x=700, pose="reach", expr="worried", look=6)
        b += [floor_line(), marker(2, 1560, 300, 150), fig, page(an["rhand"][0] + 240, an["rhand"][1] - 40, 220, lit=True)]
    elif n == 16:
        b += [ico("sofa", 1320, 520, 200, INK, .3), line(1200, 620, 1440, 420, INK, 6, .5), F(x=700, pose="dismiss", expr="calm", look=6)[0]]
    elif n == 17:
        b += [page(900, 500, 260, rough=True, op=.7), page(1020, 500, 260, lit=True, op=.8), ico("question", 1300, 260, 80, INK, .5)]
    elif n == 18:
        b += [acc("scale", 1300, 480, 220), F(x=680, pose="explain", expr="thoughtful", look=6)[0]]
    elif n == 19:
        fig, an = F(x=860, pose="stand", expr="strain")
        b += [fig, f'<g data-acc="1280,180">' + glow(1280, 180, 160, "A", .7) + f'<line x1="1140" y1="180" x2="1420" y2="180" stroke="{ACC}" stroke-width="9" stroke-linecap="round"/></g>',
              line(1280, 200, 1280, 840, INK, 3, .25, "8 12")]
    elif n == 20:
        b += [figure(1200, FLOOR + 40, 2.0, "stand", "squint", op=.12, ghost=True)[0], F(x=760, pose="hunch", expr="sad", look=4)[0]]
    elif n == 21:
        fig, an = F(x=900, pose="walk", expr="determined", look=6)
        b += [floor_line(), fig, page(an["rhand"][0] + 90, an["rhand"][1] - 30, 110, rough=True), acc("arrow_up", 1500, 400, 90)]
    # ---------------------------------------------------------------- SEÑAL 3 — Revisas sin parar
    elif n == 22:
        fig, an = figure(820, FLOOR, 1.2, "type", "uneasy", look=6)
        b += [desk(1060, 760, 440), chair(810, FLOOR, 1.2), fig, marker(3, 1560, 300, 150), acc("document", 1180, 690, 120)]
    elif n == 23:
        b += [ico("document", 960, 500, 300, INK, .9), acc("magnifier", 1060, 420, 200)]
    elif n == 24:
        b += [ico("envelope", 960, 460, 280, INK, .9)] + [f'<g data-dot="{i}">' + acc("check", 700 + i * 130, 760, 60, glow_r=50) + "</g>" for i in range(5)]
    elif n == 25:
        b += [f'<rect x="560" y="300" width="800" height="440" rx="20" fill="none" stroke="{INK}" stroke-width="5" opacity=".8"/>']
        b += [f'<rect x="{620 + k * 160}" y="420" width="130" height="24" rx="12" fill="{ACC if k == 2 else INK}" opacity="{1 if k == 2 else .5}"/>' for k in range(4)]
        b += [f'<rect x="620" y="520" width="{560}" height="24" rx="12" fill="{INK}" opacity=".35"/>']
    elif n == 26:
        b += [f'<rect x="560" y="300" width="800" height="440" rx="20" fill="none" stroke="{INK}" stroke-width="5" opacity=".8"/>']
        b += [f'<rect x="{620 + k * 160}" y="420" width="130" height="24" rx="12" fill="{INK}" opacity=".5"/>' for k in (0, 1, 3)]
        b += [f'<g data-acc="1005,432">' + glow(1005, 432, 120, "A", .8) + f'<rect x="940" y="420" width="130" height="24" rx="12" fill="{ACC}"/></g>',
              f'<path d="M940,380 Q1005,340 1070,380 M1070,480 Q1005,520 940,480" stroke="{ACC}" stroke-width="4" fill="none"/>', ico("clock", 1500, 260, 110, INK, .6)]
    elif n == 27:
        b += [ico("magnifier", 640, 500, 200, INK, .4), line(860, 300, 860, 700, INK, 3, .3, "6 10"),
              f'<g data-flow="1"><path d="M1060,500 a160,120 0 1 1 320,0 a160,120 0 1 1 -320,0" stroke="{ACC}" stroke-width="5" fill="none" stroke-dasharray="12 12"/></g>',
              ico("hand", 1220, 500, 90, INK, .8)]
    elif n == 28:
        fig, an = F(x=760, pose="reach", expr="uneasy", look=6)
        b += [fig, acc("document", an["rhand"][0] + 120, an["rhand"][1] - 20, 160), ico("check", an["rhand"][0] + 220, an["rhand"][1] - 140, 60, INK, .7)]
    elif n == 29:
        b += [f'<g data-acc="960,460">' + glow(960, 460, 340, "A", .55)
              + f'<path d="M640,360 h640 a24,24 0 0 1 24,24 v130 a24,24 0 0 1 -24,24 h-460 l-60,60 v-60 h-120 a24,24 0 0 1 -24,-24 v-130 a24,24 0 0 1 24,-24 z" fill="none" stroke="{ACC}" stroke-width="6"/>'
              + f'<text x="960" y="490" font-family="Anton" font-size="70" fill="{ACC}" text-anchor="middle">…</text></g>',
              f'<g data-flow="1"><ellipse cx="960" cy="460" rx="420" ry="230" fill="none" stroke="{INK}" stroke-width="3" opacity=".25" stroke-dasharray="10 16"/></g>']
    # ---------------------------------------------------------------- SEÑAL 4 — Recibir comentarios
    elif n == 30:
        fig, an = figure(1300, FLOOR, 1.1, "explain", "neutral", look=-6, op=.3, ghost=True)
        b += [floor_line(), marker(4, 1640, 300, 150), fig, F(x=680, pose="step_back", expr="defensive", look=6)[0]]
    elif n == 31:
        b += [praise_ring(960, 500, 360), F(x=960, pose="stand", expr="attentive")[0]]
    elif n == 32:
        b += [praise_ring(960, 500, 380, crit_scale=2.0, praise_op=.2), F(x=760, pose="stand", expr="worried", look=6)[0]]
    elif n == 33:
        b += [acc("xmark", 1300, 480, 260), F(x=700, pose="stand", expr="sad", look=6)[0]]
    elif n == 34:
        b += [ico("xmark", 1500, 700, 110, INK, .25), ico("thought", 1180, 330, 160, INK, .4), F(x=680, pose="think", expr="thoughtful", look=6)[0]]
    elif n == 35:
        b += [f'<g data-acc="960,480">' + glow(960, 480, 260, "A", .6) + f'<line x1="760" y1="480" x2="1160" y2="480" stroke="{ACC}" stroke-width="12" stroke-linecap="round"/>'
              + f'<line x1="960" y1="480" x2="960" y2="820" stroke="{ACC}" stroke-width="8"/><rect x="900" y="820" width="120" height="20" rx="6" fill="{ACC}"/></g>',
              ico("shield", 960, 360, 90, INK, .5)]
    elif n == 36:
        b += [acc("xmark", 640, 500, 180), f'<line x1="760" y1="500" x2="1120" y2="500" stroke="{ACC}" stroke-width="5" stroke-dasharray="10 10"/>',
              f'<line x1="1160" y1="460" x2="1520" y2="460" stroke="{INK}" stroke-width="10" stroke-linecap="round" opacity=".8"/>',
              f'<line x1="1340" y1="460" x2="1340" y2="760" stroke="{INK}" stroke-width="6" opacity=".8"/>', ico("check", 1340, 330, 80, INK, .6)]
    # ---------------------------------------------------------------- SEÑAL 5 — El ideal que no existe
    elif n == 37:
        b += [floor_line(), marker(5, 1640, 300, 150), F(x=700, pose="stand", expr="attentive", look=6)[0],
              glow(1180, 600, 260, "A", .6), figure(1180, FLOOR, 1.12, "stride", "proud", look=6, color=ACC, op=.75)[0]]
    elif n == 38:
        b += [floor_line(), figure(380, FLOOR, 1.0, "stand", "neutral", op=.25, ghost=True)[0], F(x=900, pose="stand", expr="attentive", look=6)[0],
              glow(1420, 600, 220, "A", .5), figure(1420, FLOOR, 1.0, "stride", "proud", look=6, color=ACC, op=.6)[0]]
    elif n == 39:
        b += [figure(1100, FLOOR + 160, 1.6, "stand", "neutral", op=.12, ghost=True)[0], F(x=700, pose="stand", expr="neutral", look=6)[0]]
    elif n == 40:
        b += [floor_line(), F(x=640, pose="stand", expr="strain", look=6)[0], glow(1460, 600, 240, "A", .55),
              figure(1460, FLOOR, 1.12, "stride", "proud", look=6, color=ACC, op=.7)[0],
              line(780, 360, 1340, 360, INK, 3, .5), line(780, 340, 780, 380, INK, 3, .5), line(1340, 340, 1340, 380, INK, 3, .5)]
    elif n == 41:
        b += [F(x=760, pose="reach", expr="worried", look=6)[0], glow(1400, 520, 220, "A", .5),
              figure(1400, FLOOR + 200, 1.8, "stride", "proud", look=6, color=ACC, op=.55)[0], ico("arrow", 1700, 520, 90, INK, .4)]
    # ---------------------------------------------------------------- CIERRE
    elif n == 42:
        b += [floor_line(), dots5(1260, 720, 380, lit=5), F(x=600, pose="stand", expr="calm", look=6)[0]]
    elif n == 43:
        b += [ruler(300, 520, 1500, ended=False)]
    elif n == 44:
        b += [acc("star", 1340, 440, 150), F(x=700, pose="reassure", expr="warm", look=6)[0]]
    elif n == 45:
        b += [ruler(300, 380, 1300, ended=True), figure(1000, FLOOR, 1.0, "stand", "serene", look=5)[0], floor_line()]
    elif n == 46:
        b += [acc("bubble", 1320, 380, 180), F(x=700, pose="point_you", expr="warm", look=3)[0]]
    elif n == 47:
        b += [acc("bell", 1340, 420, 150), F(x=760, pose="thumbs", expr="smile")[0]]
    elif n == 48:
        b += [rim(960, 500, 620), F(x=960, pose="stand", expr="serene")[0]]
    else:
        raise ValueError(n)
    return b


def thumb_b():
    """Mẫu B — triptych: terminar y pasar al siguiente · página en blanco · re-editar un detalle (vật nhấn)."""
    pw = TW / 3
    b = [panel_bg(0, 0, pw, TH, "#FFB46B", .24), panel_bg(pw, 0, pw, TH, "#7FB8FF", .26), panel_bg(2 * pw, 0, pw, TH, "#8B6CFF", .26)]
    b += [ico("trophy", 90, 380, 100, INK, .5), figure(240, 560, .95, "walk", "uneasy", look=6)[0], ico("task", 360, 250, 80, INK)]
    fig, an = figure(pw + 120, 560, .95, "reach", "worried", look=6)
    b += [fig, page(an["rhand"][0] + 80, an["rhand"][1] - 40, 110)]
    fig, an = figure(2 * pw + 120, 560, .95, "reach", "strain", look=6)
    b += [fig, ico("document", an["rhand"][0] + 60, an["rhand"][1] - 50, 120, INK), acc("magnifier", an["rhand"][0] + 80, an["rhand"][1] - 80, 90)]
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 3}" y="0" width="6" height="{TH}" fill="#000"/>')
    b.append(badge())
    return b


def thumb_c():
    """Mẫu C — lưới 6 khung."""
    pw, ph = TW / 3, TH / 2
    tints = ("#FFB46B", "#7FB8FF", "#8B6CFF", "#FF6B6B", "#5AC8A0", "#FFD9A0")
    b = [panel_bg((i % 3) * pw, (i // 3) * ph, pw, ph, t, .22) for i, t in enumerate(tints)]
    b += [ico("trophy", 100, 250, 90, INK, .6), figure(250, 320, .58, "walk", "uneasy", look=6)[0]]                   # 1
    fig, an = figure(540, 320, .58, "reach", "worried", look=6)
    b += [fig, page(an["rhand"][0] + 80, an["rhand"][1] - 20, 90)]                                                     # 2
    b += [ico("document", 1060, 170, 150, INK), acc("magnifier", 1110, 140, 110), ico("hand", 960, 260, 70, INK, .7)]  # 3
    b += [figure(110, 460, .34, "stand", "worried", look=6)[0]] + [ico("star", 200 + i * 50, 390, 34, INK, .45) for i in range(4)] + [acc("xmark", 300, 440, 40, glow_r=40)]  # 4
    b += [figure(560, 460, .34, "stand", "neutral", look=6)[0], figure(700, 460, .34, "stride", "proud", look=6, color=ACC, op=.8)[0]]  # 5
    b += [chair(1040, 520, .45), figure(1046, 520, .45, "sit", "serene")[0], ico("check", 1170, 420, 70, INK)]          # 6
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 1.5}" y="0" width="3" height="{TH}" fill="{BG}"/>')
    b.append(f'<rect x="0" y="{ph - 1.5}" width="{TW}" height="3" fill="{BG}"/>')
    b.append(badge())
    return b

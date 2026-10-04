# -*- coding: utf-8 -*-
"""
scenes.py — Kịch bản hình của project 31 "7 Hábitos Ocultos de la Gente Mentalmente Fuerte"
(38 khung + 2 thumbnail), bám theo [VISUAL DESCRIPTION] trong transcript_and_visuals.txt.
Màu nhấn #8B6CFF (05_Autoconocimiento).
Mô-típ: 7 ô số vòng cung (ô 7 sáng nhất) · bong bóng suy nghĩ nứt → tách "hecho / miedo" · thấu kính đổi nghĩa đám mây ·
la bàn giá trị vs đám đông · chuông báo động to dần · dòng năng lượng chuyển vào trong · kính lúp soi lỗi rồi buông.
"""
from scenekit import *  # noqa: F401,F403
from sticklib import *  # noqa: F401,F403  (nạp lại ACC sau khi đã set_accent theo playlist)
from scenekit import FLOOR
from thumbkit import TH, TW, badge, panel_bg


def ntile(x, y, d, state="dim", w=110):
    """Ô số d. state: dim · lit · hi (sáng nhất)."""
    h = w * 1.15
    col = INK if state == "dim" else ACC
    o = .3 if state == "dim" else 1
    body = (f'<g opacity="{o}"><rect x="{x - w / 2:.0f}" y="{y - h / 2:.0f}" width="{w:.0f}" height="{h:.0f}" rx="16" fill="{BG}" stroke="{col}" stroke-width="5"/>'
            f'<text x="{x:.0f}" y="{y + w * .26:.0f}" font-family="Anton" font-size="{w * .66:.0f}" fill="{col}" text-anchor="middle">{d}</text></g>')
    if state == "dim":
        return body
    return f'<g data-acc="{x:.0f},{y:.0f}">' + glow(x, y, w * (1.6 if state == "hi" else 1.05), "A", .9 if state == "hi" else .6) + body + "</g>"


def tiles_arc(cx, cy, r, a0, a1, states, w=90, seq=True):
    out = []
    n = len(states)
    for i, st in enumerate(states):
        a = math.radians(a0 + (a1 - a0) * i / (n - 1))
        t = ntile(cx + r * math.cos(a), cy + r * math.sin(a), i + 1, st, w * (1.25 if st == "hi" else 1))
        out.append(f'<g data-dot="{i}">{t}</g>' if seq else t)
    return "".join(out)


def title_card(d, right):
    return [ntile(760, 500, d, "hi", 220)] + right


def emo(x, y, size=90, lit=True):
    """Biểu tượng cảm xúc: trái tim + sóng."""
    g = ico("heart", x, y - size * .15, size, ACC if lit else INK) + ico("wave", x, y + size * .55, size * .7, ACC if lit else INK, .7)
    return (f'<g data-acc="{x},{y}">' + glow(x, y, size * 1.1, "A", .6) + g + "</g>") if lit else g


def build_layers(n, shot):
    F = lambda **kw: shot_fig(shot, **kw)  # noqa: E731
    b = []
    D7 = ["dim"] * 7
    # ---------------------------------------------------------------- GANCHO
    if n == 1:
        b += [floor_line(), F(x=960, pose="stand", expr="calm")[0]]
    elif n == 2:
        b += [F(x=960, pose="stand", expr="calm")[0]]
        b += [ntile(960 + 520 * math.cos(math.radians(a)), 470 + 340 * math.sin(math.radians(a)), i + 1, "dim", 70)
              for i, a in enumerate(range(200, 520, 46))]
    elif n == 3:
        b += [floor_line(), tiles_arc(1220, 760, 460, 205, 335, ["lit"] * 7, 80), F(x=560, pose="stand", expr="calm", look=6)[0]]
    elif n == 4:
        b += [tiles_arc(1300, 780, 440, 205, 335, ["dim"] * 6 + ["hi"], 76), F(x=560, pose="point_you", expr="warm", look=3)[0]]
    # ---------------------------------------------------------------- HÁBITO 1 — Morin
    elif n == 5:
        b += title_card(1, [ico("thought", 1220, 480, 200, INK, .8), crack(1160, 430, 1280, 520, seed=5, color=INK, w=4)])
    elif n == 6:
        b += [acc("clipboard", 1320, 470, 200, rows=3), F(x=680, pose="explain", expr="thoughtful", look=6)[0]]
    elif n == 7:
        fig, an = F(x=700, pose="stand", expr="attentive", look=6)
        b += [fig, ico("thought", 1300, 400, 300, INK, .8), ico("warning", 1300, 390, 110, INK)]
    elif n == 8:
        b += [ico("thought", 960, 280, 180, INK, .35), line(900, 360, 760, 460, INK, 3, .3, "6 8"), line(1020, 360, 1160, 460, INK, 3, .3, "6 8"),
              f'<g data-acc="700,560">' + glow(700, 560, 180, "A", .7) + ico("thought", 700, 560, 220, ACC) + ico("check", 700, 550, 80, ACC) + "</g>",
              ico("thought", 1220, 560, 220, INK, .6), ico("wave", 1220, 550, 90, INK, .6)]
    elif n == 9:
        b += [floor_line(), acc("clock", 1340, 420, 150), F(x=520, pose="hunch", expr="uneasy", op=.3, look=6)[0], F(x=760, pose="stand", expr="calm", look=6)[0]]
    # ---------------------------------------------------------------- HÁBITO 2 — Gross
    elif n == 10:
        b += title_card(2, [emo(1220, 480, 130)])
    elif n == 11:
        b += [ico("bank", 1180, 400, 200, INK, .5), acc("brain", 1500, 460, 140), ico("arrow", 1500, 600, 80, ACC),
              F(x=620, pose="explain", expr="thoughtful", look=6)[0]]
    elif n == 12:
        b += [ico("raincloud", 760, 480, 260, INK, .55), ico("cloud", 1240, 480, 260, INK, .9),
              f'<g data-acc="1000,480">' + glow(1000, 480, 200, "A", .7)
              + f'<ellipse cx="1000" cy="480" rx="70" ry="170" fill="{ACC}" fill-opacity=".12" stroke="{ACC}" stroke-width="7"/></g>']
    elif n == 13:
        fig, an = F(x=960, pose="open_arms", expr="calm")
        sx, sy = an["sh"]
        b += [fig, emo(sx, sy - 40 if shot == "CLOSE-UP" else sy + 40, 90)]
    elif n == 14:
        b += [floor_line(), emo(1240, 440, 110), f'<g data-dot="1">' + ico("footprint", 1520, 820, 80, INK, .9, rot=90) + "</g>",
              F(x=760, pose="stand", expr="calm", look=6)[0]]
    # ---------------------------------------------------------------- HÁBITO 3 — Valores
    elif n == 15:
        b += title_card(3, [acc("compass", 1220, 480, 170)])
    elif n == 16:
        fig, an = F(x=760, pose="stand", expr="determined", look=6)
        hx, hy = an["head"]
        b += [fig, f'<path d="M{hx + 80},{hy} Q{hx + 360},{hy - 160} {hx + 640},{hy - 200}" stroke="{ACC}" stroke-width="5" fill="none" stroke-dasharray="8 12"/>',
              acc("compass", hx + 700, hy - 210, 120),
              f'<path d="M{hx + 80},{hy + 30} Q{hx + 360},{hy + 160} {hx + 640},{hy + 220}" stroke="{INK}" stroke-width="4" fill="none" opacity=".3" stroke-dasharray="8 12"/>',
              crowd([hx + 640, hx + 720, hx + 800], hy + 420, .45, .25)]
    elif n == 17:
        b += [floor_line(), acc("compass", 960, 300, 100), F(x=760, pose="hands_hips", expr="determined", look=6)[0],
              figure(1460, FLOOR, 1.0, "cross", "squint", look=-6, op=.3, ghost=True)[0]]
    elif n == 18:
        b += [F(x=720, pose="stop", expr="calm", look=6)[0], acc("hand", 1240, 400, 110), ico("star", 1500, 560, 90, INK, .25)]
    # ---------------------------------------------------------------- HÁBITO 4 — Incomodidad
    elif n == 19:
        b += title_card(4, [ico("bell", 1220, 480, 150, INK, .4)])
    elif n == 20:
        b += [floor_line(), acc("boulder", 1400, 780, 200), F(x=900, pose="walk", expr="uneasy", look=-6)[0],
              f'<path d="M640,520 q-60,-40 -120,0 M640,600 q-60,-40 -120,0" stroke="{INK}" stroke-width="4" fill="none" opacity=".35"/>']
    elif n == 21:
        b += [ico("brain", 520, 500, 220, INK, .8)] + [f'<g data-dot="{i}">' + ico("bell", 860 + i * 300, 500, 90 + i * 60, ACC if i == 2 else INK, .5 + i * .25) + "</g>" for i in range(3)]
        b += [glow(1460, 500, 200, "A", .5)]
    elif n == 22:
        b += [floor_line(), ico("boulder", 1060, 790, 180, INK, .6), ico("bell", 1060, 560, 70, INK, .35), F(x=700, pose="stand", expr="calm", look=6)[0],
              acc("heart", 1420, 380, 90), ico("warning", 1620, 380, 90, INK, .5)]
    # ---------------------------------------------------------------- HÁBITO 5 — Soltar el control
    elif n == 23:
        b += title_card(5, [ico("hand", 1140, 560, 110, INK, .8, rot=180), ico("hand", 1340, 560, 110, INK, .8, rot=180), acc("boulder", 1240, 380, 100)])
    elif n == 24:
        b += [F(x=700, pose="stand", expr="serene", look=6)[0]]
        b += [f'<g data-dot="{i}">' + ico(nm, 1240 + i * 200, 500, 130, INK, .5 - i * .1) + "</g>" for i, nm in enumerate(("raincloud", "car", "person"))]
    elif n == 25:
        fig, an = F(x=960, pose="stand", expr="calm")
        sx, sy = an["sh"]
        b += [ico("raincloud", 360, 300, 110, INK, .25), ico("car", 360, 700, 110, INK, .25), ico("person", 1600, 500, 110, INK, .25), fig,
              f'<g data-flow="1"><path d="M460,320 Q700,420 {sx - 20},{sy + 40} M460,680 Q700,600 {sx - 20},{sy + 60}" stroke="{ACC}" stroke-width="5" fill="none" stroke-dasharray="6 18"/></g>',
              f'<g data-acc="{sx},{sy + 50}">' + glow(sx, sy + 50, 120, "A", .9) + f'<circle cx="{sx}" cy="{sy + 50}" r="14" fill="{ACC}"/></g>']
    elif n == 26:
        fig, an = F(x=760, pose="stride", expr="determined", look=6)
        b += [floor_line(), fig, acc("footprint", 1180, 860, 90, rot=90)]
    # ---------------------------------------------------------------- HÁBITO 6 — Progreso ajeno
    elif n == 27:
        b += title_card(6, [figure(1140, 700, .55, "stand", "smile", color=ACC)[0], figure(1320, 660, .55, "open_arms", "proud", color=ACC)[0]])
    elif n == 28:
        fig2, an2 = figure(1380, FLOOR, 1.0, "open_arms", "proud")
        b += [floor_line(), fig2, acc("star", an2["top"][0], an2["top"][1] - 90, 100), F(x=700, pose="thumbs", expr="smile", look=6)[0]]
    elif n == 29:
        b += [floor_line(), F(x=440, pose="stand", expr="calm", look=6)[0],
              f'<g data-acc="900,560">' + glow(900, 560, 200, "A", .6) + f'<path d="M620,860 Q800,780 900,620 T1180,380" stroke="{ACC}" stroke-width="7" fill="none"/>'
              + f'<circle cx="620" cy="860" r="12" fill="{ACC}"/></g>',
              f'<path d="M1320,700 Q1480,640 1560,520 T1780,330" stroke="{INK}" stroke-width="5" fill="none" opacity=".35"/>', f'<circle cx="1320" cy="700" r="10" fill="{INK}" opacity=".4"/>']
    elif n == 30:
        b += [ico("scale", 960, 260, 120, INK, .2),
              f'<g data-acc="760,560">' + glow(760, 560, 180, "A", .5) + f'<path d="M560,820 Q680,740 760,600 T960,380" stroke="{ACC}" stroke-width="7" fill="none"/></g>',
              f'<path d="M1060,820 Q1180,740 1260,600 T1460,380" stroke="{INK}" stroke-width="5" fill="none" opacity=".5"/>']
    # ---------------------------------------------------------------- HÁBITO 7 — Error
    elif n == 31:
        b += title_card(7, [ico("xmark", 1220, 520, 110, INK, .6), acc("magnifier", 1250, 490, 190)])
    elif n == 32:
        fig, an = F(x=960, pose="hunch", expr="resigned")
        b += [fig, f'<g data-flow="1"><ellipse cx="960" cy="520" rx="380" ry="300" fill="none" stroke="{INK}" stroke-width="4" opacity=".35" stroke-dasharray="14 12"/></g>']
        b += [ico("xmark", 960 + 380 * math.cos(math.radians(a)), 520 + 300 * math.sin(math.radians(a)), 60, INK, .45) for a in (-90, 30, 150)]
    elif n == 33:
        b += [floor_line(), f'<path d="M1100,905 Q1260,780 1420,905 Z" fill="{INK}" opacity=".12" stroke="{INK}" stroke-width="3"/>',
              ico("xmark", 1260, 860, 50, INK, .3), ico("xmark", 1000, 620, 80, INK, .8), F(x=700, pose="stand", expr="worried", look=6)[0]]
    elif n == 34:
        b += [ico("xmark", 560, 500, 110, INK, .8), acc("magnifier", 600, 460, 200), line(760, 500, 1000, 500, INK, 4, .4, "8 10"),
              F(x=1200, pose="open_arms", expr="serene")[0] if shot == "CLOSE-UP" else figure(1200, FLOOR, 1.1, "open_arms", "serene")[0],
              particles(1500, 360, 160, 120, 16, seed=34, op=.7)]
    # ---------------------------------------------------------------- CIERRE
    elif n == 35:
        b += [tiles_arc(1300, 780, 440, 205, 335, ["lit"] * 7, 76), F(x=560, pose="point_you", expr="warm", look=3)[0]]
    elif n == 36:
        b += [acc("bubble", 1240, 360, 160), f'<text x="1240" y="700" font-family="Anton" font-size="140" fill="{INK}" opacity=".6" text-anchor="middle">4/7</text>',
              F(x=600, pose="explain", expr="warm", look=6)[0]]
    elif n == 37:
        b += [floor_line(), tiles_arc(960, 820, 560, 200, 340, ["lit"] * 7, 90), F(x=960, pose="stand", expr="calm")[0]]
    elif n == 38:
        b += [floor_line(), tiles_arc(960, 820, 560, 200, 340, ["dim"] * 7, 80, seq=False), F(x=960, pose="stand", expr="serene")[0],
              acc("bell", 1620, 200, 90), acc("hand", 1780, 200, 80)]
    else:
        raise ValueError(n)
    return b


def thumb_b():
    """Mẫu B — triptych: reformular el pensamiento · sentir la emoción · soltar el peso (vật nhấn)."""
    pw = TW / 3
    b = [panel_bg(0, 0, pw, TH, "#7FB8FF", .26), panel_bg(pw, 0, pw, TH, "#FFB46B", .24), panel_bg(2 * pw, 0, pw, TH, "#8B6CFF", .26)]
    fig, an = figure(pw / 2, 560, .95, "think", "calm")
    b += [fig, ico("thought", pw / 2 + 110, 120, 140, INK), crack(pw / 2 + 80, 100, pw / 2 + 140, 140, seed=3, color=INK, w=3)]
    b += [chair(pw + pw / 2 - 10, 560, .95), figure(pw + pw / 2, 560, .95, "sit", "serene", look=0)[0], emo(pw + pw / 2 + 130, 260, 80, lit=False)]
    fig, an = figure(2 * pw + pw / 2, 560, .95, "open_arms", "serene")
    b += [fig, acc("boulder", 2 * pw + pw / 2 + 120, 150, 70)]
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 3}" y="0" width="6" height="{TH}" fill="#000"/>')
    b.append(badge())
    return b


def thumb_c():
    """Mẫu C — lưới 6 khung."""
    pw, ph = TW / 3, TH / 2
    tints = ("#7FB8FF", "#FFB46B", "#FF6B6B", "#5AC8A0", "#8C7BFF", "#FFD9A0")
    b = [panel_bg((i % 3) * pw, (i // 3) * ph, pw, ph, t, .22) for i, t in enumerate(tints)]
    b += [figure(130, 320, .58, "think", "calm")[0], ico("thought", 290, 140, 110, INK), ico("check", 290, 134, 40, INK)]           # 1
    b += [chair(560, 320, .58), figure(566, 320, .58, "sit", "serene")[0], emo(720, 170, 70, lit=False)]                             # 2
    b += [figure(1000, 320, .58, "hands_hips", "determined")[0]] + [line(1150, 140 + k * 50, 1220, 140 + k * 50, INK, 4, .5) for k in range(3)]  # 3
    b += [f'<circle cx="200" cy="420" r="80" fill="none" stroke="{ACC}" stroke-width="4" opacity=".7"/>', figure(200, 470, .3, "stand", "calm")[0]]  # 4
    b += [ico("hand", 580, 440, 70, INK, .8, rot=180), ico("hand", 700, 440, 70, INK, .8, rot=180), ico("boulder", 640, 380, 50, INK, .6)]  # 5
    b += [figure(1040, 520, .45, "hands_hips", "satisfied")[0]] + [ntile(1150 + (k % 2) * 50, 380 + (k // 2) * 50, k + 1, "lit", 38) for k in range(6)]  # 6
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 1.5}" y="0" width="3" height="{TH}" fill="{BG}"/>')
    b.append(f'<rect x="0" y="{ph - 1.5}" width="{TW}" height="3" fill="{BG}"/>')
    b.append(badge())
    return b

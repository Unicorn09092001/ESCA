# -*- coding: utf-8 -*-
"""
scenes.py — Kịch bản hình của project 29 "6 Señales de Mentalidad de Crecimiento (Y No Lo Sabías)"
(36 khung + 2 thumbnail), bám theo [VISUAL DESCRIPTION] trong transcript_and_visuals.txt.
Màu nhấn #8B6CFF (05_Autoconocimiento).
Mô-típ: 6 ô số xếp vòng cung (mờ → sáng dần) · mầm cây + não (tư duy phát triển) · dấu lỗi được soi bằng kính lúp ·
bong bóng "todavía" mở ra mũi tên · hai ngả đường (cửa đóng vs lối chấm sáng).
"""
from scenekit import *  # noqa: F401,F403
from sticklib import *  # noqa: F401,F403  (nạp lại ACC sau khi đã set_accent theo playlist)
from scenekit import FLOOR, desk
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


def tiles_arc(cx, cy, r, a0, a1, states, w=100, seq=True):
    out = []
    for i, st in enumerate(states):
        a = math.radians(a0 + (a1 - a0) * i / 5)
        t = ntile(cx + r * math.cos(a), cy + r * math.sin(a), i + 1, st, w)
        out.append(f'<g data-dot="{i}">{t}</g>' if seq else t)
    return "".join(out)


def title_card(d, right):
    return [ntile(760, 500, d, "hi", 220)] + right


def err_mark(x, y, size=110, lit=False, op=1.0):
    return acc("xmark", x, y, size) if lit else ico("xmark", x, y, size, INK, op)


def sprout_brain(x, y, size=200, op=1.0):
    return (f'<g data-acc="{x},{y}">' + glow(x, y, size * .9, "A", .55 * op) + ico("brain", x, y + size * .12, size * .8, ACC, op)
            + ico("sprout", x, y - size * .55, size * .5, ACC, op) + "</g>")


def eeg(x0, x1, y, amp=40, color=None, w=5, op=1.0):
    color = color or INK
    pts, n = [], 18
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n
        yy = y + (amp * (1 if i % 2 else -1) * (1.6 if i in (8, 9, 10) else .5) if 0 < i < n else 0)
        pts.append(f"{x:.0f},{yy:.0f}")
    return f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="{w}" opacity="{op}" stroke-linejoin="round"/>'


def word_bubble(x, y, w=420, open_end=False, lit=False, op=1.0):
    col = ACC if lit else INK
    out = (f'<g opacity="{op}"><path d="M{x - w / 2},{y - 70} h{w} a20,20 0 0 1 20,20 v100 a20,20 0 0 1 -20,20 h{-w + 80} l-40,40 v-40 h-20 '
           f'a20,20 0 0 1 -20,-20 v-100 a20,20 0 0 1 20,-20 z" fill="none" stroke="{INK}" stroke-width="5"/>'
           + "".join(f'<rect x="{x - w / 2 + w * .07 + k * w * .17:.0f}" y="{y - 16}" width="{w * .13:.0f}" height="20" rx="10" fill="{INK}" opacity=".5"/>' for k in range(4))
           + "</g>")
    ex = x + w / 2 - 50
    if open_end:
        out += (f'<g data-acc="{ex},{y - 6}">' + glow(ex, y - 6, 80, "A", .8)
                + f'<path d="M{ex - 28},{y - 6} L{ex + 22},{y - 6} M{ex + 4},{y - 24} L{ex + 22},{y - 6} L{ex + 4},{y + 12}" fill="none" stroke="{ACC}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></g>')
    else:
        out += f'<rect x="{ex - 18}" y="{y - 24}" width="36" height="36" rx="4" fill="{INK}" opacity=".7"/>'
    return out


def build_layers(n, shot):
    F = lambda **kw: shot_fig(shot, **kw)  # noqa: E731
    b = []
    D6 = ["dim"] * 6
    # ---------------------------------------------------------------- GANCHO
    if n == 1:
        b += [floor_line(), ico("mirror", 1300, 560, 300, INK, .8), ico("bubble", 960, 300, 140, INK, .35), line(900, 350, 1020, 250, INK, 5, .5),
              F(x=720, pose="stand", expr="neutral", look=6)[0]]
    elif n == 2:
        fig, an = F(x=760, pose="stand", expr="calm", look=6)
        b += [fig, sprout_brain(an["sh"][0] + 340, an["sh"][1] + 40, 150, .7)]
    elif n == 3:
        b += [tiles_arc(960, 760, 520, 200, 340, D6, 110), acc("document", 960, 640, 120, op=.6)]
    elif n == 4:
        b += [tiles_arc(1320, 760, 420, 210, 330, ["lit"] * 6, 90), F(x=560, pose="point_you", expr="warm", look=3)[0]]
    # ---------------------------------------------------------------- SEÑAL 1 — Moser
    elif n == 5:
        b += title_card(1, [ico("xmark", 1180, 500, 130, INK, .9), ico("magnifier", 1220, 460, 170, INK, .6)])
    elif n == 6:
        b += [ico("building", 1240, 420, 200, INK, .5), acc("brain", 1520, 470, 140), eeg(1420, 1620, 620, 26, ACC, 4),
              F(x=640, pose="explain", expr="thoughtful", look=6)[0]]
    elif n == 7:
        b += [err_mark(960, 260, 110), ico("brain", 620, 560, 260, INK, .6), eeg(500, 740, 780, 14, INK, 4, .5),
              acc("brain", 1300, 560, 260), eeg(1180, 1420, 780, 44, ACC, 5),
              line(900, 300, 700, 430, INK, 3, .3, "6 8"), line(1020, 300, 1220, 430, INK, 3, .3, "6 8")]
    elif n == 8:
        b += [acc("brain", 700, 500, 300), ico("xmark", 1240, 500, 120, INK), ico("magnifier", 1270, 470, 230, INK, .9),
              line(880, 500, 1110, 500, ACC, 4, .6, "6 10")]
    elif n == 9:
        b += [floor_line(), ico("xmark", 1300, 560, 120, INK, .7), F(x=760, pose="stand", expr="calm", look=6)[0]]
    elif n == 10:
        b += [ico("xmark", 640, 500, 140, INK, .4), line(780, 500, 1040, 500, INK, 4, .4, "8 10"), acc("notes", 1240, 500, 200)]
    # ---------------------------------------------------------------- SEÑAL 2 — Mueller & Dweck
    elif n == 11:
        b += title_card(2, [ico("notes", 1140, 500, 130, INK, .9), ico("bubble", 1380, 500, 120, INK, .35), line(1320, 560, 1440, 440, INK, 5, .5)])
    elif n == 12:
        b += [ico("bank", 1240, 400, 200, INK, .5)]
        b += [figure(1160 + i * 120, FLOOR, .55, "stand", "smile", look=0)[0] for i in range(3)]
        b += [F(x=620, pose="explain", expr="thoughtful", look=6)[0]]
    elif n == 13:
        fig, an = figure(820, FLOOR, .75, "step_back", "uneasy", look=-6)
        b += [floor_line(), fig, acc("bubble", an["top"][0], an["top"][1] - 120, 130), ico("star", an["top"][0], an["top"][1] - 125, 40, ACC),
              ico("boulder", 1360, 780, 220, INK, .55)]
    elif n == 14:
        fig, an = figure(900, FLOOR, .75, "walk", "determined", look=6)
        b += [floor_line(), fig, ico("bubble", an["top"][0] - 40, an["top"][1] - 120, 130, INK, .7), ico("muscle", an["top"][0] - 40, an["top"][1] - 128, 50, INK, .7),
              acc("boulder", 1360, 780, 220)]
    elif n == 15:
        fig, an = F(x=960, pose="point", expr="determined", look=6)
        b += [fig, acc("notes", 1480, 460, 170), ico("trophy", 480, 460, 150, INK, .3)]
    elif n == 16:
        b += [acc("brain", 860, 500, 300), ico("mask", 1400, 560, 160, INK, .25)]
    # ---------------------------------------------------------------- SEÑAL 3 — Lo difícil
    elif n == 17:
        b += title_card(3, [acc("target", 1180, 440, 130), ico("check", 1340, 600, 90, INK, .35)])
    elif n == 18:
        fig, an = figure(820, FLOOR, 1.2, "type", "calm", look=6)
        b += [desk(1040, 760, 420), chair(810, FLOOR, 1.2), fig, ico("laptop", 1080, 700, 120, INK, .9)]
    elif n == 19:
        fig, an = F(x=760, pose="stand", expr="attentive", look=6)
        b += [fig, ico("laptop", 400, 760, 100, INK, .3), acc("target", 1420, 460, 190), acc("spark", an["head"][0] + 160, an["head"][1] - 80, 70, glow_r=60)]
    elif n == 20:
        b += [floor_line(), crowd([260, 380, 500], FLOOR, .6, .15), acc("target", 1560, 520, 170), F(x=1100, pose="walk", expr="determined", look=6)[0]]
    # ---------------------------------------------------------------- SEÑAL 4 — Todavía
    elif n == 21:
        b += title_card(4, [word_bubble(1260, 500, 340, open_end=True)])
    elif n == 22:
        b += [word_bubble(960, 340, 520, open_end=False, op=.8), word_bubble(960, 700, 520, open_end=True)]
    elif n == 23:
        b += [word_bubble(960, 500, 760, open_end=True, op=.5)]
    elif n == 24:
        b += [f'<path d="M500,880 L960,640" stroke="{INK}" stroke-width="5" opacity=".6"/>',
              f'<path d="M960,640 L620,380" stroke="{INK}" stroke-width="5" opacity=".4"/>', ico("door", 560, 330, 160, INK, .5), line(500, 330, 620, 330, INK, 6, .6),
              f'<g data-acc="1400,380"><g data-flow="1"><path d="M960,640 Q1200,520 1640,260" stroke="{ACC}" stroke-width="7" fill="none" stroke-dasharray="4 18" stroke-linecap="round"/></g></g>',
              glow(1640, 260, 160, "A", .6), figure(940, 900, .7, "stand", "thoughtful", look=5)[0]]
    # ---------------------------------------------------------------- SEÑAL 5 — Éxito ajeno
    elif n == 25:
        b += title_card(5, [acc("star", 1140, 500, 120), ico("notes", 1340, 500, 120, INK, .8)])
    elif n == 26:
        fig, an = figure(1260, FLOOR, 1.0, "open_arms", "proud")
        b += [floor_line(), fig, acc("star", an["top"][0], an["top"][1] - 100, 110)]
        b += [f'<g data-dot="{i}">' + ico(nm, 1560 + i * 110, 280, 70, INK, .5) + "</g>" for i, nm in enumerate(("briefcase", "check", "dumbbell"))]
        b += [figure(600, FLOOR, 1.0, "stand", "attentive", look=6)[0]]
    elif n == 27:
        fig, an = F(x=860, pose="stand", expr="smile", look=6)
        hx, hy = an["head"]
        b += [fig, ico("mask", hx + 300, hy - 40, 150, INK, .45), acc("question", hx + 300, hy + 140, 90)]
    elif n == 28:
        fig, an = F(x=960, pose="think", expr="attentive")
        tx, ty = an["top"]
        b += [fig, acc("thought", tx - 260, ty - 40, 180), ico("question", tx - 260, ty - 50, 60, ACC),
              ico("thought", tx + 260, ty - 40, 160, INK, .3), ico("clover", tx + 260, ty - 50, 60, INK, .3), line(tx + 200, ty, tx + 320, ty - 90, INK, 5, .45)]
    # ---------------------------------------------------------------- SEÑAL 6 — Ya no ser el mejor
    elif n == 29:
        b += title_card(6, [ico("trophy", 1140, 460, 120, INK, .25), acc("guitar", 1340, 520, 140)])
    elif n == 30:
        fig, an = F(x=700, pose="stand", expr="calm", look=6)
        b += [fig, f'<circle cx="1320" cy="460" r="130" fill="none" stroke="{INK}" stroke-width="3" opacity=".18" stroke-dasharray="10 12"/>']
    elif n == 31:
        fig, an = figure(860, FLOOR, 1.12, "sit", "serene", look=6)
        b += [floor_line(), chair(850, FLOOR, 1.12), fig, ico("guitar", an["rhand"][0] + 30, an["rhand"][1] - 10, 120, INK),
              acc("arrow_up", 1420, 440, 120)]
    elif n == 32:
        fig, an = figure(960, FLOOR, .8, "sit", "serene", look=6)
        b += [floor_line(), rim(960, 620, 520, .7), chair(950, FLOOR, .8), fig, ico("guitar", an["rhand"][0] + 20, an["rhand"][1] - 8, 86, INK)]
    # ---------------------------------------------------------------- CIERRE
    elif n == 33:
        b += [tiles_arc(1300, 780, 440, 210, 330, ["lit"] * 6, 90), F(x=560, pose="point_you", expr="warm", look=3)[0]]
    elif n == 34:
        b += [acc("bubble", 1240, 360, 160)] + [ntile(1060 + i * 120, 640, i + 1, "dim" if i == 3 else "lit", 80) for i in range(6)]
        b += [F(x=560, pose="explain", expr="warm", look=6)[0]]
    elif n == 35:
        b += [tiles_arc(960, 820, 520, 200, 340, ["lit"] * 6, 120)]
    elif n == 36:
        b += [floor_line(), sprout_brain(560, 420, 220, .8), F(x=1000, pose="stand", expr="serene")[0], acc("bell", 1620, 200, 90), acc("hand", 1780, 200, 80)]
    else:
        raise ValueError(n)
    return b


def thumb_b():
    """Mẫu B — triptych: mirar el error con calma · recibir feedback honesto · ir hacia lo difícil (vật nhấn)."""
    pw = TW / 3
    b = [panel_bg(0, 0, pw, TH, "#7FB8FF", .26), panel_bg(pw, 0, pw, TH, "#FFB46B", .24), panel_bg(2 * pw, 0, pw, TH, "#8B6CFF", .26)]
    b += [figure(140, 560, .95, "think", "thoughtful", look=6)[0], ico("xmark", 330, 260, 90, INK), ico("magnifier", 345, 245, 140, INK, .7)]
    fig, an = figure(pw + 140, 560, .95, "reach", "attentive", look=6)
    b += [fig, ico("notes", an["rhand"][0] + 70, an["rhand"][1] - 20, 100, INK)]
    fig, an = figure(2 * pw + 130, 560, .95, "reach", "attentive", look=6)
    b += [fig, acc("target", an["rhand"][0] + 70, an["rhand"][1] - 110, 100)]
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 3}" y="0" width="6" height="{TH}" fill="#000"/>')
    b.append(badge())
    return b


def thumb_c():
    """Mẫu C — lưới 6 khung."""
    pw, ph = TW / 3, TH / 2
    tints = ("#7FB8FF", "#FFB46B", "#8B6CFF", "#5AC8A0", "#FF6B6B", "#FFD9A0")
    b = [panel_bg((i % 3) * pw, (i // 3) * ph, pw, ph, t, .22) for i, t in enumerate(tints)]
    b += [figure(120, 320, .58, "think", "thoughtful", look=6)[0], ico("xmark", 300, 160, 70, INK), ico("magnifier", 310, 150, 110, INK, .7)]   # 1
    fig, an = figure(540, 320, .58, "reach", "attentive", look=6)
    b += [fig, ico("notes", an["rhand"][0] + 50, an["rhand"][1] - 10, 70, INK)]                                       # 2
    fig, an = figure(960, 320, .58, "reach", "attentive", look=6)
    b += [fig, acc("target", an["rhand"][0] + 90, an["rhand"][1] - 60, 90)]                                             # 3
    b += [word_bubble(200, 420, 260, open_end=True)]                                                                    # 4 todavía
    b += [figure(560, 460, .34, "stand", "attentive", look=6)[0], figure(720, 460, .34, "open_arms", "proud")[0], ico("star", 790, 330, 44, INK)]  # 5
    b += [figure(1040, 520, .45, "hands_hips", "satisfied")[0], ico("guitar", 1170, 420, 70, INK)]                     # 6
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 1.5}" y="0" width="3" height="{TH}" fill="{BG}"/>')
    b.append(f'<rect x="0" y="{ph - 1.5}" width="{TW}" height="3" fill="{BG}"/>')
    b.append(badge())
    return b

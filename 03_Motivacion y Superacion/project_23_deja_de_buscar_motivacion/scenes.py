# -*- coding: utf-8 -*-
"""
scenes.py — Kịch bản hình của project 23 "¿Buscas Motivación? Deja De Buscarla y Haz Esto"
(34 khung + 2 thumbnail), bám theo [VISUAL DESCRIPTION] trong transcript_and_visuals.txt.
Màu nhấn #FF3B78 (03_Motivacion y Superacion).
Mô-típ: tia lửa tắt (chờ động lực) · dấu chân → tia lửa sáng (hành động trước, động lực sau) ·
danh sách việc nhỏ gạch xong · hẹn giờ 10 phút · điện thoại lướt video vòng lặp.
"""
from scenekit import *  # noqa: F401,F403
from sticklib import *  # noqa: F401,F403  (nạp lại ACC sau khi đã set_accent theo playlist)
from scenekit import FLOOR, table
from thumbkit import TH, TW, badge, panel_bg


def spark_off(x, y, size=160, op=.3):
    return ico("spark", x, y, size, INK, op)


def arrow_r(x0, x1, y, color=None, op=.9, w=6, dash=None):
    color = color or ACC
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<g opacity="{op}"><line x1="{x0}" y1="{y}" x2="{x1 - 6}" y2="{y}" stroke="{color}" stroke-width="{w}" stroke-linecap="round"{d}/>'
            f'<path d="M{x1 - 24},{y - 16} L{x1},{y} L{x1 - 24},{y + 16}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/></g>')


def step_spark(x0=620, x1=1300, y=520, size=180):
    """Dấu chân trước → mũi tên → tia lửa bừng sáng (xuất hiện lần lượt)."""
    mid0, mid1 = x0 + size * .7, x1 - size * .75
    return (f'<g data-dot="0">{ico("footprint", x0, y, size, INK)}</g>'
            f'<g data-dot="1">{arrow_r(mid0, mid1, y, INK, .6, 5)}</g>'
            f'<g data-dot="2">{acc("spark", x1, y, size * 1.15)}</g>')


def seated(x, s=1.12, expr="resigned", look=5, op=1.0, phone=False):
    out = chair(x - 10, FLOOR, s, op)
    fig, an = figure(x, FLOOR, s, "sit", expr, look=look, op=op)
    return out + fig, an


def hunch_phone(x, shot=None, s=1.12, expr="distracted", look=4, glow_phone=True):
    fig, an = figure(x, FLOOR, s, "hunch", expr, look=look)
    hx, hy = an["rhand"]
    ph = acc("phone", hx + 10, hy - 20, 70 * s) if glow_phone else ico("phone", hx + 10, hy - 20, 70 * s, INK)
    return fig + ph, an


def flow_line(x0, y0, x1, y1, color=None, w=6):
    color = color or ACC
    return (f'<g data-flow="1"><line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" stroke="{color}" stroke-width="{w}" '
            f'stroke-dasharray="6 22" stroke-linecap="round"/></g>')


def loop_ring(cx, cy, rx, ry, color=INK, op=.5):
    return (f'<g data-flow="1" opacity="{op}"><ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{color}" '
            f'stroke-width="5" stroke-dasharray="18 14"/></g>')


def build_layers(n, shot):
    F = lambda **kw: shot_fig(shot, **kw)  # noqa: E731
    b = []
    # ---------------------------------------------------------------- GANCHO
    if n == 1:
        fig, _ = seated(760)
        b += [floor_line(), spark_off(1420, 380, 150), fig]
    elif n == 2:
        fig, _ = seated(520)
        b += [floor_line(), fig]
        b += [f'<g data-dot="{i}">' + ico("calendar", 900 + i * 190, 360 + (i % 2) * 30, 120, INK, .35 + i * .1) + "</g>" for i in range(5)]
        b += [arrow_r(880, 1760, 520, INK, .3, 4, "10 12")]
    elif n == 3:
        b += [spark_off(1300, 470, 320, .35), F(x=620, pose="stand", expr="neutral", look=6)[0]]
    elif n == 4:
        fig, _ = seated(500)
        b += [floor_line(), fig, line(720, 700, 1460, 520, INK, 4, .25, "6 18"), acc("target", 1600, 470, 150)]
    elif n == 5:
        b += [F(x=960, pose="explain", expr="attentive")[0]]
    # ---------------------------------------------------------------- M1 — El orden al revés
    elif n == 6:
        b += [ico("spark", 700, 500, 200, INK, .8), ico("footprint", 1240, 500, 180, INK, .8)]
        b += [f'<g data-acc="970,500">' + arrow_r(840, 1110, 500, ACC, 1, 8) + "</g>",
              ico("xmark", 970, 640, 70, ACC, .9)]
    elif n == 7:
        b += [acc("nomotiv_book", 1340, 470, 240), F(x=720, pose="stand", expr="thoughtful", look=6)[0]]
    elif n == 8:
        b += [floor_line()]
        for i, x in enumerate((330, 750, 1170, 1590)):
            fig, an = figure(x, FLOOR, .78, "stand", "uneasy", look=5)
            b += [f'<g data-dot="{i}">' + fig + spark_off(x + 150, an["top"][1] + 30, 90, .35) + "</g>"]
    elif n == 9:
        b += [step_spark(640, 1300, 500, 200)]
    elif n == 10:
        fig, an = F(x=980, pose="stride", expr="determined", look=6)
        tx, ty = an["top"]
        b += [fig, ico("thought", tx - 150, ty - 40, 150, INK, .28), ico("question", tx - 150, ty - 46, 50, INK, .3)]
        b += [f'<g data-dot="{i}">' + ico("footprint", 420 + i * 150, 870 - (i % 2) * 22, 60, INK, .25 + i * .1, rot=90) + "</g>" for i in range(3)]
    elif n == 11:
        b += [floor_line(), step_spark(560, 1360, 520, 220)]
    # ---------------------------------------------------------------- M2 — El progreso pequeño
    elif n == 12:
        b += [acc("check", 740, 500, 200), ico("megaphone", 1220, 500, 190, INK, .35), ico("xmark", 1220, 500, 120, INK, .5)]
    elif n == 13:
        b += [ico("bank", 1180, 400, 220, INK, .75)]
        b += [f'<g data-dot="{i}">' + acc("notebook", 1420 + i * 130, 660, 110, op=.6) + "</g>" for i in range(3)]
        b += [F(x=620, pose="explain", expr="calm", look=6)[0]]
    elif n == 14:
        for i, nm in enumerate(("trophy", "coin", "bubble")):
            x = 560 + i * 400
            b += [f'<g data-dot="{i}">' + ico(nm, x, 480, 190, INK, .55 - i * .12) + ico("xmark", x + 80, 600, 60, INK, .45) + "</g>"]
    elif n == 15:
        b += [ico(nm, 1060 + i * 180, 220, 80, INK, .15) for i, nm in enumerate(("trophy", "coin", "bubble"))]
        b += [glow(1300, 540, 260, "A", .8), ico("todo", 1300, 540, 230, INK, rows=3, done=1, mark=ACC)]
        b += [F(x=640, pose="explain", expr="smile", look=6)[0]]
    elif n == 16:
        fig, an = F(x=760, pose="point", expr="satisfied", look=6)
        b += [fig, f'<g data-acc="1280,520">' + glow(1280, 520, 260, "A", .9) + ico("todo", 1280, 520, 260, INK, rows=3, done=2, mark=ACC) + "</g>"]
    elif n == 17:
        b += [acc("check", 760, 520, 220)]
        b += [ico("bubble", 1300, 520, 200, INK, .2), ico("sun", 1180, 250, 80, INK, .35), arrow_r(1250, 1400, 250, INK, .3, 4),
              ico("moon", 1470, 250, 80, INK, .35)]
    # ---------------------------------------------------------------- M3 — Qué hacer en la práctica
    elif n == 18:
        b += [acc("timer", 960, 500, 260, progress=1.0)]
    elif n == 19:
        b += [ico("question", 1060, 430, 230, INK, .25), ico("face", 1060, 640, 80, INK, .25, mood=-1),
              arrow_r(1200, 1340, 500, INK, .4, 5), acc("timer", 1500, 500, 170, progress=1.0)]
        b += [F(x=560, pose="think", expr="thoughtful", look=6)[0]]
    elif n == 20:
        b += [ico("book", 660, 480, 300, INK, .3, progress=0), arrow_r(900, 1160, 480, INK, .45, 5), acc("document", 1360, 480, 130)]
    elif n == 21:
        b += [ico("dumbbell", 660, 480, 300, INK, .3), arrow_r(900, 1160, 480, INK, .45, 5), acc("tshirt", 1360, 480, 150)]
    elif n == 22:
        b += [ico("document", 760, 520, 140, INK), ico("tshirt", 1160, 520, 150, INK)]
        b += [f'<g data-dot="{i}">' + acc("check", x + 70, 400, 80) + "</g>" for i, x in enumerate((760, 1160))]
        b += [F(x=430, pose="explain", expr="calm", look=6)[0]] if shot != "CLOSE-UP" else []
    elif n == 23:
        b += [ico("check", 560, 520, 150, INK, .9), flow_line(660, 520, 1180, 500), acc("brain", 1360, 500, 220)]
    elif n == 24:
        b += [ico("toggle", 560, 340, 170, INK, .35, on=False), ico("xmark", 560, 340, 140, INK, .6)]
        b += [step_spark(840, 1460, 640, 180)]
    # ---------------------------------------------------------------- M4 — La trampa
    elif n == 25:
        b += [loop_ring(960, 500, 230, 230, INK, .45), acc("phone", 960, 500, 230), ico("reel", 960, 500, 70, ACC)]
    elif n == 26:
        fig, an = hunch_phone(700, s=1.5, look=5)
        b += [fig, loop_ring(1400, 500, 170, 260, INK, .35)]
        b += [f'<g data-dot="{i}">' + ico(nm, 1400 + dx, 500 + dy, 90, INK, .55) + "</g>"
              for i, (nm, dx, dy) in enumerate((("reel", 0, -250), ("bubble", 170, 0), ("reel", 0, 250), ("note", -170, 0)))]
    elif n == 27:
        fig, an = hunch_phone(640)
        b += [floor_line(), fig, spark_off(1500, 360, 150, .3)]
        b += [ico("footprint", 900 + i * 180, 880 - (i % 2) * 20, 60, INK, .18, rot=90) for i in range(5)]
    elif n == 28:
        fig, an = hunch_phone(600, s=1.5)
        b += [fig, f'<rect x="1040" y="270" width="620" height="54" rx="27" fill="none" stroke="{INK}" stroke-width="5" opacity=".6"/>',
              f'<g data-acc="1240,297">' + glow(1240, 297, 220, "A", .7) + '<rect x="1052" y="282" width="460" height="30" rx="15" fill="' + ACC + '"/></g>']
        b += [ico("footprint", 1080 + i * 170, 860 - (i % 2) * 22, 60, INK, .15, rot=90) for i in range(4)]
    elif n == 29:
        fig, an = hunch_phone(620)
        tx, ty = an["top"]
        b += [fig, ico("thought", 1240, 400, 420, INK, .7), spark_off(1240, 390, 140, .4), loop_ring(620, 880, 200, 40, INK, .3)]
    elif n == 30:
        b += [floor_line()]
        for i, x in enumerate((240, 520, 800, 1080)):
            fig, an = figure(x, FLOOR, .62, "hunch", "distracted", look=4, op=.35 + i * .15)
            b += [f'<g data-dot="{i}">' + chair(x - 6, FLOOR, .62, .35 + i * .15) + fig + ico("phone", an["rhand"][0] + 6, an["rhand"][1] - 12, 40, INK, .5) + "</g>"]
        b += [timeline(160, 940, 1300, 940, ticks=4, color=INK, w=3, op=.3), acc("target", 1680, 420, 110)]
    # ---------------------------------------------------------------- CIERRE
    elif n == 31:
        fig, an = F(x=900, pose="reach", expr="determined", look=6)
        hx, hy = an["rhand"]
        b += [floor_line(), ico("phone", 560, 885, 60, INK, .3, rot=90), fig, acc("timer", hx + 90, hy - 20, 120, progress=1.0)]
    elif n == 32:
        fig, an = F(x=760, pose="stride", expr="determined", look=6)
        b += [fig, ico("footprint", 1080, 860, 70, INK, .9, rot=90), acc("spark", 1420, 400, 220)]
    elif n == 33:
        b += [acc("bubble", 1320, 380, 180), ico("timer", 1520, 600, 110, INK, .6, progress=1.0), F(x=700, pose="point_you", expr="warm", look=3)[0]]
    elif n == 34:
        b += [floor_line(), acc("spark", 520, 420, 300, glow_r=420), F(x=960, pose="walk", expr="serene", look=6)[0],
              acc("bell", 1620, 200, 90), acc("heart", 1780, 200, 80)]
    else:
        raise ValueError(n)
    return b


def thumb_b():
    """Mẫu B — triptych: mặc đồ tập không chờ sẵn sàng · viết 1 đoạn văn · gạch 1 việc nhỏ (vật nhấn)."""
    pw = TW / 3
    b = [panel_bg(0, 0, pw, TH, "#5AC8A0", .24), panel_bg(pw, 0, pw, TH, "#7FB8FF", .24), panel_bg(2 * pw, 0, pw, TH, "#FFB46B", .24)]
    fig, an = figure(pw / 2 - 30, 560, .95, "reach", "determined", look=6)
    b += [fig, ico("tshirt", an["rhand"][0] + 30, an["rhand"][1] - 30, 90, INK)]
    mid = pw + pw / 2
    b += [line(mid - 10, 440, mid + 190, 440, INK, 7), line(mid + 90, 440, mid + 90, 560, INK, 6), ico("document", mid + 90, 400, 70, INK),
          chair(mid - 120, 560, .9), figure(mid - 110, 560, .9, "type", "attentive", look=5)[0]]
    x3 = 2 * pw + pw / 2
    b += [figure(x3 - 90, 560, .95, "point", "satisfied", look=6)[0],
          glow(x3 + 90, 300, 160, "A", .9), ico("todo", x3 + 90, 300, 150, INK, rows=3, done=1, mark=ACC)]
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 3}" y="0" width="6" height="{TH}" fill="#000"/>')
    b.append(badge())
    return b


def thumb_c():
    """Mẫu C — lưới 6 khung."""
    pw, ph = TW / 3, TH / 2
    tints = ("#7FB8FF", "#FF6B6B", "#FFB46B", "#5AC8A0", "#8C7BFF", "#FFD9A0")
    b = [panel_bg((i % 3) * pw, (i // 3) * ph, pw, ph, t, .22) for i, t in enumerate(tints)]
    b += [chair(150, 320, .58), figure(160, 320, .58, "sit", "uneasy", look=5)[0], spark_off(320, 150, 80, .35)]     # 1 esperando
    b += [ico("footprint", 560, 200, 110, INK), arrow_r(620, 700, 200, INK, .5, 4), acc("spark", 770, 190, 120)]      # 2 acción → chispa
    b += [figure(980, 320, .58, "point", "satisfied", look=6)[0], ico("todo", 1140, 180, 120, INK, rows=3, done=1, mark=ACC)]  # 3
    b += [figure(130, 460, .34, "reach", "determined", look=6)[0], acc("timer", 300, 420, 70, progress=1.0)]           # 4 (sobre el titular)
    b += [ico("phone", 640, 420, 70, INK, .7), loop_ring(640, 420, 70, 70, INK, .4)]                                  # 5 trampa
    b += [glow(1180, 430, 160, "A", .8), ico("spark", 1180, 430, 100, ACC), figure(1040, 520, .45, "stride", "determined", look=6)[0]]  # 6
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 1.5}" y="0" width="3" height="{TH}" fill="{BG}"/>')
    b.append(f'<rect x="0" y="{ph - 1.5}" width="{TW}" height="3" fill="{BG}"/>')
    b.append(badge())
    return b

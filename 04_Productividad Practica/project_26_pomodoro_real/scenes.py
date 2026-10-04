# -*- coding: utf-8 -*-
"""
scenes.py — Kịch bản hình của project 26 "La Técnica Pomodoro Real (No la Versión de tu App)"
(49 khung + 2 thumbnail), bám theo [VISUAL DESCRIPTION] trong transcript_and_visuals.txt.
Màu nhấn #3BA7C9 (04_Productividad Practica).
Mô-típ: icon hẹn giờ "25" trong app (mảnh nhỏ) · hình tròn lớn tách 2 nửa (nửa mờ = chu kỳ 25/5,
nửa sáng = quy tắc không chia nhỏ + nhật ký gián đoạn) · đồng hồ cà chua · sợi chỉ "residuo de atención" ·
sổ ghi vạch đếm.
"""
from scenekit import *  # noqa: F401,F403
from sticklib import *  # noqa: F401,F403  (nạp lại ACC sau khi đã set_accent theo playlist)
from scenekit import FLOOR, desk, marker, table
from thumbkit import TH, TW, badge, panel_bg


def app_timer(x, y, size=150, op=1.0, color=INK):
    return (ico("phone", x, y, size, color, op)
            + f'<text x="{x}" y="{y + size * .14:.0f}" font-family="Anton" font-size="{size * .36:.0f}" fill="{color}" opacity="{op}" text-anchor="middle">25</text>')


def big_shape(cx, cy, r, mode="faint"):
    """Hình tròn lớn của 'kỹ thuật thật'. mode: faint · form · split · fade (nửa sáng chìm đi)."""
    if mode in ("faint", "form"):
        op = .18 if mode == "faint" else .45
        return (glow(cx, cy, r * 1.1, "A", .25 if mode == "form" else .12)
                + f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{ACC}" stroke-width="6" opacity="{op}" stroke-dasharray="{"18 14" if mode == "faint" else "none"}"/>')
    left = f'<path d="M{cx - 14},{cy - r} A{r},{r} 0 0 0 {cx - 14},{cy + r} Z" fill="none" stroke="{INK}" stroke-width="6" opacity=".35"/>'
    rop = 1 if mode == "split" else .12
    right = (f'<path d="M{cx + 14},{cy - r} A{r},{r} 0 0 1 {cx + 14},{cy + r} Z" fill="{ACC}" fill-opacity="{.18 * rop:.2f}" stroke="{ACC}" stroke-width="7" opacity="{rop}"/>')
    if mode == "split":
        right = f'<g data-acc="{cx + r * .45:.0f},{cy}">' + glow(cx + r * .45, cy, r * .9, "A", .6) + right + "</g>"
    return left + right


def loop_cycle(cx, cy, r=170, op=.8, size=70):
    out = [f'<g data-flow="1" opacity="{op * .6:.2f}"><circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{INK}" stroke-width="4" stroke-dasharray="14 12"/></g>']
    for i, nm in enumerate(("timer", "laptop", "bell", "sofa")):
        a = math.radians(-90 + 90 * i)
        out.append(f'<g data-dot="{i}">' + f'<circle cx="{cx + r * math.cos(a):.0f}" cy="{cy + r * math.sin(a):.0f}" r="{size * .62:.0f}" fill="{BG}"/>'
                   + ico(nm, cx + r * math.cos(a), cy + r * math.sin(a), size, INK, op) + "</g>")
    return "".join(out)


def tomato(x, y, size=160, lit=True, op=1.0):
    return acc("tomato", x, y, size, op=op) if lit else ico("tomato", x, y, size, INK, op)


def tally_page(x, y, w=260, marks=(5, 3, 4), op=1.0, lit=False):
    col = ACC if lit else INK
    h = w * 1.25
    out = [f'<rect x="{x - w / 2:.0f}" y="{y - h / 2:.0f}" width="{w:.0f}" height="{h:.0f}" rx="12" fill="{BG}" stroke="{col}" stroke-width="5" opacity="{op}"/>']
    for r, m in enumerate(marks):
        yy = y - h / 2 + h * (.25 + r * .25)
        x0 = x - w * .36
        for k in range(m):
            if k == 4:
                out.append(f'<line x1="{x0 - 8:.0f}" y1="{yy + 22:.0f}" x2="{x0 + 4 * w * .07 + 6:.0f}" y2="{yy - 22:.0f}" stroke="{col}" stroke-width="4" opacity="{op}"/>')
            else:
                out.append(f'<line x1="{x0 + k * w * .07:.0f}" y1="{yy - 24:.0f}" x2="{x0 + k * w * .07:.0f}" y2="{yy + 24:.0f}" stroke="{col}" stroke-width="4" opacity="{op}"/>')
    g = "".join(out)
    return (f'<g data-acc="{x},{y}">' + glow(x, y, w * .9, "A", .6) + g + "</g>") if lit else g


def struck(svg_icon, x, y, size, op=.6):
    return svg_icon + line(x - size * .5, y + size * .5, x + size * .5, y - size * .5, INK, 6, op)


def build_layers(n, shot):
    F = lambda **kw: shot_fig(shot, **kw)  # noqa: E731
    b = []
    # ---------------------------------------------------------------- GANCHO
    if n == 1:
        fig, an = F(x=860, pose="point", expr="neutral", look=6)
        hx, hy = an["rhand"]
        b += [floor_line(), fig, app_timer(hx + 110, hy - 40, 150)]
    elif n == 2:
        b += [big_shape(1100, 480, 330, "faint"), app_timer(1100, 480, 110), F(x=480, pose="stand", expr="neutral", look=6)[0]]
    elif n == 3:
        b += [big_shape(1250, 470, 340, "faint"), app_timer(1250, 470, 90, .8), F(x=620, pose="stand", expr="realize", look=5)[0]]
    # ---------------------------------------------------------------- PROMESA
    elif n == 4:
        b += [big_shape(1280, 470, 320, "form"), F(x=600, pose="explain", expr="attentive", look=6)[0]]
    elif n == 5:
        b += [big_shape(1100, 470, 300, "form"), app_timer(1560, 760, 100, .4), F(x=520, pose="dismiss", expr="calm", look=6)[0]]
    elif n == 6:
        b += [big_shape(960, 500, 330, "split")]
    # ---------------------------------------------------------------- 1 — Cómo casi todos la hacen mal
    elif n == 7:
        b += [floor_line(), marker(1, 1340, 380, 190), app_timer(1640, 640, 120, .7), F(x=700, pose="stand", expr="calm", look=6)[0]]
    elif n == 8:
        b += [loop_cycle(960, 500, 230, .85, 90)]
    elif n == 9:
        b += [loop_cycle(1380, 480, 170, .6, 60), F(x=640, pose="stand", expr="neutral", look=6)[0]]
    elif n == 10:
        b += [floor_line(), loop_cycle(1360, 480, 180, .75, 64), F(x=640, pose="reassure", expr="calm", look=6)[0]]
    elif n == 11:
        b += [big_shape(1200, 480, 300, "split"), loop_cycle(1060, 480, 110, .5, 40), F(x=480, pose="explain", expr="thoughtful", look=6)[0]]
    elif n == 12:
        b += [big_shape(960, 500, 320, "fade"), loop_cycle(840, 500, 140, 1, 54)]
    # ---------------------------------------------------------------- 2 — El origen real (Cirillo)
    elif n == 13:
        b += [floor_line(), marker(2, 1340, 380, 190), F(x=700, pose="stand", expr="attentive", look=6)[0]]
    elif n == 14:
        b += [ico("calendar", 1340, 420, 180, INK, .45), f'<text x="1340" y="590" font-family="Anton" font-size="64" fill="{INK}" opacity=".45" text-anchor="middle">1987</text>',
              F(x=700, pose="explain", expr="thoughtful", look=6)[0]]
    elif n == 15:
        b += [desk(960, 800, 520, .5), chair(820, FLOOR, 1.2, .45), figure(830, FLOOR, 1.2, "sit", "worried", look=5, op=.55, ghost=True)[0]]
        b += [ico("book", 1080 + dx, 760 + dy, 80, INK, .4, rot=r, progress=.3) for dx, dy, r in ((0, 0, -8), (130, -10, 12), (-30, 120, 20), (200, 110, -15))]
    elif n == 16:
        fig, an = figure(830, FLOOR, 1.2, "reach", "attentive", look=6, op=.8)
        b += [floor_line(), fig, tomato(an["rhand"][0] + 90, an["rhand"][1] - 20, 170)]
    elif n == 17:
        b += [floor_line(), table(1300, 760, 300), tomato(1300, 670, 170), F(x=700, pose="explain", expr="calm", look=6)[0]]
    elif n == 18:
        b += [f'<text x="960" y="620" font-family="Anton" font-size="360" fill="{INK}" opacity=".25" text-anchor="middle">25</text>',
              ico("star", 1260, 300, 90, INK, .3), line(1210, 350, 1310, 250, INK, 5, .4)]
    elif n == 19:
        fig, an = figure(830, FLOOR, 1.2, "type", "determined", look=6)
        b += [desk(1050, 760, 420), chair(820, FLOOR, 1.2), fig, tomato(1200, 690, 110),
              ico("thought", an["top"][0] + 120, an["top"][1] - 100, 150, INK, .2)]
    elif n == 20:
        b += [tomato(960, 500, 240)] + [f'<g data-dot="{i}"><text x="{x}" y="{y}" font-family="Anton" font-size="64" fill="{INK}" opacity=".5" text-anchor="middle">{t}</text></g>'
                                         for i, (t, x, y) in enumerate((("15", 600, 360), ("25", 1320, 360), ("40", 600, 720), ("50", 1320, 720)))]
    # ---------------------------------------------------------------- 3 — La regla: unidad indivisible (Leroy)
    elif n == 21:
        b += [floor_line(), marker(3, 1200, 340, 170), tomato(1500, 600, 200), F(x=640, pose="stand", expr="determined", look=6)[0]]
    elif n == 22:
        b += [tomato(960, 500, 220)]
        b += [f'<g data-dot="{i}">' + ico(nm, x, y, 100, INK, .6) + "</g>" for i, (nm, x, y) in enumerate((("call", 520, 300), ("question", 480, 640), ("bulb", 1440, 330)))]
        b += [struck(ico("pause", 1420, 680, 110, INK, .7), 1420, 680, 110)]
    elif n == 23:
        b += [ico("tomato", 760, 500, 220, INK, .2), line(900, 500, 1060, 500, INK, 4, .4, "8 10"), tomato(1220, 500, 240)]
    elif n == 24:
        fig, an = F(x=700, pose="stop", expr="determined", look=6)
        b += [fig, ico("thought", 1180, 330, 130, INK, .25), ico("question", 1180, 325, 50, INK, .3), acc("document", 1480, 520, 170)]
    elif n == 25:
        b += [ico("campus", 1360, 430, 220, INK, .5), F(x=700, pose="explain", expr="thoughtful", look=6)[0]]
    elif n == 26:
        fig, an = F(x=1300, pose="walk", expr="uneasy", look=6)
        hx, hy = an["sh"]
        b += [ico("task", 460, 500, 150, INK, .55), fig,
              f'<g data-acc="{(540 + hx) / 2:.0f},{(500 + hy) / 2:.0f}">' + glow((540 + hx) / 2, (500 + hy) / 2, 160, "A", .5)
              + f'<path d="M540,500 Q{(540 + hx) / 2:.0f},{hy + 120:.0f} {hx - 20:.0f},{hy:.0f}" stroke="{ACC}" stroke-width="4" fill="none" opacity=".9"/></g>']
    elif n == 27:
        fig, an = F(x=1400, pose="walk", expr="uneasy", look=6)
        b += [floor_line(), ico("task", 460, 520, 150, INK, .55), fig,
              f'<path d="M540,520 Q640,600 760,560" stroke="{ACC}" stroke-width="4" fill="none" opacity=".5"/>',
              f'<path d="M1180,520 Q1240,500 1300,480" stroke="{ACC}" stroke-width="3" fill="none" opacity=".3" stroke-dasharray="6 8"/>',
              f'<circle cx="760" cy="560" r="10" fill="{ACC}" opacity=".6"/>']
    elif n == 28:
        b += [acc("timer", 960, 480, 220, progress=1.0), ico("pause", 1180, 300, 70, INK, .4),
              f'<path d="M1060,580 Q1120,680 1220,700" stroke="{INK}" stroke-width="3" fill="none" opacity=".4"/>', f'<circle cx="1226" cy="702" r="12" fill="{INK}" opacity=".35"/>']
    elif n == 29:
        b += [ico("tomato", 760, 500, 220, INK, .35), ico("tomato", 1160, 500, 220, INK, .35),
              f'<circle cx="1560" cy="500" r="40" fill="none" stroke="{ACC}" stroke-width="4" opacity=".4"/>']
    # ---------------------------------------------------------------- 4 — La mitad olvidada: el registro
    elif n == 30:
        fig, an = F(x=700, pose="explain", expr="calm", look=6)
        b += [floor_line(), marker(4, 1340, 380, 190), fig, acc("notebook", an["rhand"][0] + 70, an["rhand"][1] - 20, 110)]
    elif n == 31:
        fig, an = F(x=640, pose="explain", expr="determined", look=6)
        b += [fig, tally_page(1100, 520, 240, (3,), lit=True)]
        b += [f'<g data-dot="{i}">' + ico(nm, 1450 + (i % 2) * 120, 300 + i * 170, 90, INK, .5) + "</g>" for i, nm in enumerate(("call", "bell", "envelope"))]
    elif n == 32:
        b += [ico("thought", 700, 480, 240, INK, .8),
              ico("door", 1220, 500, 220, INK, .6), acc("hand", 1360, 470, 110)]
    elif n == 33:
        b += [floor_line(), ico("moon", 1650, 200, 90, INK, .5), chair(700, FLOOR, 1.12), figure(710, FLOOR, 1.12, "sit", "thoughtful", look=6)[0],
              tally_page(1180, 500, 280, (5, 4, 5), lit=True)]
    elif n == 34:
        b += [ico("face", 700, 500, 200, INK, .35, mood=-1), line(600, 600, 800, 400, INK, 6, .5), line(860, 500, 1040, 500, INK, 4, .4, "8 10"),
              acc("bars", 1240, 500, 220, vals=(.4, .8, .55, .3))]
    elif n == 35:
        fig, an = F(x=860, pose="think", expr="confused")
        b += [fig, ico("cloud", an["top"][0] + 220, an["top"][1] - 60, 220, INK, .35)]
    elif n == 36:
        b += [ico("cloud", 600, 420, 220, INK, .15), line(760, 470, 940, 470, INK, 4, .4, "8 10"), tally_page(1240, 500, 300, (5, 2, 4, ), lit=True)]
    elif n == 37:
        fig, an = F(x=760, pose="stand", expr="realize", look=6)
        b += [fig, tally_page(1420, 520, 260, (5, 5, 3), lit=True)]
    # ---------------------------------------------------------------- 5 — Descanso largo y ciclo completo
    elif n == 38:
        b += [floor_line()]
        b += [f'<g data-dot="{i}">' + ico("tomato", 360 + i * 200, 360, 130, INK, .9) + ico("check", 360 + i * 200, 250, 50, INK, .7) + "</g>" for i in range(4)]
        b += [acc("sofa", 1320, 360, 200), chair(1600, FLOOR, 1.0), figure(1610, FLOOR, 1.0, "sit", "satisfied", look=-5)[0]]
    elif n == 39:
        b += [ico("boxes", 1300, 500, 220, INK, .3), F(x=680, pose="dismiss", expr="calm", look=6)[0]]
    elif n == 40:
        b += [ico("laptop", 640, 500, 220, INK), acc("sofa", 1280, 500, 220),
              f'<g data-flow="1"><path d="M790,450 Q960,360 1130,450" stroke="{ACC}" stroke-width="5" fill="none" stroke-dasharray="8 16"/>'
              f'<path d="M1130,560 Q960,650 790,560" stroke="{ACC}" stroke-width="5" fill="none" stroke-dasharray="8 16"/></g>']
    elif n == 41:
        b += [floor_line(), glow(820, 600, 300, "warm", .7), chair(810, FLOOR, 1.12), figure(820, FLOOR, 1.12, "sit", "serene", look=5)[0],
              ico("phone", 1480, 520, 110, INK, .3), acc("hand", 1300, 530, 100)]
    elif n == 42:
        fig, an = figure(820, FLOOR, 1.2, "type", "determined", look=6)
        b += [desk(1040, 760, 420), chair(810, FLOOR, 1.2), fig, acc("timer", 1200, 690, 80, progress=.6),
              ico("thought", an["top"][0] + 160, an["top"][1] - 110, 130, INK, .15), ico("sofa", an["top"][0] + 160, an["top"][1] - 116, 50, INK, .15)]
    # ---------------------------------------------------------------- CIERRE
    elif n == 43:
        b += [app_timer(760, 520, 200, .35), big_shape(1280, 500, 260, "split")]
    elif n == 44:
        fig, an = F(x=960, pose="open_arms", expr="proud")
        b += [fig, tomato(an["lhand"][0] - 120, an["lhand"][1] - 40, 150), tally_page(an["rhand"][0] + 140, an["rhand"][1] - 40, 150, (5, 2), lit=False)]
    elif n == 45:
        b += [app_timer(1260, 400, 140, .2), ico("tomato", 1520, 560, 130, INK, .2), F(x=700, pose="explain", expr="calm", look=6)[0]]
    elif n == 46:
        b += [acc("timer", 760, 500, 220, progress=1.0), ico("notebook", 1180, 500, 220, INK)]
    elif n == 47:
        fig, an = F(x=960, pose="open_arms", expr="determined", look=6)
        b += [floor_line(), fig, acc("timer", an["rhand"][0] + 90, an["rhand"][1] - 30, 110, progress=1.0), ico("notebook", an["lhand"][0] - 90, an["lhand"][1] - 30, 100, INK)]
    elif n == 48:
        b += [acc("bubble", 1320, 380, 180), F(x=700, pose="point_you", expr="warm", look=3)[0]]
    elif n == 49:
        b += [rim(960, 500, 620), F(x=960, pose="stand", expr="serene")[0]]
    else:
        raise ValueError(n)
    return b


def thumb_b():
    """Mẫu B — triptych: poner el tomate · anotar la interrupción · descanso largo (vật nhấn)."""
    pw = TW / 3
    b = [panel_bg(0, 0, pw, TH, "#FF6B6B", .22), panel_bg(pw, 0, pw, TH, "#7FB8FF", .24), panel_bg(2 * pw, 0, pw, TH, "#5AC8A0", .24)]
    fig, an = figure(pw / 2 - 50, 560, .95, "reach", "calm", look=6)
    b += [fig, ico("tomato", an["rhand"][0] + 60, an["rhand"][1] - 20, 110, INK)]
    fig, an = figure(pw + pw / 2 - 60, 560, .95, "explain", "determined", look=6)
    b += [fig, ico("notebook", an["rhand"][0] + 40, an["rhand"][1] - 40, 90, INK), ico("call", pw + pw - 70, 160, 70, INK, .5)]
    x3 = 2 * pw + pw / 2
    b += [acc("sofa", x3, 470, 220), figure(x3, 520, .8, "sit", "satisfied", look=5)[0]]
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 3}" y="0" width="6" height="{TH}" fill="#000"/>')
    b.append(badge())
    return b


def thumb_c():
    """Mẫu C — lưới 6 khung."""
    pw, ph = TW / 3, TH / 2
    tints = ("#FF6B6B", "#7FB8FF", "#FFB46B", "#8C7BFF", "#5AC8A0", "#FFD9A0")
    b = [panel_bg((i % 3) * pw, (i // 3) * ph, pw, ph, t, .22) for i, t in enumerate(tints)]
    b += [glow(213, 180, 150, "A", .6), ico("tomato", 213, 185, 190, ACC)]                                          # 1 origen
    b += [line(600, 300, 800, 300, INK, 7), line(620, 300, 620, 352, INK, 6), line(780, 300, 780, 352, INK, 6), chair(560, 320, .58), figure(566, 320, .58, "type", "determined", look=6)[0], ico("timer", 760, 260, 50, INK)]  # 2
    fig, an = figure(1000, 320, .58, "explain", "determined", look=6)
    b += [fig, ico("notebook", an["rhand"][0] + 26, an["rhand"][1] - 24, 54, INK), ico("call", 1190, 120, 60, INK, .5)]  # 3
    b += [tally_page(300, 420, 110, (5, 3), lit=True)]                                                               # 4 registro
    b += [ico("sofa", 560, 420, 110, INK, .8), ico("moon", 720, 410, 60, INK, .5)]                # 5 descanso
    b += [figure(1066, 520, .45, "hands_hips", "satisfied")[0]]                                                      # 6 cierre
    for i in (1, 2):
        b.append(f'<rect x="{i * pw - 1.5}" y="0" width="3" height="{TH}" fill="{BG}"/>')
    b.append(f'<rect x="0" y="{ph - 1.5}" width="{TW}" height="3" fill="{BG}"/>')
    b.append(badge())
    return b

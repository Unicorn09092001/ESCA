# -*- coding: utf-8 -*-
"""
sticklib.py — Thư viện vẽ người que + biểu tượng (SVG) theo STYLE RULES của kênh Cúspide Silenciosa:
nền #0B0B0C, nét trắng ấm #F5F5F0 dày, bo tròn; chỉ MỘT vật nhấn màu playlist mỗi khung.

Mọi icon được vẽ trong hộp chuẩn -50..50 rồi đặt bằng place(x, y, size).
"""
import math
import random
import re

BG = "#0B0B0C"
INK = "#F5F5F0"
ACC = "#8B6CFF"  # 05_Autoconocimiento
W, H = 1920, 1080
SW = 9  # độ dày nét chuẩn (đơn vị cục bộ)


def set_accent(hex_color):
    global ACC
    ACC = hex_color


# ----------------------------------------------------------------------------- khung SVG
def _dedupe(body):
    """Bỏ fill="none" (mặc định của stroke()) khi thẻ đã có fill riêng."""
    def fix(m):
        tag = m.group(0)
        if tag.count(' fill="') > 1:
            tag = tag.replace(' fill="none"', "", 1) if ' fill="none"' in tag else tag
        return tag
    return re.sub(r"<[a-zA-Z][^<>]*>", fix, body)


def svg_doc(body, w=W, h=H, bg=BG, vignette=True):
    body = _dedupe(body)
    vig = (f'<rect width="{w}" height="{h}" fill="url(#vig)"/>' if vignette else "")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs>
 <radialGradient id="glowA"><stop offset="0" stop-color="{ACC}" stop-opacity=".55"/><stop offset=".45" stop-color="{ACC}" stop-opacity=".18"/><stop offset="1" stop-color="{ACC}" stop-opacity="0"/></radialGradient>
 <radialGradient id="glowW"><stop offset="0" stop-color="{INK}" stop-opacity=".16"/><stop offset=".5" stop-color="{INK}" stop-opacity=".05"/><stop offset="1" stop-color="{INK}" stop-opacity="0"/></radialGradient>
 <radialGradient id="glowWarm"><stop offset="0" stop-color="#FFD9A0" stop-opacity=".16"/><stop offset=".6" stop-color="#FFD9A0" stop-opacity=".05"/><stop offset="1" stop-color="#FFD9A0" stop-opacity="0"/></radialGradient>
 <radialGradient id="vig" cx=".5" cy=".5" r=".75"><stop offset=".6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".55"/></radialGradient>
</defs>
<rect width="{w}" height="{h}" fill="{bg}"/>
{body}
{vig}
</svg>'''


def place(x, y, size, content, op=1.0, rot=0):
    k = size / 100.0
    return (f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot}) scale({k:.4f})" opacity="{op}">'
            f'{content}</g>')


def stroke(color=INK, w=SW, extra=""):
    return (f'fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" '
            f'stroke-linejoin="round" {extra}')


def glow(x, y, r, kind="A", op=1.0):
    gid = {"A": "glowA", "W": "glowW", "warm": "glowWarm"}[kind]
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="url(#{gid})" opacity="{op}"/>'


def floor_line(y=905, op=0.18):
    return f'<line x1="260" y1="{y}" x2="1660" y2="{y}" {stroke(INK, 4)} opacity="{op}"/>'


# ----------------------------------------------------------------------------- người que
POSES = {
    # arms: (L_upper, L_lower, R_upper, R_lower); legs: (L_th, L_sh, R_th, R_sh)
    # góc: 0 = hướng xuống, 90 = sang phải màn hình, -90 = sang trái, 180 = lên
    "stand":      ((-18, -8, 18, 8), (-12, -10, 12, 10)),
    "explain":    ((-18, -8, 62, 115), (-12, -10, 12, 10)),
    "explain_l":  ((-62, -115, 18, 8), (-12, -10, 12, 10)),
    "reassure":   ((-18, -8, 55, 160), (-12, -10, 12, 10)),
    "shrug":      ((-65, -165, 65, 165), (-12, -10, 12, 10)),
    "dismiss":    ((-18, -8, 75, 140), (-12, -10, 12, 10)),
    "cross":      ((-25, 95, 25, -95), (-12, -10, 12, 10)),
    "think":      ((-18, -8, 35, 205), (-12, -10, 12, 10)),
    "point":      ((-18, -8, 88, 92), (-12, -10, 12, 10)),
    "point_l":    ((-88, -92, 18, 8), (-12, -10, 12, 10)),
    "point_you":  ((-18, -8, 40, 130), (-12, -10, 12, 10)),
    "reach":      ((-18, -8, 70, 80), (-12, -10, 12, 10)),
    "reach_down": ((-18, -8, 50, 60), (-12, -10, 12, 10)),
    "push":       ((-18, -8, 80, 110), (-12, -10, 12, 10)),
    "thumbs":     ((-18, -8, 45, 172), (-12, -10, 12, 10)),
    "stop":       ((-18, -8, 85, 155), (-12, -10, 12, 10)),
    "step_back":  ((-30, -15, 80, 150), (-25, -8, 18, 25)),
    "walk":       ((20, 5, -25, -10), (-28, -12, 25, 38)),
    "stride":     ((25, 10, -30, -15), (-35, -20, 30, 45)),
    "strain":     ((-140, -168, 140, 168), (-32, 14, 32, -14)),
    "carry":      ((-135, -168, 135, 168), (-14, -8, 14, 8)),
    "hunch":      ((-12, -4, 12, 4), (-14, -6, 14, 6)),
    "type":       ((45, 95, 60, 95), (90, 0, 90, 0)),
    "sit":        ((10, 20, 25, 30), (90, 0, 90, 0)),
    "sit_away":   ((10, 20, -20, -60), (90, 0, 90, 0)),
    "hands_hips": ((-55, 40, 55, -40), (-14, -10, 14, 10)),
    "open_arms":  ((-70, -100, 70, 100), (-14, -10, 14, 10)),
    "head_shake": ((-20, -10, 20, 10), (-12, -10, 12, 10)),
    "stumble":    ((-80, -120, 70, 50), (-35, -15, 30, 10)),
    "cheer":      ((-35, -170, 35, 170), (-14, -10, 14, 10)),
}

EXPR = {
    # eyes, brows, mouth, k (độ cong miệng: + cười, - buồn)
    "neutral":    ("dot", None, "flat", 0),
    "calm":       ("dot", None, "curve", 5),
    "smile":      ("happy", None, "curve", 12),
    "warm":       ("dot", "soft", "curve", 11),
    "sad":        ("dot", "worried", "curve", -9),
    "worried":    ("dot", "worried", "curve", -5),
    "uneasy":     ("dot", "worried", "wavy", 0),
    "surprised":  ("wide", "raised", "o", 0),
    "confused":   ("dot", "tilt", "wavy", 0),
    "squint":     ("half", "angry", "flat", 0),
    "resigned":   ("half", None, "curve", -4),
    "thoughtful": ("up", "tilt", "flat", 0),
    "satisfied":  ("happy", None, "curve", 8),
    "proud":      ("happy", "raised", "curve", 13),
    "strain":     ("tight", "angry", "grit", 0),
    "conflict":   ("side", "worried", "wavy", 0),
    "determined": ("dot", "angry", "flat", 0),
    "realize":    ("wide", "raised", "curve", 2),
    "attentive":  ("dot", "raised", "flat", 0),
    "defensive":  ("dot", "angry", "curve", -4),
    "serene":     ("happy", "soft", "curve", 6),
    "distracted": ("side", None, "flat", 0),
    "avoid":      ("side", "worried", "curve", -3),
}


def _pt(p, ang, L):
    a = math.radians(ang)
    return (p[0] + L * math.sin(a), p[1] + L * math.cos(a))


def face(cx, cy, expr="neutral", look=0, color=INK, sw=4.5):
    eyes, brows, mouth, k = EXPR[expr]
    lx = look
    s = stroke(color, sw)
    out = []
    ey = cy - 6
    for side in (-1, 1):
        ex = cx + side * 16 + lx
        if eyes == "dot":
            out.append(f'<circle cx="{ex}" cy="{ey}" r="5.5" fill="{color}"/>')
        elif eyes == "up":
            out.append(f'<circle cx="{ex + 3}" cy="{ey - 4}" r="5.5" fill="{color}"/>')
        elif eyes == "side":
            out.append(f'<circle cx="{ex + 6 * (1 if lx >= 0 else -1)}" cy="{ey}" r="5.5" fill="{color}"/>')
        elif eyes == "wide":
            out.append(f'<circle cx="{ex}" cy="{ey}" r="8.5" {s}/><circle cx="{ex}" cy="{ey}" r="3.2" fill="{color}"/>')
        elif eyes == "happy":
            out.append(f'<path d="M{ex - 7},{ey + 2} Q{ex},{ey - 7} {ex + 7},{ey + 2}" {s}/>')
        elif eyes == "half":
            out.append(f'<line x1="{ex - 7}" y1="{ey}" x2="{ex + 7}" y2="{ey}" {s}/>')
        elif eyes == "tight":
            d = side * -1
            out.append(f'<path d="M{ex - 7 * d},{ey - 5} L{ex + 6 * d},{ey} L{ex - 7 * d},{ey + 5}" {s}/>')
    by = cy - 21
    if brows == "worried":
        out.append(f'<line x1="{cx - 25 + lx}" y1="{by + 4}" x2="{cx - 9 + lx}" y2="{by - 3}" {s}/>')
        out.append(f'<line x1="{cx + 25 + lx}" y1="{by + 4}" x2="{cx + 9 + lx}" y2="{by - 3}" {s}/>')
    elif brows == "angry":
        out.append(f'<line x1="{cx - 25 + lx}" y1="{by - 4}" x2="{cx - 9 + lx}" y2="{by + 3}" {s}/>')
        out.append(f'<line x1="{cx + 25 + lx}" y1="{by - 4}" x2="{cx + 9 + lx}" y2="{by + 3}" {s}/>')
    elif brows == "raised":
        for side in (-1, 1):
            bx = cx + side * 16 + lx
            out.append(f'<path d="M{bx - 8},{by - 2} Q{bx},{by - 9} {bx + 8},{by - 2}" {s}/>')
    elif brows == "soft":
        for side in (-1, 1):
            bx = cx + side * 16 + lx
            out.append(f'<path d="M{bx - 8},{by} Q{bx},{by - 5} {bx + 8},{by}" {s}/>')
    elif brows == "tilt":
        out.append(f'<line x1="{cx - 25 + lx}" y1="{by}" x2="{cx - 9 + lx}" y2="{by}" {s}/>')
        out.append(f'<path d="M{cx + 8 + lx},{by - 2} Q{cx + 16 + lx},{by - 10} {cx + 25 + lx},{by - 3}" {s}/>')
    # mũi
    out.append(f'<line x1="{cx + lx}" y1="{cy + 3}" x2="{cx + lx}" y2="{cy + 10}" {s}/>')
    my = cy + 24
    mx = cx + lx
    if mouth == "flat":
        out.append(f'<line x1="{mx - 11}" y1="{my}" x2="{mx + 11}" y2="{my}" {s}/>')
    elif mouth == "curve":
        out.append(f'<path d="M{mx - 13},{my} Q{mx},{my + k * 1.4} {mx + 13},{my}" {s}/>')
    elif mouth == "o":
        out.append(f'<ellipse cx="{mx}" cy="{my + 2}" rx="6" ry="8" {s}/>')
    elif mouth == "wavy":
        out.append(f'<path d="M{mx - 14},{my} Q{mx - 9.5},{my - 5} {mx - 5},{my} T{mx + 4},{my} T{mx + 13},{my}" {s}/>')
    elif mouth == "grit":
        out.append(f'<rect x="{mx - 13}" y="{my - 5}" width="26" height="10" rx="3" {s}/>'
                   f'<line x1="{mx}" y1="{my - 5}" x2="{mx}" y2="{my + 5}" {stroke(color, 3)}/>')
    return "".join(out)


def figure(x, y, s=1.0, pose="stand", expr="neutral", look=0, op=1.0, ghost=False,
           color=INK, tilt=0, extra_hand=None):
    """Vẽ người que, chân chạm (x, y). Trả về (svg, anchors) — anchors là toạ độ màn hình."""
    arms, legs = POSES[pose]
    sitting = pose in ("type", "sit", "sit_away")
    hip = (0, -70) if sitting else (0, -130)
    if pose == "hunch":
        hip = (0, -122)
    sh = (hip[0] + (8 if pose == "hunch" else 0), hip[1] - 125)
    neck_top = (sh[0] + (6 if pose == "hunch" else 0), sh[1] - 22)
    head = (neck_top[0], neck_top[1] - 48)
    if pose == "head_shake":
        head = (head[0] - 6, head[1])
    sw = SW
    dash = 'stroke-dasharray="16 13"' if ghost else ""
    st = stroke(color, sw, dash)
    parts = []
    # thân
    parts.append(f'<line x1="{hip[0]}" y1="{hip[1]}" x2="{neck_top[0]}" y2="{neck_top[1]}" {st}/>')
    # chân
    for th, shn in ((legs[0], legs[1]), (legs[2], legs[3])):
        k = _pt(hip, th, 68)
        f = _pt(k, shn, 70 if sitting else 66)
        parts.append(f'<polyline points="{hip[0]},{hip[1]} {k[0]:.1f},{k[1]:.1f} {f[0]:.1f},{f[1]:.1f}" {st}/>')
    # tay
    hands = []
    for up, lo in ((arms[0], arms[1]), (arms[2], arms[3])):
        e = _pt(sh, up, 72)
        h = _pt(e, lo, 68)
        hands.append(h)
        parts.append(f'<polyline points="{sh[0]},{sh[1]} {e[0]:.1f},{e[1]:.1f} {h[0]:.1f},{h[1]:.1f}" {st}/>')
    if pose == "thumbs":
        hx, hy = hands[1]
        parts.append(f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="11" {stroke(color, 7)}/>'
                     f'<line x1="{hx:.1f}" y1="{hy - 10:.1f}" x2="{hx:.1f}" y2="{hy - 32:.1f}" {stroke(color, 8)}/>')
    if pose in ("stop", "reassure", "dismiss", "step_back"):
        hx, hy = hands[1]
        for i, a in enumerate((-35, -12, 12, 35)):
            p = _pt((hx, hy), 180 + a + (0 if pose != "stop" else 20), 18)
            parts.append(f'<line x1="{hx:.1f}" y1="{hy:.1f}" x2="{p[0]:.1f}" y2="{p[1]:.1f}" {stroke(color, 5)}/>')
    # đầu
    hr = 48
    if ghost:
        parts.append(f'<circle cx="{head[0]}" cy="{head[1]}" r="{hr}" fill="{BG}" {st}/>')
    else:
        parts.append(f'<circle cx="{head[0]}" cy="{head[1]}" r="{hr}" fill="{BG}" {stroke(color, sw)}/>')
        parts.append(face(head[0], head[1], expr, look, color))
    g = (f'<g data-fig="{x:.1f},{y:.1f},{s:.3f}"><g transform="translate({x:.1f},{y:.1f}) rotate({tilt}) scale({s:.4f})" opacity="{op}">'
         + "".join(parts) + "</g></g>")

    def scr(p):
        a = math.radians(tilt)
        px, py = p[0] * s, p[1] * s
        return (x + px * math.cos(a) - py * math.sin(a), y + px * math.sin(a) + py * math.cos(a))

    anchors = {"head": scr(head), "hr": hr * s, "sh": scr(sh), "hip": scr(hip),
               "lhand": scr(hands[0]), "rhand": scr(hands[1]), "top": scr((head[0], head[1] - hr))}
    return g, anchors


SHOT = {"WIDE SHOT": 1.12, "MEDIUM SHOT": 1.5, "CLOSE-UP": 2.35}


def shot_fig(shot, x=960, pose="stand", expr="neutral", look=0, head_y=None, floor=905, **kw):
    """Đặt nhân vật theo cỡ cảnh. Close-up: căn đầu tại head_y (mặc định 420), thân tràn khỏi khung."""
    s = SHOT[shot]
    if shot == "CLOSE-UP":
        hy = head_y or 430
        local_head = 328 if pose not in ("type", "sit", "sit_away") else 268
        y = hy + local_head * s
    else:
        y = floor
    return figure(x, y, s, pose, expr, look, **kw)


# ----------------------------------------------------------------------------- icon (hộp -50..50)
def _c(color, w=7, extra=""):
    return stroke(color, w, extra)


def icon(name, color=INK, w=7, **kw):
    s = _c(color, w)
    f = color
    if name == "laptop":
        scr = kw.get("screen", "none")
        return (f'<rect x="-42" y="-38" width="84" height="54" rx="5" fill="{scr}" fill-opacity=".9" {s}/>'
                f'<path d="M-52,22 L52,22 L44,32 L-44,32 Z" {s}/>')
    if name == "envelope":
        return f'<rect x="-40" y="-27" width="80" height="54" rx="5" {s}/><path d="M-40,-25 L0,6 L40,-25" {s}/>'
    if name == "folder":
        fill = kw.get("fill", "none")
        star = kw.get("star", True)
        st = ('<path d="M0,-14 L5,-3 L17,-2 L8,6 L11,18 L0,11 L-11,18 L-8,6 L-17,-2 L-5,-3 Z" '
              f'fill="{BG if fill != "none" else color}"/>') if star else ""
        return (f'<path d="M-45,-30 L-12,-30 L-4,-20 L45,-20 L45,35 L-45,35 Z" fill="{fill}" {s}/>' + st)
    if name == "calendar":
        out = [f'<rect x="-44" y="-38" width="88" height="80" rx="7" {s}/>',
               f'<line x1="-44" y1="-18" x2="44" y2="-18" {s}/>',
               f'<line x1="-22" y1="-48" x2="-22" y2="-30" {s}/><line x1="22" y1="-48" x2="22" y2="-30" {s}/>']
        crossed = kw.get("crossed", 0)
        n = 0
        for r in range(3):
            for c in range(4):
                cx, cy = -30 + c * 20, -2 + r * 17
                if n < crossed:
                    out.append(f'<path d="M{cx - 5},{cy - 5} L{cx + 5},{cy + 5} M{cx + 5},{cy - 5} L{cx - 5},{cy + 5}" {_c(color, 3.5)}/>')
                else:
                    out.append(f'<circle cx="{cx}" cy="{cy}" r="3" fill="{color}"/>')
                n += 1
        return "".join(out)
    if name == "tag":
        return (f'<path d="M-45,-22 L22,-22 L45,0 L22,22 L-45,22 Z" {s}/><circle cx="18" cy="0" r="5" fill="{color}"/>'
                f'<line x1="-32" y1="-6" x2="2" y2="-6" {_c(color, 4)}/><line x1="-32" y1="7" x2="-6" y2="7" {_c(color, 4)}/>')
    if name == "shield":
        fill = kw.get("fill", "none")
        return f'<path d="M0,-48 L40,-34 L40,2 Q40,32 0,50 Q-40,32 -40,2 L-40,-34 Z" fill="{fill}" fill-opacity=".25" {s}/>'
    if name == "bubble":
        return (f'<path d="M-46,-32 Q-46,-40 -38,-40 L38,-40 Q46,-40 46,-32 L46,10 Q46,18 38,18 L-8,18 L-26,36 L-22,18 L-38,18 Q-46,18 -46,10 Z" {s}/>'
                f'<line x1="-30" y1="-20" x2="28" y2="-20" {_c(color, 4)}/><line x1="-30" y1="-3" x2="12" y2="-3" {_c(color, 4)}/>')
    if name == "thought":
        inner = kw.get("inner", True)
        return (f'<path d="M-30,10 Q-50,8 -46,-12 Q-48,-34 -24,-34 Q-16,-50 4,-44 Q22,-54 34,-36 Q52,-30 46,-10 Q52,10 30,12 Q16,24 0,14 Q-16,24 -30,10 Z" {s}/>'
                f'<circle cx="-30" cy="32" r="7" {_c(color, 5)}/><circle cx="-40" cy="48" r="4" {_c(color, 4)}/>'
                + (f'<path d="M-14,-14 Q-4,-26 10,-16 Q18,-4 6,2 Q-10,6 -14,-14 Z" fill="{color}" opacity=".85"/>' if inner else ""))
    if name == "door":
        return (f'<rect x="-34" y="-50" width="68" height="100" rx="3" {s}/>'
                f'<rect x="-24" y="-40" width="48" height="90" fill="{color}" opacity=".22"/>')
    if name == "clock":
        return (f'<circle cx="0" cy="0" r="38" {s}/><line x1="0" y1="0" x2="0" y2="-24" {s}/><line x1="0" y1="0" x2="-16" y2="8" {s}/>'
                f'<path d="M30,-38 A48,48 0 0 0 -30,-38" {_c(color, 5)}/><path d="M-30,-38 L-34,-24 M-30,-38 L-17,-42" {_c(color, 5)}/>')
    if name == "star":
        fill = kw.get("fill", "none")
        return f'<path d="M0,-46 L13,-14 L46,-12 L20,10 L29,44 L0,25 L-29,44 L-20,10 L-46,-12 L-13,-14 Z" fill="{fill}" fill-opacity=".35" {s}/>'
    if name == "trophy":
        return (f'<path d="M-28,-40 L28,-40 L24,-4 Q20,14 0,16 Q-20,14 -24,-4 Z" {s}/>'
                f'<path d="M-28,-30 Q-46,-30 -42,-12 Q-38,-2 -24,-4 M28,-30 Q46,-30 42,-12 Q38,-2 24,-4" {_c(color, 5)}/>'
                f'<line x1="0" y1="16" x2="0" y2="32" {s}/><rect x="-20" y="32" width="40" height="12" rx="3" {s}/>')
    if name == "brain":
        return (f'<path d="M0,-38 Q-20,-48 -34,-34 Q-50,-28 -44,-8 Q-52,10 -36,22 Q-30,40 -10,36 Q0,44 0,36 Q0,44 10,36 Q30,40 36,22 Q52,10 44,-8 Q50,-28 34,-34 Q20,-48 0,-38 Z" {s}/>'
                f'<line x1="0" y1="-38" x2="0" y2="36" {_c(color, 4)}/>'
                f'<path d="M-30,-14 Q-18,-20 -14,-6 M-34,10 Q-20,4 -16,18 M30,-14 Q18,-20 14,-6 M34,10 Q20,4 16,18" {_c(color, 4)}/>')
    if name == "puzzle":
        miss = kw.get("missing", (2, 0))
        out = []
        for r in range(3):
            for c in range(3):
                x0, y0 = -45 + c * 30, -45 + r * 30
                if (c, r) == miss:
                    gap_style = _c(kw.get("gap", color), 3, 'stroke-dasharray="5 5"')
                    out.append(f'<rect x="{x0 + 2}" y="{y0 + 2}" width="26" height="26" rx="3" {gap_style}/>')
                else:
                    out.append(f'<rect x="{x0 + 2}" y="{y0 + 2}" width="26" height="26" rx="3" {_c(color, 5)}/>')
        return "".join(out)
    if name == "boxes":
        return (f'<rect x="-46" y="0" width="44" height="40" rx="3" {s}/><rect x="4" y="0" width="44" height="40" rx="3" {s}/>'
                f'<rect x="-22" y="-42" width="44" height="40" rx="3" {s}/>'
                f'<rect x="30" y="-44" width="30" height="28" rx="3" transform="rotate(25 45 -30)" {s}/>')
    if name == "book":
        prog = kw.get("progress", 0.9)
        bar_c = kw.get("bar", color)
        return (f'<path d="M0,-30 Q-24,-42 -46,-32 L-46,24 Q-24,14 0,26 Q24,14 46,24 L46,-32 Q24,-42 0,-30 Z" {s}/>'
                f'<line x1="0" y1="-30" x2="0" y2="26" {_c(color, 4)}/>'
                f'<rect x="-44" y="38" width="88" height="10" rx="5" {_c(color, 3)}/>'
                f'<rect x="-44" y="38" width="{88 * prog:.0f}" height="10" rx="5" fill="{bar_c}"/>')
    if name == "document":
        return (f'<path d="M-30,-44 L16,-44 L32,-28 L32,44 L-30,44 Z" {s}/><path d="M16,-44 L16,-28 L32,-28" {_c(color, 5)}/>'
                + "".join(f'<line x1="-18" y1="{-18 + i * 14}" x2="{20 - (i % 2) * 14}" y2="{-18 + i * 14}" {_c(color, 4)}/>' for i in range(5)))
    if name == "magnifier":
        return f'<circle cx="-10" cy="-10" r="28" {s}/><line x1="10" y1="10" x2="40" y2="40" {_c(color, 11)}/>'
    if name == "hand":
        return (f'<path d="M-30,10 L-30,-6 Q-30,-14 -22,-14 L-22,-34 Q-22,-42 -14,-42 Q-6,-42 -6,-34 L-6,-40 Q-6,-48 2,-48 Q10,-48 10,-40 '
                f'L10,-34 Q10,-42 18,-42 Q26,-42 26,-34 L26,-20 Q26,-28 34,-28 Q42,-28 42,-20 L42,14 Q42,40 14,44 L-6,44 Q-26,40 -30,10 Z" {s}/>')
    if name == "bell":
        return (f'<path d="M-34,24 Q-26,14 -26,-6 Q-26,-38 0,-40 Q26,-38 26,-6 Q26,14 34,24 Z" {s}/>'
                f'<path d="M-8,32 Q0,42 8,32" {s}/><line x1="0" y1="-40" x2="0" y2="-48" {s}/>'
                f'<path d="M-44,-26 Q-50,-10 -44,4 M44,-26 Q50,-10 44,4" {_c(color, 4)}/>')
    if name == "mirror":
        return (f'<ellipse cx="0" cy="-6" rx="34" ry="46" {s}/><path d="M-14,-30 Q-20,-16 -16,-2" {_c(color, 4)}/>'
                f'<line x1="0" y1="40" x2="0" y2="52" {s}/><line x1="-18" y1="52" x2="18" y2="52" {s}/>')
    if name == "question":
        return (f'<path d="M-20,-22 Q-20,-46 2,-46 Q24,-46 24,-24 Q24,-8 6,-2 Q0,2 0,14" {_c(color, 10)}/>'
                f'<circle cx="0" cy="34" r="6" fill="{color}"/>')
    if name == "crumple":
        return (f'<path d="M-36,-30 L-14,-40 L4,-28 L26,-42 L40,-16 L30,4 L42,26 L18,40 L-2,30 L-26,42 L-40,18 L-30,-2 Z" {s}/>'
                f'<path d="M-14,-40 L-6,-6 L-30,-2 M-6,-6 L18,6 L30,4 M18,6 L-2,30" {_c(color, 3)}/>')
    if name == "cloud":
        return f'<path d="M-40,20 Q-56,18 -52,0 Q-50,-18 -30,-16 Q-24,-38 0,-36 Q22,-40 28,-18 Q50,-20 52,0 Q54,20 36,20 Z" {s}/>'
    if name == "raincloud":
        return (icon("cloud", color, w) + "".join(
            f'<line x1="{x}" y1="30" x2="{x - 6}" y2="46" {_c(color, 5)}/>' for x in (-26, -6, 14, 34)))
    if name == "horseshoe":
        return (f'<path d="M-30,40 L-34,0 Q-36,-40 0,-42 Q36,-40 34,0 L30,40" {_c(color, 13)}/>'
                f'<path d="M8,-50 L-4,-30 L8,-22 L-6,-2" {_c(BG, 9)}/>')
    if name == "xmark":
        return f'<path d="M-40,-40 L40,40 M40,-40 L-40,40" {_c(color, 8)}/>'
    if name == "scale":
        tilt = kw.get("tilt", 0)
        a = math.radians(tilt)
        lx, ly = -60 * math.cos(a), -60 * math.sin(a)
        rx, ry = 60 * math.cos(a), 60 * math.sin(a)
        out = [f'<line x1="0" y1="-40" x2="0" y2="48" {s}/><line x1="-22" y1="48" x2="22" y2="48" {s}/>',
               f'<line x1="{lx:.1f}" y1="{-40 + ly:.1f}" x2="{rx:.1f}" y2="{-40 + ry:.1f}" {s}/>',
               f'<circle cx="0" cy="-40" r="5" fill="{color}"/>']
        for px, py in ((lx, -40 + ly), (rx, -40 + ry)):
            out.append(f'<path d="M{px:.1f},{py:.1f} L{px - 20:.1f},{py + 26:.1f} M{px:.1f},{py:.1f} L{px + 20:.1f},{py + 26:.1f}" {_c(color, 3)}/>'
                       f'<path d="M{px - 26:.1f},{py + 26:.1f} Q{px:.1f},{py + 42:.1f} {px + 26:.1f},{py + 26:.1f} Z" {_c(color, 5)}/>')
        return "".join(out)
    if name == "gem":
        return (f'<path d="M-34,-14 L-18,-36 L18,-36 L34,-14 L0,40 Z" fill="{color}" fill-opacity=".3" {s}/>'
                f'<path d="M-34,-14 L34,-14 M-18,-36 L-8,-14 L0,40 L8,-14 L18,-36" {_c(color, 3.5)}/>'
                f'<path d="M40,-44 L44,-34 L54,-30 L44,-26 L40,-16 L36,-26 L26,-30 L36,-34 Z" fill="{color}"/>')
    if name == "notes":
        return (f'<rect x="-46" y="-30" width="40" height="50" rx="3" transform="rotate(-12 -26 -5)" {_c(color, 5)}/>'
                f'<rect x="0" y="-38" width="40" height="50" rx="3" transform="rotate(10 20 -13)" {_c(color, 5)}/>'
                f'<path d="M-36,-12 q6,-6 12,0 t12,0 M8,-22 q6,-6 12,0 t12,0 M-20,30 q8,-10 16,0 t16,0 t14,-4" {_c(color, 3.5)}/>')
    if name == "eye":
        return (f'<path d="M-50,0 Q0,-44 50,0 Q0,44 -50,0 Z" {s}/><circle cx="0" cy="0" r="15" fill="{color}"/>'
                f'<circle cx="5" cy="-5" r="4" fill="{BG}"/>')
    if name == "moon":
        return f'<path d="M10,-40 Q-30,-34 -30,0 Q-30,36 10,40 Q-12,22 -12,0 Q-12,-22 10,-40 Z" {s}/>'
    if name == "battery":
        lvl = kw.get("level", 14 / 58)  # mặc định giữ đúng hình cũ (vạch pin 14px)
        return (f'<rect x="-40" y="-20" width="74" height="40" rx="6" {s}/><rect x="36" y="-8" width="8" height="16" fill="{color}"/>'
                f'<rect x="-32" y="-12" width="{max(4, 58 * lvl):.0f}" height="24" fill="{kw.get("fill", color)}"/>')
    if name == "blank":
        return f'<rect x="-30" y="-40" width="60" height="80" rx="4" {s}/>'
    if name == "boulder":
        return (f'<path d="M-52,30 L-50,-4 L-36,-30 L-10,-46 L16,-42 L40,-30 L54,-4 L50,30 Z" fill="#26262A" {s}/>'
                f'<path d="M-36,-30 L-22,-8 L-30,14 M-22,-8 L4,-14 L16,-42 M4,-14 L18,8 L40,-2 M18,8 L10,30" {_c(color, 3.5)} opacity=".6"/>')
    if name == "pill":
        return f'<rect x="-40" y="-16" width="80" height="32" rx="16" {s}/>'
    if name == "humble":
        return (f'<circle cx="0" cy="-26" r="10" {_c(color, 5)}/><path d="M0,-16 Q-4,6 -18,18 M0,-4 L18,6" {_c(color, 5)}/>'
                f'<circle cx="0" cy="0" r="46" {_c(color, 5)}/><line x1="-32" y1="32" x2="32" y2="-32" {_c(color, 6)}/>')
    if name == "arrow":
        return f'<path d="M-44,0 L40,0 M22,-18 L42,0 L22,18" {s}/>'
    if name == "heart":
        return f'<path d="M0,40 Q-50,6 -40,-22 Q-30,-46 0,-26 Q30,-46 40,-22 Q50,6 0,40 Z" {s}/>'
    if name == "notebook":
        lit = kw.get("lit", 0)
        out = [f'<path d="M0,-34 Q-24,-42 -48,-34 L-48,36 Q-24,28 0,36 Q24,28 48,36 L48,-34 Q24,-42 0,-34 Z" {s}/>',
               f'<line x1="0" y1="-34" x2="0" y2="36" {_c(color, 4)}/>']
        for i in range(3):
            y = -16 + i * 16
            out.append(f'<line x1="8" y1="{y}" x2="40" y2="{y}" {_c(kw.get("ink", color), 4)} opacity="{1 if i < lit else .35}"/>')
            if i < lit:
                out.append(f'<circle cx="-34" cy="{y}" r="4" fill="{kw.get("ink", color)}"/>')
        return "".join(out)
    if name == "lamp":
        return (f'<path d="M-30,-10 L-10,-46 L22,-46 L38,-10 Z" {s}/><line x1="4" y1="-10" x2="4" y2="38" {s}/>'
                f'<line x1="-18" y1="40" x2="26" y2="40" {s}/>')
    if name == "building":
        return (f'<path d="M-48,-12 L0,-46 L48,-12 Z" {s}/><line x1="-46" y1="40" x2="46" y2="40" {s}/>'
                + "".join(f'<line x1="{x}" y1="-4" x2="{x}" y2="32" {_c(color, 6)}/>' for x in (-34, -12, 12, 34)))
    if name == "bulb":
        return (f'<path d="M-14,22 Q-14,8 -26,-6 Q-34,-20 -26,-34 Q-14,-50 0,-50 Q14,-50 26,-34 Q34,-20 26,-6 Q14,8 14,22 Z" {s}/>'
                f'<line x1="-12" y1="32" x2="12" y2="32" {s}/><line x1="-8" y1="42" x2="8" y2="42" {s}/>')
    if name == "books":
        return (f'<rect x="-44" y="16" width="88" height="22" rx="3" {s}/><rect x="-36" y="-8" width="76" height="22" rx="3" {s}/>'
                f'<rect x="-40" y="-32" width="70" height="22" rx="3" {s}/>')
    if name == "coin":
        return f'<circle cx="0" cy="0" r="40" {s}/><circle cx="0" cy="0" r="26" {_c(color, 4)}/><line x1="0" y1="-14" x2="0" y2="14" {_c(color, 6)}/>'
    if name == "coins":
        return "".join(f'<ellipse cx="0" cy="{30 - i * 16}" rx="38" ry="11" fill="{BG}" {s}/>' for i in range(5))
    if name == "guitar":
        return (f'<path d="M-20,46 Q-46,46 -44,22 Q-42,6 -26,4 Q-30,-12 -14,-16 Q2,-18 4,-2 Q22,-2 22,18 Q20,44 -20,46 Z" {s}/>'
                f'<circle cx="-14" cy="18" r="8" {_c(color, 4)}/><line x1="-6" y1="10" x2="40" y2="-40" {_c(color, 7)}/>'
                f'<rect x="34" y="-50" width="14" height="16" rx="3" transform="rotate(45 41 -42)" {_c(color, 5)}/>')
    if name == "note":
        return (f'<line x1="-6" y1="28" x2="-6" y2="-40" {s}/><path d="M-6,-40 Q14,-36 26,-20" {s}/>'
                f'<ellipse cx="-20" cy="30" rx="16" ry="12" fill="{color}"/>')
    if name == "wrench":
        return (f'<path d="M-36,36 L8,-8" {_c(color, 12)}/><path d="M4,-4 Q-4,-30 18,-42 Q30,-46 38,-40 L24,-26 L30,-14 L44,-28 Q48,-12 36,0 Q22,10 4,-4 Z" {s}/>')
    if name == "timer":
        prog = kw.get("progress", 1.0)
        a = 2 * math.pi * prog - math.pi / 2
        large = 1 if prog > 0.5 else 0
        arc = (f'<circle cx="0" cy="0" r="40" {_c(color, 10)}/>' if prog >= 0.999 else
               f'<path d="M0,-40 A40,40 0 {large} 1 {40 * math.cos(a):.1f},{40 * math.sin(a):.1f}" {_c(color, 10)}/>')
        return (f'<circle cx="0" cy="0" r="40" {_c(color, 3)} opacity=".35"/>' + arc
                + f'<line x1="0" y1="0" x2="0" y2="-22" {_c(color, 5)}/><line x1="-8" y1="-52" x2="8" y2="-52" {_c(color, 5)}/>')
    if name == "flame":
        return f'<path d="M0,44 Q-30,40 -28,12 Q-26,-8 -8,-22 Q-6,-6 4,-2 Q2,-28 16,-46 Q34,-18 30,10 Q28,40 0,44 Z" {s}/>'
    if name == "spark":
        return "".join(f'<line x1="{12 * math.cos(math.radians(a)):.1f}" y1="{12 * math.sin(math.radians(a)):.1f}" '
                       f'x2="{40 * math.cos(math.radians(a)):.1f}" y2="{40 * math.sin(math.radians(a)):.1f}" {_c(color, 6)}/>'
                       for a in range(0, 360, 45))
    if name == "gym":
        return (f'<path d="M-46,40 L-46,-14 L0,-42 L46,-14 L46,40 Z" {s}/>'
                f'<line x1="-22" y1="10" x2="22" y2="10" {_c(color, 6)}/><rect x="-30" y="-2" width="8" height="24" fill="{color}"/>'
                f'<rect x="22" y="-2" width="8" height="24" fill="{color}"/>')
    if name == "phone":
        return (f'<rect x="-24" y="-46" width="48" height="92" rx="9" {s}/><line x1="-8" y1="-36" x2="8" y2="-36" {_c(color, 4)}/>'
                f'<circle cx="0" cy="34" r="4" fill="{color}"/>')
    if name == "call":
        return (f'<path d="M-34,-38 Q-26,-46 -18,-38 L-8,-24 Q-4,-16 -12,-10 L-18,-6 Q-8,14 8,22 L14,16 Q20,10 28,14 L40,24 Q48,32 40,40 '
                f'Q30,50 14,44 Q-30,26 -42,-16 Q-44,-30 -34,-38 Z" {s}/>'
                f'<path d="M14,-36 Q36,-32 40,-10 M14,-20 Q24,-18 26,-8" {_c(color, 5)}/>')
    if name == "wallet":
        return (f'<rect x="-46" y="-28" width="92" height="64" rx="8" {s}/><path d="M-40,-28 L24,-44 L30,-28" {_c(color, 5)}/>'
                f'<rect x="16" y="-6" width="30" height="22" rx="5" {_c(color, 5)}/><circle cx="28" cy="5" r="4" fill="{color}"/>')
    if name == "jar":
        lvl = kw.get("level", 0.2)
        fill_c = kw.get("fill", color)
        h = 70 * lvl
        return (f'<rect x="-28" y="{40 - h:.1f}" width="56" height="{h:.1f}" rx="6" fill="{fill_c}" opacity=".55"/>'
                f'<path d="M-24,-34 L-24,-40 L24,-40 L24,-34 Q36,-30 36,-16 L36,34 Q36,46 24,46 L-24,46 Q-36,46 -36,34 L-36,-16 Q-36,-30 -24,-34 Z" {s}/>'
                f'<line x1="-26" y1="-34" x2="26" y2="-34" {_c(color, 5)}/>')
    if name == "medal":
        return (f'<path d="M-24,-48 L-6,-12 M24,-48 L6,-12" {_c(color, 8)}/><circle cx="0" cy="14" r="28" {s}/>'
                f'<path d="M0,0 L5,9 L15,10 L8,17 L10,27 L0,22 L-10,27 L-8,17 L-15,10 L-5,9 Z" fill="{color}"/>')
    if name == "briefcase":
        return (f'<rect x="-46" y="-22" width="92" height="62" rx="7" {s}/><path d="M-16,-22 L-16,-36 L16,-36 L16,-22" {s}/>'
                f'<line x1="-46" y1="4" x2="46" y2="4" {_c(color, 4)}/>')
    if name == "sun":
        out = [f'<path d="M-36,20 A36,36 0 0 1 36,20 Z" {s}/>', f'<line x1="-60" y1="20" x2="60" y2="20" {s}/>']
        for a in range(200, 345, 24):
            r = math.radians(a)
            out.append(f'<line x1="{46 * math.cos(r):.1f}" y1="{20 + 46 * math.sin(r):.1f}" x2="{60 * math.cos(r):.1f}" '
                       f'y2="{20 + 60 * math.sin(r):.1f}" {_c(color, 5)}/>')
        return "".join(out)
    if name == "arrow_up":
        return f'<path d="M0,44 L0,-40 M-24,-16 L0,-42 L24,-16" {_c(color, 10)}/>'
    if name == "pair":
        out = []
        for dx in (-22, 22):
            out.append(f'<circle cx="{dx}" cy="-26" r="13" {_c(color, 6)}/><line x1="{dx}" y1="-13" x2="{dx}" y2="20" {_c(color, 6)}/>'
                       f'<path d="M{dx - 12},44 L{dx},20 L{dx + 12},44" {_c(color, 6)}/>')
        out.append(f'<path d="M-22,0 Q0,-12 22,0" {_c(color, 6)}/>')
        return "".join(out)
    if name == "person":
        return (f'<circle cx="0" cy="-26" r="14" {_c(color, 6)}/><line x1="0" y1="-12" x2="0" y2="20" {_c(color, 6)}/>'
                f'<path d="M-16,4 L0,-4 L16,4 M-12,44 L0,20 L12,44" {_c(color, 6)}/>')
    if name == "dumbbell":
        return (f'<line x1="-30" y1="0" x2="30" y2="0" {_c(color, 8)}/><rect x="-44" y="-20" width="14" height="40" rx="3" fill="{color}"/>'
                f'<rect x="30" y="-20" width="14" height="40" rx="3" fill="{color}"/>')
    if name == "stream":
        return "".join(f'<path d="M-50,{y} Q-20,{y - 10} 10,{y} T50,{y}" {_c(color, 5)}/>' for y in (-18, 0, 18)) + \
            f'<path d="M34,-34 L52,0 L34,34" {_c(color, 6)}/>'
    if name == "bank":
        return (f'<path d="M-46,-14 L0,-44 L46,-14 Z" {s}/><rect x="-42" y="-10" width="84" height="44" {s}/>'
                f'<circle cx="0" cy="12" r="10" {_c(color, 5)}/>')
    if name == "page":
        return (f'<rect x="-34" y="-44" width="68" height="88" rx="5" {s}/><rect x="-34" y="-44" width="68" height="20" fill="{color}" opacity=".5"/>'
                + "".join(f'<circle cx="{-18 + c * 18}" cy="{-4 + r * 18}" r="3.5" fill="{color}"/>' for r in range(3) for c in range(3)))
    if name == "clover":
        out = []
        for a in (0, 90, 180, 270):
            out.append(f'<ellipse cx="0" cy="-20" rx="13" ry="20" transform="rotate({a})" {s}/>')
        return "".join(out) + f'<path d="M0,0 Q8,26 22,44" {_c(color, 6)}/>'
    if name == "shoe":
        return (f'<path d="M-46,24 L-46,-4 Q-44,-14 -34,-14 L-20,-14 L-14,-30 L6,-30 Q8,-8 30,0 Q48,6 48,18 L48,24 Z" {s}/>'
                f'<line x1="-46" y1="34" x2="48" y2="34" {_c(color, 7)}/><path d="M-10,-20 L4,-14 M-6,-26 L8,-20" {_c(color, 4)}/>')
    if name == "bedicon":
        return (f'<path d="M-48,30 L-48,-26 M-48,8 L48,8 L48,30 M-48,-6 L48,-6" {s}/>'
                f'<rect x="-40" y="-26" width="28" height="16" rx="6" {_c(color, 5)}/>')
    if name == "signpost":
        return (f'<line x1="0" y1="-44" x2="0" y2="46" {s}/><path d="M0,-34 L40,-34 L50,-24 L40,-14 L0,-14 Z" {s}/>'
                f'<path d="M0,-6 L-40,-6 L-50,4 L-40,14 L0,14 Z" {s}/>')
    if name == "org":
        return (f'<rect x="-14" y="-46" width="28" height="22" rx="4" {s}/><path d="M0,-24 L0,-8 M-34,-8 L34,-8 M-34,-8 L-34,8 M34,-8 L34,8 M0,-8 L0,8" {_c(color, 5)}/>'
                + "".join(f'<rect x="{x - 12}" y="8" width="24" height="20" rx="4" {_c(color, 5)}/>' for x in (-34, 0, 34)))
    if name == "apple":
        return (f'<path d="M0,-18 Q-18,-30 -32,-18 Q-46,-2 -36,22 Q-26,44 -8,40 Q0,36 8,40 Q26,44 36,22 Q46,-2 32,-18 Q18,-30 0,-18 Z" {s}/>'
                f'<path d="M0,-18 Q2,-34 10,-42" {_c(color, 5)}/>')
    if name == "target":
        return (f'<circle cx="0" cy="0" r="42" {s}/><circle cx="0" cy="0" r="26" {_c(color, 5)}/><circle cx="0" cy="0" r="9" fill="{color}"/>')
    if name == "check":
        return f'<path d="M-30,2 L-8,24 L32,-22" {_c(color, 10)}/>'
    if name == "hospital":
        return (f'<rect x="-44" y="-30" width="88" height="74" {s}/><rect x="-16" y="-50" width="32" height="20" {_c(color, 5)}/>'
                f'<path d="M0,-12 L0,16 M-14,2 L14,2" {_c(color, 8)}/><rect x="-10" y="26" width="20" height="18" {_c(color, 4)}/>')
    if name == "tray":
        return (f'<path d="M-50,10 L50,10 L42,26 L-42,26 Z" {s}/><ellipse cx="-16" cy="0" rx="18" ry="8" {_c(color, 5)}/>'
                f'<rect x="12" y="-24" width="16" height="30" rx="3" {_c(color, 5)}/>')
    if name == "drop":
        return f'<path d="M0,-46 Q30,-6 30,16 Q30,44 0,44 Q-30,44 -30,16 Q-30,-6 0,-46 Z" {s}/><path d="M-14,14 Q-14,28 -2,32" {_c(color, 4)}/>'
    if name == "soda":
        return (f'<path d="M-24,-40 L24,-40 L28,-30 L28,38 Q28,46 20,46 L-20,46 Q-28,46 -28,38 L-28,-30 Z" {s}/>'
                f'<line x1="-28" y1="-20" x2="28" y2="-20" {_c(color, 4)}/><line x1="-28" y1="28" x2="28" y2="28" {_c(color, 4)}/>'
                f'<path d="M-8,-4 Q8,-2 0,8 Q-8,16 8,16" {_c(color, 4)}/>')
    if name == "bars":
        vals = kw.get("vals", (.3, .5, .7, .9))
        out = [f'<line x1="-48" y1="44" x2="48" y2="44" {_c(color, 5)}/>']
        bw = 80 / len(vals)
        for i, v in enumerate(vals):
            h = 84 * v
            out.append(f'<g data-dot="{i}"><rect x="{-42 + i * bw:.1f}" y="{44 - h:.1f}" width="{bw * .7:.1f}" height="{h:.1f}" rx="3" fill="{color}"/></g>')
        return "".join(out)
    if name == "megaphone":
        return (f'<path d="M-40,-12 L-10,-12 L34,-38 L34,38 L-10,12 L-40,12 Z" {s}/><path d="M-30,12 L-22,40 L-8,40 L-12,12" {_c(color, 5)}/>')
    if name == "theater":
        out = [f'<rect x="-48" y="-46" width="96" height="46" rx="4" {s}/>']
        for r in range(2):
            for c in range(5):
                out.append(f'<path d="M{-40 + c * 20},{18 + r * 18} q6,-10 12,0" {_c(color, 4)}/>')
        return "".join(out)
    if name == "popcorn":
        return (f'<path d="M-30,-6 L30,-6 L22,46 L-22,46 Z" {s}/><path d="M-12,-6 L-8,46 M12,-6 L8,46" {_c(color, 4)}/>'
                + "".join(f'<circle cx="{x}" cy="{y}" r="10" {_c(color, 5)}/>' for x, y in ((-22, -14), (-6, -22), (10, -18), (24, -12), (2, -34), (-14, -32))))
    if name == "utensils":
        return (f'<path d="M-20,-46 L-20,-14 Q-20,-4 -12,-4 L-12,46 M-28,-46 L-28,-14 Q-28,-4 -20,-4 M-4,-46 L-4,-14 Q-4,-4 -12,-4" {_c(color, 5)}/>'
                f'<path d="M20,46 L20,-4 Q34,-14 30,-34 Q26,-48 20,-46 Q12,-30 14,-4" {_c(color, 5)}/>')
    if name == "wave":
        return "".join(f'<line x1="{x}" y1="{-h}" x2="{x}" y2="{h}" {_c(color, 7)}/>' for x, h in ((-40, 8), (-24, 22), (-8, 38), (8, 26), (24, 40), (40, 14)))
    if name == "campus":
        return (f'<rect x="-46" y="0" width="92" height="44" {s}/><rect x="-14" y="-40" width="28" height="40" {s}/>'
                f'<path d="M-14,-40 L0,-54 L14,-40" {s}/><circle cx="0" cy="-22" r="7" {_c(color, 4)}/>'
                + "".join(f'<rect x="{x}" y="14" width="12" height="16" {_c(color, 3)}/>' for x in (-38, -20, 8, 26)))
    if name == "cookie":
        return (f'<circle cx="0" cy="0" r="40" {s}/>' + "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="{color}"/>'
                                                         for x, y in ((-16, -14), (12, -20), (18, 8), (-6, 16), (-22, 8), (4, -2))))
    if name == "tshirt":
        return f'<path d="M-16,-40 Q0,-28 16,-40 L46,-24 L36,-2 L24,-8 L24,42 L-24,42 L-24,-8 L-36,-2 L-46,-24 Z" {s}/>'
    if name == "drawer":
        return (f'<rect x="-48" y="-34" width="96" height="68" rx="4" {s}/><line x1="-48" y1="0" x2="48" y2="0" {_c(color, 5)}/>'
                f'<line x1="-12" y1="-17" x2="12" y2="-17" {_c(color, 6)}/><line x1="-12" y1="17" x2="12" y2="17" {_c(color, 6)}/>')
    if name == "remote":
        return (f'<rect x="-16" y="-46" width="32" height="92" rx="8" {s}/><circle cx="0" cy="-30" r="5" fill="{color}"/>'
                + "".join(f'<circle cx="{x}" cy="{y}" r="3.5" fill="{color}"/>' for y in (-10, 4, 18) for x in (-7, 7)))
    if name == "warning":
        return (f'<path d="M0,-44 L46,38 L-46,38 Z" {s}/><line x1="0" y1="-12" x2="0" y2="14" {_c(color, 8)}/>'
                f'<circle cx="0" cy="26" r="4.5" fill="{color}"/>')
    if name == "discount":
        return (icon("tag", color, w)[:0] + f'<path d="M-45,-22 L22,-22 L45,0 L22,22 L-45,22 Z" {s}/>'
                f'<line x1="-26" y1="12" x2="2" y2="-12" {_c(color, 5)}/><circle cx="-24" cy="-8" r="5" {_c(color, 4)}/>'
                f'<circle cx="0" cy="8" r="5" {_c(color, 4)}/>')
    if name == "calcheck":
        return icon("calendar", color, w) + f'<path d="M-18,10 L-4,24 L22,-4" {_c(color, 9)}/>'
    if name == "hourglass":
        return (f'<path d="M-30,-46 L30,-46 M-30,46 L30,46 M-24,-46 Q-24,-12 0,0 Q-24,12 -24,46 M24,-46 Q24,-12 0,0 Q24,12 24,46" {s}/>'
                f'<path d="M-14,34 Q0,20 14,34 Z" fill="{color}"/><path d="M-12,-30 L12,-30 L0,-14 Z" fill="{color}" opacity=".7"/>')
    if name == "browser":
        tabs = kw.get("tabs", 4)
        out = [f'<rect x="-50" y="-30" width="100" height="72" rx="6" {s}/>', f'<line x1="-50" y1="-12" x2="50" y2="-12" {_c(color, 4)}/>']
        for i in range(tabs):
            out.append(f'<rect x="{-48 + i * 24}" y="-44" width="20" height="14" rx="3" {_c(color, 3)}/>')
        return "".join(out)
    if name == "task":
        return (f'<rect x="-36" y="-44" width="72" height="88" rx="8" {s}/>'
                f'<path d="M0,-20 L7,-6 L22,-4 L11,6 L14,21 L0,14 L-14,21 L-11,6 L-22,-4 L-7,-6 Z" fill="{color}"/>'
                f'<line x1="-20" y1="32" x2="20" y2="32" {_c(color, 4)}/>')
    if name == "muscle":
        return (f'<path d="M-44,30 L-44,6 Q-40,-6 -26,-6 L-10,-6 Q-14,-26 -4,-40 Q8,-48 14,-38 Q16,-30 8,-26 L8,-10 Q30,-20 42,0 Q48,22 30,32 Z" {s}/>')
    if name == "sofa":
        return (f'<path d="M-46,30 L-46,-4 Q-46,-12 -38,-12 L-30,-12 L-30,8 L30,8 L30,-12 L38,-12 Q46,-12 46,-4 L46,30 Z" {s}/>'
                f'<path d="M-30,-12 L-30,-30 Q-30,-38 -22,-38 L22,-38 Q30,-38 30,-30 L30,-12" {s}/>'
                f'<line x1="-40" y1="30" x2="-40" y2="40" {_c(color, 6)}/><line x1="40" y1="30" x2="40" y2="40" {_c(color, 6)}/>')
    if name == "scatter":
        import random as _r
        rr = _r.Random(4)
        pts = "".join(f'<circle cx="{-40 + i * 8}" cy="{30 - i * 5 + rr.uniform(-12, 12):.1f}" r="4.5" fill="{color}"/>' for i in range(11))
        return f'<path d="M-46,-46 L-46,42 L46,42" {_c(color, 5)}/>' + pts
    if name == "envelope2":
        return icon("envelope", color, w)
    if name == "valve":
        return (f'<circle cx="0" cy="0" r="40" {s}/><circle cx="0" cy="0" r="8" fill="{color}"/>'
                f'<line x1="0" y1="0" x2="0" y2="-30" {_c(color, 9)}/><path d="M-28,-44 A52,52 0 0 1 28,-44" {_c(color, 4)} opacity=".6"/>')
    if name == "thermo":
        lvl = kw.get("level", .5)
        h = 70 * lvl
        return (f'<path d="M-12,22 L-12,-40 Q-12,-50 0,-50 Q12,-50 12,-40 L12,22" {s}/><circle cx="0" cy="34" r="18" {s}/>'
                f'<circle cx="0" cy="34" r="10" fill="{color}"/><rect x="-4" y="{24 - h:.1f}" width="8" height="{h:.1f}" fill="{color}"/>'
                + "".join(f'<line x1="16" y1="{y}" x2="26" y2="{y}" {_c(color, 3)}/>' for y in (-36, -20, -4, 12)))
    if name == "gear":
        out = []
        for i in range(8):
            a = math.radians(i * 45)
            out.append(f'<rect x="-9" y="-50" width="18" height="18" rx="3" fill="{color}" transform="rotate({i * 45})"/>')
        return "".join(out) + f'<circle cx="0" cy="0" r="34" {s}/><circle cx="0" cy="0" r="12" {_c(color, 5)}/>'
    if name == "molecule":
        pts = ((0, 0), (-34, -22), (32, -26), (8, 38), (-30, 30))
        out = [f'<line x1="0" y1="0" x2="{x}" y2="{y}" {_c(color, 5)}/>' for x, y in pts[1:]]
        out += [f'<circle cx="{x}" cy="{y}" r="{14 if i == 0 else 10}" fill="{BG}" {_c(color, 5)}/>' for i, (x, y) in enumerate(pts)]
        return "".join(out)
    if name == "bolt":
        return f'<path d="M8,-48 L-26,6 L-2,6 L-10,48 L28,-10 L4,-10 Z" {s}/>'
    if name == "face":
        m = kw.get("mood", 0)
        return (f'<circle cx="0" cy="0" r="44" {s}/><circle cx="-15" cy="-10" r="5" fill="{color}"/><circle cx="15" cy="-10" r="5" fill="{color}"/>'
                f'<path d="M-18,18 Q0,{18 + 16 * m:.0f} 18,18" {_c(color, 5)}/>')
    if name == "journal":
        return (f'<rect x="-34" y="-46" width="68" height="92" rx="5" {s}/><line x1="-22" y1="-46" x2="-22" y2="46" {_c(color, 4)}/>'
                f'<path d="M8,-22 L8,2 M-4,-10 L20,-10" {_c(color, 7)}/><line x1="-8" y1="24" x2="24" y2="24" {_c(color, 4)}/>')
    if name == "nerves":
        out = [f'<circle cx="0" cy="-38" r="12" {_c(color, 5)}/><line x1="0" y1="-26" x2="0" y2="46" {_c(color, 6)}/>']
        for y in (-12, 6, 24, 40):
            out.append(f'<path d="M0,{y} Q-20,{y - 4} -38,{y + 6} M0,{y} Q20,{y - 4} 38,{y + 6}" {_c(color, 3.5)}/>')
            out.append(f'<circle cx="-38" cy="{y + 6}" r="4" fill="{color}"/><circle cx="38" cy="{y + 6}" r="4" fill="{color}"/>')
        return "".join(out)
    if name == "handshake":
        return (f'<path d="M-50,-6 L-26,-20 L-4,-12 L18,-22 L50,-6 M-50,-6 L-36,18 M50,-6 L36,18" {s}/>'
                f'<path d="M-30,14 L-16,26 M-20,6 L-4,20 M-8,-2 L8,12 M-36,18 Q-20,34 0,26 Q20,34 36,18" {_c(color, 5)}/>')
    if name == "tub":
        return (f'<path d="M-50,-4 L50,-4 L42,30 Q40,40 30,40 L-30,40 Q-40,40 -42,30 Z" {s}/><line x1="-36" y1="40" x2="-40" y2="48" {_c(color, 5)}/>'
                f'<line x1="36" y1="40" x2="40" y2="48" {_c(color, 5)}/>'
                + "".join(f'<rect x="{x}" y="{y}" width="16" height="16" rx="3" transform="rotate({r} {x + 8} {y + 8})" {_c(color, 4)}/>'
                          for x, y, r in ((-30, -24, 12), (-6, -28, -10), (18, -22, 20))))
    if name == "burst":
        pts = []
        for i in range(16):
            a = math.radians(i * 22.5)
            r = 48 if i % 2 == 0 else 24
            pts.append(f"{r * math.cos(a):.1f},{r * math.sin(a):.1f}")
        return f'<polygon points="{" ".join(pts)}" {s}/>'
    if name == "hashtag":
        return f'<path d="M-12,-40 L-20,40 M14,-40 L6,40 M-34,-14 L36,-14 M-38,14 L32,14" {_c(color, 8)}/>'
    raise KeyError(name)


def ico(name, x, y, size=100, color=INK, op=1.0, rot=0, w=7, **kw):
    return place(x, y, size, icon(name, color, w, **kw), op, rot)


def acc(name, x, y, size=100, op=1.0, rot=0, glow_r=None, w=7, **kw):
    """Vật nhấn màu playlist (duy nhất mỗi khung) kèm quầng sáng."""
    gr = glow_r if glow_r is not None else size * 1.15
    return (f'<g data-acc="{x:.1f},{y:.1f}">' + glow(x, y, gr, "A", op)
            + place(x, y, size, icon(name, ACC, w, **kw), op, rot) + "</g>")


def dim(name, x, y, size=100, op=0.35, rot=0, w=7, **kw):
    return place(x, y, size, icon(name, INK, w, **kw), op, rot)


def dots_arc(cx, cy, r, n=7, a0=200, a1=340, color=None, size=13, lit=None, op=1.0):
    color = color or ACC
    out = []
    for i in range(n):
        a = math.radians(a0 + (a1 - a0) * i / (n - 1))
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        on = lit is None or i < lit
        out.append(f'<g data-dot="{i}">' + glow(x, y, size * 3.2, "A", op if on else op * 0.3)
                   + f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{size}" fill="{color}" opacity="{op if on else op * 0.35}"/></g>')
    return "".join(out)


def crowd(xs, y, s=0.7, op=0.22, ghost=True, poses=None, exprs=None):
    out = []
    for i, x in enumerate(xs):
        p = poses[i % len(poses)] if poses else "stand"
        e = exprs[i % len(exprs)] if exprs else "neutral"
        out.append(figure(x, y, s, p, e, op=op, ghost=ghost)[0])
    return "".join(out)


def dust(x, y, wdt, hgt, n=26, seed=1, op=0.35):
    rnd = random.Random(seed)
    return "".join(f'<circle cx="{x + rnd.uniform(-wdt / 2, wdt / 2):.1f}" cy="{y + rnd.uniform(-hgt / 2, hgt / 2):.1f}" '
                   f'r="{rnd.uniform(1.5, 3.8):.1f}" fill="{INK}" opacity="{op * rnd.uniform(.4, 1):.2f}"/>' for _ in range(n))


def particles(x, y, wdt, hgt, n=40, seed=3, color=None, op=0.8):
    rnd = random.Random(seed)
    color = color or ACC
    return '<g data-drift="1">' + "".join(f'<circle cx="{x + rnd.uniform(-wdt / 2, wdt / 2):.1f}" cy="{y + rnd.uniform(-hgt / 2, hgt / 2):.1f}" '
                   f'r="{rnd.uniform(2, 6):.1f}" fill="{color}" opacity="{op * rnd.uniform(.25, 1):.2f}"/>' for _ in range(n)) + "</g>"


def crack(x0, y0, x1, y1, seed=2, color=None, w=6):
    rnd = random.Random(seed)
    color = color or ACC
    pts = [(x0, y0)]
    n = 7
    for i in range(1, n):
        t = i / n
        pts.append((x0 + (x1 - x0) * t + rnd.uniform(-22, 22), y0 + (y1 - y0) * t + rnd.uniform(-14, 14)))
    pts.append((x1, y1))
    d = " ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in pts)
    return (f'<polyline points="{d}" {stroke(color, w * 3)} opacity=".25"/>'
            f'<polyline points="{d}" {stroke(color, w)}/>')


def line(x0, y0, x1, y1, color=INK, w=5, op=1.0, dash=None):
    d = f'stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" {stroke(color, w, d)} opacity="{op}"/>'


def desk(x, y, wdt=420, op=1.0):
    return (f'<g opacity="{op}"><line x1="{x - wdt / 2}" y1="{y}" x2="{x + wdt / 2}" y2="{y}" {stroke(INK, 9)}/>'
            f'<line x1="{x - wdt / 2 + 30}" y1="{y}" x2="{x - wdt / 2 + 30}" y2="{y + 150}" {stroke(INK, 7)}/>'
            f'<line x1="{x + wdt / 2 - 30}" y1="{y}" x2="{x + wdt / 2 - 30}" y2="{y + 150}" {stroke(INK, 7)}/></g>')


def chair(x, y_floor, s=1.0, op=1.0):
    seat = y_floor - 70 * s
    return (f'<g opacity="{op}"><line x1="{x - 40 * s}" y1="{seat}" x2="{x + 45 * s}" y2="{seat}" {stroke(INK, 7)}/>'
            f'<line x1="{x - 40 * s}" y1="{seat}" x2="{x - 40 * s}" y2="{y_floor}" {stroke(INK, 6)}/>'
            f'<line x1="{x + 40 * s}" y1="{seat}" x2="{x + 40 * s}" y2="{y_floor}" {stroke(INK, 6)}/>'
            f'<line x1="{x - 40 * s}" y1="{seat}" x2="{x - 48 * s}" y2="{seat - 120 * s}" {stroke(INK, 6)}/></g>')


def rim(x, y, r=520, op=1.0):
    return glow(x, y, r, "warm", op)

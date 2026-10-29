"""F6 - five-sector taxonomy wheel (selected 2026-10-21; previous five-band version: prototypes/make_f6_bands_v2.py). Five equal, non-hierarchical sectors around one hub; human-readable labels only
(codes and leaf definitions: supplementary Table S8). Categories as in Section 5 (unchanged); interface categories are the five
consumer groups of D0-D8 (planner D1-D4, policy D5-D6, training D7, people D8, none D0). No counts.
Print scale: 516 x 334 pt canvas; lettering >= 7 pt.
2026-10-27: sector text made compact: each line is wrapped to the free width inside its sector at its own height (margin 5.5 pt
from ring and separators), '~' keeps phrases together, and the block position is searched per sector; ring radius 124 -> 140 pt."""
import os, sys, math, cairo
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(HERE))
from figlib import *
OUT = os.path.join(HERE, 'F6_taxonomy')
W, Ht = 516, 334
CX, CY, RO, RI = 258, 174, 140, 30
INK = (0.20, 0.20, 0.20); Q = (0.38, 0.38, 0.38)
SECT = [('Social representation', 'What is encoded about people?', 'sky',
         ['kinematic agent', 'predicted motion', 'social-space field', 'relational structure', 'linguistic / symbolic', 'implicit / latent']),
        ('FM role', 'What does the FM do?', 'green',
         ['scene~and~context interpretation', 'human-state~and relation~inference', 'social-norm~reasoning and~behaviour~selection', 'instruction~and preference~grounding', 'human-facing communication']),
        ('Social capability', 'Which property is targeted?', 'purple',
         ['safety', 'spatial-social conduct', 'human understanding', 'normative~and contextual~conduct', 'human experience']),
        ('Navigation interface', 'How does output reach action?', 'orange',
         ['planner-facing', 'policy-facing', 'training-facing', 'human-facing', 'not executed']),
        ('Evidence profile', 'How is it validated?', 'blue',
         ['offline evaluation', 'closed-loop simulation', 'physical robot', 'real people in robot trials', 'human evaluation', 'open-world~or long-duration~deployment'])]
_m = cairo.Context(cairo.RecordingSurface(cairo.CONTENT_COLOR_ALPHA, None))
def tw(s, size=7, bold=False, italic=False):
    _m.select_font_face(FONT, cairo.FONT_SLANT_ITALIC if italic else cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD if bold else cairo.FONT_WEIGHT_NORMAL)
    _m.set_font_size(eff(size)); return _m.text_extents(s).x_advance
def wrap(s, w, **k):
    out, ln = [], ''
    for x in s.split(' '):
        t = (ln + ' ' + x).strip()
        if tw(t, **k) <= w or not ln: ln = t
        else: out.append(ln); ln = x
    return out + [ln]
def tint(col, a): r, g, b = OK[col]; return (1 - a + a * r, 1 - a + a * g, 1 - a + a * b)
def draw(c):
    for i, (title, q, col, items) in enumerate(SECT):
        mid = math.radians(-90 + 72 * i); a0, a1 = mid - math.radians(36), mid + math.radians(36)
        c.save(); c.new_path(); c.arc(CX, CY, RO, a0, a1); c.arc_negative(CX, CY, RI, a1, a0); c.close_path(); c.set_source_rgb(*tint(col, 0.13)); c.fill(); c.restore()
        c.save(); c.new_path(); c.arc(CX, CY, RO, a0 + 0.012, a1 - 0.012); c.set_source_rgb(*OK[col]); c.set_line_width(2.2); c.stroke(); c.restore()
        # sector separators
        c.save(); c.new_path(); c.set_source_rgb(1, 1, 1); c.set_line_width(2.4); c.move_to(CX + RI * math.cos(a0), CY + RI * math.sin(a0)); c.line_to(CX + (RO + 2) * math.cos(a0), CY + (RO + 2) * math.sin(a0)); c.stroke(); c.restore()
        # items: each line is wrapped to the horizontal span that is free inside the sector at its height
        # (wedge between the separators and the annulus, minus a margin), so no text reaches a border
        LH, GAP, M = 7.7, (1.5 if i == 1 else 2.4), 5.5  # '~' joins words that must stay on one line
        def inside(xx, yy):
            r = math.hypot(xx - CX, yy - CY); ang = math.atan2(yy - CY, xx - CX)
            d = (ang - mid + math.pi) % (2 * math.pi) - math.pi
            if not (RI + M < r < RO - M) or abs(d) > math.radians(36): return False
            for a in (a0, a1):   # keep a margin M from both white separators
                if abs(-(xx - CX) * math.sin(a) + (yy - CY) * math.cos(a)) < M and (xx - CX) * math.cos(a) + (yy - CY) * math.sin(a) > 0: return False
            return True
        def free(y, x0):
            # free extent to the left and right of x0 for a text line with baseline y (glyph top and bottom checked)
            ext = []
            for sgn in (-1, 1):
                e = 0.0
                for k in range(1, 400):
                    xx = x0 + sgn * k * 0.5
                    if not (inside(xx, y - 5.6) and inside(xx, y + 1.6)): break
                    e = k * 0.5
                ext.append(e)
            return ext
        def place(y, x0, w):
            # centre the line on x0; shift sideways (at most 8 pt, only as far as needed) when one side is too tight
            if not (inside(x0, y - 5.6) and inside(x0, y + 1.6)): return False, x0, -w
            dl, dr = free(y, x0); half = w / 2
            if dl >= half and dr >= half: return True, x0, min(dl, dr) - half
            sh = (half - dl) if dl < half else -(half - dr)
            ok = abs(sh) <= 8 and dl + sh >= half - 1e-6 and dr - sh >= half - 1e-6
            return ok, x0 + sh, (min(dl + sh, dr - sh) - half) if ok else -abs(sh)
        def fits(y, x0, t): return place(y, x0, tw(t.replace('~', ' ')))[0]
        def layout(bx, ytop):
            y, lines = ytop, []
            for it in items:
                words, ln = it.split(' '), ''
                for w_ in words:
                    t = (ln + ' ' + w_).strip()
                    if not ln or fits(y, bx, t): ln = t
                    else: lines.append((y, ln)); y += LH; ln = w_
                lines.append((y, ln)); y += LH + GAP
            return lines, y - GAP - LH - ytop
        best = None
        for rc in [RI + 30 + 2 * k for k in range(0, 30)]:
            for dt in range(-30, 31, 3):
                bx = CX + rc * math.cos(mid); by = CY + rc * math.sin(mid) + dt
                ytop = by
                for _ in range(4):
                    lines, h = layout(bx, ytop); ytop = by - h / 2 + 2.5
                lines, h = layout(bx, ytop)
                slack = min(place(y, bx, tw(ln.replace('~', ' ')))[2] for y, ln in lines)
                score = (slack >= 0, min(slack, 3.0), -(abs(rc - (RI + RO) / 2 - 8) + abs(dt) + 4 * len(lines)))  # fit, clearance, then central placement (an extra line costs 4 pt)
                if best is None or score > best[0]: best = (score, bx, lines)
        _, bx, lines = best
        for y, ln in lines:
            ln = ln.replace('~', ' '); ok, cx, _ = place(y, bx, tw(ln)); assert ok, (title, ln)
            text(c, cx, y, ln, 7, False, 'center', INK)
        # title and question outside the ring
        ro = RO + 10; tx, ty = CX + ro * math.cos(mid), CY + ro * math.sin(mid); cs = math.cos(mid)
        al = 'center' if abs(cs) < 0.35 else ('left' if cs > 0 else 'right')
        if math.sin(mid) < -0.9: ty -= 12
        elif math.sin(mid) > 0.5: ty += 4
        text(c, tx, ty, title, 7.8, True, al, 'black'); text(c, tx, ty + 9.4, q, 7, False, al, Q, italic=True)
    c.save(); c.new_path(); c.arc(CX, CY, RI - 3, 0, 2 * math.pi); c.set_source_rgb(1, 1, 1); c.fill_preserve(); c.set_source_rgb(0.55, 0.55, 0.55); c.set_line_width(0.6); c.stroke(); c.restore()
    for k, ln in enumerate(['Foundation-', 'model-based', 'social', 'navigation']): text(c, CX, CY - 10.5 + k * 8.2, ln, 7.2, True, 'center', 'black')
render(draw, W, Ht, OUT)
print('F6 wheel done')

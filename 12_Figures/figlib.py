"""Minimal pycairo plotting helpers (no matplotlib available offline). Each figure is a draw(ctx) function rendered to
SVG, PDF (vector) and PNG (preview, 2x) with identical geometry. Colour-blind-safe palette (Okabe-Ito)."""
import cairo, csv, os, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
A = os.path.join(ROOT, '07_Literature_Analysis')
OK = {'orange': (0.902, 0.624, 0.0), 'sky': (0.337, 0.706, 0.914), 'green': (0.0, 0.620, 0.451), 'yellow': (0.941, 0.894, 0.259),
      'blue': (0.0, 0.447, 0.698), 'red': (0.835, 0.369, 0.0), 'purple': (0.800, 0.475, 0.655), 'grey': (0.6, 0.6, 0.6), 'black': (0, 0, 0),
      'light': (0.92, 0.92, 0.92), 'white': (1, 1, 1), 'dark': (0.25, 0.25, 0.25)}
FONT = 'Liberation Sans'   # Arial-metric sans serif (narrower than DejaVu Sans)
FS = 1.0   # global font multiplier
# Elsevier artwork guidance: finished lettering >= 7 pt. Every figure canvas is drawn at (or slightly below) its LaTeX
# inclusion width, so a 7.0-unit floor gives >= 7 pt printed text. 15_Manuscript/tools/figure_font_audit.py measures it.
MIN_PT = 7.0
def eff(size): return max(size * FS, MIN_PT)
def rd(n): return list(csv.DictReader(open(os.path.join(A, n))))
def render(draw, w, h, base):
    for ext, surf in [('svg', lambda: cairo.SVGSurface(base + '.svg', w, h)), ('pdf', lambda: cairo.PDFSurface(base + '.pdf', w, h))]:
        s = surf(); c = cairo.Context(s); bg(c, w, h); draw(c); s.finish()
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, int(w * 2), int(h * 2)); c = cairo.Context(s); c.scale(2, 2); bg(c, w, h); draw(c); s.write_to_png(base + '.png')
def bg(c, w, h): c.set_source_rgb(1, 1, 1); c.rectangle(0, 0, w, h); c.fill()
def text(c, x, y, s, size=9, bold=False, align='left', color='black', rotate=0, valign='baseline', italic=False):
    c.save(); c.select_font_face(FONT, cairo.FONT_SLANT_ITALIC if italic else cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD if bold else cairo.FONT_WEIGHT_NORMAL); c.set_font_size(eff(size))
    c.set_source_rgb(*OK.get(color, color) if isinstance(color, str) else color)
    e = c.text_extents(str(s)); c.translate(x, y)
    if rotate: c.rotate(rotate)
    dx = {'left': 0, 'center': -e.width / 2 - e.x_bearing, 'right': -e.width - e.x_bearing}[align]
    dy = {'baseline': 0, 'middle': eff(size) * 0.35, 'top': eff(size) * 0.8}[valign]
    c.move_to(dx, dy); c.show_text(str(s)); c.restore(); return e.width
def rect(c, x, y, w, h, fill, stroke=None, lw=0.5):
    c.rectangle(x, y, w, h); c.set_source_rgb(*(OK[fill] if isinstance(fill, str) else fill)); c.fill_preserve() if stroke else c.fill()
    if stroke: c.set_source_rgb(*(OK[stroke] if isinstance(stroke, str) else stroke)); c.set_line_width(lw); c.stroke()
def line(c, x1, y1, x2, y2, color='black', lw=0.6, dash=None):
    c.save(); c.set_source_rgb(*OK[color]); c.set_line_width(lw)
    if dash: c.set_dash(dash)
    c.move_to(x1, y1); c.line_to(x2, y2); c.stroke(); c.restore()
def legend(c, x, y, items, size=8, box=8, gap=12, horizontal=True):
    for lab, col in items:
        rect(c, x, y - box + 1, box, box, col, 'dark', 0.3); w = text(c, x + box + 3, y, lab, size)
        if horizontal: x += box + 3 + w + gap
        else: y += box + 6
def hatch(c, x, y, w, h, fill, step=2.2, lw=0.45, color=(1, 1, 1)):
    """Filled rectangle with diagonal hatching, so that categories stay distinguishable in greyscale print."""
    rect(c, x, y, w, h, fill)
    if w <= 0 or h <= 0: return
    c.save(); c.rectangle(x, y, w, h); c.clip(); c.set_source_rgb(*color); c.set_line_width(lw)
    k = -h
    while k < w:
        c.move_to(x + k, y + h); c.line_to(x + k + h, y); k += step
    c.stroke(); c.restore()
def pattern(c, x, y, w, h, fill, kind='solid', step=2.6, lw=0.5, color=(1, 1, 1)):
    """Filled rectangle with a print-safe overlay ('solid', 'diag', 'horiz', 'cross', 'dots') so that categories with similar
    luminance stay distinguishable in greyscale and for colour-vision deficiencies."""
    rect(c, x, y, w, h, fill)
    if kind == 'solid' or w <= 0 or h <= 0: return
    c.save(); c.rectangle(x, y, w, h); c.clip(); c.set_source_rgb(*color); c.set_line_width(lw)
    if kind in ('diag', 'cross'):
        k = -h
        while k < w: c.move_to(x + k, y + h); c.line_to(x + k + h, y); k += step
    if kind == 'cross':
        k = -h
        while k < w: c.move_to(x + k, y); c.line_to(x + k + h, y + h); k += step
    if kind == 'horiz':
        k = y + step / 2
        while k < y + h: c.move_to(x, k); c.line_to(x + w, k); k += step
    c.stroke()
    if kind == 'dots':
        yy = y + step / 2
        while yy < y + h:
            xx = x + step / 2
            while xx < x + w: c.arc(xx, yy, 0.55, 0, 6.2832); c.fill(); xx += step
            yy += step
    c.restore()
def lum(rgb):
    f = lambda v: v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (OK[rgb] if isinstance(rgb, str) else rgb); return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)
def contrast(a, b): la, lb = sorted((lum(a), lum(b)), reverse=True); return (la + 0.05) / (lb + 0.05)
def ink(fill): """Black or white text, whichever has the higher WCAG contrast ratio on this fill."""; return 'black' if contrast(fill, 'black') >= contrast(fill, 'white') else 'white'
# darker text variants of accent colours (WCAG contrast >= 4.5 on white); lines keep the Okabe-Ito colours
DRED, DPURPLE, DGREEN = (0.62, 0.24, 0.0), (0.50, 0.22, 0.42), (0.0, 0.42, 0.30)

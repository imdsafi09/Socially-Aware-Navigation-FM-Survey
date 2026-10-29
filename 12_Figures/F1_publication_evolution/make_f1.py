"""F1 - Publication evolution and representation shift. Data: master_literature_matrix.csv (final codes).
(a) works per year by analytical category (categories are mutually exclusive -> stacking is valid);
(b) direct papers per year by publication-status class (exclusive);
(Panel (c) of earlier versions moved to F10 (a).)"""
import os, sys, csv, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figlib import *
H = os.path.dirname(os.path.abspath(__file__))
M = rd('master_literature_matrix.csv')
CATS = [('S0', 'Surveys', (0.82, 0.82, 0.82)), ('S1+S2', 'Classical + learning', 'blue'), ('S3', 'Adjacent FM navigation', 'sky'), ('S4+S5', 'Direct FM social nav.', 'orange'), ('S6', 'Datasets / benchmarks', 'green')]
def cat(m): c = m['analytical_category']; return 'S1+S2' if c in ('S1', 'S2') else ('S4+S5' if c in ('S4', 'S5') else c)
YEARS = ['≤2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026']
def ybin(y): return '≤2016' if int(y) <= 2016 else y
cnt = collections.Counter((ybin(m['year']), cat(m)) for m in M)
STAT = [('A', 'Peer-reviewed', 'blue'), ('B', 'Accepted, not indexed', 'sky'), ('D', 'Acceptance verified', 'yellow'), ('C', 'Preprint', 'orange')]
D = [m for m in M if m['direct_fm_social'] == 'Yes']; dcnt = collections.Counter((m['year'], m['ext_status_class'][:1]) for m in D)
PCS = list(csv.DictReader(open(os.path.join(os.path.dirname(H), '..', '07_Literature_Analysis', 'prefm_comparison_set.csv'))))  # Stage 9 pre-FM comparison set
PRE = [{'final_A_social_representation': '; '.join(r['A'].split())} for r in PCS]
AX = [('A1', 'Kinematic agent'), ('A2', 'Predicted motion'), ('A3', 'Social-space field'), ('A4', 'Relational structure'), ('A5', 'Linguistic / symbolic'), ('A6', 'Implicit / latent')]
def share(G, a): return sum(1 for m in G if a in [x.strip() for x in m['final_A_social_representation'].split(';')]) / len(G)
with open(os.path.join(H, 'f1_source.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['panel', 'x', 'group', 'value'])
    for y in YEARS:
        for c, _, _ in CATS: w.writerow(['a', y, c, cnt[(y, c)]])
    for y in ['2024', '2025', '2026']:
        for s, _, _ in STAT: w.writerow(['b', y, s, dcnt[(y, s)]])
    for a, _ in AX: w.writerow(['c', a, 'Pre-FM comparison set (n=%d)' % len(PRE), round(share(PRE, a), 4)]); w.writerow(['c', a, 'Direct (n=%d)' % len(D), round(share(D, a), 4)])
# fill patterns keep categories distinguishable in greyscale and for colour-vision deficiencies
PATF = {'orange': ('diag', (1, 1, 1)), 'green': ('dots', (1, 1, 1)), 'yellow': ('horiz', (0.35, 0.35, 0.35))}
def seg(c, x, y, w, h, col):
    if col in PATF: k, pc = PATF[col]; pattern(c, x, y, w, h, OK[col], k, color=pc, step=2.4 if k != 'dots' else 2.2)
    else: rect(c, x, y, w, h, col, 'white', 0.3)
def legend2(c, x, y, items, size=7, box=7, gap=8):
    for lab, col in items:
        seg(c, x, y - box + 1, box, box, col); c.set_source_rgb(*OK['dark']); c.set_line_width(0.3); c.rectangle(x, y - box + 1, box, box); c.stroke()
        x += box + 3 + text(c, x + box + 3, y, lab, size) + gap
W, Ht = 516, 186   # print scale: canvas 516 pt (LaTeX \\textwidth 522 pt); all lettering >= 7 pt printed
def draw(c):
    # panel a
    x0, y0, pw, ph = 24, 26, 290, 120; mx = 35
    text(c, 2, 10, '(a) Works per year by analytical category (n = %d)' % len(M), 7, True)
    for t in range(0, mx + 1, 5):
        yy = y0 + ph - ph * t / mx; line(c, x0, yy, x0 + pw, yy, 'light', 0.4); text(c, x0 - 3, yy, t, 5.8, align='right', valign='middle')
    sl = pw / len(YEARS); bw = sl * 0.72
    for i, y in enumerate(YEARS):
        bx = x0 + sl * (i + 0.14); acc = 0
        for k, _, col in CATS:
            v = cnt[(y, k)]
            if v: hh = ph * v / mx; seg(c, bx, y0 + ph - ph * acc / mx - hh, bw, hh, col); acc += v
        text(c, bx + bw / 2, y0 + ph - ph * acc / mx - 2, acc, 5.6, align='center')
        text(c, bx + bw / 2, y0 + ph + 8, y, 5.6, align='center')
    line(c, x0, y0 + ph, x0 + pw, y0 + ph, lw=0.5); text(c, 7, y0 + ph / 2, 'Works', 6, rotate=-1.5708, align='center')
    legend2(c, x0, y0 + ph + 22, [(l, col) for _, l, col in CATS[:3]]); legend2(c, x0, y0 + ph + 33, [(l, col) for _, l, col in CATS[3:]])
    text(c, x0 + 4, y0 + 6, '2026: up to 19 Oct', 5.6, color='dark')
    # panel b
    x1, pw2, mx2 = 382, 100, 25
    text(c, 362, 10, '(b) Direct FM papers by status', 7, True)
    for t in range(0, mx2 + 1, 5):
        yy = y0 + ph - ph * t / mx2; line(c, x1, yy, x1 + pw2, yy, 'light', 0.4); text(c, x1 - 3, yy, t, 5.8, align='right', valign='middle')
    for i, y in enumerate(['2024', '2025', '2026']):
        bx = x1 + 8 + i * 30; acc = 0
        for s_, _, col in STAT:
            v = dcnt[(y, s_)]
            if v: hh = ph * v / mx2; seg(c, bx, y0 + ph - ph * acc / mx2 - hh, 16, hh, col); acc += v
        text(c, bx + 8, y0 + ph - ph * acc / mx2 - 2, acc, 5.6, align='center'); text(c, bx + 8, y0 + ph + 8, y, 5.6, align='center')
    line(c, x1, y0 + ph, x1 + pw2, y0 + ph, lw=0.5)
    legend2(c, 362, y0 + ph + 22, [(l, col) for _, l, col in STAT[:2]]); legend2(c, 362, y0 + ph + 33, [(l, col) for _, l, col in STAT[2:]])
render(draw, W, Ht, os.path.join(H, 'F1_publication_evolution'))
print('F1 done')

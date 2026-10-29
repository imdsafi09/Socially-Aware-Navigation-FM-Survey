"""F10 - Direct FM papers compared with the pre-FM comparison set. (a) human representation (Axis A, multi-label shares);
(b) social capabilities addressed and evaluated by direct papers, with the share of the pre-FM comparison set that evaluates each leaf.
Merges former F1(c) and F3 (main panel); CSR precedent: bar charts with direct value labels (e.g. CSR 61 (2026) 100960 Fig. 3).
Data: master/direct/capability matrices and prefm_comparison_set.csv (same sources as T6 and QF06/QF14/QF15). Print scale 516 pt (LaTeX \\textwidth 522 pt); all lettering >= 7 pt printed."""
import os, sys, csv
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figlib import *
H = os.path.dirname(os.path.abspath(__file__))
D = rd('direct_vlm_social_navigation_matrix.csv'); CAP = {r['id']: r for r in rd('social_capabilities_matrix.csv')}
M = {m['id']: m for m in rd('master_literature_matrix.csv')}
PCS = list(csv.DictReader(open(os.path.join(A, 'prefm_comparison_set.csv'))))
PRE_A = [set(r['A'].split()) for r in PCS]; PY = [set(r['cap_yes'].split()) for r in PCS]
DIR_A = [set(x.strip() for x in M[d['id']]['final_A_social_representation'].split(';')) for d in D]
AX = [('A1', 'Kinematic agent'), ('A2', 'Predicted motion'), ('A3', 'Social-space field'), ('A4', 'Relational structure'), ('A5', 'Linguistic / symbolic'), ('A6', 'Implicit / latent')]
FAM = [('SAF', 'Safety', [('SAF1', 'Collision avoidance'), ('SAF2', 'Near-collision or risk margin')]),
       ('SPA', 'Spatial-social conduct', [('SPA1', 'Personal space'), ('SPA2', 'Group and conversation space'), ('SPA3', 'Encounter conventions'), ('SPA4', 'Crowd navigation')]),
       ('HUM', 'Human understanding', [('HUM1', 'Motion understanding or prediction'), ('HUM2', 'Intention or activity inference')]),
       ('NOR', 'Normative / contextual', [('NOR1', 'Etiquette and politeness'), ('NOR2', 'Social-instruction following'), ('NOR3', 'Context-dependent conduct'), ('NOR4', 'Cultural or norm adaptation')]),
       ('EXP', 'Human experience', [('EXP1', 'Perceived safety and comfort'), ('EXP2', 'Legibility and predictability'), ('EXP3', 'Naturalness')])]
nD, nP = len(D), len(PCS)
def cnt(l, vals): return sum(1 for d in D if CAP[d['id']]['final_' + l] in vals)
ROWS = [(f, l, ln, cnt(l, ('Yes', 'Partial')), cnt(l, ('Yes',)), sum(1 for s in PY if l in s)) for f, _, ls in FAM for l, ln in ls]
with open(os.path.join(H, 'f10_source.csv'), 'w', newline='') as fo:
    w = csv.writer(fo); w.writerow(['panel', 'code', 'label', 'direct_n', 'direct_addressed', 'direct_evaluated_or_share', 'prefm_n', 'prefm_value'])
    for a, lab in AX: w.writerow(['a', a, lab, nD, '', sum(a in s for s in DIR_A), nP, sum(a in s for s in PRE_A)])
    for f, l, ln, yp, yes, pre in ROWS: w.writerow(['b', l, ln, nD, yp, yes, nP, pre])
LIGHT = (0.98, 0.84, 0.6)
DIR = (0.80, 0.47, 0.0)           # direct papers (dumbbell endpoints): orange family, as in panel (a)
PRE = OK['blue']                   # pre-FM comparison set: blue, as in panel (a)
W, Ht = 516, 280
def draw(c):
    # ---------- panel a
    text(c, 2, 9, '(a) Human representation (share of works)', 7.4, True)
    x0, y0, pw, rh = 92, 20, 70, 19
    for t in (0, 50, 100):
        xx = x0 + pw * t / 100; line(c, xx, y0 - 2, xx, y0 + rh * len(AX), 'light', 0.4); text(c, xx, y0 + rh * len(AX) + 8, f'{t}%', 7, align='center', color='dark')
    for i, (a, lab) in enumerate(AX):
        y = y0 + i * rh; text(c, x0 - 3, y + rh / 2, f'{a} {lab}', 7, align='right', valign='middle')
        for j, (G, n, col) in enumerate([(PRE_A, nP, 'blue'), (DIR_A, nD, 'orange')]):
            v = sum(a in s for s in G); ww = pw * v / n
            (hatch if col == 'orange' else rect)(c, x0, y + 2.5 + j * 7.5, ww, 6.5, col); text(c, x0 + ww + 2, y + 5.8 + j * 7.5, str(v), 7, valign='middle', color='dark')
    ly = y0 + rh * len(AX) + 22
    rect(c, 4, ly - 6, 7, 6.5, 'blue'); text(c, 14, ly, f'Pre-FM comparison set (n = {nP})', 7)
    hatch(c, 4, ly + 3, 7, 6.5, 'orange'); text(c, 14, ly + 9.4, f'Direct FM papers (n = {nD})', 7)
    for k, s_ in enumerate(['Labels: number of works. Multi-label, so', 'shares do not sum to 100%. In (b), direct', 'labels give evaluated / addressed papers;', 'pre-FM labels give evaluating works.']):
        text(c, 4, ly + 22 + k * 8.4, s_, 7, color='dark')
    # ---------- panel b
    bx = 206
    text(c, bx, 9, '(b) Capabilities: share of papers addressing vs evaluating', 7.4, True)
    x0, y0, pw = bx + 132, 24, 104
    for t in range(0, 101, 25):
        xx = x0 + pw * t / 100; line(c, xx, y0 - 2, xx, Ht - 32, 'light', 0.4); text(c, xx, Ht - 23, f'{t}%', 7, align='center', color='dark')
    y = y0; fam = None; zebra = 0
    GAPC = (0.98, 0.85, 0.62)                   # evaluation-gap band (light orange)
    def diamond(x_, y_, r_):
        c.save(); c.new_path(); c.move_to(x_, y_ - r_); c.line_to(x_ + r_, y_); c.line_to(x_, y_ + r_); c.line_to(x_ - r_, y_); c.close_path()
        c.set_source_rgb(*PRE); c.fill_preserve(); c.set_source_rgb(1, 1, 1); c.set_line_width(0.8); c.stroke(); c.restore()
    for f, l, ln, yp, yes, pre in ROWS:
        if f != fam:
            text(c, bx, y + 5, [x[1] for x in FAM if x[0] == f][0], 7.2, True, color='dark', valign='middle'); y += 10.5; fam = f
        if zebra % 2 == 0: rect(c, bx + 2, y - 0.6, x0 + pw + 66 - bx, 10.4, (0.962, 0.962, 0.962))   # row striping for reading across
        zebra += 1
        text(c, x0 - 8, y + 4.2, f'{l} {ln}', 7, align='right', valign='middle')
        ya = y + 4.2; xa = x0 + pw * yp / nD; xe = x0 + pw * yes / nD; xp = x0 + pw * pre / nP
        c.save(); c.new_path(); c.set_source_rgb(0.86, 0.86, 0.86); c.set_line_width(0.5); c.move_to(x0, ya); c.line_to(x0 + pw, ya); c.stroke(); c.restore()   # 0-100% track
        if xa > xe: rect(c, xe, ya - 2.6, xa - xe, 5.2, GAPC)                                       # evaluation gap (addressed but not evaluated)
        c.save(); c.new_path(); c.arc(xa, ya, 3.0, 0, 6.2832); c.set_source_rgb(1, 1, 1); c.fill_preserve(); c.set_source_rgb(*DIR); c.set_line_width(1.1); c.stroke(); c.restore()   # addressed
        c.save(); c.new_path(); c.arc(xe, ya, 3.0, 0, 6.2832); c.set_source_rgb(*DIR); c.fill(); c.restore()   # evaluated
        diamond(xp, ya, 3.4)                                                                               # pre-FM evaluated share (white outline keeps it visible on overlap)
        text(c, x0 + pw + 6, y + 4.2, f'{yes} / {yp}', 7, valign='middle', color='black'); text(c, x0 + pw + 46, y + 4.2, f'{pre}', 7, valign='middle', color=PRE)
        y += 11.2
    text(c, x0 + pw + 6, y0 - 7, 'direct', 7, True, color='dark'); text(c, x0 + pw + 46, y0 - 7, 'pre-FM', 7, True, color=PRE)
    ly = Ht - 10; x = bx
    c.save(); c.new_path(); c.arc(x + 3, ly - 2.5, 3.0, 0, 6.2832); c.set_source_rgb(*DIR); c.fill(); c.restore(); x += 9 + text(c, x + 9, ly, 'direct: evaluated', 7) + 9
    rect(c, x, ly - 5.1, 12, 5.2, GAPC); x += 15 + text(c, x + 15, ly, 'gap', 7) + 9
    c.save(); c.new_path(); c.arc(x + 3, ly - 2.5, 3.0, 0, 6.2832); c.set_source_rgb(1, 1, 1); c.fill_preserve(); c.set_source_rgb(*DIR); c.set_line_width(1.1); c.stroke(); c.restore(); x += 9 + text(c, x + 9, ly, 'direct: addressed', 7) + 9
    diamond(x + 3, ly - 2.5, 3.4); text(c, x + 9, ly, 'pre-FM: evaluated', 7)
render(draw, W, Ht, os.path.join(H, 'F10_fm_prefm_comparison'))
M = ['# Evidence map: F10 FM vs pre-FM comparison (generated by make_f10.py; do not edit)', '',
     f'Sources: `07_Literature_Analysis/direct_vlm_social_navigation_matrix.csv`, `social_capabilities_matrix.csv`, `master_literature_matrix.csv` (direct papers, n = {nD}); `prefm_comparison_set.csv` (pre-FM set, n = {nP}). Values are also written to `f10_source.csv`. No value is typed by hand.', '',
     '| Panel | Code | Variable | Numerator | Denominator |', '|---|---|---|---|---|']
for a_, lab in AX:
    M.append(f'| a | {a_} | direct papers with representation {a_} | {sum(a_ in s_ for s_ in DIR_A)} | {nD} |'); M.append(f'| a | {a_} | pre-FM works with representation {a_} | {sum(a_ in s_ for s_ in PRE_A)} | {nP} |')
for f_, l, ln, yp, yes, pre in ROWS:
    M.append(f'| b | {l} | direct papers addressing (Yes or Partial) | {yp} | {nD} |'); M.append(f'| b | {l} | direct papers evaluating (Yes) | {yes} | {nD} |'); M.append(f'| b | {l} | pre-FM works evaluating (`cap_yes`) | {pre} | {nP} |')
M += ['', 'Generation script: `12_Figures/F10_fm_prefm_comparison/make_f10.py`.']
open(os.path.join(H, 'EVIDENCE_MAP.md'), 'w').write('\n'.join(M) + '\n')
print('F10 done')

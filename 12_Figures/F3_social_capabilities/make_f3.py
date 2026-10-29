"""F3 - Social-capability coverage (Axis C, final 5-family / 15-leaf hierarchy).
Main figure: per leaf, share of direct papers that ADDRESS (Yes or Partial) vs EVALUATE (Yes = dedicated measure) the capability,
with the evaluated share in the pre-FM comparison set (Stage 9) as a marker. Supplementary: papers x leaves heatmap (Yes / Partial / No)."""
import os, sys, csv, re
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figlib import *
import figlib; figlib.MIN_PT = 0.0   # supplementary-only figure: dense per-paper matrix laid out for its own sizes; the 7-pt floor applies to main-text figures (09_Project_Reports/FINAL_FIGURE_SIZE_AUDIT.md)
H = os.path.dirname(os.path.abspath(__file__))
D = rd('direct_vlm_social_navigation_matrix.csv'); CAP = {r['id']: r for r in rd('social_capabilities_matrix.csv')}; M = rd('master_literature_matrix.csv')
PCS = list(csv.DictReader(open(os.path.join(os.path.dirname(H), '..', '07_Literature_Analysis', 'prefm_comparison_set.csv'))))  # Stage 9 pre-FM comparison set
PRE = [r['key'] for r in PCS]; PY = {r['key']: set(r['cap_yes'].split()) for r in PCS}
FAM = [('SAF', 'Safety', [('SAF1', 'Collision avoidance'), ('SAF2', 'Near-collision / risk margin')]),
       ('SPA', 'Spatial-social conduct', [('SPA1', 'Personal space'), ('SPA2', 'Group / conversation space'), ('SPA3', 'Encounter conventions'), ('SPA4', 'Crowd navigation')]),
       ('HUM', 'Human understanding', [('HUM1', 'Motion understanding / prediction'), ('HUM2', 'Intention / activity')]),
       ('NOR', 'Normative / contextual', [('NOR1', 'Etiquette / politeness'), ('NOR2', 'Explicit social-instruction following'), ('NOR3', 'Context-dependent conduct'), ('NOR4', 'Cultural / norm adaptation')]),
       ('EXP', 'Human experience', [('EXP1', 'Perceived safety / comfort'), ('EXP2', 'Legibility / predictability'), ('EXP3', 'Naturalness')])]
n = len(D)
def cnt(ids, l, vals): return sum(1 for i in ids if CAP.get(i, {}).get('final_' + l) in vals)
DIDS = [d['id'] for d in D]
rows = []
for f, fn, ls in FAM:
    for l, ln in ls: rows.append((f, l, ln, cnt(DIDS, l, ('Yes', 'Partial')), cnt(DIDS, l, ('Yes',)), sum(1 for k in PRE if l in PY[k])))
with open(os.path.join(H, 'f3_source.csv'), 'w', newline='') as fo:
    w = csv.writer(fo); w.writerow(['family', 'leaf', 'name', 'direct_addressed_YP', 'direct_evaluated_Yes', 'prefm_evaluated_Yes', 'n_direct', 'n_prefm'])
    for r in rows: w.writerow(list(r) + [n, len(PRE)])
W, Ht = 516, 18 + 15 * 11.5 + 5 * 9.5 + 26   # print scale: IEEE text width; fonts in printed points
def draw(c):
    x0, y0, pw = 160, 16, 210
    for t in range(0, 101, 20):
        xx = x0 + pw * t / 100; line(c, xx, y0 - 3, xx, Ht - 27, 'light', 0.4); text(c, xx, y0 - 6, f'{t}%', 5.6, align='center')
    y = y0; fam = None
    for f, l, ln, yp, yes, pre in rows:
        if f != fam:
            fn = [x[1] for x in FAM if x[0] == f][0]; text(c, 2, y + 5, f'{f}  {fn}', 6.2, True, color='dark', valign='middle'); y += 9.5; fam = f
        text(c, x0 - 4, y + 4.5, f'{l} {ln}', 5.8, align='right', valign='middle')
        rect(c, x0, y + 1, pw * yp / n, 7, (0.98, 0.84, 0.6)); rect(c, x0, y + 1, pw * yes / n, 7, 'orange')
        px = x0 + pw * pre / len(PRE); c.save(); c.set_source_rgb(*OK['blue']); c.arc(px, y + 4.5, 2.1, 0, 6.2832); c.fill(); c.restore()
        text(c, x0 + pw * max(yp / n, pre / len(PRE)) + 5, y + 4.5, f'{yes} evaluated / {yp} addressed of {n}' + (f'   pre-FM evaluated {pre}/{len(PRE)}' if pre else ''), 5.6, color='dark', valign='middle')
        y += 11.5
    ly = Ht - 15
    rect(c, x0, ly - 5, 6, 5.5, 'orange'); text(c, x0 + 9, ly - 0.5, 'Evaluated (Yes): dedicated measure', 5.8)
    rect(c, x0 + 128, ly - 5, 6, 5.5, (0.98, 0.84, 0.6)); text(c, x0 + 137, ly - 0.5, 'Addressed (Yes or Partial)', 5.8)
    c.save(); c.set_source_rgb(*OK['blue']); c.arc(x0 + 3, ly + 5.5, 2.1, 0, 6.2832); c.fill(); c.restore(); text(c, x0 + 9, ly + 7.5, f'Evaluated in pre-FM comparison set (share of {len(PRE)})', 5.8)
    text(c, 2, ly + 7.5, 'Leaf counts are non-exclusive.', 5.6, color='dark')
render(draw, W, Ht, os.path.join(H, 'F3_social_capabilities'))
# supplementary heatmap
LEAVES = [l for _, _, ls in FAM for l, _ in ls]
def okey(d):
    s = set(x.strip() for x in d['final_D_interface'].split(';')); rt = sorted(int(x[1]) for x in s if x in ('D1', 'D2', 'D3', 'D4', 'D5', 'D6'))
    return (rt[0] if rt else (7 if 'D0' in s else (8 if 'D7' in s else 9)), d['year'], d['id'])
DS = sorted(D, key=okey)
W2, H2 = 560, 90 + 11 * len(DS) + 40
def draw2(c):
    text(c, 10, 16, 'Supplementary: capability coding per direct paper (Yes = evaluated, Partial = addressed only)', 9, True)
    x0, y0, cw = 200, 70, 22
    for j, l in enumerate(LEAVES): text(c, x0 + j * cw + cw / 2 + 3, y0 - 6, l, 6.5, True, rotate=-1.2)
    for i, d in enumerate(DS):
        y = y0 + i * 11; text(c, x0 - 4, y + 8, re.sub(r'^\d{4}_[^_]+_', '', d['id']).replace('-', ' ')[:30], 6.3, align='right')
        for j, l in enumerate(LEAVES):
            v = CAP[d['id']]['final_' + l]; rect(c, x0 + j * cw + 1, y + 1, cw - 2, 9, 'orange' if v == 'Yes' else ((0.98, 0.84, 0.6) if v == 'Partial' else 'light'))
    ly = y0 + 11 * len(DS) + 20
    rect(c, x0, ly - 8, 10, 8, 'orange'); text(c, x0 + 13, ly, 'Yes', 7); rect(c, x0 + 45, ly - 8, 10, 8, (0.98, 0.84, 0.6)); text(c, x0 + 58, ly, 'Partial', 7)
    rect(c, x0 + 105, ly - 8, 10, 8, 'light'); text(c, x0 + 118, ly, 'No', 7); text(c, x0 + 150, ly, 'Rows ordered as in Table T4 (by interface).', 6.5, color='dark')
render(draw2, W2, H2, os.path.join(H, 'F3s_capability_heatmap_supplementary'))
print('F3 done')

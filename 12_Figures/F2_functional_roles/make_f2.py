"""F2 - Foundation-model functional roles (Axis B, final taxonomy) for the direct papers.
Left: paper x role matrix (multi-label; rows grouped by primary navigation interface, as in table T4); right: role totals (non-exclusive)."""
import os, sys, csv, re, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figlib import *
import figlib; figlib.MIN_PT = 0.0   # supplementary-only figure: dense per-paper matrix laid out for its own sizes; the 7-pt floor applies to main-text figures (09_Project_Reports/FINAL_FIGURE_SIZE_AUDIT.md)
H = os.path.dirname(os.path.abspath(__file__))
D = rd('direct_vlm_social_navigation_matrix.csv')
L = lambda v: [x.strip() for x in v.split(';') if x.strip()]
ROLES = [('R1', 'Scene / context\ninterpretation'), ('R2', 'Human-state /\nrelation inference'), ('R3', 'Social-norm reasoning /\nbehaviour selection'), ('R4', 'Instruction / preference\ngrounding'), ('R5', 'Human-facing\ncommunication')]
GN = {1: 'D1 semantic state', 2: 'D2 candidate selection', 3: 'D3 objective shaping', 4: 'D4 goal / waypoint', 5: 'D5 latent conditioning', 6: 'D6 direct action', 7: 'D0 non-executed', 8: 'D7 training-time only', 9: 'D8 human-facing only'}
def okey(d):
    s = set(L(d['final_D_interface'])); rt = sorted(int(x[1]) for x in s if x in ('D1', 'D2', 'D3', 'D4', 'D5', 'D6'))
    return (rt[0] if rt else (7 if 'D0' in s else (8 if 'D7' in s else 9)), d['year'], d['id'])
D = sorted(D, key=okey)
def name(i): return re.sub(r'^\d{4}_[^_]+_', '', i).replace('-', ' ')[:30]
cnt = collections.Counter(r for d in D for r in L(d['final_B_roles']))
with open(os.path.join(H, 'f2_source.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['paper_id', 'interface_group', 'interface'] + [r for r, _ in ROLES])
    for d in D: w.writerow([d['id'], GN[okey(d)[0]], d['final_D_interface']] + [int(r in L(d['final_B_roles'])) for r, _ in ROLES])
COL = {'R1': 'sky', 'R2': 'green', 'R3': 'orange', 'R4': 'blue', 'R5': 'purple'}
# print scale: canvas width = IEEE text width (516 pt); fonts in printed points
rh, cw, x0, y0 = 6.42, 26, 178, 14
NGAP = len(set(okey(d)[0] for d in D)) - 1
W, Ht = 516, y0 + rh * len(D) + 2.5 * NGAP + 6
def draw(c):
    for j, (r, lab) in enumerate(ROLES):
        text(c, x0 + j * cw + cw / 2, y0 - 4, r, 6.2, True, align='center')
    y = y0; g = None
    for d in D:
        gg = okey(d)[0]
        if gg != g:
            if g is not None: y += 2.5
            line(c, 2, y, x0 + 5 * cw, y, 'grey', 0.3); text(c, 2, y + rh * 0.55, GN[gg], 5.6, True, color='dark', valign='middle'); g = gg
        text(c, x0 - 3, y + rh * 0.55, name(d['id']) + f" ({d['year'][2:]})", 5.5, align='right', valign='middle')
        rs = L(d['final_B_roles'])
        for j, (r, _) in enumerate(ROLES):
            rect(c, x0 + j * cw + 0.7, y + 0.6, cw - 1.4, rh - 1.2, COL[r] if r in rs else 'light')
        y += rh
    bx = x0 + 5 * cw + 16
    text(c, bx, y0 + 4, f'Papers per role (non-exclusive, n = {len(D)})', 6.4, True)
    for j, (r, lab) in enumerate(ROLES):
        yy = y0 + 16 + j * 22
        text(c, bx, yy, r + '  ' + lab.replace('\n', ' '), 5.8, True)
        rect(c, bx, yy + 3, 110 * cnt[r] / len(D), 7, COL[r]); text(c, bx + 3 + 110 * cnt[r] / len(D), yy + 6.5, f'{cnt[r]}/{len(D)} ({100 * cnt[r] / len(D):.0f}%)', 5.6, valign='middle')
    rp = collections.Counter(len(L(d['final_B_roles'])) for d in D)
    yy = y0 + 16 + 5 * 22 + 4
    text(c, bx, yy, 'Roles per paper (number of papers):', 5.6)
    text(c, bx, yy + 7.5, '; '.join(f'{k} role{"s" if k > 1 else ""}: {v}' for k, v in sorted(rp.items())), 5.6)
    text(c, bx, yy + 18, 'Rows grouped by primary navigation interface', 5.5, color='dark')
    text(c, bx, yy + 25, '(Axis D; categorical, not a ranking).', 5.5, color='dark')
render(draw, W, Ht, os.path.join(H, 'F2_functional_roles'))
print('F2 done', dict(cnt))

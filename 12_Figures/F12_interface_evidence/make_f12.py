"""F12 - Navigation interfaces and evidence (replaces the interface table, Table 5 -> supplementary Table S9).
(a) For each interface D0-D8: number of direct papers (bar) and, within those papers, the share with systematic real-robot
evaluation, with an FM-independent safety guard and with cloud/hybrid/remote FM inference (shaded cells with percentages).
(b) Share of direct papers per publication year with systematic real-robot trials and with human evaluation of robot behaviour (grouped bars).
All values are computed here from 07_Literature_Analysis/direct_vlm_social_navigation_matrix.csv and asserted against the generated
findings (QF09, QF60, QF61); EVIDENCE_MAP.md is written by this script. Print scale: 516 pt canvas; lettering >= 7 pt."""
import os, sys, json, csv
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figlib import *
H = os.path.dirname(os.path.abspath(__file__))
D = rd('direct_vlm_social_navigation_matrix.csv'); QF = {q['id']: q for q in json.load(open(os.path.join(ROOT, '10_PreWriting', 'quantitative_findings.json')))}
L = lambda v: [x.strip() for x in str(v).split(';') if x.strip()]
CLOUD = ('cloud API', 'hybrid (local + cloud)', 'remote server')
IF = [('Planner-facing', [('D1', 'Semantic or social state'), ('D2', 'Candidate selection'), ('D3', 'Objective shaping'), ('D4', 'Goal or waypoints')]),
      ('Policy-facing', [('D5', 'Latent conditioning'), ('D6', 'Direct action')]), ('Training-facing', [('D7', 'Training-time supervision')]),
      ('Human-facing', [('D8', 'Human-facing channel')]), ('Not executed', [('D0', 'Non-executed decision')])]
ROWS = []
for grp, items in IF:
    for c, lab in items:
        g = [d for d in D if c in L(d['final_D_interface'])]
        n = len(g); sys_ = sum(d['final_EV3_physical_robot'] == 'systematic' for d in g)
        grd = sum(d['final_xc_safety_guard'] == 'Yes' for d in g); rem = sum(d['final_xc_inference_location'] in CLOUD for d in g)
        assert (n, sys_, grd, rem) == (QF[f'QF09_{c}']['numerator'], QF[f'QF60_{c}_sys']['numerator'], QF[f'QF60_{c}_guard']['numerator'], QF[f'QF60_{c}_remote']['numerator']), c
        ROWS.append((grp, c, lab, n, sys_, grd, rem))
YEARS = []
for y in ('2024', '2025', '2026'):
    g = [d for d in D if d['year'] == y]; s = sum(d['final_EV3_physical_robot'] == 'systematic' for d in g)
    h = sum(d['final_EV5_human_evaluation'] in ('co-present participants', 'observers/video') for d in g)
    assert (s, h, len(g)) == (QF[f'QF61_sys_{y}']['numerator'], QF[f'QF61_hum_{y}']['numerator'], QF[f'QF61_sys_{y}']['denominator']), y
    YEARS.append((y, len(g), s, h))
NB = (0.20, 0.36, 0.55)                       # bar / series colour (dark blue-grey)
W = 516; RH = 13.2
def shade(c, x, y, w, h, frac):
    g = 1 - 0.78 * frac; rect(c, x, y, w, h, (g, g + 0.03 * (1 - frac), g + 0.06 * (1 - frac) if frac < 1 else g))
    text(c, x + w / 2, y + h / 2 + 2.5, f'{round(100 * frac)}%', 7, False, 'center', 'white' if frac >= 0.55 else 'black')
def draw(c):
    # ---------------- panel (a)
    text(c, 2, 9, '(a) Interfaces and the evidence of the papers that use them', 7.4, True)
    x0 = 2; xb = 124; bw = 72; xr = 214; cw = 47; gap = 3; y0 = 40
    hdr = [('Papers', xb), ('Systematic', xr), ('FM-independent', xr + cw + gap), ('Remote / cloud', xr + 2 * (cw + gap))]
    text(c, xb, y0 - 8, 'Papers using the interface', 7, True, 'left', 'black')
    for k, (l1, l2) in enumerate((('Systematic', 'robot trials'), ('Independent', 'safety guard'), ('Remote', 'inference'))):
        cx = xr + k * (cw + gap) + cw / 2; text(c, cx, y0 - 16.6, l1, 7, True, 'center', 'black'); text(c, cx, y0 - 8, l2, 7, True, 'center', 'black')
    y = y0; last = None
    for grp, code, lab, n, s, g_, r in ROWS:
        if grp != last:
            text(c, x0, y + 8.5, grp, 7, True, 'left', (0.35, 0.35, 0.35)); y += RH; last = grp
        text(c, x0 + 6, y + 8.5, lab, 7, False, 'left', 'black'); text(c, xb - 4, y + 8.5, code, 7, False, 'right', (0.45, 0.45, 0.45))
        rect(c, xb, y + 2.2, bw * n / 12, RH - 4.4, NB); text(c, xb + bw * n / 12 + 3, y + 8.5, str(n), 7, False, 'left', 'black')
        for k, v in enumerate((s, g_, r)):
            shade(c, xr + k * (cw + gap), y + 0.8, cw, RH - 1.6, v / n if n else 0)
        y += RH
    global HA; HA = y
    text(c, x0, y + 10, f"Shares are within the papers using each interface; {QF['QF10d']['numerator']} papers use two interfaces" + (f" and {QF['QF10e']['numerator']} uses three." if QF['QF10e']['numerator'] == 1 else (f" and {QF['QF10e']['numerator']} use three." if QF['QF10e']['numerator'] else '.')), 7, False, 'left', (0.35, 0.35, 0.35))
    # ---------------- panel (b): grouped bars per year (no connecting lines: three years with very different n are not a time series)
    px = 392; pw = 120; py = y0 + 14; ph = 92
    text(c, px - 16, 9, '(b) Evidence by publication year', 7.4, True)
    HUMC = OK['orange']
    lx = px - 16                               # legend (two swatches) under the title
    rect(c, lx, 17.5, 7, 6.5, NB); w1 = text(c, lx + 10, 23.5, 'systematic robot trials', 7, False, 'left', 'black')
    pattern(c, lx, 27.5, 7, 6.5, HUMC, 'diag', step=2.0, lw=0.45, color=(1, 1, 1)); text(c, lx + 10, 33.5, 'human evaluation of behaviour', 7, False, 'left', 'black')
    for t in (0, 25, 50):
        yy = py + ph - ph * t / 55; line(c, px, yy, px + pw, yy, 'light', 0.4); text(c, px - 3, yy + 2.4, f'{t}%', 7, False, 'right', (0.35, 0.35, 0.35))
    gw = pw / 3; bw = 13
    for i, (yv, n, s, h) in enumerate(YEARS):
        gx = px + i * gw + gw / 2
        for k, (v, col) in enumerate(((s, NB), (h, HUMC))):
            frac = v / n; bh = ph * 100 * frac / 55; bx = gx - bw - 1 if k == 0 else gx + 1
            if k == 0: rect(c, bx, py + ph - bh, bw, bh, col)
            else: pattern(c, bx, py + ph - bh, bw, bh, col, 'diag', step=2.0, lw=0.45, color=(1, 1, 1))
            text(c, bx + bw / 2, py + ph - bh - 3, f'{round(100 * frac)}%', 7, False, 'center', 'black')
        line(c, px, py + ph, px + pw, py + ph, 'dark', 0.5)
        text(c, gx, py + ph + 10, yv, 7, False, 'center', 'black'); text(c, gx, py + ph + 19, f'n = {n}', 7, False, 'center', (0.35, 0.35, 0.35))
    global HB; HB = py + ph + 22
import cairo as _c
draw(_c.Context(_c.RecordingSurface(_c.CONTENT_COLOR_ALPHA, None)))
Ht = max(HA + 16, HB + 4)
render(draw, W, Ht, os.path.join(H, 'F12_interface_evidence'))
# ---------------- provenance (written by the script)
M = ['# Evidence map: F12 interfaces and evidence (generated by make_f12.py; do not edit)', '',
     f'Source matrix: `07_Literature_Analysis/direct_vlm_social_navigation_matrix.csv` ({len(D)} direct papers). Every value below is computed in the script and asserted equal to the generated findings (`10_PreWriting/quantitative_findings.json`). No value is typed by hand.', '',
     f"## Panel (a): interfaces (non-exclusive; {QF['QF10d']['numerator']} papers use two interfaces, {QF['QF10e']['numerator']} use three)", '',
     '| Interface | Variable | Numerator | Denominator | Plotted | Finding |', '|---|---|---|---|---|---|']
for grp, code, lab, n, s, g_, r in ROWS:
    M.append(f'| {code} {lab} | papers using the interface (`final_D_interface` contains {code}) | {n} | {len(D)} | bar length {n} | QF09_{code} |')
    for nm, v, col, q in (('systematic real-robot evaluation', s, '`final_EV3_physical_robot` = systematic', 'sys'), ('FM-independent safety guard', g_, '`final_xc_safety_guard` = Yes', 'guard'),
                          ('cloud / hybrid / remote inference', r, '`final_xc_inference_location` in {cloud API, hybrid, remote server}', 'remote')):
        M.append(f'| {code} | {nm} ({col}) | {v} | {n} | {round(100 * v / n) if n else 0}% | QF60_{code}_{q} |')
M += ['', '## Panel (b): evidence by publication year', '', '| Year | Variable | Numerator | Denominator | Plotted | Finding |', '|---|---|---|---|---|---|']
for yv, n, s, h in YEARS:
    M.append(f'| {yv} | systematic real-robot evaluation | {s} | {n} | {round(100 * s / n)}% | QF61_sys_{yv} |')
    M.append(f'| {yv} | human evaluation of robot behaviour (co-present or observers) | {h} | {n} | {round(100 * h / n)}% | QF61_hum_{yv} |')
M += ['', 'Generation script: `12_Figures/F12_interface_evidence/make_f12.py` (pycairo; deterministic).']
open(os.path.join(H, 'EVIDENCE_MAP.md'), 'w').write('\n'.join(M) + '\n')
# full numeric table for the supplement (Table S9), written next to the other generated tables
with open(os.path.join(ROOT, '11_Tables', 'TI_interface_evidence.csv'), 'w', newline='') as fo:
    w = csv.writer(fo); w.writerow(['Consumer', 'Interface', 'Label', 'Papers', 'Systematic robot evaluation', 'FM-independent safety guard', 'Cloud / hybrid / remote inference'])
    for grp, code, lab, n, s_, g_, r in ROWS: w.writerow([grp, code, lab, f'{n}/{len(D)}', f'{s_}/{n}', f'{g_}/{n}', f'{r}/{n}'])
    for yv, n, s_, h in YEARS: w.writerow([f'Year {yv}', '', 'all direct papers of the year', f'{n}/{len(D)}', f'{s_}/{n}', '', f'human evaluation of behaviour: {h}/{n}'])
print('F12 done')

"""F4 - Evidence profile (Axis E, final): direct papers x independent evidence dimensions EV1-EV6 (+ statistics),
rows grouped by primary navigation interface. Separates model-level reasoning evidence (EV1) from robot-level and
human-level social-navigation evidence (EV2-EV6). No ordinal score is computed."""
import os, sys, csv, re, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figlib import *
import figlib; figlib.MIN_PT = 0.0   # supplementary-only figure: dense per-paper matrix laid out for its own sizes; the 7-pt floor applies to main-text figures (09_Project_Reports/FINAL_FIGURE_SIZE_AUDIT.md)
H = os.path.dirname(os.path.abspath(__file__))
D = rd('direct_vlm_social_navigation_matrix.csv')
GN = {1: 'D1 semantic state', 2: 'D2 candidate selection', 3: 'D3 objective shaping', 4: 'D4 goal / waypoint', 5: 'D5 latent conditioning', 6: 'D6 direct action', 7: 'D0 non-executed', 8: 'D7 training-time only', 9: 'D8 human-facing only'}
def okey(d):
    s = set(x.strip() for x in d['final_D_interface'].split(';')); rt = sorted(int(x[1]) for x in s if x in ('D1', 'D2', 'D3', 'D4', 'D5', 'D6'))
    return (rt[0] if rt else (7 if 'D0' in s else (8 if 'D7' in s else 9)), d['year'], d['id'])
D = sorted(D, key=okey)
COLS = [('EV1', 'Offline\nevaluation', 'final_EV1_offline', {'Yes': 'sky'}),
        ('EV2', 'Closed-loop\nsimulation', 'final_EV2_closed_loop_sim', {'Yes': 'blue'}),
        ('EV3', 'Physical\nrobot', 'final_EV3_physical_robot', {'systematic': 'green', 'demo': (0.70, 0.88, 0.80)}),
        ('EV4', 'Real humans\nin trials', 'final_EV4_real_humans_in_trials', {'unscripted': 'red', 'staged': 'orange', 'present-type-unreported': (0.98, 0.84, 0.6), 'not-reported': (0.85, 0.85, 0.75)}),
        ('EV5', 'Human\nevaluation', 'final_EV5_human_evaluation', {'co-present participants': 'purple', 'observers/video': (0.90, 0.72, 0.82), 'text-raters': (0.85, 0.85, 0.85)}),
        ('EV6', 'Open-world\ndeployment', 'final_EV6_open_world_deployment', {'Yes': 'black'}),
        ('Stat', 'Statistical\ntesting', 'final_quality_statistical_testing', {'Yes': 'dark'})]
def val(d, k): v = d[k]; return 'Yes' if k == 'final_quality_statistical_testing' and str(v).startswith('Yes') else v
with open(os.path.join(H, 'f4_source.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['paper_id', 'interface_group'] + [c[0] for c in COLS])
    for d in D: w.writerow([d['id'], GN[okey(d)[0]]] + [val(d, c[2]) for c in COLS])
# print scale: canvas width = IEEE text width (516 pt); fonts in printed points
rh, cw, x0, y0 = 7, 47, 178, 40
NGAP = len(set(okey(d)[0] for d in D)) - 1
YT = y0 + rh * len(D) + 2.5 * NGAP          # bottom of matrix
W, Ht = 516, YT + 16 + 5 * 8.5 + 22
def draw(c):
    text(c, x0 + cw * 0.5, 6, 'model-level', 5.8, True, align='center', color='blue'); text(c, x0 + cw * 4, 6, 'robot- and human-level social-navigation evidence', 5.8, True, align='center', color='green')
    line(c, x0 + cw, 1, x0 + cw, YT + 10, 'grey', 0.5, [2, 1.5])
    for j, (k, lab, _, _) in enumerate(COLS):
        for q, part in enumerate(lab.split('\n')): text(c, x0 + j * cw + cw / 2, 15 + q * 6.5, part, 5.5, align='center')
        text(c, x0 + j * cw + cw / 2, 34, k, 6.2, True, align='center')
    y = y0; g = None
    for d in D:
        gg = okey(d)[0]
        if gg != g:
            if g is not None: y += 2.5
            line(c, 2, y, x0 + cw * len(COLS), y, 'grey', 0.3); text(c, 2, y + rh * 0.55, GN[gg], 5.6, True, color='dark', valign='middle'); g = gg
        text(c, x0 - 3, y + rh * 0.55, re.sub(r'^\d{4}_[^_]+_', '', d['id']).replace('-', ' ')[:30], 5.5, align='right', valign='middle')
        for j, (k, _, f, cmap) in enumerate(COLS):
            if val(d, f) == 'not-reported': hatch(c, x0 + j * cw + 0.7, y + 0.6, cw - 1.4, rh - 1.2, (0.85, 0.85, 0.75), color=(0.45, 0.45, 0.45))   # hatched: distinct in greyscale
            else: rect(c, x0 + j * cw + 0.7, y + 0.6, cw - 1.4, rh - 1.2, cmap.get(val(d, f), 'light'))
        y += rh
    yt = YT + 7; text(c, x0 - 3, yt, f'Totals (non-empty / {len(D)})', 5.6, True, align='right', valign='middle')
    for j, (k, _, f, cmap) in enumerate(COLS):
        nn = sum(1 for d in D if val(d, f) in cmap); text(c, x0 + j * cw + cw / 2, yt, nn, 6, True, align='center', valign='middle')
    items = [('EV1 offline evaluation: Yes', 'sky'), ('EV2 closed-loop simulation: Yes', 'blue'), ('EV3 systematic', 'green'), ('EV3 demonstration only', (0.70, 0.88, 0.80)), ('Statistical testing reported', 'dark'),
             ('EV4 unscripted public', 'red'), ('EV4 staged actors / participants', 'orange'), ('EV4 present, type unreported', (0.98, 0.84, 0.6)), ('EV4 not reported', (0.85, 0.85, 0.75)), ('Absent / none', 'light'),
             ('EV5 co-present participants', 'purple'), ('EV5 observers / video', (0.90, 0.72, 0.82)), ('EV5 text raters only', (0.85, 0.85, 0.85)), ('EV6 open-world (none in corpus)', 'black')]
    ly0 = YT + 18
    for i, (lab, col) in enumerate(items):
        lx = 4 + (i // 5) * 172; ly = ly0 + (i % 5) * 8.5
        (lambda: hatch(c, lx, ly - 5, 6, 5.5, col, color=(0.45, 0.45, 0.45)) if lab == 'EV4 not reported' else rect(c, lx, ly - 5, 6, 5.5, col, 'dark', 0.25))(); text(c, lx + 9, ly - 0.5, lab, 5.6)
    text(c, 4, Ht - 4, 'EV4 records real people during robot trials (simulated humans only, or none, shown as absent). Rows grouped by primary navigation interface.', 5.4, color='dark')
render(draw, W, Ht, os.path.join(H, 'F4_evidence_profile'))
print('F4 done')

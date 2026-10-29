"""F8 - Literature search and corpus construction (redesign 2026-10-26; previous one-column flow kept as make_f8_v1_superseded.py).
(a) Search-source map: a CONCEPTUAL wheel of the sources actually used, grouped by role; equal sectors, no counts.
(b) Unique candidates of the expansion search by FIRST-DISCOVERY route (one defined denominator, QF42), with the subset that met
    the criteria; the only quantitative chart. Raw records of the final coverage search are a different quantity and appear only
    as numbers in the flow.
(c) Screening flow from records to the final corpus, the final coverage search as a separate branch, and the pre-FM comparison set
    drawn apart because it was built by a different procedure.
Not a PRISMA diagram. Every number comes from 10_PreWriting/quantitative_findings.json or the screening record and is asserted.
Canvas 516 pt (= \\textwidth); all lettering >= 7 pt. Deterministic vector output; NO GENERATIVE IMAGE MODEL USED.
Usage: python3 make_f8.py [--proto]   (--proto also writes 12_Figures/prototypes/F_search_method_optionA.*)"""
import os, sys, json, csv, math, shutil
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figlib import *
H = os.path.dirname(os.path.abspath(__file__))
QF = {q['id']: q for q in json.load(open(os.path.join(ROOT, '10_PreWriting', 'quantitative_findings.json')))}
def n(k): return QF[k]['numerator']
SCR = list(csv.DictReader(open(os.path.join(ROOT, '07_Literature_Analysis', '_tools', 'stage2', 'screening_record.csv'))))
ROUTES = [('arXiv, pass 1', 'P1'), ('arXiv, pass 2', 'P2'), ('arXiv, pass 3', 'P3'), ('web search', 'web'), ('backward citations', 'citation'), ('final cut-off check', 'final check')]
FIRST = [(lab, sum(r['source'] == k for r in SCR), sum(r['source'] == k and r['decision'] == 'INCLUDE' for r in SCR)) for lab, k in ROUTES]
# consistency with the generated findings
assert sum(v for _, v, _ in FIRST) == n('QF42') == len(SCR)
assert sum(v for _, v, _ in FIRST[:3]) == n('QF59_arxiv_unique') and FIRST[3][1] == n('QF59_web') and FIRST[4][1] == n('QF59_citation') and FIRST[5][1] == n('QF59_finalcheck')
assert sum(i for _, _, i in FIRST) == n('QF59_ft_include')
assert n('QF58_tiab_excluded') + n('QF59_ft_assessed') == n('QF42')
assert sum(n(k) for k in ('QF59_ft_excluded', 'QF59_ft_background', 'QF59_ft_withdrawn', 'QF59_ft_related', 'QF59_ft_include')) == n('QF59_ft_assessed')
assert n('QF59_include_new') == n('QF43') and n('QF57_seed') + n('QF43') + n('QF43_final') == n('QF01')
assert n('QF62_ieee_records') + n('QF62_oa_records') + n('QF62_fw_records') + n('QF62_gs_records') == n('QF62_records')
assert n('QF62_records') - n('QF62_dups') == n('QF62_unique') == n('QF62_known') + n('QF62_new')
assert n('QF62_new') == n('QF62_excluded') + n('QF62_unresolved') + n('QF62_added') and n('QF62_added') == n('QF43_final')
W = 516; P = 8.4
INK = (0.15, 0.15, 0.16); DIM = (0.33, 0.33, 0.35)
MAIN, SIDE, FINAL = (0.905, 0.930, 0.968), (0.965, 0.965, 0.965), (0.975, 0.962, 0.925)
DISC, VERI, NAVY = (0.835, 0.875, 0.925), (0.900, 0.880, 0.835), (0.20, 0.36, 0.55)

def box(c, x, y, w, rows, fill=MAIN, stroke=(0.35, 0.35, 0.37), dash=None, minh=0, lw=None):
    h = max(4 + P * len(rows), minh)
    c.save(); c.rectangle(x, y, w, h); c.set_source_rgb(*fill); c.fill_preserve(); c.set_source_rgb(*stroke); c.set_line_width(lw if lw else (0.9 if fill in (MAIN, FINAL) else 0.45))
    if dash: c.set_dash(dash)
    c.stroke(); c.restore()
    for i, (s, b) in enumerate(rows): text(c, x + 4, y + 8.6 + i * P, s, 7.2 if b else 7, b, 'left', INK if b else DIM)
    return y + h
def arrow(c, pts, col=(0.30, 0.30, 0.32)):
    c.save(); c.set_source_rgb(*col); c.set_line_width(0.6); c.move_to(*pts[0])
    for p in pts[1:]: c.line_to(*p)
    c.stroke(); (x1, y1), (x2, y2) = pts[-2], pts[-1]
    if abs(x1 - x2) < 1e-6: d = 1 if y2 > y1 else -1; c.move_to(x2, y2); c.line_to(x2 - 2.2, y2 - d * 3.4); c.line_to(x2 + 2.2, y2 - d * 3.4)
    else: d = 1 if x2 > x1 else -1; c.move_to(x2, y2); c.line_to(x2 - d * 3.4, y2 - 2.2); c.line_to(x2 - d * 3.4, y2 + 2.2)
    c.close_path(); c.fill(); c.restore()
def title(c, x, y, s): text(c, x, y, s, 7.6, True, 'left', 'black')

# ------------------------------------------------------------------ (a) conceptual source map
SECT = [('Preprints', ['arXiv API:', '3 passes, final', 'cut-off check'], DISC),
        ('Databases', ['IEEE Xplore,', 'OpenAlex,', 'Crossref'], DISC),
        ('Web', ['general-purpose', 'search engine'], DISC),
        ('Citations', ['backward and', 'forward', 'chasing'], DISC),
        ('Verification', ['Crossref DOI,', 'publisher pages,', 'arXiv records'], VERI)]
def wheel(c, cx, cy, RO, RI):
    k = len(SECT); gap = 0.035
    for i, (t, lines, col) in enumerate(SECT):
        a0 = -math.pi / 2 + i * 2 * math.pi / k + gap / 2; a1 = a0 + 2 * math.pi / k - gap
        c.save(); c.new_path(); c.arc(cx, cy, RO, a0, a1); c.arc_negative(cx, cy, RI, a1, a0); c.close_path(); c.set_source_rgb(*col); c.fill_preserve()
        c.set_source_rgb(0.45, 0.45, 0.47); c.set_line_width(0.5)
        if col == VERI: c.set_dash([2.0, 1.4])
        c.stroke(); c.restore()
        am = (a0 + a1) / 2; rm = (RO + RI) / 2 + 2; tx, ty = cx + rm * math.cos(am), cy + rm * math.sin(am)
        rows = [(t, True)] + [(s, False) for s in lines]; y0 = ty - (len(rows) - 1) * 7.9 / 2 + 2.4
        for j, (s, b) in enumerate(rows): text(c, tx, y0 + j * 7.9, s, 7, b, 'center', INK if b else DIM)
    c.save(); c.new_path(); c.arc(cx, cy, RI - 2, 0, 2 * math.pi); c.set_source_rgb(1, 1, 1); c.fill_preserve(); c.set_source_rgb(0.45, 0.45, 0.47); c.set_line_width(0.5); c.stroke(); c.restore()
    for j, s in enumerate(('Literature', 'search and', 'verification')): text(c, cx, cy - 6.0 + j * 8.0, s, 7, True, 'center', INK)

def draw(c):
    # ---------------- (a)
    title(c, 2, 9, '(a) Sources used, by role')
    cx, cy, RO, RI = 90, 96, 78, 28
    wheel(c, cx, cy, RO, RI)
    ly = cy + RO + 12
    rect(c, 4, ly - 6, 9, 6, DISC, (0.45, 0.45, 0.47), 0.5); text(c, 16, ly, 'discovery', 7, False, 'left', INK)
    c.save(); c.rectangle(64, ly - 6, 9, 6); c.set_source_rgb(*VERI); c.fill_preserve(); c.set_source_rgb(0.45, 0.45, 0.47); c.set_line_width(0.5); c.set_dash([2.0, 1.4]); c.stroke(); c.restore()
    text(c, 76, ly, 'verification only', 7, False, 'left', INK)
    NOTE = ('Equal sectors; sector size encodes no count.', f"Google Scholar: limited manual check ({n('QF62_gs_records')} records);", 'not searched systematically. Not searched: ACM',
            'Digital Library (automated-access checks),', 'Scopus, Web of Science (not available).')
    for j, s in enumerate(NOTE):
        text(c, 4, ly + 10 + j * P, s, 7, False, 'left', DIM)
    yb = ly + 10 + len(NOTE) * P + 12
    # ---------------- (b) first-discovery bars
    title(c, 2, yb, f"(b) First discovery of the {n('QF42')} candidates")
    text(c, 2, yb + 9, 'unique candidates of the expansion search', 7, False, 'left', DIM)
    bx = 76; bw = 72; vmax = max(v for _, v, _ in FIRST); y = yb + 16
    for lab, v, inc in FIRST:
        text(c, bx - 4, y + 6.4, lab, 7, False, 'right', INK)
        L = bw * v / vmax; rect(c, bx, y + 1, max(L, 0.8), 7, (0.78, 0.83, 0.90))
        if inc: rect(c, bx, y + 1, max(bw * inc / vmax, 0.8), 7, NAVY)
        text(c, bx + max(L, 0.8) + 3, y + 6.6, f'{v}' + (f' ({inc})' if inc else ''), 7, False, 'left', INK)
        y += 10
    rect(c, 4, y + 3, 9, 6, NAVY); text(c, 16, y + 9, '(n) met the criteria', 7, False, 'left', INK)
    rect(c, 88, y + 3, 9, 6, (0.78, 0.83, 0.90)); text(c, 100, y + 9, 'screened', 7, False, 'left', INK)
    yl = y + 12
    # ---------------- (c) screening flow
    X0 = 186; title(c, X0, 9, '(c) Screening and corpus construction')
    L, LW, R, RW = X0, 158, X0 + 172, W - 2 - (X0 + 172)
    y1 = 16
    ID = [('Expansion search (stage 2)', True), (f"arXiv records, 3 passes: {n('QF59_arxiv_records')}", False), (f"web search: {n('QF59_web')}; backward citations: {n('QF59_citation')}", False),
          (f"final cut-off check: {n('QF59_finalcheck')}", False)]
    b1 = box(c, L, y1, LW, ID)
    RM = [('Repeated discoveries merged', True), (f"same work in several passes: {n('QF59_arxiv_dups')}", False)]
    ym = y1 + (b1 - y1 - (4 + P * 2)) / 2; box(c, R, ym, RW, RM, SIDE); arrow(c, [(L + LW, ym + (4 + P * 2) / 2), (R, ym + (4 + P * 2) / 2)])
    y2 = b1 + 11
    SC = [(f"Unique candidates screened: {n('QF42')}", True), ('title and abstract, criteria A–C', False)]
    b2 = box(c, L, y2, LW, SC); arrow(c, [(L + LW / 2, b1), (L + LW / 2, y2)])
    EX = [(f"Excluded at title/abstract: {n('QF58_tiab_excluded')}", True)]
    ye = y2 + (b2 - y2 - (4 + P)) / 2; box(c, R, ye, RW, EX, SIDE); arrow(c, [(L + LW, ye + (4 + P) / 2), (R, ye + (4 + P) / 2)])
    y3 = b2 + 11
    FT = [(f"Full texts assessed: {n('QF59_ft_assessed')}", True)]
    b3 = box(c, L, y3, LW, FT); arrow(c, [(L + LW / 2, b2), (L + LW / 2, y3)])
    NI = [(f"Not included: {n('QF59_ft_assessed') - n('QF59_ft_include')}", True), (f"excluded {n('QF59_ft_excluded')}; background only {n('QF59_ft_background')};", False),
          (f"withdrawn {n('QF59_ft_withdrawn')}; other version {n('QF59_ft_related')}", False)]
    yn = y3 - 4; bn = box(c, R, yn, RW, NI, SIDE); arrow(c, [(L + LW, (y3 + b3) / 2), (R, (y3 + b3) / 2)])
    y4 = max(b3, bn) + 9
    MC = [(f"Met the criteria: {n('QF59_ft_include')}", True), (f"already in seed set {n('QF59_include_inseed')}; new {n('QF59_include_new')}", False)]
    b4 = box(c, L, y4, LW, MC); arrow(c, [(L + LW / 2, b3), (L + LW / 2, y4)])
    # final coverage search (separate branch)
    yf = b4 + 10
    FS = [('Final coverage search (26 Oct 2026)', True), (f"IEEE Xplore {n('QF62_ieee_records')}, OpenAlex {n('QF62_oa_records')},", False),
          (f"forward citations {n('QF62_fw_records')} records;", False), (f"Google Scholar manual check: {n('QF62_gs_records')}", False), (f"unique works: {n('QF62_unique')}; already known: {n('QF62_known')}", False),
          (f"new {n('QF62_new')}: excluded {n('QF62_excluded')}; unresolved {n('QF62_unresolved')}", False), ('(unresolved: no full-text access)', False), (f"added to the corpus: {n('QF62_added')}", True)]
    bf = box(c, R, yf, RW, FS, (1, 1, 1), (0.35, 0.35, 0.37), [2.4, 1.6])
    # seed set
    SD = [('Seed set (stage 1)', True), (f"curated works: {n('QF57_seed')}", False)]
    ys = y1;
    y5 = max(b4 + 14, yf + 6)
    FC = [(f"Final corpus: {n('QF01')} works", True), (f"seed {n('QF57_seed')} + {n('QF43')} + {n('QF43_final')} (final search)", False), (f"direct FM social navigation {n('QF02')}", False),
          (f"classical and learning-based {n('QF57_S12')}", False), (f"adjacent FM navigation {n('QF57_S3')}", False), (f"datasets, simulators, benchmarks {n('QF57_S6')}", False),
          (f"surveys {n('QF57_S0')}", False)]
    b5 = box(c, L, y5, LW, FC, FINAL); arrow(c, [(L + LW / 2, b4), (L + LW / 2, y5)])
    arrow(c, [(R, yf + (bf - yf) / 2 + 22), (L + LW, yf + (bf - yf) / 2 + 22)], (0.55, 0.55, 0.57))
    text(c, L + LW + 3, yf + (bf - yf) / 2 + 18.5, str(n('QF62_added')), 7, False, 'left', DIM)
    yseed = b5 + 9
    bseed = box(c, L, yseed, 74, SD, (0.98, 0.94, 0.86)); arrow(c, [(L + 37, yseed), (L + 37, b5)])
    PF = [('Pre-FM comparison set (separate)', True), (f"{n('QF50_prefm_n')} works: {n('QF57_S12')} corpus works + {n('QF50_prefm_new')}", False),
          ('exemplars from 7 reference surveys', False), ('(Section 2.3); not part of the corpus count', False)]
    yp = bf + 10; bp = box(c, R, yp, RW, PF, (1, 1, 1), (0.55, 0.55, 0.57), [1.0, 1.4])
    yend = max(bseed, bp, yl) + 10
    text(c, X0, yend, 'Cut-off 19 October 2026. Not a PRISMA diagram. Counts: supplementary Table S1, parts A and B.', 7, False, 'left', DIM)
    global HT; HT = yend + 4
import cairo as _c
draw(_c.Context(_c.RecordingSurface(_c.CONTENT_COLOR_ALPHA, None)))
render(draw, W, HT, os.path.join(H, 'F8_screening_flow'))
if '--proto' in sys.argv:
    PR = os.path.join(ROOT, '12_Figures', 'prototypes'); os.makedirs(PR, exist_ok=True)
    for e in ('pdf', 'png', 'svg'): shutil.copy(os.path.join(H, f'F8_screening_flow.{e}'), os.path.join(PR, f'F_search_method_optionA.{e}'))
# ---------------- evidence map (written by the script)
M = ['# Evidence map: F8 literature search and corpus construction (generated by make_f8.py; do not edit)', '',
     '| Panel | Plotted variable | Numerator | Denominator | Source | Finding |', '|---|---|---|---|---|---|',
     '| (a) | none: conceptual map of the sources actually used, grouped by role; equal sectors | - | - | `09_Project_Reports/SEARCH_SOURCE_AUDIT.md` | - |']
for lab, v, inc in FIRST:
    M.append(f'| (b) | unique candidates first found by route "{lab}" (first-discovery source) | {v} | {n("QF42")} | `07_Literature_Analysis/_tools/stage2/screening_record.csv` (column `source`) | QF42, QF59_* |')
    M.append(f'| (b) | of these, candidates that met the criteria | {inc} | {v} | same (decision INCLUDE) | QF59_ft_include (sum) |')
for k in ('QF59_arxiv_records', 'QF59_arxiv_dups', 'QF42', 'QF58_tiab_excluded', 'QF59_ft_assessed', 'QF59_ft_include', 'QF59_include_inseed', 'QF43', 'QF43_final', 'QF57_seed', 'QF01', 'QF02',
          'QF62_ieee_records', 'QF62_oa_records', 'QF62_fw_records', 'QF62_gs_records', 'QF62_unique', 'QF62_known', 'QF62_new', 'QF62_excluded', 'QF62_unresolved', 'QF62_added', 'QF50_prefm_n'):
    M.append(f'| (c) | {QF[k]["statement"]} | {n(k)} | {QF[k]["denominator"]} | {QF[k]["source"]} | {k} |')
M += ['', 'Panel (b) uses one quantity only (unique candidates by first-discovery route). Raw records of the final coverage search overlap across sources and are therefore shown only as numbers in panel (c), not as bars.',
      'Generation script: `12_Figures/F8_screening_flow/make_f8.py` (pycairo; deterministic).']
open(os.path.join(H, 'EVIDENCE_MAP.md'), 'w').write('\n'.join(M) + '\n')
print('F8 done', round(HT, 1))

"""F9 - Evolution of social representation in robot navigation (neutral timeline; replaces the F5 concept diagram).
CSR precedent: overlapping paradigm bands on a dated axis (CSR 63 (2027) 101048 Fig. 2) and era boxes on a dated axis
(CSR 59 (2026) 100831 Fig. 1); no CSR evolution figure attributes a paradigm to its predecessor's limitation, so this figure has
no arrows between paradigms. Band start = first appearance (Era column of Table T2); dots = representative works of T2 placed at
the publication year recorded in the bibliography; every band continues to the literature cut-off because each paradigm's components
remain in use in the coded FM systems (Section III-F; T2 'Coexistence'). Print scale: canvas 516 pt (LaTeX \\textwidth 522 pt); all lettering >= 7 pt printed."""
import os, sys, re, csv
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figlib import *
H = os.path.dirname(os.path.abspath(__file__))
BIB = open(os.path.join(ROOT, '13_References', 'survey_references.bib')).read()
def year(k):
    m = re.search(r'@\w+\{' + re.escape(k) + r',.*?year = \{(\d{4})\}', BIB, re.S); assert m, k; return int(m.group(1))
GEO, PROB, LAT, LING = (0.62, 0.79, 0.93), (0.55, 0.82, 0.70), (0.80, 0.72, 0.88), (0.98, 0.76, 0.45)
# the four colours have similar luminance, so each class also has its own fill pattern (greyscale / colour-vision safe)
PAT = {GEO: 'solid', PROB: 'diag', LAT: 'dots', LING: 'horiz'}
# (paradigm label, first appearance [T2 Era], colour, representative works: (cite key, short label))
P = [('Proxemics and social spaces', 1966, GEO, [('Hall1966HallHidden', 'Hall'), ('Kirby2010KirbyCOMPANION', 'Kirby'), ('Lu2014LayeredCostmaps', 'layered costmaps'), ('Kim2022GroupEstimation', 'group spaces')]),
     ('Social forces and rules', 1995, GEO, [('Helbing1995SocialForce', 'social force model'), ('Moussaid2010MoussaidGroups', 'walking groups')]),
     ('Geometric collision avoidance', 2008, GEO, [('vandenBerg2008RVO', 'RVO'), ('vandenBerg2011ORCA', 'ORCA')]),
     ('Prediction-coupled planning', 2010, PROB, [('Trautman2010UnfreezingIGP', 'IGP'), ('al2016SocialLSTM', 'Social LSTM'), ('Trautman2015TrautmanIJRR2015', 'crowd trials')]),
     ('Inverse RL and imitation', 2012, PROB, [('Kuderer2012FeatureBasedPrediction', 'feature IRL'), ('Kretzschmar2016SociallyCompliantIRL', 'compliant IRL'), ('Okal2016BayesianIRL', 'Bayesian IRL'), ('Tai2018GAILDepth', 'GAIL')]),
     ('Deep RL crowd navigation', 2017, PROB, [('Chen2017CADRL', 'CADRL'), ('Chen2017SACADRL', 'SA-CADRL'), ('Chen2019SARLCrowdNav', 'SARL')]),
     ('Graph, attention, preference learning', 2019, PROB, [('Chen2020RGL', 'relational graph'), ('Wang2023NaviSTAR', 'NaviSTAR'), ('Raj2024HybridSocialNav', 'hybrid')]),
     ('FM navigation, no social objective', 2022, LAT, [('Shah2022LMNav', 'LM-Nav'), ('Huang2023VLMaps', 'VLMaps'), ('Shah2023ViNT', 'ViNT'), ('Yokoyama2024VLFM', 'VLFM')]),
     ('FM social reasoning over planners', 2024, LING, [('Sathyamoorthy2024CoNVOI', 'CoNVOI'), ('Song2025VLMSocialNav', 'VLM-Social-Nav'), ('Luo2025GSON', 'GSON'), ('Chen2026LISN', 'LISN')]),
     ('Distilled, latent and VLA-based', 2025, LAT, [('Narasimhan2025OLiViaNav', 'OLiVia-Nav'), ('Payandeh2026Narrate2Nav', 'Narrate2Nav'), ('Chen2026SocialNavCVPR', 'SocialNav'), ('Wang2026SALSA', 'SALSA')])]
for _, y0, _, ws in P:
    for k, _ in ws: assert year(k) >= y0 - 1, (k, year(k), y0)
CUT = 2026 + 9.6 / 12          # 19 October 2026
W, Ht = 516, 292
NX, AX0, AX1, TX = 4, 150, 334, 340   # name column, axis span, text column
BRK = 2000                    # piecewise scale: 1960-2000 compressed, 2000-cut-off expanded
def X(y): return AX0 + (y - 1960) / (BRK - 1960) * 50 if y < BRK else AX0 + 50 + (y - BRK) / (CUT - BRK) * (AX1 - AX0 - 50)
def draw(c):
    y0, rh = 20, 22
    text(c, NX, 11, 'Paradigm (first appearance)', 7.4, True, color='dark'); text(c, TX, 11, 'Representative works (markers)', 7.4, True, color='dark')
    for t in [1960, 2000, 2005, 2010, 2015, 2020]:
        line(c, X(t), y0 - 2, X(t), y0 + len(P) * rh + 2, 'light', 0.5)
        text(c, X(t), y0 + len(P) * rh + 11, str(t), 7, align='center', color='dark')
    xb = X(BRK) - 2; line(c, xb - 1.5, y0 + len(P) * rh + 6, xb + 1.5, y0 + len(P) * rh + 1, 'dark', 0.6); line(c, xb + 1.5, y0 + len(P) * rh + 6, xb + 4.5, y0 + len(P) * rh + 1, 'dark', 0.6)
    line(c, X(CUT), y0 - 2, X(CUT), y0 + len(P) * rh + 4, 'red', 0.7, [2, 1.5]); text(c, X(CUT) - 2, y0 + len(P) * rh + 11, 'cut-off', 7, False, 'left', DRED)
    for i, (lab, ys, col, ws) in enumerate(P):
        y = y0 + i * rh
        text(c, NX, y + rh / 2, f'{lab} ({ys})', 7, False, 'left', 'black', valign='middle')
        pattern(c, X(ys), y + 5, X(CUT) - X(ys), rh - 10, col, PAT[col]); c.save(); c.rectangle(X(ys), y + 5, X(CUT) - X(ys), rh - 10); c.set_source_rgb(0.45, 0.45, 0.45); c.set_line_width(0.3); c.stroke(); c.restore()
        for k, _ in ws:
            yy = year(k); c.save(); c.set_source_rgb(0.15, 0.15, 0.15); c.arc(X(yy + 0.5), y + rh / 2, 1.8, 0, 6.2832); c.fill(); c.restore()
        items = [f'{s} ({year(k)})' for k, s in ws]; l1, l2 = [], []
        for it in items: (l1 if len(', '.join(l1 + [it])) <= 44 and not l2 else l2).append(it)
        if l2: text(c, TX, y + rh / 2 - 4.2, ', '.join(l1) + ',', 7, False, 'left', 'dark', valign='middle'); text(c, TX, y + rh / 2 + 4.2, ', '.join(l2), 7, False, 'left', 'dark', valign='middle')
        else: text(c, TX, y + rh / 2, ', '.join(l1), 7, False, 'left', 'dark', valign='middle')
    ly = Ht - 26
    x = 92
    for nm, col in [('geometric', GEO), ('probabilistic / learned', PROB), ('latent / pretrained', LAT), ('linguistic', LING)]:
        pattern(c, x, ly - 6.5, 13, 7.5, col, PAT[col]); c.save(); c.rectangle(x, ly - 6.5, 13, 7.5); c.set_source_rgb(0.45, 0.45, 0.45); c.set_line_width(0.3); c.stroke(); c.restore()
        x += 16 + text(c, x + 16, ly, nm, 7) + 12
    text(c, NX, ly, 'Main representation:', 7, True, color='dark')
    text(c, NX, ly + 10, 'Bands run from first appearance to the literature cut-off; overlapping bands indicate coexistence, not replacement.', 7, color='dark')
    text(c, NX, ly + 18.4, 'The axis is compressed before 2000.', 7, color='dark')
render(draw, W, Ht, os.path.join(H, 'F9_evolution_timeline'))
print('F9 done')

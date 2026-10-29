"""Stage 4: generate QUANTITATIVE_FINDINGS.md and quantitative_findings.json directly from the final matrices.
Every number used in the manuscript must come from this file (no hand-typed percentages)."""
import csv, json, os, collections, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); A = os.path.join(ROOT, '07_Literature_Analysis')
CUT = '2026-10-19'
def rd(n): return list(csv.DictReader(open(os.path.join(A, n))))
M = rd('master_literature_matrix.csv'); D = rd('direct_vlm_social_navigation_matrix.csv'); CAP = {r['id']: r for r in rd('social_capabilities_matrix.csv')}
EV = {r['id']: r for r in rd('evidence_maturity_matrix.csv')}; MET = rd('evaluation_metrics_matrix.csv'); REP = {r['id']: r for r in rd('reproducibility_matrix.csv')}
CAI = {r['id']: r for r in csv.DictReader(open(os.path.join(A, '_tools', 'cai_citation_overlap.csv')))}
SCR = list(csv.DictReader(open(os.path.join(A, '_tools', 'stage2', 'screening_record.csv'))))
L = lambda v: [x.strip() for x in str(v).split(';') if x.strip() and x.strip() != 'NA']
nD = len(D); PRE = [m for m in M if m['analytical_category'] in ('S1', 'S2')]; nP = len(PRE)
# Stage 9: the pre-FM comparison set (12 frozen corpus works + 28 survey-selected exemplars; 07_Literature_Analysis/prefm_comparison_set.csv)
PCS = list(csv.DictReader(open(os.path.join(A, 'prefm_comparison_set.csv')))); nC = len(PCS)
for r in PCS: r['_A'] = set(r['A'].split()); r['_Y'] = set(r['cap_yes'].split()); r['_YP'] = r['_Y'] | set(r['cap_partial'].split())
PCSP = f'Pre-FM comparison set (n={nC}: 12 corpus works + {nC - 12} survey-selected exemplars)'
PCSC = 'Representative, not exhaustive: exemplars cited by reference surveys, likely biased towards well-evaluated works'
NONDIR = [m for m in M if m['analytical_category'] not in ('S0', 'S4', 'S5')]
QF = []
def q(fid, stmt, num, den, pop, src, cav='', ids=None):
    QF.append(dict(id=fid, statement=stmt, numerator=num, denominator=den, percentage=(f'{100 * num / den:.1f}%' if den else 'NA'), population=pop, source=src, cutoff=CUT, caveat=cav, ids=ids or []))
DIRP = 'Direct FM social-navigation papers (S4+S5), frozen corpus'
# ---- corpus
q('QF01', 'Unique works in the frozen corpus', len(M), len(M), 'All unique works (one note each)', 'master_literature_matrix.csv', 'Curated folders + 3-pass search; not a PRISMA review')
q('QF02', 'Direct FM social-navigation papers', nD, len(M), 'All unique works', 'master_literature_matrix.csv (direct_fm_social)')
for y in ['2024', '2025', '2026']:
    q(f'QF03_{y}', f'Direct papers published (year recorded) in {y}', sum(1 for d in D if d['year'] == y), nD, DIRP, 'direct matrix (year)', '2026 covers up to the freeze date' if y == '2026' else '')
st = collections.Counter(str(m['ext_status_class'])[:1] for m in M if m['direct_fm_social'] == 'Yes')
for c, lab in [('A', 'published and peer-reviewed (class A)'), ('B', 'accepted but not yet indexed (class B)'), ('C', 'preprint only (class C)'), ('D', 'acceptance verified, peer review not established (class D)')]:
    q(f'QF04{c}', f'Direct papers {lab}', st.get(c, 0), nD, DIRP, 'master matrix (ext_status_class)')
cs = collections.Counter(CAI[d['id']]['cai_status'] for d in D)
q('QF05a', 'Direct papers cited by Cai et al. 2026 (incl. 2 via related versions)', cs['cited'] + cs['cited (related version)'], nD, DIRP, 'cai_citation_overlap.csv')
q('QF05b', 'Direct papers first public before Cai cut-off (27 Jun 2026) but not cited by Cai', cs['not cited'], nD, DIRP, 'cai_citation_overlap.csv', 'Reason for non-citation not determinable')
q('QF05c', 'Direct papers first public after Cai cut-off', cs['after Cai cut-off'], nD, DIRP, 'cai_citation_overlap.csv')
# ---- Axis A
for a in ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']:
    q(f'QF06_{a}_direct', f'Direct papers whose human representation includes {a}', sum(1 for d in D if a in L(d['final_A_social_representation'])), nD, DIRP + ' (multi-label)', 'direct matrix final_A_social_representation')
    q(f'QF06_{a}_prefm', f'Pre-FM comparison works whose human representation includes {a}', sum(1 for r in PCS if a in r['_A']), nC, PCSP + ', multi-label', 'prefm_comparison_set.csv', PCSC)
    q(f'QF06_{a}_prefm12', f'Classical + learning corpus works (S1+S2) whose human representation includes {a}', sum(1 for m in PRE if a in L(m['final_A_social_representation'])), nP, 'S1+S2 works (n=12), multi-label', 'master matrix final_A_social_representation', 'Sensitivity: frozen-corpus pre-FM works only')
S3 = [m for m in M if m['analytical_category'] == 'S3']
q('QF07', 'Adjacent FM navigation works that do not represent humans (A0)', sum(1 for m in S3 if 'A0' in L(m['final_A_social_representation'])), len(S3), 'S3 adjacent works', 'master matrix')
# ---- Axis B
for r, lab in [('R1', 'scene/context interpretation'), ('R2', 'human-state/relation inference'), ('R3', 'social-norm reasoning/behaviour selection'), ('R4', 'instruction/preference grounding'), ('R5', 'human-facing communication')]:
    q(f'QF08_{r}', f'Direct papers with role {r} ({lab})', sum(1 for d in D if r in L(d['final_B_roles'])), nD, DIRP + ' (multi-label)', 'direct matrix final_B_roles', 'Non-exclusive; single coder')
# ---- Axis D
for i in range(9):
    c = f'D{i}'; q(f'QF09_{c}', f'Direct papers using interface {c}', sum(1 for d in D if c in L(d['final_D_interface'])), nD, DIRP + ' (multi-label)', 'direct matrix final_D_interface', 'Categorical, not a maturity order')
noc = [d['id'] for d in D if set(L(d['final_D_interface'])) <= {'D0', 'D8'}]; tro = [d['id'] for d in D if set(L(d['final_D_interface'])) <= {'D7'}]
q('QF10a', 'Direct papers whose FM output is never coupled to motion (D0/D8 only)', len(noc), nD, DIRP, 'direct matrix', ids=noc)
q('QF10b', 'Direct papers using the FM only at training time (D7 only)', len(tro), nD, DIRP, 'direct matrix', ids=tro)
q('QF10c', 'Direct papers with runtime FM-to-motion coupling (any of D1-D6)', sum(1 for d in D if set(L(d['final_D_interface'])) & {'D1', 'D2', 'D3', 'D4', 'D5', 'D6'}), nD, DIRP, 'direct matrix')
q('QF10d', 'Direct papers with two interface categories', sum(1 for d in D if len(L(d['final_D_interface'])) == 2), nD, DIRP, 'direct matrix')
q('QF10e', 'Direct papers with three interface categories', sum(1 for d in D if len(L(d['final_D_interface'])) == 3), nD, DIRP, 'direct matrix', ids=[d['id'] for d in D if len(L(d['final_D_interface'])) == 3])
for c in ['D0', 'D1', 'D3', 'D4', 'D6', 'D7']:
    g = [d for d in D if c in L(d['final_D_interface'])]
    q(f'QF11_{c}', f'Papers using {c} that have systematic real-robot evaluation', sum(1 for d in g if d['final_EV3_physical_robot'] == 'systematic'), len(g), f'Direct papers using {c}', 'direct matrix', 'Small groups; descriptive only')
d6 = [d for d in D if 'D6' in L(d['final_D_interface'])]
q('QF12', 'Direct-action (D6) papers with an FM-independent safety guard', sum(1 for d in d6 if d['final_xc_safety_guard'] == 'Yes'), len(d6), 'Direct papers using D6', 'direct matrix final_xc_safety_guard')
tc = collections.Counter(d['final_xc_temporal_coupling'] for d in D)
q('QF13', 'Direct papers with asynchronous slow/fast coupling', tc['asynchronous'], nD, DIRP, 'direct matrix final_xc_temporal_coupling', ids=[d['id'] for d in D if d['final_xc_temporal_coupling'] == 'asynchronous'])
# ---- Axis C
LEAF = ['SAF1', 'SAF2', 'SPA1', 'SPA2', 'SPA3', 'SPA4', 'HUM1', 'HUM2', 'NOR1', 'NOR2', 'NOR3', 'NOR4', 'EXP1', 'EXP2', 'EXP3']
FAM = {'SAF': LEAF[0:2], 'SPA': LEAF[2:6], 'HUM': LEAF[6:8], 'NOR': LEAF[8:12], 'EXP': LEAF[12:15]}
for f, ls in FAM.items():
    q(f'QF14_{f}_eval', f'Direct papers evaluating at least one {f} capability with a dedicated measure (Yes)', sum(1 for d in D if any(CAP[d['id']]['final_' + l] == 'Yes' for l in ls)), nD, DIRP, 'social_capabilities_matrix final_*', 'Yes = dedicated measure; depends on reporting')
    q(f'QF14_{f}_addr', f'Direct papers addressing at least one {f} capability (Yes or Partial)', sum(1 for d in D if any(CAP[d['id']]['final_' + l] in ('Yes', 'Partial') for l in ls)), nD, DIRP, 'social_capabilities_matrix final_*')
for l in LEAF:
    q(f'QF15_{l}_direct', f'Direct papers evaluating {l} (Yes)', sum(1 for d in D if CAP[d['id']]['final_' + l] == 'Yes'), nD, DIRP, 'social_capabilities_matrix')
    q(f'QF15_{l}_prefm', f'Pre-FM comparison works evaluating {l} (Yes)', sum(1 for r in PCS if l in r['_Y']), nC, PCSP, 'prefm_comparison_set.csv', PCSC)
    q(f'QF15_{l}_prefmaddr', f'Pre-FM comparison works addressing {l} (Yes or Partial)', sum(1 for r in PCS if l in r['_YP']), nC, PCSP, 'prefm_comparison_set.csv', PCSC)
    q(f'QF15_{l}_directaddr', f'Direct papers addressing {l} (Yes or Partial)', sum(1 for d in D if CAP[d['id']]['final_' + l] in ('Yes', 'Partial')), nD, DIRP, 'social_capabilities_matrix')
    q(f'QF15_{l}_prefm12', f'Classical + learning corpus works evaluating {l} (Yes)', sum(1 for m in PRE if CAP.get(m['id'], {}).get('final_' + l) == 'Yes'), nP, 'S1+S2 works (n=12)', 'social_capabilities_matrix', 'Sensitivity: frozen-corpus pre-FM works only')
# ---- Axis E
for k, lab in [('final_EV1_offline', 'offline quantitative evaluation (EV1=Yes)'), ('final_EV2_closed_loop_sim', 'closed-loop simulation (EV2=Yes)')]:
    q('QF16_' + k.split('_')[1], f'Direct papers with {lab}', sum(1 for d in D if d[k] == 'Yes'), nD, DIRP, 'evidence_maturity / direct matrix')
for v in ['systematic', 'demo', 'none']:
    q(f'QF17_EV3_{v}', f'Direct papers with physical-robot evidence = {v}', sum(1 for d in D if d['final_EV3_physical_robot'] == v), nD, DIRP, 'direct matrix final_EV3_physical_robot', 'Demo = qualitative or unreported runs')
for v in ['unscripted', 'staged', 'present-type-unreported', 'not-reported', 'simulated-only', 'none']:
    q(f'QF18_EV4_{v}', f'Direct papers whose real-human presence in trials = {v}', sum(1 for d in D if d['final_EV4_real_humans_in_trials'] == v), nD, DIRP, 'direct matrix final_EV4_real_humans_in_trials')
for v in ['co-present participants', 'observers/video', 'text-raters']:
    q('QF19_EV5_' + v.split()[0].replace('/', ''), f'Direct papers with human evaluation = {v}', sum(1 for d in D if d['final_EV5_human_evaluation'] == v), nD, DIRP, 'direct matrix final_EV5_human_evaluation', 'Rating robot behaviour only for co-present/observers', ids=[d['id'] for d in D if d['final_EV5_human_evaluation'] == v])
q('QF19_EV5_behaviour', 'Direct papers with human evaluation of robot behaviour (co-present or observers)', sum(1 for d in D if d['final_EV5_human_evaluation'] in ('co-present participants', 'observers/video')), nD, DIRP, 'direct matrix', 'None reports inferential statistics on the ratings (per notes)')
q('QF20', 'Direct papers with open-world / long-duration deployment (EV6)', sum(1 for d in D if d['final_EV6_open_world_deployment'] == 'Yes'), nD, DIRP, 'direct matrix')
q('QF21', 'Direct papers without systematic closed-loop evidence (no simulation and no systematic robot)', sum(1 for d in D if d['final_EV2_closed_loop_sim'] == 'No' and d['final_EV3_physical_robot'] != 'systematic'), nD, DIRP, 'direct matrix')
q('QF22', 'Direct papers whose only evidence is offline (EV1 only; no simulation, no robot run)', sum(1 for d in D if d['final_EV1_offline'] == 'Yes' and d['final_EV2_closed_loop_sim'] == 'No' and d['final_EV3_physical_robot'] == 'none'), nD, DIRP, 'direct matrix')
q('QF23', 'Direct papers reporting statistical testing of any result', sum(1 for d in D if str(d['final_quality_statistical_testing']).startswith('Yes')), nD, DIRP, 'direct matrix final_quality_statistical_testing', ids=[d['id'] for d in D if str(d['final_quality_statistical_testing']).startswith('Yes')])
q('QF24', 'Direct papers evaluated in both indoor and outdoor environments', sum(1 for d in D if d['final_quality_cross_environment'] == 'Yes'), nD, DIRP, 'direct matrix final_quality_cross_environment')
q('QF25', 'Direct papers reporting a numeric runtime/latency', sum(1 for d in D if d['final_quality_runtime_measured'] == 'Yes'), nD, DIRP, 'direct matrix final_quality_runtime_measured', 'Units and scopes not comparable')
# split of QF25: papers with an extracted runtime metric definition (same keyword pattern as the T8 runtime family in 11_Tables/build_tables.py, which asserts the match) vs numeric runtime given only in the system or deployment description
RT_RX = r'latency|FPS|inference|query (time|frequency|processing)|throughput|processing time|planning rate|control rate|infer\. rate|system rate|runtime|parameter count|generation time|module latency|inference speed|cycle time|\bLat\.'
rt_ids = [d['id'] for d in D if d['final_quality_runtime_measured'] == 'Yes']; rt_met = {m['id'] for m in MET if re.search(RT_RX, m['metric_name'], re.I)}
q('QF25_metric', 'Direct papers with a numeric runtime/latency that have an extracted runtime metric definition', sum(1 for i in rt_ids if i in rt_met), nD, DIRP, 'evaluation_metrics_matrix.csv (T8 runtime family) within QF25', ids=[i for i in rt_ids if i in rt_met])
q('QF25_textonly', 'Direct papers reporting numeric runtime/latency only in the system or deployment description (no runtime metric definition)', sum(1 for i in rt_ids if i not in rt_met), nD, DIRP, 'QF25 minus QF25_metric; values in deployment_runtime_matrix.csv (latency)', ids=[i for i in rt_ids if i not in rt_met])
sysr = [d for d in D if d['final_EV3_physical_robot'] == 'systematic']
q('QF26', 'Systematic real-robot papers with real humans present in trials (staged, unscripted or type unreported)', sum(1 for d in sysr if d['final_EV4_real_humans_in_trials'] in ('staged', 'unscripted', 'present-type-unreported')), len(sysr), 'Direct papers with systematic robot evidence', 'direct matrix')
det3 = [r for r in PCS if r['EV3_physical_robot'] != 'ND']; det5 = [r for r in PCS if r['EV5_human_evaluation'] != 'ND']
q('QF27a', 'Pre-FM comparison works with systematic real-robot evaluation', sum(1 for r in det3 if r['EV3_physical_robot'] == 'systematic'), len(det3), PCSP + '; works whose robot evidence is determinable', 'prefm_comparison_set.csv', PCSC + '; ND works excluded from the denominator')
q('QF27b', 'Pre-FM comparison works with human evaluation of robot behaviour', sum(1 for r in det5 if r['EV5_human_evaluation'] not in ('none', 'text-raters')), len(det5), PCSP + '; works whose human evaluation is determinable', 'prefm_comparison_set.csv', PCSC + '; ND works excluded from the denominator')
q('QF27a12', 'Classical + learning corpus works with systematic real-robot evaluation', sum(1 for m in PRE if EV[m['id']]['final_EV3_physical_robot'] == 'systematic'), nP, 'S1+S2 works (n=12)', 'evidence_maturity_matrix', 'Sensitivity: frozen-corpus pre-FM works only')
q('QF27b12', 'Classical + learning corpus works with human evaluation of robot behaviour', sum(1 for m in PRE if EV[m['id']]['final_EV5_human_evaluation'].startswith('robot-behaviour')), nP, 'S1+S2 works (n=12)', 'evidence_maturity_matrix', 'Sensitivity: frozen-corpus pre-FM works only')
# ---- cross-cutting / reliability
q('QF28', 'Direct papers with an FM-independent safety guard', sum(1 for d in D if d['final_xc_safety_guard'] == 'Yes'), nD, DIRP, 'direct matrix final_xc_safety_guard')
q('QF29', 'Systematic real-robot direct papers with an FM-independent safety guard', sum(1 for d in sysr if d['final_xc_safety_guard'] == 'Yes'), len(sysr), 'Direct papers with systematic robot evidence', 'direct matrix')
for v, lab in [('Yes', 'explicit'), ('Partial', 'partial')]:
    q(f'QF30_{lab}', f'Direct papers with {lab} uncertainty treatment', sum(1 for d in D if d['final_xc_uncertainty'] == v), nD, DIRP, 'direct matrix final_xc_uncertainty')
for v, lab in [('Yes', 'structural'), ('Partial', 'prompt/training-level')]:
    q(f'QF31_{lab.split("/")[0]}', f'Direct papers with {lab} hallucination mitigation', sum(1 for d in D if d['final_xc_hallucination_mitigation'] == v), nD, DIRP, 'direct matrix final_xc_hallucination_mitigation')
loc = collections.Counter(d['final_xc_inference_location'] for d in D)
LID = {'cloud API': 'QF32_cloud', 'hybrid (local + cloud)': 'QF32_hybrid', 'local/onboard or local server': 'QF32_local', 'remote server': 'QF32_remote', 'not reported': 'QF32_notreported',
       'n/a (FM used at training time only)': 'QF32_trainingonly', 'n/a (offline evaluation only)': 'QF32_offlineonly'}
for k, v in sorted(loc.items()): q(LID[k], f'Direct papers with inference location = {k}', v, nD, DIRP, 'direct matrix final_xc_inference_location')
rtfm = nD - loc['n/a (FM used at training time only)'] - loc['n/a (offline evaluation only)']
q('QF32_cloudremote_runtime', 'Papers with a runtime FM that rely on cloud API, hybrid or remote-server inference', loc['cloud API'] + loc['hybrid (local + cloud)'] + loc['remote server'], rtfm, 'Direct papers with an FM at runtime (excl. training-only and offline-only)', 'direct matrix final_xc_inference_location')
q('QF32_cloudremote', 'Direct papers relying on cloud API, hybrid or remote-server FM inference', loc['cloud API'] + loc['hybrid (local + cloud)'] + loc['remote server'], nD, DIRP, 'direct matrix')
q('QF33', 'Direct papers with persistent memory', sum(1 for d in D if d['final_xc_memory'] != 'No'), nD, DIRP, 'direct matrix final_xc_memory')
q('QF34', 'Direct papers treating privacy as a constraint/objective', sum(1 for d in D if d['final_xc_privacy_constraint'] != 'No'), nD, DIRP, 'direct matrix final_xc_privacy_constraint')
q('QF35', 'Direct papers releasing code (Yes)', sum(1 for d in D if REP[d['id']]['coding_code_released'] == 'Yes'), nD, DIRP, 'reproducibility_matrix coding_code_released')
q('QF36', 'Direct papers releasing a new dataset', sum(1 for d in D if REP[d['id']]['coding_new_dataset_released'] == 'Yes'), nD, DIRP, 'reproducibility_matrix')
# ---- evaluation / datasets
dm = [m for m in MET if m['direct_fm_social'] == 'Yes']
q('QF37', 'Metric definitions extracted (all works)', len(MET), len(MET), 'Metric rows', 'evaluation_metrics_matrix.csv')
for c, n in sorted(collections.Counter(m['metric_category'] for m in dm).items()):
    q(f'QF38_{c}', f'Metric definitions in direct papers in category {c}', n, len(dm), 'Metric rows from direct papers', 'evaluation_metrics_matrix.csv', 'Rows are definitions, not papers')
S6 = [m for m in M if m['analytical_category'] == 'S6']
q('QF39', 'FM-based social-navigation datasets/benchmarks within S6', sum(1 for m in S6 if m['fm_social_benchmark'] == 'Yes'), len(S6), 'S6 works', 'master matrix fm_social_benchmark')
MI = {m['id']: m for m in M}
sn = [d['id'] for d in D if str(MI[d['id']].get('snei_usage', '')).strip()]
q('QF40', 'Direct papers that use or describe SNEI', len(sn) + 1, nD, DIRP, 'notes snei_usage + Social-LLaVA (origin)', 'SNEI subsets differ; not comparable', ids=sn + ['2025_Payandeh_Social-LLaVA'])
q('QF41', 'Direct papers with Ling Xiao as co-author', sum(1 for d in D if 'Ling Xiao' in next(m for m in M if m['id'] == d['id'])['authors']), nD, DIRP, 'master matrix authors', 'Author-group concentration')
# ---- method
q('QF42', 'Candidates screened in Stage 2 (search + web + citation)', len(SCR), len(SCR), 'Screening record', 'stage2/screening_record.csv')
q('QF43', 'Works added in the Stage-2 expansion', sum(1 for m in M if m['stage2_added'] == 'Yes' and m.get('final_search_added') != 'Yes'), len(M), 'All unique works', 'master matrix stage2_added, final_search_added')
q('QF43_final', 'Works added by the final coverage search (2026-10-26)', sum(1 for m in M if m.get('final_search_added') == 'Yes'), len(M), 'All unique works', 'master matrix final_search_added', ids=[m['id'] for m in M if m.get('final_search_added') == 'Yes'])
# ---- Stage 7: cross-axis findings used in the strengthened Sections 3, 7 and 9 (existing IDs unchanged)
LEAVES = ['SAF1', 'SAF2', 'SPA1', 'SPA2', 'SPA3', 'SPA4', 'HUM1', 'HUM2', 'NOR1', 'NOR2', 'NOR3', 'NOR4', 'EXP1', 'EXP2', 'EXP3']
def yes(i, l): return CAP.get(i, {}).get('final_' + l) == 'Yes'
def anyyes(i): return any(yes(i, l) for l in LEAVES)
RT = {'D1', 'D2', 'D3', 'D4', 'D5', 'D6'}
d0 = [d for d in D if 'D0' in L(d['final_D_interface'])]; rtc = [d for d in D if set(L(d['final_D_interface'])) & RT]
q('QF44_D0_anyeval', 'Offline decision (D0) papers evaluating at least one capability leaf with a dedicated measure', sum(anyyes(d['id']) for d in d0), len(d0), 'Direct papers using D0', 'direct + capabilities matrices', 'Model-level metrics (text similarity, action accuracy) are not capability measures')
q('QF44_runtime_anyeval', 'Runtime-coupled (D1-D6) papers evaluating at least one capability leaf with a dedicated measure', sum(anyyes(d['id']) for d in rtc), len(rtc), 'Direct papers with runtime FM-to-motion coupling', 'direct + capabilities matrices')
n2 = [d for d in D if yes(d['id'], 'NOR2')]; r4 = [d for d in D if 'R4' in L(d['final_B_roles'])]; r3 = [d for d in D if 'R3' in L(d['final_B_roles'])]
q('QF45_NOR2_R4', 'Papers evaluating instruction following (NOR2) whose FM role includes instruction grounding (R4)', sum('R4' in L(d['final_B_roles']) for d in n2), len(n2), 'Direct papers evaluating NOR2', 'direct + capabilities matrices', 'Single coder; small group', ids=[d['id'] for d in n2])
q('QF45_R4_NOR2', 'R4 (instruction/preference grounding) papers that evaluate NOR2', sum(yes(d['id'], 'NOR2') for d in r4), len(r4), 'Direct papers with role R4', 'direct + capabilities matrices')
q('QF45_R3_NOR', 'R3 (FM infers norms) papers evaluating any normative/contextual (NOR) leaf', sum(any(yes(d['id'], l) for l in ['NOR1', 'NOR2', 'NOR3', 'NOR4']) for d in r3), len(r3), 'Direct papers with role R3', 'direct + capabilities matrices')
a5 = [d for d in D if 'A5' in L(d['final_A_social_representation'])]; na5 = [d for d in D if 'A5' not in L(d['final_A_social_representation'])]
q('QF46_A5_NOR23', 'A5 (linguistic representation) papers evaluating NOR2 or NOR3', sum(yes(d['id'], 'NOR2') or yes(d['id'], 'NOR3') for d in a5), len(a5), 'Direct papers with A5', 'direct + capabilities matrices', 'Paper-level association; corpus-level co-occurrence differs')
q('QF46_nonA5_NOR23', 'Papers without A5 evaluating NOR2 or NOR3', sum(yes(d['id'], 'NOR2') or yes(d['id'], 'NOR3') for d in na5), len(na5), 'Direct papers without A5', 'direct + capabilities matrices')
a24 = [d for d in D if set(L(d['final_A_social_representation'])) & {'A2', 'A4'}]
q('QF46_A24_HUM1SPA4', 'A2/A4 (predicted motion or relational) papers evaluating HUM1 or SPA4', sum(yes(d['id'], 'HUM1') or yes(d['id'], 'SPA4') for d in a24), len(a24), 'Direct papers with A2 or A4', 'direct + capabilities matrices')
CLOUD = ('cloud API', 'hybrid (local + cloud)', 'remote server')
d3 = [d for d in D if 'D3' in L(d['final_D_interface'])]; d56 = [d for d in D if set(L(d['final_D_interface'])) & {'D5', 'D6'}]
q('QF47_D3_cloud', 'Objective-shaping (D3) papers relying on cloud, hybrid or remote FM inference', sum(d['final_xc_inference_location'] in CLOUD for d in d3), len(d3), 'Direct papers using D3', 'direct matrix final_xc_inference_location')
q('QF47_D3_guard', 'Objective-shaping (D3) papers with an FM-independent safety guard', sum(d['final_xc_safety_guard'] == 'Yes' for d in d3), len(d3), 'Direct papers using D3', 'direct matrix final_xc_safety_guard')
q('QF47_D56_cloud', 'Latent-conditioning or direct-action (D5/D6) papers relying on cloud, hybrid or remote FM inference', sum(d['final_xc_inference_location'] in CLOUD for d in d56), len(d56), 'Direct papers using D5 or D6', 'direct matrix final_xc_inference_location')
q('QF47_D56_guard', 'Latent-conditioning or direct-action (D5/D6) papers with an FM-independent safety guard', sum(d['final_xc_safety_guard'] == 'Yes' for d in d56), len(d56), 'Direct papers using D5 or D6', 'direct matrix final_xc_safety_guard')
asy = [d for d in D if d['final_xc_temporal_coupling'] in ('asynchronous', 'event-triggered')]
q('QF48_async_systematic', 'Asynchronous or event-triggered papers with systematic real-robot evaluation', sum(d['final_EV3_physical_robot'] == 'systematic' for d in asy), len(asy), 'Direct papers with asynchronous or event-triggered coupling', 'direct matrix')
q('QF49_prefm_anyeval', 'Pre-FM comparison works evaluating at least one capability leaf with a dedicated measure', sum(1 for r in PCS if r['_Y']), nC, PCSP, 'prefm_comparison_set.csv', PCSC)
q('QF49_prefm12_anyeval', 'Classical + learning corpus works evaluating at least one capability leaf with a dedicated measure', sum(anyyes(m['id']) for m in PRE), nP, 'S1+S2 works (n=12)', 'capabilities matrix', 'Sensitivity: frozen-corpus pre-FM works only')
# ---- Stage 9: comparison-set composition, sensitivity, Cai coverage consequence, peer-reviewed robustness, preprint dependence, corpus categories
PAR = sorted({r['paradigm'] for r in PCS}); FTS = [r for r in PCS if r['coding_source'].startswith('full text')]
q('QF50_prefm_n', 'Works in the pre-FM comparison set', nC, nC, PCSP, 'prefm_comparison_set.csv', PCSC)
q('QF50_prefm_new', 'Survey-selected pre-FM exemplars added in Stage 9', nC - nP, nC, PCSP, 'prefm_comparison_set.csv')
q('QF50_prefm_fulltext', 'Pre-FM comparison works coded from full text', len(FTS), nC, PCSP, 'prefm_comparison_set.csv', 'The rest are coded from reference-survey descriptions')
q('QF50_prefm_paradigms', 'Pre-FM paradigms represented in the comparison set', len(PAR), len(PAR), PCSP, 'prefm_comparison_set.csv')
q('QF50_prefm_minpar', 'Smallest paradigm group in the comparison set (imitation learning)', min(sum(1 for r in PCS if r['paradigm'] == p) for p in PAR), nC, PCSP, 'prefm_comparison_set.csv', 'Only two eligible imitation-learning exemplars are cited by the reference surveys')
q('QF50_prefm_robotND', 'Pre-FM comparison works whose robot evidence is not determinable', nC - len(det3), nC, PCSP, 'prefm_comparison_set.csv')
for l in ['SPA4', 'HUM1', 'NOR2', 'NOR3']:
    q(f'QF51_par_{l}', f'Pre-FM paradigms with at least one work evaluating {l}', sum(1 for p in PAR if any(l in r['_Y'] for r in PCS if r['paradigm'] == p)), len(PAR), PCSP, 'prefm_comparison_set.csv')
q('QF51_par_A5', 'Pre-FM paradigms with at least one work representing people symbolically (A5)', sum(1 for p in PAR if any('A5' in r['_A'] for r in PCS if r['paradigm'] == p)), len(PAR), PCSP, 'prefm_comparison_set.csv')
q('QF51_par_A4', 'Pre-FM paradigms with at least one work representing relational structure (A4)', sum(1 for p in PAR if any('A4' in r['_A'] for r in PCS if r['paradigm'] == p)), len(PAR), PCSP, 'prefm_comparison_set.csv')
for l in ['SPA4', 'HUM1', 'NOR2', 'NOR3']:
    q(f'QF52_ft_{l}', f'Full-text-coded pre-FM comparison works evaluating {l}', sum(1 for r in FTS if l in r['_Y']), len(FTS), 'Full-text-coded pre-FM comparison works', 'prefm_comparison_set.csv', 'Sensitivity')
q('QF52_ft_A5', 'Full-text-coded pre-FM comparison works with A5', sum(1 for r in FTS if 'A5' in r['_A']), len(FTS), 'Full-text-coded pre-FM comparison works', 'prefm_comparison_set.csv', 'Sensitivity')
q('QF52_ft_A4', 'Full-text-coded pre-FM comparison works with A4', sum(1 for r in FTS if 'A4' in r['_A']), len(FTS), 'Full-text-coded pre-FM comparison works', 'prefm_comparison_set.csv', 'Sensitivity')
q('QF52_ft_robot', 'Full-text-coded pre-FM comparison works with systematic real-robot evaluation', sum(1 for r in FTS if r['EV3_physical_robot'] == 'systematic'), len(FTS), 'Full-text-coded pre-FM comparison works', 'prefm_comparison_set.csv', 'Sensitivity')
q('QF52_ft_human', 'Full-text-coded pre-FM comparison works with human evaluation of robot behaviour', sum(1 for r in FTS if r['EV5_human_evaluation'] not in ('none', 'text-raters', 'ND')), len(FTS), 'Full-text-coded pre-FM comparison works', 'prefm_comparison_set.csv', 'Sensitivity')
q('QF53_prefm_EXP_eval', 'Pre-FM comparison works evaluating at least one human-experience (EXP) leaf', sum(1 for r in PCS if r['_Y'] & set(FAM['EXP'])), nC, PCSP, 'prefm_comparison_set.csv', PCSC)
q('QF53_prefm_NOR_eval', 'Pre-FM comparison works evaluating at least one normative (NOR) leaf', sum(1 for r in PCS if r['_Y'] & set(FAM['NOR'])), nC, PCSP, 'prefm_comparison_set.csv', PCSC)
q('QF53_prefm_NOR_addr', 'Pre-FM comparison works addressing at least one normative (NOR) leaf', sum(1 for r in PCS if r['_YP'] & set(FAM['NOR'])), nC, PCSP, 'prefm_comparison_set.csv', PCSC)
for fam_ in ['SPA', 'HUM', 'EXP']:
    q(f'QF53_prefm_{fam_}_addr', f'Pre-FM comparison works addressing at least one {fam_} leaf (Yes or Partial)', sum(1 for r in PCS if r['_YP'] & set(FAM[fam_])), nC, PCSP, 'prefm_comparison_set.csv', PCSC)
q('QF50_prefm_secondary', 'Pre-FM comparison works coded from reference-survey descriptions only', nC - len(FTS), nC, PCSP, 'prefm_comparison_set.csv', 'No legitimate full text accessible')
q('QF53_prefm_openworld', 'Pre-FM comparison works reporting open-world or long-duration deployment', sum(1 for r in PCS if r['EV6_open_world'] == 'Yes'), nC, PCSP, 'prefm_comparison_set.csv', 'Museum tour-guide deployment', ids=[r['key'] for r in PCS if r['EV6_open_world'] == 'Yes'])
q('QF53_prefm_A5secondary', 'Pre-FM comparison works with A5 that are coded from secondary sources only', sum(1 for r in PCS if 'A5' in r['_A'] and not r['coding_source'].startswith('full text')), sum(1 for r in PCS if 'A5' in r['_A']), 'Pre-FM comparison works with A5', 'prefm_comparison_set.csv')
# Cai coverage consequence (pre-cut-off direct papers not cited by Cai vs cited)
nc = [d for d in D if CAI[d['id']]['cai_status'] == 'not cited']; ct = [d for d in D if CAI[d['id']]['cai_status'] in ('cited', 'cited (related version)')]
for l in ['NOR2', 'NOR3']:
    g = [d for d in D if yes(d['id'], l) and CAI[d['id']]['cai_status'] != 'after Cai cut-off']
    q(f'QF54_{l}_uncited', f'Pre-Cai-cut-off direct papers evaluating {l} that Cai et al. do not cite', sum(1 for d in g if CAI[d['id']]['cai_status'] == 'not cited'), len(g), f'Direct papers evaluating {l} and public before 27 Jun 2026', 'cai_citation_overlap.csv + capabilities matrix')
g = [d for d in D if 'D3' in L(d['final_D_interface']) and CAI[d['id']]['cai_status'] != 'after Cai cut-off']
q('QF54_D3_uncited', 'Pre-Cai-cut-off objective-shaping (D3) papers that Cai et al. do not cite', sum(1 for d in g if CAI[d['id']]['cai_status'] == 'not cited'), len(g), 'Direct D3 papers public before 27 Jun 2026', 'cai_citation_overlap.csv + direct matrix')
q('QF54_cited_uncoupled', 'Direct papers cited by Cai et al. whose FM output never reaches motion (D0/D8 only)', sum(1 for d in ct if set(L(d['final_D_interface'])) <= {'D0', 'D8'}), len(ct), 'Direct papers cited by Cai et al.', 'cai_citation_overlap.csv + direct matrix')
q('QF54_uncited_uncoupled', 'Pre-cut-off direct papers not cited by Cai et al. whose FM output never reaches motion', sum(1 for d in nc if set(L(d['final_D_interface'])) <= {'D0', 'D8'}), len(nc), 'Pre-cut-off direct papers not cited by Cai et al.', 'cai_citation_overlap.csv + direct matrix')
# robustness on the peer-reviewed (class A) and pre-Cai subsets
MS = {m['id']: m for m in M}
for tag, sub, lab in [('pr', [d for d in D if str(MS[d['id']]['ext_status_class']).startswith('A')], 'Peer-reviewed (class A) direct papers'),
                      ('precai', [d for d in D if CAI[d['id']]['cai_status'] != 'after Cai cut-off'], 'Direct papers public before the Cai cut-off')]:
    n = len(sub)
    q(f'QF55_{tag}_A5', f'{lab} with linguistic representation (A5)', sum(1 for d in sub if 'A5' in L(d['final_A_social_representation'])), n, lab, 'direct matrix', 'Robustness subset')
    q(f'QF55_{tag}_NOR2', f'{lab} evaluating NOR2', sum(1 for d in sub if yes(d['id'], 'NOR2')), n, lab, 'capabilities matrix', 'Robustness subset')
    q(f'QF55_{tag}_SPA4', f'{lab} evaluating SPA4', sum(1 for d in sub if yes(d['id'], 'SPA4')), n, lab, 'capabilities matrix', 'Robustness subset')
    q(f'QF55_{tag}_robot', f'{lab} with systematic real-robot evaluation', sum(1 for d in sub if d['final_EV3_physical_robot'] == 'systematic'), n, lab, 'direct matrix', 'Robustness subset')
    q(f'QF55_{tag}_human', f'{lab} with human evaluation of robot behaviour', sum(1 for d in sub if d['final_EV5_human_evaluation'] in ('co-present participants', 'observers/video')), n, lab, 'direct matrix', 'Robustness subset')
    q(f'QF55_{tag}_uncoupled', f'{lab} whose FM output never reaches motion', sum(1 for d in sub if set(L(d['final_D_interface'])) <= {'D0', 'D8'}), n, lab, 'direct matrix', 'Robustness subset')
q('QF56_D6_notpr', 'Direct-action (D6) papers that are not peer-reviewed publications (classes B-D)', sum(1 for d in d6 if not str(MS[d['id']]['ext_status_class']).startswith('A')), len(d6), 'Direct papers using D6', 'master matrix ext_status_class')
q('QF56_D56_notpr', 'Latent-conditioning or direct-action (D5/D6) papers that are not peer-reviewed publications', sum(1 for d in d56 if not str(MS[d['id']]['ext_status_class']).startswith('A')), len(d56), 'Direct papers using D5 or D6', 'master matrix ext_status_class')
cat = collections.Counter(m['analytical_category'] for m in M)
q('QF57_coded', 'Coded works (all non-survey works)', sum(v for k, v in cat.items() if k != 'S0'), len(M), 'All unique works', 'master matrix analytical_category')
for k, lab in [('S12', 'classical and learning works (S1+S2)'), ('S3', 'adjacent FM navigation works (S3)'), ('S6', 'datasets, simulators and benchmarks (S6)'), ('S0', 'surveys (S0)')]:
    v = cat['S1'] + cat['S2'] if k == 'S12' else cat[k]
    q(f'QF57_{k}', f'Corpus {lab}', v, len(M), 'All unique works', 'master matrix analytical_category')
d24 = [d for d in D if set(L(d['final_D_interface'])) & {'D2', 'D3', 'D4'}]
q('QF58_D24_any', 'Direct papers using at least one of D2, D3 or D4', len(d24), nD, DIRP, 'direct matrix')
q('QF58_D24_withD56', 'D2-D4 papers that also execute FM-generated actions or latents (D5/D6)', sum(1 for d in d24 if set(L(d['final_D_interface'])) & {'D5', 'D6'}), len(d24), 'Direct papers using D2-D4', 'direct matrix')
q('QF58_D24_planner', 'D2-D4 papers in which a planner executes FM guidance (no D5/D6)', sum(1 for d in d24 if not set(L(d['final_D_interface'])) & {'D5', 'D6'}), len(d24), 'Direct papers using D2-D4', 'direct matrix')
q('QF58_sys_human', 'Systematic real-robot direct papers with human evaluation of robot behaviour', sum(1 for d in sysr if d['final_EV5_human_evaluation'] in ('co-present participants', 'observers/video')), len(sysr), 'Direct papers with systematic robot evidence', 'direct matrix')
q('QF58_sys_nohuman', 'Systematic real-robot direct papers without human evaluation of robot behaviour', sum(1 for d in sysr if d['final_EV5_human_evaluation'] not in ('co-present participants', 'observers/video')), len(sysr), 'Direct papers with systematic robot evidence', 'direct matrix')
il = [r for r in PCS if r['paradigm'].startswith(('P6 ', 'P7 '))]
q('QF58_irlil_robot', 'IRL and imitation works in the pre-FM comparison set with systematic real-robot evaluation', sum(1 for r in il if r['EV3_physical_robot'] == 'systematic'), len(il), 'IRL and imitation works in the comparison set', 'prefm_comparison_set.csv', PCSC)
q('QF58_tiab_excluded', 'Candidates excluded at title/abstract', sum(1 for r in SCR if r['screening'] == 'title/abstract'), len(SCR), 'Screening record', 'stage2/screening_record.csv')
q('QF57_seed', 'Seed works before the Stage-2 expansion', len(M) - sum(1 for m in M if m['stage2_added'] == 'Yes'), len(M), 'All unique works', 'master matrix stage2_added')
# Stage 11 (CSR adaptation): literature search and screening flow, all from the screening record
SRC = 'stage2/screening_record.csv'
passes = [r['passes'] for r in SCR]
arx = [p for p in passes if p.startswith('P')]
q('QF59_arxiv_records', 'arXiv search records across the three passes, before removing candidates found by more than one pass', sum(len(p.split('+')) for p in arx), len(SCR), 'Screening record', SRC)
q('QF59_arxiv_dups', 'arXiv records removed because the candidate was already found by another pass', sum(len(p.split('+')) - 1 for p in arx), len(SCR), 'Screening record', SRC)
q('QF59_arxiv_unique', 'Unique candidates from the arXiv search passes', len(arx), len(SCR), 'Screening record', SRC)
q('QF59_web', 'Candidates from web discovery', sum(1 for r in SCR if r['source'] == 'web'), len(SCR), 'Screening record', SRC)
q('QF59_citation', 'Candidates from citation chasing', sum(1 for r in SCR if r['source'] == 'citation'), len(SCR), 'Screening record', SRC)
q('QF59_finalcheck', 'Candidates from the final check at the cut-off (publisher indexes)', sum(1 for r in SCR if r['source'] == 'final check'), len(SCR), 'Screening record', SRC)
ft = [r for r in SCR if r['screening'] == 'full text']
q('QF59_ft_assessed', 'Candidates assessed in full text', len(ft), len(SCR), 'Screening record', SRC)
q('QF59_ft_excluded', 'Candidates excluded after full-text assessment', sum(1 for r in ft if r['decision'] == 'EXCLUDE'), len(ft), 'Candidates assessed in full text', SRC)
q('QF59_ft_background', 'Full-text candidates kept as background references only (not coded)', sum(1 for r in ft if r['decision'] == 'BACKGROUND ONLY'), len(ft), 'Candidates assessed in full text', SRC)
q('QF59_ft_withdrawn', 'Full-text candidates withdrawn by their authors', sum(1 for r in ft if 'WITHDRAWN' in r['decision']), len(ft), 'Candidates assessed in full text', SRC)
q('QF59_ft_related', 'Full-text candidates that are another version of an included work', sum(1 for r in ft if r['decision'] == 'RELATED VERSION'), len(ft), 'Candidates assessed in full text', SRC)
inc = [r for r in ft if r['decision'] == 'INCLUDE']
q('QF59_ft_include', 'Full-text candidates meeting the inclusion criteria', len(inc), len(ft), 'Candidates assessed in full text', SRC)
q('QF59_include_inseed', 'Included candidates that were already in the seed set', sum(1 for r in inc if r['reason'].startswith('already in Stage-1')), len(inc), 'Included candidates', SRC)
q('QF59_include_new', 'Included candidates new to the corpus', sum(1 for r in inc if not r['reason'].startswith('already in Stage-1')), len(inc), 'Included candidates', SRC)
# Stage 11 (CSR adaptation): per-interface guard and inference location for the interface table (T11)
for c in ['D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8']:
    g = [d for d in D if c in L(d['final_D_interface'])]
    q(f'QF60_{c}_guard', f'Papers using {c} with an FM-independent safety guard', sum(d['final_xc_safety_guard'] == 'Yes' for d in g), len(g), f'Direct papers using {c}', 'direct matrix final_xc_safety_guard', 'Small groups; descriptive only')
    q(f'QF60_{c}_sys', f'Papers using {c} that report systematic real-robot evaluation', sum(d['final_EV3_physical_robot'] == 'systematic' for d in g), len(g), f'Direct papers using {c}', 'direct matrix final_EV3_physical_robot', 'Small groups; descriptive only')
    q(f'QF60_{c}_remote', f'Papers using {c} that rely on cloud API, hybrid or remote-server FM inference', sum(d['final_xc_inference_location'] in CLOUD for d in g), len(g), f'Direct papers using {c}', 'direct matrix final_xc_inference_location', 'Small groups; descriptive only')
# QF61: evidence by publication year and statistics on human ratings (final audit, 2026-10-21)
BEH = ('co-present participants', 'observers/video')
for y in ('2024', '2025', '2026'):
    g = [d for d in D if d['year'] == y]
    q(f'QF61_sys_{y}', f'Direct papers from {y} with systematic real-robot evaluation', sum(d['final_EV3_physical_robot'] == 'systematic' for d in g), len(g), f'Direct papers published in {y}', 'direct matrix final_EV3_physical_robot (year)')
    q(f'QF61_hum_{y}', f'Direct papers from {y} with human evaluation of robot behaviour', sum(d['final_EV5_human_evaluation'] in BEH for d in g), len(g), f'Direct papers published in {y}', 'direct matrix final_EV5_human_evaluation (year)')
g = [d for d in D if d['final_EV5_human_evaluation'] in BEH]
q('QF61_beh_stats', 'Papers with human evaluation of robot behaviour that report inferential statistics on the ratings', sum(str(d['final_quality_statistical_testing']).startswith('Yes') for d in g), len(g), 'Direct papers with human evaluation of robot behaviour', 'direct matrix final_quality_statistical_testing', ids=[d['id'] for d in g])
# QF62: final coverage search (2026-10-26; IEEE Xplore, OpenAlex, OpenAlex forward citations, one Google Scholar page)
S11 = os.path.join(ROOT, '07_Literature_Analysis', '_tools', 'stage11')
def j11(n): return json.load(open(os.path.join(S11, n)))
F11R = list(csv.DictReader(open(os.path.join(S11, 'S1_final_search_record.csv'))))
SRC11 = '07_Literature_Analysis/_tools/stage11 (S1_final_search_record.csv, *_hits.json)'
ie, oa, fw, gs = j11('ieee_hits.json'), j11('openalex_hits.json'), j11('forward_hits.json'), j11('gs_hits.json')
raw = {'ieee': sum(f['raw_results'] for f in ie['families']), 'oa': sum(f['raw_results'] for f in oa['families']), 'fw': sum(f['retrieved'] for f in fw['families']), 'gs': sum(f['listed'] for f in gs['families'])}
uniq_src = len(ie['hits']) + len(oa['hits']) + len(fw['hits']) + len(gs['hits'])
q('QF62_ieee_queries', 'IEEE Xplore query families in the final coverage search', len(ie['families']), len(ie['families']), 'IEEE Xplore queries', SRC11)
q('QF62_ieee_records', 'IEEE Xplore records retrieved (all results listed)', raw['ieee'], raw['ieee'], 'IEEE Xplore records', SRC11)
q('QF62_oa_queries', 'OpenAlex query families (title and abstract)', len(oa['families']), len(oa['families']), 'OpenAlex queries', SRC11)
q('QF62_oa_records', 'OpenAlex records retrieved (all results listed)', raw['oa'], raw['oa'], 'OpenAlex records', SRC11)
q('QF62_fw_seeds', 'Direct papers whose citing works were retrieved on OpenAlex (forward citation chasing)', sum(1 for f in fw['families'] if f['openalex']), len(fw['families']), 'Direct papers', SRC11)
q('QF62_fw_records', 'Citing records retrieved by forward citation chasing', raw['fw'], raw['fw'], 'Citing records', SRC11)
q('QF62_gs_records', 'Google Scholar records retrieved before an automated-access check stopped the search', raw['gs'], raw['gs'], 'Google Scholar records', SRC11)
q('QF62_records', 'Records retrieved in the final coverage search (all sources)', sum(raw.values()), sum(raw.values()), 'Retrieved records', SRC11)
q('QF62_dups', 'Duplicate records removed (same work retrieved more than once, within or across sources)', sum(raw.values()) - len(F11R), sum(raw.values()), 'Retrieved records', SRC11)
q('QF62_unique', 'Unique works in the final coverage search', len(F11R), sum(raw.values()), 'Retrieved records', SRC11)
known = [r for r in F11R if r['decision'] in ('ALREADY KNOWN', 'ALREADY SCREENED (Stage 2)')]
newr = [r for r in F11R if r not in known]
q('QF62_known', 'Unique works already in the corpus or in an earlier screening record', len(known), len(F11R), 'Unique works of the final search', SRC11)
q('QF62_known_corpus', 'Unique works already in the corpus', sum(1 for r in F11R if r['project_status'] == 'in corpus'), len(F11R), 'Unique works of the final search', SRC11)
q('QF62_new', 'Unique works new to the project', len(newr), len(F11R), 'Unique works of the final search', SRC11)
q('QF62_excluded', 'New works excluded', sum(1 for r in newr if r['decision'] == 'EXCLUDE'), len(newr), 'New works of the final search', SRC11)
q('QF62_ft', 'New works assessed in full text (open access or full text supplied by the authors)', sum(1 for r in newr if r['level'] == 'full text'), len(newr), 'New works of the final search', SRC11)
q('QF62_unresolved', 'New works that appear to meet, or cannot be decided against, the criteria on title and abstract but whose full text was not accessible (not coded)', sum(1 for r in newr if r['decision'].startswith('UNRESOLVED')), len(newr), 'New works of the final search', SRC11,
  ids=[r['title'] for r in newr if r['decision'].startswith('UNRESOLVED')])
q('QF62_added', 'New works added to the corpus by the final coverage search', sum(1 for r in newr if r['decision'] == 'INCLUDE'), len(newr), 'New works of the final search', SRC11)
dirids = {d['id'] for d in D}
hit = ({r['reason'].split(': ', 1)[1] for r in F11R if r['project_status'] == 'in corpus'} | {re.search(r'Corpus entry (\S+)', r['reason']).group(1) for r in F11R if r['decision'] == 'INCLUDE'}) & dirids
q('QF62_recall', 'Direct papers identified by the final coverage search (re-identified corpus papers plus the papers it added)', len(hit), nD, DIRP, SRC11, 'The missed papers are arXiv-only preprints', ids=sorted(dirids - hit))
MS = [m for m in M if m['id'] in (dirids - hit)]
q('QF62_missed_C', 'Direct papers missed by the final coverage search that are preprints (class C, arXiv only)', sum(1 for m in MS if m['ext_status_class'].startswith('C')), len(MS), 'Direct papers missed by the final coverage search', SRC11, ids=[m['id'] for m in MS])
json.dump(QF, open(os.path.join(ROOT, '10_PreWriting', 'quantitative_findings.json'), 'w'), indent=1)
out = ['# Quantitative Findings (Stage 4; QF44-QF49 added in Stage 7; pre-FM comparison set and QF50-QF57 added in Stage 9)', '', f'Generated by `10_PreWriting/build_findings.py` from the final matrices (Stage-3 taxonomy). Corpus cut-off **{CUT}**. **Only numbers listed here may be used in the manuscript.** Percentages are numerator/denominator; multi-label axes are non-exclusive.', '',
       '| ID | Statement | Num | Den | % | Population | Source | Caveat |', '|---|---|---|---|---|---|---|---|']
for f in QF: out.append(f"| {f['id']} | {f['statement']} | {f['numerator']} | {f['denominator']} | {f['percentage']} | {f['population']} | {f['source']} | {f['caveat']} |")
out += ['', f'**Total findings: {len(QF)}.** Paper lists for findings with `ids` are in `quantitative_findings.json`.']
open(os.path.join(ROOT, '10_PreWriting', 'QUANTITATIVE_FINDINGS.md'), 'w').write('\n'.join(out) + '\n')
print(len(QF))

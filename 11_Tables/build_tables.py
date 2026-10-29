"""Stage 4: populate all main (T1-T10) and supplementary (S1-S4) tables from the frozen final matrices.
Counts are computed from 07_Literature_Analysis CSVs; short analytical text cells (planner, contribution, limitation, failure modes,
roadmap) are curated below from the notes and Stage-3 reports and are traceable to the paper notes. Run: python3 11_Tables/build_tables.py"""
import csv, json, os, re, collections, glob, yaml
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); A = os.path.join(ROOT, '07_Literature_Analysis'); OUT = os.path.join(ROOT, '11_Tables')
def rd(n): return list(csv.DictReader(open(os.path.join(A, n))))
M = {m['id']: m for m in rd('master_literature_matrix.csv')}; D = rd('direct_vlm_social_navigation_matrix.csv'); DI = {d['id']: d for d in D}
CAP = {r['id']: r for r in rd('social_capabilities_matrix.csv')}; MET = rd('evaluation_metrics_matrix.csv'); DEP = {r['id']: r for r in rd('deployment_runtime_matrix.csv')}
REP = {r['id']: r for r in rd('reproducibility_matrix.csv')}; SUR = rd('existing_surveys_matrix.csv'); DS = rd('datasets_benchmarks_matrix.csv'); ADJ = rd('adjacent_foundation_model_matrix.csv')
KEYS = {v: k for k, v in json.load(open(os.path.join(ROOT, '13_References', 'citation_keys.json'))).items()}
NOTES = {}
for f in glob.glob(os.path.join(ROOT, '08_Paper_Notes', '*.md')):
    y = yaml.safe_load(open(f).read().split('---', 2)[1]); NOTES[y['id']] = y
L = lambda v: [x.strip() for x in str(v).split(';') if x.strip() and x.strip() != 'NA']
def cut(t, n):
    t = str(t)
    if len(t) <= n: return t
    t = t[:n].rsplit(' ', 1)[0].rstrip(' ,;:(') 
    return t + '…'
def short(i): return re.sub(r'^\d{4}_[^_]+_', '', i).replace('-', ' ')
def cite(i): return KEYS.get(i, i)
def write(name, cols, rows, title, notes=''):
    with open(os.path.join(OUT, name + '.csv'), 'w', newline='') as f:
        w = csv.writer(f); w.writerow(cols); w.writerows(rows)
    md = [f'# {title}', '', notes, '', '| ' + ' | '.join(cols) + ' |', '|' + '---|' * len(cols)]
    md += ['| ' + ' | '.join(str(c).replace('|', '/').replace('\n', ' ') for c in r) + ' |' for r in rows]
    open(os.path.join(OUT, name + '.md'), 'w').write('\n'.join(md) + '\n'); return len(rows)
LEGACY_MAP = {'F10': 'D6', 'F11': 'evaluator', 'F1': 'R1', 'F2': 'R2', 'F3': 'R2', 'F4': 'R3', 'F5': 'D2', 'F6': 'D3', 'F7': 'R4', 'F8': 'D7', 'F9': 'D4',
              'I1': 'D0', 'I2': 'D1', 'I3': 'D2', 'I4': 'D3', 'I5': 'D4', 'I6': 'D5/D7', 'I7': 'D6', 'C25': 'NOR4', 'C24': 'NOR3', 'C23': 'NOR2', 'C4': 'EXP1', 'C3': 'SPA1', 'C1': 'SAF1'}
def final_terms(t):
    """Translate legacy Stage-1 codes inside curated text cells into final Stage-3 codes."""
    t = re.sub(r'\b(F1[01]|F[1-9]|I[1-7]|C2[3-5]|C[134])\b', lambda m: LEGACY_MAP[m.group(1)], str(t))
    return re.sub(r'\b([A-Z]+\d)(?:[/,] ?\1\b)+', r'\1', t)
SIZES = {}
QF = {q['id']: q for q in json.load(open(os.path.join(ROOT, '10_PreWriting', 'quantitative_findings.json')))}
def qf(k): q = QF[k]; return f"{q['numerator']}/{q['denominator']}"
nD = len(D)
def dn(pred): return f"{sum(1 for d in D if pred(d))}/{nD}"
STATUS = {'A': 'published', 'B': 'accepted (not yet indexed)', 'C': 'preprint', 'D': 'acceptance verified; review not established'}
def status(i): return STATUS.get(str(M[i]['ext_status_class'])[:1], '?')
# ===================== T1 existing surveys =====================
T1 = [  # survey id, classical, learning, FM, direct VLM-SRN, repr evolution, role taxonomy, capability taxonomy, interface taxonomy, evidence analysis, eval audit, deployment/reliability, human-study analysis, cut-off
 ('2013_Kruse_Human-Aware-Navigation-Survey', 'Yes', 'No', 'No', 'No', 'Partial', 'Not applicable', 'Partial', 'Not applicable', 'No', 'Partial', 'No', 'Partial', '~2013'),
 ('2017_Charalampous_Social-Aware-Navigation-Survey', 'Yes', 'No', 'No', 'No', 'Partial', 'Not applicable', 'No', 'Not applicable', 'No', 'No', 'No', 'Partial', '2016'),
 ('2021_Moller_Human-Aware-Navigation-Survey', 'Yes', 'Yes', 'No', 'No', 'Partial', 'Not applicable', 'No', 'Not applicable', 'No', 'Partial', 'No', 'No', '2021'),
 ('2022_Gao_Evaluation-SAN-Review', 'Yes', 'Yes', 'No', 'No', 'No', 'Not applicable', 'Partial', 'Not applicable', 'Partial', 'Yes', 'No', 'Yes', '2021'),
 ('2023_Mavrogiannis_Core-Challenges-Survey', 'Yes', 'Yes', 'No', 'No', 'Partial', 'Not applicable', 'Partial', 'Not applicable', 'No', 'Partial', 'No', 'Partial', '2022'),
 ('2024_Mirsky_Conflict-Avoidance-Survey', 'Yes', 'Yes', 'No', 'No', 'No', 'Not applicable', 'Partial', 'Not applicable', 'Partial', 'Yes', 'No', 'Partial', '~2023'),
 ('2024_Singamaneni_SAN-Taxonomy-Survey', 'Yes', 'Yes', 'No', 'No', 'No', 'Not applicable', 'Partial', 'Not applicable', 'No', 'Partial', 'No', 'Partial', '2023'),
 ('2024_Karwowski_Requirements-Planning-Evaluation-Review', 'Yes', 'Yes', 'No', 'No', 'No', 'Not applicable', 'Yes', 'Not applicable', 'No', 'Yes', 'No', 'Yes', '2024'),
 ('2025_Francis_Principles-Guidelines', 'Yes', 'Yes', 'No', 'No', 'No', 'Not applicable', 'Yes', 'Not applicable', 'No', 'Yes', 'No', 'Yes', '~2024'),
 ('2025_Alyassi_Learning-SocialNav-Review-Benchmark', 'Partial', 'Yes', 'Partial', 'Partial', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', '2025'),
 ('2026_Kabir_DRL-SAN-Survey', 'Partial', 'Yes', 'Partial', 'Partial', 'No', 'No', 'Partial', 'No', 'No', 'Partial', 'No', 'No', '~2025'),
 ('2026_Pan_Foundation-LM-Navigation-Review', 'Partial', 'Partial', 'Yes', 'No', 'No', 'Partial', 'No', 'Partial', 'No', 'Partial', 'Partial', 'No', 'early 2026'),
 ('2026_Cai_VLM-Deployable-SRN-Survey', 'Partial', 'Partial', 'Yes', 'Yes', 'No', 'Partial', 'No', 'Yes', 'Partial', 'Partial', 'Partial', 'Partial', '27 Jun 2026'),  # evidence: 'explicitly annotating each paradigm with its level of supporting evidence'; human-centred outcomes (comfort, perceived safety, legibility, acceptance) discussed for evaluation (re-read 2026-10-21)
]
ov = {s['id']: re.match(r'(\d+)', s['s2_direct_overlap_with_our_survey']).group(1) for s in SUR}
cols = ['Survey', 'Cite key', 'Year', 'Classical / proxemic', 'Learning / DRL', 'Foundation models', 'Direct VLM social nav.', 'Evolution of social representation', 'FM role taxonomy',
        'Social-capability taxonomy', 'Navigation-interface taxonomy', 'Evidence-profile analysis', 'Evaluation audit', 'Deployment / reliability', 'Human-study analysis', 'Literature cut-off', 'Direct papers cited']
rows = [[short(r[0]).replace(' Survey', '').replace(' Review', ''), cite(r[0]), M[r[0]]['year']] + list(r[1:]) + [ov[r[0]]] for r in T1]
rows.append(['This survey', '-', '2026', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', '19 Oct 2026', str(nD)])
SIZES['T1'] = write('T1_existing_surveys', cols, rows, 'T1 - Existing surveys vs analytical dimensions of this survey',
    'Coding: **Yes** = covered substantively; **Partial** = covered incidentally, qualitatively or without per-paper analysis; **No** = not covered; **Not applicable** = the survey predates foundation models, so an FM-specific taxonomy cannot apply. Source: `existing_surveys_matrix.csv` (`s2_*`, `cov_*`) and FINAL_SURVEY_POSITIONING.md. Direct papers cited = lower bound (title/arXiv-id match + manual).')
# ===================== T2 evolution =====================
EVO = [
 ('Geometric collision avoidance', '2008 -> (background)', 'Moving obstacle (disc, velocity)', 'Geometry / reciprocity assumptions', 'Velocity-obstacle optimisation', 'ORCA/RVO (background); CADRL as learned counterpart', 'Collision-free reciprocal motion under its reciprocity assumption', 'Clearance only; social meaning of proximity not explicitly represented', '', 'Persists as crowd simulator and baseline'),
 ('Proxemics / spatial theory', '1966 -> (background)', 'Point with distance zones (A3)', 'Social science (Hall)', 'Costs/constraints around people', 'Hall (background); Kim 2022 group spaces', 'Explicit comfort distances (SPA1)', 'Static zones; context and intent not explicitly represented', '', 'Thresholds still define FM metrics (PSV, PSC)'),
 ('Social force / rule models', '1995 ->', 'Agent with desired velocity, anisotropic repulsion, group attraction (A1, A3, A4)', 'Hand-tuned physical analogy', 'Force integration / reactive control', cite('1995_Helbing_Social-Force'), 'Crowd-flow phenomena; simulation', 'Hand-tuned parameters; semantic context not explicit', '', 'SFM is fast loop / simulator in FM systems (LISN, PAD)'),
 ('Prediction-coupled planning', '2010 ->', 'Trajectory distribution with interaction potentials (A2, A4)', 'Probabilistic models fitted to data', 'Joint inference over predicted futures', cite('2010_Trautman_Unfreezing-IGP'), 'Interaction-aware motion; avoids freezing (HUM1, SPA4)', 'Computational cost; evaluation on replayed data; norms not explicitly modelled', '', 'Prediction modules feed FM systems (Etiquette, HCSG)'),
 ('Inverse RL / imitation', '2012 ->', 'Feature-based trajectories: clearance, passing side, groups (A2, A4)', 'Human demonstrations', 'Planning under learned cost', ', '.join(cite(i) for i in ['2012_Kuderer_Feature-Based-Prediction', '2016_Kretzschmar_Socially-Compliant-IRL', '2016_Okal_Bayesian-IRL', '2018_Tai_GAIL-Depth']), 'Learned passing / group conventions (SPA2, SPA3); naturalness (EXP3)', 'Hand-designed features; small demonstration sets', '', 'Preference learning reappears with LLM feedback (PREDILECT)'),
 ('Deep RL crowd navigation', '2017 ->', 'Disc agents with attention over agents (A1, A4)', 'Reward design + crowd simulation', 'Learned value / policy', ', '.join(cite(i) for i in ['2017_Chen_CADRL', '2017_Chen_SA-CADRL', '2019_Chen_SARL-CrowdNav']), 'Real-time crowd navigation; norm-shaped rewards', 'Reward exploitation in simulation; sim-to-real transfer; semantic context not explicit', '', 'DRL policies trained or conditioned by FMs (EvoNav, HUMA, SALM)'),
 ('Graph / attention / preference learning', '2019 -> 2024', 'Spatio-temporal graphs, embeddings (A1, A4, A6)', 'Data + human preference feedback', 'Learned / hybrid policies', ', '.join(cite(i) for i in ['2023_Wang_NaviSTAR', '2024_Raj_Hybrid-Social-Nav']), 'Human preference feedback in training; human evaluation of learned policies (EV5)', 'Geometric representations; context and instructions not explicitly represented', '', 'Coexists with FM work'),
 ('Language-conditioned / FM navigation (adjacent)', '2022 ->', f"Mostly absent (A0 in {qf('QF07')})", 'Web-scale pretraining', 'LLM planning, value maps, navigation FMs, VLAs', ', '.join(cite(i) for i in ['2022_Shah_LM-Nav', '2023_Huang_VLMaps', '2023_Shah_ViNT', '2024_Yokoyama_VLFM', '2023_Brohan_RT-2']), 'Open-vocabulary grounding; instruction following', 'No social objective; humans largely absent', '', 'Supplies backbones and interfaces (CLIP, VLA, value maps)'),
 ('VLM/LLM social reasoning over classical stacks', '2024 ->', f"Language descriptions + tracks (A5 {qf('QF06_A5_direct')}, A1 {qf('QF06_A1_direct')})", 'Pretrained priors + prompts + fine-tuning (SNEI, MUSON)', 'FM selects / shapes / sets goals; classical planner executes (D2-D4) or offline decision (D0)', ', '.join(cite(i) for i in ['2025_Song_VLM-Social-Nav', '2024_Sathyamoorthy_CoNVOI', '2025_Luo_GSON', '2026_Chen_LISN', '2026_Liao_G2-Nav', '2025_Payandeh_Social-LLaVA']), f"Context-dependent conduct (NOR3 {qf('QF15_NOR3_direct')}); instruction following (NOR2 {qf('QF15_NOR2_direct')}); explanation (R5)", f"Seconds-scale latency reported in several systems; cloud dependence; {qf('QF10a')} never coupled to motion; little human evaluation", '', 'Most frequent pattern in the corpus'),
 ('Distilled, latent and VLA social navigation', '2025 ->', f"Implicit latents (A6 {qf('QF06_A6_direct')})", 'FM as teacher or backbone; IL/RL post-training', 'Training-time supervision (D7), latent conditioning (D5), direct action (D6)', ', '.join(cite(i) for i in ['2026_Payandeh_Narrate2Nav', '2026_Elnoor_ViLAM', '2026_Ahmadi_HUMA', '2026_Hu_SPARK-VLN', '2026_Chen_SocialNav-CVPR', '2026_Wang_SALSA']), 'Real-time execution without per-step FM calls; end-to-end social VLAs', f"Limited interpretability; FM-independent safety in {qf('QF12')} D6 systems; D6 robot evidence {qf('QF11_D6')}", '', 'Newest; overlaps with the preceding paradigm'),
]
EVO = sorted(EVO, key=lambda r: int(r[1][:4]))          # chronological by first appearance; no 'transition pressure' column (avoids implied causality)
SIZES['T2'] = write('T2_evolution_social_intelligence', ['Paradigm', 'Era (first appearance)', 'Human representation (Axis A)', 'Source of social knowledge', 'Behaviour generation', 'Representative methods (cite keys)', 'Main capability gained', 'Main limitation noted in the literature', 'Coexistence'], [list(r[:8]) + [r[9]] for r in EVO],
    'T2 - Evolution of social intelligence in robot navigation',
    'Paradigms overlap; the "Coexistence" column records how each persists inside later systems. Rows marked background cite works outside the coded corpus (see 13_References, background entries). Counts from `final_*` columns (direct n = ' + str(nD) + '). Source: EVOLUTIONARY_NARRATIVE.md.')
# ===================== T3 pre-FM comparison set (Stage 9) =====================
LEAF = ['SAF1', 'SAF2', 'SPA1', 'SPA2', 'SPA3', 'SPA4', 'HUM1', 'HUM2', 'NOR1', 'NOR2', 'NOR3', 'NOR4', 'EXP1', 'EXP2', 'EXP3']
EVM = {r['id']: r for r in rd('evidence_maturity_matrix.csv')}
PCS3 = list(csv.DictReader(open(os.path.join(A, 'prefm_comparison_set.csv'))))
rows = []
for p in sorted({r['paradigm'] for r in PCS3}, key=lambda s: int(s.split()[0][1:])):
    g = sorted([r for r in PCS3 if r['paradigm'] == p], key=lambda r: int(r['year']))
    ac = collections.Counter(a for r in g for a in r['A'].split()); ev = collections.Counter(l for r in g for l in r['cap_yes'].split())
    rob = sum(1 for r in g if r['EV3_physical_robot'] == 'systematic'); hum = sum(1 for r in g if r['EV5_human_evaluation'] not in ('none', 'text-raters', 'ND'))
    nd = sum(1 for r in g if 'ND' in (r['EV3_physical_robot'], r['EV5_human_evaluation']))
    rows.append([p.split(' ', 1)[1], f"{len(g)} ({sum(1 for r in g if r['coding_source'].startswith('full text'))})", ', '.join(r['bib_key'] for r in g),
                 ' '.join(f'{a}:{ac[a]}' for a in sorted(ac)), ' '.join(f'{l}:{ev[l]}' for l in LEAF if ev[l]) or '-', str(rob), str(hum) + (f' ({nd} ND)' if nd else '')])
SIZES['T3'] = write('T3_prefm_baselines', ['Paradigm', 'Works (full text)', 'Works (cite keys)', 'Human representation (A: works)', 'Evaluated capabilities (leaf: works)', 'Systematic real robot', 'Human evaluation of behaviour'], rows,
    'T3 - Pre-FM comparison set by paradigm',
    f'Source: `07_Literature_Analysis/prefm_comparison_set.csv` ({len(PCS3)} works: the 12 coded corpus works plus exemplars cited by >= 3 of 7 reference surveys, topped up to 3 works per paradigm; selection in PREFM_BASELINE_JUSTIFICATION.md). Representative, not exhaustive. ND = not determinable from legitimately accessible sources (coded from reference-survey descriptions).')
# ===================== T4 / T5 direct tables =====================
PLAN = {
 '2024_Holk_PREDILECT': ('RL policy (SAC/PPO) + SFM repulsion', 'LLM turns free-text preference explanations into reward features', 'Simulation only; LLM limited to text parsing'),
 '2024_Sathyamoorthy_CoNVOI': ('Modified DWA', 'VLM reference paths encoding context-dependent behaviours', 'Evaluation mostly terrain/crosswalk context'),
 '2024_Wang_SALM': ('Fusion with DRL policy (LLM feedback scorer)', 'LLM and DRL navigation commands fused by an LLM feedback model', 'Simulation only; cloud LLM in control loop'),
 '2024_Yu_PANav': ('A* candidate paths', 'VLM selects the privacy-minimising path', 'No humans in quantitative evaluation'),
 '2025_Kawabata_SocialNav-MoE': ('None', 'Small MoE VLM with RL fine-tuning for social actions', 'Offline text similarity only'),
 '2025_Kong_AutoSpatial': ('None', 'Structured spatial grounding for social VLM reasoning', 'Offline; LLM/human scoring of text'),
 '2025_Liang_MOSU': ('CVAE candidates + motion planner', 'VLM ranks outdoor trajectories by social cues', 'No social metric; robot runs unquantified'),
 '2025_Luo_GSON': ('A* + BIT* re-planning + NMPC-CBF', 'LMM group inference defines social spaces', 'No human evaluation; 3 runs per scenario'),
 '2025_Martinez-Baselga_Hey-Robot': ('MPC with collision constraints', 'LLM writes and tunes MPC costs from user requests', 'Keep-distance request not fully met; lab demo'),
 '2025_Narasimhan_OLiVia-Nav': ('Learned trajectory planner + selector, PID', 'Distilled VLM context embeddings condition a learned planner', 'No safety layer; 4x3 trials'),
 '2025_Payandeh_Social-LLaVA': ('None (hard-coded demo mapping)', 'SNEI dataset; perception-to-action social VLM reasoning', 'Offline VQA; single robot demo'),
 '2025_Saito_VLM-Crowd-Mapping': ('Dijkstra on fused cost map', 'VLM crowd labels become a GPR crowd-density map', 'Two qualitative trials'),
 '2025_Song_VLM-Social-Nav': ('DWA', 'VLM output converted into a social cost term', 'Small user study; no statistics'),
 '2025_Sotomi_Transparent-Social-Nav-VLM': ('ROS2 re-planning (mechanism unspecified)', 'VLM explanations of social re-planning for trust', '4 runs; ~20 s explanation latency'),
 '2025_Wang_SAMALM': ('None (direct velocities)', 'Multi-agent LLM actors with local/global critics', 'Simulation only'),
 '2025_Weerakoon_BehAV': ('MPC on behavioural cost map', 'Language rules grounded into behaviour cost maps', 'Most rules concern terrain/objects'),
 '2025_Wen_HSAC-LLM': ('DRL policy (HSAC)', 'LLM speech for robot-pedestrian passage negotiation', 'Simulated training pedestrians respond to requests; demo only'),
 '2026_Ahmadi_HUMA': ('RL policy (Falcon)', 'Proximity-triggered VLM reasoning conditions an RL policy', 'High human-collision rate; robot demo only'),
 '2026_Bejarano_PAD': ('Global planner + SFM/DWA', 'VLM/LLM awareness map chooses dialogue vs re-planning', 'n = 8, no statistics; FMs unnamed'),
 '2026_Chen_LISN': ('SFM controller + social costmap', 'Slow VLM modulates a fast social-force controller; LISN-Bench', 'Simulation only; ~7 s VLM latency'),
 '2026_Chen_SocialNav-CVPR': ('Flow-matching action expert + locomotion policy', 'VLA-style social-navigation FM with SocNav benchmark', 'No safety layer; success-rate-only real trials'),
 '2026_Elnoor_ViLAM': ('DWA-style planner with distilled attention cost', 'Distils VLM crowd reasoning into attention maps', 'FM used offline only; no human evaluation'),
 '2026_Fang_Group-Joining': ('Local planner to predicted goal', 'Language-guided, F-formation-aware group joining', 'Small trial counts; no member ratings'),
 '2026_Fang_Obstacles-to-Etiquette': ('Modified ORCA for pedestrian avoidance along selected path', 'Fine-tuned VLM selects the socially compliant candidate path', '3 trials per method; staged actors'),
 '2026_Hu_SPARK-VLN': ('Flow-matching planner', 'Token-wise VLM latent streaming against stale observations', 'Simulation only; ~29% human-collision rate'),
 '2026_Huo_NORM-Nav': ('A* + TEB on multi-layer costmaps', 'Language norms parsed into costmap constraints', 'Pedestrian behaviour only qualitative'),
 '2026_Liao_G2-Nav': ('Gradient trajectory optimisation + pure pursuit', 'Grounded VLM costmaps with LiDAR reflex safety layer', '6 trials per method; no human study'),
 '2026_Park_TACET': ('Social costmap + quiet-locomotion RL policy', 'VLM behaviour tokens for context-appropriate gait and noise', 'Video raters only (N = 15)'),
 '2026_Payandeh_Narrate2Nav': ('Student policy + pure pursuit', 'VLM narrations distilled into an RGB-only student', 'Crowd scenario not among real-world tests'),
 '2026_Sethuraman_Context-Aware-Preferences': ('Preference-conditioned MORL policy', 'VLM/LLM translate context and rules into MORL weights', 'Humans rated text, not robot behaviour'),
 '2026_Wang_LE-Nav': ('TEB/DWA with generated hyperparameters', 'MLLM scene text conditions CVAE planner tuning', 'No statistics reported for user study'),
 '2026_Wang_MAction-SocialNav': ('None', 'Small VLM ranking multiple acceptable actions', 'Offline; 79 test samples'),
 '2026_Wang_SALSA': ('None (VLA actions)', 'Social-safety post-training of a navigation VLA', 'Quantitative results offline only'),
 '2026_Xiao_E-SocialNav': ('None', 'Efficient small VLM via SFT + DPO', 'Offline; 60 test samples'),
 '2026_Xiao_Prompting-VLMs-JSAI': ('None', 'Prompt-design study for small VLMs', 'Offline; peer review not established'),
 '2026_Xu_HCSG': ('Learned graph-transformer waypoint selection', 'VLM human-activity descriptions in a topological VLN map', 'No safety layer; no human study'),
 '2026_Zhang_GCL': ('None', 'Competitive co-distillation of small VLMs', 'Offline; no robot experiments'),
 '2026_Zhang_SAATT-Nav': ('Rollout-based selection in 2D planner', 'LLM pedestrian-intent hypotheses + rider explanations', 'Custom 2D simulation; LLM unnamed'),
 '2026_Zhang_SOPD-SocialNav': ('None (qualitative robot demo)', 'Selective on-policy distillation of a social VLM', 'Offline; robot only qualitative'),
 '2026_Zhang_Walk-With-Me': ('Low-level VLA on remote server', 'VLM-VLA hierarchy for human-accompanying outdoor navigation', '60% success; no latency reported'),
 '2026_Zhao_EvoNav': ('DRL policy (CrowdNav++)', 'LLM evolves social reward code', 'ORCA-only humans; no real robot'),
 '2026_Zhang_AHead-VLN': ('Waypoint candidates; LLM-written discrete action scripts', 'Forecast human-risk events compiled for hierarchical LLM path choice', 'Simulation only; collisions in 44% of episodes; cloud LLMs'),
 '2025_Ruo_LLM-Social-Cues': ('CBF quadratic-program controller', 'Local LLM sets navigation mode, speed bound and social-zone distance from user cues', 'Simulation only; no baselines; positions assumed known'),
 '2026_Gandotra_RBTLR': ('RRT-Connect candidates + learned selector', 'CLIP/Qwen social context conditions path selection; LLM goal assignment', 'Early-stage; demonstration only; no social metrics'),
 '2026_Oush_VLA-TurtleBot': ('Motion controller behind a LiDAR safety layer', 'LLM picks proceed, yield, avoid or stop when a person is detected', 'Simulation only; single simulated person; LLM not named'),
}
assert set(PLAN) == set(DI), set(PLAN) ^ set(DI)
def inputs(i):
    t = ' '.join(map(str, NOTES[i].get('inputs') or [])).lower(); out = []
    for k, lab in [(r'rgb-d|depth', 'RGB-D'), (r'\brgb|image|camera|egocentric|fisheye|panoramic', 'RGB'), (r'lidar|point cloud|scan', 'LiDAR'), (r'language|instruction|prompt|quer|speech|text|rules', 'Language'), (r'track|position|state|pedestrian grid', 'Tracks/states'), (r'goal', 'Goal')]:
        if re.search(k, t) and lab not in out: out.append(lab)
    if 'RGB-D' in out and 'RGB' in out: out.remove('RGB')
    return ', '.join(out)
def fmtype(i):
    c = ' '.join(map(str, NOTES[i].get('fm_class') or [])); m = '; '.join(map(str, NOTES[i].get('fm_models') or []))
    m = re.sub(r'\s*\(.*?\)', '', m)[:70]
    return f'{c} - {m}'
def okey(d):
    s_ = set(L(d['final_D_interface'])); rt = sorted(int(x[1]) for x in s_ if x in ('D1', 'D2', 'D3', 'D4', 'D5', 'D6'))
    return (rt[0] if rt else (7 if 'D0' in s_ else (8 if 'D7' in s_ else 9)), d['year'], d['id'])
ORDER = sorted(D, key=okey)
XC = lambda d: ' '.join(s for s, c in [('async', d['final_xc_temporal_coupling'] in ('asynchronous', 'event-triggered', 'hierarchical')), ('memory', d['final_xc_memory'] != 'No'),
                                        ('explanation', d['final_xc_explanation_output'].startswith('Yes (human')), ('cloud', d['final_xc_inference_location'] in ('cloud API', 'hybrid (local + cloud)', 'remote server'))] if c) or '-'
rowsA = [[d['year'], short(d['id']), cite(d['id']), status(d['id']), fmtype(d['id']), inputs(d['id']), d['final_A_social_representation'], d['final_B_roles'], d['final_D_interface'],
          PLAN[d['id']][0], d['final_xc_temporal_coupling'], d['final_xc_safety_guard'], XC(d), PLAN[d['id']][1]] for d in ORDER]
SIZES['T4'] = write('T4_direct_architecture', ['Year', 'Paper', 'Cite key', 'Status', 'FM type - models', 'Inputs', 'Human representation (A)', 'FM role (B)', 'Interface (D)', 'Planner / controller', 'Temporal coupling', 'FM-independent safety guard', 'Other attributes', 'Main contribution'], rowsA,
    'T4 - Direct FM social-navigation methods: architecture (Table A)',
    'Rows ordered by primary runtime interface (D1-D6), then D0 (non-executed), D7-only (training-time), D8-only (human-facing); ' + str(nD) + ' papers. Codes: A0-A6 representation, R1-R5 role, D0-D8 interface (categorical, not a ranking); definitions in FINAL_SURVEY_TAXONOMY.md. Status: published / accepted (not yet indexed) / preprint / acceptance verified, review not established.')
def socmet(i):
    ms = [m['metric_name'] for m in MET if m['id'] == i and m['metric_category'] in ('SOCIAL', 'SAFETY', 'HUMAN')]
    return cut('; '.join(dict.fromkeys(ms)), 120) or '-'
def lat(i): return cut(re.sub(r'\s+', ' ', str(DEP[i].get('latency', ''))), 80)
fam = {'SAF': LEAF[0:2], 'SPA': LEAF[2:6], 'HUM': LEAF[6:8], 'NOR': LEAF[8:12], 'EXP': LEAF[12:15]}
rowsB = []
for d in ORDER:
    i = d['id']; c = CAP[i]
    yes = ' '.join(l for l in LEAF if c['final_' + l] == 'Yes') or '-'
    part = ' '.join(f for f, ls in fam.items() if any(c['final_' + l] == 'Partial' for l in ls) and not any(c['final_' + l] == 'Yes' for l in ls)) or '-'
    code = REP[i]['coding_code_released']; data = REP[i]['coding_new_dataset_released']
    rowsB.append([short(i), yes, part, d['final_EV1_offline'], d['final_EV2_closed_loop_sim'], d['final_EV3_physical_robot'], d['final_EV4_real_humans_in_trials'], d['final_EV5_human_evaluation'],
                  d['final_EV6_open_world_deployment'], cut(d['final_quality_trials'], 45), 'Yes' if str(d['final_quality_statistical_testing']).startswith('Yes') else 'No', socmet(i), lat(i),
                  d['final_xc_uncertainty'], d['final_xc_hallucination_mitigation'], f'code {code}; data {data}', PLAN[i][2]])
SIZES['T5'] = write('T5_direct_evidence', ['Paper', 'Evaluated capabilities (Yes leaves)', 'Addressed-only families (Partial)', 'EV1 offline', 'EV2 closed-loop sim', 'EV3 physical robot', 'EV4 real humans in trials', 'EV5 human evaluation', 'EV6 open-world',
                                          'Trials (as reported)', 'Statistics', 'Key social / safety / human metrics', 'Runtime reported', 'Uncertainty', 'Hallucination mitigation', 'Code / data', 'Key limitation'], rowsB,
    'T5 - Direct FM social-navigation methods: capability and evidence (Table B)',
    'Same row order as T4. Yes = evaluated with a dedicated measure; Partial = addressed qualitatively, by proxy, or offline only. EV dimensions are independent (no ranking). Metric names are as printed by each paper and are not comparable across papers (see T8).')
# ===================== T6 capability coverage =====================
PRE = [i for i, m in M.items() if m['analytical_category'] in ('S1', 'S2')]; S6 = [i for i, m in M.items() if m['analytical_category'] == 'S6']
NAMES = {'SAF1': 'Collision avoidance', 'SAF2': 'Near-collision / risk margin', 'SPA1': 'Personal space', 'SPA2': 'Group / conversation space', 'SPA3': 'Encounter conventions', 'SPA4': 'Crowd navigation',
         'HUM1': 'Motion understanding / prediction', 'HUM2': 'Intention / activity inference', 'NOR1': 'Etiquette / politeness', 'NOR2': 'Explicit social-instruction following', 'NOR3': 'Context-dependent conduct',
         'NOR4': 'Cultural / norm adaptation', 'EXP1': 'Perceived safety / comfort', 'EXP2': 'Legibility / predictability', 'EXP3': 'Naturalness'}
PCS = list(csv.DictReader(open(os.path.join(A, 'prefm_comparison_set.csv')))); nC = len(PCS)
for r in PCS: r['_Y'] = set(r['cap_yes'].split())
rows = []
for f, ls in fam.items():
    rows.append([f'**{f} family**', '', f"{sum(1 for d in D if any(CAP[d['id']]['final_'+l]=='Yes' for l in ls))}/{nD}", f"{sum(1 for d in D if any(CAP[d['id']]['final_'+l] in ('Yes','Partial') for l in ls))}/{nD}",
                 f"{sum(1 for r in PCS if r['_Y'] & set(ls))}/{nC}", f"{sum(1 for i in S6 if any(CAP.get(i, {}).get('final_'+l)=='Yes' for l in ls))}/15", ''])
    for l in ls:
        ex = [cite(d['id']) for d in D if CAP[d['id']]['final_' + l] == 'Yes'][:4]
        rows.append([l, NAMES[l], f"{sum(1 for d in D if CAP[d['id']]['final_'+l]=='Yes')}/{nD}", f"{sum(1 for d in D if CAP[d['id']]['final_'+l] in ('Yes','Partial'))}/{nD}",
                     f"{sum(1 for r in PCS if l in r['_Y'])}/{nC}", f"{sum(1 for i in S6 if CAP.get(i, {}).get('final_'+l)=='Yes')}/15", ', '.join(ex) or '-'])
SIZES['T6'] = write('T6_capability_coverage', ['Code', 'Capability', 'Direct: evaluated (Yes)', 'Direct: addressed (Yes or Partial)', f'Pre-FM comparison set: evaluated (n = {nC})', 'Datasets / benchmarks: evaluated (n = 15)', 'Example direct papers (Yes)'], rows,
    'T6 - Social-capability coverage by paradigm', 'Family rows count papers with at least one leaf at that level. Source: `social_capabilities_matrix.csv` `final_*` and `prefm_comparison_set.csv` (representative, survey-selected pre-FM sample; descriptive only).')
# ===================== T7 datasets / benchmarks =====================
FMROLE = {'2024_Li_HA-VLN': 'FM generates instructions/scenes', '2026_Dong_HA-VLN-2.0': 'LLM generates instructions', '2026_Liu_MUSON': 'GPT annotation (initial)', '2025_Munje_SocialNav-SUB': 'VLMs evaluated (benchmark of VLM scene understanding)',
          '2024_Marpally_SocRATES': 'LLM generates test scenarios', '2025_Zhang_FewShot-Perception': 'LLM predicts human ratings (judge)', '2026_Huang_SONG': 'LLM generates pedestrian intents', '2026_Dai_DPed-VLN': 'VLM generates instructions',
          '2024_Shcherbyna_Arena-4.0': 'LLM-generated worlds (unnamed)', '2025_Payandeh_Social-LLaVA': 'Human-annotated VQA for VLM fine-tuning'}
DSI = {r['id']: r for r in DS}
dsrows = []
for i in sorted(set(S6) | {'2025_Payandeh_Social-LLaVA'}, key=lambda i: (M[i]['year'], i)):
    r = DSI.get(i, {}); nm = 'SNEI (via Social-LLaVA)' if i == '2025_Payandeh_Social-LLaVA' else short(i)
    size = r.get('ds_size', '')
    if i == '2025_Payandeh_Social-LLaVA': size = 'See note [a]: ~2K scenarios; 1,961 images (paper Table II); >40K QA; public release 1,508 rows'
    dsrows.append([nm, cite(i), M[i]['year'], r.get('ds_kind', ''), r.get('ds_real_synthetic', ''), cut(size, 110), cut(r.get('ds_sensors', ''), 60), cut(r.get('ds_dynamic_humans', ''), 30), cut(r.get('ds_human_trajectories', ''), 30),
                   '; '.join(x for x in [('group: ' + cut(r.get('ds_group_ann', ''), 20)) if r.get('ds_group_ann') else '', ('intent: ' + cut(r.get('ds_intention_ann', ''), 20)) if r.get('ds_intention_ann') else ''] if x)[:60],
                   cut(r.get('ds_language_ann', ''), 40), cut(r.get('ds_preference_ann', ''), 30), cut(r.get('ds_multi_action_ann', ''), 30), cut(r.get('ds_closed_loop', ''), 30), cut(r.get('ds_vlm_suitability', ''), 30), FMROLE.get(i, 'None'), cut(r.get('ds_known_limitations', ''), 90)])
SIZES['T7'] = write('T7_datasets_benchmarks', ['Resource', 'Cite key', 'Year', 'Type', 'Real / synthetic', 'Size', 'Sensors', 'Dynamic humans', 'Human trajectories', 'Group / intention labels', 'Language annotations', 'Preference labels', 'Multi-action labels', 'Closed loop', 'VLM-ready', 'FM role in resource', 'Known limitation'], dsrows,
    'T7 - Datasets, simulators and benchmarks', 'Source: `datasets_benchmarks_matrix.csv` (`ds_*`). [a] SNEI quantities are NOT collapsed: the originating paper reports ~2K scenarios, >40K QA pairs and 1,961 images (Table II); the public Hugging Face release has 1,508 rows (810 + 698; 1,479 distinct ids); later papers use a 325-image subset (265/60) or describe 810 items. The difference and the provenance (SCAND vs SCAND + MuSoHu) are unresolved; see SNEI_DATASET_RECONCILIATION.md.')
# ===================== T8 metrics =====================
MF = [
 ('Navigation success / efficiency', r'success|\bSR\b|SPL|path length|time to goal|navigation time|route completion|ego progress|distance to target|failed to plan|navigation error|\bNE\b', 'Objective', 'Robot', 'Sim / real', 'Task completion and efficiency', 'Safety margins, social quality; >= 8 incompatible "success" definitions'),
 ('Collision / human-collision rate', r'collision|H-Coll|\bCol\b|TCR', 'Objective', 'Robot', 'Sim / real', 'Physical contact (SAF1)', 'Near misses and discomfort; definitions vary (counterfactual in MUSON; manual interventions in VLM-Social-Nav)'),
 ('Near-collision / risk margin', r'near-collision|risk rate|TTC|safety violation|SVT|stopping distance|minimum distance to human|MDH|min\.? dist', 'Objective', 'Robot', 'Sim / real', 'Proximity safety (SAF2)', 'Whether proximity is socially acceptable'),
 ('Personal-space violation / compliance', r'personal|PSV|PSC|comfort (space|distance)|intrusion|discomfort|social score|disturbing individuals|AvgD', 'Objective', 'Robot', 'Sim / real', 'Proxemic compliance (SPA1)', 'Perceived comfort; thresholds differ (0.25 m vs 1.2 m vs Hall bands)'),
 ('Group-space disruption', r'group|social-zone|social zone|\bSIT\b|SIR', 'Objective', 'Robot', 'Sim / real', 'Group / F-formation respect (SPA2)', 'Group members\' perception'),
 ('Rule / instruction / region compliance', r'behavio(u)?r following|BFA|subject score|region score|assistant success|compliance rate|DCR', 'Objective', 'Robot', 'Sim / real', 'Instruction and convention compliance (NOR2, SPA3)', 'Whether rules are socially appropriate; task-specific'),
 ('Similarity to human trajectories', r'Fr.chet|ADE|FDE|AOE|MAOE|Hausdorff|L2 distance|MSE', 'Objective', 'Model / robot', 'Offline / real', 'Human-likeness proxy (EXP3 Partial)', 'Perceived naturalness; demonstrator bias'),
 ('Smoothness / comfort proxies', r'jerk|curvature|smoothness|roughness|acceleration', 'Objective', 'Robot', 'Sim / real', 'Motion quality', 'Human comfort (proxy only)'),
 ('VLM action / decision accuracy', r'action accuracy|\bAA\b|Pred@|multi-action|\bMAA\b|\bAPG\b|error rate|recall|\bAcc\b|grouping rate|crowd label|explanation accuracy|reference path error|unacceptable paths', 'Objective', 'Model', 'Offline', 'Decision correctness vs annotation', 'Whether the decision is executable or safe in closed loop'),
 ('Text similarity of reasoning', r'BERT|SBERT|SMS|\bcos\b|-cos|cosine|similarity', 'Objective (proxy)', 'Model', 'Offline', 'Agreement with reference text', 'Correctness and grounding of the reasoning; robot behaviour'),
 ('FM-as-judge / expert-system scores', r'expert-system|LLM extraction|judge|evaluator ranking|CODA', 'Subjective (model)', 'Model', 'Offline', 'Quality as judged by an FM or human judges of text', 'Validity of FM judges; robot behaviour'),
 ('Human questionnaire ratings', r'user study|questionnaire|survey|perceived|preference score|ratings|appropriateness|clarity|naturalness', 'Subjective (human)', 'Robot (human-centred)', 'Real (human study)', 'Perceived safety, comfort, naturalness, clarity, trust (EXP)', f"Small samples; rarely tested statistically ({qf('QF23')} papers report any statistics)"),
 ('Runtime / latency', r'latency|FPS|inference|query (time|frequency|processing)|throughput|processing time|planning rate|control rate|infer\. rate|system rate|runtime|parameter count|generation time|module latency|inference speed|cycle time|\bLat\.', 'Objective', 'System', 'Sim / real', 'Deployability', 'End-to-end staleness unless measured with moving humans (SPARK-VLN)'),
 ('Task-specific social measures', r'privacy|acoustic|noise|dialogue|conflict|sudden stops|stopping', 'Objective', 'Robot', 'Real / sim', 'Privacy exposure, noise, negotiation', 'Comparability across tasks and papers'),
]
DM = [m for m in MET if m['direct_fm_social'] == 'Yes' or M[m['id']]['analytical_category'] == 'S6']
rows = []
for fam_, rx, obj, lvl, app, meas, fail in MF:
    hits = [m for m in DM if re.search(rx, m['metric_name'], re.I)]
    ids = list(dict.fromkeys(m['id'] for m in hits)); names = list(dict.fromkeys(m['metric_name'] for m in hits))
    dpap = [i for i in ids if i in DI]
    rows.append([fam_, cut('; '.join(names), 150), obj, lvl, app, meas, fail, f'{len(dpap)}/{nD}', ', '.join(cite(i) for i in ids[:5])])
    if fam_ == 'Runtime / latency': assert set(dpap) == set(QF['QF25_metric']['ids']), 'runtime family must match QF25_metric (10_PreWriting/build_findings.py)'
SIZES['T8'] = write('T8_evaluation_metrics', ['Metric family', 'Metric names found (as printed)', 'Objective / subjective', 'Level', 'Applicability', 'What it measures', 'What it fails to measure', 'Direct papers using family', 'Representative papers'], rows,
    'T8 - Evaluation metrics: families, scope and blind spots',
    'Navigation success != safety != social compliance != human comfort != VLM reasoning accuracy. Families assigned by keyword over `evaluation_metrics_matrix.csv` (direct + S6 rows) and checked manually; a paper can use several families. Counts are papers using >= 1 metric of the family.')
# ===================== T9 failure modes =====================
fl = collections.defaultdict(list)
for d in D:
    for f in L(NOTES[d['id']].get('limitations_flags') and '; '.join(NOTES[d['id']]['limitations_flags'])): fl[f].append(d['id'])
FM_ = [
 ('Semantic-to-motion grounding gap', 'FM outputs language/decisions without metric grounding', 'Decision never executed, or mis-placed goals', f"{qf('QF10a')} direct papers never couple FM output to motion; Social-LLaVA uses a hard-coded action mapping; VLM baselines predict image-space goals that must be projected to the metric frame and reach lower pose validity (Group Joining)", 'Candidate selection (D2), cost layers (D3), grounding modules (G2-Nav, NORM-Nav)', 'Closed-loop testing of offline decision models', 'Observed in corpus'),
 ('Hallucination / invalid output', 'Generative decoding unconstrained by scene', 'Non-existent obstacles/people; invalid plans', f"flagged in {len(fl['hallucination'])} notes; structural safeguard in {qf('QF31_structural')}, prompt-level only in {qf('QF31_prompt')}", 'Restrict to feasible candidates (Etiquette), bounded output tuples (NORM-Nav), integer ratings (Hey Robot), critics (SAMALM)', 'No paper measures a hallucination rate in closed loop', 'Observed (mitigations); rate unmeasured'),
 ('Spatial-relation errors', 'Weak metric/3D reasoning in VLMs', 'Wrong side, distance or direction', f"flagged in {len(fl['spatial-reasoning-failure'])} notes (e.g., AutoSpatial motivation; Group Joining VLM baselines)", 'Structured spatial grounding (AutoSpatial), visual prompting with marks (CoNVOI, Etiquette)', 'Spatial accuracy rarely tested in closed loop', 'Observed in corpus'),
 ('Human-intention / activity misinterpretation', 'Ambiguous cues; single-frame context', 'Inappropriate yield/pass decisions', f"flagged in {len(fl['intention-ambiguity'])} notes; intention/activity evaluated (HUM2 Yes) in {qf('QF15_HUM2_direct')}", 'Multiple hypotheses scored by rollouts (SAATT); temporal context (HCSG)', 'Inference accuracy seldom measured', 'Observed in corpus'),
 ('Group-reasoning error', 'Visual grouping errors', 'Cutting through groups', f"flagged in {len(fl['group-detection-error'])} note (GSON grouping errors across LMMs)", 'Geometric group spaces from FM labels (GSON)', f"Group evaluation in {qf('QF15_SPA2_direct')}", 'Observed in corpus'),
 ('Prompt sensitivity', 'Output depends on prompt wording/framing', 'Unstable behaviour', f"flagged in {len(fl['prompt-sensitivity'])} notes (JSAI prompt study)", 'Prompt design studies; fine-tuning', 'Robustness not tested on robots', 'Observed in corpus'),
 ('Temporal inconsistency', 'Independent per-frame inference', 'Oscillating decisions', f"flagged in {len(fl['temporal-inconsistency'])} notes", 'Memory or temporal context (OLiVia-Nav, HCSG), slow/fast designs', 'Consistency metrics absent', 'Observed in corpus'),
 ('Latency / stale reasoning', 'Seconds-scale FM inference', 'Acting on outdated scene while people move', f"flagged in {len(fl['latency'])} notes; e.g., LISN ~7 s, Sotomi ~20 s, HUMA 2.4 s, MOSU 2.3 s; staleness quantified by SPARK-VLN", f"Asynchronous slow/fast ({qf('QF13')}), event triggering (HUMA), distillation (D7 {qf('QF09_D7')}), latent streaming", f"Latency reported numerically in {qf('QF25')} only, in non-comparable units", 'Observed in corpus'),
 ('Cloud / network dependence', 'API or remote-server inference', 'Outages, delay, data leaving the robot', f"flagged in {len(fl['cloud-dependence'])} notes; cloud/hybrid/remote inference in {qf('QF32_cloudremote')}", 'Local small VLMs (SNEI family), distillation (Narrate2Nav, OLiVia-Nav)', 'Offline fallbacks rarely evaluated', 'Observed in corpus'),
 ('Safety risks in learned or FM-conditioned execution', 'Learned or FM-conditioned execution with limited independent safety checks', 'Collisions; no guarantee', f"FM-independent safety guard in {qf('QF12')} direct-action (D6) systems; human-collision rates of ~34% (HUMA, Social-HM3D) and ~29% (SPARK-VLN realistic mode) in D5 systems", 'Keep a classical planner or CBF/reflex layer (GSON, G2-Nav, Hey Robot)', 'No shielded VLA in corpus', 'Observed in corpus'),
 ('Lack of calibrated FM uncertainty', 'FM outputs carry no calibrated confidence by default', 'Overconfident social decisions', f"explicit uncertainty treatment {qf('QF30_explicit')}; partial {qf('QF30_partial')}", 'Sampling / majority vote (PANav), GPR variance (Saito), CVAE sampling (LE-Nav)', 'No calibrated FM confidence in any direct paper', 'Observed absence'),
 ('Training-data / annotation bias', 'Teacher FM or single-annotator labels', 'Errors baked into students', f"D7 teacher use in {qf('QF09_D7')}; SNEI annotations reviewed by one person (Social-LLaVA note); GPT-generated MUSON labels", 'Human review; multi-action labels (MAction)', 'Label quality rarely audited', 'Observed in corpus'),
 ('Cultural / norm bias', 'Norms learned from pretraining data (raised as a limitation in the corpus)', 'Norms wrong in other contexts', f"cultural adaptation evaluated (NOR4 Yes) in {qf('QF15_NOR4_direct')}; flagged in {len(fl['cultural-bias'])} note", 'None in corpus', 'Entirely open', 'Raised in corpus; untested'),
 ('Privacy exposure', 'Off-robot processing of observations or derived context; observing private spaces', 'Privacy harm to bystanders', f"privacy treated by {qf('QF34')} (PANav); {qf('QF32_cloudremote')} papers use off-robot FM inference", 'Privacy-aware path selection (PANav)', 'No privacy evaluation of the FM pipeline itself', 'Partly observed; largely general deployment risk'),
]
SIZES['T9'] = write('T9_failure_modes', ['Failure mode', 'Foundation-model cause', 'Navigation consequence', 'Evidence in corpus (counts from QUANTITATIVE_FINDINGS)', 'Mitigation approaches in corpus', 'Unresolved issue', 'Evidence type'], [list(r) for r in FM_],
    'T9 - Foundation-model failure modes and mitigations in social navigation',
    '"Evidence type" separates failures directly observed in the corpus from general FM risks relevant to it. Limitation-flag counts are free-text tags from the notes (indicative only).')
# ===================== T10 roadmap =====================
RM = [
 ('Grounding offline social reasoning', f"{qf('QF10a')} direct papers never couple FM output to motion; {qf('QF22')} have offline evidence only", 'Offline accuracy does not imply safe or social motion', 'Candidate selection and cost shaping (D2/D3)', 'Closed-loop evaluation of decision models through an executable interface', 'Same model: offline score vs closed-loop social metrics'),
 ('Human-centred evidence', f"Human evaluation of robot behaviour in {qf('QF19_EV5_behaviour')} ({qf('QF19_EV5_co-present')} co-present); {qf('QF61_beh_stats')} report inferential statistics on behavioural ratings; {qf('QF23')} report statistical testing of any result", 'EXP-family claims (comfort, legibility) remain weakly validated', 'Small questionnaires (VLM-Social-Nav, PAD, LE-Nav)', 'Co-present user studies with validated instruments', 'Reported sample size, statistical test and effect size'),
 ('Real, unscripted humans and open-world deployment', f"Unscripted humans in {qf('QF18_EV4_unscripted')}; open-world deployment {qf('QF20')}", 'Staged participants know the experiment; public reactions are untested', 'Campus and public-space deployments (GSON, G2-Nav, Walk With Me)', 'Long-duration deployments in public spaces', 'Hours / km of operation; interventions; incident rates'),
 ('Safety separation for end-to-end models', f"FM-independent safety guard in {qf('QF12')} direct-action systems; {qf('QF28')} overall", 'Direct action removes the classical safety envelope', 'CBF / reflex layers around VLM costs (GSON, G2-Nav)', 'Shielded VLA policies; formal or runtime verification', 'Collision and near-collision under adversarial / dense scenes'),
 ('Uncertainty-aware social decisions', f"Explicit uncertainty {qf('QF30_explicit')}; partial {qf('QF30_partial')}", 'Overconfident social judgements in ambiguous scenes', 'Sampling, voting, GPR variance', 'Calibrated FM uncertainty propagated to the planner', 'Calibration error; abstention / fallback rates'),
 ('Latency and staleness', f"Numeric runtime in {qf('QF25')}; asynchronous designs {qf('QF13')}", 'Decisions arrive after people have moved', 'Slow/fast loops, streaming latents (SPARK-VLN), distillation', 'End-to-end latency measured on robot hardware with moving people', 'Staleness-aware benchmarks (realistic asynchronous mode)'),
 ('Comparable evaluation', f"{QF['QF37']['numerator']} metric definitions; incompatible definitions of success, collision and PSV; SNEI used in {qf('QF40')} with different subsets", 'Results cannot be compared or pooled', 'Shared benchmarks (SocialNav-SUB, LISN-Bench, SONG, DPed-VLN)', 'Closed-loop social benchmarks with fixed metric definitions and reported data subsets', 'Cross-paper leaderboards with fixed splits'),
 ('Neglected social capabilities', f"Crowd (SPA4) evaluated in {qf('QF15_SPA4_direct')} (pre-FM {qf('QF15_SPA4_prefm')}); prediction (HUM1) {qf('QF15_HUM1_direct')}; legibility (EXP2) {qf('QF15_EXP2_direct')}", 'FM work rarely measures capabilities central to earlier paradigms, although it addresses them', 'Prediction coupled with FM path selection or navigation graphs (Etiquette, HCSG)', 'FM reasoning combined with prediction-based planning', 'Dense-crowd and legibility metrics alongside norm metrics'),
 ('Validating FM-inferred norms', f"R3 (FM infers norms) papers evaluating any normative capability {qf('QF45_R3_NOR')}; instruction-following evaluations using an R4 role {qf('QF45_NOR2_R4')}", "The FM's own judgement of what is appropriate is seldom measured", 'Multi-action labels (MAction); human answer distributions (SocialNav-SUB)', 'Reference judgements of appropriate behaviour collected from people for the same scenes', 'Agreement of FM-selected behaviour with human appropriateness ratings, in closed loop'),
 ('Cultural and normative adaptation', f"Cultural adaptation evaluated in {qf('QF15_NOR4_direct')}", 'No direct paper tests whether social judgements transfer across cultures', 'None in corpus', 'Multi-site, multi-culture datasets and adaptation methods', 'Cross-cultural user studies'),
 ('Privacy and on-device inference', f"Privacy treated in {qf('QF34')}; cloud/remote inference {qf('QF32_cloudremote')}", 'Bystander data leaves the robot', 'PANav; local small VLMs', 'On-device FMs; privacy-preserving perception', 'Privacy risk metrics; on-device latency'),
 ('Reproducibility', f"Code released in {qf('QF35')}; new datasets released {qf('QF36')}", 'Claims cannot be verified', 'Code releases (BehAV, LE-Nav, E-SocialNav; DPed-VLN benchmark)', 'Released code, prompts, model versions and evaluation scripts', 'Independent replication'),
]
SIZES['T10'] = write('T10_research_roadmap', ['Open challenge', 'Evidence from corpus (exact counts)', 'Why it matters', 'Current partial solutions', 'Direction suggested by the reviewed work', 'Evidence that would establish progress'], [list(r) for r in RM],
    'T10 - Open challenges and future directions', f'All counts from 10_PreWriting/QUANTITATIVE_FINDINGS.md (direct n = {nD}; cut-off 2026-10-19).')
# ===================== Supplementary =====================
SCR = list(csv.DictReader(open(os.path.join(A, '_tools', 'stage2', 'screening_record.csv'))))
SIZES['S1'] = write('S1_screening_record', ['Key', 'First found', 'Passes', 'Title', 'First author', 'Date', 'Decision', 'Target', 'Screening level', 'Reason'],
    [[r['key'], r['source'], r['passes'], r['title'][:100], r['authors'], r['date'][:10], r['decision'], r['target'], r['screening'], final_terms(r['reason'][:140])] for r in SCR], f'S1 - Search and screening record ({len(SCR)} candidates)', 'Source: stage2/screening_record.csv; query families in TARGETED_SEARCH_LOG.md.')
SIZES['S2'] = write('S2_publication_status', ['Cite key', 'Note id', 'Category', 'Year', 'Venue', 'Status class', 'Peer reviewed', 'DOI', 'arXiv relation'],
    [[cite(i), i, m['analytical_category'], m['year'], m['venue'][:80], m['ext_status_class'], m['peer_reviewed'], m['doi'], str(m['ext_version_relationship'])[:90]] for i, m in sorted(M.items())], 'S2 - Publication status of all corpus works', 'Source: master matrix ext_* columns; PUBLICATION_STATUS_AUDIT.md.')
SIZES['S3'] = write('T_adjacent_foundation_models', ['Paper', 'Cite key', 'Year', 'Foundation-model mechanism', 'Navigation task', 'Concept inherited by social-navigation methods', 'Relevance to social navigation', 'Why NOT direct social-navigation evidence'],
    [[short(r['id']), cite(r['id']), r['year'], final_terms(r['adj_mechanism'][:140]), NOTES[r['id']].get('paper_type', '')[:40], final_terms(r['adj_inherited_by'][:120]), final_terms(r['adj_relevance'][:120]), final_terms(r['adj_why_not_direct'][:120])] for r in sorted(ADJ, key=lambda r: r['year'])],
    'S3 - Adjacent foundation-model navigation (not social-navigation evidence)', 'Source: `adjacent_foundation_model_matrix.csv` (adj_*). These works supply mechanisms (value maps, navigation FMs, VLAs, LLM planning) but have no social capability (11/13 do not represent humans).')
FC = ['final_A_social_representation', 'final_B_roles', 'final_D_interface', 'final_EV1_offline', 'final_EV2_closed_loop_sim', 'final_EV3_physical_robot', 'final_EV4_real_humans_in_trials', 'final_EV5_human_evaluation', 'final_EV6_open_world_deployment']
SIZES['S4'] = write('S4_full_final_coding', ['Note id', 'Cite key', 'Category'] + [c.replace('final_', '') for c in FC] + ['Capability leaves Yes', 'Capability leaves Partial'],
    [[i, cite(i), m['analytical_category']] + [m.get(c, '') for c in FC] + [' '.join(l for l in LEAF if CAP.get(i, {}).get('final_' + l) == 'Yes'), ' '.join(l for l in LEAF if CAP.get(i, {}).get('final_' + l) == 'Partial')] for i, m in sorted(M.items()) if m['analytical_category'] != 'S0'],
    'S4 - Full final (Stage-3) coding of all non-survey works', 'Authoritative codes; legacy codes in matrices as legacy_*.')
# file aliases requested by Stage-4 brief
import shutil
for a, b in [('T4_direct_architecture', 'T_direct_architecture'), ('T5_direct_evidence', 'T_direct_evidence'), ('T7_datasets_benchmarks', 'T_datasets_benchmarks'), ('T8_evaluation_metrics', 'T_evaluation_metrics'),
             ('T9_failure_modes', 'T_failure_modes'), ('T10_research_roadmap', 'T_research_roadmap')]:
    for ext in ('.csv', '.md'): shutil.copyfile(os.path.join(OUT, a + ext), os.path.join(OUT, b + ext))
json.dump(SIZES, open(os.path.join(OUT, 'table_row_counts.json'), 'w'), indent=1); print(SIZES)

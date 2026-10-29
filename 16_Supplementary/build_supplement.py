"""Build the reader-facing supplementary tables from 11_Tables (the CSVs there remain the audit record; do not edit outputs by hand).
Outputs (CSV + Markdown): S1 screening record, S2 publication status, S3 adjacent FM navigation, S4 full final coding,
S5 pre-FM comparison set (parts A and B), S11-S13 (per-paper architecture and evidence, per-resource datasets; formerly main-text Tables 5-7). Internal identifiers (note ids) are replaced by citation keys; internal workflow wording is rephrased."""
import csv, json, os, re
H = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(H); TB = os.path.join(ROOT, '11_Tables')
CK = json.load(open(os.path.join(ROOT, '13_References', 'citation_keys.json'))); NOTE2KEY = {v: k for k, v in CK.items()}
def clean(v):
    v = str(v)
    for a, b in [('added in Stage 2', 'included after full-text screening'), ('already in Stage-1 corpus', 'already in the seed corpus'),
                 ('not cited by direct social-navigation notes found so far', 'not cited by the direct social-navigation papers in the reviewed corpus'),
                 ('Not found / not applicable', 'none'), ('recorded in EXCLUDED_WITHDRAWN_WORKS.md', 'recorded separately as withdrawn'), ('1,961 images (paper Table II)', '1,961 images (originating paper)'), ('See note [a]: ', '[a] ')]:
        v = v.replace(a, b)
    v = re.sub(r'\s*\(DATA_QUALITY_ISSUES[^)]*\)?', '', v)
    v = re.sub(r'\(authors, p\.[^)]*\)', '(stated by the authors)', v)
    v = re.sub(r'flagged in (\d+) notes?\b', r'flagged for \1 papers', v)
    return v
def build(src, out, title, drop=(), rename=None, map_note_cols=(), path=None):
    rows = list(csv.DictReader(open(path or os.path.join(TB, src + '.csv'))))
    cols = [c for c in rows[0] if c not in drop]
    rename = rename or {}
    data = []
    for r in rows:
        d = {}
        for c in cols:
            v = r[c]
            if c in map_note_cols: v = NOTE2KEY.get(v, '') if v and v != '-' else ''
            d[rename.get(c, c)] = clean(v)
        data.append(d)
    hdr = [rename.get(c, c) for c in cols]
    with open(os.path.join(H, out + '.csv'), 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=hdr); w.writeheader(); w.writerows(data)
    md = [f'# {title}', '', f'{len(data)} rows. Machine-readable version: `{out}.csv`.', '', '| ' + ' | '.join(hdr) + ' |', '|' + '---|' * len(hdr)]
    md += ['| ' + ' | '.join(str(d[h]).replace('|', '/').replace('\n', ' ') for h in hdr) + ' |' for d in data]
    open(os.path.join(H, out + '.md'), 'w').write('\n'.join(md) + '\n')
    return len(data)
QF = {q['id']: q for q in json.load(open(os.path.join(ROOT, '10_PreWriting', 'quantitative_findings.json')))}
def qn(i): return QF[i]['numerator']
n = {}
n['S1'] = build('S1_screening_record', 'S1_screening_record', 'Table S1, part A. Screening record of all candidates identified in the expansion search and the final cut-off check',
                rename={'Key': 'Candidate id (arXiv id or key)', 'First found': 'First found (search pass P1-P3, web, citation)', 'Passes': 'Found in passes', 'Target': 'Corpus entry (cite key)'},
                map_note_cols=('Target',))
# Table S1, part B: final coverage search (stage 11, 2026-10-26); written from the stage-11 record without changes
S1B = list(csv.DictReader(open(os.path.join(ROOT, '07_Literature_Analysis', '_tools', 'stage11', 'S1_final_search_record.csv'))))
HB = ['Title', 'First author', 'Date', 'Venue', 'DOI', 'Retrieved by', 'Status in project', 'Decision', 'Screening level', 'Reason']
KB = ['title', 'first_author', 'date', 'venue', 'doi', 'sources', 'project_status', 'decision', 'level', 'reason']
order = {'INCLUDE': 0, 'UNRESOLVED (not coded)': 1, 'EXCLUDE': 2, 'ALREADY SCREENED (Stage 2)': 3, 'ALREADY KNOWN': 4}
S1B.sort(key=lambda r: (order[r['decision']], r['title'].lower()))
with open(os.path.join(H, 'S1b_final_search_record.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(HB); [w.writerow([r[k] for k in KB]) for r in S1B]
mdb = ['# Table S1, part B. Final coverage search (26 October 2026)', '',
       f"IEEE Xplore ({qn('QF62_ieee_queries')} queries, {qn('QF62_ieee_records')} records), OpenAlex ({qn('QF62_oa_queries')} query families, {qn('QF62_oa_records')} records), forward citation chasing on OpenAlex ({qn('QF62_fw_seeds')} direct papers, {qn('QF62_fw_records')} citing records) and a limited manual Google Scholar check (one results page, {qn('QF62_gs_records')} records; an automated-access check stopped the search and was not circumvented; Google Scholar was not searched systematically). "
       f"{qn('QF62_records')} records = {qn('QF62_unique')} unique works ({qn('QF62_dups')} duplicate records merged). Already known: {qn('QF62_known')}. New: {qn('QF62_new')}, of which {qn('QF62_added')} added after full-text assessment, {qn('QF62_excluded')} excluded and {qn('QF62_unresolved')} unresolved (full text not accessible; not coded). "
       'Reason codes R1-R8 as defined in the Notation section of the supplement (R7 and R8 occur only in part B). Raw retrieval files: `07_Literature_Analysis/_tools/stage11/`.', '',
       f'{len(S1B)} rows. Machine-readable version: `S1b_final_search_record.csv`.', '', '| ' + ' | '.join(HB) + ' |', '|' + '---|' * len(HB)]
mdb += ['| ' + ' | '.join(str(r[k]).replace('|', '/') for k in KB) + ' |' for r in S1B]
open(os.path.join(H, 'S1b_final_search_record.md'), 'w').write('\n'.join(mdb) + '\n'); n['S1b'] = len(S1B)
n['S2'] = build('S2_publication_status', 'S2_publication_status', f"Table S2. Publication status of all {qn('QF01')} corpus works", drop=('Note id',))
n['S3'] = build('T_adjacent_foundation_models', 'S3_adjacent_foundation_models', 'Table S3. Adjacent foundation-model navigation works (not social-navigation evidence)')
n['S4'] = build('S4_full_final_coding', 'S4_full_final_coding', f"Table S4. Full final coding of the {qn('QF57_coded')} coded works (all non-survey works)", drop=('Note id',))
n['S11'] = build('T4_direct_architecture', 'S11_direct_architecture', f"Table S11. Architecture of the {qn('QF02')} direct papers, per paper (all columns; formerly main-text Table 5, summarised in the main text by interface)")
n['S12'] = build('T5_direct_evidence', 'S12_direct_evidence', f"Table S12. Evaluated capabilities and evidence of the {qn('QF02')} direct papers, per paper (all columns; formerly main-text Table 6)")
# Table S5: reader-facing version of the pre-FM comparison set
P5 = list(csv.DictReader(open(os.path.join(ROOT, '07_Literature_Analysis', 'prefm_comparison_set.csv'))))
def sel(r):
    if r['in_frozen_corpus'] == 'Yes': return 'corpus work (retained)'
    if r['selection'].startswith('cited by'): return 'cited by at least 3 of the 7 reference surveys'
    return 'added to reach 3 works in its paradigm'
def ev(v): return {'not coded in Stage 3': 'not coded (corpus work)', 'ND': 'not determinable'}.get(v, v)
def enote(v): return '' if v == 'frozen coding' else v.replace('frozen coding; ', '').replace(' in Stage 3', '')
def meta(v): return 'corpus record' if v.startswith('frozen corpus') else ('bibliography record' if v.startswith('existing') else 'Crossref record')
H5 = ['Cite key', 'Title', 'Year', 'Venue', 'Paradigm', 'Reference surveys citing (of 7)', 'Selection', 'Coding source', 'Link', 'A (representation)', 'Evaluated capabilities (Yes)',
      'Addressed-only capabilities (Partial)', 'EV1 offline (recorded data)', 'EV2 closed-loop simulation', 'EV3 physical robot', 'EV4 real people in trials', 'EV5 human evaluation', 'EV6 open-world deployment',
      'Statistical testing', 'Evidence note', 'Metadata source']
D5 = [[r['bib_key'], r['title'], r['year'], r['venue'], r['paradigm'].split(' ', 1)[1], r['survey_count'] or '-', sel(r),
       'full text' if r['coding_source'].startswith('full text') else 'reference-survey descriptions', r['source_url'], r['A'], r['cap_yes'] or '-', r['cap_partial'] or '-',
       r['EV1_offline_recorded'], r['EV2_closed_loop_sim'], ev(r['EV3_physical_robot']), ev(r['EV4_people_in_trials']), ev(r['EV5_human_evaluation']), r['EV6_open_world'],
       ev(r['statistical_testing']), enote(r['evidence_note']), meta(r['metadata'])] for r in P5]
with open(os.path.join(H, 'S5_prefm_comparison_set.csv'), 'w', newline='') as fo:
    w = csv.writer(fo); w.writerow(H5); w.writerows(D5)
open(os.path.join(H, 'S5_prefm_comparison_set.md'), 'w').write('\n'.join([f"# Table S5, part A. Pre-FM comparison set ({qn('QF50_prefm_n')} works): selection, coding source and final coding", '',
    f"{len(D5)} rows. Machine-readable version: `S5_prefm_comparison_set.csv`. Part B (`S5b_prefm_by_paradigm.csv`) summarises the set by paradigm. Selection and limitations: manuscript Section 2.3. "
    "'Not determinable' marks evidence that the reference-survey descriptions do not establish; such works are excluded from evidence denominators. "
    "Corpus works keep their final corpus coding; EV4 and statistical testing were not coded for non-direct corpus works.", '',
    '| ' + ' | '.join(H5) + ' |', '|' + '---|' * len(H5)] + ['| ' + ' | '.join(str(c).replace('|', '/') for c in row) + ' |' for row in D5]) + '\n')
n['S5'] = len(D5)
n['S13'] = build('T7_datasets_benchmarks', 'S13_datasets_benchmarks', 'Table S13. Datasets, simulators and benchmarks, per resource (all columns; main-text Table 5 groups them into families)')
n['S5b'] = build('T3_prefm_baselines', 'S5b_prefm_by_paradigm', f"Table S5, part B. Pre-FM comparison set by paradigm (n = {qn('QF50_prefm_n')}; formerly main-text Table 4). Works: number of works (coded from full text); A and C: works per code; robot: systematic real-robot evaluation; ND: not determinable")
n['S9'] = build('TI_interface_evidence', 'S9_interface_evidence', 'Table S9. Navigation interfaces and evidence: counts behind Fig. 6 (generated by 12_Figures/F12_interface_evidence/make_f12.py)')
n['S10'] = build('T8_evaluation_metrics', 'S10_metric_families', 'Table S10. Metric families: metric names, level, what each family measures and fails to measure, and direct papers using it (counts behind Fig. 8)')
# Table S6: robustness of headline counts (all direct papers, peer-reviewed subset, pre-Cai-cut-off subset)
S6R = [('Linguistic description of people (A5)', 'QF06_A5_direct', 'QF55_pr_A5', 'QF55_precai_A5'), ('Social-instruction following evaluated (NOR2)', 'QF15_NOR2_direct', 'QF55_pr_NOR2', 'QF55_precai_NOR2'),
       ('Crowd navigation evaluated (SPA4)', 'QF15_SPA4_direct', 'QF55_pr_SPA4', 'QF55_precai_SPA4'), ('FM output never reaches motion (D0/D8 only)', 'QF10a', 'QF55_pr_uncoupled', 'QF55_precai_uncoupled'),
       ('Systematic real-robot evaluation', 'QF17_EV3_systematic', 'QF55_pr_robot', 'QF55_precai_robot'), ('Human evaluation of robot behaviour', 'QF19_EV5_behaviour', 'QF55_pr_human', 'QF55_precai_human')]
def fr(i): return f"{QF[i]['numerator']}/{QF[i]['denominator']} ({QF[i]['percentage']})"
hdr = ['Indicator', 'All direct papers', 'Peer-reviewed (class A)', 'Public before Cai et al. cut-off']
with open(os.path.join(H, 'S6_robustness.csv'), 'w', newline='') as fo:
    w = csv.writer(fo); w.writerow(hdr); [w.writerow([r[0]] + [fr(x) for x in r[1:]]) for r in S6R]
open(os.path.join(H, 'S6_robustness.md'), 'w').write('\n'.join(['# Table S6. Robustness of headline counts to publication status and to the Cai et al. cut-off', '',
    'Generated from 10_PreWriting/quantitative_findings.json. Machine-readable version: `S6_robustness.csv`.', '', '| ' + ' | '.join(hdr) + ' |', '|---|---|---|---|'] +
    ['| ' + ' | '.join([r[0]] + [fr(x) for x in r[1:]]) + ' |' for r in S6R]) + '\n')
n['S6'] = len(S6R)
# Table S7: capability coverage counts (moved from the main text in Stage 11; the main figure shows the same counts as bar labels)
n['S7'] = build('T6_capability_coverage', 'S7_capability_coverage', f"Table S7. Social-capability coverage: direct papers (n = {qn('QF02')}), pre-FM comparison set (n = {qn('QF50_prefm_n')}) and datasets and benchmarks (n = {qn('QF57_S6')})")
# Table S8: full code dictionary of the five coding dimensions and cross-cutting attributes (Phase 29)
CODES = [('A', 'A0', 'Not represented', 'Humans absent, or present only as instruction givers'), ('A', 'A1', 'Kinematic agent', 'Tracked position, velocity or disc'),
 ('A', 'A2', 'Predicted motion', 'Trajectory forecasts or distributions'), ('A', 'A3', 'Social-space field', 'Proxemic potentials, personal or group spaces, social cost layers'),
 ('A', 'A4', 'Relational or interaction structure', 'Pairwise interactions, graphs, attention over agents, groups as relations'),
 ('A', 'A5', 'Symbolic or linguistic description', 'Attributes, activities, intents or rules expressed in language or symbols'),
 ('A', 'A6', 'Implicit or latent', 'Raw images interpreted by a learned model; humans only as embeddings'),
 ('B', 'R1', 'Scene and context interpretation', 'Non-human context: place type, traversability, objects, situation'),
 ('B', 'R2', 'Human-state and relation inference', 'Motion, intent, activity, identity, group membership, crowding'),
 ('B', 'R3', 'Social-norm reasoning and behaviour selection', 'The FM itself infers what is socially appropriate and selects the behaviour'),
 ('B', 'R4', 'Instruction and preference grounding', 'Norms, preferences or tasks given in language are translated into plans, constraints or parameters'),
 ('B', 'R5', 'Human-facing communication', 'Dialogue or explanations delivered to people')]
CAPS = [('SAF1', 'Collision avoidance'), ('SAF2', 'Near-collision or risk margin'), ('SPA1', 'Personal space'), ('SPA2', 'Group and conversation space'), ('SPA3', 'Encounter conventions (passing side, yielding, queueing)'),
 ('SPA4', 'Crowd navigation'), ('HUM1', 'Motion understanding or prediction'), ('HUM2', 'Intention or activity inference'), ('NOR1', 'Etiquette and politeness'), ('NOR2', 'Explicit social-instruction following'),
 ('NOR3', 'Context-dependent conduct'), ('NOR4', 'Cultural or norm adaptation'), ('EXP1', 'Perceived safety and comfort'), ('EXP2', 'Legibility and predictability'), ('EXP3', 'Naturalness')]
CODES += [('C', c, l, 'Evaluated: dedicated metric or systematic scenario-specific criterion; addressed: targeted without such a measure') for c, l in CAPS]
CODES += [('D', 'D0', 'Non-executed decision', 'FM output compared with annotations; not executed'), ('D', 'D1', 'Semantic or social state', 'Groups, intents, activities passed to a planner'),
 ('D', 'D2', 'Candidate selection', 'FM chooses among planner-generated options'), ('D', 'D3', 'Objective, constraint or parameter shaping', 'FM sets costs, constraints or controller parameters'),
 ('D', 'D4', 'Goal, waypoint or reference trajectory', 'FM specifies where to go'), ('D', 'D5', 'Runtime latent conditioning', 'FM embeddings or tokens condition a learned policy'),
 ('D', 'D6', 'Direct action', 'FM or an FM-based policy (e.g. a VLA) outputs velocities or trajectories without an intervening planner selecting the motion; an FM-independent safety guard is coded separately'), ('D', 'D7', 'Training-time supervision', 'FM supplies labels, rewards or distillation targets; no FM at runtime'),
 ('D', 'D8', 'Human-facing channel', 'Dialogue or explanations sent to people'),
 ('E', 'EV1', 'Offline evaluation', 'Yes / No'), ('E', 'EV2', 'Closed-loop simulation', 'Yes / No'), ('E', 'EV3', 'Physical robot', 'none / demonstration / systematic'),
 ('E', 'EV4', 'Real people in robot trials', 'none / simulated only / staged / unscripted / present, type unreported / not reported'),
 ('E', 'EV5', 'Human evaluation', 'none / text raters / observers or video raters / co-present participants'), ('E', 'EV6', 'Open-world or long-duration deployment', 'Yes / No'),
 ('X', 'coupling', 'Temporal coupling', 'per decision / asynchronous slow-fast / event-triggered / offline / training only'), ('X', 'guard', 'FM-independent safety guard', 'Safety that does not rely on the FM being correct (CBF filter, reflex layer, constrained optimiser, feasible-candidate restriction)'),
 ('X', 'uncertainty', 'Uncertainty treatment', 'explicit / partial / none'), ('X', 'hallucination', 'Hallucination mitigation', 'structural / prompt or training level / none'),
 ('X', 'location', 'Inference location', 'on board / local server / remote server / cloud API / hybrid'), ('X', 'memory', 'Memory and continual adaptation', 'Persistent state across episodes'),
 ('X', 'privacy', 'Privacy constraint', 'Privacy treated as an objective or constraint'), ('X', 'explanation', 'Explanation output', 'Text delivered to people')]
DIM = {'A': 'A Social representation', 'B': 'B FM role', 'C': 'C Social capability', 'D': 'D Navigation interface', 'E': 'E Evidence profile', 'X': 'Cross-cutting attribute'}
with open(os.path.join(H, 'S8_code_dictionary.csv'), 'w', newline='') as fo:
    w = csv.writer(fo); w.writerow(['Dimension', 'Code', 'Label', 'Definition or values']); [w.writerow([DIM[d], c, l, x]) for d, c, l, x in CODES]
open(os.path.join(H, 'S8_code_dictionary.md'), 'w').write('\n'.join(['# Table S8. Code dictionary of the five coding dimensions and the cross-cutting attributes', '', 'Machine-readable version: `S8_code_dictionary.csv`. Definitions: manuscript Section 5.', '',
    '| Dimension | Code | Label | Definition or values |', '|---|---|---|---|'] + [f'| {DIM[d]} | {c} | {l} | {x} |' for d, c, l, x in CODES]) + '\n')
n['S8'] = len(CODES)
# Supplementary figures (Stage 11: per-paper matrices moved from the main text)
import shutil
for src, dst in [('F2_functional_roles/F2_functional_roles', 'FigS1_fm_roles'), ('F4_evidence_profile/F4_evidence_profile', 'FigS2_evidence_profile'), ('F3_social_capabilities/F3s_capability_heatmap_supplementary', 'FigS3_capability_heatmap'), ('F9_evolution_timeline/F9_evolution_timeline', 'FigS4_evolution_timeline')]:
    for ext in ('pdf', 'png'): shutil.copy(os.path.join(ROOT, '12_Figures', src + '.' + ext), os.path.join(H, dst + '.' + ext))
# Supplementary index (generated; counts from the quantitative-findings file)
NOTATION = open(os.path.join(H, 'supplement_notation_template.md')).read()
NOTATION = re.sub(r'@(QF\w+?)(:n)?@', lambda m: str(qn(m.group(1))) if m.group(2) else f"{qn(m.group(1))}/{QF[m.group(1)]['denominator']}", NOTATION)   # counts in the notation text come from the findings file
idx = ['# Supplementary Material', '', '**From Proxemics to Foundation Models: A Survey of Socially Aware Robot Navigation**', '',
       'This supplement contains the screening records, per-work coding tables and supporting analyses underlying the survey. The main manuscript presents condensed summaries, while the supplementary tables provide the corresponding detailed records. Each table is also provided as a machine-readable CSV file (`Supplementary_Data_tables_CSV.zip`). The discussion is in the main manuscript and is not repeated here.', '',
       '**Literature cut-off:** 19 October 2026. The final coverage search was conducted on 26 October 2026 and restricted to works dated up to the literature cut-off.', '', '| Corpus component | n |', '|---|---|',
       f"| Unique works | {qn('QF01')} |", f"| Direct foundation-model (FM) social-navigation papers | {qn('QF02')} |", f"| Classical and learning-based works | {qn('QF57_S12')} |",
       f"| Adjacent FM navigation works | {qn('QF57_S3')} |", f"| Datasets, simulators and benchmarks | {qn('QF57_S6')} |", f"| Surveys | {qn('QF57_S0')} |",
       f"| Representative pre-FM comparison set (not exhaustive; outside the corpus count; includes the {qn('QF57_S12')} classical and learning works) | {qn('QF50_prefm_n')} |", '', '## Contents', '',
       '| Item | Content | Relation to the manuscript |', '|---|---|---|',
       f"| Table S1, part A (`S1_screening_record.csv`) | Part A: all {n['S1']} candidates identified in the expansion search and the final cut-off check (three arXiv search passes, general web search, backward citation chasing; arXiv, Crossref and proceedings at the cut-off), each with its screening level, decision and reason | Section 2.2 |",
       f"| Table S1, part B (`S1b_final_search_record.csv`) | Part B: all {n['S1b']} unique works of the final coverage search (IEEE Xplore, OpenAlex, forward citation chasing, and a limited manual Google Scholar check of one results page; Google Scholar was not searched systematically), with retrieval source, decision and reason; lists the {qn('QF62_unresolved')} unresolved works | Section 2.2 |",
       f"| Table S2 (`S2_publication_status.csv`) | Publication status of all {qn('QF01')} corpus works: venue, status class, peer review, DOI and relation of the analysed copy to the published version | Section 2.4; Table S11 |",
       f"| Table S3 (`S3_adjacent_foundation_models.csv`) | The {qn('QF57_S3')} adjacent FM navigation works: mechanism, task, concept inherited by social-navigation methods, and why each is *not* evidence of social competence | Section 4 |",
       f"| Table S4 (`S4_full_final_coding.csv`) | Final coding of the {qn('QF57_coded')} non-survey corpus works on Dimensions A, B, D and E, with evaluated (Yes) and addressed-only (Partial) capability leaves | Sections 5-9 |",
       f"| Table S5 (`S5_prefm_comparison_set.csv`) | The {qn('QF50_prefm_n')}-work representative pre-FM comparison set: selection, coding source, links and coding (part A); summary by paradigm (part B, `S5b_prefm_by_paradigm.csv`; formerly main-text Table 4) | Sections 2.3, 3 and 7 |",
       '| Table S6 (`S6_robustness.csv`) | Headline counts for all direct papers, the peer-reviewed subset and papers public before the Cai et al. cut-off | Section 10.5 |',
       f"| Table S7 (`S7_capability_coverage.csv`) | Capability counts per leaf: direct evaluated and addressed, pre-FM evaluated, datasets evaluated | Section 7; Fig. 7 |",
       f"| Table S8 (`S8_code_dictionary.csv`) | Full code dictionary of the five coding dimensions and the cross-cutting attributes | Section 5; Fig. 4 |",
       '| Table S9 (`S9_interface_evidence.csv`) | Counts behind Fig. 6: papers per interface and, within them, systematic robot evaluation, FM-independent safety guard and remote inference; evidence by publication year | Sections 5 and 9; Fig. 6 |',
       '| Table S10 (`S10_metric_families.csv`) | Full metric-family table (formerly a main-text table): metric names found, level, what each family measures and fails to measure, direct papers using it | Section 8; Fig. 8 |',
       '| Table S11 (`S11_direct_architecture.csv`) | Per-paper architecture of every direct paper: publication status, FM models, inputs, Dimensions A, B and D, planner or controller, temporal coupling, FM-independent safety guard, other attributes and main contribution (formerly main-text Table 5) | Sections 5 and 6; Table 4 |',
       '| Table S12 (`S12_direct_evidence.csv`) | Per-paper evaluated capabilities and evidence: EV1-EV6, trials, statistics, key metrics, runtime, uncertainty, hallucination mitigation, code/data release and key limitation (formerly main-text Table 6) | Sections 6, 7 and 9 |',
       '| Table S13 (`S13_datasets_benchmarks.csv`) | Per-resource inventory of datasets, simulators and benchmarks: size, sensors, human trajectories, group/intention, preference and multi-action labels, closed loop, VLM-readiness, FM role and limitations (the main-text Table 5 groups them into families) | Section 8; Table 5 |',
       '| Fig. S1 | FM roles (Dimension B) per direct paper, grouped by primary interface | Section 5.2; Table S11 |',
       '| Fig. S2 | Evidence profile (Dimension E) per direct paper, grouped by primary interface | Section 9; Table S12 |',
       '| Fig. S3 | Capability coding (Dimension C) per direct paper | Section 7 |',
       '| Fig. S4 | Dated timeline of the paradigms of social representation (overlapping bands; no causal ordering) | Section 3; Table 3 |', '',
       NOTATION.strip(), '',
       '**Pre-FM comparison set (S5):** "Not determinable" marks evidence that the reference-survey descriptions used for coding do not establish; such works are excluded from evidence denominators. Every work in Table S5 (parts A and B) is cited by its key and listed in full in the reference list at the end of this supplement.', '',
       '## Reproducibility', '',
       '- Every table in this supplement, like every count in the manuscript, is generated from the per-paper records.',
       '- Coding followed the five-dimensional scheme defined in the main manuscript (Section 5). Repeat-coding and metric-based consistency checks (Section 2.5) were used to assess internal consistency; these checks do not constitute inter-rater reliability.']
open(os.path.join(H, 'Supplementary_Material.md'), 'w').write('\n'.join(idx) + '\n')
json.dump(n, open(os.path.join(H, 'row_counts.json'), 'w'), indent=1); print(n)

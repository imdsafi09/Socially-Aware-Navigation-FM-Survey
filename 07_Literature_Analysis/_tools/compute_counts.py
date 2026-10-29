"""Compute corpus statistics ONLY from the CSV matrices in 07_Literature_Analysis.
Writes 07_Literature_Analysis/corpus_counts.json and prints a markdown report used in 09_Project_Reports."""
import csv, json, os, collections, re

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def read(n): return list(csv.DictReader(open(os.path.join(OUT, n))))


def pct(a, b): return f'{a}/{b} ({100*a/b:.1f}%)' if b else f'{a}/0'


master = read('master_literature_matrix.csv')
direct = read('direct_vlm_social_navigation_matrix.csv')
caps = read('social_capabilities_matrix.csv')
ev = read('evidence_maturity_matrix.csv')
dep = read('deployment_runtime_matrix.csv')
rep = read('reproducibility_matrix.csv')
C = {}

# ---- corpus level
n_unique = len(master)
dups = [m for m in master if m['duplicate_copies'].strip()]
n_dup_files = sum(len([x for x in m['duplicate_copies'].split('; ') if x.strip()]) for m in dups)
C['total_pdfs'] = n_unique + n_dup_files
C['unique_papers'] = n_unique
C['papers_with_duplicate_pdf_copies'] = len(dups)
C['duplicate_pdf_files'] = n_dup_files
C['papers_with_related_versions_noted'] = sum(1 for m in master if m['related_versions'].strip())
C['peer_reviewed'] = collections.Counter(m['peer_reviewed'] for m in master)
C['peer_reviewed_via_external_citation'] = [m['id'] for m in master if m['peer_reviewed'] == 'Yes' and not str(m.get('ext_status_class', '')).startswith('A') and re.search(r'cite|citation|reference list', m['peer_review_basis'], re.I)]
C['external_status_class'] = dict(collections.Counter(str(m.get('ext_status_class', ''))[:1] or 'none' for m in master))
C['direct_external_status_class'] = dict(collections.Counter(str(m.get('ext_status_class', ''))[:1] or 'none' for m in master if m['direct_fm_social'] == 'Yes'))
C['stage2_added'] = [m['id'] for m in master if m.get('stage2_added') == 'Yes']
C['taxonomy_review_required'] = {m['id']: m['taxonomy_review_required'] for m in master if m.get('taxonomy_review_required')}
C['analytical_category'] = collections.Counter(m['analytical_category'] for m in master)
C['physical_folder'] = collections.Counter(m['physical_source_folder'] for m in master)
C['folder_vs_category'] = collections.Counter(f"{m['physical_source_folder']} -> {m['analytical_category']}" for m in master)
C['folder_category_match'] = collections.Counter(m['folder_category_match'] for m in master)
C['per_year'] = dict(sorted(collections.Counter(m['year'] for m in master).items()))
C['fm_used'] = collections.Counter(m['fm_used'] for m in master)
C['fm_social_benchmarks'] = [m['id'] for m in master if m['fm_social_benchmark'] == 'Yes']
C['evidence_all_nonsurvey'] = collections.Counter(e['legacy_E_evidence'] for e in ev if e['analytical_category'] != 'S0')

# ---- direct set
D = direct; nD = len(D)
C['direct_total'] = nD
C['direct_peer_reviewed'] = collections.Counter(d['peer_reviewed'] for d in D)
C['direct_per_year'] = dict(sorted(collections.Counter(d['year'] for d in D).items()))
roles = collections.Counter()
for d in D:
    for r in [x.strip() for x in d['legacy_F_roles'].split(';') if x.strip()]: roles[r] += 1
C['direct_roles'] = {f'F{i}': roles.get(f'F{i}', 0) for i in range(1, 12)}
C['direct_integration'] = {f'I{i}': sum(1 for d in D if d['legacy_I_integration'] == f'I{i}') for i in range(8)}
C['direct_evidence'] = {f'E{i}': sum(1 for d in D if d['legacy_E_evidence'] == f'E{i}') for i in range(6)}
dids = {d['id'] for d in D}
capD = [c for c in caps if c['id'] in dids]
capcols = [k for k in caps[0].keys() if re.match(r'legacy_C\d+_', k)]
C['direct_capabilities'] = {k[7:]: dict(collections.Counter(c[k] for c in capD)) for k in capcols}
C['direct_offline_only_E0_E1'] = sum(1 for d in D if d['legacy_E_evidence'] in ('E0', 'E1'))
C['direct_simulation_only_E2'] = sum(1 for d in D if d['legacy_E_evidence'] == 'E2')
C['direct_real_robot_systematic'] = sum(1 for d in D if d['coding_real_robot'] == 'Systematic')
C['direct_real_robot_demo_only'] = sum(1 for d in D if d['coding_real_robot'] == 'Demo')
C['direct_real_robot_any'] = C['direct_real_robot_systematic'] + C['direct_real_robot_demo_only']
C['direct_formal_human_study'] = sum(1 for d in D if d['coding_human_subject_study'] == 'Yes')
C['direct_text_raters_only'] = sum(1 for d in D if d['coding_human_subject_study'].startswith('Text'))
for k in ['latency_reported', 'safety_mechanism', 'uncertainty_treatment', 'hallucination_treatment',
          'code_released', 'new_dataset_released']:
    C['direct_' + k] = dict(collections.Counter(d['coding_' + k] for d in D))
closed = [d for d in D if d['legacy_E_evidence'] in ('E2', 'E3', 'E4', 'E5')]
C['direct_closed_loop_total'] = len(closed)
C['direct_closed_loop_safety_yes'] = sum(1 for d in closed if d['coding_safety_mechanism'] == 'Yes')
C['direct_closed_loop_latency_yes'] = sum(1 for d in closed if d['coding_latency_reported'] == 'Yes')
# critic vs controller grouping by integration level
grp = {'offline decision/classification (I0-I1)': ('I0', 'I1'),
       'semantic representation/critic/cost (I2-I4)': ('I2', 'I3', 'I4'),
       'waypoint/policy/direct action (I5-I7)': ('I5', 'I6', 'I7')}
C['direct_integration_groups'] = {g: sum(1 for d in D if d['legacy_I_integration'] in v) for g, v in grp.items()}
# capability prevalence (Yes / Yes+Partial)
prev = {}
for k in capcols:
    yes = sum(1 for c in capD if c[k] == 'Yes'); part = sum(1 for c in capD if c[k] == 'Partial')
    prev[k[7:]] = {'Yes': yes, 'Yes_or_Partial': yes + part}
C['direct_capability_prevalence'] = prev
# capability prevalence among closed-loop direct papers
cl_ids = {d['id'] for d in closed}
C['direct_closedloop_capability_yes'] = {k[7:]: sum(1 for c in capD if c['id'] in cl_ids and c[k] == 'Yes') for k in capcols}

# cross-tabulations used in reports
def xtab(rows, a, b): 
    t = collections.defaultdict(collections.Counter)
    for r in rows: t[r[a]][r[b]] += 1
    return {k: dict(sorted(v.items())) for k, v in sorted(t.items())}
C['direct_xtab_integration_evidence'] = xtab(D, 'legacy_I_integration', 'legacy_E_evidence')
C['direct_xtab_peer_reviewed_evidence'] = xtab(D, 'peer_reviewed', 'legacy_E_evidence')
C['direct_xtab_year_evidence'] = xtab(D, 'year', 'legacy_E_evidence')
C['direct_xtab_real_robot_safety'] = xtab(D, 'coding_real_robot', 'coding_safety_mechanism')
C['direct_xtab_real_robot_latency'] = xtab(D, 'coding_real_robot', 'coding_latency_reported')
C['direct_closed_loop_integration'] = dict(sorted(collections.Counter(d['legacy_I_integration'] for d in closed).items()))
C['direct_offline_ids'] = sorted(d['id'] for d in D if d['legacy_E_evidence'] in ('E0', 'E1'))
C['direct_human_study_ids'] = sorted(d['id'] for d in D if d['coding_human_subject_study'] == 'Yes')
C['direct_real_robot_systematic_ids'] = sorted(d['id'] for d in D if d['coding_real_robot'] == 'Systematic')

met = read('evaluation_metrics_matrix.csv')
C['metric_rows_total'] = len(met)
C['metric_rows_direct'] = sum(1 for m in met if m['direct_fm_social'] == 'Yes')
C['metric_categories_direct'] = dict(collections.Counter(m['metric_category'] for m in met if m['direct_fm_social'] == 'Yes').most_common())
C['direct_limitation_flags'] = dict(collections.Counter(f for d in D for f in d['limitations_flags'].split('; ') if f).most_common())


# ================= Stage-3 FINAL taxonomy counts (authoritative) =================
def lst(v): return [x.strip() for x in str(v).split(';') if x.strip() and x.strip() != 'NA']
F = {}
F['note'] = 'Authoritative Stage-3 codes (final_* columns). Keys outside this block are legacy Stage-1/2 codes (F/I/E/C).'
F['direct_total'] = nD
F['A_social_representation_direct'] = dict(sorted(collections.Counter(a for d in D for a in lst(d['final_A_social_representation'])).items()))
F['A_social_representation_by_category'] = {cat: dict(sorted(collections.Counter(a for m in master if m['analytical_category'] == cat for a in lst(m['final_A_social_representation'])).items())) for cat in ['S1', 'S2', 'S3', 'S4', 'S5', 'S6']}
F['A_social_representation_n_by_category'] = {cat: sum(1 for m in master if m['analytical_category'] == cat) for cat in ['S1', 'S2', 'S3', 'S4', 'S5', 'S6']}
F['B_roles'] = dict(sorted(collections.Counter(r for d in D for r in lst(d['final_B_roles'])).items()))
F['B_roles_per_paper'] = dict(sorted(collections.Counter(len(lst(d['final_B_roles'])) for d in D).items()))
F['D_interface'] = dict(sorted(collections.Counter(r for d in D for r in lst(d['final_D_interface'])).items()))
F['D_interface_per_paper'] = dict(sorted(collections.Counter(len(lst(d['final_D_interface'])) for d in D).items()))
F['temporal_coupling'] = dict(sorted(collections.Counter(d['final_xc_temporal_coupling'] for d in D).items()))
for k in ['EV1_offline', 'EV2_closed_loop_sim', 'EV3_physical_robot', 'EV4_real_humans_in_trials', 'EV5_human_evaluation', 'EV6_open_world_deployment']:
    F[k] = dict(sorted(collections.Counter(d['final_' + k] for d in D).items()))
F['EV_profiles'] = dict(collections.Counter('|'.join([d['final_EV1_offline'][0], d['final_EV2_closed_loop_sim'][0], d['final_EV3_physical_robot'], d['final_EV5_human_evaluation']]) for d in D).most_common())
F['EV_no_closed_loop'] = sum(1 for d in D if d['final_EV2_closed_loop_sim'] == 'No' and d['final_EV3_physical_robot'] != 'systematic')
F['EV_sim_only'] = sum(1 for d in D if d['final_EV2_closed_loop_sim'] == 'Yes' and d['final_EV3_physical_robot'] != 'systematic')
F['EV_robot_systematic_with_real_humans'] = sum(1 for d in D if d['final_EV3_physical_robot'] == 'systematic' and d['final_EV4_real_humans_in_trials'] in ('staged', 'unscripted', 'present-type-unreported'))
F['EV_robot_systematic_unscripted_humans'] = sum(1 for d in D if d['final_EV3_physical_robot'] == 'systematic' and d['final_EV4_real_humans_in_trials'] == 'unscripted')
F['EV_statistical_testing_yes'] = sum(1 for d in D if str(d['final_quality_statistical_testing']).startswith('Yes'))
F['EV_cross_environment'] = sum(1 for d in D if d['final_quality_cross_environment'] == 'Yes')
LEAF = ['SAF1', 'SAF2', 'SPA1', 'SPA2', 'SPA3', 'SPA4', 'HUM1', 'HUM2', 'NOR1', 'NOR2', 'NOR3', 'NOR4', 'EXP1', 'EXP2', 'EXP3']
cd = {c['id']: c for c in caps}
F['C_leaves'] = {l: {'Yes': sum(1 for d in D if cd[d['id']]['final_' + l] == 'Yes'), 'Yes_or_Partial': sum(1 for d in D if cd[d['id']]['final_' + l] in ('Yes', 'Partial'))} for l in LEAF}
fam = {'SAF': ['SAF1', 'SAF2'], 'SPA': ['SPA1', 'SPA2', 'SPA3', 'SPA4'], 'HUM': ['HUM1', 'HUM2'], 'NOR': ['NOR1', 'NOR2', 'NOR3', 'NOR4'], 'EXP': ['EXP1', 'EXP2', 'EXP3']}
F['C_families'] = {f: {'Yes': sum(1 for d in D if any(cd[d['id']]['final_' + l] == 'Yes' for l in ls)), 'Yes_or_Partial': sum(1 for d in D if any(cd[d['id']]['final_' + l] in ('Yes', 'Partial') for l in ls))} for f, ls in fam.items()}
F['C_leaves_all_nonsurvey'] = {l: sum(1 for c in caps if c['analytical_category'] != 'S0' and c['final_' + l] == 'Yes') for l in LEAF}
F['xc'] = {k: dict(collections.Counter(str(d['final_xc_' + k])[:60] for d in D)) for k in ['memory', 'continual_adaptation', 'explanation_output', 'safety_guard', 'uncertainty', 'hallucination_mitigation', 'privacy_constraint', 'inference_location']}
F['xtab_interface_EV3'] = {i: dict(collections.Counter(d['final_EV3_physical_robot'] for d in D if i in lst(d['final_D_interface']))) for i in sorted(F['D_interface'])}
F['xtab_role_interface'] = {r: dict(collections.Counter(i for d in D if r in lst(d['final_B_roles']) for i in lst(d['final_D_interface']))) for r in sorted(F['B_roles'])}
C['final'] = F
json.dump(C, open(os.path.join(OUT, 'corpus_counts.json'), 'w'), indent=1, default=dict)

# ---- markdown print
def line(*a): print(*a)
line('## Corpus level')
line(f"- Total PDFs: {C['total_pdfs']}; unique papers: {C['unique_papers']}; duplicate PDF files: {C['duplicate_pdf_files']} (in {C['papers_with_duplicate_pdf_copies']} papers); papers with related versions noted: {C['papers_with_related_versions_noted']}")
line(f"- Peer-reviewed: {dict(C['peer_reviewed'])}")
line(f"- Analytical categories: {dict(sorted(C['analytical_category'].items()))}")
line(f"- Per year: {C['per_year']}")
line(f"- FM-based social benchmarks/datasets: {C['fm_social_benchmarks']}")
line('## Direct set')
line(f"- Total {nD}; peer review {dict(C['direct_peer_reviewed'])}; per year {C['direct_per_year']}")
line(f"- Roles {C['direct_roles']}")
line(f"- Integration {C['direct_integration']}; groups {C['direct_integration_groups']}")
line(f"- Evidence {C['direct_evidence']}")
line(f"- offline-only {pct(C['direct_offline_only_E0_E1'],nD)}; sim-only {pct(C['direct_simulation_only_E2'],nD)}; real-robot systematic {pct(C['direct_real_robot_systematic'],nD)}; demo-only {pct(C['direct_real_robot_demo_only'],nD)}; formal human study {pct(C['direct_formal_human_study'],nD)}; text-raters only {pct(C['direct_text_raters_only'],nD)}")
for k in ['latency_reported', 'safety_mechanism', 'uncertainty_treatment', 'hallucination_treatment', 'code_released', 'new_dataset_released']:
    line(f"- {k}: {C['direct_'+k]}")
line(f"- closed-loop {C['direct_closed_loop_total']}: safety Yes {C['direct_closed_loop_safety_yes']}, latency Yes {C['direct_closed_loop_latency_yes']}")
line('- capability prevalence (Yes / Yes+Partial):')
for k, v in prev.items(): line(f"  - {k}: {v['Yes']} / {v['Yes_or_Partial']}  (closed-loop Yes: {C['direct_closedloop_capability_yes'][k]})")

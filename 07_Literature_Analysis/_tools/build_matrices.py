"""Build the 12 Stage-1 matrices and corpus counts directly from 08_Paper_Notes YAML front matter.
Usage: python3 07_Literature_Analysis/_tools/build_matrices.py
Every row carries note_file and source_pdf for traceability. Values are copied from notes; nothing is
re-typed. Derived counts are written to 07_Literature_Analysis/corpus_counts.json."""
import yaml, glob, os, csv, json, collections, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
NOTES = os.path.join(ROOT, '08_Paper_Notes')
OUT = os.path.join(ROOT, '07_Literature_Analysis')
CATLABEL = {'S0': 'Existing survey/review/guidelines', 'S1': 'Classical social navigation',
            'S2': 'Learning-based social navigation', 'S3': 'Adjacent foundation-model navigation',
            'S4': 'Direct FM social navigation (peer-reviewed)', 'S5': 'Direct FM social navigation (preprint/accepted-not-indexed/unclear)',
            'S6': 'Dataset/benchmark/simulator/evaluation'}
CAPS = [f'C{i}' for i in range(1, 26)]
CAPNAMES = ['Physical collision safety', 'Near-collision avoidance', 'Proxemics/personal space', 'Perceived safety',
            'Human motion understanding', 'Trajectory prediction', 'Human-intention inference', 'Activity understanding',
            'Group awareness', 'F-formation/conversation preservation', 'Social etiquette', 'Yielding',
            'Passing convention', 'Doorway behavior', 'Crosswalk/sidewalk behavior', 'Queue behavior', 'Crowd behavior',
            'Legibility', 'Predictability', 'Naturalness', 'Human comfort', 'Politeness',
            'Explicit social instruction following', 'Context-dependent behavior', 'Cultural/social-norm adaptation']
ROLES = [f'F{i}' for i in range(1, 12)]
ROLENAMES = ['Semantic scene interpreter', 'Human intention/activity inference', 'Group/social-relation inference',
             'Social-rule reasoner', 'Path/trajectory critic', 'Cost/reward/constraint generator',
             'High-level task planner', 'Policy-learning/distillation teacher', 'Waypoint/trajectory generator',
             'Direct policy/VLA action generator', 'Benchmark/evaluator/annotator']


def s(v):
    if v is None: return 'Not reported'
    if isinstance(v, bool): return 'Yes' if v else 'No'  # YAML 1.1 reads unquoted Yes/No as booleans
    if isinstance(v, list): return '; '.join(s(x) for x in v) if v else ''
    if isinstance(v, dict): return '; '.join(f'{k}: {s(x)}' for k, x in v.items())
    return str(v)


def load():
    P = []
    for f in sorted(glob.glob(NOTES + '/*.md')):
        y = yaml.safe_load(open(f).read().split('---', 2)[1])
        y['_note'] = '08_Paper_Notes/' + os.path.basename(f)
        P.append(y)
    return P


def is_direct(y): return y['analytical_category'] in ('S4', 'S5')


def is_fm_social_benchmark(y):
    caps = y.get('capabilities') or {}
    return (y['analytical_category'] == 'S6' and str(y.get('fm_used')) == 'Yes'
            and any(str(caps.get(c)) in ('Yes', 'Partial') for c in CAPS))


def base(y):
    a = y.get('authors') or []
    first = a[0] if a else 'Not reported'
    return {'id': y['id'], 'first_author': first, 'year': y['year'], 'title': y['title'],
            'analytical_category': y['analytical_category'],
            'analytical_category_label': CATLABEL[y['analytical_category']],
            'physical_source_folder': y['physical_source_folder'], 'source_pdf': y['source_pdfs'][0],
            'note_file': y['_note']}


LEGACY = {'roles': 'legacy_F_roles', 'integration': 'legacy_I_integration', 'evidence': 'legacy_E_evidence'}
def legacy_rename(r):
    return {(LEGACY.get(k) or ('legacy_' + k if re.match(r'C\d+_', k) else k)): v for k, v in r.items()}
LEAF = ['SAF1', 'SAF2', 'SPA1', 'SPA2', 'SPA3', 'SPA4', 'HUM1', 'HUM2', 'NOR1', 'NOR2', 'NOR3', 'NOR4', 'EXP1', 'EXP2', 'EXP3']
def final_cols(y, full=False):
    fc = y.get('final_coding') or {}
    if fc.get('status'): return {'final_A_social_representation': 'NA'}
    r = {'final_A_social_representation': fc.get('A_social_representation'), 'final_B_roles': fc.get('B_roles'), 'final_D_interface': fc.get('D_interface')}
    for k, v in (fc.get('E_evidence_profile') or {}).items(): r['final_' + k] = v
    if full:
        for k, v in (fc.get('E_quality_attributes') or {}).items(): r['final_quality_' + k] = v
        for k, v in (fc.get('cross_cutting') or {}).items(): r['final_xc_' + k] = v
        caps = fc.get('C_capabilities') or {}
        r['final_C_leaves_Yes'] = [l for l in LEAF if caps.get(l) == 'Yes']
        r['final_C_leaves_Partial'] = [l for l in LEAF if caps.get(l) == 'Partial']
    return r

def write(name, rows, cols=None):
    rows = [legacy_rename(r) for r in rows]
    if cols: cols = [LEGACY.get(c) or ('legacy_' + c if re.match(r'C\d+_', c) else c) for c in cols]
    if not rows: rows = [{}]
    if not cols:  # union of keys over all rows, first-seen order (rows can carry optional blocks)
        cols = []
        for r in rows:
            cols += [k for k in r if k not in cols]
    with open(os.path.join(OUT, name), 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction='ignore')
        w.writeheader()
        for r in rows: w.writerow({k: s(r.get(k, '')) for k in cols})
    return len(rows)


def main():
    P = load()
    sizes = {}
    # 1 master
    rows = []
    for y in P:
        r = base(y)
        r.update({'authors': y.get('authors'), 'venue': y.get('venue'), 'volume': y.get('volume'),
                  'issue': y.get('issue'), 'pages': y.get('pages'), 'doi': y.get('doi'), 'url': y.get('url'),
                  'pub_status': y.get('pub_status'), 'peer_reviewed': y.get('peer_reviewed'),
                  'peer_review_basis': y.get('peer_review_basis'), 'duplicate_copies': y.get('duplicate_copies'),
                  'related_versions': y.get('related_versions'), 'folder_category_match': y.get('folder_category_match'),
                  'category_rationale': y.get('category_rationale'), 'paper_type': y.get('paper_type'),
                  'fm_used': y.get('fm_used'), 'fm_class': y.get('fm_class'), 'fm_models': y.get('fm_models'),
                  'fm_size': y.get('fm_size'), 'method_family': y.get('method_family'), 'roles': y.get('roles'),
                  'integration': y.get('integration'), 'evidence': y.get('evidence'),
                  'evidence_rationale': y.get('evidence_rationale'), 'real_robot': y['coding']['real_robot'],
                  'human_subject_study': y['coding']['human_subject_study'],
                  'web_verification_required': y.get('web_verification_required'),
                  'direct_fm_social': 'Yes' if is_direct(y) else 'No',
                  'fm_social_benchmark': 'Yes' if is_fm_social_benchmark(y) else 'No'})
        r.update(final_cols(y))
        ev = y.get('external_verification') or {}
        st2 = y.get('stage2') or {}
        r.update({'ext_status_class': ev.get('status_class'), 'ext_verified_on': ev.get('verified_on'),
                  'ext_arxiv': ev.get('arxiv', ev.get('arxiv_id')), 'ext_version_relationship': ev.get('version_relationship'),
                  'ext_sources': ev.get('sources', ev.get('source')), 'stage2_added': 'Yes' if st2.get('added') else 'No', 'final_search_added': 'Yes' if str(st2.get('added_stage', '')).startswith('final coverage search') else 'No',
                  'stage2_download_source': st2.get('download_source', ''),
                  'taxonomy_review_required': st2.get('taxonomy_review_required', ''),
                  'snei_usage': y.get('snei_usage', '')})
        rows.append(r)
    sizes['master_literature_matrix.csv'] = write('master_literature_matrix.csv', rows)
    # 2 surveys
    rows = []
    for y in P:
        if 'survey' not in y: continue
        r = base(y); sv = y['survey']
        r.update({'venue': y.get('venue'), 'peer_reviewed': y.get('peer_reviewed'), 'paper_type': y.get('paper_type')})
        for k in ['scope', 'years_covered', 'search_strategy', 'inclusion', 'exclusion', 'n_papers', 'n_refs', 'taxonomy',
                  'taxonomy_dims', 'datasets_covered', 'simulators_covered', 'metrics_covered']:
            r[k] = sv.get(k)
        for k, v in (sv.get('coverage') or {}).items(): r['cov_' + k] = v
        for k, v in (sv.get('stage2_coverage') or {}).items(): r['s2_' + k] = v
        rows.append(r)
    sizes['existing_surveys_matrix.csv'] = write('existing_surveys_matrix.csv', rows)
    # 3 classical (all notes with classical block, incl. IRL papers coded S2)
    rows = []
    for y in P:
        if 'classical' not in y: continue
        r = base(y); r.update({'evidence': y.get('evidence'), 'method_family': y.get('method_family')})
        for k, v in y['classical'].items(): r[k] = v
        rows.append(r)
    sizes['classical_social_navigation_matrix.csv'] = write('classical_social_navigation_matrix.csv', rows)
    # 4 learning
    rows = []
    for y in P:
        if 'learning' not in y: continue
        r = base(y); r.update({'evidence': y.get('evidence'), 'method_family': y.get('method_family')})
        for k, v in y['learning'].items(): r[k] = v
        rows.append(r)
    sizes['learning_based_social_navigation_matrix.csv'] = write('learning_based_social_navigation_matrix.csv', rows)
    # 5 adjacent
    rows = []
    for y in P:
        if y['analytical_category'] != 'S3': continue
        r = base(y)
        r.update({'fm_class': y.get('fm_class'), 'fm_models': y.get('fm_models'), 'roles': y.get('roles'),
                  'integration': y.get('integration'), 'evidence': y.get('evidence'),
                  'real_robot': y['coding']['real_robot']})
        for k, v in (y.get('adjacent') or {}).items(): r['adj_' + k] = v
        rows.append(r)
    sizes['adjacent_foundation_model_matrix.csv'] = write('adjacent_foundation_model_matrix.csv', rows)
    # 6 direct
    rows = []
    for y in P:
        if not is_direct(y): continue
        r = base(y); e = y.get('exp') or {}
        r.update({'venue': y.get('venue'), 'peer_reviewed': y.get('peer_reviewed'), 'fm_class': y.get('fm_class'),
                  'fm_models': y.get('fm_models'), 'fm_size': y.get('fm_size'), 'method_family': y.get('method_family'),
                  'roles': y.get('roles'), 'integration': y.get('integration'),
                  'integration_rationale': y.get('integration_rationale'), 'evidence': y.get('evidence'),
                  'evidence_rationale': y.get('evidence_rationale'), 'inputs': y.get('inputs'),
                  'outputs': y.get('outputs'), 'human_repr': y.get('human_repr'),
                  'datasets': e.get('datasets'), 'simulators': e.get('simulators'), 'robots': e.get('robots'),
                  'environment': e.get('environment'), 'scenarios': e.get('scenarios'), 'baselines': e.get('baselines'),
                  'real_robot_trials': e.get('real_robot_trials'), 'human_study': e.get('human_study'),
                  'statistical_testing': e.get('statistical_testing')})
        for k, v in y['coding'].items(): r['coding_' + k] = v
        r['limitations_flags'] = y.get('limitations_flags')
        r.update(final_cols(y, full=True))
        rows.append(r)
    sizes['direct_vlm_social_navigation_matrix.csv'] = write('direct_vlm_social_navigation_matrix.csv', rows)
    # 7 datasets/benchmarks: all S6 + any paper releasing a new dataset
    rows = []
    for y in P:
        if not (y['analytical_category'] == 'S6' or y['coding']['new_dataset_released'] == 'Yes' or 'dataset' in y): continue
        r = base(y); r.update({'paper_type': y.get('paper_type'), 'fm_used': y.get('fm_used'),
                               'new_dataset_released': y['coding']['new_dataset_released']})
        for k, v in (y.get('dataset') or {}).items(): r['ds_' + k] = v
        rows.append(r)
    sizes['datasets_benchmarks_matrix.csv'] = write('datasets_benchmarks_matrix.csv', rows)
    # 8 metrics (long format)
    rows = []
    for y in P:
        for m in y.get('metrics') or []:
            parts = [p.strip() for p in str(m).split('|')]
            parts += [''] * (5 - len(parts))
            r = base(y)
            r.update({'metric_category': parts[0], 'metric_name': parts[1], 'unit': parts[2], 'definition': parts[3],
                      'page': parts[4] if len(parts) == 5 else ' | '.join(parts[4:]),
                      'direct_fm_social': 'Yes' if is_direct(y) else 'No'})
            rows.append(r)
    sizes['evaluation_metrics_matrix.csv'] = write('evaluation_metrics_matrix.csv', rows)
    # 9 social capabilities
    rows = []
    for y in P:
        caps = y.get('capabilities') or {}
        if all(str(caps.get(c)) == 'NA' for c in CAPS): continue
        r = base(y); r.update({'evidence': y.get('evidence'), 'direct_fm_social': 'Yes' if is_direct(y) else 'No'})
        fcc = (y.get('final_coding') or {}).get('C_capabilities') or {}
        for l in LEAF: r['final_' + l] = fcc.get(l, 'NA')
        for c, n in zip(CAPS, CAPNAMES): r[f'{c}_{n}'] = caps.get(c, 'Not reported')
        rows.append(r)
    capcols = list(rows[0].keys())  # renamed to legacy_ for C-columns by write()
    sizes['social_capabilities_matrix.csv'] = write('social_capabilities_matrix.csv', rows, capcols)
    # 10 evidence maturity
    rows = []
    for y in P:
        r = base(y); e = y.get('exp') or {}
        r.update({'evidence': y.get('evidence'), 'evidence_rationale': y.get('evidence_rationale'),
                  'integration': y.get('integration'), 'real_robot': y['coding']['real_robot'],
                  'human_subject_study': y['coding']['human_subject_study'],
                  'real_robot_trials_note': e.get('real_robot_trials'), 'human_study_note': e.get('human_study'),
                  'statistical_testing': e.get('statistical_testing'), 'simulators': e.get('simulators'),
                  'direct_fm_social': 'Yes' if is_direct(y) else 'No'})
        r.update(final_cols(y))
        rows.append(r)
    sizes['evidence_maturity_matrix.csv'] = write('evidence_maturity_matrix.csv', rows)
    # 11 deployment/runtime
    rows = []
    for y in P:
        if y['analytical_category'] == 'S0': continue
        r = base(y); r['fm_used'] = y.get('fm_used')
        for k, v in (y.get('deployment') or {}).items(): r[k] = v
        for k in ['latency_reported', 'safety_mechanism', 'uncertainty_treatment', 'hallucination_treatment']:
            r['coding_' + k] = y['coding'][k]
        r['direct_fm_social'] = 'Yes' if is_direct(y) else 'No'
        for k, v in ((y.get('final_coding') or {}).get('cross_cutting') or {}).items(): r['final_xc_' + k] = v
        rows.append(r)
    sizes['deployment_runtime_matrix.csv'] = write('deployment_runtime_matrix.csv', rows)
    # 12 reproducibility
    rows = []
    for y in P:
        r = base(y)
        for k, v in (y.get('repro') or {}).items(): r[k] = v
        r['coding_code_released'] = y['coding']['code_released']
        r['coding_new_dataset_released'] = y['coding']['new_dataset_released']
        r['direct_fm_social'] = 'Yes' if is_direct(y) else 'No'
        rows.append(r)
    sizes['reproducibility_matrix.csv'] = write('reproducibility_matrix.csv', rows)
    json.dump(sizes, open(os.path.join(OUT, '_tools', 'matrix_row_counts.json'), 'w'), indent=1)
    print(json.dumps(sizes, indent=1))


if __name__ == '__main__':
    main()

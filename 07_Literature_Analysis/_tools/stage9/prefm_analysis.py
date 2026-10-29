"""Stage 9: cross-paradigm comparison of the pre-FM comparison set with the direct FM papers.
Writes 07_Literature_Analysis/prefm_comparison_stats.json (read by 10_PreWriting/build_findings.py) and prints a summary.
Pooled shares, paradigm-balanced shares (mean of within-paradigm shares) and two sensitivity subsets (full-text-coded only; the
12 frozen-corpus works) are reported. 'ND' evidence values are excluded from evidence denominators and counted separately."""
import csv, os, json, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..')); A = os.path.join(ROOT, '07_Literature_Analysis')
LEAVES = ['SAF1', 'SAF2', 'SPA1', 'SPA2', 'SPA3', 'SPA4', 'HUM1', 'HUM2', 'NOR1', 'NOR2', 'NOR3', 'NOR4', 'EXP1', 'EXP2', 'EXP3']
FAM = {'SAF': LEAVES[0:2], 'SPA': LEAVES[2:6], 'HUM': LEAVES[6:8], 'NOR': LEAVES[8:12], 'EXP': LEAVES[12:15]}
P = list(csv.DictReader(open(os.path.join(A, 'prefm_comparison_set.csv'))))
for r in P: r['Y'] = set(r['cap_yes'].split()); r['YP'] = r['Y'] | set(r['cap_partial'].split()); r['Aset'] = set(r['A'].split())
CAP = {r['id']: r for r in csv.DictReader(open(os.path.join(A, 'social_capabilities_matrix.csv')))}
EVM = {r['id']: r for r in csv.DictReader(open(os.path.join(A, 'evidence_maturity_matrix.csv')))}
D = [r for r in csv.DictReader(open(os.path.join(A, 'direct_vlm_social_navigation_matrix.csv')))]
DIR = []
for d in D:
    c = CAP[d['id']]; e = EVM[d['id']]
    DIR.append({'id': d['id'], 'Y': {l for l in LEAVES if c['final_' + l] == 'Yes'}, 'YP': {l for l in LEAVES if c['final_' + l] in ('Yes', 'Partial')},
                'Aset': set(d['final_A_social_representation'].replace(';', ' ').split()), 'EV3': e['final_EV3_physical_robot'], 'EV5': e['final_EV5_human_evaluation'], 'EV6': e['final_EV6_open_world_deployment']})
def share(rows, f): return sum(1 for r in rows if f(r)), len(rows)
def stats(rows):
    out = {'n': len(rows)}
    out['A'] = {a: share(rows, lambda r, a=a: a in r['Aset'])[0] for a in ['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6']}
    out['eval'] = {l: share(rows, lambda r, l=l: l in r['Y'])[0] for l in LEAVES}
    out['addr'] = {l: share(rows, lambda r, l=l: l in r['YP'])[0] for l in LEAVES}
    out['fam_eval'] = {f: share(rows, lambda r, ls=ls: bool(r['Y'] & set(ls)))[0] for f, ls in FAM.items()}
    out['any_eval'] = share(rows, lambda r: bool(r['Y']))[0]
    return out
def evid(rows, key3, key5, key6):
    det3 = [r for r in rows if r[key3] != 'ND']; det5 = [r for r in rows if r[key5] != 'ND']
    return {'robot_systematic': sum(1 for r in det3 if r[key3] == 'systematic'), 'robot_any': sum(1 for r in det3 if r[key3] in ('systematic', 'demo')), 'robot_det': len(det3),
            'robot_ND': len(rows) - len(det3), 'human_eval': sum(1 for r in det5 if r[key5] not in ('none', 'text-raters')), 'human_det': len(det5), 'human_ND': len(rows) - len(det5),
            'open_world': sum(1 for r in rows if r[key6] == 'Yes')}
def balanced(rows, f):
    by = collections.defaultdict(list)
    for r in rows: by[r['paradigm']].append(r)
    vals = [sum(1 for r in g if f(r)) / len(g) for g in by.values()]
    return round(sum(vals) / len(vals), 3)
res = {'prefm': stats(P), 'direct': stats(DIR)}
res['prefm_evidence'] = evid(P, 'EV3_physical_robot', 'EV5_human_evaluation', 'EV6_open_world')
res['direct_evidence'] = evid([{**d, 'EV3x': d['EV3'], 'EV5x': d['EV5'], 'EV6x': d['EV6']} for d in DIR], 'EV3x', 'EV5x', 'EV6x')
FT = [r for r in P if r['coding_source'].startswith('full text')]; C12 = [r for r in P if r['in_frozen_corpus'] == 'Yes']
res['prefm_fulltext'] = {**stats(FT), 'evidence': evid(FT, 'EV3_physical_robot', 'EV5_human_evaluation', 'EV6_open_world')}
res['prefm_corpus12'] = {**stats(C12), 'evidence': evid(C12, 'EV3_physical_robot', 'EV5_human_evaluation', 'EV6_open_world')}
res['prefm_balanced'] = {f'eval_{l}': balanced(P, lambda r, l=l: l in r['Y']) for l in LEAVES}
res['prefm_balanced'].update({f'A_{a}': balanced(P, lambda r, a=a: a in r['Aset']) for a in ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']})
res['prefm_balanced']['robot_systematic'] = balanced([r for r in P if r['EV3_physical_robot'] != 'ND'], lambda r: r['EV3_physical_robot'] == 'systematic')
res['prefm_balanced']['human_eval'] = balanced([r for r in P if r['EV5_human_evaluation'] != 'ND'], lambda r: r['EV5_human_evaluation'] not in ('none', 'text-raters'))
res['by_paradigm'] = {}
for p in sorted({r['paradigm'] for r in P}, key=lambda s: int(s.split()[0][1:])):
    g = [r for r in P if r['paradigm'] == p]
    res['by_paradigm'][p] = {'n': len(g), 'fulltext': sum(1 for r in g if r['coding_source'].startswith('full text')),
                             'eval_leaves': dict(collections.Counter(l for r in g for l in r['Y'])),
                             'robot_systematic': sum(1 for r in g if r['EV3_physical_robot'] == 'systematic'), 'human_eval': sum(1 for r in g if r['EV5_human_evaluation'] not in ('none', 'text-raters', 'ND')),
                             'A5': sum(1 for r in g if 'A5' in r['Aset'])}
res['prefm_A5_works'] = [r['key'] for r in P if 'A5' in r['Aset']]
res['prefm_NOR_eval_works'] = {l: [r['key'] for r in P if l in r['Y']] for l in ['NOR1', 'NOR2', 'NOR3', 'NOR4']}
res['prefm_NOR_addr_works'] = {l: [r['key'] for r in P if l in r['YP']] for l in ['NOR1', 'NOR2', 'NOR3', 'NOR4']}
res['prefm_human_eval_works'] = [r['key'] for r in P if r['EV5_human_evaluation'] not in ('none', 'text-raters', 'ND')]
res['prefm_open_world_works'] = [r['key'] for r in P if r['EV6_open_world'] == 'Yes']
res['n_paradigms'] = len(res['by_paradigm']); res['n_fulltext'] = len(FT); res['n_secondary'] = len(P) - len(FT); res['n_new'] = len(P) - len(C12)
json.dump(res, open(os.path.join(A, 'prefm_comparison_stats.json'), 'w'), indent=1)
if __name__ == '__main__':
    pf, dr = res['prefm'], res['direct']
    print(f"pre-FM n={pf['n']} (full text {len(FT)}), direct n={dr['n']}")
    print('A     ', {a: (pf['A'][a], dr['A'][a]) for a in pf['A']})
    print('eval  ', {l: (pf['eval'][l], dr['eval'][l]) for l in LEAVES})
    print('addr  ', {l: (pf['addr'][l], dr['addr'][l]) for l in LEAVES})
    print('famev ', {f: (pf['fam_eval'][f], dr['fam_eval'][f]) for f in FAM}, 'any', pf['any_eval'], dr['any_eval'])
    print('evid  ', res['prefm_evidence'], res['direct_evidence'])
    print('FT    ', {l: res['prefm_fulltext']['eval'][l] for l in ['SPA4', 'HUM1', 'NOR2', 'NOR3', 'EXP1', 'EXP2']}, res['prefm_fulltext']['evidence'], 'A5', res['prefm_fulltext']['A']['A5'])
    print('C12   ', {l: res['prefm_corpus12']['eval'][l] for l in ['SPA4', 'HUM1', 'NOR2', 'NOR3']}, res['prefm_corpus12']['evidence'])
    print('bal   ', res['prefm_balanced'])
    for p, v in res['by_paradigm'].items(): print('  ', p[:40], v)
    print('A5 works', res['prefm_A5_works'], 'NOR eval', res['prefm_NOR_eval_works'], 'human eval', res['prefm_human_eval_works'], 'open world', res['prefm_open_world_works'])

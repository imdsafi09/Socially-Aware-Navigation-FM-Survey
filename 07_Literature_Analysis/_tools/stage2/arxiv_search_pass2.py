"""Stage 2 second (final) targeted search pass: 12 terminology families from the user's brief, 2025-01-01..2026-10-19.
Results: search/pass2_<family>.json and search/pass2_union.json."""
import json, os, time, importlib.util
spec = importlib.util.spec_from_file_location('s1', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'arxiv_search.py'))
src = open(spec.origin).read().split('union = ')[0].split('import sys\nonly')[0]
ns = {"__file__": spec.origin}; exec(src.replace("DATE = 'submittedDate:[202301010000 TO 202610162359]'", "DATE = 'submittedDate:[202501010000 TO 202610192359]'"), ns)
FM = ns['FM']; run = ns['run']; OUT = ns['OUT']
NAV = '(all:navigation OR all:navigate)'
FAM = {
 'P01_socially_intelligent_nav_FM': f'(all:"socially intelligent" OR all:"social intelligence") AND {NAV} AND {FM}',
 'P02_human_centric_VLM_nav': f'(all:"human-centric" OR all:"human-centered") AND {NAV} AND (all:VLM OR all:"vision-language" OR all:"vision language")',
 'P03_norm_aware_nav': f'(all:"norm-aware" OR all:"social norms" OR all:"social norm" OR all:normative) AND {NAV} AND {FM}',
 'P04_multimodal_social_robot_nav': f'all:multimodal AND (all:"social robot navigation" OR all:"social navigation" OR all:"socially aware navigation")',
 'P05_human_intention_VLM_nav': f'(all:"human intention" OR all:"pedestrian intention" OR all:"human intent") AND {NAV} AND {FM}',
 'P06_group_aware_nav_FM': f'(all:"group-aware" OR all:"social group" OR all:"social groups" OR all:"F-formation") AND {NAV} AND {FM}',
 'P07_language_conditioned_human_aware': f'(all:"language-conditioned" OR all:"language-guided" OR all:"language-instructed" OR all:instruction) AND (all:"human-aware" OR all:"socially aware" OR all:"socially-aware" OR all:"social navigation")',
 'P08_explanation_social_nav': f'(all:explanation OR all:explainable OR all:transparency OR all:explainability) AND (all:"social navigation" OR all:"socially aware navigation" OR all:"social robot navigation")',
 'P09_FM_human_aware_nav': f'(all:"human-aware" OR all:"human aware") AND {NAV} AND {FM}',
 'P10_embodied_social_reasoning': f'(all:"social reasoning" OR all:"embodied social") AND (all:robot OR all:embodied) AND {FM}',
 'P11_social_spatial_reasoning_nav': f'(all:"spatial reasoning" AND all:social) AND {NAV} AND {FM}',
 'P12_comfort_proxemic_LLM_nav': f'(all:comfort OR all:proxemics OR all:"personal space" OR all:etiquette) AND {NAV} AND {FM}',
}
union = {}
for k, q in FAM.items():
    hits, tot = run(q)
    json.dump({'family': k, 'query': q, 'run_date': time.strftime('%Y-%m-%d'), 'total_results': tot, 'hits': hits}, open(os.path.join(OUT, f'pass2_{k}.json'), 'w'), indent=1)
    for h in hits:
        u = union.setdefault(h['id'].rsplit('v', 1)[0], dict(h, families=[])); u['families'].append(k)
    print(k, 'total', tot, 'fetched', len(hits), flush=True)
json.dump(union, open(os.path.join(OUT, 'pass2_union.json'), 'w'), indent=1); print('union', len(union))

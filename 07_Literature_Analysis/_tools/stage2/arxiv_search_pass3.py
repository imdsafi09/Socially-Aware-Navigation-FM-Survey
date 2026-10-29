"""Stage 2 third (saturation-check) pass: 10 further terminology variants not used in passes 1-2, 2025-01-01..2026-10-19.
Results: search/pass3_<family>.json and search/pass3_union.json."""
import json, os, time, importlib.util
spec = importlib.util.spec_from_file_location('s1', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'arxiv_search.py'))
src = open(spec.origin).read().split('union = ')[0].split('import sys\nonly')[0]
ns = {"__file__": spec.origin}; exec(src.replace("DATE = 'submittedDate:[202301010000 TO 202610162359]'", "DATE = 'submittedDate:[202401010000 TO 202610192359]'"), ns)
FM = ns['FM']; run = ns['run']; OUT = ns['OUT']
NAV = '(all:navigation OR all:navigate)'
FAM = {
 'Q01_pedestrian_aware_FM_nav': f'(all:"pedestrian-aware" OR all:"pedestrian aware" OR all:"pedestrian-rich") AND {NAV} AND {FM}',
 'Q02_crowd_aware_FM_nav': f'(all:"crowd-aware" OR all:"crowd navigation" OR all:"dense crowds") AND {FM}',
 'Q03_social_VLN': f'(all:"social VLN" OR all:"social vision-language navigation" OR all:"dynamic VLN" OR all:"human-aware VLN")',
 'Q04_socially_compliant_VLA': f'(all:"socially compliant" OR all:"social compliance") AND (all:VLA OR all:"vision-language-action" OR all:"world model")',
 'Q05_human_robot_coexistence_nav': f'(all:"shared spaces" OR all:"human-populated" OR all:"human-inhabited" OR all:"public spaces") AND {NAV} AND {FM}',
 'Q06_legible_polite_nav_FM': f'(all:legible OR all:legibility OR all:polite OR all:politeness OR all:courteous) AND {NAV} AND {FM}',
 'Q07_social_costmap_language': f'(all:"social cost" OR all:"social costmap" OR all:"social constraints") AND {NAV} AND (all:language OR {FM})',
 'Q08_assistive_guide_robot_FM': f'(all:"guide robot" OR all:"guide dog" OR all:wheelchair OR all:"assistive navigation") AND (all:pedestrian OR all:social OR all:crowd) AND {FM}',
 'Q09_quadruped_humanoid_social_nav': f'(all:quadruped OR all:legged OR all:humanoid) AND (all:"social navigation" OR all:"socially aware" OR all:pedestrians) AND {FM}',
 'Q10_social_nav_LLM_reward_or_eval': f'(all:"social navigation" OR all:"crowd navigation") AND (all:reward OR all:evaluation OR all:benchmark) AND (all:LLM OR all:"large language model" OR all:VLM)',
}
union = {}
for k, q in FAM.items():
    hits, tot = run(q)
    json.dump({'family': k, 'query': q, 'run_date': time.strftime('%Y-%m-%d'), 'total_results': tot, 'hits': hits}, open(os.path.join(OUT, f'pass3_{k}.json'), 'w'), indent=1)
    for h in hits:
        u = union.setdefault(h['id'].rsplit('v', 1)[0], dict(h, families=[])); u['families'].append(k)
    print(k, 'total', tot, 'fetched', len(hits), flush=True)
json.dump(union, open(os.path.join(OUT, 'pass3_union.json'), 'w'), indent=1); print('union', len(union))

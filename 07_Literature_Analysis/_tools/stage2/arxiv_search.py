"""Stage 2 targeted search (Task 5): run each query family against the arXiv API (title+abstract fields),
restricted to submissions 2023-01-01..freeze date. Raw hits saved to search/arxiv_<family>.json; union saved to search/arxiv_union.json."""
import urllib.request, urllib.parse, time, json, os, sys
import xml.etree.ElementTree as ET
T = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(T, 'search')
NS = {'a': 'http://www.w3.org/2005/Atom', 'x': 'http://arxiv.org/schemas/atom'}
DATE = 'submittedDate:[202301010000 TO 202610162359]'
FM = '(all:"vision-language" OR all:"vision language" OR all:VLM OR all:LVLM OR all:"large language model" OR all:LLM OR all:"multimodal model" OR all:"foundation model" OR all:"vision-language-action" OR all:VLA OR all:MLLM)'
FAMILIES = {
 'F01_social_robot_nav_VLM': f'all:"social robot navigation" AND {FM}',
 'F02_socially_aware_nav': f'all:"socially aware navigation" AND {FM}',
 'F03_socially_compliant_nav': f'all:"socially compliant navigation" AND {FM}',
 'F04_human_aware_nav': f'all:"human-aware navigation" AND {FM}',
 'F05_social_navigation_generic': f'all:"social navigation" AND {FM}',
 'F06_crowd_navigation_FM': f'(all:"crowd navigation" OR all:"navigation in crowds" OR all:"crowded") AND all:robot AND {FM}',
 'F07_human_aware_VLN': '(all:"human-aware" OR all:"human-centric" OR all:"socially aware") AND (all:"vision-and-language navigation" OR all:VLN)',
 'F08_socially_aware_embodied_nav': '(all:"socially-aware" OR all:"socially aware" OR all:"social compliance") AND all:"embodied navigation"',
 'F09_social_nav_costmap_VLM': f'all:costmap AND (all:social OR all:pedestrian OR all:human) AND {FM}',
 'F10_social_nav_VLA': '(all:"vision-language-action" OR all:VLA) AND (all:social OR all:pedestrian OR all:crowd) AND all:navigation',
 'F11_proxemics_FM': f'(all:proxemics OR all:"personal space") AND all:robot AND {FM}',
 'F12_social_nav_dataset_language': '(all:"social navigation" OR all:"social robot navigation") AND (all:dataset OR all:benchmark) AND (all:language OR all:VQA OR all:reasoning)',

 'F13_title_social_nav_absFM': f'ti:social AND ti:navigation AND {FM}',
 'F14_title_human_crowd_ped_nav_absFM': f'(ti:human OR ti:crowd OR ti:pedestrian OR ti:pedestrians OR ti:people) AND (ti:navigation OR ti:navigate) AND {FM}',
 'F15_human_centric_nav': f'(all:"human-centric" OR all:"human-populated" OR all:"human-crowded" OR all:"shared spaces") AND all:navigation AND {FM}',
 'F16_title_VLM_robot_nav_social_abs': '(ti:VLM OR ti:"vision-language" OR ti:"vision language" OR ti:LLM OR ti:"language model" OR ti:multimodal) AND ti:navigation AND (abs:social OR abs:pedestrian OR abs:pedestrians OR abs:crowd OR abs:etiquette OR abs:proxemic)',
}
def run(q):
    hits = []; start = 0
    while True:
        url = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query': f'({q}) AND {DATE}', 'start': start, 'max_results': 200, 'sortBy': 'submittedDate', 'sortOrder': 'descending'})
        for i in range(5):
            try: r = urllib.request.urlopen(url, timeout=90).read(); break
            except Exception: time.sleep(10 * (i + 1))
        root = ET.fromstring(r); es = root.findall('a:entry', NS)
        for e in es:
            g = lambda t: (e.find(t, NS).text if e.find(t, NS) is not None else None)
            hits.append({'id': g('a:id').split('/abs/')[-1], 'title': ' '.join(g('a:title').split()), 'published': g('a:published')[:10],
                         'updated': g('a:updated')[:10], 'comment': g('x:comment'), 'journal_ref': g('x:journal_ref'), 'doi': g('x:doi'),
                         'authors': [a.find('a:name', NS).text for a in e.findall('a:author', NS)], 'abstract': ' '.join(g('a:summary').split())})
        tot = int(root.find('{http://a9.com/-/spec/opensearch/1.1/}totalResults').text)
        start += 200; time.sleep(4)
        if start >= tot or not es or start >= 800: return hits, tot
import sys
only = sys.argv[1:]
union = json.load(open(os.path.join(OUT, 'arxiv_union.json'))) if only else {}
for k, q in FAMILIES.items():
    if only and k not in only: continue
    hits, tot = run(q)
    json.dump({'family': k, 'query': q, 'date_filter': DATE, 'run_date': time.strftime('%Y-%m-%d'), 'total_results': tot, 'hits': hits}, open(os.path.join(OUT, f'arxiv_{k}.json'), 'w'), indent=1)
    for h in hits:
        u = union.setdefault(h['id'].split('v')[0] if 'v' in h['id'][-3:] else h['id'], dict(h, families=[])); u['families'].append(k)
    print(k, 'total', tot, 'fetched', len(hits), flush=True)
json.dump(union, open(os.path.join(OUT, 'arxiv_union.json'), 'w'), indent=1)
print('union', len(union))

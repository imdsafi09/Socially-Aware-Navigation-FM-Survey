"""Stage 11 final coverage search (2026-10-26) on OpenAlex (indexes journal articles and proceedings from IEEE, ACM, Springer,
Elsevier etc., plus arXiv). Query families = the established social-navigation terms crossed with FM terms, searched in title and
abstract, publication dates 2023-01-01 .. 2026-10-19 (the corpus cut-off). Raw responses are stored in stage11/raw/.
No API key; no e-mail parameter. Output: stage11/openalex_hits.json."""
import json, os, time, urllib.parse, urllib.request
H = os.path.dirname(os.path.abspath(__file__)); RAW = os.path.join(H, 'raw')
FM = '("foundation model" OR "large language model" OR LLM OR "vision-language model" OR "vision language model" OR VLM OR "large multimodal model" OR "multimodal large language model" OR "vision-language-action" OR VLA)'
SOC = {'O01 social navigation': '"social navigation"', 'O02 socially aware navigation': '"socially aware navigation" OR "socially-aware navigation"',
       'O03 socially compliant navigation': '"socially compliant navigation" OR "socially-compliant navigation"',
       'O04 human-aware navigation': '"human-aware navigation" OR "human aware navigation" OR "human-aware robot navigation"',
       'O05 crowd navigation': '"crowd navigation" OR "crowd-aware navigation"', 'O06 norm-aware navigation': '"norm-aware navigation" OR "social norm" OR "social norms"',
       'O07 social robot navigation': '"social robot navigation" OR "socially intelligent navigation"',
       'O08 pedestrian-aware / group / F-formation': '"pedestrian-aware" OR "group navigation" OR "F-formation" OR "social group"',
       'O09 legibility / politeness': 'legibility OR legible OR politeness OR polite',
       'O10 social reasoning / instruction / context': '"social reasoning" OR "social instruction" OR "context-aware navigation" OR "human interaction"'}
ROBOT = '(robot OR robots OR robotic OR "mobile robot" OR navigation)'
hits = {}; log = []
for fam, s in SOC.items():
    q = f'({s}) AND {FM}' + (f' AND {ROBOT}' if fam[:3] in ('O06', 'O08', 'O09', 'O10') else '')
    if fam[:3] in ('O06', 'O09', 'O10'): q += ' AND navigation'
    cursor, n_fetched, total = '*', 0, None
    while cursor and n_fetched < 600:
        u = 'https://api.openalex.org/works?' + urllib.parse.urlencode({'filter': f'title_and_abstract.search:{q},from_publication_date:2023-01-01,to_publication_date:2026-10-19',
                 'per-page': 200, 'cursor': cursor, 'select': 'id,doi,title,publication_date,type,primary_location,authorships,ids'})
        d = json.load(urllib.request.urlopen(u, timeout=60)); total = d['meta']['count']
        open(os.path.join(RAW, f"openalex_{fam[:3]}_{n_fetched}.json"), 'w').write(json.dumps(d))
        for w in d['results']:
            r = hits.setdefault(w['id'], {'id': w['id'], 'doi': w.get('doi'), 'title': w.get('title') or '', 'date': w.get('publication_date'), 'type': w.get('type'),
                 'venue': ((w.get('primary_location') or {}).get('source') or {}).get('display_name'), 'first_author': (w['authorships'][0]['author']['display_name'] if w.get('authorships') else ''),
                 'families': []})
            r['families'].append(fam[:3])
        n_fetched += len(d['results']); cursor = d['meta'].get('next_cursor') if d['results'] else None; time.sleep(1)
    log.append({'family': fam, 'query': q, 'raw_results': total, 'fetched': n_fetched}); print(fam, total, n_fetched)
json.dump({'run': '2026-10-26', 'source': 'OpenAlex API', 'date_window': '2023-01-01..2026-10-19', 'families': log, 'hits': list(hits.values())},
          open(os.path.join(H, 'openalex_hits.json'), 'w'), indent=1)
print('unique', len(hits))

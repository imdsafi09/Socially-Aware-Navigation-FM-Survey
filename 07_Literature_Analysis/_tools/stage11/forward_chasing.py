"""Stage 11 forward citation chasing (2026-10-26) on OpenAlex: for every direct paper of the corpus, locate its OpenAlex
record (DOI, else exact-title search) and retrieve all works that cite it, published up to the cut-off (2026-10-19).
Raw responses in stage11/raw/; output stage11/forward_hits.json (one record per unique citing work)."""
import csv, json, os, re, time, urllib.parse, urllib.request
H = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(H, '..', '..', '..'))
D = list(csv.DictReader(open(os.path.join(ROOT, '07_Literature_Analysis', 'direct_vlm_social_navigation_matrix.csv'))))
M = {m['id']: m for m in csv.DictReader(open(os.path.join(ROOT, '07_Literature_Analysis', 'master_literature_matrix.csv')))}
def get(u):
    for k in range(3):
        try: return json.load(urllib.request.urlopen(u, timeout=60))
        except Exception as e: time.sleep(5 * (k + 1)); err = e
    raise err
def norm(t): return re.sub(r'[^a-z0-9]', '', (t or '').lower())
seeds = []; hits = {}
for d in D:
    m = M[d['id']]; doi = (m.get('doi') or '').lower().replace('https://doi.org/', ''); rec = None
    if doi:
        try: rec = get('https://api.openalex.org/works/doi:' + urllib.parse.quote(doi) + '?select=id,title,cited_by_count')
        except Exception: rec = None
    if not rec:
        try: r = get('https://api.openalex.org/works?' + urllib.parse.urlencode({'filter': 'title.search:' + re.sub(r'[^A-Za-z0-9 -]', ' ', m['title'])[:200], 'select': 'id,title,cited_by_count', 'per-page': 5}))
        except Exception: r = {'results': []}
        cand = [w for w in r['results'] if norm(w['title'])[:40] == norm(m['title'])[:40]]
        rec = max(cand, key=lambda w: w['cited_by_count']) if cand else None
    if not rec: seeds.append({'paper': d['id'], 'openalex': None, 'cited_by_count': None, 'retrieved': 0}); print('not found', d['id']); continue
    wid = rec['id'].rsplit('/', 1)[1]; cursor = '*'; n = 0
    while cursor:
        cf = os.path.join(H, 'raw', f'cites_{d["id"]}_{n}.json')
        r = json.load(open(cf)) if os.path.exists(cf) else get('https://api.openalex.org/works?' + urllib.parse.urlencode({'filter': f'cites:{wid},to_publication_date:2026-10-19', 'per-page': 200, 'cursor': cursor,
                 'select': 'id,doi,title,publication_date,type,primary_location,authorships'}))
        open(os.path.join(H, 'raw', f'cites_{d["id"]}_{n}.json'), 'w').write(json.dumps(r))
        for w in r['results']:
            h = hits.setdefault(w['id'], {'id': w['id'], 'doi': w.get('doi'), 'title': w.get('title') or '', 'date': w.get('publication_date'), 'type': w.get('type'),
                 'venue': ((w.get('primary_location') or {}).get('source') or {}).get('display_name'), 'first_author': (w['authorships'][0]['author']['display_name'] if w.get('authorships') else ''), 'families': []})
            h['families'].append('cites:' + d['id'])
        n += len(r['results']); cursor = r['meta'].get('next_cursor') if r['results'] else None; time.sleep(0.5)
    seeds.append({'paper': d['id'], 'openalex': wid, 'cited_by_count': rec['cited_by_count'], 'retrieved': n}); print(d['id'], wid, rec['cited_by_count'], n)
json.dump({'run': '2026-10-26', 'source': 'OpenAlex forward citations', 'families': seeds, 'hits': list(hits.values())}, open(os.path.join(H, 'forward_hits.json'), 'w'), indent=1)
print('unique citing works', len(hits))

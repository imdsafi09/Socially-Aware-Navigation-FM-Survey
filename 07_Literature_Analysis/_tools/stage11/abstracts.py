"""Fetch title/abstract/venue/date for the stage-11 shortlist from OpenAlex (title search; best title match). Output shortlist_abstracts.json."""
import json, os, re, time, urllib.parse, urllib.request
H = os.path.dirname(os.path.abspath(__file__)); out = {}
cache = os.path.join(H, 'shortlist_abstracts.json')
if os.path.exists(cache): out = json.load(open(cache))
def norm(t): return re.sub(r'[^a-z0-9]', '', (t or '').lower())
for t in json.load(open(os.path.join(H, 'shortlist.json'))):
    if t in out and out[t].get('abstract'): continue
    q = re.sub(r'[^A-Za-z0-9 -]', ' ', t)[:150]
    try: r = json.load(urllib.request.urlopen('https://api.openalex.org/works?' + urllib.parse.urlencode({'filter': 'title.search:' + q, 'per-page': 5,
             'select': 'id,doi,title,publication_date,type,primary_location,abstract_inverted_index,authorships,locations'}), timeout=60))
    except Exception as e: print('ERR', t, e); continue
    best = [w for w in r['results'] if norm(w['title'])[:35] == norm(t)[:35]] or r['results'][:1]
    if not best: out[t] = {'found': False}; continue
    w = best[0]; ii = w.get('abstract_inverted_index') or {}
    words = sorted(((p, k) for k, ps in ii.items() for p in ps)); ab = ' '.join(k for _, k in words)
    out[t] = {'found': True, 'id': w['id'], 'doi': w.get('doi'), 'title': w['title'], 'date': w.get('publication_date'), 'type': w.get('type'),
              'venue': ((w.get('primary_location') or {}).get('source') or {}).get('display_name'), 'authors': [a['author']['display_name'] for a in w.get('authorships', [])][:6],
              'urls': [l.get('landing_page_url') for l in w.get('locations', []) if l.get('landing_page_url')][:4], 'abstract': ab}
    time.sleep(0.4)
json.dump(out, open(cache, 'w'), indent=1); print(len(out))

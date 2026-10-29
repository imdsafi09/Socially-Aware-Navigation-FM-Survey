"""Merge the stage-11 sources into unique candidate works (DOI, arXiv id, normalised title; versions of one work are merged:
an arXiv record and its published version, or two OpenAlex records of one paper, count once). Writes stage11/union.json."""
import json, os, re
H = os.path.dirname(os.path.abspath(__file__))
def norm(t): return re.sub(r'[^a-z0-9]', '', (t or '').lower().replace('*', ''))[:55]
SRC = [('IEEE Xplore', 'ieee_hits_dedup.json'), ('Google Scholar', 'gs_hits_dedup.json'), ('OpenAlex search', 'openalex_hits_dedup.json'), ('OpenAlex forward citations', 'forward_hits_dedup.json')]
U = {}; events = 0
for src, f in SRC:
    for h in json.load(open(os.path.join(H, f)))['hits']:
        k = norm(h['title']); events += 1
        u = U.setdefault(k, {'title': h['title'], 'sources': [], 'records': 0, 'status': h['status'], 'match': h['match'], 'doi': h.get('doi'), 'date': h.get('date'), 'venue': h.get('venue'), 'type': h.get('type'), 'first_author': h.get('first_author')})
        if src not in u['sources']: u['sources'].append(src)
        u['records'] += 1
        for fld in ('doi', 'date', 'venue', 'type', 'first_author'):
            if not u.get(fld) and h.get(fld): u[fld] = h[fld]
        if u['status'] == 'new' and h['status'] != 'new': u['status'], u['match'] = h['status'], h['match']
json.dump({'retrieval_events': events, 'unique': list(U.values())}, open(os.path.join(H, 'union.json'), 'w'), indent=1)
from collections import Counter
print('events', events, 'unique', len(U), Counter(u['status'] for u in U.values()))

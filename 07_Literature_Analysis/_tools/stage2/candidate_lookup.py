"""Stage 2: Crossref lookup (title + first author) for Critical/High missing-literature candidates. Cache: cache_candidates.json."""
import json, os, re, sys, time, importlib.util
T = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('h', os.path.join(T, 'harvest_meta.py')); h = importlib.util.module_from_spec(spec)
src = open(os.path.join(T, "harvest_meta.py")).read(); src = src[:src.index("def arxiv(")]; exec(compile(src, "h", "exec"), h.__dict__)
Q = json.load(open(os.path.join(T, 'candidate_queries.json')))
C = json.load(open(os.path.join(T, 'cache_candidates.json'))) if os.path.exists(os.path.join(T, 'cache_candidates.json')) else {}
for k, (title, author) in Q.items():
    if k in C and 'error' not in str(C[k])[:20]: continue
    C[k] = h.crossref(title, author); time.sleep(1.5)
    json.dump(C, open(os.path.join(T, 'cache_candidates.json'), 'w'), indent=1)
for k in Q:
    b = C[k][0] if isinstance(C[k], list) and C[k] else {}
    print(k, '|', b.get('sim'), b.get('DOI'), '|', (b.get('container') or '')[:60], '|', b.get('volume'), b.get('issue'), b.get('page'), b.get('published'), '|', (b.get('title') or '')[:60])

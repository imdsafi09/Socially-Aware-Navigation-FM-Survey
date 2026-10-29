"""Turn the browser-captured result lists (ieee_*.txt, acm_*.txt, gs_*.txt) into stage11/<source>_hits.json for dedup.py."""
import glob, json, os, re, sys
H = os.path.dirname(os.path.abspath(__file__))
for src in ('ieee', 'acm', 'gs'):
    files = sorted(glob.glob(os.path.join(H, f'{src}_*.txt')))
    if not files: continue
    hits = {}; fams = []
    for f in files:
        L = open(f).read().splitlines(); q = L[0][7:]; meta = L[1]; raw = int(re.search(r'RAW RESULTS: (\d+)', meta).group(1))
        fam = os.path.basename(f)[:-4]; fams.append({'family': fam, 'query': q, 'meta': meta, 'raw_results': raw, 'listed': len(L) - 2})
        for ln in L[2:]:
            p = [x.strip() for x in ln.split(' | ')]
            h = hits.setdefault(p[0].lower(), {'title': p[0], 'url': p[1] if len(p) > 1 else '', 'venue': p[2] if len(p) > 2 else '', 'families': []}); h['families'].append(fam)
    json.dump({'run': '2026-10-26', 'source': src, 'families': fams, 'hits': list(hits.values())}, open(os.path.join(H, f'{src}_hits.json'), 'w'), indent=1)
    print(src, len(hits))

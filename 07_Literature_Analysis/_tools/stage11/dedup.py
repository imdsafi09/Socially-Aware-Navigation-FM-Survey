"""Deduplicate stage-11 hits (any source file given on the command line) against the project: the 95-work master matrix
(by DOI, arXiv id, normalised title), the 284-candidate Stage-2 screening record and the Stage-7 freshness hits.
Prints and writes stage11/<source>_dedup.json with status: corpus / screened_stage2 / screened_stage7 / new."""
import csv, json, os, re, sys
H = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(H, '..', '..', '..'))
def norm(t): return re.sub(r'[^a-z0-9]', '', (t or '').lower())[:60]
M = list(csv.DictReader(open(os.path.join(ROOT, '07_Literature_Analysis', 'master_literature_matrix.csv'))))
SR = list(csv.DictReader(open(os.path.join(ROOT, '07_Literature_Analysis', '_tools', 'stage2', 'screening_record.csv'))))
F7 = json.load(open(os.path.join(ROOT, '07_Literature_Analysis', '_tools', 'stage7', 'freshness_hits.json')))
corpus_t = {norm(m['title']): m['id'] for m in M}; corpus_d = {m['doi'].lower().replace('https://doi.org/', ''): m['id'] for m in M if m.get('doi')}
corpus_a = {re.sub(r'v\d+$', '', m.get('ext_arxiv') or ''): m['id'] for m in M if m.get('ext_arxiv')}
for m in M:
    for v in (m.get('related_versions') or '').split(';'):
        if norm(v): corpus_t.setdefault(norm(v), m['id'])
s2_t = {norm(r['title'].split(':')[0] if r['title'].endswith(')') and '...' in r['title'] else r['title']): r for r in SR}; s2_k = {r['key']: r for r in SR}
f7_t = {norm(r['title']): r for r in F7}; f7_d = {str(r['id']).lower(): r for r in F7}
def classify(h):
    doi = (h.get('doi') or '').lower().replace('https://doi.org/', ''); t = norm(h['title'])
    arx = re.search(r'10\.48550/arxiv\.(\d{4}\.\d{4,5})', doi); arx = arx.group(1) if arx else h.get('arxiv')
    if doi in corpus_d: return 'corpus', corpus_d[doi]
    if arx and arx in corpus_a: return 'corpus', corpus_a[arx]
    if t in corpus_t: return 'corpus', corpus_t[t]
    if arx and arx in s2_k: return 'screened_stage2', s2_k[arx]['decision']
    if t in s2_t: return 'screened_stage2', s2_t[t]['decision']
    if doi in f7_d or t in f7_t: return 'screened_stage7', 'freshness'
    return 'new', ''
if __name__ == '__main__':
    for f in sys.argv[1:]:
        d = json.load(open(f)); hits = d['hits']
        for h in hits: h['status'], h['match'] = classify(h)
        out = f.replace('.json', '_dedup.json'); json.dump(d, open(out, 'w'), indent=1)
        from collections import Counter; print(f, len(hits), Counter(h['status'] for h in hits))

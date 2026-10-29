"""Discovery pass: 7-word shingles that occur in the reference lists of >= K of the seven reference surveys."""
import re, sys
from collections import defaultdict
from survey_citation_counts import texts
K = int(sys.argv[1]) if len(sys.argv) > 1 else 4
def refs(t):
    i = max(t.rfind(' references '), t.rfind(' bibliography '))
    return t[i:] if i > len(t) * 0.5 else t[int(len(t) * 0.6):]
sh = defaultdict(set)
for k, t in texts.items():
    w = refs(t).split()
    for i in range(len(w) - 6):
        g = ' '.join(w[i:i + 7])
        if re.search(r'\d', g) or any(x in g for x in ('proceedings', 'conference', 'international', 'ieee', 'robotics and automation', 'transactions', 'journal', 'vol ', 'pp ')):
            continue
        sh[g].add(k)
common = sorted((g for g, s in sh.items() if len(s) >= K), key=lambda g: -len(sh[g]))
seen = []
for g in common:
    if any(len(set(g.split()) & set(s.split())) >= 5 for s in seen):
        continue
    seen.append(g); print(len(sh[g]), g)

"""Count how many of the seven reference surveys cite each candidate pre-FM work (title-fragment match)."""
import os, re, json, csv, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
TXT = os.path.join(ROOT, '07_Literature_Analysis', '_tools', 'extracted_text')
SURVEYS = {
 'Kruse2013': '00_Existing_Surveys__1-s2.0-S0921889013001048-main.txt',
 'Charalampous2017': '00_Existing_Surveys__1-s2.0-S0921889016302287-main.txt',
 'Moller2021': '00_Existing_Surveys__1-s2.0-S0921889021001226-main.txt',
 'Mavrogiannis2023': '00_Existing_Surveys__3583741.txt',
 'Singamaneni2024': '00_Existing_Surveys__2807-A-survey-on-socially-aware-robot-navigation_-taxonomy-and-future-challenges.txt',
 'Alyassi2025': '00_Existing_Surveys__frobt-12-1658643.txt',
 'Kabir2026': '00_Existing_Surveys__s10489-025-06982-5.txt',
}
def norm(s):
    s = s.replace('‐', '-').replace('‑', '-').replace('–', '-').replace('—', '-').replace('’', "'").replace('ﬁ', 'fi').replace('ﬂ', 'fl')
    s = re.sub(r'-\s*\n\s*', '', s)          # de-hyphenate line breaks
    s = s.lower(); s = re.sub(r'[^a-z0-9]+', ' ', s)
    return re.sub(r'\s+', ' ', s)
texts = {k: norm(open(os.path.join(TXT, v), errors='ignore').read()) for k, v in SURVEYS.items()}
def count(fragment):
    f = norm(fragment).strip()
    return [k for k, t in texts.items() if f in t]
if __name__ == '__main__':
    cands = list(csv.DictReader(open(sys.argv[1])))
    out = []
    for c in cands:
        hits = count(c['title_fragment'])
        out.append({**c, 'n_surveys': len(hits), 'surveys': ';'.join(hits)})
    w = csv.DictWriter(open(sys.argv[2], 'w', newline=''), fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
    for o in sorted(out, key=lambda o: (o['paradigm'], -o['n_surveys'])):
        print(f"{o['paradigm'][:10]:10} {o['n_surveys']} {o['key'][:28]:28} {o['surveys']}")

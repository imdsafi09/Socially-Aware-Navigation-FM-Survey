"""Write README.md for the public repository from the structured records (no hand-typed counts or links).
Reads: 07_Literature_Analysis/master_literature_matrix.csv, 07_Literature_Analysis/prefm_comparison_set.csv,
16_Supplementary/S2_publication_status.csv, 13_References/citation_keys.json, 10_PreWriting/quantitative_findings.json.
Only links (DOI, publisher page, arXiv abstract page) are listed; no article PDF is redistributed."""
import csv, json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def rd(p): return list(csv.DictReader(open(os.path.join(ROOT, p), encoding='utf-8')))
M = rd('07_Literature_Analysis/master_literature_matrix.csv')
PCS = rd('07_Literature_Analysis/prefm_comparison_set.csv')
S2 = {r['Cite key']: r for r in rd('16_Supplementary/S2_publication_status.csv')}
KEY = {v: k for k, v in json.load(open(os.path.join(ROOT, '13_References', 'citation_keys.json'))).items()}
QF = {q['id']: q for q in json.load(open(os.path.join(ROOT, '10_PreWriting', 'quantitative_findings.json')))}
def n(k): return QF[k]['numerator']

BIB = open(os.path.join(ROOT, '13_References', 'survey_references.bib'), encoding='utf-8').read()
DOI = {k: d for k, d in re.findall(r'@\w+\{([^,]+),(?:(?!\n@).)*?\bdoi\s*=\s*\{([^}]+)\}', BIB, re.S)}
def ok(v): return bool(v) and v.strip() not in ('', 'NA', 'none', 'None', '-') and not v.startswith('Not found')
def cell(s): return re.sub(r'\s+', ' ', str(s)).replace('|', '/').strip()
def arxiv_abs(a):
    a = re.sub(r'v\d+$', '', a.strip())
    return f'https://arxiv.org/abs/{a}'
def links(url, arx):
    out = []
    if ok(url):
        lab = 'arXiv' if 'arxiv.org/abs/' in url else ('DOI' if 'doi.org/' in url else 'Publisher page')
        out.append(f'[{lab}]({url})')
    if re.fullmatch(r'(\d{4}\.\d{4,5}|[a-z\-]+(\.[A-Z]{2})?/\d{7})(v\d+)?', arx.strip()) and not (ok(url) and 'arxiv.org/abs/' in url):
        out.append(f'[arXiv]({arxiv_abs(arx)})')
    return ' · '.join(out) or '-'
def venue(r):
    v = r['venue']
    if not ok(v): return '-'
    return 'arXiv preprint' if re.match(r'\s*arXiv', v) else cell(v)
def status(i):
    s = S2.get(KEY.get(i, ''), {}).get('Status class', '')
    return {'A': 'peer-reviewed', 'B': 'accepted, not yet indexed', 'C': 'preprint', 'D': 'acceptance verified'}.get(s[:1], '-')

SECTIONS = [('Direct foundation-model social navigation', ('S4', 'S5'), True),
            ('Adjacent foundation-model navigation', ('S3',), False),
            ('Datasets, simulators and benchmarks', ('S6',), False),
            ('Classical and learning-based social navigation', ('S1', 'S2'), False),
            ('Existing surveys, reviews and guidelines', ('S0',), False)]

def table(rows, with_status):
    rows = sorted(rows, key=lambda r: (-int(r['year']), r['title'].lower()))
    hd = '| Year | Title | Venue | ' + ('Status | ' if with_status else '') + 'Links |'
    sp = '|---|---|---|' + ('---|' if with_status else '') + '---|'
    body = [f"| {r['year']} | {cell(r['title'])} | {venue(r)} | " + (f"{status(r['id'])} | " if with_status else '') + f"{links(r['url'], r['ext_arxiv'])} |" for r in rows]
    return [hd, sp] + body

L = ['# From Proxemics to Foundation Models: A Survey of Socially Aware Robot Navigation', '',
     'Coding records, screening records and scripts accompanying the survey *From Proxemics to Foundation Models: A Survey of Socially Aware Robot Navigation* (M. Imad and S. Y. Shin). The citation will be added on publication.', '',
     f"The corpus contains {n('QF01')} works, including {n('QF02')} direct foundation-model (FM) social-navigation papers, with a literature cut-off of 19 October 2026 and a final coverage search on 26 October 2026 restricted to works dated up to the cut-off. A representative pre-FM comparison set of {n('QF50_prefm_n')} works is coded with the same scheme. Every count, table and data-driven figure of the survey and its supplementary material is generated from the records in this repository by the scripts below.", '',
     '## Copyright of the reviewed articles', '',
     'The reviewed articles are **not** included in this repository, because most of them are under publisher copyright. Each work is listed below with a link to its DOI, publisher page or arXiv abstract page; readers obtain the articles from these sources. The version used for coding is recorded in [`16_Supplementary/S2_publication_status.csv`](16_Supplementary/S2_publication_status.csv). The paper notes in `08_Paper_Notes/` are the authors\' structured summaries with page references, not copies of the articles.', '',
     '## Repository contents', '',
     '| Path | Content |', '|---|---|',
     '| [`08_Paper_Notes/`](08_Paper_Notes) | One structured note per corpus work (YAML front matter with the final coding, followed by a summary) |',
     '| [`07_Literature_Analysis/`](07_Literature_Analysis) | Coding matrices generated from the notes (direct papers, capabilities, evidence, deployment, metrics, reproducibility, datasets), the pre-FM comparison set, and the search and screening scripts and records (`_tools/stage2`: expansion search and screening; `_tools/stage11`: final coverage search; `_tools/stage9`: pre-FM comparison set) |',
     '| [`10_PreWriting/`](10_PreWriting) | `quantitative_findings.json`: every count reported in the survey, with numerator, denominator, population and source (`build_findings.py`) |',
     '| [`11_Tables/`](11_Tables) | Generated tables (CSV and Markdown) |',
     '| [`12_Figures/`](12_Figures) | Figure scripts (pycairo, deterministic vector output) and the generated figures; no generative image model is used |',
     '| [`13_References/`](13_References) | Verified bibliographic metadata and the generated reference database |',
     '| [`16_Supplementary/`](16_Supplementary) | Supplementary material: Tables S1–S13 (CSV and Markdown), Figs. S1–S4, the supplement PDF and its LaTeX source |',
     '| [`15_Manuscript/references.bib`](15_Manuscript/references.bib) | Bibliography used by the supplement build |', '',
     '## Rebuilding', '',
     'Requirements: Python 3 (tested with 3.12) with `pycairo` and `PyYAML` (`pip install -r requirements.txt`); XeLaTeX with the TeX Gyre, DejaVu and Latin Modern fonts for the supplement PDF (optional).', '',
     '```bash', './build.sh', '```', '',
     'The build regenerates the pre-FM comparison set, the reference database, the quantitative findings, the tables, the figures, the supplementary tables and (if XeLaTeX is available) the supplement PDF, and finally this README. The earlier stages that produced the notes from the source articles (`07_Literature_Analysis/_tools/build_matrices.py` and `stage3/`) and the retrieval scripts (arXiv, OpenAlex, forward citation chasing) are included to document the procedure; they need the source articles or network access and are not part of `build.sh`.', '',
     '## Licence', '',
     'Code (`*.py`, `*.sh`): MIT licence ([`LICENSE`](LICENSE)). Data, notes, tables and figures: Creative Commons Attribution 4.0 International ([`LICENSE-DATA.md`](LICENSE-DATA.md)). Bibliographic metadata of the reviewed works and short quotations remain subject to the rights of their owners.', '',
     '## Reviewed works', '',
     'Links only; no article PDF is redistributed. Sorted by year (newest first).', '']
for title, cats, st in SECTIONS:
    rows = [r for r in M if r['analytical_category'] in cats]
    L += [f'### {title} ({len(rows)})', ''] + table(rows, st) + ['']
pre = sorted(PCS, key=lambda r: (r['paradigm'], int(r['year'])))
L += [f'### Representative pre-FM comparison set ({len(pre)})', '',
      f"Representative rather than exhaustive: exemplars cited by at least three of seven reference surveys per paradigm, plus the corpus works (survey Section 2.3). {sum(1 for r in PCS if r['in_frozen_corpus'] == 'Yes')} of these works are also listed above.", '',
      '| Paradigm | Year | Title | Venue | Link |', '|---|---|---|---|---|']
def prefm_url(r):
    d = DOI.get(r['bib_key']) or DOI.get(r['key'])
    return f'https://doi.org/{d}' if d else r['source_url']
def paradigm(p): return cell(re.sub(r'^P\d+\s*', '', p))
L += [f"| {paradigm(r['paradigm'])} | {r['year']} | {cell(r['title'])} | {cell(r['venue']) if ok(r['venue']) else '-'} | {links(prefm_url(r), '')} |" for r in pre]
open(os.path.join(ROOT, 'README.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print(f'README.md written ({len(M)} corpus works, {len(PCS)} pre-FM works)')

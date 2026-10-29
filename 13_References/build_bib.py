"""Stage 4: build survey_references.bib and REFERENCE_STATUS.md from the frozen notes (corpus works) and the
Stage-2 missing-literature decisions (background-only anchors). No field is invented: only note/Crossref/PMLR/CVF/
J-STAGE/arXiv-verified values are written; unresolved status goes into `note` fields and REFERENCE_STATUS.md."""
import os, re, glob, json, unicodedata, collections, yaml
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
T2 = os.path.join(ROOT, '07_Literature_Analysis', '_tools')
PUB = {'10.1109': 'IEEE', '10.1145': 'ACM', '10.1016': 'Elsevier', '10.1177': 'SAGE', '10.1007': 'Springer', '10.3389': 'Frontiers Media',
       '10.3390': 'MDPI', '10.1609': 'AAAI Press', '10.15607': 'Robotics: Science and Systems Foundation', '10.52202': 'Curran Associates',
       '10.23919': 'IEEE', '10.1103': 'American Physical Society', '10.11517': 'The Japanese Society for Artificial Intelligence', '10.1111': 'Wiley',
       '10.1371': 'Public Library of Science'}
# Journal articles cited with volume/issue use the issue (print) year, not the online-first year (Crossref published-print; checked 2026-10-20)
ISSUE_YEAR = {'RiosMartinez': 2015}
def ascii(s): return unicodedata.normalize('NFKD', str(s)).encode('ascii', 'ignore').decode()
def tex(s):
    s = str(s)
    for a, b in [('\\', ''), ('&', r'\&'), ('%', r'\%'), ('#', r'\#'), ('_', r'\_')]: s = s.replace(a, b)
    return s
COMPOUND = {'Edison Jair Bejarano Sepulveda': ('BejaranoSepulveda', 'Bejarano Sepulveda, Edison Jair'), 'J. van den Berg': ('vandenBerg', 'van den Berg, J.')}
def last(name):
    if name in COMPOUND: return COMPOUND[name][0]
    parts = ascii(name).replace('.', ' ').split()
    if len(parts) >= 2 and parts[-2].lower() in ('de', 'van', 'von', 'der'): return parts[-2].capitalize() + parts[-1]
    return re.sub(r'[^A-Za-z]', '', parts[-1]) if parts else 'Anon'
def bibname(n):
    if n in COMPOUND: return COMPOUND[n][1]
    p = str(n).split()
    if len(p) >= 2 and p[-2].lower() in ('de', 'van', 'von', 'der'): return f"{' '.join(p[-2:])}, {' '.join(p[:-2])}"
    return f"{p[-1]}, {' '.join(p[:-1])}" if len(p) > 1 else n
def authors_field(names):
    """Names up to the first 'et al.' item (notes record e.g. 'et al. (45 authors, alphabetical)'), then BibTeX 'and others'."""
    out = []
    for a in names:
        if re.match(r'\s*et al', str(a)): return ' and '.join(out) + ' and others'
        out.append(tex(bibname(a)))
    return ' and '.join(out)
def pages_field(p):
    p = str(p)
    m = re.match(r'^\s*(\d+)\s*[-–]\s*(\d+)', p)
    if m: return 'pages', f'{m.group(1)}--{m.group(2)}'
    m = re.search(r'Article\s+(\d+)', p)
    if m: return 'eid', m.group(1)
    return None, None
def kind(y):
    sc = str((y.get('external_verification') or {}).get('status_class', ''))[:1]
    v = str(y['venue'])
    if sc in ('C', 'B'): return 'misc'
    if sc == 'D': return 'inproceedings'
    if re.search(r'Conference|Proceedings|Symposium|Workshop|ICRA|IROS|CVPR|NeurIPS|ICASSP|RSS|Robotics: Science|Companion', v, re.I) and not re.search(r'Letters|Transactions|Journal|Review E|Computing Surveys', v):
        return 'inproceedings'
    return 'article'
def arxiv_id(y):
    ev = y.get('external_verification') or {}
    a = str(ev.get('arxiv', ev.get('arxiv_id', '')))
    m = re.match(r'(cond-mat/\d+|\d{4}\.\d{4,5})(v\d+)?', a)
    return m.group(1) if m else None
def main():
    notes = []
    for f in sorted(glob.glob(os.path.join(ROOT, '08_Paper_Notes', '*.md'))):
        notes.append(yaml.safe_load(open(f).read().split('---', 2)[1]))
    keys = {}; out = []; status = []; seen_doi = collections.Counter(); seen_title = collections.Counter()
    for y in notes:
        tag = re.sub(r'[^A-Za-z0-9]', '', y['id'].split('_', 2)[2])
        key = f"{last(y['authors'][0])}{y['year']}{tag}"
        if key in keys: key += 'b'
        keys[key] = y['id']
        ev = y.get('external_verification') or {}; sc = str(ev.get('status_class', ''))
        k = kind(y); F = {'author': authors_field(y['authors']), 'title': '{' + tex(y['title']) + '}', 'year': str(y['year'])}
        ax = arxiv_id(y); doi = str(y['doi']) if str(y['doi']).startswith('10.') else None
        if k == 'article':
            F['journal'] = tex(y['venue'])
            if str(y.get('volume')) not in ('NA', 'Not reported', 'None'): F['volume'] = str(y['volume'])
            if str(y.get('issue')) not in ('NA', 'Not reported', 'None'): F['number'] = str(y['issue'])
        elif k == 'inproceedings':
            F['booktitle'] = tex(re.sub(r'\s*\(per .*?\)', '', str(y['venue'])))
        if k != 'misc':
            pk, pv = pages_field(y.get('pages'))
            if pk: F[pk] = pv
            if doi: F['doi'] = doi; F['publisher'] = PUB.get(doi.split('/')[0], '') or None
            elif 'proceedings.mlr.press' in str(y['url']): F['publisher'] = 'PMLR'
            elif 'thecvf.com' in str(y['url']): F['publisher'] = 'IEEE/CVF'
        F['url'] = str(y['url'])
        if ax: F['eprint'] = ax; F['archiveprefix'] = 'arXiv'
        notes_txt = []
        if sc.startswith('B'):
            notes_txt.append('Accepted according to author or citing-paper statement; proceedings not yet indexed as of 2026-10-19 (' + '; '.join(ev.get('sources', []))[:160] + ')')
        if sc.startswith('C'): notes_txt.append('arXiv preprint; no verified peer-reviewed version as of 2026-10-19')
        if sc.startswith('D'): notes_txt.append('Conference acceptance verified; peer-review status not independently established')
        if 'different title' in str(ev.get('version_relationship', '')) or 'retitled' in str(y.get('peer_review_basis', '')):
            notes_txt.append('Published under a different title than the arXiv version')
        if notes_txt: F['note'] = '. '.join(notes_txt)
        F = {a: b for a, b in F.items() if b}
        out.append(f'@{k}{{{key},\n' + ',\n'.join(f'  {a} = {{{b}}}' for a, b in F.items()) + '\n}\n')
        cls = {'A': 'verified published', 'B': 'accepted/not yet officially indexed', 'C': 'preprint', 'D': 'publication status uncertain (acceptance verified, peer review not established)'}.get(sc[:1], 'unknown')
        miss = [f for f in ['doi', 'pages', 'volume'] if f not in F and k == 'article'] + ([f for f in ['pages'] if f not in F and f not in ('eid',)] if k == 'inproceedings' and 'eid' not in F else [])
        if k != 'misc' and not doi and 'publisher' in F and F['publisher'] in ('PMLR', 'IEEE/CVF'): miss = [m for m in miss if m != 'doi'] + ['doi (none exists: PMLR/CVF open access)']
        status.append((key, y['id'], y['category'], cls, k, ', '.join(miss) or '-'))
        if doi: seen_doi[doi.lower()] += 1
        seen_title[re.sub(r'[^a-z0-9]', '', y['title'].lower())[:60]] += 1
    # background-only anchors (Critical/High BACKGROUND ONLY decisions)
    ML = json.load(open(os.path.join(T2, 'missing_lit_rows.json'))); CC = json.load(open(os.path.join(T2, 'stage2', 'cache_candidates.json')))
    bg = []
    BGV = {k: v for k, v in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'background_verified.json'))).items() if not k.startswith('_')}
    for r in ML:
        if r['priority'] not in ('Critical', 'High') or not r['decision'].startswith('BACKGROUND'): continue
        c = CC.get(r['key']); b = c[0] if isinstance(c, list) and c and c[0].get('sim', 0) >= 0.95 else None
        key = f"{last(r['authors'].split(',')[0])}{r['year']}{re.sub(r'[^A-Za-z0-9]', '', r['key'])}"
        if key in keys: key += 'bg'
        keys[key] = 'BACKGROUND:' + r['key']
        if b:
            typ = 'article' if b['type'] == 'journal-article' else ('inproceedings' if b['type'] == 'proceedings-article' else 'incollection')
            F = {'author': ' and '.join(tex(bibname(a)) for a in b['authors']) + (' and others' if len(b['authors']) >= 12 else ''), 'title': '{' + tex(b['title']) + '}',
                 'year': str(ISSUE_YEAR.get(r['key'], (b.get('published') or [[r['year']]])[0][0]))}
            F['journal' if typ == 'article' else 'booktitle'] = tex(b['container'])
            if b.get('volume') and typ == 'article': F['volume'] = b['volume']
            if b.get('issue') and typ == 'article': F['number'] = b['issue']
            if b.get('page'): F['pages'] = b['page'].replace('-', '--')
            elif b.get('article-number'): F['eid'] = b['article-number']
            F['doi'] = b['DOI']; F['publisher'] = b.get('publisher') or ''
            F = {a: v for a, v in F.items() if v}
            st = 'verified published (Crossref)'
        elif key in BGV:
            typ = BGV[key]['type']; F = dict(BGV[key]['fields'])
            st = 'verified background (publisher/proceedings/catalogue record; see background_verified.json)'
            b = True
        else:
            typ = 'misc'
            F = {'author': tex(re.sub(r'\s*,?\s*et al\.?.*$', ' and others', r['authors']).replace(', ', ' and ')), 'title': '{' + tex(r['title']) + '}', 'year': str(r['year']),
                 'howpublished': tex(r['venue_as_cited']), 'note': 'Metadata as cited by corpus papers; not externally verified (background reference)'}
            st = 'background, metadata as cited (verify before final submission)'
        bg.append(f'@{typ}{{{key},\n' + ',\n'.join(f'  {a} = {{{v}}}' for a, v in F.items()) + '\n}\n')
        status.append((key, 'BACKGROUND:' + r['key'], 'background', st, typ, '-' if b else 'doi/pages/venue unverified'))
    for key, v in BGV.items():   # Stage-7 extra background entries not in the Stage-2 decision list
        if not v.get('extra') or key in keys: continue
        keys[key] = 'BACKGROUND:stage7'
        bg.append(f"@{v['type']}{{{key},\n" + ',\n'.join(f'  {a} = {{{b}}}' for a, b in v['fields'].items()) + '\n}\n')
        status.append((key, 'BACKGROUND:stage7-freshness', 'background', 'verified background (publisher/proceedings/catalogue record; see background_verified.json)', v['type'], '-'))
    PV = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'prefm_verified.json')))
    for key, v in PV.items():   # Stage-9 pre-FM comparison works (Crossref-verified; analysed in the comparison set, not coded corpus works)
        if key.startswith('_') or v.get('status') != 'VERIFIED' or key in keys: continue
        keys[key] = 'PREFM:stage9'
        bg.append(f"@{v['type']}{{{key},\n" + ',\n'.join(f'  {a} = {{{b}}}' for a, b in v['fields'].items()) + '\n}\n')
        status.append((key, 'PREFM:stage9-comparison-set', 'background', 'verified pre-FM comparison work (Crossref; see prefm_verified.json)', v['type'], '-'))
    hdr = ('% survey_references.bib - generated by 13_References/build_bib.py from the frozen corpus (2026-10-19).\n'
           '% Corpus works: metadata from 08_Paper_Notes (externally verified in Stage 2). Background anchors: Crossref when verified, otherwise as cited.\n'
           '% Do not edit by hand; edit notes or build_bib.py and regenerate.\n\n')
    open(os.path.join(ROOT, '13_References', 'survey_references.bib'), 'w').write(hdr + '% ===== Corpus works =====\n\n' + '\n'.join(out) + '\n% ===== Background-only references =====\n\n' + '\n'.join(bg))
    dupd = [d for d, n in seen_doi.items() if n > 1]; dupt = [t for t, n in seen_title.items() if n > 1]
    cnt = collections.Counter(s[3] for s in status)
    L = ['# Reference Status (Stage 4; background anchors verified in Stage 7)', '', 'Generated by `13_References/build_bib.py` from the frozen notes and Stage-2 decisions. Freeze date 2026-10-19.', '',
         f'**Entries:** {len(status)} ({len(out)} corpus works + {len(bg)} background-only anchors).', '',
         '| Status | Entries |', '|---|---|'] + [f'| {k} | {v} |' for k, v in sorted(cnt.items())] + ['',
         f'**Duplicate DOIs:** {dupd or "none"}. **Duplicate titles:** {dupt or "none"}. **Citation-key collisions:** none remaining ({sum(1 for k in keys if k.endswith("bg"))} background keys suffixed with `bg` to avoid clashing with corpus keys).', '',
         '**Rules applied:**',
         '- published metadata preferred over arXiv; arXiv kept as `eprint` for alternate versions;',
         '- accepted-but-not-indexed works (class B) are `@misc` with a note quoting the acceptance source;',
         '- preprints are `@misc` with an `eprint`;',
         '- JSAI 2026 is `@inproceedings` with a note on peer review;',
         '- no page numbers, DOIs or issues are invented. PMLR and CVF open-access papers have no DOI, and none is given.',
         '', '| Key | Note id / background key | Category | Status | BibTeX type | Missing or unverifiable fields |', '|---|---|---|---|---|---|']
    L += [f'| {a} | {b} | {c} | {d} | {e} | {f} |' for a, b, c, d, e, f in status]
    open(os.path.join(ROOT, '13_References', 'REFERENCE_STATUS.md'), 'w').write('\n'.join(L) + '\n')
    json.dump(keys, open(os.path.join(ROOT, '13_References', 'citation_keys.json'), 'w'), indent=1)
    print(len(out), len(bg), cnt, dupd, dupt)
if __name__ == '__main__': main()

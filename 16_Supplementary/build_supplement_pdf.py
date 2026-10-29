"""Build a single reader-facing supplementary PDF (Supplementary_Material.pdf) from the generated supplement files.
Front matter: Supplementary_Material.md (index, notation, SNEI note). Tables: S1-S13 as landscape long tables (S11-S13 are the per-paper/per-resource tables moved from the main text in the 2026-10-26 compression pass).
Requires xelatex. Run after build_supplement.py.
Also writes the self-contained LaTeX source of the supplement to latex_source/ (Supplementary_Material.tex, references.bib, the
generated .bbl and figures/), compiled here from exactly those files."""
import csv, os, re, subprocess, shutil, tempfile
H = os.path.dirname(os.path.abspath(__file__))
TABLES = [('S1_screening_record', 'Table S1, part A. Screening record of the expansion search and the final cut-off check (19 October 2026)'), ('S1b_final_search_record', 'Table S1, part B. Screening record of the final coverage search (26 October 2026)'), ('S2_publication_status', 'Table S2. Publication status of all corpus works'),
          ('S3_adjacent_foundation_models', 'Table S3. Adjacent foundation-model navigation works (not social-navigation evidence)'),
          ('S4_full_final_coding', 'Table S4. Full final coding of all non-survey corpus works'), ('S5_prefm_comparison_set', 'Table S5, part A. Pre-FM comparison set: per-work selection and coding'),
          ('S5b_prefm_by_paradigm', 'Table S5, part B. Pre-FM comparison set by paradigm'),
          ('S6_robustness', 'Table S6. Robustness of headline counts'),
          ('S7_capability_coverage', 'Table S7. Social-capability coverage'), ('S8_code_dictionary', 'Table S8. Code dictionary'),
          ('S9_interface_evidence', 'Table S9. Navigation interfaces and evidence'), ('S10_metric_families', 'Table S10. Metric families'),
          ('S11_direct_architecture', 'Table S11. Architecture of the direct papers (per paper)'), ('S12_direct_evidence', 'Table S12. Capabilities and evidence of the direct papers (per paper)'),
          ('S13_datasets_benchmarks', 'Table S13. Datasets, simulators and benchmarks (per resource)')]
FIGS = [('FigS1_fm_roles', 'Fig. S1. FM roles per direct paper (Dimension B), grouped by primary navigation interface'),
        ('FigS2_evidence_profile', 'Fig. S2. Evidence profile per direct paper (Dimension E), grouped by primary navigation interface'),
        ('FigS3_capability_heatmap', 'Fig. S3. Capability coding per direct paper (Dimension C)'),
        ('FigS4_evolution_timeline', 'Fig. S4. Dated timeline of the paradigms of social representation. Each band runs from the approximate first appearance of a paradigm to the literature cut-off; markers show representative works at their publication year. Overlapping bands indicate coexistence, not replacement or causal progression')]
def fig_tex(name, title):
    return '\n'.join([r'\clearpage', r'\section*{' + esc(title) + '}', r'\addcontentsline{toc}{section}{' + esc(title) + '}', r'\begin{center}\includegraphics[width=\linewidth,height=0.85\textheight,keepaspectratio]{figures/' + name + r'}\end{center}'])
def esc(s):
    s = re.sub(r'"([^"\n]*)"', '\u201c\\1\u201d', str(s))   # typographic double quotes, as in the manuscript
    for a, b in [('\\', r'\textbackslash{}'), ('&', r'\&'), ('%', r'\%'), ('#', r'\#'), ('_', r'\_'), ('$', r'\$'), ('{', r'\{'), ('}', r'\}'), ('~', r'\textasciitilde{}'), ('^', r'\textasciicircum{}')]:
        s = s.replace(a, b)
    s = re.sub(r'(https?://\S+)', lambda m: r'\url{' + m.group(1).replace(r'\_', '_').replace(r'\%', '%').replace(r'\#', '#').replace(r'\&', '&') + '}', s)
    return re.sub('([\u0370-\u03ff\u1f00-\u1fff\u2500-\u257f]+)', r'{\\fbfont \1}', s)   # Greek and box drawing (record titles, author names): not in Termes
def inline(s):
    s = esc(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', s); s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?!\w)', r'\\emph{\1}', s)
    return re.sub(r'`([^`]+)`', lambda m: r'\texttt{' + m.group(1).replace(r'\_', r'\_\allowbreak{}') + '}', s)   # file names may break after '_'
def md_to_tex(md):
    out, lines, i = [], md.splitlines(), 0
    while i < len(lines):
        l = lines[i]
        if l.startswith('# '): i += 1; continue
        if l.startswith('## '): out.append(r'\section*{' + inline(l[3:]) + '}'); i += 1; continue
        if l.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                if not re.match(r'^\|[-|\s:]+\|$', lines[i]): rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')])
                i += 1
            n = len(rows[0])   # column widths follow the content length; they include the 2\tabcolsep padding, so the table never exceeds the text width
            wt = [max(min(max(len(r[j]) if j < len(r) else 0 for r in rows), 80), 8) ** 0.85 for j in range(n)]; ws = [x / sum(wt) for x in wt]
            out.append(r'\begin{longtable}{' + ' '.join(f'>{{\\raggedright\\arraybackslash\\hspace{{0pt}}}}p{{\\dimexpr {w:.4f}\\linewidth-2\\tabcolsep\\relax}}' for w in ws) + r'}\toprule')
            out.append(' & '.join(r'\textbf{' + inline(c) + '}' for c in rows[0]) + r'\\\midrule')
            out += [' & '.join(inline(c) for c in r + [''] * (n - len(r))) + r'\\' for r in rows[1:]]
            out.append(r'\bottomrule\end{longtable}'); continue
        if re.match(r'^\s*- ', l):
            out.append(r'\begin{itemize}\setlength\itemsep{0pt}')
            while i < len(lines) and (re.match(r'^\s*- ', lines[i]) or (lines[i].startswith('  ') and lines[i].strip())):
                ll = lines[i]
                if re.match(r'^\s*- ', ll): out.append(r'\item ' + inline(re.sub(r'^\s*- ', '', ll)))
                else: out.append(inline(ll.strip()))
                i += 1
            out.append(r'\end{itemize}'); continue
        out.append(inline(l) if l.strip() else ''); i += 1
    return '\n'.join(out)
# Columns whose cite keys are rendered as real citations, so that every work of the pre-FM comparison set is listed in the
# supplement's own reference list (generated by BibTeX from the manuscript bibliography; numbering independent of the main text).
CITE_COLS = {'S5_prefm_comparison_set': ('Cite key',), 'S5b_prefm_by_paradigm': ('Works (cite keys)',)}
BIB = os.path.join(os.path.dirname(H), '15_Manuscript', 'references.bib')
def brk(s):
    """Escape a table cell and add break opportunities inside long unbroken tokens (cite keys, DOIs, identifiers)."""
    out = []
    for tok in re.split(r'(\s+)', str(s)):
        if len(tok) > 9 and not tok.startswith('http'):
            tok = re.sub(r'([/._:;-])', '\\1\x00', tok); tok = re.sub(r'(?<=[a-z0-9])(?=[A-Z])', '\x00', tok); tok = re.sub(r'(?<=[A-Za-z])(?=[0-9]{4})', '\x00', tok)
        out.append(tok)
    return esc(''.join(out)).replace('\x00', r'\allowbreak{}')
def table_tex(name, title):
    rows = list(csv.reader(open(os.path.join(H, name + '.csv'))))
    hdr, body = rows[0], rows[1:]
    n = len(hdr)
    lens = [max([len(hdr[j])] + [len(r[j]) for r in body if j < len(r)]) for j in range(n)]
    hw = [max([len(w) for w in re.split(r'[\s_]+', h) if w] + [len(w) for r in body if j < len(r) for w in re.split(r'[\s/-]+', r[j]) if w and not w.startswith('http')] or [4]) for j, h in enumerate(hdr)]   # longest word in the column
    wts = [min(max(l, hw[j] + 1, 7), 70) ** 0.8 for j, l in enumerate(lens)]; tot = sum(wts)
    fs = 5.0 if n > 9 else 7.0   # \tiny or \scriptsize, as chosen below
    hl = [max([len(w) for w in re.split(r'[\s_]+', h) if w] or [4]) for h in hdr]
    bl = [max([len(w) for r in body if j < len(r) for w in re.split(r'[\s/-]+', r[j]) if w and not w.startswith('http')] or [1]) for j in range(n)]
    # longest word must fit: bold header ~0.66 em per character, regular body ~0.58 em (conservative for Nimbus Roman, the manuscript's Times face); 762pt = landscape text width
    mn = [max(0.034, (max(hl[j] * 0.66, bl[j] * 0.58) * fs + 6) / 762.0) for j in range(n)]
    fr = [w / tot for w in wts]
    for _ in range(4):   # raise narrow columns to their minimum and take the space from the others
        fr = [max(f, m) for f, m in zip(fr, mn)]; ex = sum(fr) - 1
        if ex <= 1e-6: break
        free = [f - m for f, m in zip(fr, mn)]; tf = sum(free)
        if tf <= ex: break   # minimums alone exceed the width: scale proportionally below
        fr = [f - ex * fr_ / tf for f, fr_ in zip(fr, free)]
    fr = [f / sum(fr) for f in fr]
    # each column width includes its 2\tabcolsep padding, so the full table equals \linewidth (previously it overran the margin by n x 4pt)
    cols = ' '.join(f'>{{\\raggedright\\arraybackslash\\hspace{{0pt}}}}p{{\\dimexpr {f:.4f}\\linewidth-2\\tabcolsep\\relax}}' for f in fr)
    size = r'\tiny' if n > 9 else r'\scriptsize'
    t = [r'\begin{landscape}', r'\section*{' + esc(title) + '}', r'\addcontentsline{toc}{section}{' + esc(title) + '}',
         f'{len(body)} rows. Machine-readable version: \\texttt{{{esc(name)}.csv}}.\\par', r'{' + size + r'\setlength{\tabcolsep}{2pt}\renewcommand{\arraystretch}{1.05}',
         r'\begin{longtable}{' + cols + r'}\toprule', ' & '.join(r'\textbf{' + brk(h) + '}' for h in hdr) + r'\\\midrule\endhead', r'\bottomrule\endfoot']
    ck = [j for j, h in enumerate(hdr) if h in CITE_COLS.get(name, ())]
    def cell(j, c): return ', '.join(brk(k) + r'~\cite{' + k + '}' for k in re.split(r'\s*[;,]\s*', c) if k) if j in ck else brk(c)
    t += [' & '.join(cell(j, c) for j, c in enumerate((r + [''] * (n - len(r)))[:n])) + r'\\' for r in body]
    t += [r'\end{longtable}}', r'\end{landscape}']
    return '\n'.join(t)
# TeX Gyre Termes / Heros: the URW Nimbus Roman / Nimbus Sans designs used by the manuscript (txfonts), with the wider Unicode
# coverage that Table S1 needs (Vietnamese and Turkish titles, U+2010 hyphens); the URW base-35 files lack these glyphs.
FONTS = [r'\setmainfont{TeX Gyre Termes}', r'\setsansfont{TeX Gyre Heros}']
def main():
    md = open(os.path.join(H, 'Supplementary_Material.md')).read()
    title = re.search(r'^\*\*(.+?)\*\*$', md, re.M).group(1)
    # Same class and typefaces as the manuscript (elsarticle with the times option = Times/Nimbus Roman text, Helvetica/Nimbus Sans
    # sans serif, txfonts-style Times maths, CM typewriter); XeLaTeX is kept for the Unicode titles in Table S1, so the identical URW
    # designs are loaded through fontspec. elsarticle supplies the section-heading style and natbib (numbered).
    doc = [r'% Supplementary Material for "' + title + '"', r'% Generated by 16_Supplementary/build_supplement_pdf.py; do not edit by hand (regenerate instead).',
           r'% Compile with XeLaTeX (Unicode titles in Table S1): xelatex, bibtex, xelatex, xelatex. Supplementary_Material.bbl is included,',
           r'% so bibtex is optional. Fonts: TeX Gyre Termes, Heros and Termes Math, Latin Modern Mono, DejaVu Serif (all in TeX Live).',
           r'\documentclass[a4paper,10pt]{elsarticle}', r'\usepackage[a4paper,margin=1.4cm]{geometry}', r'\usepackage{amsmath}', r'\usepackage{unicode-math}',
           *FONTS, r'\newfontfamily\fbfont{DejaVu Serif}[Scale=MatchLowercase]', r'\setmonofont{Latin Modern Mono}', r'\setmathfont{TeX Gyre Termes Math}',
           r'\usepackage{longtable,booktabs,array,pdflscape,enumitem,graphicx,xcolor}', r'\definecolor{csrlink}{RGB}{33,150,209}',
           r'\usepackage[colorlinks=true,linkcolor=csrlink,citecolor=csrlink,urlcolor=csrlink,filecolor=csrlink]{hyperref}', r'\AtBeginDocument{\hypersetup{linkcolor=csrlink,citecolor=csrlink,urlcolor=csrlink,filecolor=csrlink}}', r'\usepackage{xurl}', r'\setlength{\parindent}{0pt}\setlength{\parskip}{4pt}',
           r'\begin{document}', r'{\Large\bfseries Supplementary Material\par}\vspace{4pt}{\large ' + esc(title) + r'\par}\vspace{8pt}', md_to_tex(md.split('\n', 3)[3]),
           r'\clearpage\tableofcontents\clearpage'] + [table_tex(n, t) for n, t in TABLES] + [fig_tex(n, t) for n, t in FIGS] + [r'\clearpage\renewcommand{\refname}{References cited in Table S5 (pre-FM comparison set)}\addcontentsline{toc}{section}{References cited in Table S5}',
           r'\renewcommand{\bibpreamble}{\small Numbering is independent of the main manuscript; every work of the pre-FM comparison set is listed.\par}', r'\bibliographystyle{elsarticle-num}', r'\bibliography{references}', r'\end{document}']
    J = 'Supplementary_Material'
    tmp = tempfile.mkdtemp(); open(os.path.join(tmp, J + '.tex'), 'w').write('\n'.join(doc) + '\n')
    shutil.copy(BIB, os.path.join(tmp, 'references.bib')); os.makedirs(os.path.join(tmp, 'figures'))
    for n, _ in FIGS: shutil.copy(os.path.join(H, n + '.pdf'), os.path.join(tmp, 'figures', n + '.pdf'))
    subprocess.run(['xelatex', '-interaction=nonstopmode', J + '.tex'], cwd=tmp, capture_output=True, text=True)
    subprocess.run(['bibtex', J], cwd=tmp, capture_output=True, text=True)
    for _ in range(2):
        r = subprocess.run(['xelatex', '-interaction=nonstopmode', J + '.tex'], cwd=tmp, capture_output=True, text=True)
    log = open(os.path.join(tmp, J + '.log'), errors='ignore').read()
    if r.returncode != 0 or not os.path.exists(os.path.join(tmp, J + '.pdf')): print(log[-3000:]); raise SystemExit('xelatex failed')
    shutil.copy(os.path.join(tmp, J + '.pdf'), os.path.join(H, J + '.pdf'))
    SRC = os.path.join(H, 'latex_source'); shutil.rmtree(SRC, ignore_errors=True); os.makedirs(os.path.join(SRC, 'figures'))
    for f in (J + '.tex', 'references.bib', J + '.bbl'): shutil.copy(os.path.join(tmp, f), os.path.join(SRC, f))
    for n, _ in FIGS: shutil.copy(os.path.join(tmp, 'figures', n + '.pdf'), os.path.join(SRC, 'figures', n + '.pdf'))
    pages = re.search(r'Output written on ' + J + r'.pdf \((\d+) pages', log)
    bbl = open(os.path.join(tmp, J + '.bbl')).read(); nref = bbl.count('\\bibitem')
    if 'undefined' in log and re.search(r'Citation .* undefined', log): raise SystemExit('undefined citation in supplement')
    print('supplement references:', nref)
    print('Supplementary_Material.pdf', pages.group(1) if pages else '?', 'pages; overfull hboxes:', log.count('Overfull \\hbox'), '; missing glyphs:', log.count('Missing character'))
if __name__ == '__main__': main()

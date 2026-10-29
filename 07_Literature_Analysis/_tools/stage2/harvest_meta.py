"""Stage 2: harvest bibliographic metadata for every note from Crossref (DOI registration metadata) and the arXiv API.
Raw responses are cached in cache/<id>.json for audit. No values are written to notes by this script."""
import yaml, glob, os, json, re, time, urllib.request, urllib.parse, difflib, sys
import xml.etree.ElementTree as ET
T = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(T, '..', '..', '..'))
UA = {'User-Agent': 'VLM-SocialNav-Survey-metadata-check/1.0'}
def get(url):
    for i in range(3):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40).read().decode('utf-8', 'replace')
        except Exception as e:
            err = e; time.sleep(3)
    return 'ERROR: ' + str(err)
def norm(s): return re.sub(r'[^a-z0-9 ]', '', re.sub(r'\s+', ' ', str(s).lower())).strip()
def sim(a, b): return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()
def crossref(title, author):
    q = urllib.parse.urlencode({'query.bibliographic': title, 'query.author': author, 'rows': 5})
    r = get('https://api.crossref.org/works?' + q)
    try: items = json.loads(r)['message']['items']
    except Exception: return {'error': r[:200]}
    out = []
    for it in items:
        t = (it.get('title') or [''])[0]
        out.append({'sim': round(sim(t, title), 3), 'DOI': it.get('DOI'), 'type': it.get('type'), 'title': t,
                    'container': (it.get('container-title') or [''])[0], 'event': (it.get('event') or {}).get('name'),
                    'volume': it.get('volume'), 'issue': it.get('issue'), 'page': it.get('page'), 'article-number': it.get('article-number'),
                    'published': (it.get('published') or {}).get('date-parts'), 'publisher': it.get('publisher'),
                    'authors': [f"{a.get('given','')} {a.get('family','')}".strip() for a in it.get('author', [])][:12],
                    'url': (it.get('resource') or {}).get('primary', {}).get('URL') or it.get('URL')})
    return sorted(out, key=lambda x: -x['sim'])
NS = {'a': 'http://www.w3.org/2005/Atom', 'x': 'http://arxiv.org/schemas/atom'}
def arxiv(title):
    t = re.sub(r'[^A-Za-z0-9 ]', ' ', title); t = ' '.join(t.split()[:14])
    r = get('https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query': f'ti:"{t}"', 'max_results': 3}))
    try: root = ET.fromstring(r)
    except Exception: return {'error': r[:200]}
    out = []
    for e in root.findall('a:entry', NS):
        tt = ' '.join(e.find('a:title', NS).text.split())
        out.append({'sim': round(sim(tt, title), 3), 'id': e.find('a:id', NS).text, 'title': tt,
                    'published': e.find('a:published', NS).text, 'updated': e.find('a:updated', NS).text,
                    'journal_ref': (e.find('x:journal_ref', NS).text if e.find('x:journal_ref', NS) is not None else None),
                    'doi': (e.find('x:doi', NS).text if e.find('x:doi', NS) is not None else None),
                    'comment': (e.find('x:comment', NS).text if e.find('x:comment', NS) is not None else None),
                    'authors': [a.find('a:name', NS).text for a in e.findall('a:author', NS)][:12]})
    return sorted(out, key=lambda x: -x['sim'])
only = sys.argv[1:]
for f in sorted(glob.glob(os.path.join(ROOT, '08_Paper_Notes', '*.md'))):
    y = yaml.safe_load(open(f).read().split('---')[1]); nid = y['id']
    if only and nid not in only: continue
    cp = os.path.join(T, 'cache', nid + '.json')
    if os.path.exists(cp) and not only: continue
    fa = (y.get('authors') or [''])[0]; fam = fa.split()[-1] if fa else ''
    res = {'id': nid, 'title': y['title'], 'first_author': fa, 'queried': time.strftime('%Y-%m-%d'),
           'crossref': crossref(y['title'], fam), 'arxiv': arxiv(y['title'])}
    json.dump(res, open(cp, 'w'), indent=1); time.sleep(1.5)
    c = res['crossref'][0] if isinstance(res['crossref'], list) and res['crossref'] else {}
    a = res['arxiv'][0] if isinstance(res['arxiv'], list) and res['arxiv'] else {}
    print(nid, '| CR', c.get('sim'), c.get('DOI'), c.get('type'), '| AX', a.get('sim'), a.get('id'), a.get('doi'), flush=True)

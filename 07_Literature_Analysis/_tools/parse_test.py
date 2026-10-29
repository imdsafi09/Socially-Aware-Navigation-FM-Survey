import yaml,glob,sys,os
d=__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','..','08_Paper_Notes')
ok=0
for f in sorted(glob.glob(d+'/*.md')):
    t=open(f).read()
    if not t.startswith('---'): print('NOFM',f); continue
    fm=t.split('---',2)[1]
    try:
        y=yaml.safe_load(fm); ok+=1
        caps=y.get('capabilities',{})
        if len(caps)!=25: print('CAPS',os.path.basename(f),len(caps))
        for k in ['id','category','evidence','integration','peer_reviewed','year','title']:
            if k not in y: print('MISSING',k,os.path.basename(f))
        if y['id']+'.md'!=os.path.basename(f): print('IDMISMATCH',f)
    except Exception as e: print('ERR',os.path.basename(f),str(e)[:300])
print('parsed',ok)

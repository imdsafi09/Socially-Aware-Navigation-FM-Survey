import yaml,glob,os,re,csv,json,collections
ROOT=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','..'))
def notes():
    N={}
    for f in sorted(glob.glob(ROOT+'/08_Paper_Notes/*.md')):
        t=open(f).read(); _,fm,body=t.split('---',2); y=yaml.safe_load(fm); y['_body']=body; N[y['id']]=y
    return N
def direct(N): return {k:v for k,v in N.items() if v['category'] in ('S4','S5')}

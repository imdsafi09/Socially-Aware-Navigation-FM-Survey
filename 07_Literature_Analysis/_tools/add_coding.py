"""Adds/updates a standardized `coding:` block and `physical_source_folder`/`analytical_category`
fields to every note's YAML front matter. Codes are manual judgments derived from the note's own
free-text fields (deployment/repro/exp); rules are documented in CODING_RULES below and in
09_Project_Reports/CORPUS_SUMMARY.md."""
import yaml,glob,os,re,json
N=__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','..','08_Paper_Notes')
CODING_RULES={
 'latency_reported':'Yes = numeric FM/system inference time or rate reported (s, Hz, FPS); Partial = only qualitative/figure; No = not reported; NA = survey',
 'safety_mechanism':'Yes = explicit safety layer independent of the FM in the deployed/evaluated system (collision checking, CBF, obstacle-cost planner, reflex/velocity filter, restriction to collision-free candidates); No = none reported; NA = survey or non-FM paper',
 'uncertainty_treatment':'Yes = explicit uncertainty quantification used in decisions; Partial = indirect (likelihoods propagated, multi-answer/ambiguity sets, stochastic prediction outside FM); No; NA = survey or non-FM paper',
 'hallucination_treatment':'Yes = structural mitigation (FM output restricted to pre-verified options/bounded scores, or verification step) ; Partial = prompt-level or training-level mitigation claimed without verification; No; NA = survey or non-FM paper',
 'code_released':'Yes = code available or stated available; Promised = to be released; Partial = partial/related code; No = not reported or not released; NA = survey',
 'new_dataset_released':'Yes = paper introduces and releases/makes public a new dataset/benchmark; No = new data created but not stated released; NA = no new dataset or survey',
 'real_robot':'Systematic = evidence >= E3; Demo = qualitative real-robot demonstration only; No; NA = survey',
 'human_subject_study':'Yes = formal human evaluation of robot behaviour (E4); Text-raters = humans rated model text/annotations only; No; NA = survey',
}
manual={
# id: (latency, safety, uncertainty, hallucination, code, newdata)
'2024_Sathyamoorthy_CoNVOI':('Yes','Yes','No','Partial','Yes','NA'),
'2025_Narasimhan_OLiVia-Nav':('Yes','No','No','No','No','No'),
'2025_Luo_GSON':('Yes','Yes','No','Partial','No','No'),
'2025_Payandeh_Social-LLaVA':('No','No','No','Partial','No','Yes'),
'2025_Song_VLM-Social-Nav':('Yes','Yes','No','Partial','No','NA'),
'2025_Weerakoon_BehAV':('Yes','Yes','Partial','No','Yes','NA'),
'2025_Wen_HSAC-LLM':('No','No','No','No','No','NA'),
'2026_Bejarano_PAD':('No','Yes','No','No','No','NA'),
'2026_Chen_SocialNav-CVPR':('Yes','No','No','No','No','No'),
'2026_Fang_Obstacles-to-Etiquette':('No','Yes','Partial','Yes','No','No'),
'2025_Kong_AutoSpatial':('No','No','No','Partial','No','No'),
'2026_Wang_MAction-SocialNav':('Yes','No','Partial','No','No','No'),
'2026_Xiao_E-SocialNav':('Yes','No','No','Partial','Yes','No'),
'2025_Kawabata_SocialNav-MoE':('Yes','No','No','No','Promised','NA'),
'2026_Elnoor_ViLAM':('Yes','Yes','No','No','No','No'),
'2026_Liao_G2-Nav':('Yes','Yes','Partial','Yes','Promised','NA'),
'2026_Xiao_Prompting-VLMs-JSAI':('No','No','No','No','No','NA'),
'2026_Xu_HCSG':('No','No','No','No','Partial','NA'),
'2026_Zhang_GCL':('No','No','No','No','No','NA'),
'2026_Zhang_SOPD-SocialNav':('Yes','No','No','No','No','NA'),
# FM-based social benchmarks/datasets
'2024_Li_HA-VLN':('No','No','No','Partial','Yes','Yes'),
'2026_Dong_HA-VLN-2.0':('No','No','No','Partial','Yes','Yes'),
'2026_Liu_MUSON':('No','NA','No','Partial','No','Yes'),
'2025_Munje_SocialNav-SUB':('No','NA','Partial','NA','Yes','Yes'),
# adjacent FM
'2022_Ahn_SayCan':('No','No','Partial','Yes','Partial','NA'),
'2022_Shah_LM-Nav':('No','No','Partial','No','Yes','NA'),
'2023_Brohan_RT-2':('Yes','No','No','Partial','No','NA'),
'2023_Driess_PaLM-E':('No','No','No','No','No','NA'),
'2023_Huang_VLMaps':('No','No','No','No','Yes','NA'),
'2023_Huang_VoxPoser':('No','No','No','No','Partial','NA'),
'2023_Liang_Code-as-Policies':('No','No','No','No','Yes','Yes'),
'2023_Shah_GNM':('No','No','NA','NA','Yes','Yes'),
'2023_Shah_ViNT':('Partial','No','NA','Partial','Yes','NA'),
'2024_Sridhar_NoMaD':('No','No','Partial','NA','Yes','NA'),
'2024_Yokoyama_VLFM':('Partial','No','Partial','No','No','NA'),
'2024_Zhou_NavGPT':('No','No','No','Partial','Yes','NA'),
'2025_Song_VL-TGS':('Yes','Yes','No','Yes','No','NA'),
'2024_Shcherbyna_Arena-4.0':('Partial','NA','NA','NA','Yes','Yes'),
# Stage-2 additions (direct FM social navigation)
'2026_Payandeh_Narrate2Nav':('No','No','No','No','No','No'),
'2026_Chen_LISN':('Yes','Yes','No','Partial','No','No'),
'2026_Huo_NORM-Nav':('No','Yes','No','Yes','No','NA'),
'2025_Sotomi_Transparent-Social-Nav-VLM':('Yes','No','No','No','No','NA'),
'2025_Saito_VLM-Crowd-Mapping':('No','Yes','Partial','No','No','NA'),
'2025_Martinez-Baselga_Hey-Robot':('Yes','Yes','No','Yes','Promised','NA'),
'2026_Wang_LE-Nav':('Yes','Yes','Partial','Partial','Yes','No'),
'2024_Holk_PREDILECT':('No','Yes','No','No','No','NA'),
'2025_Liang_MOSU':('Yes','No','No','Partial','No','NA'),
'2024_Wang_SALM':('No','No','No','Partial','No','NA'),
'2025_Wang_SAMALM':('No','No','Partial','Yes','No','NA'),
'2026_Zhang_Walk-With-Me':('No','No','No','No','No','NA'),
'2026_Wang_SALSA':('No','No','No','No','No','NA'),
'2026_Ahmadi_HUMA':('Yes','No','No','No','No','NA'),
'2026_Park_TACET':('Yes','Yes','No','Partial','No','No'),  # 2026-10-27 claim-citation audit correction (CLAIM_CITATION_INTEGRITY_AUDIT.md, Post-audit corrections): reasoner latency 2.6 s median, 95th pct 3.5 s (p3)
'2026_Zhang_SAATT-Nav':('No','Yes','Partial','Yes','No','NA'),
'2026_Sethuraman_Context-Aware-Preferences':('Yes','No','No','Partial','Yes','NA'),
'2024_Yu_PANav':('No','Yes','Partial','Yes','No','NA'),
'2026_Fang_Group-Joining':('Yes','Yes','No','NA','No','No'),
'2026_Zhao_EvoNav':('No','No','No','Partial','No','NA'),
'2026_Hu_SPARK-VLN':('Yes','No','No','No','No','No'),
'2026_Zhang_AHead-VLN':('No','No','No','Yes','No','NA'),  # Stage 9: no numeric latency; no FM-independent guard on executed actions; structural output restriction
'2025_Ruo_LLM-Social-Cues':('No','Yes','No','Yes','No','NA'),  # Stage 11: CBF constraints independent of the LLM; bounded function-calling outputs
'2026_Gandotra_RBTLR':('Yes','Yes','No','No','No','NA'),  # Stage 11: 0.33 s cycle; collision-free RRT-Connect candidates
'2026_Oush_VLA-TurtleBot':('Partial','Yes','No','Yes','No','NA'),  # Stage 11: LLM delay discussed only; LiDAR safety layer; discrete action set
# Stage-2 additions (FM-based benchmarks/evaluation)
'2024_Marpally_SocRATES':('Yes','NA','No','Partial','No','NA'),
'2025_Zhang_FewShot-Perception':('No','NA','No','No','No','No'),
'2026_Huang_SONG':('No','NA','No','No','No','No'),
'2026_Dai_DPed-VLN':('No','NA','No','No','Yes','Yes'),
}
nonfm_latency={'2010_Trautman_Unfreezing-IGP':'Yes','2012_Kuderer_Feature-Based-Prediction':'Yes','2017_Chen_CADRL':'Yes','2017_Chen_SA-CADRL':'Yes','2018_Tai_GAIL-Depth':'Yes','2022_Biswas_SocNavBench':'Yes'}
nonfm_code={'2018_Tai_GAIL-Depth':'Yes','2019_Chen_SARL-CrowdNav':'Yes','2020_Tsoi_SEAN':'Yes','2021_Kastner_Arena-Rosnav':'Yes','2022_Biswas_SocNavBench':'Yes','2023_Wang_NaviSTAR':'Yes','2016_Okal_Bayesian-IRL':'Partial','2023_Nguyen_MuSoHu':'Yes'}
nonfm_data={'2018_Tai_GAIL-Depth':'Yes','2022_Biswas_SocNavBench':'Yes','2022_Karnan_SCAND':'Yes','2023_Nguyen_MuSoHu':'Yes','2024_Hirose_SACSoN':'Yes'}
def rr(y):
    if y['category']=='S0': return 'NA'
    ev=str(y['evidence']); rt=str(y['exp'].get('real_robot_trials',''))
    if ev in ('E3','E4','E5'): return 'Systematic'
    if rt.startswith('Yes') or rt.startswith('Partial'): return 'Demo'
    return 'No'
def hs(y):
    if y['category']=='S0': return 'NA'
    if str(y['evidence']) in ('E4','E5'): return 'Yes'
    h=str(y['exp'].get('human_study',''))
    if h.startswith('Yes') or 'rat' in h.lower() or 'judge' in h.lower() or 'evaluators' in h.lower(): return 'Text-raters/other'
    return 'No'
for f in sorted(glob.glob(N+'/*.md')):
    t=open(f).read(); _,fm,body=t.split('---',2)
    y=yaml.safe_load(fm); i=y['id']
    fm=re.sub(r'\ncoding:\n(  .*\n)+','\n',fm)
    fm=re.sub(r'\nphysical_source_folder: .*','',fm); fm=re.sub(r'\nanalytical_category: .*','',fm)
    if y['category']=='S0':
        c=dict(latency_reported='NA',safety_mechanism='NA',uncertainty_treatment='NA',hallucination_treatment='NA',code_released='NA',new_dataset_released='NA')
    elif i in manual:
        a=manual[i]; c=dict(zip(['latency_reported','safety_mechanism','uncertainty_treatment','hallucination_treatment','code_released','new_dataset_released'],a))
    else:
        c=dict(latency_reported=nonfm_latency.get(i,'No'),safety_mechanism='NA',uncertainty_treatment='NA',hallucination_treatment='NA',code_released=nonfm_code.get(i,'No'),new_dataset_released=nonfm_data.get(i,'NA'))
    c['real_robot']=rr(y); c['human_subject_study']=hs(y)
    psf=os.path.dirname(y['source_pdfs'][0])
    add=f'physical_source_folder: "{psf}"\nanalytical_category: "{y["category"]}"\ncoding:\n'+''.join(f'  {k}: "{v}"\n' for k,v in c.items())
    fm=fm.rstrip('\n')+'\n'+add
    open(f,'w').write('---'+fm+'---'+body)
    y2=yaml.safe_load(fm); assert y2['coding']==c
print('ok')
json.dump(CODING_RULES,open(os.path.dirname(__file__)+'/coding_rules.json','w'),indent=1)

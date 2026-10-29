"""Stage 3: write the FINAL taxonomy coding into every note as `final_coding` (authoritative).
Old F/I/E/C fields stay in the notes as provenance and are exported to matrices with a `legacy_` prefix."""
import os, re, yaml, glob, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from final_codes import *
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
ADJ = {  # capability adjudications from the metric-route consistency check (TAXONOMY_CONSISTENCY_AUDIT.md section 3)
 '2024_Wang_SALM': {'SPA1': 'Yes'}, '2025_Wang_SAMALM': {'SPA1': 'Yes'}, '2025_Song_VLM-Social-Nav': {'EXP1': 'Yes'}, '2025_Wen_HSAC-LLM': {'SAF2': 'Yes'},
 '2026_Bejarano_PAD': {'SAF2': 'Yes'}, '2026_Chen_SocialNav-CVPR': {'NOR1': 'Partial'}, '2026_Elnoor_ViLAM': {'SAF1': 'Partial'}, '2026_Fang_Group-Joining': {'SPA1': 'Yes'},
 '2026_Park_TACET': {'SPA1': 'Yes'}, '2026_Xu_HCSG': {'SAF2': 'Partial'}, '2026_Zhang_SAATT-Nav': {'SAF2': 'Yes'}}
AUDIT = {  # 2026-10-27 claim-citation audit corrections, checked against the full texts (CLAIM_CITATION_INTEGRITY_AUDIT.md, Post-audit corrections)
 '2026_Zhang_Walk-With-Me': {'NOR2': 'No'},          # instructions are destination requests ("I want to go for a walk"), not social instructions
 # HUM1 evaluated only with a prediction-specific metric; ablations of a forecasting module on navigation metrics = addressed (applied to both sets)
 '2026_Fang_Obstacles-to-Etiquette': {'HUM1': 'Partial'}, '2026_Xu_HCSG': {'HUM1': 'Partial'}, '2026_Zhang_AHead-VLN': {'HUM1': 'Partial'},
 '2010_Trautman_Unfreezing-IGP': {'HUM1': 'Partial'}, '2023_Wang_NaviSTAR': {'HUM1': 'Partial'},
 # 2024_Raj_Hybrid-Social-Nav EXP2 kept as evaluated: p5 lists the item 'It was clear what the robot wanted to do' (Frontal Approach Q5, Narrow Doorway Q4), per-question averages in Fig. 5 (audit finding CCI-107 overturned)
}
for k, v in CAP_OVERRIDE.items(): ADJ.setdefault(k, {}).update(v)
for k, v in AUDIT.items(): ADJ.setdefault(k, {}).update(v)
MEMORY = {'2025_Narasimhan_OLiVia-Nav': 'lifelong caption/embedding database', '2026_Sethuraman_Context-Aware-Preferences': 'persistent rule memory updated from user feedback'}
ADAPT = {'2025_Narasimhan_OLiVia-Nav': 'online lifelong update', '2026_Sethuraman_Context-Aware-Preferences': 'rule updating from user feedback'}
PRIVACY = {'2024_Yu_PANav': 'privacy of occupants is the navigation objective'}
def loc(y, iface):
    s = str((y.get('deployment') or {}).get('api_cloud_local', 'Not reported'))
    if iface and set(iface) <= {'D7'}: return 'n/a (FM used at training time only)'
    if iface and set(iface) <= {'D0'}: return 'n/a (offline evaluation only)'
    if re.search(r'hybrid', s, re.I) or (re.search(r'cloud|api', s, re.I) and re.search(r'local', s, re.I)): return 'hybrid (local + cloud)'
    if re.search(r'remote server|server', s, re.I): return 'remote server'
    if re.search(r'cloud|api', s, re.I): return 'cloud API'
    if re.search(r'local', s, re.I): return 'local/onboard or local server'
    return 'not reported'
def ev_nondirect(y):
    e = str(y['evidence']); c = y['coding']; sims = (y.get('exp') or {}).get('simulators')
    return {'EV1_offline': 'Yes' if e == 'E1' else 'No', 'EV2_closed_loop_sim': 'Yes' if (e == 'E2' or (sims and sims not in ('Not reported', [], 'NA'))) and e != 'NA' else 'No',
            'EV3_physical_robot': {'Systematic': 'systematic', 'Demo': 'demo'}.get(c['real_robot'], 'none'), 'EV4_real_humans_in_trials': 'not coded (non-direct work)',
            'EV5_human_evaluation': {'Yes': 'robot-behaviour evaluation (type not differentiated)', 'Text-raters/other': 'text-raters'}.get(c['human_subject_study'], 'none'),
            'EV6_open_world_deployment': 'No'}
def main():
    n = 0
    for f in sorted(glob.glob(ROOT + '/08_Paper_Notes/*.md')):
        t = open(f).read(); _, fm, body = t.split('---', 2); y = yaml.safe_load(fm); k = y['id']
        if y['category'] == 'S0':
            fc = {'status': 'NA (survey)'}
        else:
            caps = leaf_values(y.get('capabilities') or {}); caps.update(ADJ.get(k, {}))
            fc = {'taxonomy_version': 'Stage-3 final (2026-10-19)', 'A_social_representation': A[k].split(),
                  'C_capabilities': caps}
            if y['category'] in ('S4', 'S5'):
                d = direct_final(k); c = y['coding']; e = y['exp']
                fc.update({'B_roles': d['roles'], 'D_interface': d['interface'],
                           'E_evidence_profile': {kk: d[kk] for kk in d if kk.startswith('EV')},
                           'E_quality_attributes': {'trials': e.get('n_trajectories'), 'statistical_testing': e.get('statistical_testing'),
                                                    'cross_environment': 'Yes' if str(e.get('indoor_outdoor')) == 'both' else 'No/unclear', 'runtime_measured': c['latency_reported']},
                           'cross_cutting': {'temporal_coupling': d['temporal_coupling'], 'memory': MEMORY.get(k, 'No'), 'continual_adaptation': ADAPT.get(k, 'No'),
                                             'explanation_output': 'Yes (human-facing)' if 'R5' in d['roles'] else ('Yes (text output, not delivered to people)' if re.search(r'explanation', str(y.get('outputs')), re.I) else 'No'),
                                             'safety_guard': c['safety_mechanism'], 'uncertainty': c['uncertainty_treatment'], 'hallucination_mitigation': c['hallucination_treatment'],
                                             'privacy_constraint': PRIVACY.get(k, 'No'), 'inference_location': loc(y, d['interface'])}})
            else:
                fc.update({'B_roles': 'NA (not a direct FM social-navigation method)', 'D_interface': 'NA', 'E_evidence_profile': ev_nondirect(y)})
        y['final_coding'] = fc
        out = '---\n' + yaml.safe_dump(y, sort_keys=False, allow_unicode=True, width=1000, default_flow_style=None) + '---' + body
        yaml.safe_load(out.split('---')[1]); open(f, 'w').write(out); n += 1
    print('notes updated', n)
if __name__ == '__main__': main()

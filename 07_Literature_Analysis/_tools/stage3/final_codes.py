"""Stage-3 FINAL taxonomy: definitions, old->new mappings and manual codes (authoritative)."""
from recode import NEW
AXIS_A = {'A0': 'Humans not represented', 'A1': 'Kinematic agent (position/velocity/disc, tracked obstacle)', 'A2': 'Predicted motion (trajectory forecast/distribution)',
          'A3': 'Social-space field (proxemic potential, personal/group space, social cost layer)', 'A4': 'Relational/interaction structure (pairwise, graph, group, attention over agents)',
          'A5': 'Symbolic/linguistic description (attributes, captions, intents/rules in language)', 'A6': 'Implicit perceptual/latent (raw images to a learned model, embeddings)'}
ROLES = {'R1': 'Scene and context interpretation', 'R2': 'Human-state and relation inference', 'R3': 'Social-norm reasoning and behaviour selection',
         'R4': 'Instruction/preference grounding and task planning', 'R5': 'Human-facing communication (dialogue/explanation)'}
IFACE = {'D0': 'Non-executed decision (output evaluated offline only)', 'D1': 'Semantic/social-state representation for planner',
         'D2': 'Candidate selection/ranking', 'D3': 'Objective, constraint or parameter shaping (runtime)', 'D4': 'Goal/waypoint/trajectory specification',
         'D5': 'Runtime latent conditioning of a learned policy', 'D6': 'Direct action generation', 'D7': 'Training-time supervision (FM absent at runtime)',
         'D8': 'Human-facing channel (no motion coupling)'}
X2D = {f'X{i}': f'D{i}' for i in range(9)}
CAPH = {  # family -> leaf -> old C codes
 'SAF Safety': {'SAF1 Collision avoidance': ['C1'], 'SAF2 Near-collision / risk margin': ['C2']},
 'SPA Spatial-social conduct': {'SPA1 Personal space / proxemics': ['C3'], 'SPA2 Group and conversation space': ['C9', 'C10'],
                                'SPA3 Encounter conventions (yield, pass, doorway, sidewalk/crosswalk, queue)': ['C12', 'C13', 'C14', 'C15', 'C16'], 'SPA4 Crowd navigation': ['C17']},
 'HUM Human understanding': {'HUM1 Motion understanding and prediction': ['C5', 'C6'], 'HUM2 Intention and activity inference': ['C7', 'C8']},
 'NOR Normative and contextual behaviour': {'NOR1 Etiquette / politeness': ['C11', 'C22'], 'NOR2 Explicit social-instruction following': ['C23'],
                                            'NOR3 Context-dependent conduct (incl. non-spatial: speed, noise)': ['C24'], 'NOR4 Cultural / norm adaptation': ['C25']},
 'EXP Human-experience outcomes': {'EXP1 Perceived safety and comfort': ['C4', 'C21'], 'EXP2 Legibility and predictability': ['C18', 'C19'], 'EXP3 Naturalness': ['C20']},
}
LEAVES = {l.split()[0]: (fam.split()[0], l, cs) for fam, ls in CAPH.items() for l, cs in ls.items()}
RANK = {'Yes': 2, 'Partial': 1}
def leaf_values(caps):
    out = {}
    for code, (fam, name, cs) in LEAVES.items():
        v = max((RANK.get(str(caps.get(c)), 0) for c in cs), default=0)
        allna = all(str(caps.get(c)) == 'NA' for c in cs)
        out[code] = 'NA' if allna else {2: 'Yes', 1: 'Partial', 0: 'No'}[v]
    return out
# Stage-3 capability overrides after flag resolution / metric-route check (documented in SOCIAL_CAPABILITY_TAXONOMY_REVIEW + audit)
CAP_OVERRIDE = {'2024_Yu_PANav': {'NOR3': 'Partial'}}   # privacy reclassified as ethical/deployment constraint, not a capability
A = {
 '1995_Helbing_Social-Force': 'A1 A3 A4', '2010_Trautman_Unfreezing-IGP': 'A2 A4', '2012_Kuderer_Feature-Based-Prediction': 'A2', '2016_Kretzschmar_Socially-Compliant-IRL': 'A2 A4',
 '2016_Okal_Bayesian-IRL': 'A1 A4', '2017_Chen_CADRL': 'A1', '2017_Chen_SA-CADRL': 'A1', '2018_Tai_GAIL-Depth': 'A6', '2019_Chen_SARL-CrowdNav': 'A1 A4',
 '2022_Kim_Group-Estimation': 'A3 A4', '2023_Wang_NaviSTAR': 'A1 A4 A6', '2024_Raj_Hybrid-Social-Nav': 'A1 A6',
 '2022_Ahn_SayCan': 'A0', '2022_Shah_LM-Nav': 'A0', '2023_Brohan_RT-2': 'A6', '2023_Driess_PaLM-E': 'A0', '2023_Huang_VLMaps': 'A0', '2023_Huang_VoxPoser': 'A0',
 '2023_Liang_Code-as-Policies': 'A0', '2023_Shah_GNM': 'A0', '2023_Shah_ViNT': 'A6', '2024_Sridhar_NoMaD': 'A0', '2024_Yokoyama_VLFM': 'A0', '2024_Zhou_NavGPT': 'A0', '2025_Song_VL-TGS': 'A0',
 '2024_Holk_PREDILECT': 'A1', '2024_Sathyamoorthy_CoNVOI': 'A1 A6', '2025_Kong_AutoSpatial': 'A5', '2025_Luo_GSON': 'A1 A2 A3 A4', '2025_Martinez-Baselga_Hey-Robot': 'A1 A2',
 '2025_Narasimhan_OLiVia-Nav': 'A5 A6', '2025_Payandeh_Social-LLaVA': 'A5', '2025_Saito_VLM-Crowd-Mapping': 'A5', '2025_Song_VLM-Social-Nav': 'A1 A5',
 '2025_Sotomi_Transparent-Social-Nav-VLM': 'A5 A6', '2025_Weerakoon_BehAV': 'A3 A5', '2025_Wen_HSAC-LLM': 'A1 A5', '2026_Bejarano_PAD': 'A1 A2 A5', '2026_Chen_LISN': 'A1 A3 A5',
 '2026_Chen_SocialNav-CVPR': 'A6', '2026_Fang_Obstacles-to-Etiquette': 'A1 A2 A3 A5', '2026_Huo_NORM-Nav': 'A3 A5', '2026_Payandeh_Narrate2Nav': 'A5 A6', '2026_Wang_LE-Nav': 'A1 A5',
 '2026_Wang_MAction-SocialNav': 'A5', '2026_Xiao_E-SocialNav': 'A5', '2024_Wang_SALM': 'A1 A4 A5', '2024_Yu_PANav': 'A3', '2025_Kawabata_SocialNav-MoE': 'A5', '2025_Liang_MOSU': 'A6',
 '2025_Wang_SAMALM': 'A1 A5', '2026_Ahmadi_HUMA': 'A5 A6', '2026_Elnoor_ViLAM': 'A3 A6', '2026_Fang_Group-Joining': 'A1 A3 A4', '2026_Hu_SPARK-VLN': 'A6', '2026_Liao_G2-Nav': 'A1 A3 A5',  # audit 2026-10-27: no human trajectory prediction; velocity-shaped Gaussian at current position = A3 (p5 eq. 2)

 '2026_Park_TACET': 'A6', '2026_Sethuraman_Context-Aware-Preferences': 'A1', '2026_Wang_SALSA': 'A6', '2026_Xiao_Prompting-VLMs-JSAI': 'A5', '2026_Xu_HCSG': 'A1 A2 A5 A6',
 '2026_Zhang_GCL': 'A5', '2026_Zhang_SAATT-Nav': 'A1 A2 A3 A5', '2026_Zhang_SOPD-SocialNav': 'A5', '2026_Zhang_Walk-With-Me': 'A6', '2026_Zhang_AHead-VLN': 'A2 A5 A6', '2025_Ruo_LLM-Social-Cues': 'A1 A3 A5', '2026_Gandotra_RBTLR': 'A1 A5 A6', '2026_Oush_VLA-TurtleBot': 'A1 A5', '2026_Zhao_EvoNav': 'A1',
 '2020_Tsoi_SEAN': 'A1', '2021_Kastner_Arena-Rosnav': 'A0', '2022_Biswas_SocNavBench': 'A1 A2', '2022_Karnan_SCAND': 'A6', '2023_Nguyen_MuSoHu': 'A6', '2024_Hirose_SACSoN': 'A6',
 '2024_Li_HA-VLN': 'A1 A5', '2024_Marpally_SocRATES': 'A1', '2024_Shcherbyna_Arena-4.0': 'A1 A4', '2025_Munje_SocialNav-SUB': 'A1 A2 A4', '2025_Zhang_FewShot-Perception': 'A1 A5',
 '2026_Dai_DPed-VLN': 'A1', '2026_Dong_HA-VLN-2.0': 'A1 A3 A4 A5', '2026_Huang_SONG': 'A1', '2026_Liu_MUSON': 'A2 A5',
}
# Evidence profile EV1-EV6 for direct papers (from recode vector; humans refined)
HUMANS = {'2024_Sathyamoorthy_CoNVOI': 'present-type-unreported', '2025_Liang_MOSU': 'none', '2025_Narasimhan_OLiVia-Nav': 'staged', '2026_Chen_SocialNav-CVPR': 'not-reported',
          '2026_Huo_NORM-Nav': 'present-type-unreported', '2026_Payandeh_Narrate2Nav': 'present-type-unreported', '2026_Sethuraman_Context-Aware-Preferences': 'present-type-unreported',
          '2026_Xu_HCSG': 'present-type-unreported', '2026_Fang_Group-Joining': 'present-type-unreported', '2025_Weerakoon_BehAV': 'staged',
          # audit 2026-10-27: unrecruited/naturally occurring status not established by the source (location alone is not sufficient)
          '2025_Sotomi_Transparent-Social-Nav-VLM': 'present-type-unreported', '2026_Elnoor_ViLAM': 'present-type-unreported', '2026_Liao_G2-Nav': 'present-type-unreported',
          '2026_Wang_LE-Nav': 'present-type-unreported', '2026_Zhang_Walk-With-Me': 'present-type-unreported'}
HMAP = {'none': 'none', 'sim': 'simulated-only', 'staged': 'staged', 'natural': 'unscripted', 'unspecified': 'present-type-unreported'}
EV6 = {}  # no direct paper has open-world / long-duration deployment
TEMPORAL = {k: v[3] for k, v in NEW.items()}
def direct_final(k):
    r, x, v, tm = NEW[k]
    off, sim, rob, hum, hev = v.split()
    hum = HUMANS.get(k, HMAP[hum])
    if rob == 'none' and hum not in ('simulated-only', 'none'): hum = 'none'
    if rob != 'none' and hum == 'simulated-only': hum = 'not-reported'  # real-robot runs whose human participants are not described
    return {'roles': r.split(), 'interface': [X2D[t] for t in x.split()], 'temporal_coupling': tm,
            'EV1_offline': 'Yes' if off == 'Y' else 'No', 'EV2_closed_loop_sim': 'Yes' if sim == 'Y' else 'No', 'EV3_physical_robot': rob,
            'EV4_real_humans_in_trials': hum if rob != 'none' else ('simulated-only' if sim == 'Y' and hum == 'simulated-only' else 'none'),
            'EV5_human_evaluation': {'none': 'none', 'text': 'text-raters', 'observer': 'observers/video', 'copresent': 'co-present participants'}[hev],
            'EV6_open_world_deployment': EV6.get(k, 'No')}

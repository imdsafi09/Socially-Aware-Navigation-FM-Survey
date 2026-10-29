"""Stage 9: build the pre-FM comparison set (07_Literature_Analysis/prefm_comparison_set.csv).

Selection rule (applied mechanically below):
  1. Candidate pool: pre-FM exemplars named in the paradigm sections of seven reference surveys (Kruse 2013, Charalampous 2017,
     Moller 2021, Mavrogiannis 2023, Singamaneni 2024, Alyassi 2025, Kabir 2026), plus a discovery pass over their reference lists
     (discover_common_refs.py). Survey-citation counts come from survey_citation_counts.py (title-fragment match).
  2. Eligibility: a social/human-aware navigation method, or a human-motion model built for or used in robot navigation; no FM;
     not a survey, dataset, simulator or pure human-factors study without a navigation method.
  3. Selection per paradigm: every eligible candidate cited by >= 3 of the 7 surveys; if a paradigm then holds fewer than 3 works
     (counting the 12 works already coded in the corpus), add the next most-cited eligible candidates (ties included) until it holds 3.
  4. The 12 pre-FM works of the frozen corpus are always retained with their frozen final coding.
Coding follows the frozen taxonomy (Axis A, capability leaves Yes/Partial, evidence EV1-EV6). 'ND' = not determinable from the
sources we could legitimately access; ND is never counted as evidence and is reported separately.
"""
import csv, os, json, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PARADIGMS = ['P1 Geometric and socially aware planning', 'P2 Proxemics and social costmaps', 'P3 Social-force models', 'P4 Group and F-formation navigation',
             'P5 Trajectory prediction and prediction-coupled planning', 'P6 Inverse reinforcement learning', 'P7 Imitation learning', 'P8 Deep reinforcement learning',
             'P9 Attention, graph and transformer models', 'P10 Hybrid model-based and learned']
PCODE = {p.split()[0]: p for p in PARADIGMS}
# candidate -> (paradigm, eligible, eligibility note)
CAND = {
 'Fiorini1998VO': ('P1', True, ''), 'vandenBerg2011ORCA': ('P1', True, ''), 'vandenBerg2008RVO': ('P1', True, ''), 'Sisbot2007HAMP': ('P1', True, ''),
 'Kirby2009COMPANION': ('P1', True, ''), 'Pandey2010Framework': ('P1', True, ''), 'Mavrogiannis2018SocialMomentum': ('P1', True, ''), 'Kruse2012Legible': ('P1', True, ''),
 'Lam2011Harmonious': ('P1', True, ''), 'Svenstrup2010Trajectory': ('P1', True, ''), 'Mehta2016MPDM': ('P1', True, ''), 'Thrun1999Minerva': ('P1', True, 'IJRR 2000 version (title matched in 3 surveys)'),
 'Mavrogiannis2019HRI': ('P1', True, 'user study of a navigation method (Social Momentum) against ORCA and teleoperation'),
 'Pacchierotti2006Passing': ('P2', True, ''), 'Lu2014Layered': ('P2', True, ''), 'Kollmitz2015TimeDependent': ('P2', True, ''), 'Truong2017Proactive': ('P2', True, ''),
 'Kruse2014Directional': ('P2', True, ''), 'Scandolo2011Anthropomorphic': ('P2', True, ''), 'Mead2016Proxemics': ('P2', True, ''), 'Chung2010Spatial': ('P2', True, ''),
 'Charalampous2016SocialMaps': ('P2', True, ''),
 'Moussaid2010Groups': ('P3', False, 'pedestrian-dynamics study without a robot navigation method'), 'Ferrer2013Companion': ('P3', True, ''), 'Shiomi2014Acceptable': ('P3', True, ''),
 'Zanlungo2011Explicit': ('P3', False, 'pedestrian model without a robot navigation method'), 'Ferrer2013SocialForceLearned': ('P3', True, ''),
 'RiosMartinez2011RiskRRT': ('P4', True, ''), 'Wang2021GMPC': ('P4', True, ''), 'Katyal2022GroupAware': ('P4', True, ''), 'Truong2017Approach': ('P4', True, ''),
 'Cristani2011FFormation': ('P4', False, 'F-formation detection without navigation'), 'Yang2020GroupSpace': ('P4', False, 'placeholder fragment; no matching work'),
 'Pellegrini2009YNWA': ('P5', True, 'social motion model used for tracking/prediction; ETH benchmark origin'), 'Alahi2016SocialLSTM': ('P5', True, ''), 'Gupta2018SocialGAN': ('P5', True, ''),
 'Salzmann2020Trajectronpp': ('P5', True, ''), 'Sadeghian2019SoPhie': ('P5', True, ''), 'Mohamed2020STGCNN': ('P5', True, ''), 'Bennewitz2005MotionPatterns': ('P5', True, ''),
 'Ziebart2009PlanningPrediction': ('P5', True, ''), 'Kitani2012Activity': ('P5', True, ''), 'Vemula2018SocialAttention': ('P5', True, ''), 'Trautman2015IJRR': ('P5', True, ''),
 'Henry2010Crowded': ('P6', True, ''), 'Vasquez2014IRLFeatures': ('P6', True, ''), 'Kim2016SociallyAdaptive': ('P6', True, ''), 'Luber2012Learning': ('P6', True, ''),
 'Pfeiffer2016Predictably': ('P7', True, ''), 'Hamandi2019DeepMoTIon': ('P7', True, ''), 'Pfeiffer2017Perception': ('P7', False, 'end-to-end collision avoidance without human-aware objective'),
 'Karnan2022SCAND': ('P7', False, 'dataset (S6 in the corpus), not a method'),
 'Everett2018GA3C': ('P8', True, ''), 'Everett2021PedRich': ('P8', True, ''), 'Long2018Decentralized': ('P8', False, 'multi-robot collision avoidance without humans'),
 'PerezDArpino2021Constrained': ('P8', True, ''), 'Sathyamoorthy2020DenseCAvoid': ('P8', True, ''), 'Samsani2021Resemblance': ('P8', True, ''), 'Liu2020DRLCrowded': ('P8', True, ''),
 'Chen2020RGL': ('P9', True, ''), 'Liu2021DSRNN': ('P9', True, ''), 'Liu2023CrowdNavpp': ('P9', True, ''), 'Chen2020Gaze': ('P9', True, ''), 'Zhou2022SGD3QN': ('P9', True, ''),
 'Brito2021Subgoal': ('P10', True, ''), 'Poddar2023CrowdMotion': ('P10', True, ''), 'Samavi2024SICNav': ('P10', True, ''), 'Kastner2021Connecting': ('P10', True, ''),
 'Sathyamoorthy2020Frozone': ('P10', True, ''),
}
# the 12 frozen corpus works (note id) and their paradigm
CORPUS12 = {'1995_Helbing_Social-Force': 'P3', '2010_Trautman_Unfreezing-IGP': 'P5', '2012_Kuderer_Feature-Based-Prediction': 'P6', '2016_Kretzschmar_Socially-Compliant-IRL': 'P6',
            '2016_Okal_Bayesian-IRL': 'P6', '2017_Chen_CADRL': 'P8', '2017_Chen_SA-CADRL': 'P8', '2018_Tai_GAIL-Depth': 'P7', '2019_Chen_SARL-CrowdNav': 'P9',
            '2022_Kim_Group-Estimation': 'P4', '2023_Wang_NaviSTAR': 'P9', '2024_Raj_Hybrid-Social-Nav': 'P10'}
CORPUS_CAND_KEYS = {'Helbing1995SFM', 'Trautman2010IGP', 'Kuderer2012Feature', 'Kretzschmar2016IRL', 'Okal2016BIRL', 'Chen2017CADRL', 'Chen2017SACADRL', 'Tai2018GAIL',
                    'Chen2019SARL', 'Kim2022Group', 'Wang2023NaviSTAR', 'Raj2024Hybrid'}
FT, SEC = 'full text', 'secondary: reference-survey descriptions (full text not legitimately accessible)'
# key -> coding. A, Yes leaves, Partial leaves, EV1 (offline vs recorded data), EV2, EV3, EV4, EV5, EV6, stats, source, url, venue, evidence note
C = {
 'vandenBerg2008RVO': ('A1', '', 'SAF1 SPA4', 'No', 'Yes', 'none', 'none', 'none', 'No', 'No', SEC, 'https://doi.org/10.1109/ROBOT.2008.4543489', 'ICRA 2008',
                       'Simulated multi-agent scenarios; collision- and oscillation-free motion shown qualitatively'),
 'Thrun1999Minerva': ('A1', 'SAF1', 'SPA4 EXP1', 'No', 'No', 'systematic', 'unscripted', 'co-present', 'Yes', 'No', SEC, 'https://doi.org/10.1177/02783640022067922', 'IJRR 19(11) 2000',
                      'Two-week museum deployment; statistics on performance and collision avoidance; visitor impressions of the robot (Mavrogiannis et al. 2023, Sec. 4.2.4.3)'),
 'Sisbot2007HAMP': ('A1 A3', '', 'SAF1 SPA1 EXP1 EXP2', 'No', 'Yes', 'demo', 'staged', 'none', 'No', 'No', SEC, 'https://doi.org/10.1109/TRO.2007.904911', 'IEEE T-RO 23(5) 2007',
                    'Safety, visibility and hidden-zone cost grids; robot-human interactions in a lab described as a demonstration (Mavrogiannis et al. 2023, Table 4)'),
 'Pandey2010Framework': ('A1 A3', '', 'SAF1 SPA1 SPA2 SPA3 NOR1', 'No', 'ND', 'ND', 'ND', 'ND', 'No', 'ND', SEC, 'https://doi.org/10.1109/IROS.2010.5649688', 'IROS 2010',
                         'Rule-based conventions (overtake on the right, avoid passing through groups, keep right in hallways) per Kruse et al. 2013; evaluation not determinable'),
 'Svenstrup2010Trajectory': ('A1 A2 A3', '', 'SAF1 SPA1 EXP3', 'No', 'Yes', 'none', 'none', 'none', 'No', 'No', FT, 'https://vbn.aau.dk/ws/files/43408396/05651531.pdf', 'IROS 2010',
                             'RRT/MPC through a person-dependent potential field; demonstrated in a simulated pedestrian street'),
 'Mavrogiannis2018SocialMomentum': ('A1 A4', 'EXP2', 'SAF1 SPA3 HUM1', 'No', 'Yes', 'none', 'none', 'observers/video', 'No', 'Yes', FT, 'https://rpal.cs.cornell.edu/docs/MavEtal_HRI_2018.pdf', 'HRI 2018',
                                    'Simulation; online video study of legibility (N = 180) with t-tests'),
 'Mavrogiannis2019HRI': ('A1 A4', 'EXP1', 'SAF1 SPA4 EXP2 EXP3', 'No', 'No', 'systematic', 'staged', 'co-present', 'No', 'Yes', FT, 'https://rpal.cs.cornell.edu/docs/MavEtal_HRI_2019.pdf', 'HRI 2019',
                         'Lab study, N = 105, three participants at a time; trajectories and questionnaire; statistical tests'),
 'Pacchierotti2006Passing': ('A1 A3', 'SPA1 EXP1', 'SAF1 SPA3', 'No', 'No', 'systematic', 'staged', 'co-present', 'No', 'No', FT, 'https://faculty.cc.gatech.edu/~hic/hic-papers/roman06-pacchierotti-final.pdf', 'RO-MAN 2006',
                             'Corridor passing with 10 participants; 5-point comfort ratings per lateral distance'),
 'Chung2010Spatial': ('A1 A2 A3', '', 'SPA1 HUM1 NOR3', 'No', 'ND', 'ND', 'ND', 'ND', 'No', 'ND', SEC, 'https://doi.org/10.1109/IROS.2010.5649718', 'IROS 2010',
                      'Map of place-specific "spatial effects" learned from observed pedestrians (Kruse et al. 2013); evaluation not determinable'),
 'Charalampous2016SocialMaps': ('A1 A3 A5', '', 'SPA1 HUM2 NOR3', 'No', 'ND', 'demo', 'ND', 'ND', 'No', 'ND', SEC, 'https://doi.org/10.1016/j.eswa.2016.09.026', 'Expert Syst. Appl. 66 (2016)',
                                'Deep action recognition assigns activity labels that select rule-based proxemic zones (Moller et al. 2021); custom robot base (Singamaneni et al. 2024)'),
 'Shiomi2014Acceptable': ('A1 A2', 'SAF2 EXP1', 'SAF1 SPA4 EXP3', 'No', 'No', 'systematic', 'unscripted', 'co-present', 'No', 'No', FT, 'https://irc.atr.jp/~m-shiomi/page/PDF/2014_IJSR_PedestrianModel_Submit.pdf', 'IJSR 6(3) 2014',
                          'Lab comparison rated by participants; two-hour shopping-mall field trials counting unsafe pedestrian reactions'),
 'Ferrer2013Companion': ('A1 A2 A4', '', 'SAF1 SPA1 EXP1', 'No', 'ND', 'demo', 'ND', 'ND', 'No', 'ND', SEC, 'https://doi.org/10.1109/IROS.2013.6696576', 'IROS 2013',
                         'Extended SFM with person-person, object-person and robot-person interactions (Charalampous et al. 2017); robot Tibi (Singamaneni et al. 2024)'),
 'Truong2017Approach': ('A1 A3 A4', '', 'SPA1 SPA2', 'No', 'ND', 'demo', 'ND', 'ND', 'No', 'ND', SEC, 'https://doi.org/10.1109/TCDS.2017.2751963', 'IEEE T-CDS 10(3) 2018',
                        'Approaching poses for individuals and groups using dynamic social zones; custom robot (Singamaneni et al. 2024)'),
 'Wang2021GMPC': ('A2 A3 A4', 'SAF1 SAF2 SPA2 SPA4', 'HUM1',  # audit 2026-10-27: prediction quality not evaluated (navigation metrics only)
 'No', 'Yes', 'none', 'none', 'none', 'No', 'Yes', FT, 'https://arxiv.org/abs/2107.11637', 'CoRL 2021',
                  'Simulated pedestrian scenes from ETH/UCY; group intrusions and minimum distance; Mann-Whitney tests; group-prediction ablation'),
 'Katyal2022GroupAware': ('A1 A4', 'SAF1 SPA1 SPA2 SPA4', '', 'No', 'Yes', 'none', 'none', 'none', 'No', 'Yes', FT, 'https://arxiv.org/abs/2012.12291', 'IROS 2022',
                          'CrowdNav simulation; collisions, individual discomfort, group intersections; t-tests'),
 'Pellegrini2009YNWA': ('A1 A2 A4', 'HUM1', '', 'Yes', 'No', 'none', 'none', 'none', 'No', 'No', SEC, 'https://doi.org/10.1109/ICCV.2009.5459260', 'ICCV 2009',
                        'Social motion model for tracking; prediction evaluated on recorded crowd video (ETH)'),
 'Alahi2016SocialLSTM': ('A2 A4', 'HUM1', '', 'Yes', 'No', 'none', 'none', 'none', 'No', 'No', FT, 'https://openaccess.thecvf.com/content_cvpr_2016/papers/Alahi_Social_LSTM_Human_CVPR_2016_paper.pdf', 'CVPR 2016',
                         'ADE/FDE on ETH and UCY'),
 'Vemula2018SocialAttention': ('A2 A4', 'HUM1', '', 'Yes', 'No', 'none', 'none', 'none', 'No', 'No', FT, 'https://arxiv.org/abs/1710.04689', 'ICRA 2018', 'ADE/FDE on ETH and UCY'),
 'Henry2010Crowded': ('A1', '', 'SPA3 SPA4 EXP3', 'No', 'Yes', 'none', 'none', 'none', 'No', 'No', FT, 'https://www.tu-ilmenau.de/fileadmin/Bereiche/IA/neurob/Publikationen/conferences_int/2010/Henry-ICRA-2010.pdf', 'ICRA 2010',
                      'Crowd simulator; path similarity to simulated human paths'),
 'Vasquez2014IRLFeatures': ('A1', '', 'SPA4 EXP3', 'Yes', 'Yes', 'none', 'none', 'none', 'No', 'No', SEC, 'https://doi.org/10.1109/IROS.2014.6942731', 'IROS 2014',
                            'Experimental comparison of IRL algorithms and crowd features on recorded crowd data (Alyassi et al. 2025; Mavrogiannis et al. 2023)'),
 'Kim2016SociallyAdaptive': ('A1 A3', '', 'SAF1 SPA1 SPA4 EXP3', 'No', 'No', 'systematic', 'present-type-unreported', 'none', 'No', 'No', FT, 'https://www.cs.mcgill.ca/~jpineau/files/kim-SORO15.pdf', 'IJSR 8(1) 2016',
                             'Robotic wheelchair; scenario-based and field runs compared with human trajectories'),
 'Luber2012Learning': ('A1 A2', '', 'SAF1 SPA1 EXP3', 'No', 'Yes', 'demo', 'ND', 'none', 'No', 'ND', SEC, 'https://doi.org/10.1109/IROS.2012.6385716', 'IROS 2012',
                       'Motion prototypes learned from overhead video; better than a proxemics baseline in simulation (Moller et al. 2021); listed as demonstration (Mavrogiannis et al. 2023)'),
 'Hamandi2019DeepMoTIon': ('A6', 'SAF1', 'SPA3 EXP3', 'No', 'Yes', 'none', 'none', 'none', 'No', 'No', FT, 'https://arxiv.org/abs/1803.03719', 'RO-MAN 2019',
                           'Trained on ETH pedestrians; simulated evaluation with collision counts and similarity to human paths'),
 'Everett2018GA3C': ('A1', 'SAF1 SPA4', 'SPA3', 'No', 'Yes', 'demo', 'staged', 'none', 'No', 'No', FT, 'https://arxiv.org/abs/1805.01956', 'IROS 2018',
                     'Simulation with up to 10 agents; hardware demonstration among pedestrians'),
 'Liu2020DRLCrowded': ('A1 A6', '', 'SAF1 SPA4', 'No', 'Yes', 'ND', 'ND', 'ND', 'No', 'ND', SEC, 'https://doi.org/10.1109/IROS45743.2020.9341540', 'IROS 2020',
                       'Imitation plus DRL with separate static and dynamic channels (abstract via publisher record); robot evidence not determinable'),
 'Chen2020RGL': ('A1 A4', 'SAF1 SPA4', 'HUM1', 'No', 'Yes', 'demo', 'present-type-unreported', 'none', 'No', 'No', FT, 'https://arxiv.org/abs/1909.13165', 'IROS 2020',
                 'CrowdNav simulation; Pioneer real-world demonstrations'),
 'Sathyamoorthy2020Frozone': ('A1 A2 A3', 'SAF1 SPA4', 'SPA1 SPA3', 'No', 'Yes', 'demo', 'present-type-unreported', 'none', 'No', 'No', FT, 'https://arxiv.org/abs/2003.05395', 'RA-L 5(3) 2020',
                              'Gazebo crowds (success, freezing rate, pedestrian-friendliness); Jackal and Turtlebot runs in indoor crowds'),
 'Brito2021Subgoal': ('A1 A2', 'SAF1 SPA4', '', 'No', 'Yes', 'none', 'none', 'none', 'No', 'Yes', FT, 'https://arxiv.org/abs/2102.13073', 'RA-L 6(3) 2021',
                      'Simulation with 6-10 agents; Mann-Whitney tests'),
}
TITLES = {r['key']: r for r in csv.DictReader(open(os.path.join(HERE, 'prefm_candidates_counts.csv')))}
def select():
    have = collections.Counter(CORPUS12.values()); sel = {}
    for p in PCODE:
        cands = sorted([(int(TITLES[k]['n_surveys']), k) for k, (pp, el, _) in CAND.items() if pp == p and el and k in TITLES and k not in CORPUS_CAND_KEYS], reverse=True)
        chosen = [(n, k, 'cited by >= 3 of 7 reference surveys') for n, k in cands if n >= 3]
        rest = [(n, k) for n, k in cands if n < 3 and n >= 1]
        while have[p] + len(chosen) < 3 and rest:
            top = rest[0][0]; tie = [x for x in rest if x[0] == top]
            chosen += [(n, k, f'fill rule: paradigm below 3 works; next most-cited (n = {n})') for n, k in tie]; rest = [x for x in rest if x[0] != top]
        for n, k, why in chosen: sel[k] = (p, n, why)
    return sel
def main():
    sel = select()
    missing = set(sel) - set(C); assert not missing, f'selected but not coded: {missing}'
    extra = set(C) - set(sel); assert not extra, f'coded but not selected: {extra}'
    CAPM = {r['id']: r for r in csv.DictReader(open(os.path.join(ROOT, '07_Literature_Analysis', 'social_capabilities_matrix.csv')))}
    LV = ['SAF1', 'SAF2', 'SPA1', 'SPA2', 'SPA3', 'SPA4', 'HUM1', 'HUM2', 'NOR1', 'NOR2', 'NOR3', 'NOR4', 'EXP1', 'EXP2', 'EXP3']
    KEYS = json.load(open(os.path.join(ROOT, '13_References', 'citation_keys.json'))); inv = {v: k for k, v in KEYS.items()}
    MM = {r['id']: r for r in csv.DictReader(open(os.path.join(ROOT, '07_Literature_Analysis', 'master_literature_matrix.csv')))}
    EVM = {r['id']: r for r in csv.DictReader(open(os.path.join(ROOT, '07_Literature_Analysis', 'evidence_maturity_matrix.csv')))}
    rows = []
    for nid, p in CORPUS12.items():
        ck = inv[nid]; e = EVM[nid]; cp = CAPM[nid]
        s = {'A_social_representation': MM[nid]['final_A_social_representation'], 'Capability leaves Yes': ' '.join(l for l in LV if cp['final_' + l] == 'Yes'),
             'Capability leaves Partial': ' '.join(l for l in LV if cp['final_' + l] == 'Partial'), 'EV1_offline': e['final_EV1_offline'], 'EV2_closed_loop_sim': e['final_EV2_closed_loop_sim'],
             'EV3_physical_robot': e['final_EV3_physical_robot'], 'EV5_human_evaluation': e['final_EV5_human_evaluation'], 'EV6_open_world_deployment': e['final_EV6_open_world_deployment']}
        ev5 = 'co-present' if s['EV5_human_evaluation'].startswith('robot') else 'none'
        rows.append(dict(key=ck, corpus_note=nid, in_frozen_corpus='Yes', title=MM[nid]['title'], year=MM[nid]['year'], venue=MM[nid].get('venue', ''), paradigm=PCODE[p],
                         survey_count='', selection='frozen-corpus pre-FM work (retained)', coding_source='full text (frozen Stage-3 coding)', source_url=MM[nid].get('url', ''),
                         A=s['A_social_representation'].replace(';', ''), cap_yes=s['Capability leaves Yes'], cap_partial=s['Capability leaves Partial'],
                         EV1_offline_recorded=s['EV1_offline'], EV2_closed_loop_sim=s['EV2_closed_loop_sim'], EV3_physical_robot=s['EV3_physical_robot'],
                         EV4_people_in_trials='not coded in Stage 3', EV5_human_evaluation=ev5, EV6_open_world=s['EV6_open_world_deployment'], statistical_testing='not coded in Stage 3',
                         evidence_note='frozen coding; human evaluation type not differentiated in Stage 3' if ev5 != 'none' else 'frozen coding'))
    for k, (p, n, why) in sorted(sel.items(), key=lambda kv: (int(kv[1][0][1:]), -kv[1][1], kv[0])):
        a, y, pa, e1, e2, e3, e4, e5, e6, st, src, url, ven, note = C[k]
        rows.append(dict(key=k, corpus_note='', in_frozen_corpus='No', title=TITLES[k]['title'], year=TITLES[k]['year'], venue=ven, paradigm=PCODE[p], survey_count=n,
                         selection=why, coding_source=src, source_url=url, A=a, cap_yes=y, cap_partial=pa, EV1_offline_recorded=e1, EV2_closed_loop_sim=e2, EV3_physical_robot=e3,
                         EV4_people_in_trials=e4, EV5_human_evaluation=e5, EV6_open_world=e6, statistical_testing=st, evidence_note=note))
    # bibliographic fields from verified records only (13_References/prefm_verified.json; existing bibliography keys otherwise)
    vp = os.path.join(ROOT, '13_References', 'prefm_verified.json'); V = json.load(open(vp)) if os.path.exists(vp) else {}
    EX = V.get('_existing_keys', {})
    for r in rows:
        if r['in_frozen_corpus'] == 'Yes': r['bib_key'] = r['key']; r['metadata'] = 'frozen corpus note (Stage 2 verified)'; continue
        v = V.get(r['key'], {})
        if r['key'] in EX: r['bib_key'] = EX[r['key']]; r['metadata'] = 'existing verified background entry'
        elif v.get('status') == 'VERIFIED':
            r['bib_key'] = r['key']; r['metadata'] = v['source']; r['source_url'] = 'https://doi.org/' + v['fields']['doi']
            r['venue'] = (v['fields'].get('journal') or v['fields'].get('booktitle', '')).replace('\\&', '&'); r['year'] = v['fields']['year']
        else: r['bib_key'] = ''; r['metadata'] = 'NOT VERIFIED'
    rows.sort(key=lambda r: (int(r['paradigm'].split()[0][1:]), r['in_frozen_corpus'] != 'Yes', int(r['year'])))
    out = os.path.join(ROOT, '07_Literature_Analysis', 'prefm_comparison_set.csv')
    w = csv.DictWriter(open(out, 'w', newline=''), fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print(len(rows), 'works;', collections.Counter(r['paradigm'].split()[0] for r in rows), collections.Counter(r['coding_source'][:9] for r in rows))
    excluded = {k: v[2] for k, v in CAND.items() if not v[1]}
    json.dump({'selected_new': {k: v for k, v in sel.items()}, 'ineligible': excluded}, open(os.path.join(HERE, 'prefm_selection_log.json'), 'w'), indent=1)
if __name__ == '__main__': main()

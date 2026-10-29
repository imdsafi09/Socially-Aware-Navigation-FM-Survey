---
id: 2023_Wang_NaviSTAR
source_pdfs: [04_Direct_VLM_SocialNav/B_Peer_Reviewed_Boundary/NaviSTAR_Socially_Aware_Robot_Navigation_with_Hybrid_Spatio-Temporal_Graph_Transformer_and_Preference_Learning.pdf]
duplicate_copies: []
related_versions: []
title: 'NaviSTAR: Socially Aware Robot Navigation with Hybrid Spatio-Temporal Graph Transformer and Preference Learning'
authors: &id001 [Weizheng Wang, Ruiqi Wang, Le Mao, Byung-Cheol Min]
year: 2023
venue: 2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
volume: NA
issue: NA
pages: 11348-11355
doi: 10.1109/IROS55552.2023.10341395
url: https://doi.org/10.1109/IROS55552.2023.10341395
pub_status: conference
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1109/IROS55552.2023.10341395); arXiv abs page (2304.05979v2). PDF-derived basis (Stage 1): IEEE IROS 2023 proceedings header with DOI (p.1).'
category: S2
folder: 04_Direct_VLM_SocialNav/B_Peer_Reviewed_Boundary
folder_category_match: 'No'
category_rationale: Learning-based (DRL + spatio-temporal graph Transformer + human preference learning) crowd navigation; no VLM/LLM/foundation model is used, so it is not direct FM social navigation. Folder placement as 'boundary' presumably due to Transformer/preference learning; reclassified S2.
paper_type: method
fm_used: 'No'
fm_class: [None]
fm_models: []
fm_size: NA
method_family: [DRL (SAC off-policy), GNN (Chebyshev GCN), 'Transformer (spatio-temporal, multi-modal cross-attention)', 'preference learning (human feedback reward model, FAPL)']
roles: []
roles_evidence: {}
integration: NA
integration_rationale: No foundation model.
evidence: E4
evidence_rationale: Simulation (500 tests) plus real-robot tests with 8 participants (IRB-reviewed), each algorithm tested 5 times, Likert comfort/naturalness questionnaire; no statistical tests (p.7-8).
inputs: ['human trajectories (positions, velocities, radius) over time', robot state, goal]
outputs: ['velocity/action (vx, vy)', value]
human_repr: ['disc/agent state (position, velocity, radius)', spatio-temporal graph node, learned embedding (attention maps)]
capabilities: {C1: 'Yes', C2: Partial, C3: Partial, C4: Partial, C5: 'Yes', C6: Partial, C7: Partial, C8: 'No', C9: 'No', C10: 'No', C11: Partial, C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: 'Yes', C18: 'No', C19: 'No', C20: 'Yes', C21: 'Yes', C22: 'No', C23: 'No', C24: 'No', C25: 'No'}
exp:
  datasets: []
  simulators: ['2D gym-based crowd simulator (CrowdNav-style), ORCA humans, invisible robot, 20 m x 22 m open space, FOV 90/180/360']
  robots: [robot with Kinect V2 (86 deg FOV); platform not named]
  environment: simulated open space; real-world test setting not detailed
  indoor_outdoor: Not reported
  sensors: [Kinect V2 RGB-D]
  humans: ORCA simulated humans (10/15/20); 8 real participants
  n_scenes: open space (sim)
  n_trajectories: 500 sim test cases per configuration; 5 real tests per algorithm
  n_participants: 8 (1 female, 7 male); >10 human supervisors gave 5,000 preference labels for training
  split: NA
  baselines: [ORCA, CADRL, SARL, RGL, SRNN, STAR+PPO (ablation), NaviSRNN (ablation)]
  ablation: 'Yes'
  real_robot_trials: 'Yes'
  human_study: 'Yes'
  statistical_testing: 'No'
  scenarios: [crowd crossing (circle crossing), limited FOV]
metrics: [NAV | Success rate | % | successful cases out of 500 tests | p.6, 'SOCIAL | Social score F_SC | (-inf, 100] | 100[v F_time + (1-v) F_scc + v'' FF]; v=0.35, v''=0.25; F_scc uses uncomfortable distance 0.45 m | p.6', 'NAV | F_time | [0,1] | normalized navigation time cost | p.6', 'SOCIAL | F_scc social compliance cost | [0,1] | sigmoid-normalized weighted intrusion into 0.45 m uncomfortable distance | p.6', 'HUMAN | Comfort index + naturalness index | [20,100] | Likert (1-5) sums x10 | p.8']
deployment: {fm_model: NA, model_size: NA, api_cloud_local: NA, onboard_offboard: Not reported, gpu: Not reported, cpu: Not reported, latency: Not reported, query_frequency: NA, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: NA, caching: NA, event_triggered: NA, distillation: 'No', quantization: 'No', fallback_planner: 'No', safety_shield: 'No', emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: NA, real_time_claim_supported: NA}
repro: {code: Yes (stated), code_url: 'https://sites.google.com/view/san-navistar', dataset: NA, dataset_url: NA, checkpoints: Not reported, prompts_published: NA, hardware_specified: Partial (Kinect V2), hyperparameters: 'Partial (lr 4e-5, 1e4 episodes)', protocol_described: Partial (details on website), project_page: 'https://sites.google.com/view/san-navistar', concerns: Invisible-robot assumption in simulation; user study details deferred to website.}
limitations_flags: [sim-to-real, limited-scenarios]
web_verification_required: [User-study details on project website.]
cited_missing: [FAPL feedback-efficient active preference learning (IROS 2022), RGL relational graph learning (IROS 2020), DS-RNN decentralized structural RNN (ICRA 2021), Liu 2022 interaction graphs + trajectory prediction (ICRA 2023), STAR trajectory transformer (ECCV 2020), B-Pref, Trautman IJRR 2015, Garrell & Sanfeliu 2012 accompany groups]
learning: {type: DRL + Transformer/GNN + preference learning (hybrid), state_repr: 'Joint state of robot and observable humans (position, velocity, radius) over T timesteps as spatio-temporal graph', human_repr: Agent nodes with observable state; Gaussian-kernel adjacency, reward_design: Learned reward network r_alpha from human preferences over trajectory segments (FAPL), social_reward: 'Implicit via human preference labels (5,000 from >10 supervisors)', prediction_model: Implicit (temporal transformer); no explicit trajectory forecast, group_modeling: 'No', training_env: 2D gym crowd simulator with ORCA humans, sim_dependence: High (trained in 2D sim; invisible robot), interpretability: 'Attention-map visualization (Fig.4, Fig.7)', generalization: FOV 90/180/360 and 10/15/20 humans in sim, real_world_validation: 'Yes, 8 participants, 5 runs per algorithm', social_metrics: 'Social score (with 0.45 m uncomfortable distance), comfort/naturalness index'}
coding: {latency_reported: 'No', safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: 'Yes', new_dataset_released: NA, real_robot: Systematic, human_subject_study: 'Yes'}
pdf_metadata_stage1:
  year: 2023
  authors: *id001
  venue: 2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Detroit
  volume: Not reported
  issue: Not reported
  pages: 11348-11355
  doi: 10.1109/IROS55552.2023.10341395
  url: https://sites.google.com/view/san-navistar
  pub_status: conference
  peer_reviewed: 'Yes'
  peer_review_basis: IEEE IROS 2023 proceedings header with DOI (p.1).
project_url: https://sites.google.com/view/san-navistar
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: 2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
  verified_doi: 10.1109/IROS55552.2023.10341395
  verified_url: https://doi.org/10.1109/IROS55552.2023.10341395
  verified_pages: 11348-11355
  arxiv: 2304.05979v2
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1109/IROS55552.2023.10341395)', arXiv abs page (2304.05979v2)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A4, A6]
  C_capabilities: {SAF1: 'Yes', SAF2: Partial, SPA1: Partial, SPA2: 'No', SPA3: 'No', SPA4: 'Yes', HUM1: Partial, HUM2: Partial, NOR1: Partial, NOR2: 'No', NOR3: 'No', NOR4: 'No', EXP1: 'Yes', EXP2: 'No', EXP3: 'Yes'}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: systematic, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: robot-behaviour evaluation (type not differentiated), EV6_open_world_deployment: 'No'}
physical_source_folder: "04_Direct_VLM_SocialNav/B_Peer_Reviewed_Boundary"
analytical_category: "S2"
coding:
  latency_reported: "No"
  safety_mechanism: "NA"
  uncertainty_treatment: "NA"
  hallucination_treatment: "NA"
  code_released: "Yes"
  new_dataset_released: "NA"
  real_robot: "Systematic"
  human_subject_study: "Yes"
---

# NaviSTAR (Wang, Wang, Mao, Min — IROS 2023)

Page convention: PDF index (p.N); printed pp.11348–11355.

## A. Bibliographic
IROS 2023, DOI 10.1109/IROS55552.2023.10341395; Purdue SMART Lab + BUCT. Code/videos https://sites.google.com/view/san-navistar. Peer-reviewed.

## B. Position — **S2 (reclassified from 04B boundary folder)**
No VLM/LLM/foundation model is used. It is a learning-based social navigation method (spatio-temporal graph Transformer encoder + SAC + human preference-learned reward). Relevant to our historical narrative as the "Transformer + human feedback" stage immediately preceding FM methods; it is NOT direct FM social navigation.

## C. Research problem
- **Problem:** encode complex HHI/HRI spatio-temporal dependencies; handcrafted rewards cannot quantify social compliance (p.1).
- **Contributions:** hybrid spatio-temporal graph Transformer (spatial transformer with Chebyshev GCN + multi-head attention; temporal transformer; multi-modal cross-attention fusion); off-policy RL + preference learning; social score function; sim + real user study (p.2).

## D. Technical method
POMDP with observable human states [p_x, p_y, v_x, v_y, radius] (p.2). Spatial transformer (GCN Eq.3 + MHA Eq.4–7, gated fusion Eq.8–9), temporal transformer (Eq.10–11), multi-modal transformer (Eq.12–16), decoder → V and π. Reward network trained from preference labels over trajectory segments (Eq.17–19), SAC policy optimisation (FAPL procedure). Sim: 20 m × 22 m, humans on 8 m circle, ORCA, invisible robot, holonomic action [v_x, v_y], lr 4e-5, 1e4 episodes (p.5–6).

## E. Human/social representation — agent discs with velocities as ST-graph nodes; learned attention; social discomfort radius 0.45 m in metric.

## F–H. FM roles: none; integration NA.

## G. Social capabilities
C1 Yes (success/failure incl. collisions in F_SC) · C5 Yes (ST-graph interaction modelling) · C17 Yes (10–20 humans) · C20, C21 Yes (naturalness and comfort indices in user study) · C2/C3 Partial (0.45 m uncomfortable distance in F_scc) · C4 Partial (comfort index) · C6/C7 Partial (implicit intents via attention) · C11 Partial (preference-learned norms) · others No.

## I. Evidence — E4 (small user study; no statistics).

## J. Experimental evidence — sim 500 random cases per setting; FOV 90/180/360; 10/15/20 humans; real-world 8 participants, YOLO+DeepSort velocity + MonStereo distance, Kinect V2; 4 algorithms tested 5 times each (p.6–8). Preference data: >10 supervisors, 5,000 preferences (p.8). IRB reviewed (footnote p.7).

## K. Metrics — success rate, social score F_SC, comfort+naturalness index.

## L. Quantitative results
Table I social score (p.7; FOV 90/180/360 | humans 10/15/20): ORCA 21.1/23.2/27.4 | 29.2/25.7/22.6; CADRL 62.7/65.4/69.6 | 77.1/73.2/70.1; SARL 31.3/34.1/39.7 | 42.2/39.1/36.7; RGL 76.5/81.3/84.9 | 90.3/88.3/86.6; SRNN 80.4/84.7/88.6 | 87.1/84.8/81.2; STAR+PPO 85.1/88.9/91.3 | 99.2/95.4/94.3; NaviSRNN 89.3/91.6/94.5 | 95.7/93.4/91.2; NaviSTAR 91.7/93.1/94.2 | 98.9/98.5/95.8. (NaviSTAR is not best at FOV-360 [NaviSRNN 94.5] or 10 humans [STAR+PPO 99.2].) Success rates in Fig.5 only (bar chart).
User study (p.8): average score NaviSTAR 93, NaviSRNN 89, STAR+PPO 86, SRNN 80 (range 20–100).

## M. Deployment — not reported.

## N. Limitations
1. Stated: none explicit.
2. Future work: not stated.
3. Observable: invisible-robot simulation assumption (humans don't react); 8 participants; no statistics; real-world setting details on website only; social score is a custom composite.

## O. Reproducibility — code stated; partial hyperparameters.

## P. Learning-based special analysis — see `learning:` block. Transition marker: replaces handcrafted social reward with *human-preference-learned* reward — an implicit, data-driven social objective (precursor to FM-derived rewards).

## Q. Cited works possibly missing — FAPL (IROS 2022); RGL; DS-RNN; Liu 2022 interaction graphs; STAR (ECCV 2020).

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue 2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS); DOI 10.1109/IROS55552.2023.10341395; pages 11348-11355; URL https://doi.org/10.1109/IROS55552.2023.10341395.
- Sources: Crossref (exact title match, DOI 10.1109/IROS55552.2023.10341395); arXiv abs page (2304.05979v2).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - venue: PDF-derived '2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Detroit' -> externally verified '2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)'
- Changed field - volume: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - issue: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - url: PDF-derived 'https://sites.google.com/view/san-navistar' -> externally verified 'https://doi.org/10.1109/IROS55552.2023.10341395'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

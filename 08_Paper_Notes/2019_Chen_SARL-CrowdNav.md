---
id: 2019_Chen_SARL-CrowdNav
source_pdfs: [02_Learning_Based_Social_Navigation/Crowd-Robot_Interaction_Crowd-Aware_Robot_Navigation_With_Attention-Based_Deep_Reinforcement_Learning.pdf]
duplicate_copies: []
related_versions: []
title: 'Crowd-Robot Interaction: Crowd-aware Robot Navigation with Attention-based Deep Reinforcement Learning'
authors: &id001 [Changan Chen, Yuejiang Liu, Sven Kreiss, Alexandre Alahi]
year: 2019
venue: 2019 International Conference on Robotics and Automation (ICRA)
volume: NA
issue: NA
pages: 6015-6022
doi: 10.1109/ICRA.2019.8794134
url: https://doi.org/10.1109/ICRA.2019.8794134
pub_status: conference
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1109/ICRA.2019.8794134); arXiv abs page (1809.08835v2). PDF-derived basis (Stage 1): ICRA 2019 header and IEEE copyright/ISBN on p.1 (IEEE Xplore copy).'
category: S2
folder: 02_Learning_Based_Social_Navigation
folder_category_match: 'Yes'
category_rationale: Attention-based DRL (SARL/LM-SARL) jointly modelling human-robot and human-human interactions; introduced the CrowdNav simulator widely used as a baseline.
paper_type: method; simulator
fm_used: 'No'
fm_class: [None]
fm_models: []
fm_size: NA
method_family: [DRL (deep V-learning), imitation warm start (ORCA demos), self-attention pooling, local occupancy maps for human-human interaction]
roles: []
roles_evidence: {}
integration: NA
integration_rationale: No foundation model.
evidence: E2
evidence_rationale: 500 random circle-crossing test cases in simulation (invisible and visible settings; Tables I-II); real-world Segway demonstration only via video.
inputs: ['robot state (distance to goal, v_pref, velocity, radius)', 'each human''s position, velocity, radius, distance', local 4x4 map of neighbours per human]
outputs: ['discrete action: 5 speeds x 16 headings (holonomic)']
human_repr: [agent states + pairwise interaction embeddings + human-centric local occupancy/velocity maps; attention scores]
capabilities: {C1: 'Yes', C2: 'Yes', C3: Partial, C4: 'No', C5: Partial, C6: Partial, C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: 'Yes', C18: 'No', C19: 'No', C20: 'No', C21: Partial, C22: 'No', C23: 'No', C24: 'No', C25: 'No'}
exp:
  datasets: [3k ORCA demonstration episodes (imitation warm start)]
  simulators: [CrowdNav (Python; humans controlled by ORCA with sampled parameters)]
  robots: [Segway Loomo (real demo)]
  environment: circle-crossing scenario, radius 4 m
  indoor_outdoor: NA
  sensors: [ground-truth agent states (sim)]
  humans: simulated ORCA agents (invisible / visible robot settings)
  n_scenes: circle crossing
  n_trajectories: 500 test cases per setting
  n_participants: NA
  split: random training vs 500 test cases
  baselines: [ORCA, CADRL, LSTM-RL]
  ablation: Yes (SARL vs LM-SARL)
  real_robot_trials: Partial (video demo)
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [crowd crossing (circle)]
metrics: [NAV | Success | rate | reaching goal without collision | p.5, SAFETY | Collision | rate | robot colliding with humans | p.5, NAV | Time | s | navigation time to goal | p.5, OTHER | Reward | scalar | discounted cumulative reward | p.5, SOCIAL | Disc. (discomfort frequency) | fraction of duration ('%' in caption) | t_disc/T with separation < 0.2 m | p.5]
deployment: {fm_model: NA, model_size: 'MLPs (150,100), (100,50), (100,100), (150,100,100)', api_cloud_local: NA, onboard_offboard: Not reported, gpu: NA, cpu: i7-8700 (training ~10 h), latency: Not reported, query_frequency: NA, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: NA, caching: NA, event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: 'No', safety_shield: 'No', emergency_behavior: Not reported, uncertainty: NA, hallucination_mitigation: NA, real_time_claim_supported: NA}
repro: {code: 'Yes', code_url: 'https://github.com/vita-epfl/CrowdNav', dataset: NA, dataset_url: NA, checkpoints: Not reported, prompts_published: NA, hardware_specified: Partial, hyperparameters: 'Yes', protocol_described: 'Yes', project_page: NA, concerns: Simulated humans are ORCA agents; single circle-crossing scenario; holonomic robot.}
limitations_flags: [sim-to-real, no-human-study, limited-scenarios]
web_verification_required: []
cited_missing: [LSTM-RL (Everett IROS 2018), Social LSTM, Social GAN, Social Attention (Vemula 2018), SoPhie, IGP (Trautman)]
learning: {type: DRL (deep V-learning) with IL warm start, state_repr: robot-centric joint state; per-human pairwise embeddings; attention-weighted crowd vector, human_repr: position/velocity/radius plus local maps of neighbours (human-human interaction), reward_design: +1 goal; -0.25 collision; -0.1 + d/2 when separation d < 0.2 m (removed in invisible setting), social_reward: Partial (discomfort-distance penalty only), prediction_model: Environment-queried next state during training; trajectory predictor suggested for deployment, group_modeling: No (implicit human-human interaction via local maps), training_env: CrowdNav circle crossing with ORCA humans, sim_dependence: High, interpretability: 'Medium (attention scores visualizable, Fig.6)', generalization: Arbitrary number of humans via attention pooling, real_world_validation: Video demo only, social_metrics: Discomfort frequency}
coding: {latency_reported: 'No', safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: 'Yes', new_dataset_released: NA, real_robot: Demo, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2019
  authors: *id001
  venue: 2019 International Conference on Robotics and Automation (ICRA), Montreal
  volume: NA
  issue: NA
  pages: 6015-6022
  doi: Not reported
  url: https://github.com/vita-epfl/CrowdNav
  pub_status: conference
  peer_reviewed: 'Yes'
  peer_review_basis: ICRA 2019 header and IEEE copyright/ISBN on p.1 (IEEE Xplore copy).
project_url: https://github.com/vita-epfl/CrowdNav
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: 2019 International Conference on Robotics and Automation (ICRA)
  verified_doi: 10.1109/ICRA.2019.8794134
  verified_url: https://doi.org/10.1109/ICRA.2019.8794134
  verified_pages: 6015-6022
  arxiv: 1809.08835v2
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1109/ICRA.2019.8794134)', arXiv abs page (1809.08835v2)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A4]
  C_capabilities: {SAF1: 'Yes', SAF2: 'Yes', SPA1: Partial, SPA2: 'No', SPA3: 'No', SPA4: 'Yes', HUM1: Partial, HUM2: 'No', NOR1: 'No', NOR2: 'No', NOR3: 'No', NOR4: 'No', EXP1: Partial, EXP2: 'No', EXP3: 'No'}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: demo, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "02_Learning_Based_Social_Navigation"
analytical_category: "S2"
coding:
  latency_reported: "No"
  safety_mechanism: "NA"
  uncertainty_treatment: "NA"
  hallucination_treatment: "NA"
  code_released: "Yes"
  new_dataset_released: "NA"
  real_robot: "Demo"
  human_subject_study: "No"
---

# Crowd-Robot Interaction / SARL (Chen, Liu, Kreiss, Alahi — ICRA 2019)

Page convention: PDF index (p.N).

## A. Bibliographic — ICRA 2019, Montreal, pp.6015–6022 (IEEE Xplore copy). EPFL VITA. Code: CrowdNav.

## B. Position — S2: the CrowdNav/SARL baseline that most later DRL and several VLM social-navigation papers compare against or build on.

## C. Research problem — DRL methods aggregate pairwise interactions crudely (maximin, LSTM) and ignore human-human interactions (p.1). Contributions: self-attention pooling over human-robot interactions; local maps for human-human interactions; CrowdNav simulator; real Segway demo (p.1–2).

## D. Method — Eq.1 value-based planning; reward Eq.2; local map tensor M_i (Eq.4); embeddings e_i, h_i (Eq.5–6); attention α_i from e_i and mean embedding (Eq.7–8); crowd vector c = Σ softmax(α_i) h_i (Eq.9); value v = f_v(s, c) (Eq.10); 80 discrete actions; IL on 3k ORCA episodes then RL with ε-greedy (0.5→0.1 over 5k episodes) (p.2–4).

## L. Quantitative results
- Table I (invisible; success / collision / time s / reward): ORCA 0.43 / 0.57 / 10.86 / 0.054; CADRL 0.78 / 0.22 / 10.80 / 0.222; LSTM-RL 0.95 / 0.03 / 11.82 / 0.279; SARL 1.00 / 0.00 / 10.55 / 0.338; LM-SARL 1.00 / 0.00 / 10.46 / 0.342.
- Table II (visible; success / collision / time / disc. / reward): ORCA 0.99 / 0.00* / 12.29 / 0.00* / 0.284; CADRL 0.94 / 0.03 / 10.82 / 0.10 / 0.291; LSTM-RL 0.98 / 0.02 / 11.29 / 0.05 / 0.299; SARL 0.99 / 0.01 / 10.58 / 0.02 / 0.332; LM-SARL 1.00 / 0.00 / 10.59 / 0.03 / 0.334 (*ORCA zero by design).
- Observations: in the visible setting LM-SARL's advantage over SARL is only in reward (0.334 vs 0.332); SARL has lower discomfort (0.02 vs 0.03) and time; "Disc." described as % but reported as fractions.

## N. Limitations
1. **Stated:** human-human interaction effects diluted in quantitative results (p.5).
2. **Observable:** ORCA-driven humans; single scenario family; holonomic robot; real-world unquantified; discomfort is the only social metric.
3. **Social relevance:** crowd-aware, but no norms, groups or human perception.

## P. Learning-based analysis — see `learning:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue 2019 International Conference on Robotics and Automation (ICRA); DOI 10.1109/ICRA.2019.8794134; pages 6015-6022; URL https://doi.org/10.1109/ICRA.2019.8794134.
- Sources: Crossref (exact title match, DOI 10.1109/ICRA.2019.8794134); arXiv abs page (1809.08835v2).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - venue: PDF-derived '2019 International Conference on Robotics and Automation (ICRA), Montreal' -> externally verified '2019 International Conference on Robotics and Automation (ICRA)'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified '10.1109/ICRA.2019.8794134'
- Changed field - url: PDF-derived 'https://github.com/vita-epfl/CrowdNav' -> externally verified 'https://doi.org/10.1109/ICRA.2019.8794134'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

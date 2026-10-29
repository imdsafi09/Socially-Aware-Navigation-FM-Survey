---
id: 2017_Chen_CADRL
source_pdfs: [02_Learning_Based_Social_Navigation/1609.07845.pdf]
duplicate_copies: []
related_versions: ['Published: IEEE ICRA 2017, Singapore (per corpus citations); corpus copy arXiv:1609.07845v2 (28 Sep 2016)']
title: Decentralized Non-communicating Multiagent Collision Avoidance with Deep Reinforcement Learning
authors: &id001 [Yu Fan Chen, Miao Liu, Michael Everett, Jonathan P. How]
year: 2017
venue: 2017 IEEE International Conference on Robotics and Automation (ICRA)
volume: NA
issue: NA
pages: 285-292
doi: 10.1109/ICRA.2017.7989037
url: https://doi.org/10.1109/ICRA.2017.7989037
pub_status: conference (corpus copy preprint)
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1109/ICRA.2017.7989037); arXiv abs page (1609.07845v2). PDF-derived basis (Stage 1): Corpus copy arXiv v2 without venue; corpus papers cite it as ICRA 2017, Singapore. WEB_VERIFICATION_REQUIRED.'
category: S2
folder: 02_Learning_Based_Social_Navigation
folder_category_match: 'Yes'
category_rationale: Deep RL value network for decentralized multiagent collision avoidance (CADRL), foundational to DRL crowd navigation; no foundation model.
paper_type: method
fm_used: 'No'
fm_class: [None]
fm_models: []
fm_size: NA
method_family: [DRL (deep V-learning), imitation initialization from ORCA, one-step lookahead]
roles: []
roles_evidence: {}
integration: NA
integration_rationale: No foundation model.
evidence: E2
evidence_rationale: 'Simulation-only evaluation: crossing scenarios and 100 random test cases per configuration (2-8 agents) vs ORCA (Table I, Figs.7-9).'
inputs: ['own state (position, velocity, radius, goal, preferred speed, heading)', 'other agents'' observable states (position, velocity, radius)']
outputs: [velocity vector (action)]
human_repr: ['agent as disc with position, velocity, radius; hidden intent unobserved; constant-velocity one-step propagation']
capabilities: {C1: 'Yes', C2: Partial, C3: 'No', C4: 'No', C5: Partial, C6: Partial, C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: Partial, C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: Partial, C18: 'No', C19: 'No', C20: Partial, C21: 'No', C22: 'No', C23: 'No', C24: 'No', C25: 'No'}
exp:
  datasets: ['500 ORCA trajectories (~20,000 state-value pairs) for initialization']
  simulators: [custom 2D multiagent simulation]
  robots: []
  environment: open square domains 4x4 to 7x7 m
  indoor_outdoor: NA
  sensors: [ground-truth agent states]
  humans: simulated agents with pedestrian-like parameters (v_pref 0.5-1.5 m/s, r 0.3-0.5 m), reciprocal policies
  n_scenes: crossing configurations + 4 random configurations
  n_trajectories: 100 random test cases per configuration
  n_participants: NA
  split: training on random cases; evaluation on held-out test cases
  baselines: [ORCA]
  ablation: Partial (with/without kinematic constraints)
  real_robot_trials: 'No'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [crossing, swapping, circle, non-cooperative agent, static obstacles]
metrics: ['NAV | Extra time to goal (t_e) | s | time to goal minus straight-line lower bound, averaged over agents (Eq.12) | p.6', SAFETY | Average minimum separation distance | m | minimum separation between agents | p.8, 'DEPLOY | Computation time per iteration | ms | 5.7 ms (2 agents), 62 ms (10 agents) on i7-5820K | p.5-6']
deployment: {fm_model: NA, model_size: '3 hidden layers (150,100,100)', api_cloud_local: NA, onboard_offboard: NA, gpu: NA, cpu: Intel i7-5820K, latency: 5.7 ms per iteration (2 agents); 62 ms (10 agents decentralized), query_frequency: NA, planner_frequency: NA, controller_frequency: NA, asynchronous: NA, caching: NA, event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: 'No', safety_shield: 'No', emergency_behavior: Not reported, uncertainty: Implicit in value function, hallucination_mitigation: NA, real_time_claim_supported: Yes (timing reported)}
repro: {code: Not reported, code_url: NA, dataset: NA, dataset_url: NA, checkpoints: NA, prompts_published: NA, hardware_specified: Yes (CPU), hyperparameters: 'Partial (network size, epsilon schedule, penalties)', protocol_described: 'Yes', project_page: NA, concerns: Reciprocity assumption in training; no human data.}
limitations_flags: [sim-to-real, no-human-study, limited-scenarios]
web_verification_required: [ICRA 2017 publication details.]
cited_missing: [Kuderer feature-based prediction (RSS 2012), Trautman ICRA 2013 cooperation case, BRVO, Hybrid RVO, Ferrer social-aware urban navigation (ECMR 2013)]
learning: {type: 'DRL (deep V-learning, two-agent value network)', state_repr: 'agent-centric 15-d joint state (distance to goal, velocities, relative position, radii, heading)', human_repr: other agents as discs with observable position/velocity/radius, reward_design: +1 goal; -0.25 collision; -0.1 - d_min/2 if d_min < 0.2 m; cooperation penalty 0.1 when own extra time small and other's large, social_reward: Partial (cooperation penalty discourages aggressive behaviour; no explicit social norms), prediction_model: Filtered constant-velocity one-step propagation, group_modeling: 'No', training_env: '2D simulation, self-play with reciprocity', sim_dependence: High, interpretability: Low (value network) but one-step lookahead visualizable, generalization: Two-agent network extended to n agents via min over neighbors (Eq.11), real_world_validation: 'No', social_metrics: Min separation only}
coding: {latency_reported: 'Yes', safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: 'No', new_dataset_released: NA, real_robot: 'No', human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2017
  authors: *id001
  venue: IEEE ICRA 2017 (per citations); corpus copy arXiv v2
  volume: NA
  issue: NA
  pages: 8 (PDF)
  doi: Not reported
  url: Not reported
  pub_status: conference (corpus copy preprint)
  peer_reviewed: 'Yes'
  peer_review_basis: Corpus copy arXiv v2 without venue; corpus papers cite it as ICRA 2017, Singapore. WEB_VERIFICATION_REQUIRED.
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: 2017 IEEE International Conference on Robotics and Automation (ICRA)
  verified_doi: 10.1109/ICRA.2017.7989037
  verified_url: https://doi.org/10.1109/ICRA.2017.7989037
  verified_pages: 285-292
  arxiv: 1609.07845v2
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1109/ICRA.2017.7989037)', arXiv abs page (1609.07845v2)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1]
  C_capabilities: {SAF1: 'Yes', SAF2: Partial, SPA1: 'No', SPA2: 'No', SPA3: Partial, SPA4: Partial, HUM1: Partial, HUM2: 'No', NOR1: 'No', NOR2: 'No', NOR3: 'No', NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: Partial}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: none, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "02_Learning_Based_Social_Navigation"
analytical_category: "S2"
coding:
  latency_reported: "Yes"
  safety_mechanism: "NA"
  uncertainty_treatment: "NA"
  hallucination_treatment: "NA"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "No"
  human_subject_study: "No"
---

# CADRL (Chen, Liu, Everett, How — ICRA 2017)

Page convention: PDF index (p.N).

## A. Bibliographic — corpus copy arXiv:1609.07845v2 (28 Sep 2016); MIT; cited as ICRA 2017. Funded by Ford.

## B. Position — S2: origin of the CADRL / SA-CADRL / LSTM-RL / CrowdNav DRL line used as baselines throughout the corpus.

## C. Research problem — anticipating interactions is computationally prohibitive for non-communicating agents; reaction-based methods (RVO/ORCA) are myopic and unnatural (p.1–2). Contributions: two-agent DRL collision avoidance; generalization to n agents; kinematic constraints; simulation comparison vs ORCA (p.2).

## D. Method — value network V(s_jn) estimating time to goal (Eq.6); one-step lookahead over 25 precomputed + 10 sampled actions (Eq.7, Alg.1); initialization by regression on ORCA trajectories, then RL with ε-greedy self-play and experience replay (Alg.2); rotational constraints (Eq.9–10); multiagent extension via min over neighbours (Eq.11) (p.3–5).

## L. Quantitative results (Table I, p.8, visually verified; t_e avg / 75th / 90th percentile in s; min separation m)
- 2 agents: ORCA 0.46 / 0.45 / 0.73, CADRL 0.27 / 0.33 / 0.56, CADRL w/ cstr 0.31 / 0.42 / 0.60; separation 0.122 / 0.199 / 0.198.
- 4 agents: 0.69 / 0.85 / 1.85; 0.31 / 0.40 / 0.76; 0.39 / 0.53 / 0.86; separation 0.120 / 0.192 / 0.191.
- 6 agents: 0.65 / 0.83 / 1.50; 0.44 / 0.56 / 0.87; 0.48 / 0.63 / 1.02; separation 0.118 / 0.117 / 0.180.
- 8 agents: 0.96 / 1.33 / 1.84; 0.54 / 0.70 / 1.01; 0.59 / 0.77 / 1.09; separation 0.110 / 0.171 / 0.170.
- Timing: 5.7 ms/iteration (2 agents); 62 ms (10 agents decentralized); training < 3 h (p.5–6).
- **Data-quality notes:** 6-agent CADRL min separation 0.117 m breaks the pattern (others 0.17–0.20 m) and is below the 0.2 m reward margin — possibly a typo; column header "OCRA" (sic); ORCA 2-agent 75th percentile (0.45) below its mean (0.46) (possible but noteworthy).

## N. Limitations
1. **Stated (p.5, p.7):** two-agent value network is only an approximation of a true multiagent value function; can get stuck in dense obstacle fields (collision avoidance, not path planning).
2. **Observable:** reciprocity assumption; no real robot; no human-perceived social criteria; humans modelled as reciprocal agents.
3. **Social relevance:** collision avoidance ≠ social compliance; cooperation penalty is the only social-like term.

## P. Learning-based analysis — see `learning:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue 2017 IEEE International Conference on Robotics and Automation (ICRA); DOI 10.1109/ICRA.2017.7989037; pages 285-292; URL https://doi.org/10.1109/ICRA.2017.7989037.
- Sources: Crossref (exact title match, DOI 10.1109/ICRA.2017.7989037); arXiv abs page (1609.07845v2).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - venue: PDF-derived 'IEEE ICRA 2017 (per citations); corpus copy arXiv v2' -> externally verified '2017 IEEE International Conference on Robotics and Automation (ICRA)'
- Changed field - pages: PDF-derived '8 (PDF)' -> externally verified '285-292'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified '10.1109/ICRA.2017.7989037'
- Changed field - url: PDF-derived 'Not reported' -> externally verified 'https://doi.org/10.1109/ICRA.2017.7989037'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

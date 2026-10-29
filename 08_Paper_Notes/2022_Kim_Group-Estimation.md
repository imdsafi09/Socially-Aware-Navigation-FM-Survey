---
id: 2022_Kim_Group-Estimation
source_pdfs: [02_Learning_Based_Social_Navigation/Group_Estimation_for_Social_Robot_Navigation_in_Crowded_Environments.pdf]
duplicate_copies: []
related_versions: []
title: Group Estimation for Social Robot Navigation in Crowded Environments
authors: &id001 [Mincheul Kim, Youngsun Kwon, Sung-Eui Yoon]
year: 2022
venue: 2022 22nd International Conference on Control, Automation and Systems (ICCAS)
volume: NA
issue: NA
pages: 1421-1425
doi: 10.23919/ICCAS55662.2022.10003761
url: https://doi.org/10.23919/ICCAS55662.2022.10003761
pub_status: conference
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.23919/ICCAS55662.2022.10003761). PDF-derived basis (Stage 1): ICCAS 2022 proceedings header and ICROS ISBN/copyright on p.1 (IEEE Xplore copy).'
category: S2
folder: 02_Learning_Based_Social_Navigation
folder_category_match: 'Yes'
category_rationale: DRL (PPO) navigation with HDBSCAN-based group clustering, asymmetric-Gaussian individual spaces, convex-hull group spaces and a group-aware reward; no foundation model.
paper_type: method
fm_used: 'No'
fm_class: [None]
fm_models: []
fm_size: NA
method_family: [DRL (PPO), unsupervised clustering (HDBSCAN), proxemic personal-space model, group-space convex hull, reward shaping]
roles: []
roles_evidence: {}
integration: NA
integration_rationale: No foundation model.
evidence: E2
evidence_rationale: Simulation-only evaluation (Stage ROS with extended-social-force groups), 100 unseen episodes per scenario (Table 1).
inputs: [last three lidar scans, local goal, robot velocity, observed human positions and velocities (for grouping)]
outputs: ['linear velocity v in [0,1]', 'angular velocity w in [-1,1]']
human_repr: [individual space as 2-D asymmetric Gaussian (front/side/rear variances from speed), group space as convex hull of member individual spaces, groups via HDBSCAN on position and velocity]
capabilities: {C1: Partial, C2: 'No', C3: 'Yes', C4: 'No', C5: Partial, C6: 'No', C7: 'No', C8: 'No', C9: 'Yes', C10: 'No', C11: Partial, C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: 'Yes', C18: 'No', C19: 'No', C20: 'No', C21: Partial, C22: 'No', C23: 'No', C24: 'No', C25: 'No'}
exp:
  datasets: []
  simulators: [Stage ROS (2-D) with extended social force model groups]
  robots: []
  environment: circle scenario (13 humans); cross/plus-shaped corridor scenario (22 humans)
  indoor_outdoor: NA
  sensors: [simulated 2-D lidar]
  humans: simulated groups following extended social force (Moussaid 2010)
  n_scenes: 2 scenarios
  n_trajectories: 100 unseen test episodes per scenario; 10,000 training episodes
  n_participants: NA
  split: training vs unseen test episodes
  baselines: ['DRL-Long (Fan et al., IJRR 2020)']
  ablation: 'No'
  real_robot_trials: 'No'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [crowd, group crossing, corridor]
metrics: [NAV | Success rate | fraction | over 100 test episodes | p.4, NAV | Average length | m (implied) | trajectory length in successful episodes | p.4, 'SOCIAL | Individual discomfort | count | number of robot intrusions into personal spaces (Hall), success episodes only | p.3-4']
deployment: {fm_model: NA, model_size: Not reported, api_cloud_local: NA, onboard_offboard: NA, gpu: Not reported, cpu: Not reported, latency: Not reported, query_frequency: NA, planner_frequency: NA, controller_frequency: NA, asynchronous: NA, caching: NA, event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: NA, safety_shield: NA, emergency_behavior: NA, uncertainty: NA, hallucination_mitigation: NA, real_time_claim_supported: NA}
repro: {code: Not reported, code_url: NA, dataset: NA, dataset_url: NA, checkpoints: NA, prompts_published: NA, hardware_specified: 'No', hyperparameters: 'Partial (lambda1 0.1, d_safe 2.0, PPO, Adam)', protocol_described: Partial, project_page: NA, concerns: 5-page paper; source of human velocities for clustering not specified; metrics on success-only subsets.}
limitations_flags: [sim-to-real, no-human-study, weak-baselines, limited-scenarios]
web_verification_required: []
cited_missing: ['Wang, Mavrogiannis, Steinfeld group-based motion prediction (CoRL 2022)', Moussaid 2010 walking behaviour of pedestrian groups, DS-RNN (Liu ICRA 2021), Chen RA-L 2020 GCN with gaze attention, Kirby 2010 social robot navigation thesis, Group LSTM]
learning: {type: DRL (PPO), state_repr: 3 stacked lidar scans + local goal + robot velocity (DRL-Long architecture), human_repr: estimated group spaces from clustering observed human states, reward_design: 'R = R_g + R_c + R_w + R_grp; R_grp = lambda1 * sum_j min(0, d_grp_j - d_safe), lambda1 = 0.1, d_safe = 2.0 m', social_reward: Yes (group-space violation penalty), prediction_model: 'No', group_modeling: Yes (HDBSCAN on position + velocity; convex hull of asymmetric Gaussian spaces), training_env: 'Stage ROS crowd simulation, 10,000 episodes per scenario', sim_dependence: High, interpretability: Medium (explicit group spaces), generalization: Trained and tested per scenario, real_world_validation: 'No', social_metrics: Individual discomfort (personal-space intrusions)}
coding: {latency_reported: 'No', safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: 'No', new_dataset_released: NA, real_robot: 'No', human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2022
  authors: *id001
  venue: 22nd International Conference on Control, Automation and Systems (ICCAS 2022), Busan
  volume: NA
  issue: NA
  pages: 1421-1425
  doi: Not reported
  url: Not reported
  pub_status: conference
  peer_reviewed: 'Yes'
  peer_review_basis: ICCAS 2022 proceedings header and ICROS ISBN/copyright on p.1 (IEEE Xplore copy).
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: 2022 22nd International Conference on Control, Automation and Systems (ICCAS)
  verified_doi: 10.23919/ICCAS55662.2022.10003761
  verified_url: https://doi.org/10.23919/ICCAS55662.2022.10003761
  verified_pages: 1421-1425
  arxiv: NA
  version_relationship: Corpus copy is the published version
  sources: ['Crossref (exact title match, DOI 10.23919/ICCAS55662.2022.10003761)']
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A3, A4]
  C_capabilities: {SAF1: Partial, SAF2: 'No', SPA1: 'Yes', SPA2: 'Yes', SPA3: 'No', SPA4: 'Yes', HUM1: Partial, HUM2: 'No', NOR1: Partial, NOR2: 'No', NOR3: 'No', NOR4: 'No', EXP1: Partial, EXP2: 'No', EXP3: 'No'}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: none, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "02_Learning_Based_Social_Navigation"
analytical_category: "S2"
coding:
  latency_reported: "No"
  safety_mechanism: "NA"
  uncertainty_treatment: "NA"
  hallucination_treatment: "NA"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "No"
  human_subject_study: "No"
---

# Group Estimation for Social Navigation (Kim, Kwon, Yoon — ICCAS 2022)

Page convention: PDF index (p.N).

## A. Bibliographic — ICCAS 2022, Busan, pp.1421–1425 (IEEE Xplore copy); KAIST, KIST.

## B. Position — S2: explicit group-space modelling in DRL; pre-FM counterpart to VLM group reasoning (e.g., GSON).

## C. Research problem — multi-robot-style DRL ignores human factors such as walking groups; attention/GCN/SRNN methods assume all human states observable (p.1). Contributions: behaviour-based group clustering and group spaces; group-aware reward; simulation evaluation (p.2).

## D. Method — HDBSCAN on (x, y, v, θ); individual space as asymmetric Gaussian with σ_h = max(2v, 0.5), σ_s = 2/3 σ_h, σ_r = 1/2 σ_h (Eq.1–5); group space = convex hull of members' individual spaces (Eq.6); PPO policy on DRL-Long architecture; R_grp penalizes distance < 2.0 m to group hulls (Eq.7–9) (p.2–3).

## L. Quantitative results (Table 1, p.4; success / average length / individual discomfort)
- Circle (13 humans): DRL-Long 0.45 / 27.555 / 14.822; ours 0.49 / 31.320 / 8.958.
- Cross (22 humans): DRL-Long 0.49 / 18.807 / 7.909; ours 0.71 / 18.271 / 7.824.
- **Data-quality notes:** length and discomfort computed over successful episodes only, so compared subsets differ; the introduction criticizes prior methods for assuming observable human poses/velocities, yet the grouping uses observed human positions and velocities without stating how they are obtained; low absolute success (0.45–0.71) for both methods; single baseline.

## N. Limitations
1. **Stated:** none explicit.
2. **Observable:** simulation only; one baseline; no statistics; short paper; group dynamics from a social-force variant (sim-to-real gap).
3. **Social relevance:** directly targets group awareness (C9) with a proxemic metric (C3).

## P. Learning-based analysis — see `learning:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue 2022 22nd International Conference on Control, Automation and Systems (ICCAS); DOI 10.23919/ICCAS55662.2022.10003761; pages 1421-1425; URL https://doi.org/10.23919/ICCAS55662.2022.10003761.
- Sources: Crossref (exact title match, DOI 10.23919/ICCAS55662.2022.10003761).
- Version relationship: Corpus copy is the published version.
- Changed field - venue: PDF-derived '22nd International Conference on Control, Automation and Systems (ICCAS 2022), Busan' -> externally verified '2022 22nd International Conference on Control, Automation and Systems (ICCAS)'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified '10.23919/ICCAS55662.2022.10003761'
- Changed field - url: PDF-derived 'Not reported' -> externally verified 'https://doi.org/10.23919/ICCAS55662.2022.10003761'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

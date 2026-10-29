---
id: 2021_Kastner_Arena-Rosnav
source_pdfs: [06_Datasets_Benchmarks_Evaluation/Arena-Rosnav_Towards_Deployment_of_Deep-Reinforcement-Learning-Based_Obstacle_Avoidance_into_Conventional_Autonomous_Navigation_Systems.pdf]
duplicate_copies: []
related_versions: [Arena 4.0 (arXiv 2024) - in corpus (2024_Shcherbyna_Arena-4.0), 'Arena-Rosnav 2.0 (IROS 2023), Arena-Bench (RA-L 2022), Arena 3.0 (RSS 2024) - not in corpus']
title: 'Arena-Rosnav: Towards Deployment of Deep-Reinforcement-Learning-Based Obstacle Avoidance into Conventional Autonomous Navigation Systems'
authors: &id001 [Linh Kästner, Teham Buiyan, Lei Jiao, Tuan Anh Le, Xinlin Zhao, Zhengcheng Shen, Jens Lambrecht]
year: 2021
venue: 2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
volume: NA
issue: NA
pages: 6456-6463
doi: 10.1109/IROS51168.2021.9636226
url: https://doi.org/10.1109/IROS51168.2021.9636226
pub_status: conference
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref DOI 10.1109/IROS51168.2021.9636226 (DOI lookup); arXiv abs page (2104.03616v2). PDF-derived basis (Stage 1): IEEE IROS 2021 header and DOI on p.1 (IEEE Xplore copy).'
category: S6
folder: 06_Datasets_Benchmarks_Evaluation
folder_category_match: Partial
category_rationale: 'Training/testing platform integrating DRL local planners with conventional ROS stacks (benchmark role; predecessor of Arena 4.0). Not social navigation: dynamic obstacles are random-moving generic obstacles, not humans; secondary contribution is a DRL (A3C+GRU) local planner (S2-like).'
paper_type: simulator; method
fm_used: 'No'
fm_class: [None]
fm_models: []
fm_size: NA
method_family: ['DRL (A3C, GRU memory)', hierarchical planning (A* + intermediate waypoint generator + DRL local planner), curriculum learning]
roles: []
roles_evidence: {}
integration: NA
integration_rationale: No foundation model.
evidence: E2
evidence_rationale: 100 simulated runs per planner, scenario and obstacle velocity on two 2D maps (Table I, Figs.4-6); no real robot.
inputs: ['2D LiDAR (360 deg, downsampled to 344)', subgoal position and angle]
outputs: [continuous linear and angular velocity]
human_repr: [none (generic circular dynamic obstacles moving randomly)]
capabilities: {C1: NA, C2: NA, C3: NA, C4: NA, C5: NA, C6: NA, C7: NA, C8: NA, C9: NA, C10: NA, C11: NA, C12: NA, C13: NA, C14: NA, C15: NA, C16: NA, C17: NA, C18: NA, C19: NA, C20: NA, C21: NA, C22: NA, C23: NA, C24: NA, C25: NA}
exp:
  datasets: []
  simulators: [Arena-Rosnav 2D simulator (ROS)]
  robots: [simulated robot (model not specified)]
  environment: office map and empty map
  indoor_outdoor: indoor
  sensors: [2D LiDAR]
  humans: none (dynamic obstacles)
  n_scenes: 2 maps; 5/10/20 dynamic obstacles x 3 velocities
  n_trajectories: 100 runs per planner per scenario
  n_participants: NA
  split: NA
  baselines: [CADRL, DWA, MPC, TEB]
  ablation: 'No'
  real_robot_trials: 'No'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [crossing obstacles, corridor blocking]
metrics: [NAV | Time | s | average time to reach goal | p.6-7, NAV | Path | m | average distance travelled | p.6-7, SAFETY | Collisions | count | collisions with all objects (per 100 runs implied) | p.6-7, 'NAV | Success | % | goal reached with fewer than two collisions, 3-min timeout | p.6', OTHER | Relative overall performance | % | sum of metric ratios relative to ARENA planner | p.7]
deployment: {fm_model: NA, model_size: NA, api_cloud_local: NA, onboard_offboard: NA, gpu: 'RTX 3090 (training, 8-20 h)', cpu: Not reported, latency: Not reported, query_frequency: NA, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: NA, caching: NA, event_triggered: Global replanning triggered when off-course or stuck >4 s, distillation: NA, quantization: NA, fallback_planner: Global A* replanning, safety_shield: 'No', emergency_behavior: Not reported, uncertainty: NA, hallucination_mitigation: NA, real_time_claim_supported: NA}
repro: {code: 'Yes', code_url: 'https://github.com/ignc-research/arena-rosnav', dataset: NA, dataset_url: NA, checkpoints: Not reported, prompts_published: NA, hardware_specified: Partial, hyperparameters: Yes (Table II) but inconsistent with text, protocol_described: Partial, project_page: NA, concerns: Hyperparameter table lists epsilon/clip-range (DQN/PPO-style) and lr 0.00025 while text describes A3C with lr 0.0001; obstacle velocities in text (0.1/0.3/0.5) differ from Table I (0.1/0.2/0.3).}
limitations_flags: [sim-to-real, limited-scenarios]
web_verification_required: []
cited_missing: [NavRep (ICRA 2021), Güldenring learning local planners for human-aware navigation, PRM-RL, AutoRL, Truong proactive social motion model (T-ASE 2017), Truong dynamic social zone (IJSR 2016), Sisbot 2005 navigation in the presence of humans]
learning: {type: DRL (A3C actor-critic with GRU), state_repr: downsampled LiDAR scan + relative subgoal, human_repr: none (obstacles), reward_design: 'success +15, collision -10, danger -0.15 within safe distance, progress (w_p 0.25 / w_n 0.4), standstill -0.01', social_reward: 'No', prediction_model: 'No', group_modeling: 'No', training_env: 2D randomized maps with random static and dynamic obstacles; curriculum, sim_dependence: High, interpretability: Low, generalization: Tested on 2 maps and 3 obstacle velocities, real_world_validation: 'No', social_metrics: None}
dataset: {kind: training/benchmark platform (2D ROS simulator), real_synthetic: synthetic, size: '2 maps (office, empty); 5/10/20 dynamic obstacles x 3 velocities; 100 runs per planner per scenario', environments: indoor 2D maps, sensors: 2D LiDAR (simulated), ego_view: NA, rgb: 'No', rgbd: 'No', lidar: 'Yes (2D, simulated)', human_trajectories: 'No', dynamic_humans: No (generic random-moving obstacles), group_ann: 'No', intention_ann: 'No', activity_ann: 'No', language_ann: 'No', social_rule_ann: 'No', preference_ann: 'No', multi_action_ann: 'No', personal_space_ann: 'No', site_diversity: 2 maps, closed_loop: 'Yes', vlm_suitability: 'No', real_robot_compat: Partial (ROS integration with conventional stack; no real-robot validation), standard_metrics: 'Time, path length, collisions, success (<2 collisions, 3-min timeout)', known_limitations: Not social navigation (no humans); text/table inconsistencies (DATA_QUALITY_ISSUES section 9)}
coding: {latency_reported: 'No', safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: 'Yes', new_dataset_released: NA, real_robot: 'No', human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2021
  authors: *id001
  venue: 2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Prague
  volume: NA
  issue: NA
  pages: 6456-6463
  doi: 10.1109/IROS51168.2021.9636226
  url: https://github.com/ignc-research/arena-rosnav
  pub_status: conference
  peer_reviewed: 'Yes'
  peer_review_basis: IEEE IROS 2021 header and DOI on p.1 (IEEE Xplore copy).
project_url: https://github.com/ignc-research/arena-rosnav
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: 2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
  verified_doi: 10.1109/IROS51168.2021.9636226
  verified_url: https://doi.org/10.1109/IROS51168.2021.9636226
  verified_pages: 6456-6463
  arxiv: 2104.03616v2
  version_relationship: Corpus copy is the published IEEE version
  sources: [Crossref DOI 10.1109/IROS51168.2021.9636226 (DOI lookup), arXiv abs page (2104.03616v2)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A0]
  C_capabilities: {SAF1: NA, SAF2: NA, SPA1: NA, SPA2: NA, SPA3: NA, SPA4: NA, HUM1: NA, HUM2: NA, NOR1: NA, NOR2: NA, NOR3: NA, NOR4: NA, EXP1: NA, EXP2: NA, EXP3: NA}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: none, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "06_Datasets_Benchmarks_Evaluation"
analytical_category: "S6"
coding:
  latency_reported: "No"
  safety_mechanism: "NA"
  uncertainty_treatment: "NA"
  hallucination_treatment: "NA"
  code_released: "Yes"
  new_dataset_released: "NA"
  real_robot: "No"
  human_subject_study: "No"
---

# Arena-Rosnav (Kästner et al., IROS 2021)

Page convention: PDF index (p.N).

## A. Bibliographic — IROS 2021, pp.6456–6463, DOI 10.1109/IROS51168.2021.9636226; TU Berlin. IEEE Xplore copy (download watermark Sep 2026).

## B. Position — Folder 06 platform; **not social navigation** (no human models). Relevant as the root of the Arena platform line (Arena 4.0, SocialNav2025 competition host). Capabilities coded NA.

## C. Research problem — DRL local planners are myopic and hard to integrate into conventional stacks for long-range navigation (p.1). Contributions: training/testing framework in ROS, intermediate waypoint generator, integration of TEB/DWA/MPC/CADRL/CrowdNav for comparison (p.1–2).

## D. Method — A* global path; subgoal = intersection of look-ahead circle (d_ahead = 1.55 m) with global path; replanning if off-course or stuck (t_lim = 4 s); A3C with GRU on 344-beam LiDAR; actions v ∈ [0, 0.3] m/s, ω ∈ [−2.7, 2.7] ("m/s" in text, sic) (p.2–4).

## L. Quantitative results (Table I, p.7, visually verified; Time s / Path m / Collisions / Success %)
- Overall average: CADRL 170.511 / 33.381 / 41.33 / 88.05; ARENA 158.57 / 30.99 / 19.88 / 94.61; DWA 197.11 / 31.972 / 70.66 / 77.1; MPC 153.49 / 28.443 / 23.8 / 92.5; TEB 188.43 / 30.115 / 24.88 / 91.83.
- Hardest (v_obs 0.3 m/s, 20 obstacles): CADRL 62%, ARENA 81% (65 collisions), DWA 56%, MPC 70.5%, TEB 68%.
- Empty map: TEB best collisions (18.6) and success (94.1) vs ARENA 23.7 / 92.7; Office map: ARENA best (16 / 96.4).
**Data-quality notes:** text (p.7) attributes 68% to DWA, but Table I gives 68% to TEB and 56% to DWA; conclusion claims learning-based planners superior "on all metrics" (p.8), but MPC has best overall time/path and CADRL's overall success (88.05%) is below MPC and TEB; text velocities 0.1/0.3/0.5 m/s vs Table 0.1/0.2/0.3 m/s; hyperparameter table inconsistent with the A3C description.

## N. Limitations
1. **Stated (p.8):** future semantics for behaviour adaptation; better intermediate planner.
2. **Observable:** no humans or social metrics; random-moving obstacles; 2D simulation only; no statistics; overclaimed conclusion.
3. **Relevance:** lineage only.

## P. Learning-based analysis — see `learning:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue 2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS); DOI 10.1109/IROS51168.2021.9636226; pages 6456-6463; URL https://doi.org/10.1109/IROS51168.2021.9636226.
- Sources: Crossref DOI 10.1109/IROS51168.2021.9636226 (DOI lookup); arXiv abs page (2104.03616v2).
- Version relationship: Corpus copy is the published IEEE version.
- Changed field - venue: PDF-derived '2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Prague' -> externally verified '2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)'
- Changed field - url: PDF-derived 'https://github.com/ignc-research/arena-rosnav' -> externally verified 'https://doi.org/10.1109/IROS51168.2021.9636226'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

---
id: 2016_Okal_Bayesian-IRL
source_pdfs: [01_Classical_Social_Navigation/Learning_socially_normative_robot_navigation_behaviors_with_Bayesian_inverse_reinforcement_learning.pdf]
duplicate_copies: []
related_versions: []
title: Learning Socially Normative Robot Navigation Behaviors with Bayesian Inverse Reinforcement Learning
authors: &id001 [Billy Okal, Kai O. Arras]
year: 2016
venue: 2016 IEEE International Conference on Robotics and Automation (ICRA)
volume: NA
issue: NA
pages: 2889-2895
doi: 10.1109/ICRA.2016.7487452
url: https://doi.org/10.1109/ICRA.2016.7487452
pub_status: conference
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1109/ICRA.2016.7487452). PDF-derived basis (Stage 1): ICRA 2016 header and IEEE copyright (IEEE Xplore copy).'
category: S2
folder: 01_Classical_Social_Navigation
folder_category_match: Partial
category_rationale: Learning from demonstration via Bayesian IRL on a controller-graph MDP, producing social costmaps for a classical planner; pre-deep-learning, hence placed in the classical folder, but methodologically learning-based.
paper_type: method
fm_used: 'No'
fm_class: [None]
fm_models: []
fm_size: NA
method_family: ['inverse reinforcement learning (Bayesian, trajectory-based TBIRL)', controller graph (SMDP), costmap-based planning (A* + elastic band)]
roles: []
roles_evidence: {}
integration: NA
integration_rationale: No foundation model.
evidence: E2
evidence_rationale: Quantitative results from PedSim simulation (15 runs per behaviour with 95% intervals) in lobby/hallway/intersection scenarios; real-robot (Daryl) results are qualitative examples.
inputs: [person positions/headings and pair-wise social relations (laser group tracker on robot), obstacles, robot goal]
outputs: [learned reward -> social costmap layer for move_base]
human_repr: [persons with position/heading; pair-wise relations as line segments; distance features]
capabilities: {C1: Partial, C2: 'No', C3: 'Yes', C4: 'No', C5: Partial, C6: 'No', C7: 'No', C8: Partial, C9: 'Yes', C10: Partial, C11: 'Yes', C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: 'Yes', C18: 'No', C19: 'No', C20: 'No', C21: Partial, C22: Partial, C23: 'No', C24: 'Yes', C25: 'No'}
exp:
  datasets: [10 joystick expert demonstrations per behaviour]
  simulators: [PedSim (social force model; open source)]
  robots: ['Daryl (differential drive, humanized appearance)']
  environment: lobby 30x30 m (50 persons, 18 relations); hallway 120x40 m (400 persons, two flows); intersection 40x40 m (280 persons)
  indoor_outdoor: indoor
  sensors: [laser (group tracker on robot)]
  humans: simulated social-force pedestrians incl. groups; real persons in robot demos
  n_scenes: 3 simulated scenarios + real examples
  n_trajectories: 15 runs per behaviour (random starts/goals)
  n_participants: NA
  split: demonstrations vs randomized test runs
  baselines: [contrasting learned behaviours (polite/sociable/rude; merge/nomerge; slipstream/direct)]
  ablation: 'No'
  real_robot_trials: Partial (qualitative)
  human_study: 'No'
  statistical_testing: Partial (95% intervals)
  scenarios: [conversational group / photography group (do not cross), flows in hallway (merge), chaotic intersection (slipstream following)]
metrics: [NAV | Path length | m | | p.5, NAV | Cumulative heading changes (CHC) | rad | path smoothness | p.5, NAV | Mission completion | % | goal reached (abort if stuck >10 min) | p.5, NAV | Time to goal | s | | p.5, SOCIAL | Crossed pair-wise social relations | count | relation disturbance | p.5, 'SOCIAL | Proxemic intrusions (social 1.2-3.6 m, personal 0.45-1.2 m, intimate 0-0.45 m) | count | | p.5']
deployment: {fm_model: NA, model_size: NA, api_cloud_local: NA, onboard_offboard: Not reported, gpu: NA, cpu: Not reported, latency: Not reported, query_frequency: NA, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: NA, caching: NA, event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: NA, safety_shield: NA, emergency_behavior: NA, uncertainty: Bayesian reward posterior (expert optimality beta), hallucination_mitigation: NA, real_time_claim_supported: NA}
repro: {code: Simulator open source; learning code not stated, code_url: 'https://github.com/srl-freiburg/pedsim_ros', dataset: 'No', dataset_url: NA, checkpoints: NA, prompts_published: NA, hardware_specified: Partial, hyperparameters: 'Yes (delta 0.4, N_max 440, K 20, epsilon 0.01)', protocol_described: Partial, project_page: NA, concerns: Results only in plots; subjective metrics are proxies (authors acknowledge no user study).}
limitations_flags: [no-human-study, sim-to-real]
web_verification_required: []
cited_missing: ['Vasquez, Okal, Arras IROS 2014 IRL feature comparison', Henry et al. 2010 learning to navigate through crowds, Kim & Pineau socially adaptive path planning, Sisbot human-aware motion planner, Lu layered costmaps, Ramachandran & Amir BIRL]
learning: {type: 'IRL (Bayesian, trajectory-sampled likelihood)', state_repr: 'controller-graph macro states (continuous, POSQ local controllers)', human_repr: 'distance to persons, obstacles and social-relation segments; relative heading of persons', reward_design: 'linear in 6 features (distances to persons/obstacles/relations, relative heading, heading deviation, distance to goal)', social_reward: Yes (learned from demonstrations of polite/sociable/rude etc.), prediction_model: 'No', group_modeling: Yes (pair-wise relations; group tracker grouping probability > 0.5), training_env: PedSim simulation; 10 demonstrations per behaviour, sim_dependence: Medium-high, interpretability: 'High (linear reward, costmaps)', generalization: Same features learn multiple behaviours; varied starts/goals, real_world_validation: Qualitative examples, social_metrics: 'Relation disturbance, proxemic intrusions'}
classical: {human_is: agent with personal spaces and social ties, social_repr: learned costmap over proxemic and relation features, hand_rules: Partial (hand-chosen features), math_model: MDP/SMDP on controller graph; Bayesian IRL posterior (Eq.5-9), planner: weighted A* on learned costmap + elastic band, interpretability: High, strengths: Context-dependent behaviours (polite/sociable/rude) from few demonstrations; groups respected, limitations: Feature engineering; behaviours defined by demonstrator; proxy social metrics, later_improvement: DRL and VLM methods generalize context and norms without hand-crafted features}
coding: {latency_reported: 'No', safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: Partial, new_dataset_released: NA, real_robot: Demo, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2016
  authors: *id001
  venue: 2016 IEEE International Conference on Robotics and Automation (ICRA), Stockholm
  volume: NA
  issue: NA
  pages: 2889-2895
  doi: Not reported
  url: https://github.com/srl-freiburg/pedsim_ros (simulator)
  pub_status: conference
  peer_reviewed: 'Yes'
  peer_review_basis: ICRA 2016 header and IEEE copyright (IEEE Xplore copy).
project_url: https://github.com/srl-freiburg/pedsim_ros (simulator)
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: 2016 IEEE International Conference on Robotics and Automation (ICRA)
  verified_doi: 10.1109/ICRA.2016.7487452
  verified_url: https://doi.org/10.1109/ICRA.2016.7487452
  verified_pages: 2889-2895
  arxiv: NA
  version_relationship: Corpus copy is the published version
  sources: ['Crossref (exact title match, DOI 10.1109/ICRA.2016.7487452)']
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A4]
  C_capabilities: {SAF1: Partial, SAF2: 'No', SPA1: 'Yes', SPA2: 'Yes', SPA3: 'No', SPA4: 'Yes', HUM1: Partial, HUM2: Partial, NOR1: 'Yes', NOR2: 'No', NOR3: 'Yes', NOR4: 'No', EXP1: Partial, EXP2: 'No', EXP3: 'No'}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: demo, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "01_Classical_Social_Navigation"
analytical_category: "S2"
coding:
  latency_reported: "No"
  safety_mechanism: "NA"
  uncertainty_treatment: "NA"
  hallucination_treatment: "NA"
  code_released: "Partial"
  new_dataset_released: "NA"
  real_robot: "Demo"
  human_subject_study: "No"
---

# Bayesian IRL for Socially Normative Navigation (Okal & Arras, ICRA 2016)

Page convention: PDF index (p.N).

## A. Bibliographic — ICRA 2016, Stockholm, pp.2889–2895 (IEEE Xplore copy); Univ. of Freiburg, Bosch. SPENCER project.

## B. Position — classical-era learning-from-demonstration (IRL) social navigation; coded S2 (learning-based) though in folder 01.

## C. Research problem — IRL for social navigation limited to simple behaviours/grid worlds that scale poorly (p.1–2). Contributions: controller-graph representation; trajectory-based Bayesian IRL (TBIRL); learning multiple behaviours of varying social normativeness with the same features (p.1–2).

## D. Method — controller graph G = ⟨V, E, W⟩ with POSQ local controllers (Alg.1); BIRL posterior (Eq.5–7); TBIRL likelihood over sampled trajectories (Eq.9, Alg.2); six features; learned rewards as costmap layer in move_base (p.2–5).

## L. Results — plots only (Figs.5–8, 15 runs, 95% intervals): social normativeness costs longer, less smooth paths in the lobby; polite behaviour minimizes intrusions and relation crossings; sociable approaches people closely without crossing relations; merge (hallway) and slipstream (intersection) improve mission completion at the cost of longer times. Robot Daryl avoids splitting a conversing pair when tracker grouping probability > 0.5, passes between unrelated persons (Fig.9). No numeric tables.

## N. Limitations
1. **Stated (p.5):** subjective metrics emulate perception; user studies beyond scope.
2. **Observable:** quantitative results only graphical; behaviours defined by authors' demonstrations; real robot qualitative.
3. **Social relevance:** explicit context-dependent styles (C24) and group ties (C9/C10), precursors of VLM-based context reasoning.

## P. Classical / learning analysis — see `classical:` and `learning:` blocks.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue 2016 IEEE International Conference on Robotics and Automation (ICRA); DOI 10.1109/ICRA.2016.7487452; pages 2889-2895; URL https://doi.org/10.1109/ICRA.2016.7487452.
- Sources: Crossref (exact title match, DOI 10.1109/ICRA.2016.7487452).
- Version relationship: Corpus copy is the published version.
- Changed field - venue: PDF-derived '2016 IEEE International Conference on Robotics and Automation (ICRA), Stockholm' -> externally verified '2016 IEEE International Conference on Robotics and Automation (ICRA)'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified '10.1109/ICRA.2016.7487452'
- Changed field - url: PDF-derived 'https://github.com/srl-freiburg/pedsim_ros (simulator)' -> externally verified 'https://doi.org/10.1109/ICRA.2016.7487452'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

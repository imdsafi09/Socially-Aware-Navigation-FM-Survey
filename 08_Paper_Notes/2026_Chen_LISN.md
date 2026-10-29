---
id: 2026_Chen_LISN
source_pdfs: [04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/LISN_arXiv2512.09920v1.pdf]
duplicate_copies: []
related_versions: ['arXiv:2512.09920v1 (10 Dec 2025) = corpus copy; published version ICRA 2026']
title: 'LISN: Language-Instructed Social Navigation with VLM-based Controller Modulating'
authors: [Junting Chen, Yunchuan Li, Panfeng Jiang, Jiacheng Du, Zixuan Chen, Chenrui Tie, Jiajun Deng, Lin Shao]
year: 2026
venue: 2026 IEEE International Conference on Robotics and Automation (ICRA)
volume: NA
issue: NA
pages: 1855-1862
doi: 10.1109/ICRA57385.2026.11695757
url: https://doi.org/10.1109/ICRA57385.2026.11695757
pub_status: conference (corpus copy is arXiv author version)
peer_reviewed: 'Yes'
peer_review_basis: 'Crossref record: ICRA 2026, pp. 1855-1862, DOI 10.1109/ICRA57385.2026.11695757 (verified 2026-10-19). Corpus PDF is arXiv v1.'
category: S4
folder: 04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core
folder_category_match: 'Yes'
category_rationale: GPT-4o slow loop interprets language instructions and scene semantics and modulates social-costmap attributes and social-force controller parameters; new LISN-Bench for language-instructed social navigation.
paper_type: method + benchmark
fm_used: 'Yes'
fm_class: [VLM, open-vocabulary perception]
fm_models: [GPT-4o (slow-loop reasoner), Grounded-SAM 2 (segmentation tool), RoboPoint (point prediction tool)]
fm_size: Not reported (API)
method_family: [prompting with tool calls, fast-slow hierarchy, social force model, social costmap layer]
roles: [F1, F4, F6, F7, F11]
roles_evidence: {F1: 'VLM identifies salient entities (doctor, restricted regions) via Grounded-SAM 2 / RoboPoint tool calls (p.4).', F4: 'Interprets instruction-specified social rules (keep away from patients, avoid yellow zones).', F6: Sets cost_value / inflation_radius / decay of a SocialLayer and SFM weights (p.5)., F7: 'Selects behaviour mode (Follow, Goal, exploratory, idle) mapped to predefined parameters (p.1).', F11: Introduces LISN-Bench with subject and region compliance scores.}
integration: I4
integration_rationale: VLM outputs cost-layer attributes and controller parameters consumed by a 5 ms SFM controller and costmap (p.4).
evidence: E2
evidence_rationale: Closed-loop simulation in Arena 3.0 (5 tasks, >=3 scenarios each, 5-9 repetitions); explicitly no real-robot evaluation (p.8).
inputs: [RGB, LiDAR, language instruction, conversation history]
outputs: [costmap attributes, controller parameters, behaviour mode, navigation goal point]
human_repr: [segmented person mask projected to costmap, 'identity class (e.g., doctor)', SFM agent]
capabilities: {C1: 'Yes', C2: 'No', C3: 'Yes', C4: 'No', C5: Partial, C6: 'No', C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: Partial, C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: Partial, C18: 'No', C19: 'No', C20: Partial, C21: Partial, C22: 'No', C23: 'Yes', C24: 'Yes', C25: 'No'}
exp:
  datasets: []
  simulators: ['Arena 3.0 (ROS Noetic, Gazebo) with hospital and warehouse assets']
  robots: [simulated differential-drive robot]
  environment: hospital and warehouse
  indoor_outdoor: indoor
  sensors: [RGB, LiDAR]
  humans: simulated pedestrians with predefined trajectories and identities
  n_scenes: 5 tasks x >=3 scenarios
  n_trajectories: 5-9 repetitions per scenario
  n_participants: NA
  split: NA
  baselines: [VLM-Nav, VLM-Social-Nav (re-implemented)]
  ablation: 'No'
  real_robot_trials: 'No'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [Follow Doctor, Reception Desk, Public Area, Go to Forklift in Hurry, Go to Forklift Carefully]
metrics: [NAV | Success Rate | % | reaches goal while satisfying task-specific semantic constraints | p.3, SAFETY | Collision Rate | % | runs with collisions against pedestrians or obstacles | p.3, SOCIAL | Path Smoothness | rad (cumulative curvature) | sum of wrapped heading changes; defined lower = smoother but reported with up-arrow | p.3, SOCIAL | Average Subject Score | 0-100 | distance-based score toward specific subjects (U-shaped for following) | p.3, SOCIAL | Average Region Score | 0-100 | 100 minus severity-weighted zone-violation penalties | p.3, DEPLOY | Slow / fast loop latency | ms | VLM 7094 ms average (10 runs); SFM controller 5.27 ms (100 runs) | p.7]
deployment: {fm_model: GPT-4o, model_size: Not reported, api_cloud_local: Cloud API, onboard_offboard: Simulation, gpu: Not reported, cpu: Not reported, latency: VLM slow loop ~7.1 s; fast loop 5.27 ms, query_frequency: Every ~10 s or on new user query, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Yes (fast-slow), caching: Not reported, event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: SFM controller continues with last parameters, safety_shield: Costmap layers fused by max-value so obstacle costs always respected; SFM reactive avoidance, emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: Parameter values predefined in system prompt; VLM selects modes/tools rather than raw controls, real_time_claim_supported: Yes (in simulation)}
repro: {code: Not reported (project website only), code_url: Not reported, dataset: LISN-Bench (release not stated), dataset_url: Not reported, checkpoints: Not reported, prompts_published: Partial, hardware_specified: Not reported, hyperparameters: Not reported, protocol_described: Not reported, project_page: 'https://social-nav.github.io/LISN-project/', concerns: Simulation only; baselines re-implemented by the authors; path-smoothness direction inconsistent.}
limitations_flags: [latency, cloud-dependence, limited-scenarios, no-human-study, sim-to-real]
web_verification_required: []
cited_missing: [Arena 3.0 (RSS 2024), RoboPoint, Grounded-SAM 2, SFW-SAC, VLM-Nav]
external_verification: {verified_on: '2026-10-19', status_class: 'A: published, peer-reviewed', source: Crossref DOI 10.1109/ICRA57385.2026.11695757, arxiv_id: 2512.09920v1}
stage2: {added: true, download_source: 'https://arxiv.org/pdf/2512.09920v1', source_type: arXiv (author version), inclusion_reason: Direct FM social navigation (language-instructed social norms); peer-reviewed; cited by G2-Nav; not cited by Cai 2026 though on arXiv before its cut-off.}
coding: {latency_reported: 'Yes', safety_mechanism: 'Yes', uncertainty_treatment: 'No', hallucination_treatment: Partial, code_released: 'No', new_dataset_released: 'No', real_robot: 'No', human_subject_study: 'No'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A3, A5]
  C_capabilities: {SAF1: 'Yes', SAF2: 'No', SPA1: 'Yes', SPA2: 'No', SPA3: 'No', SPA4: Partial, HUM1: Partial, HUM2: 'No', NOR1: Partial, NOR2: 'Yes', NOR3: 'Yes', NOR4: 'No', EXP1: Partial, EXP2: 'No', EXP3: Partial}
  B_roles: [R1, R2, R4]
  D_interface: [D3, D4]
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: none, EV4_real_humans_in_trials: simulated-only, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: 5-9 repetitions per scenario, statistical_testing: 'No', cross_environment: No/unclear, runtime_measured: 'Yes'}
  cross_cutting: {temporal_coupling: asynchronous, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'Yes', uncertainty: 'No', hallucination_mitigation: Partial, privacy_constraint: 'No', inference_location: cloud API}
physical_source_folder: "04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core"
analytical_category: "S4"
coding:
  latency_reported: "Yes"
  safety_mechanism: "Yes"
  uncertainty_treatment: "No"
  hallucination_treatment: "Partial"
  code_released: "No"
  new_dataset_released: "No"
  real_robot: "No"
  human_subject_study: "No"
---

# LISN / Social-Nav-Modulator (Chen et al., ICRA 2026)

Page convention: PDF index of the corpus copy (arXiv v1).

## A. Bibliographic
ICRA 2026, pp. 1855-1862, DOI 10.1109/ICRA57385.2026.11695757 (Crossref-verified 2026-10-19). Corpus copy arXiv:2512.09920v1. Peer-reviewed: Yes.

## B. Position
S4 direct. New task framing: language-instructed social navigation (instructions carrying social rules) with a benchmark (LISN-Bench, built on Arena 3.0). VLM acts as a slow-loop *modulator* of a classical social planner (I4), similar in spirit to G2-Nav and VLM-Social-Nav but changing controller parameters as well as costs.

## C. Research problem
Existing social-navigation benchmarks measure low-level metrics; robots must also comply with instructions and social norms expressed in language (p.1). VLM latency (seconds) is incompatible with reactive control.

## D. Method
Slow system: GPT-4o + tools (RoboPoint, Grounded-SAM 2) produce visual markers and parameter updates (Eq.1). Fast system: SocialLayer costmap (exponential decay around VLM-tagged entities) + SFM local planner with modified following force (Eq.5-6).

## G. Social capabilities
C1 Yes (collision rate) · C3 Yes (subject score enforcing distance bands) · C23 Yes (instruction compliance measured by success with semantic constraints and region score) · C24 Yes (hurry vs carefully) · C5 Partial (tracking the doctor) · C11, C17 Partial · C20/C21 Partial (curvature smoothness as comfort proxy) · others No.

## H/I. I4; E2.

## L. Results (Table II)
Success: 100/100/90/100/66.67% across five tasks vs VLM-Social-Nav 0/50/30/60/0; collision 5.88/0/10/0/0%. Subject score (Follow Doctor) 78.63 vs 71.84; region score (Forklift Carefully) 80.50 vs 36.56. Average success 91.3%.

## M. Deployment
GPT-4o slow loop 7.1 s average; SFM fast loop 5.27 ms.

## N. Limitations
1. Stated: simulation only; tasks/metrics not exhaustive; future cultural norms and real robots (p.8).
2. Observable: smoothness metric defined "lower = smoother" yet reported with an up-arrow and higher values described as better (data-quality issue); baselines re-implemented; no statistics.

## P. Direct-paper questions (abridged)
1 Instruction- and norm-compliant navigation. 3 GPT-4o + tool models. 6 Parameters, costs, markers. 7 SFM controller + costmap. 10 Costmap max-fusion; reactive SFM. 21 Asynchronous; 7 s VLM. 23 Simulation only. 24 No human study.

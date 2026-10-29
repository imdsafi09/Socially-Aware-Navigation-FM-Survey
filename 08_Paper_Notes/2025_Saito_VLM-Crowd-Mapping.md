---
id: 2025_Saito_VLM-Crowd-Mapping
source_pdfs: [04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/VLM-Crowd-Mapping-SafeMobility_arXiv2602.10910v1.pdf]
duplicate_copies: []
related_versions: ['arXiv:2602.10910v1 (11 Feb 2026) = corpus copy (posted after the conference publication)']
title: Safe mobility support system using crowd mapping and avoidance route planning using VLM
authors: [Sena Saito, Kenta Tabata, Renato Miyagusuku, Koichi Ozaki]
year: 2025
venue: 2025 IEEE International Conference on Real-time Computing and Robotics (RCAR)
volume: NA
issue: NA
pages: 727-732
doi: 10.1109/RCAR65431.2025.11139707
url: https://doi.org/10.1109/RCAR65431.2025.11139707
pub_status: conference (corpus copy is arXiv version)
peer_reviewed: 'Yes'
peer_review_basis: 'Crossref record: RCAR 2025, pp. 727-732, DOI 10.1109/RCAR65431.2025.11139707; arXiv journal_ref also names RCAR 2025 (verified 2026-10-19).'
category: S4
folder: 04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core
folder_category_match: 'Yes'
category_rationale: A VLM classifies camera views as crowd/free; results are interpolated by Gaussian process regression into a crowd-density "abstraction map" used for crowd-avoiding route planning on a real campus robot.
paper_type: method
fm_used: 'Yes'
fm_class: [VLM]
fm_models: [gpt-4o-mini]
fm_size: Not reported (API)
method_family: [zero-shot prompting, Gaussian process regression, costmap fusion, Dijkstra]
roles: [F1, F6]
roles_evidence: {F1: VLM returns "crowd" or "free" for the forward view (Table II) (p.6)., F6: Binary crowd labels every 3 m are GPR-interpolated into a crowd cost layer fused with the geometric map (p.1).}
integration: I4
integration_rationale: VLM labels become a cost layer for Dijkstra global planning.
evidence: E0
evidence_rationale: Two real-world trials with an intentionally staged crowd of eight students; outcomes shown as maps/paths only, no quantitative metrics (p.4).
inputs: [RGB camera image, robot pose (3D LiDAR SLAM), fixed prompt]
outputs: [binary crowd label, GPR crowd-density map, global route]
human_repr: [crowd presence (binary) at robot location]
capabilities: {C1: Partial, C2: 'No', C3: 'No', C4: 'No', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: Partial, C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: 'No', C24: Partial, C25: 'No'}
exp:
  datasets: []
  simulators: []
  robots: ['custom wheeled robot (ASUS PN50, VLP-16, 2x RPLIDAR S2M1, Logicool C930e)']
  environment: Utsunomiya University campus
  indoor_outdoor: outdoor
  sensors: [3D LiDAR, 2D LiDAR, RGB camera]
  humans: intentionally created crowd of 8 students
  n_scenes: 2 trials
  n_trajectories: '2'
  n_participants: 8 crowd actors (not a study)
  split: NA
  baselines: []
  ablation: Map weighting ratios (1:1, 1:9, 1:1:1, 2:2:1, 4:4:1)
  real_robot_trials: Partial (2 qualitative trials)
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [crowd avoidance on campus route]
metrics: [OTHER | VLM crowd label | crowd/free | per image case (far / near / passed) | p.5]
deployment: {fm_model: gpt-4o-mini, model_size: Not reported, api_cloud_local: Cloud API, onboard_offboard: Onboard PC + cloud VLM, gpu: Not reported, cpu: ASUS PN50, latency: Not reported, query_frequency: Every 3 m of travel, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Not reported, caching: Not reported, event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: Not reported, safety_shield: Geometric obstacle costs retained in fused map (classical planner), emergency_behavior: Not reported, uncertainty: Partial (GPR variance interpreted as confidence), hallucination_mitigation: No (unstable labels reported), real_time_claim_supported: Not reported}
repro: {code: Not reported, code_url: Not reported, dataset: Not reported, dataset_url: Not reported, checkpoints: Not reported, prompts_published: Yes (prompt in Table II), hardware_specified: 'Yes', hyperparameters: Not reported, protocol_described: Not reported, project_page: Not reported, concerns: Two trials; no metrics; crowd treated as quasi-static.}
limitations_flags: [limited-scenarios, no-human-study, cloud-dependence]
web_verification_required: []
cited_missing: [Trautman IGP (in corpus), SARL (in corpus)]
external_verification: {verified_on: '2026-10-19', status_class: 'A: published, peer-reviewed', source: Crossref DOI 10.1109/RCAR65431.2025.11139707, arxiv_id: 2602.10910v1}
stage2: {added: true, download_source: 'https://arxiv.org/pdf/2602.10910v1', source_type: arXiv (posted after publication), inclusion_reason: Direct FM crowd-aware navigation (criteria A+B+C met); peer-reviewed; evidence minimal.}
coding: {latency_reported: 'No', safety_mechanism: 'Yes', uncertainty_treatment: Partial, hallucination_treatment: 'No', code_released: 'No', new_dataset_released: NA, real_robot: Demo, human_subject_study: 'No'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A5]
  C_capabilities: {SAF1: Partial, SAF2: 'No', SPA1: 'No', SPA2: 'No', SPA3: 'No', SPA4: Partial, HUM1: 'No', HUM2: 'No', NOR1: 'No', NOR2: 'No', NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: [R2]
  D_interface: [D3]
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'No', EV3_physical_robot: demo, EV4_real_humans_in_trials: staged, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: '2', statistical_testing: 'No', cross_environment: No/unclear, runtime_measured: 'No'}
  cross_cutting: {temporal_coupling: per-decision, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'Yes', uncertainty: Partial, hallucination_mitigation: 'No', privacy_constraint: 'No', inference_location: cloud API}
physical_source_folder: "04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core"
analytical_category: "S4"
coding:
  latency_reported: "No"
  safety_mechanism: "Yes"
  uncertainty_treatment: "Partial"
  hallucination_treatment: "No"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "Demo"
  human_subject_study: "No"
---

# VLM crowd mapping for crowd-avoiding routes (Saito et al., RCAR 2025)

Page convention: PDF index of the corpus copy (arXiv v1).

## A. Bibliographic
RCAR 2025, pp. 727-732, DOI 10.1109/RCAR65431.2025.11139707 (Crossref-verified). Utsunomiya University. Peer-reviewed: Yes.

## B. Position
S4 direct with weak evidence (E0): VLM as abstract-concept (crowd) detector feeding a probabilistic cost layer; avoids crowded areas at route level rather than negotiating with people.

## C-D. Problem and method
Crowds are abstract concepts hard to quantify; gpt-4o-mini returns crowd/free per image every 3 m; GPR (RBF) interpolates into an "Abstraction Map"; fused with geometric map; Dijkstra planning.

## G. Social capabilities
C17 Partial (crowd avoidance, qualitative) · C1 Partial · C24 Partial · others No.

## H/I. I4; E0 (two qualitative real trials).

## L. Results
VLM labelled the crowd "free" from a distance and after passing, "crowd" when close (Table II); planned routes avoided the staged crowd in both trials; geometric:crowd weighting 9:1 ignores the crowd.

## N. Limitations
Stated: unstable recognition near the crowd; forward camera offsets crowd location; crowd assumed nearly static. Observable: no quantitative evaluation, no baselines.

## P. Direct-paper questions (abridged)
1 Crowd-avoiding route planning. 3 gpt-4o-mini. 6 Binary labels -> GPR cost layer. 10 Geometric costs retained. 19 GPR variance only. 23 Real robot (2 trials). 24 No.

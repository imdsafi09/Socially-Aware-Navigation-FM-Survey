---
id: 2025_Martinez-Baselga_Hey-Robot
source_pdfs: [04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/Hey-Robot-LLM-MPC_arXiv2409.13393v1.pdf]
duplicate_copies: []
related_versions: ['arXiv:2409.13393v1 (20 Sep 2024) = corpus copy; published version ICRA 2025']
title: Hey Robot! Personalizing Robot Navigation Through Model Predictive Control with a Large Language Model
authors: [Diego Martinez-Baselga, Oscar de Groot, Luzia Knoedler, Javier Alonso-Mora, Luis Riazuelo, Luis Montano]
year: 2025
venue: 2025 IEEE International Conference on Robotics and Automation (ICRA)
volume: NA
issue: NA
pages: 11002-11009
doi: 10.1109/ICRA55743.2025.11128826
url: https://doi.org/10.1109/ICRA55743.2025.11128826
pub_status: conference (corpus copy is arXiv author version)
peer_reviewed: 'Yes'
peer_review_basis: 'Crossref record: ICRA 2025, pp. 11002-11009, DOI 10.1109/ICRA55743.2025.11128826 (verified 2026-10-19).'
category: S4
folder: 04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core
folder_category_match: 'Yes'
category_rationale: LLM/VLM assistants generate and tune MPC cost functions from user instructions (e.g., keep distance from people, follow a human, navigate as in a hospital) for navigation among pedestrians; MPC keeps collision constraints.
paper_type: method
fm_used: 'Yes'
fm_class: [LLM, VLM]
fm_models: [GPT-4o-mini (four assistants incl. camera assistant)]
fm_size: Not reported (API)
method_family: [LLM code generation, prompted weight retrieval, MPC with homology-class guidance (Acados)]
roles: [F1, F4, F6, F7]
roles_evidence: {F1: 'Camera assistant describes the scene (crowded, narrow, hospital) as bullet points (p.3).', F4: 'Interprets context norms such as hospital-appropriate motion (query e, Table V).', F6: Generates cost-function code and importance ratings 0-10 converted to weights (p.3)., F7: Capability assistant routes queries; switches tasks (follow path / follow human / reach goal).}
integration: I4
integration_rationale: LLM output reconfigures the MPC cost and parameters; the MPC computes controls with collision constraints (p.2).
evidence: E2
evidence_rationale: 'Simulation: 10 runs x 6 queries (Table V) and 5 runs x 2 tasks with Social-Force pedestrians; lab demonstration with Turtlebot 2 and 4 pedestrians (qualitative).'
inputs: [natural-language user queries, RGB image (camera assistant), human positions + constant-velocity prediction, local costmap]
outputs: [MPC cost-function code, weights and parameters, control commands (via MPC)]
human_repr: [disk with constant-velocity predicted trajectory]
capabilities: {C1: 'Yes', C2: 'No', C3: 'Yes', C4: 'No', C5: 'No', C6: Partial, C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: 'No', C18: 'No', C19: 'No', C20: Partial, C21: Partial, C22: 'No', C23: 'Yes', C24: 'Yes', C25: 'No'}
exp:
  datasets: []
  simulators: [custom simulation with Clearpath Jackal and Social-Force pedestrians]
  robots: ['Turtlebot 2 (lab, OptiTrack)']
  environment: corridor-like scenario; lab
  indoor_outdoor: indoor
  sensors: [OptiTrack (real), camera]
  humans: simulated SFM pedestrians; 4 people in lab demo
  n_scenes: corridor scenario
  n_trajectories: 10 simulations per query (6 queries)
  n_participants: NA
  split: NA
  baselines: [default query (no extra instruction)]
  ablation: Per-assistant evaluation (10 trials per prompt)
  real_robot_trials: Partial (qualitative lab demo)
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [follow path, follow closest human, drive quickly/carefully, factory, hospital, keep >=1.5 m from pedestrians]
metrics: [OTHER | Assistant success rate | fraction | correct routing / cost generation / weight retrieval over 10 trials | p.5, SAFETY | Collision rate | fraction | per 10 simulations | p.6, SOCIAL | Min. distance | m | minimum distance to pedestrians | p.6, 'DEPLOY | Query processing time | s | capability 1.91, cost generation 4.02, weight retrieval 1.16, camera 1.79 (mean) | p.5']
deployment: {fm_model: GPT-4o-mini, model_size: Not reported, api_cloud_local: Cloud API, onboard_offboard: Not reported, gpu: Not reported, cpu: Not reported, latency: ~3 s for parameter updates; ~7 s with new cost generation, query_frequency: Per user query, planner_frequency: Not reported, controller_frequency: MPC every control period (rate not reported), asynchronous: Yes (MPC keeps running), caching: Not reported, event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: Not reported, safety_shield: MPC collision-avoidance constraints for humans and static obstacles (Eq.3), emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: Code template and predefined cost terms; LLM rates importance as integers 0-10 instead of raw weights, real_time_claim_supported: Yes for MPC; LLM reconfiguration takes seconds}
repro: {code: Promised ("released upon acceptance"), code_url: Not reported, dataset: Not reported, dataset_url: Not reported, checkpoints: Not reported, prompts_published: Partial, hardware_specified: Partial, hyperparameters: Not reported, protocol_described: Not reported, project_page: Not reported, concerns: 'Instruction "keep at least 1.5 m" yields 1.16 m minimum distance (not satisfied, not discussed); real-world part qualitative.'}
limitations_flags: [cloud-dependence, limited-scenarios, no-human-study]
web_verification_required: []
cited_missing: [Language-to-costmap (Sharma et al.), VR-based personalized navigation (de Heuvel)]
external_verification: {verified_on: '2026-10-19', status_class: 'A: published, peer-reviewed', source: Crossref DOI 10.1109/ICRA55743.2025.11128826, arxiv_id: 2409.13393v1}
stage2: {added: true, download_source: 'https://arxiv.org/pdf/2409.13393v1', source_type: arXiv (author version), inclusion_reason: Direct FM human-aware navigation (cost generation incl. distance-to-people); peer-reviewed; found in saturation search; not cited by Cai 2026.}
coding: {latency_reported: 'Yes', safety_mechanism: 'Yes', uncertainty_treatment: 'No', hallucination_treatment: 'Yes', code_released: Promised, new_dataset_released: NA, real_robot: Demo, human_subject_study: 'No'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A2]
  C_capabilities: {SAF1: 'Yes', SAF2: 'No', SPA1: 'Yes', SPA2: 'No', SPA3: 'No', SPA4: 'No', HUM1: Partial, HUM2: 'No', NOR1: 'No', NOR2: 'Yes', NOR3: 'Yes', NOR4: 'No', EXP1: Partial, EXP2: 'No', EXP3: Partial}
  B_roles: [R1, R4]
  D_interface: [D3]
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: demo, EV4_real_humans_in_trials: staged, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: 10 simulations per query (6 queries), statistical_testing: 'No', cross_environment: No/unclear, runtime_measured: 'Yes'}
  cross_cutting: {temporal_coupling: asynchronous, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'Yes', uncertainty: 'No', hallucination_mitigation: 'Yes', privacy_constraint: 'No', inference_location: cloud API}
physical_source_folder: "04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core"
analytical_category: "S4"
coding:
  latency_reported: "Yes"
  safety_mechanism: "Yes"
  uncertainty_treatment: "No"
  hallucination_treatment: "Yes"
  code_released: "Promised"
  new_dataset_released: "NA"
  real_robot: "Demo"
  human_subject_study: "No"
---

# Hey Robot! (Martinez-Baselga et al., ICRA 2025)

Page convention: PDF index of the corpus copy (arXiv v1).

## A. Bibliographic
ICRA 2025, pp. 11002-11009, DOI 10.1109/ICRA55743.2025.11128826 (Crossref-verified). Universidad de Zaragoza / TU Delft. Peer-reviewed: Yes.

## B. Position
S4 direct. LLM as **cost-function programmer** for a collision-constrained MPC: personalised, context-dependent social behaviour (distance to people, speed in hospitals) without retraining.

## C-D. Problem and method
End users cannot configure navigation behaviour (p.1). Four GPT-4o-mini assistants: capability (route query), cost generation (writes CasADi cost code), camera (scene description), weight retrieval (integer importance -> weights). MPC with ellipsoidal human-avoidance constraints and parallel homology-class guidance.

## G. Social capabilities
C1 Yes (no collisions in 60 runs) · C3 Yes (minimum distance responds to keep-distance query, 1.16 m vs 0.22 m default) · C23 Yes (instruction compliance measured per assistant) · C24 Yes (hospital/factory) · C6 Partial (constant-velocity prediction) · C20/C21 Partial (velocity/acceleration smoothness) · others No.

## H/I. I4; E2 (lab run qualitative).

## L. Results
Assistants: cost generation 0.9-1.0 success; weight retrieval 0.8-1.0 (Table II). Table V: "drive carefully" and "hospital" halve speed (1.38-1.41 m/s); "keep at least 1.5 m" raises min distance to 1.16 m.

## N. Limitations
Stated: limited to cost inputs and perception; future scene segmentation and realistic environments with different users. Observable: keep-distance instruction not fully satisfied; LLM delays of seconds; no human evaluation.

## P. Direct-paper questions (abridged)
1 Personalised/context-aware navigation among people. 3 GPT-4o-mini. 6 Cost code, weights. 7 MPC. 10 MPC collision constraints. 21 3-7 s per reconfiguration. 23 Lab demo. 24 No.

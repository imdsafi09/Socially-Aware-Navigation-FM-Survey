---
id: 2025_Ruo_LLM-Social-Cues
source_pdfs: [04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/Ruo_LLM-Social-Cues_ROMAN2025.pdf]
duplicate_copies: []
related_versions: [RO-MAN 2025 proceedings version = corpus copy (no arXiv version found)]
title: An LLM-based Architecture for Socially Intelligent Robot Navigation based on Social Cues
authors: [Andrea Ruo, Jonathan Cacace, Magí Dalmau-Moreno, Lorenzo Sabattini, Valeria Villani]
year: 2025
venue: 2025 34th IEEE International Conference on Robot and Human Interactive Communication (RO-MAN)
volume: NA
issue: NA
pages: 1494-1500
doi: 10.1109/RO-MAN63969.2025.11217843
url: https://doi.org/10.1109/RO-MAN63969.2025.11217843
pub_status: conference
peer_reviewed: 'Yes'
peer_review_basis: IEEE RO-MAN 2025 proceedings, pp. 1494-1500, DOI 10.1109/RO-MAN63969.2025.11217843 (IEEE Xplore record; full text read 2026-10-26).
category: S4
folder: 04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core
folder_category_match: 'Yes'
category_rationale: 'Two-layer social navigation: a local LLM (function calling) infers the navigation mode (reach, follow, accompany), the maximum speed and the social-zone distance from the user request and social cues (age category, comfort); a control-barrier-function controller enforces collision avoidance, speed and field-of-view constraints and the asymmetric social space. Simulation in Gazebo plus an offline 100-request accuracy test.'
paper_type: method
fm_used: 'Yes'
fm_class: [LLM]
fm_models: ['llama3.1:8b', command-r7b (via Ollama)]
fm_size: 8B and 7B
method_family: [LLM function calling, control barrier functions, proxemic social space]
roles: [F2, F4, F6, F7]
roles_evidence: {F2: 'The LLM updates the user parameters (category, confidence) from the request (p.3).', F4: Social-zone distance and speed are chosen from comfort and age category (p.4)., F6: LLM outputs maximum speed and social-zone distance that parameterise the CBF constraints and goal pose (p.4)., F7: 'Navigation mode (reach, accompany, follow) inferred from the request (p.4).'}
integration: I4
integration_rationale: FM outputs constraints/parameters (speed bound, social distance) and goal pose consumed by a CBF controller; CBF collision-avoidance constraints hold independently of the LLM.
evidence: E2
evidence_rationale: Gazebo closed-loop simulation (reach and follow-accompany use cases) plus an offline accuracy test of LLM parameter outputs on 100 requests (manually checked); no real robot, no human study.
inputs: [user request (text), 'user database (id, category, confidence, pose)', laser scan]
outputs: [navigation mode, robot maximum speed, social zone distance, goal pose]
human_repr: ['user pose (position, orientation)', asymmetric Gaussian social interaction space, user category and comfort state in structured text]
capabilities: {C1: Partial, C2: 'No', C3: Partial, C4: Partial, C5: 'No', C6: 'No', C7: Partial, C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: 'No', C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: Partial, C24: 'Yes', C25: 'No'}
exp:
  datasets: Not reported
  simulators: [Gazebo]
  robots: [simulated differential-drive robot]
  environment: indoor room with three static obstacles and a door
  indoor_outdoor: indoor
  sensors: [laser scan]
  humans: simulated users (positions assumed known)
  n_scenes: 1 scenario, 2 use cases
  n_trajectories: Not reported (example runs per use case)
  n_participants: NA
  split: 100 offline requests for the parameter-accuracy test
  baselines: None
  ablation: 'No'
  real_robot_trials: 'No'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [reach (two users), follow then accompany]
metrics: ['VLM | Navigation-mode accuracy | % | correct mode over 100 requests, manually checked | p.6', VLM | Max-speed accuracy | % | speed value compatible with the user context over 100 requests | p.6, VLM | Social-distance accuracy | % | social-zone distance compatible with the user comfort context over 100 requests | p.6]
deployment: {fm_model: 'llama3.1:8b; command-r7b', model_size: 8B; 7B, api_cloud_local: Local (Ollama), onboard_offboard: Not reported (simulation), gpu: Not reported, cpu: Not reported, latency: Not reported, query_frequency: per user request or context change, planner_frequency: Not reported, controller_frequency: 50 Hz (simulation), asynchronous: Yes (LLM per request; CBF control at 50 Hz), caching: Not reported, event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: Not reported, safety_shield: Yes (CBF collision-avoidance constraints independent of the LLM; LLM parameters bounded to predefined ranges), emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: Yes (structured function-calling outputs within empirically bounded ranges), real_time_claim_supported: 'No'}
repro: {code: Not reported, code_url: Not reported, dataset: NA, dataset_url: Not reported, checkpoints: Not reported, prompts_published: Yes (Table I), hardware_specified: Not reported, hyperparameters: Not reported, protocol_described: Partial, project_page: 'Video: doi 10.5281/zenodo.15075165', concerns: Not reported}
limitations_flags: [sim-only, no-human-study, no-latency]
web_verification_required: []
cited_missing: [SALM]
external_verification: {verified_on: '2026-10-26', status_class: 'A: published, peer-reviewed', source: IEEE Xplore record and DOI 10.1109/RO-MAN63969.2025.11217843, publication_status: Published (RO-MAN 2025), peer_reviewed_note: Proceedings paper; no arXiv version found}
stage2: {added: true, added_stage: final coverage search (2026-10-26), source_type: full text supplied by the authors (library access), relative_to_cai_cutoff: before Cai cut-off (27 Jun 2026), download_source: IEEE Xplore (Kumoh National Institute of Technology licence), inclusion_reason: 'Direct FM social navigation: LLM-derived social constraints (distance, speed, navigation mode) enforced by CBFs. Venue-only paper found by the final coverage search (IEEE Xplore and OpenAlex).'}
coding: {latency_reported: 'No', safety_mechanism: 'Yes', uncertainty_treatment: 'No', hallucination_treatment: 'Yes', code_released: 'No', new_dataset_released: NA, real_robot: 'No', human_subject_study: 'No'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A3, A5]
  C_capabilities: {SAF1: Partial, SAF2: 'No', SPA1: Partial, SPA2: 'No', SPA3: 'No', SPA4: 'No', HUM1: 'No', HUM2: Partial, NOR1: 'No', NOR2: Partial, NOR3: 'Yes', NOR4: 'No', EXP1: Partial, EXP2: 'No', EXP3: 'No'}
  B_roles: [R2, R3, R4]
  D_interface: [D3, D4]
  E_evidence_profile: {EV1_offline: 'Yes', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: none, EV4_real_humans_in_trials: simulated-only, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: Not reported (example runs per use case), statistical_testing: 'No', cross_environment: No/unclear, runtime_measured: 'No'}
  cross_cutting: {temporal_coupling: per-instruction, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'Yes', uncertainty: 'No', hallucination_mitigation: 'Yes', privacy_constraint: 'No', inference_location: local/onboard or local server}
physical_source_folder: "04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core"
analytical_category: "S4"
coding:
  latency_reported: "No"
  safety_mechanism: "Yes"
  uncertainty_treatment: "No"
  hallucination_treatment: "Yes"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "No"
  human_subject_study: "No"
---

# LLM social-cue architecture (Ruo et al., RO-MAN 2025)

Page convention: PDF index of the corpus copy (IEEE Xplore PDF, 7 pages).

## A. Bibliographic
IEEE RO-MAN 2025 (Eindhoven), pp. 1494-1500, DOI 10.1109/RO-MAN63969.2025.11217843. University of Modena and Reggio Emilia; Eurecat. Published, peer-reviewed. No arXiv version found.

## B. Position
S4 direct. Found by the final coverage search (2026-10-26). Meets A (mobile robot navigation in a Gazebo social environment), B (local LLMs choose navigation mode, speed and social distance) and C (proxemic distance and speed adapted to the user's comfort and age category; reach, follow and accompany behaviours).

## D. Method
High-level layer: an LLM with function calling receives the user request and user parameters (category, confidence, pose) and returns the navigation mode, the maximum speed (0.1-0.8 m/s) and the social-zone distance (1.0-1.4 m), using prompts listed in Table I (p.4). Low-level layer: a CBF quadratic program enforces collision avoidance, the speed bound and a field-of-view constraint; the social-zone distance sets the asymmetric Gaussian social space used to place the goal pose (p.4).

## G. Social capabilities
C24 Yes (context-dependent conduct: speed and distance chosen from user category and comfort, accuracy measured over 100 requests) · C3 Partial (asymmetric social space; distances plotted, no violation metric) · C1 Partial (CBF collision avoidance; no collision metric) · C4 Partial (comfort motivates the distance; not measured) · C7 Partial (navigation mode inferred from the request) · C23 Partial (requests such as "stay far" are followed; not separated in the evaluation) · others No.

## H/I. D3 (constraints and parameters) and D4 (goal pose); E2.

## L. Results
LLM output accuracy over 100 requests: navigation mode 87%, maximum speed 76%, social distance 85% (mean 82%). In simulation the CBF controller respected the LLM-set speed bounds and social distances in the reach and follow-accompany cases (velocity and distance plots).

## N. Limitations
Stated: simulation only; parameters inferred per request rather than continuously; no user study yet. Observable: no baselines; no collision or comfort metrics; user positions assumed known; no latency reported.

---
id: 2026_Oush_VLA-TurtleBot
source_pdfs: [04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/Oush_VLA-TurtleBot_ICCRE2026.pdf]
duplicate_copies: []
related_versions: [ICCRE 2026 proceedings version = corpus copy (no arXiv version found)]
title: Vision Language Action for TurtleBot Mobile Robot Path Planning
authors: [Noor Oush, Reza Alirezaee, Saeed Mozaffari, Shahpour Alirezaee]
year: 2026
venue: 2026 11th International Conference on Control and Robotics Engineering (ICCRE)
volume: NA
issue: NA
pages: 139-144
doi: 10.1109/ICCRE69951.2026.11593560
url: https://doi.org/10.1109/ICCRE69951.2026.11593560
pub_status: conference
peer_reviewed: 'Yes'
peer_review_basis: IEEE ICCRE 2026 proceedings, DOI 10.1109/ICCRE69951.2026.11593560 (IEEE Xplore record; full text read 2026-10-26).
category: S4
folder: 04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core
folder_category_match: 'Yes'
category_rationale: 'Human-aware navigation in Gazebo: YOLO detections and LiDAR distances are summarised into a scene state from which an LLM chooses a discrete navigation action (proceed, yield, avoid left/right, stop) when a human is detected; an LLM-independent LiDAR safety layer can override the action before a motion controller executes it.'
paper_type: method
fm_used: 'Yes'
fm_class: [LLM]
fm_models: [LLM (not named)]
fm_size: Not reported
method_family: [LLM discrete action selection, YOLO + LiDAR scene summary, deterministic safety override]
roles: [F1, F4, F10]
roles_evidence: {F1: YOLO and LiDAR outputs are abstracted into a scene/state summary for the LLM (p.2)., F4: 'The LLM decides whether to proceed, yield to a human or select an avoidance direction (p.3).', F10: The LLM output is a discrete navigation action mapped to velocities by a motion controller (p.3).}
integration: I7
integration_rationale: The FM selects a discrete navigation action that a motion controller executes directly (direct action, no intervening planner); an independent LiDAR safety layer validates and can override it.
evidence: E2
evidence_rationale: Gazebo simulation with a TurtleBot3 Waffle, static and moving simulated human agents; no real robot, no human study.
inputs: [RGB camera (YOLO detections), 2D LiDAR, navigation goal]
outputs: ['discrete navigation action (proceed, yield, avoid left/right, stop)']
human_repr: [detected human (YOLO class and position), LiDAR distance/free space, structured scene/state summary]
capabilities: {C1: Partial, C2: 'Yes', C3: 'No', C4: 'No', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: Partial, C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: 'No', C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: 'No', C24: 'No', C25: 'No'}
exp:
  datasets: Not reported
  simulators: [Gazebo]
  robots: [TurtleBot3 Waffle (simulated)]
  environment: indoor rooms with furniture
  indoor_outdoor: indoor
  sensors: [RGB camera, 2D LiDAR]
  humans: simulated human agent (static, crossing, dangerous proximity)
  n_scenes: 4 scenarios
  n_trajectories: Not reported
  n_participants: NA
  split: NA
  baselines: [LiDAR only, Vision + LiDAR, Vision + LLM (no safety layer)]
  ablation: Yes (module combinations)
  real_robot_trials: 'No'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [no human, static human, crossing human, human within the safety threshold]
metrics: [NAV | Goal completion rate | % | goals reached per scenario | p.4, NAV | Average time | s | mean time to reach the goal | p.4, SAFETY | Minimum distance to obstacles | m | minimum separation from obstacles and the human agent | p.4, OTHER | Oscillation | qualitative (low/moderate/high) | observed oscillatory motion | p.4, SAFETY | Safety-override frequency | qualitative (low/high) | activations of the LiDAR safety override | p.3]
deployment: {fm_model: Not reported, model_size: Not reported, api_cloud_local: Not reported, onboard_offboard: External computer (ROS 2 Humble), gpu: Not reported, cpu: Not reported, latency: Not reported numerically (LLM delay discussed), query_frequency: on human detection or blocked free space, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Not reported, caching: Not reported, event_triggered: 'Yes', distillation: Not reported, quantization: Not reported, fallback_planner: Not reported, safety_shield: Yes (deterministic LiDAR safety layer validates and overrides LLM actions), emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: Yes (outputs restricted to a discrete action set and validated by the safety layer), real_time_claim_supported: 'No'}
repro: {code: Not reported, code_url: Not reported, dataset: NA, dataset_url: Not reported, checkpoints: Not reported, prompts_published: 'No', hardware_specified: Not reported, hyperparameters: Not reported, protocol_described: Partial, project_page: Not reported, concerns: Not reported}
limitations_flags: [sim-only, no-human-study, fm-unnamed, no-latency]
web_verification_required: []
cited_missing: []
external_verification: {verified_on: '2026-10-26', status_class: 'A: published, peer-reviewed', source: IEEE Xplore record and DOI 10.1109/ICCRE69951.2026.11593560, publication_status: Published (ICCRE 2026), peer_reviewed_note: Proceedings paper; no arXiv version found}
stage2: {added: true, added_stage: final coverage search (2026-10-26), source_type: full text supplied by the authors (library access), relative_to_cai_cutoff: before Cai cut-off (27 Jun 2026), download_source: IEEE Xplore (Kumoh National Institute of Technology licence), inclusion_reason: Direct FM human-aware navigation (LLM chooses yield/avoid/stop actions around humans behind an independent safety layer). Found by the final coverage search (IEEE Xplore).}
coding: {latency_reported: Partial, safety_mechanism: 'Yes', uncertainty_treatment: 'No', hallucination_treatment: 'Yes', code_released: 'No', new_dataset_released: NA, real_robot: 'No', human_subject_study: 'No'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A5]
  C_capabilities: {SAF1: Partial, SAF2: 'Yes', SPA1: 'No', SPA2: 'No', SPA3: Partial, SPA4: 'No', HUM1: 'No', HUM2: 'No', NOR1: 'No', NOR2: 'No', NOR3: 'No', NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: [R1, R3]
  D_interface: [D6]
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: none, EV4_real_humans_in_trials: simulated-only, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: Not reported, statistical_testing: 'No', cross_environment: No/unclear, runtime_measured: Partial}
  cross_cutting: {temporal_coupling: event-triggered, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'Yes', uncertainty: 'No', hallucination_mitigation: 'Yes', privacy_constraint: 'No', inference_location: not reported}
physical_source_folder: "04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core"
analytical_category: "S4"
coding:
  latency_reported: "Partial"
  safety_mechanism: "Yes"
  uncertainty_treatment: "No"
  hallucination_treatment: "Yes"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "No"
  human_subject_study: "No"
---

# VLA for TurtleBot path planning (Oush et al., ICCRE 2026)

Page convention: PDF index of the corpus copy (IEEE Xplore PDF, 6 pages).

## A. Bibliographic
ICCRE 2026, pp. 139-144, DOI 10.1109/ICCRE69951.2026.11593560. University of Windsor. Published, peer-reviewed. No arXiv version found.

## B. Position
S4 direct. Found by the final coverage search (2026-10-26). Meets A (TurtleBot3 navigation in Gazebo), B (an LLM decides the navigation action) and C (human-aware navigation: yielding to and keeping distance from a detected person). Borderline on C: the targeted behaviour is mainly safe avoidance and yielding around a single person.

## D. Method
YOLO detections, LiDAR distances and the goal form a scene/state summary (p.2). On human detection or blocked free space, an LLM (not named) returns a discrete action (proceed, yield, avoid left, stop). A deterministic LiDAR safety layer validates the action and overrides it with a stop below a distance threshold; a motion controller converts the action into velocities on /cmd_vel (p.3).

## G. Social capabilities
C2 Yes (minimum separation from the human agent and obstacles reported per scenario) · C1 Partial (collision avoidance; no collision count) · C12 Partial (yielding action) · others No.

## H/I. D6 (direct action from a discrete set, executed by the motion controller, behind an FM-independent safety layer); E2.

## L. Results
Goal completion 100% in all scenarios; mean time 45 s with a static and 50 s with a moving human; minimum distance 1 m and 0.4 m; oscillation moderate to high. Ablation: LiDAR only 28 s; Vision + LLM without the safety layer 50 s with low override frequency; full system 40 s with frequent overrides.

## N. Limitations
Stated: simulation only; oscillations under symmetric free space; YOLO misses fall back to LiDAR control; LLM latency. Observable: LLM unnamed; no social or comfort metrics; single simulated person; no statistics.

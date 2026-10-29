---
id: 2026_Huo_NORM-Nav
source_pdfs: [04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/NORM-Nav_arXiv2605.16979v1.pdf]
duplicate_copies: []
related_versions: ['arXiv:2605.16979v1 (16 May 2026) = corpus copy; published version ICRA 2026']
title: 'NORM-Nav: Zero-Shot Mobile Robot Navigation with Natural Language Behavioral Constraints'
authors: [Dongjie Huo, Junhui Wang, Chao Gao, Yan Qiao, Dong Zhang, Guyue Zhou]
year: 2026
venue: 2026 IEEE International Conference on Robotics and Automation (ICRA)
volume: NA
issue: NA
pages: 1139-1146
doi: 10.1109/ICRA57385.2026.11696526
url: https://doi.org/10.1109/ICRA57385.2026.11696526
pub_status: conference (corpus copy is arXiv author version)
peer_reviewed: 'Yes'
peer_review_basis: 'Crossref record: ICRA 2026, pp. 1139-1146, DOI 10.1109/ICRA57385.2026.11696526 (verified 2026-10-19). arXiv v1 posted 16 May 2026.'
category: S4
folder: 04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core
folder_category_match: 'Yes'
category_rationale: LLM parses natural-language behavioural norms ("keep right", "pass pedestrians on the left", "slow down near vehicles") into structured constraints grounded by open-vocabulary perception and encoded as multi-layer costmaps. Social element is convention compliance; pedestrian-directed behaviour is shown only qualitatively (borderline direct; included for consistency with BehAV).
paper_type: method
fm_used: 'Yes'
fm_class: [VLM/LLM, open-vocabulary segmentation]
fm_models: [Qwen-VL-Max (instruction parsing), Grounded-SAM 2 (open-vocabulary grounding)]
fm_size: Not reported (API)
method_family: [zero-shot prompting, structured constraint parsing, camera-LiDAR fusion, multi-layer costmaps, A* + TEB]
roles: [F1, F4, F6]
roles_evidence: {F1: 'GSAM2 grounds referenced objects (pedestrian, vehicle, grass, crosswalk) in RGB, fused with LiDAR (p.3).', F4: 'LLM converts behavioural norms into (object, direction, velocity, traversability) tuples (p.3).', F6: 'Constraints encoded as semantic, directional and velocity costmap layers (p.3).'}
integration: I4
integration_rationale: LLM output becomes costmap layers consumed by standard A*/TEB planners; velocity layer caps local-planner speed (p.5).
evidence: E2
evidence_rationale: Quantitative evaluation in simulation (OpenBench MEDIUM; SR in 10% steps, trial count not stated); real-world SCOUT 2.0 runs are qualitative demonstrations only (p.7).
inputs: [natural-language behavioural constraints, RGB-D, 3D LiDAR]
outputs: [structured constraints, multi-layer costmap, speed limit]
human_repr: [pedestrian as grounded semantic object with bounding box]
capabilities: {C1: Partial, C2: 'No', C3: 'No', C4: 'No', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: Partial, C12: 'No', C13: Partial, C14: 'No', C15: 'Yes', C16: 'No', C17: 'No', C18: 'No', C19: 'No', C20: Partial, C21: 'No', C22: 'No', C23: 'Yes', C24: Partial, C25: 'No'}
exp:
  datasets: []
  simulators: [OpenBench MEDIUM environment]
  robots: [simulated 4-wheel differential robot, 'AgileX SCOUT 2.0 (real, demonstrations)']
  environment: outdoor campus/road scenes
  indoor_outdoor: outdoor
  sensors: [Livox MID-360 LiDAR, RealSense D455 RGB-D]
  humans: pedestrians appear in real-world demonstrations only
  n_scenes: 4 task categories
  n_trajectories: Not reported (success in 10% increments)
  n_participants: NA
  split: NA
  baselines: [BehAV, InstructNav, Interactive Navigation Framework (INF)]
  ablation: Yes (interpolation parameter alpha)
  real_robot_trials: Partial (qualitative demonstrations)
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [region following, region avoidance, traversable obstacle, combined, speed constraints]
metrics: [NAV | Success Rate | % | reaches goal while fully respecting all behavioural constraints | p.6, NAV | SPL | % | success weighted by path length | p.6, OTHER | Frechet Distance | m | similarity to a human tele-operated reference path | p.6, SOCIAL | Behavioral Following Accuracy (BFA) | % | fraction of trajectory length consistent with the behavioural constraints | p.6]
deployment: {fm_model: Qwen-VL-Max, model_size: Not reported, api_cloud_local: Cloud API (parsing), onboard_offboard: 'Onboard planning (AMD R9-7945HX, RTX 4060)', gpu: RTX 4060 (onboard), cpu: Not reported, latency: Not reported, query_frequency: Per instruction (offline + online constraint sets), planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Not reported, caching: Not reported, event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: Geometric traversability layer and A*/TEB, safety_shield: Geometric obstacle layer (cost 255) always preserved in fusion (Eq.17), emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: Output restricted to enumerated tuple values (Table I) and grounded through perception, real_time_claim_supported: Not reported}
repro: {code: Not reported, code_url: Not reported, dataset: Not reported, dataset_url: Not reported, checkpoints: Not reported, prompts_published: Not reported, hardware_specified: 'Yes', hyperparameters: 'Partial (alpha, cost bounds, resolution)', protocol_described: Not reported, project_page: 'https://ei-nav.github.io/NORM-Nav', concerns: Number of simulated trials not stated; pedestrian-directed social behaviour only demonstrated qualitatively.}
limitations_flags: [cloud-dependence, limited-scenarios, no-human-study]
web_verification_required: []
cited_missing: [OpenBench, InstructNav, Interactive navigation with LLM/VLM (Zhang 2024)]
external_verification: {verified_on: '2026-10-19', status_class: 'A: published, peer-reviewed', source: Crossref DOI 10.1109/ICRA57385.2026.11696526, arxiv_id: 2605.16979v1}
stage2: {added: true, download_source: 'https://arxiv.org/pdf/2605.16979v1', source_type: arXiv (author version), inclusion_reason: 'Direct (norm/convention-aware navigation via LLM costmaps); peer-reviewed; arXiv posted before Cai cut-off (May 2026), not cited by Cai. Borderline social scope flagged.'}
coding: {latency_reported: 'No', safety_mechanism: 'Yes', uncertainty_treatment: 'No', hallucination_treatment: 'Yes', code_released: 'No', new_dataset_released: NA, real_robot: Demo, human_subject_study: 'No'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A3, A5]
  C_capabilities: {SAF1: Partial, SAF2: 'No', SPA1: 'No', SPA2: 'No', SPA3: 'Yes', SPA4: 'No', HUM1: 'No', HUM2: 'No', NOR1: Partial, NOR2: 'Yes', NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: Partial}
  B_roles: [R1, R4]
  D_interface: [D3]
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: demo, EV4_real_humans_in_trials: present-type-unreported, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: Not reported (success in 10% increments), statistical_testing: 'No', cross_environment: No/unclear, runtime_measured: 'No'}
  cross_cutting: {temporal_coupling: per-instruction, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'Yes', uncertainty: 'No', hallucination_mitigation: 'Yes', privacy_constraint: 'No', inference_location: cloud API}
physical_source_folder: "04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core"
analytical_category: "S4"
coding:
  latency_reported: "No"
  safety_mechanism: "Yes"
  uncertainty_treatment: "No"
  hallucination_treatment: "Yes"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "Demo"
  human_subject_study: "No"
---

# NORM-Nav (Huo et al., ICRA 2026)

Page convention: PDF index of the corpus copy (arXiv v1).

## A. Bibliographic
ICRA 2026, pp. 1139-1146, DOI 10.1109/ICRA57385.2026.11696526 (Crossref-verified 2026-10-19). Corpus copy arXiv:2605.16979v1. Peer-reviewed: Yes.

## B. Position
S4 direct, **borderline**: the social capability is compliance with locally expected behavioural conventions (keep right, pass on a specified side, slow down near vulnerable road users). Most evaluated constraints refer to regions and objects (grass, crosswalks, cars, curtains); pedestrian-directed behaviour appears only in real-world demonstrations. Retained as direct for consistency with BehAV (rule-guided costmaps, S4 in Stage 1).

## C. Research problem
Costmap navigation ignores behavioural conventions; learning-based language navigation needs data and generalises poorly (p.1).

## D. Method
LLM (Qwen-VL-Max) parses offline + online instructions into tuples (O, d, v, t); GSAM2 + LiDAR projection and DBSCAN build object boxes; four layers (geometric, semantic traversability, directional with power-law interpolation, velocity) fused into spatial and kinematic costmaps; A* global + TEB local.

## G. Social capabilities
C15 Yes (keep-to-side / crosswalk rules evaluated via SR/BFA) · C23 Yes (instruction compliance) · C11, C13 Partial (conventions; bypass pedestrians from instructed side shown qualitatively) · C1 Partial (collision-free statements) · C20 Partial (Frechet distance to human reference) · C24 Partial · others No.

## H/I. I4; E2 (real robot = demonstration only).

## L. Results (Table III)
Combined task: SR 90% vs BehAV 30%, InstructNav 20%; BFA 85% vs 39%/36%; FD 3.01 vs 7.02/6.45. Traversable-obstacle task: SR 80% vs INF 70%.

## N. Limitations
Observable: trial counts not stated; no human evaluation; social behaviour towards people not quantified; LLM latency not reported.

## P. Direct-paper questions (abridged)
1 Norm/convention-compliant navigation from language. 3 Qwen-VL-Max, GSAM2. 6 Structured constraint tuples. 7 Costmap layers. 10 Geometric layer preserved. 23 Real robot demonstration only. 24 No human study.

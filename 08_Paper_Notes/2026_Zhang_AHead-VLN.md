---
id: 2026_Zhang_AHead-VLN
source_pdfs: [04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/AHead-VLN_IJCAI2026_0696.pdf]
duplicate_copies: []
related_versions: [IJCAI 2026 proceedings version = corpus copy (no arXiv version found)]
title: 'AHead-VLN: A Hierarchical Reasoning Framework Guided by Foresight for Human-Aware Navigation'
authors: [Junyi Zhang, Ziwen Luo, Yinzhe Zhou, Xinghe Chu, Zhaoming Lu]
year: 2026
venue: Proceedings of the Thirty-Fifth International Joint Conference on Artificial Intelligence (IJCAI)
volume: NA
issue: NA
pages: 6254-6262
doi: 10.24963/ijcai.2026/696
url: https://doi.org/10.24963/ijcai.2026/696
pub_status: conference
peer_reviewed: 'Yes'
peer_review_basis: IJCAI 2026 proceedings, pp. 6254-6262, DOI 10.24963/ijcai.2026/696 (publisher record verified in Stage 7; full text read in Stage 9).
category: S4
folder: 04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core
folder_category_match: 'Yes'
category_rationale: 'Human-aware VLN in continuous environments: a "Brain" LLM selects among geometrically feasible candidate paths using structured, partly templated-language risk events derived from forecast occupancy of people, and a "Cerebellum" LLM writes discrete action scripts (including waiting) for each candidate; evaluated on the HA-VLN benchmark with human-collision metrics.'
paper_type: method
fm_used: 'Yes'
fm_class: [LLM/VLM]
fm_models: [gpt-4o-2024-05-13 (Brain), gpt-3.5-turbo (Cerebellum)]
fm_size: Not reported (proprietary API models)
method_family: [hierarchical LLM planner, candidate-path selection, spatio-temporal occupancy forecasting, neural-to-symbolic risk compilation]
roles: [F4, F7, F10]
roles_evidence: {F4: Brain LLM trades off instruction progress against predicted risk and chooses the path (p.5)., F7: Brain LLM grounds the route instruction in candidate paths (p.5)., F10: 'Cerebellum LLM writes action scripts from a predefined discrete action space, including waiting and detouring (p.5).'}
integration: I7
integration_rationale: The FM selects among planner-proposed candidate paths (candidate selection) and its action script from a discrete primitive set is executed directly (direct action); no FM-independent filter on the executed actions.
evidence: E2
evidence_rationale: Closed-loop simulation only (HA-VLN simulator, HA-R2R instructions; 90 scans, 216 evaluation trajectories); no real robot, no human study.
inputs: [panoramic RGB-D, language instruction]
outputs: [selected path index, discrete action script]
human_repr: [forecast spatio-temporal occupancy of dynamic entities, structured risk events with templated language descriptions, implicit (vision)]
capabilities: {C1: 'Yes', C2: 'No', C3: 'No', C4: 'No', C5: 'No', C6: 'Yes', C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: Partial, C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: Partial, C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: 'No', C24: 'No', C25: 'No'}
exp:
  datasets: [HA-R2R (HA-VLN)]
  simulators: [HA-VLN simulator]
  robots: [simulated agent]
  environment: Not reported
  indoor_outdoor: indoor
  sensors: Not reported
  humans: simulated human models (910 human models, 428 regions across 90 scans)
  n_scenes: 90 scans
  n_trajectories: 216 evaluation trajectories
  n_participants: Not reported
  split: zero-shot evaluation subset
  baselines: ['HA-VLN-CMA (Base, DA, *)', HA-VLN-VL, ETPNav, BEVBert]
  ablation: Yes (w/o PRA; serial scripts; w/o Cerebellum; both removed)
  real_robot_trials: 'No'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: Not reported
metrics: [NAV | NE | m | navigation error | p.6, SAFETY | TCR | collisions/episode | total collision rate with pedestrians | p.6, SAFETY | CR | % episodes | episodes with at least one collision | p.6, NAV | SR | % | within 3 m of the goal and no collision in the episode | p.6]
deployment: {fm_model: gpt-4o-2024-05-13 and gpt-3.5-turbo, model_size: Not reported, api_cloud_local: Cloud API, onboard_offboard: Simulation (API calls), gpu: two NVIDIA A100 (training of the risk module), cpu: Not reported, latency: Not reported numerically (parallel scripting claimed to reduce latency), query_frequency: Not reported, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: No (parallel script generation per decision), caching: Not reported, event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: Not reported, safety_shield: No (executed actions come from the LLM script), emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: 'Yes (structural: path index chosen among candidates; actions restricted to a predefined discrete action set)', real_time_claim_supported: 'No'}
repro: {code: Not reported, code_url: Not reported, dataset: Not reported, dataset_url: Not reported, checkpoints: Not reported, prompts_published: Partial (prompt structure in Fig. 3), hardware_specified: Not reported, hyperparameters: Not reported, protocol_described: Not reported, project_page: Not reported, concerns: Not reported}
limitations_flags: [sim-only, no-human-study, cloud-dependency]
web_verification_required: []
cited_missing: [HA-VLN 2.0, NavGPT, MapGPT, DiscussNav]
external_verification: {verified_on: '2026-10-20', status_class: 'A: published, peer-reviewed', source: IJCAI 2026 proceedings page and DOI 10.24963/ijcai.2026/696, publication_status: Published (IJCAI 2026), peer_reviewed_note: Proceedings paper; no arXiv version found}
stage2: {added: true, download_source: 'https://www.ijcai.org/proceedings/2026/0696.pdf', source_type: publisher open access, inclusion_reason: Direct FM human-aware navigation with human-collision metrics. Venue-only paper found in the Stage-7 final check outside the arXiv-centred search; coded in Stage 9., relative_to_cai_cutoff: after Cai cut-off (27 Jun 2026)}
coding: {latency_reported: 'No', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: 'Yes', code_released: 'No', new_dataset_released: NA, real_robot: 'No', human_subject_study: 'No'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A2, A5, A6]
  C_capabilities: {SAF1: 'Yes', SAF2: 'No', SPA1: 'No', SPA2: 'No', SPA3: Partial, SPA4: Partial, HUM1: Partial, HUM2: 'No', NOR1: 'No', NOR2: 'No', NOR3: 'No', NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: [R1, R3, R4]
  D_interface: [D2, D6]
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: none, EV4_real_humans_in_trials: simulated-only, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: 216 evaluation trajectories, statistical_testing: 'No', cross_environment: No/unclear, runtime_measured: 'No'}
  cross_cutting: {temporal_coupling: per-decision, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'No', uncertainty: 'No', hallucination_mitigation: 'Yes', privacy_constraint: 'No', inference_location: cloud API}
physical_source_folder: "04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core"
analytical_category: "S4"
coding:
  latency_reported: "No"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "Yes"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "No"
  human_subject_study: "No"
---

# AHead-VLN (Zhang et al., IJCAI 2026)

Page convention: PDF index of the corpus copy (IJCAI proceedings PDF, 9 pages).

## A. Bibliographic
IJCAI 2026, pp. 6254-6262, DOI 10.24963/ijcai.2026/696. Beijing University of Posts and Telecommunications. Publication status: published, peer-reviewed. No arXiv version found.

## B. Position
S4 direct. Found in the Stage-7 final check as a venue-only paper outside the arXiv-centred search; coded in Stage 9. Meets A (VLN in continuous environments among moving people), B (GPT-4o and GPT-3.5 make route and action decisions) and C (human-collision avoidance among pedestrians, waiting and yielding at bottlenecks).

## D. Method
A waypoint predictor proposes candidate paths; a spatio-temporal occupancy forecaster (KPConv/BEV, fine-tuned in HA-VLN) predicts future occupancy of static, movable and dynamic entities. The path-risk association module compiles the forecast into a per-path tactical summary and risk events (time window, path segment, templated description) (p.4). The Brain LLM chooses a path index; Cerebellum LLMs write action scripts from a discrete action set for every candidate in parallel, and the script of the chosen path is executed (p.5).

## G. Social capabilities
C1 Yes (TCR and CR count collisions with pedestrians) · C6 Yes (ablation removing the risk module that carries the forecast raises TCR from 3.89 to 23.12) · C12 Partial (waiting at a narrow passage to avoid deadlock, Fig. 1) · C17 Partial (populated HA-VLN scenes; crowd navigation not measured as such) · others No. Personal space and yielding conventions are named in the motivation but not measured.

## H/I. I7 (candidate selection + direct action); E2.

## L. Results
Zero-shot on HA-R2R: NE 5.68, TCR 3.89, CR 0.44, SR 0.17 (best SR among the compared methods; best zero-shot baseline SR 0.15). Ablation: w/o PRA SR 0.06, TCR 23.12; serial scripts SR 0.12; w/o Cerebellum SR 0.14.

## N. Limitations
Stated: risk misestimation in occluded layouts; ambiguous instruction grounding and imperfect action timing; real-world deployment left to future work. Observable: simulation only; low absolute success (17%); collision in 44% of episodes; proprietary cloud models; no FM-independent safety layer on executed actions; no latency figures.

---
id: 2026_Gandotra_RBTLR
source_pdfs: [05_Direct_VLM_SocialNav_Preprints/Gandotra_RBTLR_HRIcompanion2026.pdf]
duplicate_copies: []
related_versions: [HRI 2026 companion proceedings version = corpus copy (no arXiv version found)]
title: 'RBTLR: A Framework for Safe Social Robot Navigation in Novel Human-Centric Environments'
authors: [Nayesha Gandotra]
year: 2026
venue: Companion Proceedings of the 21st ACM/IEEE International Conference on Human-Robot Interaction (HRI Companion '26)
volume: NA
issue: NA
pages: 461-465
doi: 10.1145/3776734.3794437
url: https://doi.org/10.1145/3776734.3794437
pub_status: conference (companion proceedings)
peer_reviewed: Not established
peer_review_basis: Published in the HRI 2026 companion proceedings (ACM, DOI 10.1145/3776734.3794437); the track and its review procedure are not stated in the paper.
category: S5
folder: 05_Direct_VLM_SocialNav_Preprints
folder_category_match: Partial
category_rationale: 'Early-stage social-navigation pipeline: CLIP video/text embeddings of the social scene (with Qwen-VLM captions) condition a learned selector that ranks collision-free RRT-Connect candidate paths; an LLM assigns goals and asks users to resolve ambiguities. Placed in S5 because peer review of the companion track is not established.'
paper_type: method (early results)
fm_used: 'Yes'
fm_class: [VLM (contrastive), VLM, LLM]
fm_models: [CLIP ViT-B/32, Qwen VLM (version not reported), LLM (not named)]
fm_size: Not reported
method_family: [candidate path selection, CLIP social-context embedding, LLM goal assignment]
roles: [F1, F5, F7]
roles_evidence: {F1: 'Social Context Module: CLIP frame embeddings and Qwen captions of a 1-s video window (p.2).', F5: Selector scores candidate trajectories for social appropriateness from scene embeddings (p.3)., F7: LLM parses commands into goal coordinates and resolves ambiguous targets with the user (p.1).}
integration: I6
integration_rationale: FM embeddings condition a learned (non-FM) trajectory selector at runtime (as in OLiVia-Nav); an LLM specifies goals and queries users for clarification.
evidence: E2
evidence_rationale: Simulated restaurant demonstration with projected human detections; only the selection-cycle time is reported; no quantitative social evaluation, no real robot, no human study.
inputs: [egocentric RGB video (8 frames), candidate trajectories, natural-language command]
outputs: [selected trajectory, goal coordinates, clarification question]
human_repr: [human positions from YOLOv8 detections, CLIP video embedding (implicit), scene captions encoded as text embeddings]
capabilities: {C1: Partial, C2: 'No', C3: Partial, C4: 'No', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: Partial, C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: 'No', C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: Partial, C24: Partial, C25: 'No'}
exp:
  datasets: [NavWareSet (training of the selector and temporal aggregation)]
  simulators: [simulated restaurant environment (MoveIt planning)]
  robots: [simulated UR10e-based robot]
  environment: restaurant
  indoor_outdoor: indoor
  sensors: [RGB camera]
  humans: human positions projected from detections
  n_scenes: '1'
  n_trajectories: Not reported
  n_participants: NA
  split: NA
  baselines: None
  ablation: 'No'
  real_robot_trials: 'No'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [goal ambiguity resolution (water station)]
metrics: [DEPLOY | Selection cycle time | s | full trajectory-selection cycle incl. embedding recall and inference (about 0.33 s) | p.4]
deployment: {fm_model: CLIP ViT-B/32; Qwen VLM; LLM (not named), model_size: Not reported, api_cloud_local: Not reported, onboard_offboard: Not reported (simulation), gpu: Not reported, cpu: Not reported, latency: 0.33 s per selection cycle, query_frequency: per replanning cycle, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: 'No', caching: Not reported, event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: Not reported, safety_shield: Yes (candidates are collision-free RRT-Connect paths), emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: No (caption hallucination named as a risk; mitigation left to future work), real_time_claim_supported: Partial}
repro: {code: Not reported, code_url: Not reported, dataset: NA, dataset_url: Not reported, checkpoints: Not reported, prompts_published: 'No', hardware_specified: Not reported, hyperparameters: Not reported, protocol_described: Partial, project_page: Demonstration videos (Google Drive link), concerns: Not reported}
limitations_flags: [sim-only, no-human-study, early-stage]
web_verification_required: []
cited_missing: [NavWareSet]
external_verification: {verified_on: '2026-10-26', status_class: 'D: conference paper; acceptance verified, peer review not established', source: ACM DL record and DOI 10.1145/3776734.3794437, publication_status: Published (HRI 2026 companion proceedings), peer_reviewed_note: Companion track; review procedure not stated}
stage2: {added: true, added_stage: final coverage search (2026-10-26), source_type: full text supplied by the authors (library access), relative_to_cai_cutoff: before Cai cut-off (27 Jun 2026), download_source: 'ACM Digital Library (open access, CC BY-NC-ND)', inclusion_reason: Direct FM social navigation (FM social context conditions path selection; LLM goal assignment). Found by the final coverage search (OpenAlex).}
coding: {latency_reported: 'Yes', safety_mechanism: 'Yes', uncertainty_treatment: 'No', hallucination_treatment: 'No', code_released: 'No', new_dataset_released: NA, real_robot: 'No', human_subject_study: 'No'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A5, A6]
  C_capabilities: {SAF1: Partial, SAF2: 'No', SPA1: Partial, SPA2: 'No', SPA3: Partial, SPA4: 'No', HUM1: 'No', HUM2: 'No', NOR1: 'No', NOR2: Partial, NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: [R1, R4, R5]
  D_interface: [D5, D4, D8]
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: none, EV4_real_humans_in_trials: simulated-only, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: Not reported, statistical_testing: 'No', cross_environment: No/unclear, runtime_measured: 'Yes'}
  cross_cutting: {temporal_coupling: per-decision, memory: 'No', continual_adaptation: 'No', explanation_output: Yes (human-facing), safety_guard: 'Yes', uncertainty: 'No', hallucination_mitigation: 'No', privacy_constraint: 'No', inference_location: not reported}
physical_source_folder: "05_Direct_VLM_SocialNav_Preprints"
analytical_category: "S5"
coding:
  latency_reported: "Yes"
  safety_mechanism: "Yes"
  uncertainty_treatment: "No"
  hallucination_treatment: "No"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "No"
  human_subject_study: "No"
---

# RBTLR (Gandotra, HRI 2026 companion)

Page convention: PDF index of the corpus copy (ACM PDF, 5 pages).

## A. Bibliographic
Companion Proceedings of HRI 2026 (Edinburgh), pp. 461-465, DOI 10.1145/3776734.3794437. Carnegie Mellon University. Status class D: published in companion proceedings; peer-review procedure of the track not established. No arXiv version found.

## B. Position
S5 direct. Found by the final coverage search (2026-10-26). Meets A (robot path selection in a simulated restaurant), B (CLIP and Qwen-VLM social context; LLM goal assignment) and C (selection of socially appropriate paths: personal space, yielding). Early-stage: architecture and demonstration only.

## D. Method
RRT-Connect (MoveIt) proposes collision-free candidate paths; a Social Context Module extends OLiVia-Nav's SC-CLIP with an LSTM over CLIP embeddings of a 1-s video window and Qwen captions encoded with CLIP's text encoder (p.2); a cross-attention selector trained with a ranking loss on NavWareSet scores each candidate (p.4); an LLM assigns goals from commands and asks the user to resolve ambiguous targets (p.1).

## G. Social capabilities
C3 Partial (personal space named as the selection target) · C12 Partial (yielding) · C1 Partial (collision-free candidates) · C23 Partial (real-time user feedback such as "you were too close" proposed) · C24 Partial (restaurant context) · others No. No social metric is reported.

## H/I. D5 (FM embeddings condition the learned selector), D4 (LLM goal assignment), D8 (clarification dialogue); E2.

## L. Results
Qualitative demonstration in a simulated restaurant; selection cycle about 0.33 s.

## N. Limitations
Stated: early results; VLM caption hallucinations can mislead the selector; quantitative safety and social metrics and physical-robot trials left to future work. Observable: no baselines, no social evaluation, LLM not named.

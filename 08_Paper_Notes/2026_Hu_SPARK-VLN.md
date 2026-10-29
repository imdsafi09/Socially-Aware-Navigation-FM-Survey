---
id: 2026_Hu_SPARK-VLN
source_pdfs: [05_Direct_VLM_SocialNav_Preprints/SPARK-VLN_arXiv2607.16806v1.pdf]
duplicate_copies: []
related_versions: ['arXiv:2607.16806v1 (18 Jul 2026) = corpus copy']
title: Token-Wise Latent Streaming from Slow Reasoners to Fast Planners for Dynamic Vision Language Navigation
authors: [Tianshuai Hu, Yangyi Zhong, Zeying Gong, Lingdong Kong, Xiaodong Mei, Guoyang Zhao, Xiaolu Liu, Song Wang, Rong Li, Junwei Liang]
year: 2026
venue: arXiv preprint (arXiv:2607.16806v1)
volume: NA
issue: NA
pages: NA
doi: Not found / not applicable
url: https://arxiv.org/abs/2607.16806
pub_status: preprint
peer_reviewed: 'No'
peer_review_basis: arXiv 2607.16806v1 only (posted 2026-07-18; no comment or journal_ref). No verified peer-reviewed version found as of corpus freeze date (2026-10-19) via Crossref title search.
category: S5
folder: 05_Direct_VLM_SocialNav_Preprints
folder_category_match: 'Yes'
category_rationale: 'Dual-system dynamic social VLN: a slow VLM reasoner (VILA-based, 8B) streams token-wise hidden states to a fast flow-matching planner so that the planner acts on fresh guidance while pedestrians keep moving; new asynchronous benchmark with personal-space compliance, human-collision and distance-to-pedestrian metrics.'
paper_type: method + benchmark
fm_used: 'Yes'
fm_class: [VLM]
fm_models: [VILA-based VLM reasoner (8B)]
fm_size: 8B
method_family: [dual-system (slow VLM / fast planner), token-wise hidden-state streaming, flow-matching trajectory planner, asynchronous benchmark]
roles: [F1, F7]
roles_evidence: {F1: VLM hidden states encode directional intent and pedestrian context (p.2)., F7: VLM interprets the instruction and provides evolving high-level guidance to the planner.}
integration: I6
integration_rationale: Streamed VLM latents condition a learned flow-matching planner at runtime through a learned bridge/conditioner (same coding as HUMA); the FM does not output actions directly.
evidence: E2
evidence_rationale: Closed-loop simulation only (indoor scenes with ORCA pedestrians, idealized and realistic asynchronous modes); no real robot, no human study.
inputs: [egocentric RGB, language instruction]
outputs: [streamed latent guidance, trajectory (fast planner)]
human_repr: [implicit (vision); ORCA pedestrians in simulation]
capabilities: {C1: 'Yes', C2: 'No', C3: 'Yes', C4: 'No', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: Partial, C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: Partial, C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: Partial, C24: 'No', C25: 'No'}
exp:
  datasets: Not reported
  simulators: [custom dynamic social VLN benchmark (indoor scenes; ORCA pedestrians)]
  robots: [simulated agent]
  environment: Not reported
  indoor_outdoor: indoor
  sensors: Not reported
  humans: simulated ORCA pedestrians (density scaled to area)
  n_scenes: diverse indoor scenes (bedroom, office, hall, corridor)
  n_trajectories: Not reported in text read
  n_participants: Not reported
  split: Not reported
  baselines: [Seq2Seq, CMA, NaVid, Uni-NaVid, NaVILA, DualVLN, NavDP (PointNav)]
  ablation: Yes (stream vs wait-then-act; bridge design)
  real_robot_trials: 'No'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [frontal approach, intersection, following, corner]
metrics: ['NAV | SR / NE / SPL | % / m / % | success, navigation error, success weighted by path length | p.6', SOCIAL | PSC | % | personal space compliance | p.6, SAFETY | Col | % | human collision rate | p.6, SOCIAL | AvgD | m | average distance to nearest pedestrian | p.6, 'DEPLOY | Lat. / Disp. | s / m | per-inference latency and pedestrian displacement during inference (RTX 4090): stream 0.185 s avg | p.9']
deployment: {fm_model: VILA-based 8B VLM, model_size: 8B, api_cloud_local: Local, onboard_offboard: Simulation (RTX 4090), gpu: RTX 4090, cpu: Not reported, latency: 0.185 s average (max 1.030 s) per inference with streaming vs 0.788 s wait-then-act, query_frequency: Not reported, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: 'Yes (dual-system, streaming)', caching: Not reported, event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: Not reported, safety_shield: No (learned planner), emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: 'No', real_time_claim_supported: Partial (simulation latency only)}
repro: {code: Not reported, code_url: Not reported, dataset: Not reported, dataset_url: Not reported, checkpoints: Not reported, prompts_published: Not reported, hardware_specified: Not reported, hyperparameters: Not reported, protocol_described: Not reported, project_page: Not reported, concerns: Not reported}
limitations_flags: [sim-to-real, no-human-study, latency]
web_verification_required: []
cited_missing: [NaVILA, NaVid, DualVLN, NavDP, Falcon/Social-HM3D]
external_verification: {verified_on: '2026-10-19', status_class: 'C: preprint only', source: arXiv abs page + Crossref title search (no match), arxiv_id: 2607.16806v1, publication_status: Preprint, peer_reviewed_note: No verified peer-reviewed version found as of corpus freeze date}
stage2: {added: true, download_source: 'https://arxiv.org/pdf/2607.16806v1', source_type: arXiv, inclusion_reason: Direct FM dynamic social VLN with social metrics; after Cai cut-off. Retrieved by pass-1 search but missed in first screening; included after re-screening., relative_to_cai_cutoff: after Cai cut-off (27 Jun 2026)}
coding: {latency_reported: 'Yes', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: 'No', code_released: 'No', new_dataset_released: 'No', real_robot: 'No', human_subject_study: 'No'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A6]
  C_capabilities: {SAF1: 'Yes', SAF2: 'No', SPA1: 'Yes', SPA2: 'No', SPA3: Partial, SPA4: Partial, HUM1: 'No', HUM2: 'No', NOR1: 'No', NOR2: Partial, NOR3: 'No', NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: [R1, R4]
  D_interface: [D5]
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: none, EV4_real_humans_in_trials: simulated-only, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: Not reported in text read, statistical_testing: 'No', cross_environment: No/unclear, runtime_measured: 'Yes'}
  cross_cutting: {temporal_coupling: asynchronous, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'No', uncertainty: 'No', hallucination_mitigation: 'No', privacy_constraint: 'No', inference_location: local/onboard or local server}
physical_source_folder: "05_Direct_VLM_SocialNav_Preprints"
analytical_category: "S5"
coding:
  latency_reported: "Yes"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "No"
  code_released: "No"
  new_dataset_released: "No"
  real_robot: "No"
  human_subject_study: "No"
---

# SPARK-VLN (Hu et al., arXiv 2026)

Page convention: PDF index of the corpus copy (arXiv v1).

## A. Bibliographic
arXiv:2607.16806v1 (18 Jul 2026). HKUST (Guangzhou). Publication status: Preprint; Peer reviewed: No verified peer-reviewed version found as of corpus freeze date.

## B. Position
S5 direct. Addresses **VLM latency vs moving pedestrians** ("observation staleness") explicitly, and shows that synchronous benchmarks hide it. After Cai cut-off. Same group as Falcon/Social-HM3D (Gong).

## G. Social capabilities
C1 Yes (human collision rate) · C3 Yes (personal-space compliance) · C12, C17, C23 Partial · others No.

## H/I. I6; E2.

## L. Results
Idealized: SR 41.60%, SPL 34.67%, PSC 96.2% (best). Realistic: SR 34.80% vs NaVILA 29.00% and DualVLN 22.90%; PSC 93.9%; collision 29.3%; AvgD 5.13 m. Stream vs wait-then-act: SR +10.0 points; latency 0.185 s vs 0.788 s.

## N. Limitations
Stated: future work on pedestrian intent prediction (reactive, not anticipatory). Observable: simulation only; human-collision rate still ~29% in the realistic mode; no safety layer.

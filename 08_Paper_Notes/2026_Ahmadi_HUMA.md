---
id: 2026_Ahmadi_HUMA
source_pdfs: [05_Direct_VLM_SocialNav_Preprints/HUMA-Think-When-It-Matters_arXiv2607.10991v1.pdf]
duplicate_copies: []
related_versions: ['arXiv:2607.10991v1 = corpus copy']
title: 'Think When It Matters: Conditional VLM Reasoning for Social Navigation with RL Policies'
authors: [Ali Ahmadi, Hamed Rahimi, Adrien Jacquet Cretides, Marie Samson, Mahdi Khoramshahi, Mohamed Chetouani]
year: 2026
venue: arXiv preprint (arXiv:2607.10991v1)
volume: NA
issue: NA
pages: NA
doi: Not found / not applicable
url: https://arxiv.org/abs/2607.10991
pub_status: preprint
peer_reviewed: 'No'
peer_review_basis: 'arXiv 2607.10991v1 only (posted 2026-07-13, latest version 2026-07-13); arXiv comment: CoRL 2026 submission. 15 pages, 7 figures. No verified peer-reviewed version found as of corpus freeze date (2026-10-19) via Crossref title search.'
category: S5
folder: 05_Direct_VLM_SocialNav_Preprints
folder_category_match: 'Yes'
category_rationale: 'Conditional VLM reasoning: a LoRA-fine-tuned Qwen3-VL-2B (trained on SNEI) is invoked only when a proximity-based switch detects social relevance; its output conditions an RL navigation policy (Falcon) in Social-HM3D/MP3D.'
paper_type: method
fm_used: 'Yes'
fm_class: [VLM]
fm_models: [Qwen3-VL-2B (LoRA on SNEI)]
fm_size: 2B
method_family: [conditional (event-triggered) VLM reasoning, RL policy conditioning (Falcon), LoRA fine-tuning]
roles: [F1, F2, F4]
roles_evidence: {F1: VLM describes social scene when triggered., F2: Predicts human behaviour/intent (SNEI-style perception and prediction)., F4: Reasons about appropriate social action.}
integration: I6
integration_rationale: VLM output conditions the RL policy (learned conditioning); alternative coding I5. Event-triggered invocation.
evidence: E2
evidence_rationale: Social-HM3D and Social-MP3D simulation benchmarks; Mirokai real-robot demonstration qualitative.
inputs: [RGB-D, proximity signal]
outputs: [social reasoning embedding/text, policy actions (RL)]
human_repr: [implicit + VLM text]
capabilities: {C1: 'Yes', C2: 'No', C3: 'No', C4: 'No', C5: Partial, C6: 'No', C7: Partial, C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: Partial, C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: 'No', C24: Partial, C25: 'No'}
exp:
  datasets: [SNEI (VLM fine-tuning)]
  simulators: [Habitat Social-HM3D, Social-MP3D]
  robots: [Mirokai (demonstration)]
  environment: Not reported
  indoor_outdoor: indoor
  sensors: Not reported
  humans: simulated humanoids
  n_scenes: Not reported
  n_trajectories: Not reported
  n_participants: Not reported
  split: Not reported
  baselines: [Falcon, other Social-HM3D baselines]
  ablation: Yes (trigger, always-on reasoning)
  real_robot_trials: Partial (qualitative demonstration)
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: Not reported
metrics: [NAV | Success rate | % | Social-HM3D 62.07; MP3D 70.35 | p.7, SAFETY | Human collision (H-Coll) | % | Social-HM3D 34.48; MP3D 20.82 | p.7, 'DEPLOY | VLM call latency | ms | 2,425 ms per call | p.8']
deployment: {fm_model: Qwen3-VL-2B, model_size: 2B, api_cloud_local: Local, onboard_offboard: Onboard (NVIDIA Thor) in demo, gpu: NVIDIA Jetson Thor, cpu: Not reported, latency: '2,425 ms per VLM call', query_frequency: Not reported, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: 'Yes', caching: Not reported, event_triggered: Yes (proximity-based social-context switch), distillation: Not reported, quantization: Not reported, fallback_planner: RL policy runs without VLM when not triggered, safety_shield: 'No', emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: 'No', real_time_claim_supported: Not reported}
repro: {code: Not reported, code_url: Not reported, dataset: Not reported, dataset_url: Not reported, checkpoints: Not reported, prompts_published: Not reported, hardware_specified: Not reported, hyperparameters: Not reported, protocol_described: Not reported, project_page: Not reported, concerns: Not reported}
limitations_flags: [latency, sim-to-real, no-human-study]
web_verification_required: []
cited_missing: [Falcon (Social-HM3D), Social-LLaVA/SNEI (in corpus)]
dataset: {uses_snei: 'Yes - fine-tuned on SNEI; describes SNEI as built on "the SCAN benchmark" (sic, likely SCAND)'}
external_verification: {verified_on: '2026-10-19', status_class: 'C: preprint only (CoRL 2026 submission per arXiv comment; not an acceptance)', source: arXiv abs page + Crossref title search (no match), arxiv_id: 2607.10991v1, publication_status: Preprint, peer_reviewed_note: No verified peer-reviewed version found as of corpus freeze date}
stage2: {added: true, download_source: 'https://arxiv.org/pdf/2607.10991v1', source_type: arXiv, inclusion_reason: 'Direct: conditional VLM social reasoning for RL policy; after Cai cut-off.', relative_to_cai_cutoff: after Cai cut-off (27 Jun 2026)}
coding: {latency_reported: 'Yes', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: 'No', code_released: 'No', new_dataset_released: NA, real_robot: Demo, human_subject_study: 'No'}
snei_usage: {reported_quantity: Not stated, unit: image-question-answer pairs, what_it_represents: SNEI used to fine-tune Qwen3-VL-2B, page: p.6, remark: Describes SNEI as "constructed on top of the SCAN benchmark" (sic), provenance_note: SNEI provenance (SCAND vs SCAND+MuSoHu) UNRESOLVED; see SNEI_DATASET_RECONCILIATION.md}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A5, A6]
  C_capabilities: {SAF1: 'Yes', SAF2: 'No', SPA1: 'No', SPA2: 'No', SPA3: 'No', SPA4: Partial, HUM1: Partial, HUM2: Partial, NOR1: 'No', NOR2: 'No', NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: [R2, R3]
  D_interface: [D5]
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: demo, EV4_real_humans_in_trials: not-reported, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: Not reported, statistical_testing: 'No', cross_environment: No/unclear, runtime_measured: 'Yes'}
  cross_cutting: {temporal_coupling: event-triggered, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'No', uncertainty: 'No', hallucination_mitigation: 'No', privacy_constraint: 'No', inference_location: local/onboard or local server}
physical_source_folder: "05_Direct_VLM_SocialNav_Preprints"
analytical_category: "S5"
coding:
  latency_reported: "Yes"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "No"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "Demo"
  human_subject_study: "No"
---

# HUMA / Think When It Matters (Ahmadi et al., arXiv 2026)

## A. Bibliographic
arXiv:2607.10991v1 (13 Jul 2026); comment "CoRL 2026 submission" (a submission, not an acceptance). Sorbonne Université / ISIR + Enchanted Tools. Publication status: Preprint; Peer reviewed: No verified peer-reviewed version found as of corpus freeze date.

## B. Position
S5. **Event-triggered VLM reasoning** to cope with VLM latency; uses SNEI. After Cai cut-off.

## G. Capabilities
C1 Yes (human-collision rate) · C5, C7, C17, C24 Partial · others No.

## H/I. I6 (or I5); E2.

## L. Results
Social-HM3D SR 62.07%, H-Coll 34.48%; MP3D SR 70.35%, H-Coll 20.82%; VLM call 2.4 s.

## N. Limitations
Observable: high human-collision rates remain; real robot qualitative; SNEI provenance misdescribed ("SCAN").

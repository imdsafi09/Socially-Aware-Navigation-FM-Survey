---
id: 2026_Zhang_SAATT-Nav
source_pdfs: [05_Direct_VLM_SocialNav_Preprints/SAATT-Nav_arXiv2603.13698v2.pdf]
duplicate_copies: []
related_versions: ['arXiv:2603.13698v2 = corpus copy']
title: 'SAATT Nav: a Socially Aware Autonomous Transparent Transportation Navigation Framework for Wheelchairs'
authors: [Yutong Zhang, Shaiv Y. Mehra, Bradley S. Duerstock, Juan P. Wachs]
year: 2026
venue: arXiv preprint (arXiv:2603.13698v2)
volume: NA
issue: NA
pages: NA
doi: Not found / not applicable
url: https://arxiv.org/abs/2603.13698
pub_status: preprint
peer_reviewed: 'No'
peer_review_basis: 'arXiv 2603.13698v2 only (posted 2026-03-14, latest version 2026-03-18); arXiv comment: 8 pages, 4 figures, 2 tables, 1 algorithm. Submitted to IROS 2026. No verified peer-reviewed version found as of corpus freeze date (2026-10-19) via Crossref title search.'
category: S5
folder: 05_Direct_VLM_SocialNav_Preprints
folder_category_match: 'Yes'
category_rationale: LLM generates multiple pedestrian-intent hypotheses that are scored by forward rollouts for a socially aware, transparent wheelchair navigation framework; F-formation-aware social bubbles; explanation to the rider.
paper_type: method
fm_used: 'Yes'
fm_class: [LLM]
fm_models: [LLM (model not named)]
fm_size: Not reported
method_family: [LLM intent hypothesis generation, rollout scoring, social bubble / F-formation, explanation]
roles: [F2, F3, F5]
roles_evidence: {F2: LLM proposes k=8 pedestrian-intent hypotheses., F3: Group/F-formation bubbles considered., F5: Hypotheses scored via rollouts to select behaviour.}
integration: I3
integration_rationale: LLM hypotheses are scored and selected by rollout evaluation.
evidence: E2
evidence_rationale: Custom 2D simulation, 360 trials, Friedman/Conover statistical tests; no real robot.
inputs: [pedestrian tracks, scene description]
outputs: [intent hypotheses, selected plan, explanation]
human_repr: [tracked agents with intents; F-formation bubbles]
capabilities: {C1: 'Yes', C2: 'No', C3: 'Yes', C4: 'No', C5: 'No', C6: 'No', C7: 'Yes', C8: 'No', C9: Partial, C10: Partial, C11: 'No', C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: 'No', C18: Partial, C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: 'No', C24: 'No', C25: 'No'}
exp:
  datasets: Not reported
  simulators: [custom 2D simulation]
  robots: [simulated wheelchair]
  environment: Not reported
  indoor_outdoor: Not reported
  sensors: Not reported
  humans: simulated pedestrians
  n_scenes: Not reported
  n_trajectories: 360 trials
  n_participants: Not reported
  split: Not reported
  baselines: [social-force / non-LLM planners]
  ablation: 'Yes'
  real_robot_trials: 'No'
  human_study: 'No'
  statistical_testing: Yes (Friedman, Conover post-hoc)
  scenarios: Not reported
metrics: [SAFETY | Collisions / min distance | count / m | per trial | p.5, SOCIAL | Personal-space intrusion | % | social bubble violations | p.5]
deployment: {fm_model: LLM (unnamed), model_size: Not reported, api_cloud_local: Not reported, onboard_offboard: Not reported, gpu: Not reported, cpu: Not reported, latency: Not reported, query_frequency: Not reported, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Not reported, caching: Not reported, event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: Not reported, safety_shield: Rollout scoring, emergency_behavior: Not reported, uncertainty: Partial (multiple hypotheses), hallucination_mitigation: Partial (hypotheses checked by rollouts), real_time_claim_supported: Not reported}
repro: {code: Not reported, code_url: Not reported, dataset: Not reported, dataset_url: Not reported, checkpoints: Not reported, prompts_published: Not reported, hardware_specified: Not reported, hyperparameters: Not reported, protocol_described: Not reported, project_page: Not reported, concerns: LLM not named.}
limitations_flags: [sim-to-real, no-human-study]
web_verification_required: []
cited_missing: []
external_verification: {verified_on: '2026-10-19', status_class: 'C: preprint only (arXiv comment: submitted to IROS 2026; acceptance not found)', source: arXiv abs page + Crossref title search (no match), arxiv_id: 2603.13698v2, publication_status: Preprint, peer_reviewed_note: No verified peer-reviewed version found as of corpus freeze date}
stage2: {added: true, download_source: 'https://arxiv.org/pdf/2603.13698v2', source_type: arXiv, inclusion_reason: 'Direct: LLM intent reasoning for socially aware wheelchair navigation; before Cai cut-off, not cited by Cai.', relative_to_cai_cutoff: before Cai cut-off (27 Jun 2026); not cited by Cai, taxonomy_review_required: Transparency/explanation to rider not represented in F1-F11 / C1-C25.}
coding: {latency_reported: 'No', safety_mechanism: 'Yes', uncertainty_treatment: Partial, hallucination_treatment: 'Yes', code_released: 'No', new_dataset_released: NA, real_robot: 'No', human_subject_study: 'No'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A2, A3, A5]
  C_capabilities: {SAF1: 'Yes', SAF2: 'Yes', SPA1: 'Yes', SPA2: Partial, SPA3: 'No', SPA4: 'No', HUM1: 'No', HUM2: 'Yes', NOR1: 'No', NOR2: 'No', NOR3: 'No', NOR4: 'No', EXP1: 'No', EXP2: Partial, EXP3: 'No'}
  B_roles: [R2, R5]
  D_interface: [D1, D8]
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: none, EV4_real_humans_in_trials: simulated-only, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: 360 trials, statistical_testing: 'Yes (Friedman, Conover post-hoc)', cross_environment: No/unclear, runtime_measured: 'No'}
  cross_cutting: {temporal_coupling: per-decision, memory: 'No', continual_adaptation: 'No', explanation_output: Yes (human-facing), safety_guard: 'Yes', uncertainty: Partial, hallucination_mitigation: 'Yes', privacy_constraint: 'No', inference_location: not reported}
physical_source_folder: "05_Direct_VLM_SocialNav_Preprints"
analytical_category: "S5"
coding:
  latency_reported: "No"
  safety_mechanism: "Yes"
  uncertainty_treatment: "Partial"
  hallucination_treatment: "Yes"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "No"
  human_subject_study: "No"
---

# SAATT Nav (Zhang, Mehra, Duerstock, Wachs; arXiv 2026)

## A. Bibliographic
arXiv:2603.13698v2 (Mar 2026); comment "Submitted to IROS 2026" (no acceptance evidence). Purdue. Publication status: Preprint; Peer reviewed: No verified peer-reviewed version found as of corpus freeze date.

## B. Position
S5. LLM as **intent-hypothesis generator** (F2) with rollout verification. **TAXONOMY_REVIEW_REQUIRED**: transparency/explanation to the rider (also in Sotomi et al.).

## G. Capabilities
C1, C3, C7 Yes · C9, C10, C18 Partial · others No.

## H/I. I3; E2 (with statistical tests, unusual in this corpus).

## N. Limitations
Observable: simulation only; LLM unnamed; no human evaluation of transparency claims.

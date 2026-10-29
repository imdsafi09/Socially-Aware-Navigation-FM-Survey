---
id: 2024_Wang_SALM
source_pdfs: [05_Direct_VLM_SocialNav_Preprints/SALM-SRLM_arXiv2403.15648v3.pdf]
duplicate_copies: []
related_versions: ['arXiv:2403.15648v3 = corpus copy']
title: Unifying Large Language Model and Deep Reinforcement Learning for Human-in-Loop Interactive Socially-aware Navigation
authors: [Weizheng Wang, Ike Obi, Aniket Bera, Byung-Cheol Min]
year: 2024
venue: arXiv preprint (arXiv:2403.15648v3)
volume: NA
issue: NA
pages: NA
doi: Not found / not applicable
url: https://arxiv.org/abs/2403.15648
pub_status: preprint
peer_reviewed: 'No'
peer_review_basis: 'arXiv 2403.15648v3 only (posted 2024-03-22, latest version 2025-03-07); arXiv comment: none. No verified peer-reviewed version found as of corpus freeze date (2026-10-19) via Crossref title search.'
category: S5
folder: 05_Direct_VLM_SocialNav_Preprints
folder_category_match: 'Yes'
category_rationale: GPT-4o-based large navigation model (LNM) proposes robot velocities from language and scene context and is fused with a DRL social policy through an LLM critic (feedback model); human-in-loop interactive social navigation.
paper_type: method
fm_used: 'Yes'
fm_class: [LLM/VLM]
fm_models: [GPT-4o (LNM and LLM feedback model)]
fm_size: Not reported (API)
method_family: [LLM action generation, DRL (NaviSTAR-style spatio-temporal transformer), graph-of-thought critic fusion]
roles: [F4, F5, F7, F10]
roles_evidence: {F4: LNM reasons about social context and human requests., F5: LLM feedback model scores and weights the LNM and DRL actions., F7: Interprets human-in-loop commands into navigation tasks., F10: LNM outputs robot velocity commands directly.}
integration: I7
integration_rationale: LLM-generated velocities are fused with DRL velocities by the LLM critic and executed.
evidence: E2
evidence_rationale: Simulation with crowd simulators, 50 test cases x 2 tasks; no real-robot quantitative evaluation.
inputs: [human positions/velocities, robot state, language commands]
outputs: [velocity commands, fusion weights]
human_repr: [agent states in text and spatio-temporal graph]
capabilities: {C1: 'Yes', C2: 'No', C3: Partial, C4: 'No', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: Partial, C18: 'No', C19: 'No', C20: 'No', C21: Partial, C22: 'No', C23: 'Yes', C24: 'No', C25: 'No'}
exp:
  datasets: Not reported
  simulators: [2D crowd simulator (ORCA/SFM humans)]
  robots: [simulated holonomic robot]
  environment: Not reported
  indoor_outdoor: NA
  sensors: Not reported
  humans: simulated
  n_scenes: Not reported
  n_trajectories: 50 test cases per task
  n_participants: Not reported
  split: Not reported
  baselines: ['DRL baselines (SARL, NaviSTAR family)', LLM-only]
  ablation: Yes (LNM-only, DRL-only, fusion)
  real_robot_trials: 'No'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: Not reported
metrics: [NAV | Success rate | % | reaching goal without collision over 50 cases (SALM 86%) | p.7, SOCIAL | Social score | % | discomfort/intrusion-based score (SALM 82) | p.7]
deployment: {fm_model: GPT-4o, model_size: Not reported, api_cloud_local: Cloud API, onboard_offboard: Simulation, gpu: Not reported, cpu: Not reported, latency: Not reported, query_frequency: Not reported, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Not reported, caching: Not reported, event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: Not reported, safety_shield: No independent shield, emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: Partial (critic fusion with DRL), real_time_claim_supported: Not reported}
repro: {code: Not reported, code_url: Not reported, dataset: Not reported, dataset_url: Not reported, checkpoints: Not reported, prompts_published: Not reported, hardware_specified: Not reported, hyperparameters: Not reported, protocol_described: Not reported, project_page: Not reported, concerns: Not reported}
limitations_flags: [latency, cloud-dependence, sim-to-real, no-human-study]
web_verification_required: []
cited_missing: [NaviSTAR (in corpus)]
external_verification: {verified_on: '2026-10-19', status_class: 'C: preprint only', source: arXiv abs page + Crossref title search (no match), arxiv_id: 2403.15648v3, publication_status: Preprint, peer_reviewed_note: No verified peer-reviewed version found as of corpus freeze date}
stage2: {added: true, download_source: 'https://arxiv.org/pdf/2403.15648v3', source_type: arXiv, inclusion_reason: 'Direct: LLM generates and critiques social-navigation actions; before Cai cut-off, not cited by Cai.', relative_to_cai_cutoff: before Cai cut-off (27 Jun 2026); not cited by Cai}
coding: {latency_reported: 'No', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: Partial, code_released: 'No', new_dataset_released: NA, real_robot: 'No', human_subject_study: 'No'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A4, A5]
  C_capabilities: {SAF1: 'Yes', SAF2: 'No', SPA1: 'Yes', SPA2: 'No', SPA3: 'No', SPA4: Partial, HUM1: 'No', HUM2: 'No', NOR1: 'No', NOR2: 'Yes', NOR3: 'No', NOR4: 'No', EXP1: Partial, EXP2: 'No', EXP3: 'No'}
  B_roles: [R3, R4]
  D_interface: [D6, D2]
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: none, EV4_real_humans_in_trials: simulated-only, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: 50 test cases per task, statistical_testing: 'No', cross_environment: No/unclear, runtime_measured: 'No'}
  cross_cutting: {temporal_coupling: per-decision, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'No', uncertainty: 'No', hallucination_mitigation: Partial, privacy_constraint: 'No', inference_location: cloud API}
physical_source_folder: "05_Direct_VLM_SocialNav_Preprints"
analytical_category: "S5"
coding:
  latency_reported: "No"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "Partial"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "No"
  human_subject_study: "No"
---

# SALM (Wang, Obi, Bera, Min; arXiv 2024-2025)

## A. Bibliographic
arXiv:2403.15648v3 (v1 Mar 2024, v3 Mar 2025). Purdue University. Publication status: Preprint; Peer reviewed: No verified peer-reviewed version found as of corpus freeze date.

## B. Position
S5. LLM as **direct action generator** (F10, I7) whose outputs are arbitrated with a DRL social policy by an LLM critic; human-in-loop commands. Same group as NaviSTAR and SAMALM.

## G. Social capabilities
C1 Yes · C23 Yes (human commands) · C3, C17, C21 Partial (social score; crowd simulation) · others No.

## H/I. I7; E2 (simulation only).

## L. Results
Fusion (SALM) success 86%, social score 82 on 50 test cases, above LNM-only and DRL-only variants (exact page of table: see PDF).

## N. Limitations
Observable: simulation only; cloud LLM in the control loop without latency report; no safety layer independent of the critic.

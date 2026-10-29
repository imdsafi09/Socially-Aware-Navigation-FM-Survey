---
id: 2025_Wang_SAMALM
source_pdfs: [05_Direct_VLM_SocialNav_Preprints/SAMALM_arXiv2503.09758v1.pdf]
duplicate_copies: []
related_versions: ['arXiv:2503.09758v1 = corpus copy']
title: Multi-Agent LLM Actor-Critic Framework for Social Robot Navigation
authors: [Weizheng Wang, Ike Obi, Byung-Cheol Min]
year: 2025
venue: arXiv preprint (arXiv:2503.09758v1)
volume: NA
issue: NA
pages: NA
doi: Not found / not applicable
url: https://arxiv.org/abs/2503.09758
pub_status: preprint
peer_reviewed: 'No'
peer_review_basis: 'arXiv 2503.09758v1 only (posted 2025-03-12, latest version 2025-03-12); arXiv comment: none. No verified peer-reviewed version found as of corpus freeze date (2026-10-19) via Crossref title search.'
category: S5
folder: 05_Direct_VLM_SocialNav_Preprints
folder_category_match: 'Yes'
category_rationale: 'Multi-agent LLM actor-critic framework: LLM actors propose actions for each robot, local and global LLM critics verify social compliance and coordination among humans.'
paper_type: method
fm_used: 'Yes'
fm_class: [LLM/VLM]
fm_models: [GPT-4o (main), other zero-shot LLMs as baselines]
fm_size: Not reported (API)
method_family: [multi-agent LLM actor-critic, entropy-based score fusion]
roles: [F4, F5, F7, F10]
roles_evidence: {F4: Actors reason about social norms for each robot., F5: Local and global critics evaluate and correct actions., F7: Global critic coordinates robots., F10: Actors output velocity commands.}
integration: I7
integration_rationale: LLM-produced velocity actions (after critic verification) are executed directly.
evidence: E2
evidence_rationale: Simulation with multiple robots and humans; 50 test cases per setting; no real-robot quantitative trials.
inputs: [robot and human states as text]
outputs: [velocity commands per robot]
human_repr: [agent states in text]
capabilities: {C1: 'Yes', C2: 'No', C3: Partial, C4: 'No', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: Partial, C18: 'No', C19: 'No', C20: 'No', C21: Partial, C22: 'No', C23: 'No', C24: 'No', C25: 'No'}
exp:
  datasets: Not reported
  simulators: [2D multi-robot crowd simulator]
  robots: [simulated robots (3-5)]
  environment: Not reported
  indoor_outdoor: Not reported
  sensors: Not reported
  humans: simulated
  n_scenes: Not reported
  n_trajectories: 50 test cases per setting
  n_participants: Not reported
  split: Not reported
  baselines: [zero-shot LLMs (0-32% SR), DRL baselines]
  ablation: Yes (critic components)
  real_robot_trials: 'No'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: Not reported
metrics: [NAV | Success rate | % | GPT-4o SAMALM 68/70/30 across settings | p.7, SOCIAL | Social/discomfort score | % | intrusion-based | p.7]
deployment: {fm_model: GPT-4o, model_size: Not reported, api_cloud_local: Cloud API, onboard_offboard: Simulation, gpu: Not reported, cpu: Not reported, latency: Not reported, query_frequency: Not reported, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Not reported, caching: Not reported, event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: Not reported, safety_shield: 'No', emergency_behavior: Not reported, uncertainty: Partial (entropy-based fusion), hallucination_mitigation: Partial (critic verification), real_time_claim_supported: Not reported}
repro: {code: Not reported, code_url: Not reported, dataset: Not reported, dataset_url: Not reported, checkpoints: Not reported, prompts_published: Not reported, hardware_specified: Not reported, hyperparameters: Not reported, protocol_described: Not reported, project_page: Not reported, concerns: 'Table header "Human&Robot 5&3" vs text "5 robots, 3 humans" (data-quality issue).'}
limitations_flags: [latency, cloud-dependence, sim-to-real, no-human-study]
web_verification_required: []
cited_missing: []
external_verification: {verified_on: '2026-10-19', status_class: 'C: preprint only', source: arXiv abs page + Crossref title search (no match), arxiv_id: 2503.09758v1, publication_status: Preprint, peer_reviewed_note: No verified peer-reviewed version found as of corpus freeze date}
stage2: {added: true, download_source: 'https://arxiv.org/pdf/2503.09758v1', source_type: arXiv, inclusion_reason: 'Direct: multi-agent LLM actors/critics for social navigation; before Cai cut-off, not cited by Cai.', relative_to_cai_cutoff: before Cai cut-off (27 Jun 2026); not cited by Cai}
coding: {latency_reported: 'No', safety_mechanism: 'No', uncertainty_treatment: Partial, hallucination_treatment: 'Yes', code_released: 'No', new_dataset_released: NA, real_robot: 'No', human_subject_study: 'No'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A5]
  C_capabilities: {SAF1: 'Yes', SAF2: 'No', SPA1: 'Yes', SPA2: 'No', SPA3: 'No', SPA4: Partial, HUM1: 'No', HUM2: 'No', NOR1: 'No', NOR2: 'No', NOR3: 'No', NOR4: 'No', EXP1: Partial, EXP2: 'No', EXP3: 'No'}
  B_roles: [R3]
  D_interface: [D6, D2]
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: none, EV4_real_humans_in_trials: simulated-only, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: 50 test cases per setting, statistical_testing: 'No', cross_environment: No/unclear, runtime_measured: 'No'}
  cross_cutting: {temporal_coupling: per-decision, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'No', uncertainty: Partial, hallucination_mitigation: 'Yes', privacy_constraint: 'No', inference_location: cloud API}
physical_source_folder: "05_Direct_VLM_SocialNav_Preprints"
analytical_category: "S5"
coding:
  latency_reported: "No"
  safety_mechanism: "No"
  uncertainty_treatment: "Partial"
  hallucination_treatment: "Yes"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "No"
  human_subject_study: "No"
---

# SAMALM (Wang, Obi, Min; arXiv 2025)

## A. Bibliographic
arXiv:2503.09758v1 (Mar 2025). Purdue. Publication status: Preprint; Peer reviewed: No verified peer-reviewed version found as of corpus freeze date.

## B. Position
S5. Multi-robot extension of LLM-as-actor social navigation with explicit critic verification (F5) - one of few multi-agent FM social-navigation works.

## G. Capabilities
C1 Yes · C3, C17, C21 Partial · others No.

## H/I. I7; E2.

## L. Results
Zero-shot LLMs 0-32% success; SAMALM (GPT-4o) 68/70/30% across settings.

## N. Limitations
Observable: simulation only; low success in the hardest setting; inconsistent human/robot count between table header and text (data-quality issue).

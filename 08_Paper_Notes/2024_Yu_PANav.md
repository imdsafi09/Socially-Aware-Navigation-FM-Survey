---
id: 2024_Yu_PANav
source_pdfs: [05_Direct_VLM_SocialNav_Preprints/PANav_arXiv2410.04302v1.pdf]
duplicate_copies: []
related_versions: ['arXiv:2410.04302v1 = corpus copy']
title: 'PANav: Toward Privacy-Aware Robot Navigation via Vision-Language Models'
authors: [Bangguo Yu, Hamidreza Kasaei, Ming Cao]
year: 2024
venue: arXiv preprint (arXiv:2410.04302v1)
volume: NA
issue: NA
pages: NA
doi: Not found / not applicable
url: https://arxiv.org/abs/2410.04302
pub_status: preprint
peer_reviewed: 'No'
peer_review_basis: 'arXiv 2410.04302v1 only (posted 2024-10-05, latest version 2024-10-05); arXiv comment: 7 pages, 6 figures, conference. No verified peer-reviewed version found as of corpus freeze date (2026-10-19) via Crossref title search.'
category: S5
folder: 05_Direct_VLM_SocialNav_Preprints
folder_category_match: 'Yes'
category_rationale: GPT-4 Turbo selects among A* candidate paths to minimise privacy intrusion (avoid viewing/entering private areas and people's private spaces) - a socially motivated navigation criterion.
paper_type: method
fm_used: 'Yes'
fm_class: [VLM]
fm_models: [GPT-4 Turbo (vision)]
fm_size: Not reported (API)
method_family: [VLM path selection, A* candidates, majority vote over 5 runs]
roles: [F1, F4, F5]
roles_evidence: {F1: Identifies privacy-sensitive objects/areas., F4: Reasons about privacy norms., F5: Chooses among candidate paths (5-run majority vote).}
integration: I3
integration_rationale: VLM selects one of the geometric candidate paths.
evidence: E1
evidence_rationale: Offline evaluation on S3DIS (3 areas x 3 episodes); Jackal demonstration qualitative.
inputs: [semantic map / images, candidate paths]
outputs: [selected path]
human_repr: [privacy-sensitive regions]
capabilities: {C1: 'No', C2: 'No', C3: 'No', C4: 'No', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: Partial, C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: 'No', C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: 'No', C24: 'Yes', C25: 'No'}
exp:
  datasets: [S3DIS]
  simulators: Not reported
  robots: [Clearpath Jackal (demonstration)]
  environment: Not reported
  indoor_outdoor: indoor
  sensors: Not reported
  humans: none quantitatively
  n_scenes: Not reported
  n_trajectories: 3 areas x 3 episodes
  n_participants: Not reported
  split: Not reported
  baselines: [A* shortest path]
  ablation: Partial
  real_robot_trials: Partial (demonstration)
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: Not reported
metrics: ['SOCIAL | Privacy risk | score | Gaussian-modulated privacy exposure along path (Area 3: 960.534 vs A* 1928.649) | p.5', 'NAV | Path length | units | per episode (4,973 vs A* 3,373 in Area 3) | p.6']
deployment: {fm_model: GPT-4 Turbo, model_size: Not reported, api_cloud_local: Cloud API, onboard_offboard: Not reported, gpu: Not reported, cpu: Not reported, latency: Not reported, query_frequency: Not reported, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Not reported, caching: Not reported, event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: Not reported, safety_shield: A* geometric planning, emergency_behavior: Not reported, uncertainty: Partial (5-run majority vote), hallucination_mitigation: 'Partial (majority vote, candidate selection)', real_time_claim_supported: Not reported}
repro: {code: Not reported, code_url: Not reported, dataset: Not reported, dataset_url: Not reported, checkpoints: Not reported, prompts_published: Not reported, hardware_specified: Not reported, hyperparameters: Not reported, protocol_described: Not reported, project_page: Not reported, concerns: Area_5a privacy risk 1564.794 in table vs 1804.972 in text (data-quality issue).}
limitations_flags: [cloud-dependence, limited-scenarios, no-human-study]
web_verification_required: []
cited_missing: []
external_verification: {verified_on: '2026-10-19', status_class: 'C: preprint only', source: arXiv abs page + Crossref title search (no match), arxiv_id: 2410.04302v1, publication_status: Preprint, peer_reviewed_note: No verified peer-reviewed version found as of corpus freeze date}
stage2: {added: true, download_source: 'https://arxiv.org/pdf/2410.04302v1', source_type: arXiv, inclusion_reason: 'Direct (borderline): VLM privacy-aware path selection; before Cai cut-off, not cited by Cai.', relative_to_cai_cutoff: before Cai cut-off (27 Jun 2026); not cited by Cai, taxonomy_review_required: Privacy-aware navigation not represented in C1-C25.}
coding: {latency_reported: 'No', safety_mechanism: 'Yes', uncertainty_treatment: Partial, hallucination_treatment: 'Yes', code_released: 'No', new_dataset_released: NA, real_robot: Demo, human_subject_study: 'No'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A3]
  C_capabilities: {SAF1: 'No', SAF2: 'No', SPA1: 'No', SPA2: 'No', SPA3: 'No', SPA4: 'No', HUM1: 'No', HUM2: 'No', NOR1: Partial, NOR2: 'No', NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: [R1, R3]
  D_interface: [D2]
  E_evidence_profile: {EV1_offline: 'Yes', EV2_closed_loop_sim: 'No', EV3_physical_robot: demo, EV4_real_humans_in_trials: none, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: 3 areas x 3 episodes, statistical_testing: 'No', cross_environment: No/unclear, runtime_measured: 'No'}
  cross_cutting: {temporal_coupling: per-decision, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'Yes', uncertainty: Partial, hallucination_mitigation: 'Yes', privacy_constraint: privacy of occupants is the navigation objective, inference_location: cloud API}
physical_source_folder: "05_Direct_VLM_SocialNav_Preprints"
analytical_category: "S5"
coding:
  latency_reported: "No"
  safety_mechanism: "Yes"
  uncertainty_treatment: "Partial"
  hallucination_treatment: "Yes"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "Demo"
  human_subject_study: "No"
---

# PANav (Yu, Kasaei, Cao; arXiv 2024)

## A. Bibliographic
arXiv:2410.04302v1 (Oct 2024; comment "conference", unnamed). University of Groningen. Publication status: Preprint; Peer reviewed: No verified peer-reviewed version found as of corpus freeze date.

## B. Position
S5. **TAXONOMY_REVIEW_REQUIRED**: privacy-aware navigation is not represented in C1-C25 (closest C11/C24). Included as direct because privacy of occupants is a social norm and the VLM materially decides the path.

## H/I. I3; E1.

## N. Limitations
Observable: no humans in quantitative evaluation; tiny episode count; inconsistent risk value table vs text.

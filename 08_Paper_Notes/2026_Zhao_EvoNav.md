---
id: 2026_Zhao_EvoNav
source_pdfs: [05_Direct_VLM_SocialNav_Preprints/EvoNav_arXiv2605.11859v1.pdf]
duplicate_copies: []
related_versions: ['arXiv:2605.11859v1 = corpus copy']
title: 'EvoNav: Evolutionary Reward Function Design for Robot Navigation with Large Language Models'
authors: [Zhikai Zhao, Chuanbo Hua, Federico Berto, Zihan Ma, Kanghoon Lee, Jiachen Li, Jinkyoo Park]
year: 2026
venue: arXiv preprint (arXiv:2605.11859v1)
volume: NA
issue: NA
pages: NA
doi: Not found / not applicable
url: https://arxiv.org/abs/2605.11859
pub_status: preprint
peer_reviewed: 'No'
peer_review_basis: 'arXiv 2605.11859v1 only (posted 2026-05-12, latest version 2026-05-12); arXiv comment: none. No verified peer-reviewed version found as of corpus freeze date (2026-10-19) via Crossref title search.'
category: S5
folder: 05_Direct_VLM_SocialNav_Preprints
folder_category_match: 'Yes'
category_rationale: LLM (gpt-oss-120B) evolves reward-function code for crowd navigation RL (CrowdNav++), with social-distance and intrusion terms; policy trained with evolved reward.
paper_type: method
fm_used: 'Yes'
fm_class: [LLM]
fm_models: [gpt-oss-120B]
fm_size: 120B
method_family: [LLM evolutionary reward design, deep RL (CrowdNav++)]
roles: [F6, F8]
roles_evidence: {F6: LLM writes reward code including social terms., F8: Evolved reward trains the navigation policy.}
integration: I6
integration_rationale: FM influences policy only through training reward.
evidence: E2
evidence_rationale: 2D ORCA crowd simulation (CrowdNav++); no real robot.
inputs: [environment code / metrics feedback]
outputs: [reward function code]
human_repr: [ORCA agents]
capabilities: {C1: 'Yes', C2: 'No', C3: 'Yes', C4: 'No', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: 'Yes', C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: 'No', C24: 'No', C25: 'No'}
exp:
  datasets: Not reported
  simulators: [CrowdNav++ (ORCA humans)]
  robots: [simulated holonomic robot]
  environment: Not reported
  indoor_outdoor: Not reported
  sensors: Not reported
  humans: simulated
  n_scenes: Not reported
  n_trajectories: Not reported
  n_participants: Not reported
  split: Not reported
  baselines: [hand-crafted CrowdNav++ reward, Eureka-style baselines]
  ablation: 'Yes'
  real_robot_trials: 'No'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: Not reported
metrics: [NAV | Success rate | % | 93.22 +- 0.61% | p.6, SAFETY | Collision rate | % | 4.47 +- 0.42% | p.6, SOCIAL | Intrusion time ratio (ITR) / social distance | % / m | per episode | p.6]
deployment: {fm_model: gpt-oss-120B (training only), model_size: 120B, api_cloud_local: Local/cluster (training), onboard_offboard: Not reported, gpu: Not reported, cpu: Not reported, latency: NA (offline reward design), query_frequency: Not reported, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Not reported, caching: Not reported, event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: Not reported, safety_shield: 'No', emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: Partial (evolutionary selection on metrics), real_time_claim_supported: Not reported}
repro: {code: Not reported, code_url: Not reported, dataset: Not reported, dataset_url: Not reported, checkpoints: Not reported, prompts_published: Not reported, hardware_specified: Not reported, hyperparameters: Not reported, protocol_described: Not reported, project_page: Not reported, concerns: Not reported}
limitations_flags: [sim-to-real, no-human-study]
web_verification_required: []
cited_missing: [Eureka, CrowdNav++]
external_verification: {verified_on: '2026-10-19', status_class: 'C: preprint only', source: arXiv abs page + Crossref title search (no match), arxiv_id: 2605.11859v1, publication_status: Preprint, peer_reviewed_note: No verified peer-reviewed version found as of corpus freeze date}
stage2: {added: true, download_source: 'https://arxiv.org/pdf/2605.11859v1', source_type: arXiv, inclusion_reason: 'Direct: LLM reward design for social crowd navigation; before Cai cut-off, not cited by Cai.', relative_to_cai_cutoff: before Cai cut-off (27 Jun 2026); not cited by Cai}
coding: {latency_reported: 'No', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: Partial, code_released: 'No', new_dataset_released: NA, real_robot: 'No', human_subject_study: 'No'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1]
  C_capabilities: {SAF1: 'Yes', SAF2: 'No', SPA1: 'Yes', SPA2: 'No', SPA3: 'No', SPA4: 'Yes', HUM1: 'No', HUM2: 'No', NOR1: 'No', NOR2: 'No', NOR3: 'No', NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: [R3]
  D_interface: [D7]
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: none, EV4_real_humans_in_trials: simulated-only, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: Not reported, statistical_testing: 'No', cross_environment: No/unclear, runtime_measured: 'No'}
  cross_cutting: {temporal_coupling: training-only, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'No', uncertainty: 'No', hallucination_mitigation: Partial, privacy_constraint: 'No', inference_location: n/a (FM used at training time only)}
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

# EvoNav (Zhao et al., arXiv 2026)

## A. Bibliographic
arXiv:2605.11859v1 (12 May 2026). KAIST et al. Publication status: Preprint; Peer reviewed: No verified peer-reviewed version found as of corpus freeze date.

## B. Position
S5. LLM as **reward designer** (F6/F8, I6) for crowd navigation.

## G. Capabilities
C1, C3, C17 Yes (simulated) · others No.

## H/I. I6; E2.

## L. Results
SR 93.22%, collision 4.47% in CrowdNav++.

## N. Limitations
Observable: ORCA-only humans; no real-world or human evaluation.

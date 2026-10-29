---
id: 2026_Wang_SALSA
source_pdfs: [05_Direct_VLM_SocialNav_Preprints/SALSA-Act-on-What-You-See_arXiv2606.10495v2.pdf]
duplicate_copies: []
related_versions: ['arXiv:2606.10495v2 = corpus copy']
title: 'Act on What You See: Unlocking Safe Social Navigation in Vision-Language-Action Models'
authors: [Qingzi Wang, Xiyang Wu, Guangyao Shi, Dianwei Chen, Xianfeng Yang, Dinesh Manocha]
year: 2026
venue: arXiv preprint (arXiv:2606.10495v2)
volume: NA
issue: NA
pages: NA
doi: Not found / not applicable
url: https://arxiv.org/abs/2606.10495
pub_status: preprint
peer_reviewed: 'No'
peer_review_basis: 'arXiv 2606.10495v2 only (posted 2026-06-09, latest version 2026-06-14); arXiv comment: none. No verified peer-reviewed version found as of corpus freeze date (2026-10-19) via Crossref title search.'
category: S5
folder: 05_Direct_VLM_SocialNav_Preprints
folder_category_match: 'Yes'
category_rationale: Post-trains a 7B navigation VLA (OmniVLA) with LoRA to make it safe and socially compliant around pedestrians; evaluated offline on SCAND with near-collision and counterfactual accuracy metrics plus a quadruped demo.
paper_type: method
fm_used: 'Yes'
fm_class: [VLA]
fm_models: [OmniVLA (7B)]
fm_size: 7B
method_family: [VLA post-training (LoRA), counterfactual data, safety-aware fine-tuning]
roles: [F10]
roles_evidence: {F10: VLA outputs navigation actions directly.}
integration: I7
integration_rationale: Fine-tuned VLA maps observations to actions.
evidence: E1
evidence_rationale: Quantitative evaluation offline on SCAND; Unitree quadruped deployment shown qualitatively.
inputs: [RGB, goal]
outputs: [actions/waypoints]
human_repr: [implicit]
capabilities: {C1: Partial, C2: 'Yes', C3: 'No', C4: 'No', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: Partial, C18: 'No', C19: 'No', C20: Partial, C21: 'No', C22: 'No', C23: 'No', C24: 'No', C25: 'No'}
exp:
  datasets: [SCAND]
  simulators: Not reported
  robots: [Unitree quadruped (demonstration)]
  environment: Not reported
  indoor_outdoor: outdoor
  sensors: Not reported
  humans: real pedestrians in dataset
  n_scenes: Not reported
  n_trajectories: Not reported
  n_participants: Not reported
  split: Not reported
  baselines: [OmniVLA (base), other navigation foundation models]
  ablation: 'Yes'
  real_robot_trials: Partial (qualitative demonstration)
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: Not reported
metrics: [SAFETY | Near-collision reduction | % | -86.4% vs base OmniVLA (offline SCAND) | p.6, OTHER | Counterfactual accuracy (CF-Acc) | % | 52.8 -> 93.0 | p.6, NAV | Goal ratio | % | progress toward goal (OmniVLA 108.9%) | p.6]
deployment: {fm_model: OmniVLA 7B, model_size: 7B, api_cloud_local: Local, onboard_offboard: Not reported, gpu: Not reported, cpu: Not reported, latency: Not reported, query_frequency: Not reported, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Not reported, caching: Not reported, event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: Not reported, safety_shield: No (safety learned in policy), emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: 'No', real_time_claim_supported: Not reported}
repro: {code: Not reported, code_url: Not reported, dataset: Not reported, dataset_url: Not reported, checkpoints: Not reported, prompts_published: Not reported, hardware_specified: Not reported, hyperparameters: Not reported, protocol_described: Not reported, project_page: Not reported, concerns: 'Abstract suggests the 86.4% reduction covers real-world deployment, but quantitative results are offline; goal ratio >100% for base model unexplained (data-quality issue).'}
limitations_flags: [no-human-study, limited-scenarios]
web_verification_required: []
cited_missing: [OmniVLA, CityWalker]
external_verification: {verified_on: '2026-10-19', status_class: 'C: preprint only', source: arXiv abs page + Crossref title search (no match), arxiv_id: 2606.10495v2, publication_status: Preprint, peer_reviewed_note: No verified peer-reviewed version found as of corpus freeze date}
stage2: {added: true, download_source: 'https://arxiv.org/pdf/2606.10495v2', source_type: arXiv, inclusion_reason: 'Direct: socially safe VLA post-training; before Cai cut-off (9 Jun 2026), not cited by Cai.', relative_to_cai_cutoff: before Cai cut-off (27 Jun 2026); not cited by Cai}
coding: {latency_reported: 'No', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: 'No', code_released: 'No', new_dataset_released: NA, real_robot: Demo, human_subject_study: 'No'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A6]
  C_capabilities: {SAF1: Partial, SAF2: 'Yes', SPA1: 'No', SPA2: 'No', SPA3: 'No', SPA4: Partial, HUM1: 'No', HUM2: 'No', NOR1: 'No', NOR2: 'No', NOR3: 'No', NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: Partial}
  B_roles: [R3]
  D_interface: [D6]
  E_evidence_profile: {EV1_offline: 'Yes', EV2_closed_loop_sim: 'No', EV3_physical_robot: demo, EV4_real_humans_in_trials: none, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: Not reported, statistical_testing: 'No', cross_environment: No/unclear, runtime_measured: 'No'}
  cross_cutting: {temporal_coupling: per-decision, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'No', uncertainty: 'No', hallucination_mitigation: 'No', privacy_constraint: 'No', inference_location: local/onboard or local server}
physical_source_folder: "05_Direct_VLM_SocialNav_Preprints"
analytical_category: "S5"
coding:
  latency_reported: "No"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "No"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "Demo"
  human_subject_study: "No"
---

# SALSA / Act on What You See (Wang et al., arXiv 2026)

## A. Bibliographic
arXiv:2606.10495v2 (v1 9 Jun 2026, v2 14 Jun 2026). University of Maryland (Manocha group). Publication status: Preprint; Peer reviewed: No verified peer-reviewed version found as of corpus freeze date.

## B. Position
S5. One of few works making a **navigation VLA itself socially safe** (I7) rather than wrapping it.

## G. Capabilities
C2 Yes (near-collision metric) · C1, C17, C20 Partial · others No.

## H/I. I7; E1 (real robot demo only).

## L. Results
Offline SCAND: near-collisions -86.4%; CF-Acc 52.8% -> 93.0%.

## N. Limitations
Observable: quantitative evaluation offline only; abstract framing overstates real-world evidence; goal ratio 108.9% unexplained (data-quality issue).

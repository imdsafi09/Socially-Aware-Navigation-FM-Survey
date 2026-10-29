---
id: 2026_Zhang_Walk-With-Me
source_pdfs: [05_Direct_VLM_SocialNav_Preprints/Walk-With-Me_arXiv2604.26839v1.pdf]
duplicate_copies: []
related_versions: ['arXiv:2604.26839v1 = corpus copy']
title: 'Walk With Me: Long-Horizon Social Navigation for Human-Centric Outdoor Assistance'
authors: [Lingfeng Zhang, Xiaoshuai Hao, Xizhou Bu, Yingbo Tang, Hongsheng Li, Jinghui Lu, Xiu-shen Wei, Jiayi Ma, Yu Liu, Jing Zhang, Hangjun Ye, Xiaojun Liang, Long Chen, Wenbo Ding]
year: 2026
venue: arXiv preprint (arXiv:2604.26839v1)
volume: NA
issue: NA
pages: NA
doi: Not found / not applicable
url: https://arxiv.org/abs/2604.26839
pub_status: preprint
peer_reviewed: 'No'
peer_review_basis: 'arXiv 2604.26839v1 only (posted 2026-04-29, latest version 2026-04-29); arXiv comment: none. No verified peer-reviewed version found as of corpus freeze date (2026-10-19) via Crossref title search.'
category: S5
folder: 05_Direct_VLM_SocialNav_Preprints
folder_category_match: 'Yes'
category_rationale: 'Hierarchical system for long-horizon outdoor social navigation assisting a human: a high-level VLM handles destination reasoning and safety decisions (stop/wait), a low-level VLA produces socially compliant motion; real-world outdoor trials.'
paper_type: method
fm_used: 'Yes'
fm_class: [VLM, VLA]
fm_models: [high-level VLM (remote server), low-level VLA (SocialNav-based variant best in ablation)]
fm_size: Not reported
method_family: [hierarchical VLM-VLA, remote inference]
roles: [F1, F4, F7, F10]
roles_evidence: {F1: VLM interprets outdoor scene and user request., F4: 'Safety reasoning: stop/wait decisions near pedestrians/traffic.', F7: Destination and sub-goal planning over long horizon., F10: VLA outputs low-level motion.}
integration: I7
integration_rationale: VLA directly generates actions; VLM gates/plans.
evidence: E3
evidence_rationale: 20 real-world outdoor trials (success 12/20 = 60%) with systematic reporting; no human-subject evaluation.
inputs: [RGB, user language request]
outputs: [sub-goals, stop/wait decisions, actions]
human_repr: [implicit in VLM/VLA]
capabilities: {C1: Partial, C2: 'No', C3: 'No', C4: 'No', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: Partial, C13: 'No', C14: 'No', C15: Partial, C16: 'No', C17: Partial, C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: 'Yes', C24: Partial, C25: 'No'}
exp:
  datasets: Not reported
  simulators: Not reported
  robots: [real mobile platform (outdoor)]
  environment: outdoor urban/campus
  indoor_outdoor: outdoor
  sensors: Not reported
  humans: real pedestrians; assisted user
  n_scenes: Not reported
  n_trajectories: 20 real trials
  n_participants: Not reported
  split: Not reported
  baselines: [VLA variants (ablation)]
  ablation: Yes (low-level VLA choice)
  real_robot_trials: 'Yes'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: Not reported
metrics: [NAV | Success rate | % | 12/20 real trials (60%) | p.10]
deployment: {fm_model: VLM + VLA, model_size: Not reported, api_cloud_local: Remote server (NVIDIA H20), onboard_offboard: Offboard inference, gpu: NVIDIA H20 (server), cpu: Not reported, latency: Not reported, query_frequency: Not reported, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Not reported, caching: Not reported, event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: Not reported, safety_shield: VLM safety stop/wait module (not formally verified), emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: Not reported, real_time_claim_supported: Not reported}
repro: {code: Not reported, code_url: Not reported, dataset: Not reported, dataset_url: Not reported, checkpoints: Not reported, prompts_published: Not reported, hardware_specified: Not reported, hyperparameters: Not reported, protocol_described: Not reported, project_page: Not reported, concerns: Not reported}
limitations_flags: [latency, cloud-dependence, limited-scenarios, no-human-study]
web_verification_required: []
cited_missing: [SocialNav (in corpus)]
external_verification: {verified_on: '2026-10-19', status_class: 'C: preprint only', source: arXiv abs page + Crossref title search (no match), arxiv_id: 2604.26839v1, publication_status: Preprint, peer_reviewed_note: No verified peer-reviewed version found as of corpus freeze date}
stage2: {added: true, download_source: 'https://arxiv.org/pdf/2604.26839v1', source_type: arXiv, inclusion_reason: 'Direct: VLM+VLA social outdoor assistance with real trials; cited by Cai 2026 [78].', relative_to_cai_cutoff: 'before Cai cut-off (27 Jun 2026); cited by Cai [78]'}
coding: {latency_reported: 'No', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: 'No', code_released: 'No', new_dataset_released: NA, real_robot: Systematic, human_subject_study: 'No'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A6]
  C_capabilities: {SAF1: Partial, SAF2: 'No', SPA1: 'No', SPA2: 'No', SPA3: Partial, SPA4: Partial, HUM1: 'No', HUM2: 'No', NOR1: 'No', NOR2: 'No', NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: [R3, R4]
  D_interface: [D4, D6]
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'No', EV3_physical_robot: systematic, EV4_real_humans_in_trials: present-type-unreported, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: 20 real trials, statistical_testing: 'No', cross_environment: No/unclear, runtime_measured: 'No'}
  cross_cutting: {temporal_coupling: hierarchical, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'No', uncertainty: 'No', hallucination_mitigation: 'No', privacy_constraint: 'No', inference_location: remote server}
physical_source_folder: "05_Direct_VLM_SocialNav_Preprints"
analytical_category: "S5"
coding:
  latency_reported: "No"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "No"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "Systematic"
  human_subject_study: "No"
---

# Walk With Me (Zhang et al., arXiv 2026)

## A. Bibliographic
arXiv:2604.26839v1 (29 Apr 2026). Publication status: Preprint; Peer reviewed: No verified peer-reviewed version found as of corpus freeze date.

## B. Position
S5. Human-accompanying outdoor assistance: hierarchical VLM (planning/safety) + VLA (action). Cited by Cai et al. 2026 (ref. [78]).

## G. Capabilities
C23 Yes · C1, C12, C15, C17, C24 Partial · others No.

## H/I. I7; E3.

## L. Results
Real-world success 60% (12/20); SocialNav-based low-level VLA best in ablation.

## N. Limitations
Observable: remote H20 server; no latency figure; no human-subject evaluation of accompaniment quality.

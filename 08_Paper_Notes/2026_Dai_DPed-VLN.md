---
id: 2026_Dai_DPed-VLN
source_pdfs: [06_Datasets_Benchmarks_Evaluation/DPed-VLN_arXiv2609.21504v1.pdf]
duplicate_copies: []
related_versions: ['arXiv:2609.21504v1 = corpus copy']
title: 'DPed-VLN: A Benchmark for Socially Compliant Vision-and-Language Navigation in Dynamic Pedestrian Environments'
authors: [Haojie Dai, Xiangyi Wang, Liuyi Wang, Kai Sheng, Zongtao He, Chengju Liu, Wei Ye, Qijun Chen]
year: 2026
venue: arXiv preprint (arXiv:2609.21504v1)
volume: NA
issue: NA
pages: NA
doi: Not found / not applicable
url: https://arxiv.org/abs/2609.21504
pub_status: preprint
peer_reviewed: 'No'
peer_review_basis: 'arXiv 2609.21504v1 (posted 2026-09-18; comment: none). No verified peer-reviewed version found as of corpus freeze date (2026-10-19) via Crossref title search.'
category: S6
folder: 06_Datasets_Benchmarks_Evaluation
folder_category_match: 'Yes'
category_rationale: Habitat 3.0 benchmark for socially compliant VLN among dynamic pedestrians (33,093 episodes, 66,186 instructions incl. VLM-generated pedestrian-prior instructions); evaluates NaVILA, StreamVLN and an RL method with personal-space and collision metrics.
paper_type: benchmark
fm_used: 'Yes'
fm_class: [VLM]
fm_models: [VLM for instruction/context generation (model not identified in text read)]
fm_size: Not reported
method_family: [benchmark construction, socially constrained expert paths, VLM instruction generation]
roles: [F11]
roles_evidence: {F11: VLM summarises scene and dynamic context to generate instructions with pedestrian priors (p.4).}
integration: I1
integration_rationale: FM used in dataset construction; evaluated agents include VLM-based VLN models.
evidence: E2
evidence_rationale: Simulation benchmark (Habitat 3.0, ORCA humanoids).
inputs: [Habitat scenes, trajectories]
outputs: [instructions, episodes]
human_repr: [ORCA-controlled humanoids]
capabilities: {C1: 'Yes', C2: 'No', C3: 'Yes', C4: 'No', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: 'No', C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: Partial, C24: 'No', C25: 'No'}
exp:
  datasets: Not reported
  simulators: [Habitat 3.0]
  robots: [Spot-like robot model (sim)]
  environment: Not reported
  indoor_outdoor: Not reported
  sensors: Not reported
  humans: Not reported
  n_scenes: Not reported
  n_trajectories: Not reported
  n_participants: Not reported
  split: Not reported
  baselines: [NaVILA, StreamVLN, DPet-RL]
  ablation: Not reported
  real_robot_trials: 'No'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: Not reported
metrics: ['NAV | SR / SPL / STL | % | success, path efficiency, success weighted by time | p.5', SAFETY | HCR | % | human collision rate | p.5, SOCIAL | PSC | % | personal-space compliance | p.5]
repro: {code: 'Yes', code_url: 'https://github.com/tju-dhj/DPedVLN', dataset: Not reported, dataset_url: Not reported, checkpoints: Not reported, prompts_published: Not reported, hardware_specified: Not reported, hyperparameters: Not reported, protocol_described: Not reported, project_page: Not reported, concerns: Not reported}
limitations_flags: [sim-to-real]
web_verification_required: [Name of VLM used for instruction generation.]
cited_missing: [HA-VLN (in corpus), StreamVLN, NaVILA]
dataset: {kind: benchmark, real_synthetic: synthetic, size: '33,093 episodes; 66,186 instruction-trajectory pairs', closed_loop: 'Yes', dynamic_humans: 'Yes', language_ann: 'Yes', standard_metrics: 'SR, SPL, STL, HCR, PSC'}
external_verification: {verified_on: '2026-10-19', status_class: 'C: preprint only', source: arXiv abs page + Crossref title search (no match), arxiv_id: 2609.21504v1}
stage2: {added: true, download_source: 'https://arxiv.org/pdf/2609.21504v1', source_type: arXiv, inclusion_reason: Social VLN benchmark with VLM-generated instructions; after Cai cut-off.}
deployment: {fm_model: Not reported, model_size: Not reported, api_cloud_local: Not reported, onboard_offboard: Not reported, gpu: Not reported, cpu: Not reported, latency: Not reported, query_frequency: Not reported, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Not reported, caching: Not reported, event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: Not reported, safety_shield: Not reported, emergency_behavior: Not reported, uncertainty: Not reported, hallucination_mitigation: Not reported, real_time_claim_supported: Not reported}
coding: {latency_reported: 'No', safety_mechanism: NA, uncertainty_treatment: 'No', hallucination_treatment: 'No', code_released: 'Yes', new_dataset_released: 'Yes', real_robot: 'No', human_subject_study: 'No'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1]
  C_capabilities: {SAF1: 'Yes', SAF2: 'No', SPA1: 'Yes', SPA2: 'No', SPA3: 'No', SPA4: 'No', HUM1: 'No', HUM2: 'No', NOR1: 'No', NOR2: Partial, NOR3: 'No', NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: none, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "06_Datasets_Benchmarks_Evaluation"
analytical_category: "S6"
coding:
  latency_reported: "No"
  safety_mechanism: "NA"
  uncertainty_treatment: "No"
  hallucination_treatment: "No"
  code_released: "Yes"
  new_dataset_released: "Yes"
  real_robot: "No"
  human_subject_study: "No"
---

# DPed-VLN (Dai et al., arXiv 2026)

## A. Bibliographic
arXiv:2609.21504v1 (18 Sep 2026). Tongji University. Code: github.com/tju-dhj/DPedVLN. Publication status: Preprint; Peer reviewed: No verified peer-reviewed version found as of corpus freeze date. After Cai cut-off.

## B. Position
S6: socially compliant VLN benchmark, complementary to HA-VLN / HA-VLN 2.0.

---
id: 2024_Hirose_SACSoN
source_pdfs: [06_Datasets_Benchmarks_Evaluation/SACSoN-HuRoN_arXiv2306.01874v3.pdf]
duplicate_copies: []
related_versions: ['arXiv:2306.01874v3 = corpus copy']
title: 'SACSoN: Scalable Autonomous Control for Social Navigation'
authors: [Noriaki Hirose, Dhruv Shah, Ajay Sridhar, Sergey Levine]
year: 2024
venue: IEEE Robotics and Automation Letters
volume: '9'
issue: '1'
pages: 49-56
doi: 10.1109/LRA.2023.3329626
url: https://doi.org/10.1109/LRA.2023.3329626
pub_status: journal (corpus copy is arXiv author version)
peer_reviewed: 'Yes'
peer_review_basis: 'Crossref record: RA-L 9(1):49-56, DOI 10.1109/LRA.2023.3329626 (verified 2026-10-19).'
category: S6
folder: 06_Datasets_Benchmarks_Evaluation
folder_category_match: 'Yes'
category_rationale: HuRoN dataset (>75 h of autonomous robot data with >4,000 human interactions across 5 office environments) and a counterfactual-perturbation policy for socially unobtrusive navigation; non-FM, but a data source for navigation foundation models (Cai Table 2).
paper_type: dataset + method
fm_used: 'No'
fm_class: []
fm_models: []
fm_size: NA
method_family: [autonomous data collection, counterfactual perturbation, visual navigation policy (GNM/ViNT lineage)]
roles: []
roles_evidence: {}
integration: NA
integration_rationale: No FM.
evidence: E3
evidence_rationale: Real-robot evaluation of the learned policy among people in office environments.
inputs: [RGB]
outputs: [actions]
human_repr: [implicit (vision)]
capabilities: {C1: 'Yes', C2: 'No', C3: 'No', C4: 'No', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: Partial, C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: 'No', C18: 'No', C19: 'No', C20: 'No', C21: Partial, C22: 'No', C23: 'No', C24: 'No', C25: 'No'}
exp:
  datasets: [HuRoN]
  simulators: Not reported
  robots: [real wheeled robot]
  environment: Not reported
  indoor_outdoor: indoor
  sensors: Not reported
  humans: Not reported
  n_scenes: Not reported
  n_trajectories: Not reported
  n_participants: Not reported
  split: Not reported
  baselines: Not reported
  ablation: Not reported
  real_robot_trials: 'Yes'
  human_study: Not reported
  statistical_testing: Not reported
  scenarios: Not reported
metrics: []
repro: {code: Not reported, code_url: Not reported, dataset: Yes (public), dataset_url: Not reported, checkpoints: Not reported, prompts_published: Not reported, hardware_specified: Not reported, hyperparameters: Not reported, protocol_described: Not reported, project_page: Not reported, concerns: Not reported}
limitations_flags: [dataset-bias]
web_verification_required: []
cited_missing: [GNM (in corpus), ViNT (in corpus)]
dataset: {kind: dataset, real_synthetic: real, size: '>75 h, 58.7 km, >4,000 human interactions', environments: 5 office environments, sensors: 'RGB (fisheye/360), odometry', ego_view: 'Yes', rgb: 'Yes', dynamic_humans: Yes (natural), closed_loop: 'No', vlm_suitability: Medium-High, real_robot_compat: Yes (robot data), known_limitations: Office settings only}
external_verification: {verified_on: '2026-10-19', status_class: 'A: published, peer-reviewed', source: Crossref DOI 10.1109/LRA.2023.3329626, arxiv_id: 2306.01874v3}
stage2: {added: true, download_source: 'https://arxiv.org/pdf/2306.01874v3', source_type: arXiv, inclusion_reason: Data infrastructure for navigation foundation models in human environments (Cai Table 2).}
deployment: {fm_model: Not reported, model_size: Not reported, api_cloud_local: Not reported, onboard_offboard: Not reported, gpu: Not reported, cpu: Not reported, latency: Not reported, query_frequency: Not reported, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Not reported, caching: Not reported, event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: Not reported, safety_shield: Not reported, emergency_behavior: Not reported, uncertainty: Not reported, hallucination_mitigation: Not reported, real_time_claim_supported: Not reported}
coding: {latency_reported: 'No', safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: 'No', new_dataset_released: 'Yes', real_robot: Systematic, human_subject_study: 'No'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A6]
  C_capabilities: {SAF1: 'Yes', SAF2: 'No', SPA1: 'No', SPA2: 'No', SPA3: Partial, SPA4: 'No', HUM1: 'No', HUM2: 'No', NOR1: 'No', NOR2: 'No', NOR3: 'No', NOR4: 'No', EXP1: Partial, EXP2: 'No', EXP3: 'No'}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'No', EV3_physical_robot: systematic, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "06_Datasets_Benchmarks_Evaluation"
analytical_category: "S6"
coding:
  latency_reported: "No"
  safety_mechanism: "NA"
  uncertainty_treatment: "NA"
  hallucination_treatment: "NA"
  code_released: "No"
  new_dataset_released: "Yes"
  real_robot: "Systematic"
  human_subject_study: "No"
---

# SACSoN / HuRoN (Hirose, Shah, Sridhar, Levine; RA-L 2024)

## A. Bibliographic
RA-L 9(1):49-56, DOI 10.1109/LRA.2023.3329626 (Crossref-verified). UC Berkeley / Toyota. Peer-reviewed: Yes.

## B. Position
S6 non-FM dataset: large real robot-human interaction corpus used in navigation-foundation-model training; cited in Cai et al. 2026 Table 2.

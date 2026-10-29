---
id: 2023_Nguyen_MuSoHu
source_pdfs: [06_Datasets_Benchmarks_Evaluation/MuSoHu_arXiv2303.14880v2.pdf]
duplicate_copies: []
related_versions: ['arXiv:2303.14880v2 = corpus copy']
title: 'Toward Human-Like Social Robot Navigation: A Large-Scale, Multi-Modal, Social Human Navigation Dataset'
authors: [Duc M. Nguyen, Mohammad Nazeri, Amirreza Payandeh, Aniket Datar, Xuesu Xiao]
year: 2023
venue: 2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
volume: NA
issue: NA
pages: 7442-7447
doi: 10.1109/IROS55552.2023.10342447
url: https://doi.org/10.1109/IROS55552.2023.10342447
pub_status: conference (corpus copy is arXiv author version)
peer_reviewed: 'Yes'
peer_review_basis: 'Crossref record: IROS 2023, pp. 7442-7447, DOI 10.1109/IROS55552.2023.10342447; arXiv v2 comment "Accepted by IROS 2023" (verified 2026-10-19).'
category: S6
folder: 06_Datasets_Benchmarks_Evaluation
folder_category_match: 'Yes'
category_rationale: Large multi-modal dataset of human social navigation recorded with a helmet sensor suite (~100 km, 20 h, 300 trials, 13 humans); non-FM, but cited by SNEI-based work as a source (E-SocialNav) and used to learn human-like social navigation.
paper_type: dataset
fm_used: 'No'
fm_class: []
fm_models: []
fm_size: NA
method_family: [dataset collection]
roles: []
roles_evidence: {}
integration: NA
integration_rationale: No FM.
evidence: E1
evidence_rationale: Dataset paper; data collected by humans, not a robot evaluation.
inputs: []
outputs: []
human_repr: [egocentric human walker trajectories and surrounding people (raw sensors)]
capabilities: {C1: NA, C2: NA, C3: NA, C4: NA, C5: NA, C6: NA, C7: NA, C8: NA, C9: NA, C10: NA, C11: NA, C12: NA, C13: NA, C14: NA, C15: NA, C16: NA, C17: NA, C18: NA, C19: NA, C20: NA, C21: NA, C22: NA, C23: NA, C24: NA, C25: NA}
exp:
  datasets: [MuSoHu]
  simulators: Not reported
  robots: []
  environment: Not reported
  indoor_outdoor: Not reported
  sensors: Not reported
  humans: Not reported
  n_scenes: Not reported
  n_trajectories: Not reported
  n_participants: 13 demonstrators
  split: Not reported
  baselines: Not reported
  ablation: Not reported
  real_robot_trials: 'No'
  human_study: 'No'
  statistical_testing: Not reported
  scenarios: Not reported
metrics: []
repro: {code: Yes (data-collection hardware/software), code_url: 'https://github.com/RobotiXX/MuSoHu-data-collection', dataset: Yes (public), dataset_url: Not reported, checkpoints: Not reported, prompts_published: Not reported, hardware_specified: Not reported, hyperparameters: Not reported, protocol_described: Not reported, project_page: Not reported, concerns: Not reported}
limitations_flags: [dataset-bias]
web_verification_required: []
cited_missing: [SCAND (in corpus)]
dataset: {kind: dataset, real_synthetic: real, size: '~100 km, 20 h, 300 trials, 13 human demonstrators', environments: George Mason University campus and Washington DC, sensors: '3D LiDAR, stereo/depth, 360 camera, IMU, microphone array, GNSS (helmet)', ego_view: 'Yes', rgb: 'Yes', lidar: 'Yes', dynamic_humans: Yes (natural), language_ann: 'No', closed_loop: 'No', vlm_suitability: Medium (egocentric RGB; SNEI provenance claimed by E-SocialNav), real_robot_compat: Partial (human-mounted sensors), known_limitations: Human (not robot) embodiment; single region}
external_verification: {verified_on: '2026-10-19', status_class: 'A: published, peer-reviewed', source: Crossref DOI 10.1109/IROS55552.2023.10342447, arxiv_id: 2303.14880v2}
stage2: {added: true, download_source: 'https://arxiv.org/pdf/2303.14880v2', source_type: arXiv, inclusion_reason: Data infrastructure for VLM social-navigation datasets (SNEI provenance; Cai Table 2).}
deployment: {fm_model: Not reported, model_size: Not reported, api_cloud_local: Not reported, onboard_offboard: Not reported, gpu: Not reported, cpu: Not reported, latency: Not reported, query_frequency: Not reported, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Not reported, caching: Not reported, event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: Not reported, safety_shield: Not reported, emergency_behavior: Not reported, uncertainty: Not reported, hallucination_mitigation: Not reported, real_time_claim_supported: Not reported}
coding: {latency_reported: 'No', safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: 'Yes', new_dataset_released: 'Yes', real_robot: 'No', human_subject_study: 'No'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A6]
  C_capabilities: {SAF1: NA, SAF2: NA, SPA1: NA, SPA2: NA, SPA3: NA, SPA4: NA, HUM1: NA, HUM2: NA, NOR1: NA, NOR2: NA, NOR3: NA, NOR4: NA, EXP1: NA, EXP2: NA, EXP3: NA}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'Yes', EV2_closed_loop_sim: 'No', EV3_physical_robot: none, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "06_Datasets_Benchmarks_Evaluation"
analytical_category: "S6"
coding:
  latency_reported: "No"
  safety_mechanism: "NA"
  uncertainty_treatment: "NA"
  hallucination_treatment: "NA"
  code_released: "Yes"
  new_dataset_released: "Yes"
  real_robot: "No"
  human_subject_study: "No"
---

# MuSoHu (Nguyen, Nazeri, Payandeh, Datar, Xiao; IROS 2023)

## A. Bibliographic
IROS 2023, pp. 7442-7447, DOI 10.1109/IROS55552.2023.10342447 (Crossref-verified). George Mason University. Peer-reviewed: Yes.

## B. Position
S6 non-FM dataset; included as data infrastructure because SNEI-derived work (E-SocialNav) states SNEI derives from SCAND and MuSoHu, whereas Social-LLaVA states SCAND only (provenance unresolved; see SNEI reconciliation). Cited in Cai et al. 2026 Table 2.

---
id: 2025_Zhang_FewShot-Perception
source_pdfs: [06_Datasets_Benchmarks_Evaluation/FewShot-LLM-Perception-SocialNav_arXiv2512.16019v1.pdf]
duplicate_copies: []
related_versions: ['arXiv:2512.16019v1 = corpus copy', 'Related, distinct earlier work: Zhang et al., "Predicting Human Perceptions of Robot Performance during Navigation Tasks", ACM THRI 14(3):1-27 (2025), DOI 10.1145/3719020 (not a version of this paper)']
title: Few-Shot Inference of Human Perceptions of Robot Performance in Social Navigation Scenarios
authors: [Qiping Zhang, Nathan Tsoi, Mofeed Nagib, Hao-Tien Lewis Chiang, Marynel Vázquez]
year: 2025
venue: arXiv preprint (arXiv:2512.16019v1)
volume: NA
issue: NA
pages: NA
doi: Not found / not applicable
url: https://arxiv.org/abs/2512.16019
pub_status: preprint
peer_reviewed: 'No'
peer_review_basis: 'arXiv 2512.16019v1 (posted 2025-12-17; comment: none). No verified peer-reviewed version found as of corpus freeze date (2026-10-19) via Crossref title search.'
category: S6
folder: 06_Datasets_Benchmarks_Evaluation
folder_category_match: 'Yes'
category_rationale: LLMs (Gemini 2.0 Flash, GPT-4.1 mini, Llama 3.2 90B) predict human perceptions of robot performance (competence, surprise, intention) from spatio-temporal navigation cues with few in-context examples; extends SEAN TOGETHER to 404 episodes from 69 participants.
paper_type: evaluation method + dataset extension
fm_used: 'Yes'
fm_class: [LLM]
fm_models: [Gemini 2.0 Flash, GPT-4.1 mini, Llama 3.2 90B]
fm_size: 90B (Llama); others not reported
method_family: [in-context few-shot prediction, linear mixed models]
roles: [F11]
roles_evidence: {F11: LLM predicts human ratings of robot navigation episodes (p.5).}
integration: I1
integration_rationale: Offline prediction of human perceptions; not in the control loop.
evidence: E4
evidence_rationale: Human ratings of real-robot navigation episodes (69 participants, 404 episodes) are the ground truth for evaluation; LLM predictions compared with supervised baselines with mixed-model statistics.
inputs: [textualised spatio-temporal robot/human features, K demonstrations]
outputs: [predicted competence / surprise / intention ratings]
human_repr: [tracked positions as text]
capabilities: {C1: 'No', C2: 'No', C3: 'No', C4: Partial, C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: 'No', C18: Partial, C19: Partial, C20: 'No', C21: 'No', C22: 'No', C23: 'No', C24: 'No', C25: 'No'}
exp:
  datasets: [SEAN TOGETHER v2 (extended)]
  simulators: Not reported
  robots: [mobile robot (data collection)]
  environment: Not reported
  indoor_outdoor: Not reported
  sensors: Not reported
  humans: Not reported
  n_scenes: Not reported
  n_trajectories: 404 episodes
  n_participants: '69'
  split: Not reported
  baselines: [random forest, supervised models]
  ablation: Yes (K = 4 vs 64)
  real_robot_trials: Yes (data collection)
  human_study: Yes (ratings as labels)
  statistical_testing: Yes (linear mixed models)
  scenarios: Not reported
metrics: [HUMAN | Prediction accuracy | % | classification accuracy on competence/surprise/intention over 25 runs | p.5]
deployment: {fm_model: Gemini 2.0 Flash / GPT-4.1 mini / Llama 3.2 90B, model_size: Not reported, api_cloud_local: Cloud API / local, onboard_offboard: Not reported, gpu: Not reported, cpu: Not reported, latency: Not reported, query_frequency: Not reported, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Not reported, caching: Not reported, event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: Not reported, safety_shield: Not reported, emergency_behavior: Not reported, uncertainty: Not reported, hallucination_mitigation: Not reported, real_time_claim_supported: Not reported}
repro: {code: Not reported, code_url: Not reported, dataset: Extended dataset; link omitted for review, dataset_url: Not reported, checkpoints: Not reported, prompts_published: Not reported, hardware_specified: Not reported, hyperparameters: Not reported, protocol_described: Not reported, project_page: Not reported, concerns: Not reported}
limitations_flags: [dataset-bias]
web_verification_required: []
cited_missing: [SEAN TOGETHER]
dataset: {kind: human-perception dataset extension, real_synthetic: real, size: 404 labelled episodes from 69 participants, sensors: robot and human tracking, preference_ann: Yes (human ratings), site_diversity: single lab protocol, release: Link withheld for review}
external_verification: {verified_on: '2026-10-19', status_class: 'C: preprint only', source: arXiv abs page + Crossref title search (no match), arxiv_id: 2512.16019v1}
stage2: {added: true, download_source: 'https://arxiv.org/pdf/2512.16019v1', source_type: arXiv, inclusion_reason: FM predicting human perceptions of social-navigation behaviour (evaluation).}
coding: {latency_reported: 'No', safety_mechanism: NA, uncertainty_treatment: 'No', hallucination_treatment: 'No', code_released: 'No', new_dataset_released: 'No', real_robot: Systematic, human_subject_study: 'Yes'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A5]
  C_capabilities: {SAF1: 'No', SAF2: 'No', SPA1: 'No', SPA2: 'No', SPA3: 'No', SPA4: 'No', HUM1: 'No', HUM2: 'No', NOR1: 'No', NOR2: 'No', NOR3: 'No', NOR4: 'No', EXP1: Partial, EXP2: Partial, EXP3: 'No'}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'No', EV3_physical_robot: systematic, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: robot-behaviour evaluation (type not differentiated), EV6_open_world_deployment: 'No'}
physical_source_folder: "06_Datasets_Benchmarks_Evaluation"
analytical_category: "S6"
coding:
  latency_reported: "No"
  safety_mechanism: "NA"
  uncertainty_treatment: "No"
  hallucination_treatment: "No"
  code_released: "No"
  new_dataset_released: "No"
  real_robot: "Systematic"
  human_subject_study: "Yes"
---

# Few-shot inference of human perceptions (Zhang, Tsoi, Nagib, Chiang, Vazquez; arXiv 2025)

## A. Bibliographic
arXiv:2512.16019v1 (17 Dec 2025). Yale University / Google DeepMind. Publication status: Preprint; Peer reviewed: No verified peer-reviewed version found as of corpus freeze date.

## B. Position
S6: LLM as **proxy evaluator of human perception** of social navigation - relevant to evaluation-rigour discussion (FM judges vs human judges).

## L. Results
LLMs (Gemini, GPT) outperform a random-forest baseline except on Surprise with K = 64; K has significant effects on Competence and Surprise accuracy (mixed models).

## N. Limitations
Observable: single-site lab dataset; predictions from textualised tracks rather than vision.

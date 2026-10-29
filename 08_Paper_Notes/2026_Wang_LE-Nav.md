---
id: 2026_Wang_LE-Nav
source_pdfs: [04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/LE-Nav_arXiv2507.11001v1.pdf]
duplicate_copies: []
related_versions: ['arXiv:2507.11001v1 (15 Jul 2025) = corpus copy; published version IEEE T-ASE vol. 23 (2026)']
title: 'Learning to Tune Like an Expert: Interpretable and Scene-Aware Navigation via MLLM Reasoning and CVAE-Based Adaptation'
authors: [Yanbo Wang, Zipeng Fang, Lei Zhao, Weidong Chen]
year: 2026
venue: IEEE Transactions on Automation Science and Engineering
volume: '23'
issue: Not reported
pages: 6674-6686
doi: 10.1109/TASE.2026.3673004
url: https://doi.org/10.1109/TASE.2026.3673004
pub_status: journal (corpus copy is arXiv author version)
peer_reviewed: 'Yes'
peer_review_basis: 'Crossref record: IEEE T-ASE vol. 23, pp. 6674-6686 (2026), DOI 10.1109/TASE.2026.3673004 (verified 2026-10-19).'
category: S4
folder: 04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core
folder_category_match: 'Yes'
category_rationale: MLLM (GPT-4o / Qwen-VL-Max / Kimi) produces chain-of-thought scene descriptions that condition a CVAE generating planner hyperparameters (TEB/DWA) for a service wheelchair; evaluated in >100 real trials incl. pedestrian-crossing and dense-crowd scenarios and a user study on perceived safety and social acceptance.
paper_type: method
fm_used: 'Yes'
fm_class: [MLLM]
fm_models: [GPT-4o (main), Qwen-VL-Max, Kimi-latest (comparison)]
fm_size: Not reported (API)
method_family: [one-shot exemplar + CoT prompting, conditional VAE, 'planner hyperparameter modulation (TEB, DWA)', packet-loss augmentation]
roles: [F1, F6]
roles_evidence: {F1: 'MLLM scene description (layout, people, density) via one-shot exemplars and CoT (p.1).', F6: 'Scene description conditions CVAE that outputs planner hyperparameters (cost weights, limits) (p.1).'}
integration: I4
integration_rationale: FM output conditions planner parameters; TEB/DWA generate motion (p.6).
evidence: E4
evidence_rationale: Over a hundred real-world trials on a smart wheelchair across five scenarios incl. multi-agent crossing and high-density pedestrians, plus blinded user study with ten groups rating perceived safety and social acceptance (pedestrian and rider perspectives) (p.10).
inputs: [RGB, LiDAR, MLLM scene text (logprobs)]
outputs: [planner hyperparameters]
human_repr: [described in MLLM scene text; obstacles in planner costmap]
capabilities: {C1: 'Yes', C2: 'Yes', C3: 'No', C4: 'Yes', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: Partial, C18: 'No', C19: 'No', C20: Partial, C21: 'Yes', C22: 'No', C23: 'No', C24: 'Yes', C25: 'No'}
exp:
  datasets: [expert-tuned hyperparameter dataset (real-world)]
  simulators: []
  robots: [smart wheelchair platform]
  environment: indoor corridors, crowded areas
  indoor_outdoor: indoor
  sensors: [RGB, LiDAR]
  humans: real pedestrians; ten participant groups in the user study
  n_scenes: 5 scenarios
  n_trajectories: '>100 real-world trials'
  n_participants: ten groups (size per group not reported)
  split: Not reported
  baselines: [TEB-progressive, TEB-conservative, DWA-progressive, DWA-conservative, DADWA (RL-tuned)]
  ablation: Yes (MLLM choice, packet loss)
  real_robot_trials: 'Yes'
  human_study: Yes (blinded, Likert 1-5, pedestrian and user questionnaires)
  statistical_testing: Not reported
  scenarios: [narrow passages, continuous turns in tight corridors, dynamic multi-agent crossing, static path efficiency, high-density pedestrian avoidance]
metrics: [NAV | Failed to plan | count | timeouts and collisions | p.8, SAFETY | Risk rate | % | risk within local costmap / relaxed to TTC>5 s / TTC>2 s | p.8, NAV | Ego progress | % | progress metric on successful runs | p.8, SOCIAL | Acceleration / jerk | m/s^2 / m/s^3 | comfort proxies over successful runs | p.8, 'HUMAN | Questionnaire scores | 1-5 | pedestrian: safe distance, comfort; user: safety, route acceptability, smoothness | p.10', DEPLOY | MLLM query frequency | Hz | ~0.5 Hz scene updates | p.7]
deployment: {fm_model: GPT-4o, model_size: Not reported, api_cloud_local: Cloud API, onboard_offboard: Onboard planner; cloud MLLM, gpu: RTX 3060 (reported), cpu: Not reported, latency: MLLM ~0.5 Hz; packet loss handled by masking, query_frequency: ~0.5 Hz, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: 'Yes', caching: Not reported, event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: TEB/DWA continue with generated parameters, safety_shield: Classical TEB/DWA obstacle avoidance, emergency_behavior: Not reported, uncertainty: Partial (CVAE sampling over k samples; MLLM logprobs), hallucination_mitigation: 'Partial (one-shot exemplars, CoT; MLLM describes scene, does not command motion)', real_time_claim_supported: Yes (planners run locally)}
repro: {code: 'Yes', code_url: 'https://github.com/Cavendish518/LE-Nav', dataset: Not reported, dataset_url: Not reported, checkpoints: Not reported, prompts_published: Not reported, hardware_specified: Partial, hyperparameters: Partial, protocol_described: Not reported, project_page: Not reported, concerns: User-study group sizes and statistics not reported in the text read.}
limitations_flags: [cloud-dependence, latency]
web_verification_required: [User-study size per group and statistical tests (check supplementary).]
cited_missing: [DADWA, APPL family]
external_verification: {verified_on: '2026-10-19', status_class: 'A: published, peer-reviewed', source: Crossref DOI 10.1109/TASE.2026.3673004, arxiv_id: 2507.11001v1}
stage2: {added: true, download_source: 'https://arxiv.org/pdf/2507.11001v1', source_type: arXiv (author version), inclusion_reason: Direct FM socially acceptable navigation with real-world and human evaluation; peer-reviewed journal; found in pass-2 search; not cited by Cai 2026.}
coding: {latency_reported: 'Yes', safety_mechanism: 'Yes', uncertainty_treatment: Partial, hallucination_treatment: Partial, code_released: 'Yes', new_dataset_released: 'No', real_robot: Systematic, human_subject_study: 'Yes'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A5]
  C_capabilities: {SAF1: 'Yes', SAF2: 'Yes', SPA1: 'No', SPA2: 'No', SPA3: 'No', SPA4: Partial, HUM1: 'No', HUM2: 'No', NOR1: 'No', NOR2: 'No', NOR3: 'Yes', NOR4: 'No', EXP1: 'Yes', EXP2: 'No', EXP3: Partial}
  B_roles: [R1, R2]
  D_interface: [D3]
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'No', EV3_physical_robot: systematic, EV4_real_humans_in_trials: present-type-unreported, EV5_human_evaluation: co-present participants, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: '>100 real-world trials', statistical_testing: Not reported, cross_environment: No/unclear, runtime_measured: 'Yes'}
  cross_cutting: {temporal_coupling: asynchronous, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'Yes', uncertainty: Partial, hallucination_mitigation: Partial, privacy_constraint: 'No', inference_location: cloud API}
physical_source_folder: "04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core"
analytical_category: "S4"
coding:
  latency_reported: "Yes"
  safety_mechanism: "Yes"
  uncertainty_treatment: "Partial"
  hallucination_treatment: "Partial"
  code_released: "Yes"
  new_dataset_released: "No"
  real_robot: "Systematic"
  human_subject_study: "Yes"
---

# LE-Nav (Wang, Fang, Zhao, Chen; IEEE T-ASE 2026)

Page convention: PDF index of the corpus copy (arXiv v1).

## A. Bibliographic
IEEE T-ASE vol. 23, pp. 6674-6686 (2026), DOI 10.1109/TASE.2026.3673004 (Crossref-verified). Shanghai Jiao Tong University. Code on GitHub. Peer-reviewed: Yes.

## B. Position
S4 direct. MLLM as **scene interpreter conditioning planner tuning** (I4), with one of the stronger evidence profiles among added papers (real trials + user study with pedestrians and riders).

## C-D. Problem and method
Fixed planner parameters fail across scenes and reduce social acceptance; RL tuners suffer sim-to-real gaps (p.1). MLLM scene description (one-shot + CoT) -> transformer condition encoder -> CVAE generates TEB/DWA hyperparameters; trained on expert tuning data; packet-loss augmentation.

## G. Social capabilities
C1, C2 Yes (failures/collisions; TTC-based risk) · C4 Yes (perceived safety from pedestrians and riders) · C21 Yes (comfort ratings) · C24 Yes (scene-dependent parameters) · C17 Partial (high-density pedestrian scenario) · C20 Partial · others No.

## H/I. I4; E4.

## L. Results
User study: LE-Nav-DWA highest on all five questionnaire dimensions, then LE-Nav-TEB, then DADWA (Fig. 7). Scenario (c) multi-agent crossing: LE-Nav-DWA score 0.9129 vs DADWA 0.8956 (Table III).

## N. Limitations
Observable: MLLM low update rate; statistical tests not reported for the user study; scenario descriptions rely on cloud MLLM.

## P. Direct-paper questions (abridged)
1 Scene-aware, socially acceptable planner tuning. 3 GPT-4o (+Qwen-VL-Max, Kimi). 6 Scene text -> hyperparameters. 7 TEB/DWA. 10 Classical planners. 21 ~0.5 Hz. 23 Real robot. 24 Yes.

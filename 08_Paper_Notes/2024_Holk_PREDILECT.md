---
id: 2024_Holk_PREDILECT
source_pdfs: [04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/PREDILECT_arXiv2402.15420v1.pdf]
duplicate_copies: []
related_versions: ['arXiv:2402.15420v1 (23 Feb 2024) = corpus copy; published version HRI 2024 (ACM)']
title: 'PREDILECT: Preferences Delineated with Zero-Shot Language-based Reasoning in Reinforcement Learning'
authors: [Simon Holk, Daniel Marta, Iolanda Leite]
year: 2024
venue: Proceedings of the 2024 ACM/IEEE International Conference on Human-Robot Interaction (HRI 2024)
volume: NA
issue: NA
pages: 259-268
doi: 10.1145/3610977.3634970
url: https://doi.org/10.1145/3610977.3634970
pub_status: conference (corpus copy is arXiv version; ACM PDF not retrievable by script)
peer_reviewed: 'Yes'
peer_review_basis: 'Crossref record: HRI 2024 proceedings, pp. 259-268, DOI 10.1145/3610977.3634970 (verified 2026-10-19).'
category: S4
folder: 04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core
folder_category_match: 'Yes'
category_rationale: GPT-4 extracts features and sentiment (e.g., distance to humans, speed) from humans' free-text explanations of trajectory preferences, shaping the learned reward for socially compliant robot navigation trained with real MTurk feedback.
paper_type: method
fm_used: 'Yes'
fm_class: [LLM]
fm_models: [GPT-4]
fm_size: Not reported (API)
method_family: [preference-based RL, zero-shot LLM feature extraction, reward learning, SAC/PPO (stable-baselines)]
roles: [F6, F8]
roles_evidence: {F6: LLM maps text to feature highlights that reshape the reward-learning objective (p.1)., F8: Learned reward trains the RL navigation policy (FM only in training loop).}
integration: I6
integration_rationale: LLM influences the reward used to train the policy; no LLM at execution.
evidence: E2
evidence_rationale: Simulated social-navigation scenario (Unity, Pepper robot, three humans) trained with 400 preferences from 20 MTurk participants per condition; MuJoCo sanity tasks with an oracle (p.5).
inputs: [pairs of trajectory videos, human preference + free text]
outputs: [feature highlights, learned reward]
human_repr: [lidar-ray distance features to humans (sim)]
capabilities: {C1: 'No', C2: 'No', C3: Partial, C4: 'No', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: 'No', C18: 'No', C19: 'No', C20: 'No', C21: Partial, C22: 'No', C23: 'No', C24: Partial, C25: 'No'}
exp:
  datasets: []
  simulators: [Unity social navigation scene (Pepper), OpenAI Gym Reacher and Cheetah]
  robots: [simulated Pepper]
  environment: simulated room with three humans
  indoor_outdoor: indoor (sim)
  sensors: [lidar rays (sim)]
  humans: simulated humans; 40 MTurk raters (20 per condition after exclusions)
  n_scenes: 1 social navigation scene
  n_trajectories: 400 preferences per condition
  n_participants: 43 recruited, 40 retained
  split: NA
  baselines: [preference-only reward learning]
  ablation: Yes (loss components)
  real_robot_trials: 'No'
  human_study: Human raters provided training feedback (not an evaluation of the final policy)
  statistical_testing: Not reported for social navigation
  scenarios: [robot navigating between three humans to a goal]
metrics: [OTHER | Learned-reward convergence | normalised reward | reward of learned policy vs baseline | p.7, VLM | LLM extraction accuracy | qualitative examples | mapping of text to features (Table 3) | p.6]
deployment: {fm_model: GPT-4 (training-time only), model_size: Not reported, api_cloud_local: Cloud API, onboard_offboard: Simulation, gpu: Not reported, cpu: Not reported, latency: Not reported, query_frequency: Not reported, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Not reported, caching: Not reported, event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: Not reported, safety_shield: Social force model repulsion in the robot controller ("to ensure safety"), emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: 'No', real_time_claim_supported: NA}
repro: {code: Not reported, code_url: Not reported, dataset: Not reported, dataset_url: Not reported, checkpoints: Not reported, prompts_published: Not reported, hardware_specified: Not reported, hyperparameters: Not reported, protocol_described: Not reported, project_page: 'https://sites.google.com/view/rl-predilect', concerns: Simulation only; LLM role limited to text parsing; social metrics not reported.}
limitations_flags: [limited-scenarios, no-human-study]
web_verification_required: []
cited_missing: [Preference-based RL (Christiano et al.), B-Pref]
external_verification: {verified_on: '2026-10-19', status_class: 'A: published, peer-reviewed', source: Crossref DOI 10.1145/3610977.3634970, arxiv_id: 2402.15420v1}
stage2: {added: true, download_source: 'https://arxiv.org/pdf/2402.15420v1', source_type: arXiv (ACM DL PDF returned HTTP 403), inclusion_reason: 'LLM-shaped reward learning for socially compliant navigation; peer-reviewed (HRI 2024); before Cai cut-off, not cited by Cai.'}
coding: {latency_reported: 'No', safety_mechanism: 'Yes', uncertainty_treatment: 'No', hallucination_treatment: 'No', code_released: 'No', new_dataset_released: NA, real_robot: 'No', human_subject_study: Text-raters/other}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1]
  C_capabilities: {SAF1: 'No', SAF2: 'No', SPA1: Partial, SPA2: 'No', SPA3: 'No', SPA4: 'No', HUM1: 'No', HUM2: 'No', NOR1: 'No', NOR2: 'No', NOR3: Partial, NOR4: 'No', EXP1: Partial, EXP2: 'No', EXP3: 'No'}
  B_roles: [R4]
  D_interface: [D7]
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: none, EV4_real_humans_in_trials: simulated-only, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: 400 preferences per condition, statistical_testing: Not reported for social navigation, cross_environment: No/unclear, runtime_measured: 'No'}
  cross_cutting: {temporal_coupling: training-only, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'Yes', uncertainty: 'No', hallucination_mitigation: 'No', privacy_constraint: 'No', inference_location: n/a (FM used at training time only)}
physical_source_folder: "04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core"
analytical_category: "S4"
coding:
  latency_reported: "No"
  safety_mechanism: "Yes"
  uncertainty_treatment: "No"
  hallucination_treatment: "No"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "No"
  human_subject_study: "Text-raters/other"
---

# PREDILECT (Holk, Marta, Leite; HRI 2024)

Page convention: PDF index of the corpus copy (arXiv v1).

## A. Bibliographic
HRI 2024, pp. 259-268, DOI 10.1145/3610977.3634970 (Crossref-verified). KTH. Peer-reviewed: Yes.

## B. Position
S4 direct, early (Feb 2024) example of an LLM acting as a **reward-shaping intermediary** between human language feedback and social-navigation policy learning (I6).

## C-D. Problem and method
Preference-based RL needs many queries; text explanations add information. GPT-4 detects features (speed, distance to humans, goal distance) and sentiment in explanations; highlights reshape reward-learning losses.

## G. Social capabilities
C3 Partial (distance-to-human feature in reward) · C21 Partial (raters asked to judge comfort) · C24 Partial · others No.

## H/I. I6; E2.

## L. Results
With real MTurk feedback, PREDILECT converges to reward just above 0.8 vs lower for preference-only baseline; reports policies emphasising safety when only safety features are used.

## N. Limitations
Observable: simulation only; social outcomes (distances, discomfort) not reported numerically in the main text read; MTurk raters judged videos as training signal.

## P. Direct-paper questions (abridged)
1 Learning socially compliant navigation from human preferences + language. 3 GPT-4. 6 Feature highlights. 7 Reward learning. 10 SFM repulsion. 23 Simulation. 24 Human feedback for training only.

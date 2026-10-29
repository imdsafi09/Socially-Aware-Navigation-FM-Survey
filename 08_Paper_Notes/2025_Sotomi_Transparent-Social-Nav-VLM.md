---
id: 2025_Sotomi_Transparent-Social-Nav-VLM
source_pdfs: [04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/Transparent-Social-Nav-VLM_arXiv2504.05477v1.pdf]
duplicate_copies: []
related_versions: ['arXiv:2504.05477v1 (7 Apr 2025), title "Trust Through Transparency: Explainable Social Navigation for Autonomous Mobile Robots via Vision-Language Models" = corpus copy; published at RO-MAN 2025 under the title "Transparent Social Navigation for Autonomous Mobile Robots Via Vision-Language Models"']
title: Transparent Social Navigation for Autonomous Mobile Robots Via Vision-Language Models
authors: [Oluwadamilola Sotomi, Devika Kodi, Aliasghar Arab]
year: 2025
venue: 2025 34th IEEE International Conference on Robot and Human Interactive Communication (RO-MAN)
volume: NA
issue: NA
pages: 1646-1651
doi: 10.1109/RO-MAN63969.2025.11217693
url: https://doi.org/10.1109/RO-MAN63969.2025.11217693
pub_status: conference (corpus copy is arXiv preprint with different title)
peer_reviewed: 'Yes'
peer_review_basis: 'Crossref record: RO-MAN 2025, pp. 1646-1651, DOI 10.1109/RO-MAN63969.2025.11217693, same three authors (verified 2026-10-19). Published title differs from arXiv title.'
category: S4
folder: 04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core
folder_category_match: 'Yes'
category_rationale: VLM/LLM pipeline (BLIP captions + Grad-CAM + GPT-3.5) detects social conflicts during navigation and explains the robot's socially motivated re-planning to people; user survey on trust. Primary contribution is explanation of social-navigation behaviour (TAXONOMY_REVIEW_REQUIRED).
paper_type: method + user study
fm_used: 'Yes'
fm_class: [VLM, LLM]
fm_models: [BLIP (captioning), 'GPT-3.5 Turbo (explanation generation, remote API)']
fm_size: Not reported
method_family: [captioning, Grad-CAM saliency, prompted explanation generation, ROS2 modules]
roles: [F1, F2]
roles_evidence: {F1: BLIP captions the robot view; VLM node detects potential social conflict (p.4)., F2: 'Conflict detection concerns ongoing human interactions (e.g., people conversing) (Eq.5).', Other: Explanation/communication of navigation decisions to bystanders - not represented in F1-F11 (TAXONOMY_REVIEW_REQUIRED).}
integration: I2
integration_rationale: Conflict flag triggers a path update in the navigation stack (Algorithm 1); explanations are output to people, not consumed by the planner. Mechanism of re-planning not specified (low confidence).
evidence: E4
evidence_rationale: Real robot (MYAGV, 14 m delivery task, 4 runs averaged per condition) with and without explanations, plus post-run survey of N=30 observers on trust/clarity (p.5); no inferential statistics.
inputs: [RGB image (every 5 s)]
outputs: [natural-language explanation (speech + display), heatmap overlay, conflict flag]
human_repr: [caption-level description of people, saliency heatmap]
capabilities: {C1: 'No', C2: 'No', C3: Partial, C4: Partial, C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: 'No', C10: Partial, C11: 'No', C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: 'No', C18: Partial, C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: 'No', C24: Partial, C25: 'No'}
exp:
  datasets: [196 evaluated images for explanation accuracy]
  simulators: []
  robots: ['MYAGV mobile robot (Raspberry Pi 4B, camera, speaker, display)']
  environment: hallway and maker-space
  indoor_outdoor: indoor
  sensors: [RGB camera]
  humans: people in the environment; 30 survey participants (students and faculty)
  n_scenes: 2 tests (manual / autonomous navigation)
  n_trajectories: average of 4 runs per condition
  n_participants: '30'
  split: NA
  baselines: [same robot without explanations]
  ablation: With vs without explainability
  real_robot_trials: 'Yes'
  human_study: Yes (post-run survey of observers)
  statistical_testing: No (percentages; preference score)
  scenarios: [14 m delivery task near people]
metrics: ['NAV | Total trajectory / total time | m / s | per test, average of 4 runs | p.5', SOCIAL | Social conflicts detected / sudden stops | count | per run | p.5, HUMAN | Survey agreement and preference score PS | % | PS = (U + 0.5N)/T x 100 over 30 participants | p.5, VLM | Explanation accuracy | % | confusion matrix over 196 images (82.14%) | p.1, 'DEPLOY | Explanation latency | s | 5.986-50.688 s, mean ~20 s over 88 samples | p.5']
deployment: {fm_model: BLIP (local) + GPT-3.5 Turbo (cloud), model_size: Not reported, api_cloud_local: Hybrid (cloud LLM), onboard_offboard: Raspberry Pi 4B robot; explainability module on separate system, gpu: None reported, cpu: 'Raspberry Pi 4 Model B (quad-core Cortex-A72, 4 GB)', latency: ~20 s mean explanation latency (6-51 s), query_frequency: Image every 5 s / manual trigger, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Not reported, caching: Not reported, event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: Not reported, safety_shield: Not described, emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: 'No', real_time_claim_supported: No (authors acknowledge latency)}
repro: {code: Not reported, code_url: Not reported, dataset: Not reported, dataset_url: Not reported, checkpoints: Not reported, prompts_published: Yes (LLM guiding prompt in paper), hardware_specified: 'Yes', hyperparameters: Not reported, protocol_described: Not reported, project_page: Not reported, concerns: '"Significant" improvements claimed without statistical tests; 4 runs; explanation latency far above navigation time scales.'}
limitations_flags: [latency, cloud-dependence, limited-scenarios, resource-requirements]
web_verification_required: []
cited_missing: [XAI for robotic vehicles (authors prior work), Grad-CAM, BLIP]
external_verification: {verified_on: '2026-10-19', status_class: 'A: published, peer-reviewed', source: Crossref DOI 10.1109/RO-MAN63969.2025.11217693 (title differs from arXiv), arxiv_id: 2504.05477v1}
stage2: {added: true, taxonomy_review_required: Explanation/transparency of social-navigation decisions is not represented by F1-F11 or C1-C25., download_source: 'https://arxiv.org/pdf/2504.05477v1', source_type: 'arXiv (pre-publication version, different title)', inclusion_reason: Explanation directly tied to socially aware navigation behaviour; peer-reviewed; human evaluation.}
coding: {latency_reported: 'Yes', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: 'No', code_released: 'No', new_dataset_released: NA, real_robot: Systematic, human_subject_study: 'Yes'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A5, A6]
  C_capabilities: {SAF1: 'No', SAF2: 'No', SPA1: Partial, SPA2: Partial, SPA3: 'No', SPA4: 'No', HUM1: 'No', HUM2: 'No', NOR1: 'No', NOR2: 'No', NOR3: Partial, NOR4: 'No', EXP1: Partial, EXP2: Partial, EXP3: 'No'}
  B_roles: [R1, R5]
  D_interface: [D1, D8]
  E_evidence_profile: {EV1_offline: 'Yes', EV2_closed_loop_sim: 'No', EV3_physical_robot: systematic, EV4_real_humans_in_trials: present-type-unreported, EV5_human_evaluation: observers/video, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: average of 4 runs per condition, statistical_testing: No (percentages; preference score), cross_environment: No/unclear, runtime_measured: 'Yes'}
  cross_cutting: {temporal_coupling: per-decision, memory: 'No', continual_adaptation: 'No', explanation_output: Yes (human-facing), safety_guard: 'No', uncertainty: 'No', hallucination_mitigation: 'No', privacy_constraint: 'No', inference_location: hybrid (local + cloud)}
physical_source_folder: "04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core"
analytical_category: "S4"
coding:
  latency_reported: "Yes"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "No"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "Systematic"
  human_subject_study: "Yes"
---

# Transparent Social Navigation via VLMs (Sotomi, Kodi, Arab; RO-MAN 2025)

Page convention: PDF index of the corpus copy (arXiv v1, titled "Trust Through Transparency ...").

## A. Bibliographic
RO-MAN 2025, pp. 1646-1651, DOI 10.1109/RO-MAN63969.2025.11217693 (Crossref-verified). arXiv title differs from the published title; same authors (New York University). Peer-reviewed: Yes.

## B. Position
S4 direct. Primary concern: **explanation of social-navigation behaviour** (why the robot re-plans around people), aiming at trust; decision-making itself is thin (conflict flag triggers re-planning). Not generic robot explanation: explanations are generated in the social-navigation loop. **TAXONOMY_REVIEW_REQUIRED**: explanation/communication is not covered by F1-F11 or C1-C25 (closest: C18 legibility). No new class created.

## C. Problem
AMRs do not communicate their decisions; trust suffers (p.1). Social norm constraints formalised (Eq.3-5: social distance, acceleration near people, not disrupting interacting groups).

## D. Method
ROS2 nodes: camera -> BLIP caption -> Grad-CAM heatmap -> GPT-3.5 explanation (prompt in paper) -> speech + display; conflict detection triggers re-planning (Algorithm 1).

## G. Social capabilities
C10 Partial (avoid interrupting people conversing, Fig. 1) · C3 Partial (formulated, not measured) · C4 Partial (trust/understanding ratings, not perceived-safety scales) · C18 Partial (explanations make decisions understandable) · C24 Partial · others No.

## H/I. I2 (low confidence); E4 (observer survey, no statistics).

## L. Results
With explanations: time 22.6 vs 25.3 s, sudden stops 18 vs 21 (autonomous, 4-run averages); survey: 73.3% agree explanations helped understanding, PS 76.7%; explanation accuracy 82.14% (196 images); latency mean ~20 s.

## N. Limitations
1. Stated: proof of concept; latency on Raspberry Pi; future edge/distributed computing (p.4).
2. Observable: "significant" increases without tests; tiny run counts; explanation delays (~20 s) exceed interaction time scales.

## P. Direct-paper questions (abridged)
1 Explainable social navigation for trust. 3 BLIP + GPT-3.5. 6 Natural-language explanations. 10 Not described. 21 ~20 s. 23 Real robot. 24 Yes (N = 30 survey).

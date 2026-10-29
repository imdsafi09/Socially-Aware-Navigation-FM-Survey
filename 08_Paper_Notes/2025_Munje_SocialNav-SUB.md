---
id: 2025_Munje_SocialNav-SUB
source_pdfs: [06_Datasets_Benchmarks_Evaluation/munje25a.pdf]
duplicate_copies: []
related_versions: []
title: 'SocialNav-SUB: Benchmarking VLMs for Scene Understanding in Social Robot Navigation'
authors: &id001 [Michael J. Munje, Chen Tang, Shuijing Liu, Zichao Hu, Yifeng Zhu, Jiaxun Cui, Garrett Warnell, Joydeep Biswas, Peter Stone]
year: 2025
venue: Proceedings of The 9th Conference on Robot Learning (CoRL 2025), PMLR 305
volume: NA
issue: NA
pages: 1120-1143
doi: Not found / not applicable
url: https://proceedings.mlr.press/v305/munje25a.html
pub_status: conference; benchmark/dataset
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): PMLR proceedings page (https://proceedings.mlr.press/v305/munje25a.html); arXiv abs page (2509.08757v1). PDF-derived basis (Stage 1): CoRL 2025 footer (p.1).'
category: S6
folder: 06_Datasets_Benchmarks_Evaluation
folder_category_match: 'Yes'
category_rationale: VQA benchmark and human-labelled dataset evaluating VLM scene understanding (spatial, spatiotemporal, social reasoning) in real social navigation scenarios from SCAND.
paper_type: benchmark; dataset
fm_used: 'Yes'
fm_class: [VLM]
fm_models: [Gemini 2.0, Gemini 2.5, GPT-4o, OpenAI o4-mini, LLaVA-Next-Video]
fm_size: Not reported
method_family: [VQA benchmarking, chain-of-thought prompting, visual prompting (numbered markers + BEV)]
roles: [F1, F2, F11]
roles_evidence: {F11: Benchmark evaluates VLMs as scene interpreters against human responses (p.5-7)., F1: Spatial and spatiotemporal reasoning questions about pedestrians' positions/motions (p.5)., F2: 'Social reasoning questions about whether/how robot and pedestrians interact and pedestrians'' intentions (goal obstruction, robot action to person) (p.5, App.7.6).'}
integration: I0
integration_rationale: Offline VQA; preliminary waypoint-selection probe (App.7.1) is also offline (selection vs human operator's future position).
evidence: E0
evidence_rationale: Offline VQA on 60 SCAND scenarios with human-labelled ground truth; no closed-loop navigation (p.5-8).
inputs: ['RGB image sequence (2.5 s at 4 Hz, 10 frames)', BEV with tracked pedestrian positions, numbered visual markers, multiple-choice questions]
outputs: [VQA answer (multiple choice), waypoint selection (appendix)]
human_repr: [tracked pedestrian with numbered marker, 3D position estimated by PHALP + Kalman smoothing, BEV trajectory, 'human-labelled relations (obstruction, robot action to person)']
capabilities: {C1: 'No', C2: 'No', C3: 'No', C4: 'No', C5: Partial, C6: Partial, C7: Partial, C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: Partial, C13: Partial, C14: 'No', C15: 'No', C16: 'No', C17: Partial, C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: 'No', C24: 'No', C25: 'No'}
exp:
  datasets: ['SCAND (60 curated scenarios; 4,968 unique questions)', CODa (pose pipeline validation)]
  simulators: []
  robots: []
  environment: 'university campus (SCAND): outdoor walkways, narrow doorways/corridors, sidewalks, street crossings'
  indoor_outdoor: both
  sensors: [RGB, odometry]
  humans: real (recorded); 1-13 pedestrians per scene (mean 6.65, SD 2.80)
  n_scenes: 60 scenarios
  n_trajectories: NA
  n_participants: 153 Prolific participants (>=5 per scenario), IRB-approved
  split: NA
  baselines: [Human Oracle, Average Human, Rule-Based]
  ablation: Yes (CoT, BEV, spatial context; waypoint selection with context sources)
  real_robot_trials: 'No'
  human_study: Yes (annotation study, not robot-behaviour evaluation)
  statistical_testing: Partial (standard errors reported)
  scenarios: [crowd, doorway, corridor, sidewalk, street crossing, blind corner]
metrics: [VLM | Probability of Agreement (PA) | 0-1 | mean fraction of human answers matching evaluated answer | p.5, VLM | Consensus-Weighted PA (CWPA) | ratio | agreements scaled by 1/(fraction choosing modal answer) | p.6, VLM | Failure rate (FR) | % | model answer received zero human probability | App. p.19, VLM | Waypoint selection accuracy | % | agreement with human operator's future waypoint (5 runs) | App. p.14]
deployment: {fm_model: NA, model_size: NA, api_cloud_local: API models + local LLaVA-Next-Video, onboard_offboard: NA, gpu: Not reported, cpu: NA, latency: Not reported, query_frequency: NA, planner_frequency: NA, controller_frequency: NA, asynchronous: NA, caching: NA, event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: NA, safety_shield: NA, emergency_behavior: NA, uncertainty: Human-answer distribution used to weight evaluation, hallucination_mitigation: NA, real_time_claim_supported: NA}
repro: {code: Yes (stated), code_url: 'https://larg.github.io/socialnav-sub', dataset: 'Yes', dataset_url: 'https://larg.github.io/socialnav-sub', checkpoints: NA, prompts_published: Yes (Fig.8 full prompt; question table), hardware_specified: 'No', hyperparameters: Default VLM hyperparameters, protocol_described: 'Yes', project_page: 'https://larg.github.io/socialnav-sub', concerns: Single query per question (no sampling variance); campus-only.}
limitations_flags: [dataset-bias, spatial-reasoning-failure, limited-scenarios]
web_verification_required: []
cited_missing: ['SPACE: Does spatial cognition emerge in frontier models? (2024)', VIVA benchmark, PHALP, Moussaid 2010 pedestrian social groups, HEIGHT, Mobility VLA, LeLaN, SPARKLE, HuBo-VLM]
dataset: {kind: benchmark (VQA) + human-labelled dataset, real_synthetic: real, size: '60 scenarios; 4,968 questions; >=5 human answers each', environments: UT Austin campus (SCAND), sensors: robot front RGB + odometry; derived BEV, ego_view: 'Yes', rgb: 'Yes', rgbd: 'No', lidar: No (not used), human_trajectories: 'Yes (estimated 3D, Kalman-smoothed; ADE 0.67 m on CODa)', dynamic_humans: 'Yes', group_ann: 'No', intention_ann: 'Yes (social reasoning questions: obstruction, robot action to person)', activity_ann: 'No', language_ann: Yes (multiple-choice VQA), social_rule_ann: Partial, preference_ann: Yes (distribution of human answers), multi_action_ann: Partial (human answer distributions capture disagreement), personal_space_ann: 'No', site_diversity: Single campus, closed_loop: 'No', vlm_suitability: High (designed for VLMs), real_robot_compat: 'No', standard_metrics: 'PA, CWPA', known_limitations: Single campus; limited models/scenarios (authors)}
coding: {latency_reported: 'No', safety_mechanism: NA, uncertainty_treatment: Partial, hallucination_treatment: NA, code_released: 'Yes', new_dataset_released: 'Yes', real_robot: 'No', human_subject_study: Text-raters/other}
pdf_metadata_stage1:
  year: 2025
  authors: *id001
  venue: 9th Conference on Robot Learning (CoRL 2025), Seoul (PMLR)
  volume: Not reported
  issue: Not reported
  pages: 24 (PDF); 1120-1143 per citing papers
  doi: Not reported
  url: https://larg.github.io/socialnav-sub
  pub_status: conference; benchmark/dataset
  peer_reviewed: 'Yes'
  peer_review_basis: CoRL 2025 footer (p.1).
project_url: https://larg.github.io/socialnav-sub
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: Proceedings of The 9th Conference on Robot Learning (CoRL 2025), PMLR 305
  verified_doi: Not found / not applicable
  verified_url: https://proceedings.mlr.press/v305/munje25a.html
  verified_pages: 1120-1143
  arxiv: 2509.08757v1
  version_relationship: Corpus copy is the PMLR published version; arXiv 2509.08757v1 alternate
  sources: ['PMLR proceedings page (https://proceedings.mlr.press/v305/munje25a.html)', arXiv abs page (2509.08757v1)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A2, A4]
  C_capabilities: {SAF1: 'No', SAF2: 'No', SPA1: 'No', SPA2: 'No', SPA3: Partial, SPA4: Partial, HUM1: Partial, HUM2: Partial, NOR1: 'No', NOR2: 'No', NOR3: 'No', NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'No', EV3_physical_robot: none, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: text-raters, EV6_open_world_deployment: 'No'}
physical_source_folder: "06_Datasets_Benchmarks_Evaluation"
analytical_category: "S6"
coding:
  latency_reported: "No"
  safety_mechanism: "NA"
  uncertainty_treatment: "Partial"
  hallucination_treatment: "NA"
  code_released: "Yes"
  new_dataset_released: "Yes"
  real_robot: "No"
  human_subject_study: "Text-raters/other"
---

# SocialNav-SUB (Munje et al., CoRL 2025)

Page convention: PDF index (p.N).

## A. Bibliographic — CoRL 2025 (PMLR; cited as pp.1120–1143). UT Austin, ARL, Sony AI. Project/code/data https://larg.github.io/socialnav-sub. Peer-reviewed.

## B. Position — S6. The corpus's principal benchmark for *social scene understanding* by VLMs; provides quantitative evidence that VLM reasoning ≠ human-level social scene understanding.

## C. Research problem — whether VLMs can understand complex social navigation scenes (spatial/spatiotemporal relations, intentions); prior evaluations limited to controlled scenarios (p.1–2). Contributions: human-labelled VQA dataset (4,968 questions), first VQA benchmark for social robot navigation (60 SCAND scenarios), experiments with SOTA VLMs vs human and rule-based baselines (p.2–3).

## D. Method — SCAND scene mining (weighted score of crowd size, near-robot pedestrians, lateral robot motion); PHALP tracking + 3D pose, Kalman smoothing, projection to front view and BEV with numbered markers; 2.5 s segments at 4 Hz; multiple-choice questions in spatial / spatiotemporal / social categories; ≥5 human answers per scenario; metrics PA and CWPA (Eq.1–2); baselines Human Oracle (modal answer), Average Human, Rule-Based (hand-crafted rules on positions); CoT prompting by sequential questioning (p.4–7).

## L. Quantitative results (Table 1, p.7; PA / CWPA)
| Model | All | Spatial | Spatiotemporal | Social |
|---|---|---|---|---|
| Human Oracle | 0.74 / 1.0 | 0.71 / 1.0 | 0.73 / 1.0 | 0.76 / 1.0 |
| Average Human | 0.60 / 0.80 | 0.56 / 0.79 | 0.59 / 0.80 | 0.62 / 0.81 |
| Rule-Based | 0.64 / 0.84 | 0.57 / 0.79 | 0.62 / 0.84 | 0.71 / 0.92 |
| Gemini 2.0 | 0.58 / 0.79 | 0.55 / 0.77 | 0.46 / 0.64 | 0.63 / 0.84 |
| Gemini 2.5 | 0.54 / 0.73 | 0.51 / 0.72 | 0.52 / 0.73 | 0.55 / 0.73 |
| GPT-4o | 0.50 / 0.69 | 0.56 / 0.79 | 0.51 / 0.71 | 0.47 / 0.63 |
| o4-mini | 0.62 / 0.82 | 0.54 / 0.74 | 0.59 / 0.79 | 0.66 / 0.87 |
| LLaVA-Next-Video | 0.46 / 0.61 | 0.35 / 0.46 | 0.58 / 0.79 | 0.48 / 0.62 |
(All ± ≤0.01 standard error.)
Table 2 ablation (PA spatial / spatiotemporal / social): GPT-4o CoT+BEV 0.56/0.51/0.47, No CoT 0.58/0.53/0.35, No BEV 0.51/0.44/0.42; LLaVA-Next-Video 0.35/0.58/0.48, 0.35/0.58/0.38, 0.35/0.61/0.46; Gemini 2.0 0.55/0.46/0.63, 0.56/0.48/0.58, 0.56/0.46/0.64.
Table 3 (App., waypoint selection accuracy vs human operator; No context / Random / Same-model / Human-oracle context): o4-mini 36.14±1.31 / 30.88±2.12 / 38.95±1.51 / 46.32±1.19 %; Gemini 2.0 37.19±4.75 / 34.74±4.09 / 41.05±2.58 / 46.67±3.62 %; Gemini 2.5 34.39±1.97 / 32.28±1.72 / 37.19±1.70 / 42.11±2.88 %.
Failure rates (App. Table 4, overall): o4-mini 6.42%, GPT-4o 23.63%, LLaVA-Next 33.78%, Gemini 2.0 15.00%, Gemini 2.5 9.02%; "yielding to" answers have high FR (e.g., GPT-4o 84.85%).
- Key finding (authors): best VLM (o4-mini) underperforms rule-based and human-oracle baselines; VLMs closer to humans in social than spatial reasoning (p.7).
- Pose pipeline ADE 0.67 ± 0.14 m on CODa (App.7.3). Human study: 153 participants, age 18–80 (mean 37.70), 44% male / 54% female / 2% other (App.7.4).

## N. Limitations — 1. Stated (p.9): single campus (SCAND); limited models and scenarios. 2. Future: more datasets, fine-tuning on the human data, spatially fine-tuned/social VLMs, hybrid approaches. 3. Observable: single query per question; Table 2 text refers to "Table 13" (typo); offline.

## P. Dataset analysis — see `dataset:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue Proceedings of The 9th Conference on Robot Learning (CoRL 2025), PMLR 305; DOI Not found / not applicable; pages 1120-1143; URL https://proceedings.mlr.press/v305/munje25a.html.
- Sources: PMLR proceedings page (https://proceedings.mlr.press/v305/munje25a.html); arXiv abs page (2509.08757v1).
- Version relationship: Corpus copy is the PMLR published version; arXiv 2509.08757v1 alternate.
- Changed field - venue: PDF-derived '9th Conference on Robot Learning (CoRL 2025), Seoul (PMLR)' -> externally verified 'Proceedings of The 9th Conference on Robot Learning (CoRL 2025), PMLR 305'
- Changed field - volume: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - issue: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - pages: PDF-derived '24 (PDF); 1120-1143 per citing papers' -> externally verified '1120-1143'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified 'Not found / not applicable'
- Changed field - url: PDF-derived 'https://larg.github.io/socialnav-sub' -> externally verified 'https://proceedings.mlr.press/v305/munje25a.html'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

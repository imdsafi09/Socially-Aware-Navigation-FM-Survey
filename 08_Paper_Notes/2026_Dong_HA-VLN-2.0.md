---
id: 2026_Dong_HA-VLN-2.0
source_pdfs: [05_Direct_VLM_SocialNav_Preprints/2503.14229v5.pdf]
duplicate_copies: [06_Datasets_Benchmarks_Evaluation/2503.14229v5.pdf]
related_versions: ['Predecessor: HA-VLN 1.0 (NeurIPS 2024 D&B) - see 2024_Li_HA-VLN']
title: 'HA-VLN 2.0: An Open Benchmark and Leaderboard for Human-Aware Navigation in Discrete and Continuous Environments with Dynamic Multi-Human Interactions'
authors: &id001 [Yifei Dong, Fengyi Wu, Qi He, Lingdong Kong, Heng Li, Minghan Li, Zebang Cheng, Yuxuan Zhou, Jingdong Sun, Qi Dai, Alexander G. Hauptmann, Zhi-Qi Cheng]
year: 2026
venue: arXiv:2503.14229v5 [cs.AI], 18 Aug 2026 (document dated July 10, 2026)
volume: NA
issue: NA
pages: '35'
doi: Not found / not applicable
url: https://arxiv.org/abs/2503.14229
pub_status: accepted per author statement; not yet indexed
peer_reviewed: Accepted (not yet indexed)
peer_review_basis: 'Externally verified (2026-10-19): arXiv abs page (2503.14229v5): v5 (18 Aug 2026) comment "Accepted to IROS 2026"; Crossref title search: no match; OpenReview shows only a withdrawn ICLR 2026 submission; IROS 2026 proceedings not yet indexed.'
category: S6
folder: 05_Direct_VLM_SocialNav_Preprints (copy also in 06_Datasets_Benchmarks_Evaluation)
folder_category_match: Partial
category_rationale: Benchmark/simulator/dataset/leaderboard for human-aware VLN in discrete and continuous settings; LLMs used offline to generate instructions and multi-human scenarios; benchmarks VLM/VLA navigation agents (NaVid, NaVILA) zero-shot.
paper_type: benchmark; dataset; simulator
fm_used: 'Yes'
fm_class: [LLM]
fm_models: [ChatGPT-4o and LLaMA-3-8B-Instruct (instruction and multi-human scenario generation; description QC), MDM (text-to-motion), 'Evaluated agents incl. NaVid and NaVILA (video-VLM/VLA navigation models, zero-shot)']
fm_size: 8B (LLaMA-3); others not reported
method_family: [imitation learning (Recurrent VLN-BERT based HA-VLN-VL), 'cross-modal attention (HA-VLN-CMA with EnvDrop, DAgger)', PSO-based human placement]
roles: [F11]
roles_evidence: {F11: 'ChatGPT-4o/LLaMA-3-8B-Instruct generate HA-R2R socially grounded instructions and multi-human scenario descriptions with human refinement (p.5-7, App.C.2).'}
integration: I0
integration_rationale: Paper's own FM use is offline data generation; navigation baselines are learned VLN policies. (Benchmark separately evaluates VLA-type agents NaVid/NaVILA zero-shot.)
evidence: E3
evidence_rationale: Closed-loop simulation benchmark plus real-world Unitree Go2-EDU deployment in 4 indoor layouts x 3 instances, 30 episodes each, with 2-4 free-moving volunteers; no human-subject evaluation (p.10, App.D).
inputs: [RGB, depth, natural language instruction]
outputs: ['discrete/continuous actions (forward 0.25 m, turn 15 deg, stop)']
human_repr: [SMPL motion sequences with region-grounded activities, multi-human interaction groups (2-4 persons), bounding volumes for collision, personal-space thresholds (3 m DE; overlapping radii CE), language description of human activities]
capabilities: {C1: 'Yes', C2: Partial, C3: Partial, C4: 'No', C5: Partial, C6: 'No', C7: 'No', C8: Partial, C9: Partial, C10: Partial, C11: Partial, C12: Partial, C13: 'No', C14: Partial, C15: 'No', C16: 'No', C17: Partial, C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: Partial, C24: Partial, C25: 'No'}
exp:
  datasets: ['HAPS 2.0: 486 SMPL motion models (172 aligned motions), 26 regions, 58,320 frames; 910 human models across 428 regions in 90 scans (111 outdoor, 72 two-person, 59 three-person, 15 four-person groups)', 'HA-R2R: 16,844 instructions (train 10,819 / val_seen 778 / val_unseen 1,839 / test 3,408; test across 18 withheld buildings)']
  simulators: ['HA-VLN-CE (continuous, Habitat-based navmesh)', 'HA-VLN-DE (discrete, extends HA3D)']
  robots: ['Unitree Go2-EDU (RealSense D435i, MID360 LiDAR, IMU)']
  environment: indoor (Matterport3D) + some outdoor regions; real office, living room, hallway, lobby
  indoor_outdoor: both
  sensors: [RGB-D, 3D LiDAR (real robot), IMU]
  humans: simulated multi-human (up to 10 per scene in CE); 2-4 free-moving volunteers (real)
  n_scenes: 90 scans; 4 real layout types x 3 instances
  n_trajectories: 16,844 instructions; 30 real episodes per instance
  n_participants: 26 volunteers (HAPS QA); real-world volunteers 2-4 per trial (total not reported)
  split: 10,819/778/1,839/3,408
  baselines: [HA-VLN-CMA-Base, HA-VLN-CMA-DA, HA-VLN-CMA*, HA-VLN-VL, BEVBert, ETPNav, NaVid, NaVILA, Speaker-Follower, Rec (PREVALENT), Rec (OSCAR), Airbert, NavCoT]
  ablation: Yes (human presence vs cylinders, interaction enrichment, step size, RGB/depth, cross-domain)
  real_robot_trials: 'Yes'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [conversational group, multi-human groups, corridor crossing, stairs, doorway, crowded junction]
metrics: ['SAFETY | Total Collision Rate (TCR) | collisions per instance | collisions within 1 m of a human excluding unavoidable critical activities | p.7, App.D.1', 'SAFETY | Collision Rate (CR) | ratio | instances with >=1 collision, normalised by fraction beta of human-affected instructions | App.D.1', NAV | Navigation Error (NE) | m | distance to goal | p.8, NAV | Success Rate (SR) | ratio | stops close to goal AND demonstrates effective obstacle avoidance | p.8, 'NAV | Navigation Success Rate (NSR) | ratio | real-world success over 30 episodes per instance | App.D, Table 10', DEPLOY | Simulation speed | FPS | 30-60 FPS on single 24GB GPU (CE); mesh retrieval <50 ms | p.6]
deployment: {fm_model: NA, model_size: NA, api_cloud_local: LLMs offline, onboard_offboard: Not reported for agents on Go2, gpu: RTX 4090-class 24GB (simulation), cpu: Not reported, latency: Not reported, query_frequency: NA, planner_frequency: NA, controller_frequency: NA, asynchronous: NA, caching: NA, event_triggered: NA, distillation: 'No', quantization: 'No', fallback_planner: 'No', safety_shield: 'No', emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: Iterative prompt refinement + human review of generated instructions, real_time_claim_supported: NA}
repro: {code: 'Yes', code_url: 'https://github.com/UWMILab/HA-VLN', dataset: Yes (stated released), dataset_url: 'https://uwmilab.github.io/HA-VLN-webpage', checkpoints: Not reported, prompts_published: Partial (Listings 3-4), hardware_specified: Partial, hyperparameters: Partial, protocol_described: 'Yes (leaderboard, server-side evaluation)', project_page: 'https://uwmilab.github.io/HA-VLN-webpage', concerns: Ethics statement claims no human subjects despite volunteer trials; 'Use of LLMs' statement contradicts LLM-generated dataset content.}
limitations_flags: [sim-to-real, limited-scenarios]
web_verification_required: [Venue status of HA-VLN 2.0, Leaderboard availability]
cited_missing: [VLN-CE (Krantz 2020), HabiCrowd (Vuong 2024), NaVid, NaVILA, BEVBert, ETPNav, NavCoT, NavGPT, EnvDrop, DAgger]
dataset: {kind: simulator + dataset + benchmark + leaderboard, real_synthetic: synthetic SMPL humans in scanned environments, size: '16,844 instructions; 910 human models; 90 scans', environments: indoor homes (26 region types) + outdoor regions (111 outdoor humans), sensors: RGB-D egocentric, ego_view: 'Yes', rgb: 'Yes', rgbd: 'Yes', lidar: No (sim); real robot has LiDAR, human_trajectories: Yes (SMPL motion with movement; 268 complex motions), dynamic_humans: 'Yes', group_ann: 'Yes (2-, 3-, 4-person interaction groups)', intention_ann: 'No', activity_ann: Yes (172 activity types), language_ann: Yes (socially grounded instructions), social_rule_ann: Partial (instructions say e.g. 'do not disturb'), preference_ann: 'No', multi_action_ann: 'No', personal_space_ann: Partial (thresholds for collision), site_diversity: 90 scans, closed_loop: Yes (DE and CE), vlm_suitability: High (benchmarks NaVid/NaVILA), real_robot_compat: Demonstrated (Unitree Go2), standard_metrics: 'NE, SR, TCR, CR (+ NSR
    real)', known_limitations: Simulated humans scripted (reactivity not described); collisions defined by proximity; real-world results only NSR}
coding: {latency_reported: 'No', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: Partial, code_released: 'Yes', new_dataset_released: 'Yes', real_robot: Systematic, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2026
  authors: *id001
  venue: arXiv:2503.14229v5 [cs.AI], 18 Aug 2026 (document dated July 10, 2026)
  volume: NA
  issue: NA
  pages: '35'
  doi: Not reported
  url: https://uwmilab.github.io/HA-VLN-webpage ; code https://github.com/UWMILab/HA-VLN
  pub_status: preprint; benchmark/dataset
  peer_reviewed: 'No'
  peer_review_basis: arXiv v5 without venue statement (p.1). First arXiv version 2025 (ID 2503); no acceptance stated.
project_url: https://uwmilab.github.io/HA-VLN-webpage ; code https://github.com/UWMILab/HA-VLN
external_verification:
  verified_on: '2026-10-19'
  status_class: 'B: accepted per authors/arXiv; proceedings not yet available'
  verified_venue: arXiv:2503.14229v5 [cs.AI], 18 Aug 2026 (document dated July 10, 2026)
  verified_doi: Not found / not applicable
  verified_url: https://arxiv.org/abs/2503.14229
  verified_pages: NA
  arxiv: 2503.14229v5
  version_relationship: arXiv only; published version not yet available
  sources: ['arXiv abs page (2503.14229v5): v5 (18 Aug 2026) comment "Accepted to IROS 2026"', 'Crossref title search: no match', OpenReview shows only a withdrawn ICLR 2026 submission; IROS 2026 proceedings not yet indexed]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A3, A4, A5]
  C_capabilities: {SAF1: 'Yes', SAF2: Partial, SPA1: Partial, SPA2: Partial, SPA3: Partial, SPA4: Partial, HUM1: Partial, HUM2: Partial, NOR1: Partial, NOR2: Partial, NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: systematic, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "05_Direct_VLM_SocialNav_Preprints"
analytical_category: "S6"
coding:
  latency_reported: "No"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "Partial"
  code_released: "Yes"
  new_dataset_released: "Yes"
  real_robot: "Systematic"
  human_subject_study: "No"
---

# HA-VLN 2.0 (Dong, Wu et al., arXiv v5 2026)

Page convention: PDF index (p.N); 35 pages.

## A. Bibliographic — arXiv:2503.14229v5 (18 Aug 2026); UW, NUS, CMU, MSR; equal contribution in random order. Code https://github.com/UWMILab/HA-VLN; site https://uwmilab.github.io/HA-VLN-webpage. Identical copy in 06. Not peer-reviewed (as of this version).

## B. Position — S6 (benchmark). Extends HA-VLN 1.0 to continuous control, multi-human interactions, outdoor regions, socially grounded instructions and a leaderboard. Highly relevant evaluation resource: the only corpus benchmark that evaluates VLA/video-VLM navigators (NaVid, NaVILA) among dynamic humans.

## C. Research problem — social awareness under-explored in VLN; coarse instructions; static assumptions (p.1). Contributions: standardized task & metrics incl. personal-space adherence; HAPS 2.0 + DE/CE simulators; 16,844 instructions benchmark; real-robot validation + leaderboard (abstract, p.2–3).

## D. Technical method
- HAPS 2.0: original 435 HAPS-1 pairs found >50% misaligned → 2-round manual verification → 172 aligned motions; 486 motion models over 26 regions; ChatGPT-4o-assisted QC (p.5, App.B.1).
- Placement: coarse (semantic object matching + PSO with ≥1 m from objects), fine (9-camera multi-view verification; >430 annotation hours → 529 models in 374 regions), Stage 2 LLM-generated multi-human scenarios with 4 rounds manual review → 910 models in 428 regions (p.5–6).
- Rendering: dual-thread producer–consumer; mesh retrieval <50 ms; CE 30–60 FPS on 24 GB GPU, up to 10 humans/scene (p.6).
- Personal-space enforcement: 3 m threshold in DE; overlapping radii in CE (p.4). Collisions trigger automatic revert (p.6).
- Agents: HA-VLN-VL (Recurrent VLN-BERT, IL), HA-VLN-CMA (BERT + ResNet + MHA; +EnvDrop, +DAgger) (p.7).

## E. Human/social representation — SMPL meshes with activities; multi-human groups; language references; proximity thresholds.

## F. Roles — F11 (offline LLM data generation). ## H. Integration — I0. ## I. Evidence — E3.

## G. Capabilities (benchmark-level)
C1 Yes · C2/C3 Partial (personal-space thresholds as collisions) · C5, C8, C9, C10 Partial (dynamic multi-human activities and groups exist; evaluated only through collisions) · C11, C12, C14, C17, C23, C24 Partial · others No.

## J. Experimental evidence — retrained vs zero-shot on val seen/unseen/test; DE comparisons; ablations; real Go2-EDU, 4 layouts × 3 instances × 30 episodes, w/ and w/o 2–4 volunteers (App.D).

## L. Quantitative results
Table 1 (HA-VLN-CE; visually verified from 260-dpi crop; NE / TCR / CR / SR):
| Agent | Val-seen Retrained | Val-seen Zero-shot | Val-unseen Retrained | Val-unseen Zero-shot | Test Retrained | Test Zero-shot |
|---|---|---|---|---|---|---|
| HA-VLN-CMA-Base | 7.63/63.09/0.77/0.05 | 7.88/63.84/0.75/0.04 | 7.34/47.06/0.77/0.07 | 7.95/63.96/0.76/0.03 | 7.30/47.55/0.76/0.07 | 7.89/62.14/0.74/0.04 |
| HA-VLN-CMA-DA | 6.11/17.45/0.61/0.17 | 6.95/37.85/0.72/0.07 | 7.00/27.25/0.69/0.09 | 7.05/38.22/0.73/0.05 | 7.12/28.33/0.69/0.08 | 6.98/36.53/0.73/0.06 |
| HA-VLN-CMA* | 5.61/3.34/0.60/0.17 | 7.10/29.99/0.69/0.11 | 6.23/8.10/0.69/0.10 | 6.62/32.48/0.70/0.09 | 6.64/9.23/0.72/0.09 | 7.09/31.80/0.75/0.09 |
| HA-VLN-VL | 5.02/4.44/0.52/0.20 | 7.82/3.67/0.45/0.05 | 5.35/6.63/0.59/0.14 | 7.15/3.97/0.46/0.06 | 5.52/5.96/0.63/0.14 | 7.41/3.38/0.58/0.07 |
| BEVBert | 5.53/3.64/0.46/0.27 | 6.11/4.29/0.47/0.19 | 5.51/4.71/0.55/0.21 | 6.10/5.72/0.56/0.15 | 6.33/4.25/0.58/0.18 | 6.54/4.39/0.54/0.14 |
| ETPNav | 5.17/4.07/0.43/0.24 | 7.72/6.31/0.61/0.12 | 5.43/6.94/0.58/0.17 | 7.40/7.94/0.71/0.08 | 5.94/5.96/0.58/0.16 | 7.59/5.64/0.73/0.09 |
| NaVid | – | 6.58/7.92/0.57/0.10 | – | 6.43/10.59/0.67/0.07 | – | 6.72/8.51/0.65/0.08 |
| NaVILA | – | 6.73/5.49/0.53/0.14 | – | 6.26/7.28/0.61/0.10 | – | 6.85/6.37/0.59/0.11 |
- Best test-retrained SR is 0.18 (BEVBert); zero-shot VLA-type models SR ≤ 0.14 with CR ≥ 0.53 — even strong navigation FMs collide frequently in human-populated settings.
Table 2 (DE unseen; VLN NE/SR → HA-VLN-DE NE/TCR/CR/SR): Speaker-Follower 6.62/0.35 → 7.44/0.32/0.72/0.21; Rec(PREVALENT) 3.93/0.63 → 6.12/0.29/0.81/0.33; Rec(OSCAR) 4.29/0.59 → 6.12/0.28/0.78/0.34; Airbert 4.01/0.62 → 5.54/0.30/0.83/0.36; NavCoT 6.26/0.40 → 6.83/0.36/0.85/0.23.
Table 10 (real-world NSR, w/o → w/ humans, 30 episodes × 3 instances): CMA-Base (VLN-CE) ALL 0.26 → 0.09; VL (VLN-CE) 0.40 → 0.12; CMA-Base (HA-VLN) 0.25 → 0.15; VL (HA-VLN) 0.44 → 0.18 (Living Room 0.42/0.17, Office 0.43/0.17, Hallway 0.49/0.20, Lobby 0.43/0.17).
Text: replacing humans with cylinders reduces TCR ~36% and raises SR ~10%; removing interaction enrichment reduces TCR up to 22% and raises SR up to 25% (p.10).

## N. Limitations
1. **Stated:** challenges in tight corridors and sudden crowd convergence; partial observability (p.10, App.D).
2. **Future work:** refined collision forecasting and reactive control (App.D).
3. **Observable:** real-world success ≤ 0.20 with humans; ethics statement says "no human subjects" though volunteers present; App.F says LLMs used only for manuscript rephrasing, contradicting their documented role in dataset generation; proximity thresholds differ DE (3 m) vs CE.

## O. Reproducibility — code, data, leaderboard stated.

## P. Dataset analysis — see `dataset:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: B: accepted per authors/arXiv; proceedings not yet available; venue arXiv:2503.14229v5 [cs.AI], 18 Aug 2026 (document dated July 10, 2026); DOI Not found / not applicable; pages NA; URL https://arxiv.org/abs/2503.14229.
- Sources: arXiv abs page (2503.14229v5): v5 (18 Aug 2026) comment "Accepted to IROS 2026"; Crossref title search: no match; OpenReview shows only a withdrawn ICLR 2026 submission; IROS 2026 proceedings not yet indexed.
- Version relationship: arXiv only; published version not yet available.
- Changed field - doi: PDF-derived 'Not reported' -> externally verified 'Not found / not applicable'
- Changed field - url: PDF-derived 'https://uwmilab.github.io/HA-VLN-webpage ; code https://github.com/UWMILab/HA-VLN' -> externally verified 'https://arxiv.org/abs/2503.14229'
- Changed field - pub_status: PDF-derived 'preprint; benchmark/dataset' -> externally verified 'accepted per author statement; not yet indexed'
- Changed field - peer_reviewed: PDF-derived 'No' -> externally verified 'Accepted (not yet indexed)'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

## Stage-7 status re-check (2026-10-19)
arXiv v5 (18 Aug 2026) states Accepted to IROS 2026; IROS 2026 held 27 Sep-1 Oct 2026; not yet in Crossref/IEEE Xplore. Status unchanged: accepted, not yet indexed. See 09_Project_Reports/PUBLICATION_STATUS_FINAL_CHECK.md.

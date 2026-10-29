---
id: 2024_Li_HA-VLN
source_pdfs: [04_Direct_VLM_SocialNav/B_Peer_Reviewed_Boundary/NeurIPS-2024-human-aware-vision-and-language-navigation-bridging-simulation-to-reality-with-dynamic-human-interactions-Paper-Datasets_and_Benchmarks_Track.pdf]
duplicate_copies: [06_Datasets_Benchmarks_Evaluation/NeurIPS-2024-human-aware-vision-and-language-navigation-bridging-simulation-to-reality-with-dynamic-human-interactions-Paper-Datasets_and_Benchmarks_Track.pdf]
related_versions: ['Successor: HA-VLN 2.0 (arXiv:2503.14229v5) - separate work, see 2025_Dong_HA-VLN-2.0']
title: 'Human-Aware Vision-and-Language Navigation: Bridging Simulation to Reality with Dynamic Human Interactions'
authors: &id001 [Heng Li, Minghan Li, Zhi-Qi Cheng, Yifei Dong, Yuxuan Zhou, Jun-Yan He, Qi Dai, Teruko Mitamura, Alexander G. Hauptmann]
year: 2024
venue: Advances in Neural Information Processing Systems 37 (NeurIPS 2024, Datasets and Benchmarks Track)
volume: NA
issue: NA
pages: 119411-119442
doi: 10.52202/079017-3795
url: https://doi.org/10.52202/079017-3795
pub_status: conference; benchmark/dataset
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.52202/079017-3795); arXiv abs page (2406.19236v3). PDF-derived basis (Stage 1): NeurIPS 2024 Datasets and Benchmarks Track footer (p.1); acknowledges anonymous reviewers (p.11).'
category: S6
folder: 04_Direct_VLM_SocialNav/B_Peer_Reviewed_Boundary (copy also in 06_Datasets_Benchmarks_Evaluation)
folder_category_match: Partial
category_rationale: Primary contribution is a simulator (HA3D), dataset (HA-R2R, HAPS) and benchmark for human-aware VLN; LLM (GPT-4) is used only offline for data generation; agents are BERT/ResNet-based policies, not VLM-reasoning navigation.
paper_type: benchmark; dataset; simulator; method
fm_used: 'Yes'
fm_class: [LLM]
fm_models: [GPT-4 / GPT-4 Turbo (gpt-4-1106-preview) for activity descriptions and instruction generation, MDM motion diffusion model (text-to-motion), BERT embeddings in agents]
fm_size: Not reported
method_family: ['imitation learning (seq2seq LSTM, VLN-CM)', 'decision transformer (VLN-DT, offline RL from random walks)', cross-modal attention fusion]
roles: [F11]
roles_evidence: {F11: 'GPT-4 generates human-activity descriptions (filtered by 50-participant survey) and HA-R2R instructions combining R2R instructions with activity and relative-position info (p.3, p.5, App.C.1).'}
integration: I0
integration_rationale: FM used only offline for dataset construction; navigation agents do not query an LLM/VLM at runtime.
evidence: E2
evidence_rationale: Quantitative closed-loop evaluation in HA3D simulator (validation seen/unseen); real-world Unitree GO1 tests are qualitative demonstrations (success and a collision failure shown) without metrics (p.9-10, App.D.4).
inputs: [RGB-D egocentric (60 deg FOV), natural language instruction]
outputs: [discrete action (forward/left/right/up/down/stop)]
human_repr: [SMPL 3D human mesh with activity (simulation), human-occupied viewpoint nodes, 1 m collision radius, natural-language activity description in instruction]
capabilities: {C1: 'Yes', C2: Partial, C3: Partial, C4: 'No', C5: Partial, C6: 'No', C7: 'No', C8: Partial, C9: 'No', C10: 'No', C11: 'No', C12: Partial, C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: 'No', C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: Partial, C24: Partial, C25: 'No'}
exp:
  datasets: ['HA-R2R: 21,567 instructions, 145 activity types (start 1,047; obstacle 3,666; surrounding 14,469; end 1,041)', 'HAPS: 145 activity descriptions -> 435 SMPL motion models (~422 retained), 52,200 frames', 'Matterport3D (90 buildings, 29 region types)']
  simulators: ['HA3D (Matterport3D + dynamic SMPL humans, 16 FPS activities)']
  robots: ['Unitree GO1-EDU (Jetson TX2, Raspberry Pi 4B, fisheye camera, ultrasonic sensor, IMU)']
  environment: indoor (Matterport3D houses; real office)
  indoor_outdoor: indoor
  sensors: [RGB-D (sim), fisheye RGB (real), ultrasonic, IMU]
  humans: 374 simulated humans (avg 4 per building; 49.2% stationary); real people in office demo
  n_scenes: 90 buildings
  n_trajectories: 21,567 instructions; R2R splits (val seen/unseen)
  n_participants: 50 survey participants (activity description selection)
  split: R2R validation seen / unseen
  baselines: [Speaker-Follower, Rec (PREVALENT), Rec (OSCAR), Airbert, Oracle]
  ablation: Yes (egocentric vs panoramic; optimal vs sub-optimal expert; static vs dynamic; reward strategies; random-walk proportion)
  real_robot_trials: Partial (qualitative)
  human_study: No (survey only for dataset curation)
  statistical_testing: 'No'
  scenarios: [static person, humans in hallway, human activities at nodes, instruction mentioning humans]
metrics: ['SAFETY | Total Collision Rate (TCR) | rate | average collisions within 1 m radius per instance, excluding unavoidable critical-node activities | p.7', SAFETY | Collision Rate (CR) | ratio | instances with >=1 collision / (beta L) | p.7, NAV | Navigation Error (NE) | m | distance final position to target | p.7, NAV | Success Rate (SR) | ratio | completed within range and without collisions | p.7, DEPLOY | Simulator speed | fps | up to 300 fps at 640x480 on RTX 3050; 40 MB memory | p.5]
deployment: {fm_model: NA, model_size: NA, api_cloud_local: GPT-4 offline (data generation), onboard_offboard: Agent on Jetson TX2 (real demo), gpu: Jetson TX2 (robot); RTX 3050 (simulator benchmark), cpu: Raspberry Pi 4B (motion control), latency: Not reported, query_frequency: NA, planner_frequency: NA, controller_frequency: NA, asynchronous: NA, caching: NA, event_triggered: NA, distillation: 'No', quantization: 'No', fallback_planner: 'No', safety_shield: 'No', emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: Human validation of GPT-4 generated instructions/descriptions, real_time_claim_supported: NA}
repro: {code: 'Yes', code_url: 'https://github.com/lpercc/HA3D_simulator', dataset: Yes (HAPS Google Drive link; HA-R2R), dataset_url: 'https://drive.google.com/drive/folders/1aswHATnKNViqw6QenAwdQRTwXQQE5jd3', checkpoints: Not reported, prompts_published: Partial (prompt format Listing 1-2), hardware_specified: 'Yes', hyperparameters: Partial, protocol_described: 'Yes', project_page: 'https://lpercc.github.io/HA3D_simulator/', concerns: Matterport3D access by request; real-robot results qualitative.}
limitations_flags: [sim-to-real, limited-scenarios, no-human-study]
web_verification_required: []
cited_missing: [R2R (Anderson 2018), Habitat 3.0, Sim2Real predictivity (Kadian 2020), Sim-to-real transfer for VLN (Anderson 2021), MDM motion diffusion, SMPL, Decision Transformer, Airbert, Recurrent VLN-BERT, Speaker-Follower]
dataset: {kind: simulator + dataset + benchmark, real_synthetic: synthetic humans in real-scan environments (Matterport3D), size: '21,567 instructions; 435 motion models; 90 buildings; 374 humans', environments: 'indoor homes/buildings, 29 region types', sensors: RGB-D egocentric renders, ego_view: Yes (60 deg), rgb: 'Yes', rgbd: 'Yes', lidar: 'No', human_trajectories: 'Yes (SMPL motion sequences, avg 2.85 m)', dynamic_humans: 'Yes', group_ann: 'No', intention_ann: 'No', activity_ann: Yes (145 activity descriptions), language_ann: Yes (instructions with human activity descriptions), social_rule_ann: 'No', preference_ann: 'No', multi_action_ann: 'No', personal_space_ann: Partial (1 m collision threshold), site_diversity: 90 buildings, closed_loop: 'Yes', vlm_suitability: High (language instructions + egocentric RGB), real_robot_compat: Demonstrated qualitatively (Unitree GO1), standard_metrics: 'NE, SR, TCR, CR', known_limitations: Humans do not react to agent; no social nuances or group
    dynamics; indoor only (authors)}
coding: {latency_reported: 'No', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: Partial, code_released: 'Yes', new_dataset_released: 'Yes', real_robot: Demo, human_subject_study: Text-raters/other}
pdf_metadata_stage1:
  year: 2024
  authors: *id001
  venue: 38th Conference on Neural Information Processing Systems (NeurIPS 2024), Track on Datasets and Benchmarks
  volume: Not reported
  issue: Not reported
  pages: 32 (incl. appendix)
  doi: Not reported
  url: https://lpercc.github.io/HA3D_simulator/
  pub_status: conference; benchmark/dataset
  peer_reviewed: 'Yes'
  peer_review_basis: NeurIPS 2024 Datasets and Benchmarks Track footer (p.1); acknowledges anonymous reviewers (p.11).
project_url: https://lpercc.github.io/HA3D_simulator/
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: Advances in Neural Information Processing Systems 37 (NeurIPS 2024, Datasets and Benchmarks Track)
  verified_doi: 10.52202/079017-3795
  verified_url: https://doi.org/10.52202/079017-3795
  verified_pages: 119411-119442
  arxiv: 2406.19236v3
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.52202/079017-3795)', arXiv abs page (2406.19236v3)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A5]
  C_capabilities: {SAF1: 'Yes', SAF2: Partial, SPA1: Partial, SPA2: 'No', SPA3: Partial, SPA4: 'No', HUM1: Partial, HUM2: Partial, NOR1: 'No', NOR2: Partial, NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: demo, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: text-raters, EV6_open_world_deployment: 'No'}
physical_source_folder: "04_Direct_VLM_SocialNav/B_Peer_Reviewed_Boundary"
analytical_category: "S6"
coding:
  latency_reported: "No"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "Partial"
  code_released: "Yes"
  new_dataset_released: "Yes"
  real_robot: "Demo"
  human_subject_study: "Text-raters/other"
---

# HA-VLN: Human-Aware Vision-and-Language Navigation (Li et al., NeurIPS 2024 D&B)

Page convention: PDF index (p.N); 32 pages incl. appendices.

## A. Bibliographic
NeurIPS 2024 Datasets & Benchmarks Track; CMU, Columbia, Mannheim, Alibaba, MSR. Equal-contribution authors in random order (p.1). Project https://lpercc.github.io/HA3D_simulator/. Identical copy in 06 (md5). Peer-reviewed: Yes.

## B. Position — **S6 (benchmark/dataset); folder 04B boundary**
Extends VLN to dynamic human-populated environments. FM role limited to offline LLM data generation; runtime agents are BERT/ResNet policies. Relevant to the survey as an evaluation resource bridging VLN and human-aware navigation; not a VLM-reasoning social navigation method.

## C. Research problem
Relax VLN assumptions: egocentric 60° action space, dynamic humans (SMPL), sub-optimal expert supervision (p.1–3). Contributions: HA-VLN task; HA3D simulator + HA-R2R; VLN-CM and VLN-DT agents; evaluation protocol (p.2).

## D. Technical method
- HAPS: GPT-4 generates activity descriptions per 29 regions; 50-participant survey in 5 rounds selects 145; MDM converts to 435 SMPL 120-frame motions (p.3, App.B.1).
- Human placement: count per building = area / 67 m² per capita (US 2021) (p.4). Collision signal when agent–human distance < threshold (default 1 m) (App.B.4).
- HA-R2R: GPT-4 Turbo few-shot prompt merges R2R instruction + activity + relative position; human validation; avg instruction length 29 → 69 words; vocabulary 990 → 4,500 (p.5).
- Oracle: A* on graph excluding human-affected nodes; dynamic adjustment or rerouting (App.C.2).
- VLN-CM: BERT + LSTM + ResNet-152 + cross-attention, trained by imitation of Oracle (Eq.2). VLN-DT: decision transformer on 10⁴ random-walk trajectories (max 30 steps, context 15, RTG 5) with target/distance/human rewards (Eq.3) (p.6).

## E. Human/social representation — SMPL meshes with activities; occupied nodes; 1 m collision radius; activity descriptions in language.

## F. Roles — F11 only (offline data generation). ## H. Integration — I0. ## I. Evidence — E2 (real robot qualitative).

## G. Social capabilities (for the benchmark/agents)
C1 Yes (TCR, CR, SR includes no-collision) · C2/C3 Partial (1 m proximity counted as collision) · C5 Partial (dynamic humans) · C8 Partial (activities exist but agent not evaluated on activity understanding) · C12 Partial (Oracle waits/reroutes) · C23 Partial (instructions mention humans) · C24 Partial · others No.

## J. Experimental evidence — R2R val seen/unseen; baselines Speaker-Follower, Rec(PREVALENT), Rec(OSCAR), Airbert (retrained and zero-shot); Oracle; real Unitree GO1-EDU office demos (App.D.4).

## K. Metrics — TCR, CR, NE, SR (critical-node-adjusted, Eq.4–5); simulator fps.

## L. Quantitative results
- Table 1 (egocentric vs panoramic; NE/TCR/CR/SR): seen Egocentric 7.21/0.69/1.00/0.20, Panoramic 5.58/0.24/0.80/0.34; unseen Egocentric 8.09/0.54/0.58/0.16, Panoramic 7.16/0.25/0.57/0.23.
- Table 2 (optimal vs sub-optimal expert): seen 3.61/0.15/0.52/0.53 vs 3.98/0.18/0.63/0.50; unseen 5.43/0.26/0.69/0.41 vs 5.24/0.24/0.67/0.40.
- Table 3 (static vs dynamic; NE/SR): seen 2.68/0.75 vs 5.24/0.40; unseen 4.01/0.62 vs 3.98/0.50.
- Table 4 (retrained; w/o human → w/ human NE/SR): seen Speaker-Follower 6.62/0.35 → 5.58/0.34; Rec(PREVALENT) 3.93/0.63 → 4.95/0.41; Rec(OSCAR) 4.29/0.59 → 4.67/0.42; Airbert 4.01/0.62 → 3.98/0.50. unseen SF 3.36/0.66 → 7.16/0.23; PREVALENT 2.90/0.72 → 5.86/0.36; OSCAR 3.11/0.71 → 5.86/0.38; Airbert 2.68/0.75 → 5.24/0.40.
  - *Data-quality note:* Table 3 "static" seen (2.68/0.75) equals Airbert's Table 4 *unseen* w/o-human values, and Table 3 "dynamic" seen (5.24/0.40) equals Airbert unseen w/-human; Table 3 unseen (4.01/0.62 → 3.98/0.50) equals Airbert *seen* values. Seen/unseen labels appear swapped between Table 3 and Table 4 (or within Table 4). Flagged; values recorded as printed.
- Table 5 (retrained TCR/CR seen; unseen): SF 0.24/0.87; 0.25/0.63 · PREVALENT 0.21/0.75; 0.24/0.70 · OSCAR 0.18/0.75; 0.23/0.69 · Airbert 0.18/0.68; 0.24/0.74.
- Table 6 Oracle: seen NE 0.62, TCR 0.04, CR 0.175, SR 0.91; unseen 0.67, 0.008, 0.037, 0.89.
- Table 7 zero-shot (w/ human NE/SR): seen SF 7.12/0.24, PREVALENT 6.93/0.26, OSCAR 7.45/0.23, Airbert 6.27/0.30; unseen SF 4.96/0.40, PREVALENT 7.59/0.21, OSCAR 8.37/0.20, Airbert 7.16/0.25.
- Table 8 (NE/TCR/CR/SR seen | unseen): VLN-DT (100% random) 8.51/0.30/0.77/0.21 | 8.22/0.37/0.58/0.11; VLN-CM 0% random 7.31/0.38/0.73/0.19 | 8.22/0.42/0.62/0.12; 3% 7.23/0.75/0.87/0.20 | 8.23/0.82/0.61/0.13; 25% 7.85/0.85/0.61/0.16 | 8.42/0.99/0.52/0.12; 50% 8.67/0.98/0.52/0.11 | 8.74/1.15/0.45/0.09; 100% 10.61/1.01/0.62/0.03 | 10.39/1.14/0.48/0.02.
- Simulator: up to 300 fps at 640×480 on RTX 3050; 40 MB memory (p.5).

## M. Deployment — Jetson TX2 agent (real demo); no latency.

## N. Limitations
1. **Stated (p.10):** captures human presence and basic movement but not breadth of behavioural patterns and social nuances; indoor only.
2. **Future work:** sophisticated social interactions, group dynamics, interpersonal behaviours; higher-fidelity avatars; outdoor; domain adaptation.
3. **Observable:** simulated humans non-reactive; "collision" = within 1 m (conflates proximity with contact); real-world qualitative; table label inconsistency.

## O. Reproducibility — code, data and project page given.

## P. Dataset special analysis — see `dataset:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue Advances in Neural Information Processing Systems 37 (NeurIPS 2024, Datasets and Benchmarks Track); DOI 10.52202/079017-3795; pages 119411-119442; URL https://doi.org/10.52202/079017-3795.
- Sources: Crossref (exact title match, DOI 10.52202/079017-3795); arXiv abs page (2406.19236v3).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - venue: PDF-derived '38th Conference on Neural Information Processing Systems (NeurIPS 2024), Track on Datasets and Benchmarks' -> externally verified 'Advances in Neural Information Processing Systems 37 (NeurIPS 2024, Datasets and Benchmarks Track)'
- Changed field - volume: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - issue: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - pages: PDF-derived '32 (incl. appendix)' -> externally verified '119411-119442'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified '10.52202/079017-3795'
- Changed field - url: PDF-derived 'https://lpercc.github.io/HA3D_simulator/' -> externally verified 'https://doi.org/10.52202/079017-3795'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

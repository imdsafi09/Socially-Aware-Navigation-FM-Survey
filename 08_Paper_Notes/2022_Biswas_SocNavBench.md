---
id: 2022_Biswas_SocNavBench
source_pdfs: [06_Datasets_Benchmarks_Evaluation/2103_00047.pdf]
duplicate_copies: []
related_versions: ['Published: ACM Transactions on Human-Robot Interaction 11(3):1-24, 2022 (per multiple corpus citations); corpus copy is arXiv:2103.00047v2 (28 Jul 2021), ''Manuscript submitted to ACM'' with placeholder DOI']
title: 'SocNavBench: A Grounded Simulation Testing Framework for Evaluating Social Navigation'
authors: &id001 [Abhijat Biswas, Allan Wang, Gustavo Silvera, Aaron Steinfeld, Henny Admoni]
year: 2022
venue: ACM Transactions on Human-Robot Interaction
volume: '11'
issue: '3'
pages: 1-24
doi: 10.1145/3476413
url: https://doi.org/10.1145/3476413
pub_status: journal; benchmark/dataset (corpus copy preprint)
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1145/3476413); arXiv abs page (2103.00047v2). PDF-derived basis (Stage 1): Several corpus papers cite THRI 11(3) 2022; corpus v2 acknowledges anonymous reviewers (p.22). WEB_VERIFICATION_REQUIRED for final DOI.'
category: S6
folder: 06_Datasets_Benchmarks_Evaluation
folder_category_match: 'Yes'
category_rationale: Simulation benchmark for social navigation with replayed real pedestrian trajectories (ETH/UCY), photorealistic RGB-D rendering and a metric suite.
paper_type: benchmark
fm_used: 'No'
fm_class: [None]
fm_models: []
fm_size: NA
method_family: [benchmark/simulator, replayed real pedestrian trajectories]
roles: []
roles_evidence: {}
integration: NA
integration_rationale: No foundation model.
evidence: E2
evidence_rationale: Systematic simulation comparison of Social Forces, ORCA, SA-CADRL and a pedestrian-unaware baseline on 33 curated episodes with a metric suite (Tables 2-4, Figs.6-11); no real-world or human evaluation.
inputs: ['Schematic mode: all pedestrian positions (perfect perception)', 'Full-render mode: RGB-D from configurable 6-DoF camera']
outputs: [velocity commands (unicycle) or position commands (velocity-limited holonomic)]
human_repr: ['replayed pre-recorded trajectories (ETH/UCY), non-reactive', SURREAL human meshes posed by recorded heading/speed (Full-render)]
capabilities: {C1: 'Yes', C2: 'Yes', C3: Partial, C4: 'No', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: Partial, C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: Partial, C18: Partial, C19: Partial, C20: 'No', C21: 'No', C22: 'No', C23: 'No', C24: Partial, C25: 'No'}
exp:
  datasets: [ETH, 'UCY (Univ, Zara)', Hotel]
  simulators: ['SocNavBench (HumANav/Swiftshader rendering, SD3DIS meshes, SURREAL humans)']
  robots: [simulated Pioneer 3-DX]
  environment: ETH, Univ, DoubleHotel, Zara maps (outdoor pedestrian areas)
  indoor_outdoor: outdoor
  sensors: [simulated RGB-D (Full-render), ground-truth positions (Schematic)]
  humans: replayed real pedestrian trajectories; 24-72 per episode (mean 44, sd 13); non-reactive
  n_scenes: 33 curated episodes (<=60 s each); random episode sampling also supported
  n_trajectories: 33 episodes x 4 algorithms; 29 completed by all
  n_participants: NA
  split: NA
  baselines: [Social Forces (PedSim), ORCA, SA-CADRL (4-agent pretrained), pedestrian-unaware meta-planner baseline]
  ablation: 'No'
  real_robot_trials: 'No'
  human_study: 'No'
  statistical_testing: No (mean +/- sd, violin plots)
  scenarios: [crossing dense crowd flows, obstacle-rich outdoor maps]
metrics: [NAV | Overall success rate | fraction | reached goal and no pedestrian collision | p.12-13, NAV | Failure cases (T/PC/EC) | count tuple | Timeout / Pedestrian Collision / Environment Collision | p.13, SAFETY | Total pedestrian collisions | count | over episodes completed by all | p.13, DEPLOY | Average planning wait time | s | simulator wait per step (Table 2 header says per episode) | p.13, NAV | Path length | m | total distance traversed | p.11, NAV | Path length ratio | ratio | defined as straight-line/path length (values >1 reported) | p.11, NAV | Path irregularity | rad | mean abs angle between heading and goal vector | p.11, NAV | Goal traversal ratio | ratio | end/start distance to goal for incomplete episodes | p.11, NAV | Path traversal time | s | simulator time | p.11, NAV | Average speed | m/s | | p.11, 'NAV | Average energy expenditure | J | integral of squared velocity, unit mass | p.11', NAV | Average acceleration | m/s^2 | | p.12, 'NAV | Average jerk | m/s^3 | lower
    = smoother, ''more predictable and legible'' | p.12', 'SOCIAL | Closest-pedestrian distance | m | per trajectory segment, saturated at 10 m | p.12', 'SAFETY | Time-to-collision | s | min linear-extrapolation TTC to any pedestrian, saturated at 10 s | p.13']
deployment: {fm_model: NA, model_size: NA, api_cloud_local: NA, onboard_offboard: NA, gpu: Not reported, cpu: Not reported, latency: Planning wall time reported (Table 2), query_frequency: NA, planner_frequency: NA, controller_frequency: NA, asynchronous: Supported (simulator mode); synchronous default, caching: NA, event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: NA, safety_shield: NA, emergency_behavior: NA, uncertainty: NA, hallucination_mitigation: NA, real_time_claim_supported: NA}
repro: {code: Yes (stated open source), code_url: Not reported (text says 'at this url'), dataset: Yes (ETH/UCY-based episodes), dataset_url: Not reported, checkpoints: SA-CADRL authors' pretrained model, prompts_published: NA, hardware_specified: 'No', hyperparameters: 'Partial (meta-planner horizon 6 s, checkpoint radius 1 m)', protocol_described: 'Yes', project_page: Not reported, concerns: 'Non-reactive pedestrians; synchronous mode removes compute-time penalty; baselines modified (ORCA coefficients, no kinematic constraints).'}
limitations_flags: [sim-to-real, no-human-study, limited-scenarios]
web_verification_required: [THRI 11(3) 2022 DOI and final pagination; code URL.]
cited_missing: [HumANav dataset (Tolani 2021), SURREAL, TrajNet benchmark, Crowd against the machine (CrowdBot benchmark), Social-LSTM, Social-GAN, SoPhie, Bera SocioSense, Mavrogiannis topology-based navigation]
dataset: {kind: benchmark + simulator, real_synthetic: 'hybrid (real trajectories, synthetic rendering)', size: 33 curated episodes; random sampling, environments: 4 maps from ETH/UCY sites, sensors: 'RGB-D (rendered), top view', ego_view: Yes (Full-render), rgb: 'Yes', rgbd: 'Yes', lidar: 'No', human_trajectories: 'Yes (real, replayed)', dynamic_humans: Yes (non-reactive), group_ann: 'No (groups present in data, not annotated)', intention_ann: 'No', activity_ann: 'No', language_ann: 'No', social_rule_ann: 'No', preference_ann: 'No', multi_action_ann: 'No', personal_space_ann: 'No', site_diversity: 4 maps, closed_loop: Yes (robot closed-loop; pedestrians open-loop), vlm_suitability: Medium (photorealistic RGB-D available but no language), real_robot_compat: No (ROS interface planned), standard_metrics: 'Success, collisions, TTC, closest-pedestrian distance, path/motion quality', known_limitations: 'Non-reactive pedestrians invalid for negotiation scenarios (authors, p.20-21)'}
coding: {latency_reported: 'Yes', safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: 'Yes', new_dataset_released: 'Yes', real_robot: 'No', human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2022
  authors: *id001
  venue: ACM Transactions on Human-Robot Interaction (per citations); corpus copy arXiv v2 2021
  volume: 11 (per citations)
  issue: 3 (per citations)
  pages: 24 (PDF); 1-24 (per citations)
  doi: Not reported (placeholder 10.1145/nnnnnnn.nnnnnnn in corpus copy)
  url: Not reported
  pub_status: journal; benchmark/dataset (corpus copy preprint)
  peer_reviewed: 'Yes'
  peer_review_basis: Several corpus papers cite THRI 11(3) 2022; corpus v2 acknowledges anonymous reviewers (p.22). WEB_VERIFICATION_REQUIRED for final DOI.
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: ACM Transactions on Human-Robot Interaction
  verified_doi: 10.1145/3476413
  verified_url: https://doi.org/10.1145/3476413
  verified_pages: 1-24
  arxiv: 2103.00047v2
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1145/3476413)', arXiv abs page (2103.00047v2)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A2]
  C_capabilities: {SAF1: 'Yes', SAF2: 'Yes', SPA1: Partial, SPA2: 'No', SPA3: Partial, SPA4: Partial, HUM1: 'No', HUM2: 'No', NOR1: 'No', NOR2: 'No', NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: Partial, EXP3: 'No'}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: none, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "06_Datasets_Benchmarks_Evaluation"
analytical_category: "S6"
coding:
  latency_reported: "Yes"
  safety_mechanism: "NA"
  uncertainty_treatment: "NA"
  hallucination_treatment: "NA"
  code_released: "Yes"
  new_dataset_released: "Yes"
  real_robot: "No"
  human_subject_study: "No"
---

# SocNavBench (Biswas et al., THRI 2022)

Page convention: PDF index (p.N).

## A. Bibliographic — corpus copy arXiv:2103.00047v2 (28 Jul 2021), ACM THRI template, "Manuscript submitted to ACM", placeholder DOI; cited by corpus papers as ACM THRI 11(3):1–24 (2022). CMU.

## B. Position — S6. Standard grounded-simulation benchmark for classical/DRL social navigation; precursor evaluation style that VLM papers mostly have not adopted.

## C. Research problem — per-method, inconsistent evaluations; synthetic pedestrian models act as ground truth in self-play/against-all simulation (p.1–5). Contributions: photorealistic simulator with algorithm-agnostic API; 33 curated episodes from real data; metric suite; comparison of three methods + baseline (p.3).

## D. Method — ETH/UCY trajectories replayed at 25 fps, non-reactive (collisions registered, motion unchanged) (p.6); Schematic vs Full-render (RGB-D) modes; synchronous (default) vs asynchronous; socket API sense-plan-act; Pioneer 3-DX unicycle or velocity-limited holonomic (p.8–11). Assumption: recorded trajectories are pedestrians' preferred paths, so disruption = poor social navigation (p.6, p.20).

## G. Capabilities — C1 Yes (pedestrian collisions); C2 Yes (TTC); C3 Partial (closest distance, not personal-space model); C12 Partial (yielding discussed qualitatively); C17 Partial (dense crowd episodes, no crowd-specific metric); C18/C19 Partial (jerk interpreted as predictability/legibility proxy, p.12); C24 Partial (authors argue context-dependent metric weighting, p.2, p.20); rest No.

## L. Quantitative results (visually verified, p.15)
Table 2 (meta): Social Forces 32/33, (1/0/0), 1 collision, 18.23 ± 7.41 s; ORCA 24/33, (1/8/0), 15, 48.84 ± 23.06; SA-CADRL 18/33, (0/14/1), 40, 46.78 ± 21.38; Baseline 9/33, (1/23/0), 64, 51.12 ± 16.21.
Table 3 (path; length m / length ratio / goal traversal ratio / irregularity rad / time s): SF 17.25 ± 4.05 / 1.15 ± 0.23 / 0.52 / 1.66 ± 0.95 / 15.93 ± 4.17; ORCA 17.66 ± 5.22 / 1.17 ± 0.26 / 0.21 / 1.56 ± 1.01 / 22.06 ± 7.78; SA-CADRL 15.70 ± 3.72 / 1.04 ± 0.05 / 0.51 / 1.68 ± 1.04 / 15.14 ± 4.21; Baseline 15.88 ± 3.57 / 1.05 ± 0.11 / 0.09 / 1.65 ± 1.02 / 16.08 ± 3.73.
Table 4 (motion; speed m/s / energy J / accel m/s² / jerk m/s³): SF 1.09 ± 0.27 / 398.33 ± 95.45 / 0.39 ± 1.43 / 2.70 ± 28.23; ORCA 0.80 ± 0.27 / 315.03 ± 89.89 / 0.31 ± 1.26 / 6.28 ± 28.85; SA-CADRL 1.04 ± 0.36 / 367.58 ± 87.24 / 0.93 ± 2.91 / 31.68 ± 87.71; Baseline 0.99 ± 0.42 / 370.88 ± 84.55 / 4.81 ± 9.07 / 180.86 ± 303.88.
29/33 episodes completed by all four; metrics computed on these (p.15).
**Data-quality notes:** (i) path length ratio defined as straight-line ÷ path length (p.11) yet values >1 are reported and "high ratio" is read as circuitous (p.17) → definition inverted; (ii) baseline collisions 64 (Table 2) vs "60 pedestrians across 23 episodes" (p.17); (iii) Table 2 column "planning wall time per episode" vs text/Fig.8 "per planning step".

## N. Limitations
1. **Stated (p.20–21):** non-reactive replay misrepresents negotiation scenarios (e.g., single pedestrian in an aisle); real-world experiments still necessary.
2. **Future (p.21–22):** partial reactivity, deviation metrics, ROS interface, URDF robots.
3. **Observable:** no human perception metrics; modified baselines (ORCA, CADRL without kinematic constraints); no statistical tests.
4. **VLM relevance:** RGB-D Full-render mode could host VLM methods, but no language/semantic social labels.

## P. Benchmark analysis — see `dataset:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue ACM Transactions on Human-Robot Interaction; DOI 10.1145/3476413; pages 1-24; URL https://doi.org/10.1145/3476413.
- Sources: Crossref (exact title match, DOI 10.1145/3476413); arXiv abs page (2103.00047v2).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - venue: PDF-derived 'ACM Transactions on Human-Robot Interaction (per citations); corpus copy arXiv v2 2021' -> externally verified 'ACM Transactions on Human-Robot Interaction'
- Changed field - volume: PDF-derived '11 (per citations)' -> externally verified '11'
- Changed field - issue: PDF-derived '3 (per citations)' -> externally verified '3'
- Changed field - pages: PDF-derived '24 (PDF); 1-24 (per citations)' -> externally verified '1-24'
- Changed field - doi: PDF-derived 'Not reported (placeholder 10.1145/nnnnnnn.nnnnnnn in corpus copy)' -> externally verified '10.1145/3476413'
- Changed field - url: PDF-derived 'Not reported' -> externally verified 'https://doi.org/10.1145/3476413'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

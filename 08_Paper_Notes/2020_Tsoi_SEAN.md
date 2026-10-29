---
id: 2020_Tsoi_SEAN
source_pdfs: [06_Datasets_Benchmarks_Evaluation/2009.04300v1.pdf]
duplicate_copies: []
related_versions: ['SEAN 2.0: Formalizing and generating social situations for robot navigation (Tsoi et al., IEEE RA-L 7(4):11047-11054, 2022) - cited by several corpus surveys; NOT in corpus', 'SEAN-EP (Tsoi et al., arXiv 2012.12336, 2020) - cited in corpus; NOT in corpus']
title: 'SEAN: Social Environment for Autonomous Navigation'
authors: &id001 [Nathan Tsoi, Mohamed Hussein, Jeacy Espinoza, Xavier Ruiz, Marynel Vázquez]
year: 2020
venue: Proceedings of the 8th International Conference on Human-Agent Interaction (HAI 2020)
volume: NA
issue: NA
pages: 281-283
doi: 10.1145/3406499.3418760
url: https://doi.org/10.1145/3406499.3418760
pub_status: proceedings; benchmark/dataset (simulator) (corpus copy preprint)
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref DOI 10.1145/3406499.3418760 (verified via DOI lookup; title search returned no match); arXiv abs page (2009.04300v1). PDF-derived basis (Stage 1): Corpus copy is arXiv v1 (ACM template, no venue block); Arena 4.0 (corpus) cites it as HAI 2020 proceedings pp.281-283 (short paper). WEB_VERIFICATION_REQUIRED.'
category: S6
folder: 06_Datasets_Benchmarks_Evaluation
folder_category_match: 'Yes'
category_rationale: Open-source Unity+ROS social navigation simulator with pedestrian agents and an evaluation toolkit (Trial Runner).
paper_type: simulator
fm_used: 'No'
fm_class: [None]
fm_models: []
fm_size: NA
method_family: [simulation platform, crowd flow prediction + Unity path planning for pedestrians]
roles: []
roles_evidence: {}
integration: NA
integration_rationale: No foundation model.
evidence: E2
evidence_rationale: Platform demonstrated with ROS Navigation Stack and teleoperation in simulation, mean +/- sd over 10 episodes per condition (Table 1, p.2); no real-world or human-subject evaluation.
inputs: [simulated VLP-16 LiDAR, simulated RGB camera]
outputs: [ROS navigation goal / velocity commands (via ROS)]
human_repr: [animated pedestrian agents with start/goal positions (crowd-flow prediction + Unity NavMesh)]
capabilities: {C1: 'Yes', C2: Partial, C3: Partial, C4: 'No', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: 'No', C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: 'No', C24: 'No', C25: 'No'}
exp:
  datasets: []
  simulators: [SEAN (Unity 3D + ROS Melodic via ROS#)]
  robots: [Clearpath Jackal (simulated), Clearpath Warthog (simulated)]
  environment: Lab scene (indoor) and outdoor city scene
  indoor_outdoor: both
  sensors: [simulated Velodyne VLP-16, simulated RGB camera]
  humans: simulated dynamic pedestrians
  n_scenes: '2'
  n_trajectories: 10 episodes per condition
  n_participants: NA
  split: NA
  baselines: [ROS Navigation Stack (minimally tuned), teleoperation (gamepad)]
  ablation: 'No'
  real_robot_trials: 'No'
  human_study: 'No'
  statistical_testing: No (mean +/- sd only)
  scenarios: [point-to-point navigation with pedestrians]
metrics: [NAV | Complete (goal reached) | % | robot reached goal before timeout | p.2, NAV | Elapsed | s | time to final position | p.2, NAV | Final Dist | m | final distance to goal | p.2, SAFETY | Collisions | count | collisions with static objects (pedestrian collisions recorded separately per text) | p.2, SOCIAL | Ped. Dist | m | closest distance between robot and pedestrians | p.2, SAFETY | Pedestrian collisions | count | collisions with pedestrians (stated as tracked; not separately shown in Table 1) | p.2]
deployment: {fm_model: NA, model_size: NA, api_cloud_local: NA, onboard_offboard: NA, gpu: Not reported, cpu: Not reported, latency: NA, query_frequency: NA, planner_frequency: NA, controller_frequency: NA, asynchronous: NA, caching: NA, event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: NA, safety_shield: NA, emergency_behavior: NA, uncertainty: NA, hallucination_mitigation: NA, real_time_claim_supported: NA}
repro: {code: 'Yes (open source, stated)', code_url: 'https://sean.interactive-machines.com/', dataset: NA, dataset_url: NA, checkpoints: NA, prompts_published: NA, hardware_specified: 'No', hyperparameters: No (ROS stack 'minimally tuned'), protocol_described: Partial (Trial Runner records initial conditions for replay), project_page: 'https://sean.interactive-machines.com/', concerns: Very short paper; pedestrian behaviour model not described in detail; does not react to robot (not stated).}
limitations_flags: [limited-scenarios, sim-to-real, no-human-study]
web_verification_required: [HAI 2020 publication details of SEAN 1.0.]
cited_missing: [SEAN 2.0 (RA-L 2022), SEAN-EP (2020), MengeROS, Menge, Tjomsland 2020 social appropriateness dataset (MANNERS-DB), Mavrogiannis HRI 2019 effects of navigation strategies]
dataset: {kind: simulator, real_synthetic: synthetic, size: '2 scenes (lab, city); 2 robots', environments: indoor lab; outdoor city, sensors: 'simulated LiDAR, RGB', ego_view: Yes (robot camera view), rgb: 'Yes', rgbd: 'No', lidar: 'Yes', human_trajectories: Yes (simulated), dynamic_humans: 'Yes', group_ann: 'No', intention_ann: 'No', activity_ann: 'No', language_ann: 'No', social_rule_ann: 'No', preference_ann: 'No', multi_action_ann: 'No', personal_space_ann: 'No', site_diversity: 2 scenes, closed_loop: 'Yes', vlm_suitability: 'Medium (photorealistic Unity rendering supports vision-based methods, p.1)', real_robot_compat: Partial (ROS interface; sim-to-real untested), standard_metrics: 'Success, time, final distance, collisions, closest pedestrian distance', known_limitations: 'Few scenes, robots and metrics (authors, p.2)'}
coding: {latency_reported: 'No', safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: 'Yes', new_dataset_released: NA, real_robot: 'No', human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2020
  authors: *id001
  venue: Proceedings of the 8th International Conference on Human-Agent Interaction (HAI 2020), pp. 281-283 (per Arena 4.0 citation); corpus copy arXiv:2009.04300v1
  volume: NA
  issue: NA
  pages: 3 (PDF); 281-283 (per citation)
  doi: Not reported
  url: https://sean.interactive-machines.com/
  pub_status: proceedings; benchmark/dataset (simulator) (corpus copy preprint)
  peer_reviewed: 'Yes'
  peer_review_basis: Corpus copy is arXiv v1 (ACM template, no venue block); Arena 4.0 (corpus) cites it as HAI 2020 proceedings pp.281-283 (short paper). WEB_VERIFICATION_REQUIRED.
project_url: https://sean.interactive-machines.com/
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: Proceedings of the 8th International Conference on Human-Agent Interaction (HAI 2020)
  verified_doi: 10.1145/3406499.3418760
  verified_url: https://doi.org/10.1145/3406499.3418760
  verified_pages: 281-283
  arxiv: 2009.04300v1
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: [Crossref DOI 10.1145/3406499.3418760 (verified via DOI lookup; title search returned no match), arXiv abs page (2009.04300v1)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1]
  C_capabilities: {SAF1: 'Yes', SAF2: Partial, SPA1: Partial, SPA2: 'No', SPA3: 'No', SPA4: 'No', HUM1: 'No', HUM2: 'No', NOR1: 'No', NOR2: 'No', NOR3: 'No', NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: none, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "06_Datasets_Benchmarks_Evaluation"
analytical_category: "S6"
coding:
  latency_reported: "No"
  safety_mechanism: "NA"
  uncertainty_treatment: "NA"
  hallucination_treatment: "NA"
  code_released: "Yes"
  new_dataset_released: "NA"
  real_robot: "No"
  human_subject_study: "No"
---

# SEAN (Tsoi et al., HAI 2020)

Page convention: PDF index (p.N).

## A. Bibliographic — arXiv:2009.04300v1 (9 Sep 2020), Yale / Rutgers. ACM template without venue block; cited by Arena 4.0 as HAI 2020 (pp.281–283) → treated as peer-reviewed short paper (flagged for web verification). Successor SEAN 2.0 (RA-L 2022) is cited by corpus surveys but not in corpus.

## B. Position — S6 simulator. Early photorealistic social-navigation simulator; relevant to VLM methods because it renders camera views (p.1), but no language/FM support.

## C. Research problem — lack of high-fidelity simulation for social robot navigation and of reproducible comparisons (p.1). Contributions: Unity+ROS platform, two scenes, two robots, Trial Runner evaluation toolkit (p.1–2).

## D. Method — Unity (PhysX) + ROS via ROS#; Windows 10 / Ubuntu 18.04 + ROS Melodic; pedestrians use crowd-flow prediction (Sohn 2020) + Unity path planning; adjustable density; Trial Runner configures episodes, records initial conditions for replay, logs metrics (p.1–2).

## E. Human representation — animated pedestrian agents moving between start/goal positions; whether they react to the robot is not stated.

## G. Capabilities — C1 Yes (pedestrian collisions tracked); C2/C3 Partial (closest pedestrian distance as proxy); all others No. Platform-level coding (what the toolkit measures).

## I. Evidence — E2: simulation, 10 episodes per condition.

## L. Quantitative results (Table 1, p.2; μ ± σ over 10 episodes)
| Scene | Robot | Elapsed (s) | Complete | Final Dist (m) | Ped. Dist (m) | Collisions |
|---|---|---|---|---|---|---|
| Lab | Jackal (ROS) | 24.51 ± 19.36 | 60% | 2.26 ± 2.92 | 1.54 ± 1.76 | 7.1 ± 9.4 |
| Lab | Jackal (teleop) | 21.6 ± 28.08 | 88% | 1.14 ± 1.99 | 0.92 ± 1.16 | 4.63 ± 5.83 |
| City | Jackal (ROS) | 37.09 ± 13.74 | 29% | 9.54 ± 8.94 | 0.64 ± 0.42 | 20 ± 30.83 |
| City | Jackal (teleop) | 38.54 ± 29.5 | 80% | 4.59 ± 11.87 | 1.06 ± 0.67 | 3.1 ± 7.58 |
| City | Warthog (teleop) | 31.7 ± 20.94 | 100% | 0.48 ± 0.01 | 2.27 ± 1.08 | 0 ± 0 |
- Observation: "Complete" percentages such as 88% and 29% are not multiples of 10% despite "10 episodes" in the caption (data-quality note).

## N. Limitations
1. **Stated (p.2):** limited scenes, robots and metrics; simulation not a replacement for real-world testing; low ROS performance due to mapping without humans and conservative behaviour.
2. **Future (p.2):** sim-to-real transfer tests; human evaluation of robot behaviour from SEAN videos.
3. **Observable:** short paper; no social metrics beyond distance/collisions; pedestrian model details sparse; no statistics.
4. **VLM relevance:** none directly.

## P. Dataset/simulator analysis — see `dataset:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue Proceedings of the 8th International Conference on Human-Agent Interaction (HAI 2020); DOI 10.1145/3406499.3418760; pages 281-283; URL https://doi.org/10.1145/3406499.3418760.
- Sources: Crossref DOI 10.1145/3406499.3418760 (verified via DOI lookup; title search returned no match); arXiv abs page (2009.04300v1).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - venue: PDF-derived 'Proceedings of the 8th International Conference on Human-Agent Interaction (HAI 2020), pp. 281-283 (per Arena 4.0 citation); corpus copy arXiv:2009.04300v1' -> externally verified 'Proceedings of the 8th International Conference on Human-Agent Interaction (HAI 2020)'
- Changed field - pages: PDF-derived '3 (PDF); 281-283 (per citation)' -> externally verified '281-283'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified '10.1145/3406499.3418760'
- Changed field - url: PDF-derived 'https://sean.interactive-machines.com/' -> externally verified 'https://doi.org/10.1145/3406499.3418760'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

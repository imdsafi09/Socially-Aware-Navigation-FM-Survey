---
id: 2023_Shah_GNM
source_pdfs: [03_Adjacent_Foundation_Model_Navigation/2210.03370v2.pdf]
duplicate_copies: []
related_versions: ['Published: IEEE ICRA 2023 (per corpus citation); corpus copy arXiv:2210.03370v2 (22 May 2023)']
title: 'GNM: A General Navigation Model to Drive Any Robot'
authors: &id001 [Dhruv Shah, Ajay Sridhar, Arjun Bhorkar, Noriaki Hirose, Sergey Levine]
year: 2023
venue: 2023 IEEE International Conference on Robotics and Automation (ICRA)
volume: NA
issue: NA
pages: 7226-7233
doi: 10.1109/ICRA48891.2023.10161227
url: https://doi.org/10.1109/ICRA48891.2023.10161227
pub_status: conference (corpus copy preprint)
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1109/ICRA48891.2023.10161227); arXiv abs page (2210.03370v2). PDF-derived basis (Stage 1): Corpus copy arXiv v2 without venue; cited as ICRA 2023 in corpus. WEB_VERIFICATION_REQUIRED.'
category: S3
folder: 03_Adjacent_Foundation_Model_Navigation
folder_category_match: 'Yes'
category_rationale: Cross-embodiment visual navigation foundation model (image-goal) trained on heterogeneous multi-robot data; no social behaviour modelled or evaluated.
paper_type: model
fm_used: 'Yes'
fm_class: [NavFM]
fm_models: [GNM (MobileNetV2 encoders + FC heads)]
fm_size: Not reported
method_family: [imitation learning (supervised waypoint regression), goal-conditioned policy, topological graph navigation]
roles: [F9, F10]
roles_evidence: {F9: 'Predicts sequence of tau=5 normalized future waypoints {p, psi} tracked by robot-specific controller (p.3-4).', F10: Serves as the end-to-end visuomotor policy (with low-level tracker) (p.4).}
integration: I6
integration_rationale: Learned navigation policy (waypoint action space) deployed with topological graph and low-level controller.
evidence: E3
evidence_rationale: Zero-shot real-robot deployment on LoCoBot, Jackal, Vizbot, DJI Tello across ~20 indoor/outdoor environments with success-rate tables (Tables II-V); no human study.
inputs: [current RGB (85x64), goal image, k=5 past frames (embodiment context)]
outputs: [normalized waypoints and yaw (5 steps), temporal distance to goal]
human_repr: [none]
capabilities: {C1: NA, C2: NA, C3: NA, C4: NA, C5: NA, C6: NA, C7: NA, C8: NA, C9: NA, C10: NA, C11: NA, C12: NA, C13: NA, C14: NA, C15: NA, C16: NA, C17: NA, C18: NA, C19: NA, C20: NA, C21: NA, C22: NA, C23: NA, C24: NA, C25: NA}
exp:
  datasets: [GoStanford, RECON, CoryHall, Berkeley, SCAND-S (Spot), SCAND-J (Jackal), Seattle, TartanDrive, NeBula]
  simulators: []
  robots: [LoCoBot, Clearpath Jackal, Vizbot (Roomba-based), DJI Tello]
  environment: indoor offices/hallways; outdoor sidewalks/off-road
  indoor_outdoor: both
  sensors: [monocular/fisheye RGB]
  humans: none in evaluation
  n_scenes: ~20 indoor/outdoor environments (Jackal/LoCoBot); 10 for design ablations
  n_trajectories: Not reported
  n_participants: NA
  split: Small/Mid/Large = first 2/4/6 datasets
  baselines: ['single-dataset policies (GS, RECON, CoryHall)', GS + ImageNet pretraining]
  ablation: Yes (action space, context, architecture, data scale)
  real_robot_trials: 'Yes'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: []
metrics: [NAV | Success rate | 0-1 | 'mean progress made towards the goal' | p.4]
deployment: {fm_model: GNM, model_size: Not reported, api_cloud_local: Local, onboard_offboard: Not reported, gpu: Multi-GPU training (unspecified), cpu: Not reported, latency: Not reported, query_frequency: every time step, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Not reported, caching: NA, event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: Topological graph + Dijkstra subgoals, safety_shield: 'No', emergency_behavior: Not reported, uncertainty: NA, hallucination_mitigation: NA, real_time_claim_supported: NA}
repro: {code: 'Yes', code_url: sites.google.com/view/drive-any-robot, dataset: Yes (released), dataset_url: sites.google.com/view/drive-any-robot, checkpoints: Yes (released), prompts_published: NA, hardware_specified: Partial, hyperparameters: 'Partial (Adam 5e-4, batch 400-1200, k=5, tau=5)', protocol_described: Partial, project_page: sites.google.com/view/drive-any-robot, concerns: Number of trials per environment not reported; success defined as mean progress.}
limitations_flags: [limited-scenarios]
web_verification_required: [ICRA 2023 publication details.]
cited_missing: [ViNG (Shah 2021), RECON (Shah 2021), ExAug (ICRA 2023), Deep Visual MPC-Policy Learning (GoStanford), TartanDrive, Hierarchically integrated models (Kang 2021)]
adjacent: {mechanism: Single goal-conditioned visuomotor navigation policy trained on 60-70 h of heterogeneous multi-robot data with normalized waypoint action space and temporal embodiment context., relevance: Navigation foundation model lineage (GNM -> ViNT -> NoMaD) used as base policies/baselines in VLM social navigation; training data includes SCAND sidewalks with pedestrians but social behaviour is not evaluated., why_not_direct: 'No language, no humans in evaluation, no social metrics.', inherited_by: 'Cited by corpus SocialNav (CVPR 2026, Chu); ViNT/NoMaD (adjacent) build on it.'}
coding: {latency_reported: 'No', safety_mechanism: 'No', uncertainty_treatment: NA, hallucination_treatment: NA, code_released: 'Yes', new_dataset_released: 'Yes', real_robot: Systematic, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2023
  authors: *id001
  venue: IEEE ICRA 2023 (per citation); corpus copy arXiv v2
  volume: NA
  issue: NA
  pages: 8 (PDF)
  doi: Not reported
  url: sites.google.com/view/drive-any-robot
  pub_status: conference (corpus copy preprint)
  peer_reviewed: 'Yes'
  peer_review_basis: Corpus copy arXiv v2 without venue; cited as ICRA 2023 in corpus. WEB_VERIFICATION_REQUIRED.
project_url: sites.google.com/view/drive-any-robot
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: 2023 IEEE International Conference on Robotics and Automation (ICRA)
  verified_doi: 10.1109/ICRA48891.2023.10161227
  verified_url: https://doi.org/10.1109/ICRA48891.2023.10161227
  verified_pages: 7226-7233
  arxiv: 2210.03370v2
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1109/ICRA48891.2023.10161227)', arXiv abs page (2210.03370v2)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A0]
  C_capabilities: {SAF1: NA, SAF2: NA, SPA1: NA, SPA2: NA, SPA3: NA, SPA4: NA, HUM1: NA, HUM2: NA, NOR1: NA, NOR2: NA, NOR3: NA, NOR4: NA, EXP1: NA, EXP2: NA, EXP3: NA}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'No', EV3_physical_robot: systematic, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "03_Adjacent_Foundation_Model_Navigation"
analytical_category: "S3"
coding:
  latency_reported: "No"
  safety_mechanism: "No"
  uncertainty_treatment: "NA"
  hallucination_treatment: "NA"
  code_released: "Yes"
  new_dataset_released: "Yes"
  real_robot: "Systematic"
  human_subject_study: "No"
---

# GNM (Shah et al., ICRA 2023)

Page convention: PDF index (p.N).

## A. Bibliographic — corpus copy arXiv:2210.03370v2 (22 May 2023); UC Berkeley, Toyota. Cited as ICRA 2023.

## B. Position — S3 adjacent: navigation foundation model (NavFM), not language-based.

## C. Research problem — robot-specific data fragmentation limits learned navigation (p.1). Contributions: multi-robot dataset aggregation and a general omnipolicy that transfers to new robots (p.1).

## D. Method — image-goal navigation; normalized relative waypoints + yaw scaled by robot top speed; temporal distance head; embodiment context from k = 5 past frames; MobileNetV2 dual encoders; trained with ℓ2 regression on positives/negatives; deployed with topological graph + Dijkstra (p.2–4).

## L. Quantitative results
- Table II (mean success, GS / RECON / GNM-Mid): LoCoBot 0.26 / 0.62 / 0.96; Tello 0.21 / 0.79 / 0.99; Vizbot 0.51 / 0.26 / 0.93; Jackal 0.31 / 0.68 / 0.94.
- Table III (LoCoBot; Indoor Easy / Moderate / Outdoor): CoryHall 0.22/0.13/0.29; GS 0.25/0.16/0.44; GS+ImageNet 0.35/0.35/0.57; GNM-Small 0.82/0.59/1.0; GNM-Mid 1.0/0.97/0.83; GNM-Large 1.0/1.0/0.83.
- Table IV (Jackal; Outdoor Easy / Hard / Indoor): GS 0.25/0.05/0.40; RECON 0.67/0.48/0.36; +ImageNet 0.72/0.52/0.31; GNM-Small 0.75/0.52/0.42; GNM-Mid 1.0/1.0/0.82; GNM-Large 1.0/1.0/0.88.
- Table V (LoCoBot): action space Easy/Moderate — velocities 0.73/0.54, waypoints 0.42/0.26, normalized waypoints 1.0/0.95; architecture — stacked 0.52/0.72, Siamese 0.73/0.26, conditioned 1.0/0.95; context Easy/Moderate/Hard — none 1.0/0.79/0.36, static 1.0/0.86/0.5, temporal 1.0/0.92/0.7.
- Fig.5 robustness (single-domain vs GNM): steering 0.30 vs 0.89; viewpoint 0.17 vs 0.81; physical 0.81 vs 1.0.
- **Data-quality notes:** dataset described as "60 hours" (abstract, p.2) vs Table I total "70h"; text says "8 datasets" but Table I lists 9.

## N. Limitations
1. **Stated (p.6):** assumes ground robots with forward RGB; diverse sensing/actuation/traversability not handled; dataset could be larger.
2. **Observable:** trial counts unreported; success = mean progress (not binary); no dynamic agents evaluated.
3. **Social relevance:** base policy for later socially aware adaptation (e.g., CVPR 2026 SocialNav); itself socially agnostic.

## P. Adjacent analysis — see `adjacent:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue 2023 IEEE International Conference on Robotics and Automation (ICRA); DOI 10.1109/ICRA48891.2023.10161227; pages 7226-7233; URL https://doi.org/10.1109/ICRA48891.2023.10161227.
- Sources: Crossref (exact title match, DOI 10.1109/ICRA48891.2023.10161227); arXiv abs page (2210.03370v2).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - venue: PDF-derived 'IEEE ICRA 2023 (per citation); corpus copy arXiv v2' -> externally verified '2023 IEEE International Conference on Robotics and Automation (ICRA)'
- Changed field - pages: PDF-derived '8 (PDF)' -> externally verified '7226-7233'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified '10.1109/ICRA48891.2023.10161227'
- Changed field - url: PDF-derived 'sites.google.com/view/drive-any-robot' -> externally verified 'https://doi.org/10.1109/ICRA48891.2023.10161227'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

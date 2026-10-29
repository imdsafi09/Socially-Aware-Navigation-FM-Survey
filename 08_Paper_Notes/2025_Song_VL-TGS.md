---
id: 2025_Song_VL-TGS
source_pdfs: [04_Direct_VLM_SocialNav/B_Peer_Reviewed_Boundary/tgs.pdf]
duplicate_copies: []
related_versions: ['arXiv:2408.02454 ''TGS'' (cited by AutoSpatial [20]); not in corpus']
title: 'VL-TGS: Trajectory Generation and Selection Using Vision Language Models in Mapless Outdoor Environments'
authors: &id001 [Daeun Song, Jing Liang, Xuesu Xiao, Dinesh Manocha]
year: 2025
venue: IEEE Robotics and Automation Letters
volume: '10'
issue: '6'
pages: 5791-5798
doi: 10.1109/LRA.2025.3559822
url: https://doi.org/10.1109/LRA.2025.3559822
pub_status: journal
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1109/LRA.2025.3559822); arXiv abs page (2408.02454v6). PDF-derived basis (Stage 1): Received 4 Dec 2024; accepted 30 Mar 2025; recommended by AE upon reviewers'' comments (p.1).'
category: S3
folder: 04_Direct_VLM_SocialNav/B_Peer_Reviewed_Boundary
folder_category_match: Partial
category_rationale: VLM selects among CVAE-generated candidate trajectories to satisfy semantic traversability conventions (pavement, curbs, crosswalks) in 'human-centered' outdoor environments; no human interaction is evaluated, so classified adjacent (boundary).
paper_type: method
fm_used: 'Yes'
fm_class: [VLM]
fm_models: [GPT-4V]
fm_size: Not reported
method_family: [CVAE trajectory generation (MTG), visual prompting, zero-shot, DWA]
roles: [F1, F4, F5]
roles_evidence: {F5: 'VLM selects best numbered candidate trajectory from visually annotated image (Eq.2-3, p.3-4).', F4: 'Prompt includes rules: walk on pavements, avoid rough terrain, follow the rules, cannot go over curbs (p.4).', F1: 'VLM semantic understanding of crosswalks, curbs, flower beds (p.1-3).'}
integration: I3
integration_rationale: VLM ranks/selects among geometric candidates; DWA executes selected 10 m trajectory (p.4, p.7).
evidence: E3
evidence_rationale: Offline frame-based evaluation (20 frames x 5 repetitions per scenario) plus a single real-robot run per method on a ~100 m route with failure counts; no humans as evaluated agents (p.5-7).
inputs: [RGB, LiDAR, robot velocities, GPS goal, candidate paths, natural language prompt]
outputs: [path ranking/selection, trajectory (10 m), velocity/action (via DWA)]
human_repr: [none explicit (humans only as potential obstacles; 'MTG often overlooks small dynamic obstacles such as humans' qualitative)]
capabilities: {C1: NA, C2: NA, C3: NA, C4: NA, C5: NA, C6: NA, C7: NA, C8: NA, C9: NA, C10: NA, C11: NA, C12: NA, C13: NA, C14: NA, C15: NA, C16: NA, C17: NA, C18: NA, C19: NA, C20: NA, C21: NA, C22: NA, C23: NA, C24: NA, C25: NA}
exp:
  datasets: [GND global navigation dataset (CVAE training)]
  simulators: []
  robots: [Clearpath Husky]
  environment: outdoor campus (flower bed, curb, crosswalk, corner)
  indoor_outdoor: outdoor
  sensors: [Velodyne VLP16 LiDAR, Realsense D435i, GPS]
  humans: none in benchmark scenarios (stationary environments)
  n_scenes: 4 scenarios
  n_trajectories: 20 frames x 5 repetitions per scenario/method; 1 real run per method
  n_participants: NA
  split: NA
  baselines: [MTG, ViNT, NoMaD, PIVOT, CoNVOI]
  ablation: Yes (random generator vs CVAE; heuristic selector vs VLM)
  real_robot_trials: 'Yes'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [crosswalk, sidewalk/curb, flower bed, corner]
metrics: [OTHER | Traversability | % | ratio of trajectory waypoints in traversable area of binary map | p.5, OTHER | Frechet Distance w.r.t. human tele-operation | m | curve similarity | p.5, NAV | Number of Failures | count | human interventions to recover robot | p.7, NAV | Travel Distance | m | real-world route | p.7, NAV | Travel Time | s | real-world route | p.7]
deployment: {fm_model: GPT-4V, model_size: Not reported, api_cloud_local: Cloud (online large VLM), onboard_offboard: Laptop i7 + RTX 2080 on robot; VLM online, gpu: RTX 2080, cpu: Intel i7, latency: 'VLM outputs 2-4 s (p.4, p.7)', query_frequency: Re-prompted after each response (every 2-4 s), planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Yes (DWA follows last selected 10 m trajectory while waiting), caching: Long 10 m trajectories reduce update needs, event_triggered: 'No', distillation: 'No', quantization: 'No', fallback_planner: DWA continues on last trajectory, safety_shield: DWA dynamic obstacle avoidance, emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: VLM limited to choosing among traversable candidates, real_time_claim_supported: No (authors state VLM unsuitable for high-frequency real-time decisions)}
repro: {code: Not reported, code_url: NA, dataset: GND (cited), dataset_url: NA, checkpoints: NA, prompts_published: Yes (full prompt p.4), hardware_specified: 'Yes', hyperparameters: Partial, protocol_described: Partial, project_page: Not reported (supplementary video), concerns: Single real run per method; offline 'frames' evaluation.}
limitations_flags: [latency, cloud-dependence, limited-scenarios]
web_verification_required: []
cited_missing: [MTG mapless trajectory generator (ICRA 2024), DTG diffusion trajectory generation (IROS 2024), GND dataset (ICRA 2025), PIVOT, Set-of-Mark prompting, CoWs on pasture, Shtedritski CLIP red circle]
adjacent: {mechanism: 'Propose-and-select: generative (CVAE) geometric candidates + VLM visual-prompt selection of semantically appropriate trajectory', relevance: 'Demonstrates VLM as path critic for conventions of human-centred spaces (crosswalks, pavements); direct template for later social path selection', why_not_direct: 'No humans in evaluated scenarios; objective is semantic traversability, not interaction with people', inherited_by: Fang et al. 2026 'From Obstacles to Etiquette' explicitly cites VL-TGS as closest propose-and-select work; GSON/OLiVia-style candidate selection}
coding: {latency_reported: 'Yes', safety_mechanism: 'Yes', uncertainty_treatment: 'No', hallucination_treatment: 'Yes', code_released: 'No', new_dataset_released: NA, real_robot: Systematic, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2025
  authors: *id001
  venue: IEEE Robotics and Automation Letters
  volume: '10'
  issue: '6'
  pages: 5791-5798
  doi: 10.1109/LRA.2025.3559822
  url: Not reported
  pub_status: journal
  peer_reviewed: 'Yes'
  peer_review_basis: Received 4 Dec 2024; accepted 30 Mar 2025; recommended by AE upon reviewers' comments (p.1).
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: IEEE Robotics and Automation Letters
  verified_doi: 10.1109/LRA.2025.3559822
  verified_url: https://doi.org/10.1109/LRA.2025.3559822
  verified_pages: 5791-5798
  arxiv: 2408.02454v6
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1109/LRA.2025.3559822)', arXiv abs page (2408.02454v6)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A0]
  C_capabilities: {SAF1: NA, SAF2: NA, SPA1: NA, SPA2: NA, SPA3: NA, SPA4: NA, HUM1: NA, HUM2: NA, NOR1: NA, NOR2: NA, NOR3: NA, NOR4: NA, EXP1: NA, EXP2: NA, EXP3: NA}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'No', EV3_physical_robot: systematic, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "04_Direct_VLM_SocialNav/B_Peer_Reviewed_Boundary"
analytical_category: "S3"
coding:
  latency_reported: "Yes"
  safety_mechanism: "Yes"
  uncertainty_treatment: "No"
  hallucination_treatment: "Yes"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "Systematic"
  human_subject_study: "No"
---

# VL-TGS (Song, Liang, Xiao, Manocha — RA-L 2025)

Page convention: PDF index (p.N); printed pp.5791–5798.

## A. Bibliographic — IEEE RA-L 10(6):5791–5798, Jun 2025, DOI 10.1109/LRA.2025.3559822; peer-reviewed. Earlier arXiv "TGS" (2408.02454) cited elsewhere.

## B. Position — **S3 adjacent (boundary; folder 04B)**
Relevant: VLM-as-path-critic with visual prompting in human-centred outdoor spaces (crosswalk/pavement conventions). Not direct: no people in benchmark; behaviours concern semantic traversability. The authors say focus is navigation decisions aligned "with social and environmental cues" (p.7) but no social interaction is tested.

## C. Research problem — mapless global outdoor navigation satisfying traversability constraints and human-like paths (abstract). Contributions: CVAE generation + VLM selection; visual prompting for spatial reasoning; evaluation in 4 outdoor scenarios (+20.81% traversability, 28.51% Fréchet) (p.2).

## D. Technical method — attention-based CVAE (MTG) on consecutive LiDAR + velocities generates diverse ~10 m trajectories via orthogonal embedding projections (Eq.4); 2 consecutive steps pooled; Hausdorff filtering (Eq.5); projected to image, numbered by distance-to-goal; GPT-4V selects one with prompt (p.4); DWA executes; VLM re-prompted every 2–4 s.

## J–L. Experiments and results (Table I, p.6, visually verified; mean ± std over 20 frames × 5 reps)
Traversability (%) — Flower bed / Curb / Crosswalk / Corner: MTG 58.19±16.65 / 67.12±15.65 / 61.82±10.95 / 44.71±18.35; ViNT 63.62±18.49 / 78.37±17.94 / 84.78±3.16 / 44.95±17.16; NoMaD 75.64±15.04 / 83.13±10.04 / 79.24±13.36 / 77.38±18.59; PIVOT 64.75±19.63 / 79.58±12.86 / 76.78±10.41 / 68.66±15.76; CoNVOI 81.10±9.98 / 75.68±12.86 / 86.24±12.63 / 88.46±11.45; VL-TGS 87.22±10.27 / 89.93±7.11 / 87.44±9.78 / 78.00±7.79.
Fréchet (m): MTG 6.61±1.91 / 8.40±6.30 / 10.42±2.53 / 9.93±3.04; ViNT 10.43±2.92 / 10.78±3.08 / 8.94±2.29 / 12.71±2.43; NoMaD 7.65±3.32 / 8.71±3.53 / 11.87±2.99 / 9.62±2.60; PIVOT 8.41±1.85 / 7.86±1.55 / 10.53±3.00 / 9.48±3.15; CoNVOI 11.64±0.47 / 12.24±1.12 / 11.33±1.26 / 12.36±2.15; VL-TGS 5.27±1.65 / 7.93±1.28 / 6.38±2.95 / 8.49±2.29.
- Data-quality note: Curb Fréchet bolded for VL-TGS (7.93) although PIVOT is lower (7.86).
Table II real world (single run each; failures / distance m / time s): MTG 8/111.65/201; NoMaD 6/100.79/168; CoNVOI 13/115.77/257; VL-TGS 4/97.53/151.

## M. Deployment — GPT-4V online, 2–4 s; long trajectories + DWA bridge latency.

## N. Limitations — 1. Stated: low frequency of online large VLMs unsuitable for high-frequency decisions; benchmark scenarios stationary; performance depends on VLM robustness; generator could be replaced (p.7–8). 2. Future: faster VLMs; better generators. 3. Observable: one real run per method; no humans; frame-level offline metric.

## P. Adjacent analysis — see `adjacent:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue IEEE Robotics and Automation Letters; DOI 10.1109/LRA.2025.3559822; pages 5791-5798; URL https://doi.org/10.1109/LRA.2025.3559822.
- Sources: Crossref (exact title match, DOI 10.1109/LRA.2025.3559822); arXiv abs page (2408.02454v6).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - url: PDF-derived 'Not reported' -> externally verified 'https://doi.org/10.1109/LRA.2025.3559822'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

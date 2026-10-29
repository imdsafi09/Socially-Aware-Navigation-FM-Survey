---
id: 2024_Yokoyama_VLFM
source_pdfs: [03_Adjacent_Foundation_Model_Navigation/VLFM_Vision-Language_Frontier_Maps_for_Zero-Shot_Semantic_Navigation.pdf]
duplicate_copies: []
related_versions: []
title: 'VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation'
authors: &id001 [Naoki Yokoyama, Sehoon Ha, Dhruv Batra, Jiuguang Wang, Bernadette Bucher]
year: 2024
venue: 2024 IEEE International Conference on Robotics and Automation (ICRA)
volume: NA
issue: NA
pages: 42-48
doi: 10.1109/ICRA57147.2024.10610712
url: https://doi.org/10.1109/ICRA57147.2024.10610712
pub_status: conference
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1109/ICRA57147.2024.10610712); arXiv abs page (2312.03275v1). PDF-derived basis (Stage 1): ICRA 2024 header with DOI (IEEE Xplore copy).'
category: S3
folder: 03_Adjacent_Foundation_Model_Navigation
folder_category_match: 'Yes'
category_rationale: Zero-shot ObjectNav using BLIP-2 image-text similarity to build a value map for frontier selection; no humans or social behaviour.
paper_type: method
fm_used: 'Yes'
fm_class: [VLM, CLIP-style]
fm_models: [BLIP-2 (image-text cosine similarity), Grounding-DINO, YOLOv7 (not FM), Mobile-SAM, ZoeDepth (real robot)]
fm_size: Not reported
method_family: [frontier-based exploration, language-grounded value map, DRL PointNav policy (VER)]
roles: [F1, F5]
roles_evidence: {F1: BLIP-2 cosine similarity between RGB and prompt 'Seems like there is a <target object> ahead.' projected into a value map (p.3-4)., F5: Value map scores rank candidate frontier waypoints; highest chosen (p.2-3).}
integration: I3
integration_rationale: VLM produces semantic scores used to rank frontier waypoints, which are then executed by a PointNav policy (sim) or Spot API (real).
evidence: E2
evidence_rationale: Systematic closed-loop evaluation in Habitat on Gibson (1000 eps), HM3D (2000) and MP3D (2195); real-world Spot deployment is a demonstration without reported metrics.
inputs: [egocentric RGB-D, odometry, target object category]
outputs: [frontier/value maps, waypoint selection, STOP]
human_repr: [none]
capabilities: {C1: NA, C2: NA, C3: NA, C4: NA, C5: NA, C6: NA, C7: NA, C8: NA, C9: NA, C10: NA, C11: NA, C12: NA, C13: NA, C14: NA, C15: NA, C16: NA, C17: NA, C18: NA, C19: NA, C20: NA, C21: NA, C22: NA, C23: NA, C24: NA, C25: NA}
exp:
  datasets: ['Gibson ObjectNav val (1000 episodes, 5 scenes)', 'HM3D val (2000 episodes, 20 scenes, 6 categories)', 'MP3D val (2195 episodes, 11 scenes, 21 categories)']
  simulators: [Habitat]
  robots: [Boston Dynamics Spot (real demo)]
  environment: indoor homes (sim); office building floor (real)
  indoor_outdoor: indoor
  sensors: [RGB-D, odometry]
  humans: none
  n_scenes: 5 + 20 + 11 sim scenes; 1 real floor
  n_trajectories: 5195 sim episodes
  n_participants: NA
  split: validation splits
  baselines: [PONI, PIRLNav, RegQLearn, SemExp, ZSON, CoW, ESC, SemUtil]
  ablation: Yes (value update method)
  real_robot_trials: Partial (demonstration only)
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: []
metrics: ['NAV | Success Rate (SR) | % | STOP within 1 m of target within 500 steps | p.2, p.5', NAV | SPL | % | success weighted by inverse path length | p.5]
deployment: {fm_model: BLIP-2 + Grounding-DINO + Mobile-SAM + ZoeDepth, model_size: Not reported, api_cloud_local: Local, onboard_offboard: 'Offboard laptop (RTX 4090 Max-Q, 16 GB) for real robot', gpu: RTX 4090 Max-Q mobile (real); 4 GPUs for PointNav training, cpu: Not reported, latency: '''real-time'' stated; no numbers', query_frequency: per step, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Not reported, caching: NA, event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: NA, safety_shield: 'No', emergency_behavior: Not reported, uncertainty: FOV-based confidence channel for value fusion, hallucination_mitigation: NA, real_time_claim_supported: 'Partial (claimed, unquantified)'}
repro: {code: Not reported in text, code_url: NA, dataset: Public benchmarks, dataset_url: NA, checkpoints: NA, prompts_published: Yes (prompt given), hardware_specified: 'Yes', hyperparameters: Partial, protocol_described: 'Yes', project_page: naoki.io/vlfm, concerns: Real-world results qualitative.}
limitations_flags: [limited-scenarios]
web_verification_required: []
cited_missing: [ESC (zero-shot ObjectNav), SemUtil, LGX, ZSON, PIRLNav, VER (Variable Experience Rollout), Grounding-DINO, BLIP-2]
adjacent: {mechanism: 'VLM image-text similarity projected into a top-down value map, fused with confidence weighting, ranks exploration frontiers.', relevance: 'Example of VLM as dense spatial scorer (F5, I3) that avoids vision-to-text bottlenecks; directly analogous to VLM path/trajectory scoring in social navigation.', why_not_direct: Object search only; no humans or social norms., inherited_by: Cited by corpus Cai survey.}
coding: {latency_reported: Partial, safety_mechanism: 'No', uncertainty_treatment: Partial, hallucination_treatment: 'No', code_released: 'No', new_dataset_released: NA, real_robot: Demo, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2024
  authors: *id001
  venue: 2024 IEEE International Conference on Robotics and Automation (ICRA), Yokohama
  volume: NA
  issue: NA
  pages: 42-48
  doi: 10.1109/ICRA57147.2024.10610712
  url: naoki.io/vlfm
  pub_status: conference
  peer_reviewed: 'Yes'
  peer_review_basis: ICRA 2024 header with DOI (IEEE Xplore copy).
project_url: naoki.io/vlfm
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: 2024 IEEE International Conference on Robotics and Automation (ICRA)
  verified_doi: 10.1109/ICRA57147.2024.10610712
  verified_url: https://doi.org/10.1109/ICRA57147.2024.10610712
  verified_pages: 42-48
  arxiv: 2312.03275v1
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1109/ICRA57147.2024.10610712)', arXiv abs page (2312.03275v1)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A0]
  C_capabilities: {SAF1: NA, SAF2: NA, SPA1: NA, SPA2: NA, SPA3: NA, SPA4: NA, HUM1: NA, HUM2: NA, NOR1: NA, NOR2: NA, NOR3: NA, NOR4: NA, EXP1: NA, EXP2: NA, EXP3: NA}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: demo, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "03_Adjacent_Foundation_Model_Navigation"
analytical_category: "S3"
coding:
  latency_reported: "Partial"
  safety_mechanism: "No"
  uncertainty_treatment: "Partial"
  hallucination_treatment: "No"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "Demo"
  human_subject_study: "No"
---

# VLFM (Yokoyama et al., ICRA 2024)

Page convention: PDF index (p.N).

## A. Bibliographic — ICRA 2024, pp.42–48, DOI 10.1109/ICRA57147.2024.10610712. Boston Dynamics AI Institute, Georgia Tech.

## B. Position — S3 adjacent: VLM-scored frontier exploration.

## C. Research problem — prior zero-shot ObjectNav converts vision to text (detectors + LLM), creating bottlenecks and compute needs (p.2). Contribution: language-grounded value maps directly from RGB via BLIP-2 (p.1–2).

## D. Method — occupancy/frontier map from depth; value map with semantic and confidence channels; confidence cos²(θ/(θ_fov/2)·π/2); confidence-weighted fusion; YOLOv7 / Grounding-DINO detection + Mobile-SAM; PointNav policy trained with VER (2.5B steps, ~7 days, 4 GPUs) (p.2–5).

## L. Quantitative results (visually verified p.5)
- Table I (SPL / SR): Gibson VLFM 52.2 / 84.0 vs SemUtil 40.5 / 69.3, PONI 41.0 / 73.6, SemExp 33.9 / 65.7, RegQLearn 31.3 / 63.7; HM3D VLFM 30.4 / 52.5 vs PIRLNav 27.1 / 64.1, ESC 22.3 / 39.2, ZSON 12.6 / 25.5; MP3D VLFM 17.5 / 36.4 vs ESC 14.2 / 28.7, PONI 12.1 / 31.8, ZSON 4.8 / 15.3, CoW 3.7 / 7.4.
- Table II (value update; Gibson / HM3D / MP3D SPL-SR): replacement 48.0-76.1 / 26.5-44.5 / 16.6-31.7; unweighted 50.9-83.0 / 30.0-51.8 / 17.1-35.0; weighted 52.2-84.0 / 30.4-52.5 / 17.5-36.4.
- Stair-requiring episodes cause 14.6% (HM3D) and 9.6% (MP3D) failures (p.6).
- **Data-quality note:** text claims +19.2% SPL and +19.0% SR over SemExp on Gibson (p.5), but Table I gives 52.2 − 33.9 = 18.3 SPL and 84.0 − 65.7 = 18.3 SR.

## N. Limitations
1. **Stated (p.6):** assumes targets visible from default camera height; task-specific value map not reusable for sequential or VLN tasks; single-floor only.
2. **Observable:** real-world deployment unquantified; no dynamic agents.
3. **Social relevance:** mechanism only.

## P. Adjacent analysis — see `adjacent:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue 2024 IEEE International Conference on Robotics and Automation (ICRA); DOI 10.1109/ICRA57147.2024.10610712; pages 42-48; URL https://doi.org/10.1109/ICRA57147.2024.10610712.
- Sources: Crossref (exact title match, DOI 10.1109/ICRA57147.2024.10610712); arXiv abs page (2312.03275v1).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - venue: PDF-derived '2024 IEEE International Conference on Robotics and Automation (ICRA), Yokohama' -> externally verified '2024 IEEE International Conference on Robotics and Automation (ICRA)'
- Changed field - url: PDF-derived 'naoki.io/vlfm' -> externally verified 'https://doi.org/10.1109/ICRA57147.2024.10610712'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

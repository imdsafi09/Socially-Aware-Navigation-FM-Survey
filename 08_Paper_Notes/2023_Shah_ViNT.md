---
id: 2023_Shah_ViNT
source_pdfs: [03_Adjacent_Foundation_Model_Navigation/2306.14846v2.pdf]
duplicate_copies: []
related_versions: []
title: 'ViNT: A Foundation Model for Visual Navigation'
authors: &id001 [Dhruv Shah, Ajay Sridhar, Nitish Dashora, Kyle Stachowicz, Kevin Black, Noriaki Hirose, Sergey Levine]
year: 2023
venue: Proceedings of The 7th Conference on Robot Learning (CoRL 2023), PMLR 229
volume: NA
issue: NA
pages: 711-733
doi: Not found / not applicable
url: https://proceedings.mlr.press/v229/shah23a.html
pub_status: conference
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): PMLR proceedings page (https://proceedings.mlr.press/v229/shah23a.html); arXiv abs page (2306.14846v2). PDF-derived basis (Stage 1): CoRL 2023 footer on p.1 of arXiv v2.'
category: S3
folder: 03_Adjacent_Foundation_Model_Navigation
folder_category_match: 'Yes'
category_rationale: Transformer-based navigation foundation model for image-goal navigation with diffusion subgoal proposals and prompt-tuning adaptation; pedestrian avoidance shown only anecdotally.
paper_type: model
fm_used: 'Yes'
fm_class: [NavFM]
fm_models: [ViNT (31M params; EfficientNet-B0 encoders + 4-layer Transformer), image-to-image diffusion model for subgoal proposals]
fm_size: 31M
method_family: [imitation learning (max-likelihood waypoint + distance), Transformer, diffusion subgoal generation, topological graph search, prompt-tuning adaptation]
roles: [F9, F10]
roles_evidence: {F9: Predicts H=5 normalized future waypoints tracked by PD controller at 4 Hz (p.3-4)., F10: Serves as the visuomotor policy across robots zero-shot (Sec. 6.2).}
integration: I6
integration_rationale: Learned navigation policy with waypoint action space inside a topological-graph planner.
evidence: E3
evidence_rationale: Real-robot exploration and position/GPS/satellite-guided navigation on LoCoBot, Go1, Vizbot, Jackal with success/SPL/distance metrics (Tables 1-3); pedestrian avoidance is a single qualitative example (Fig.11); no human study.
inputs: [current + 5 past RGB frames (85x64), 'subgoal image (or adapted goal token: GPS/routing)']
outputs: [normalized waypoints (H=5), temporal distance]
human_repr: [none explicit (pedestrians only as obstacles in images)]
capabilities: {C1: NA, C2: NA, C3: NA, C4: NA, C5: NA, C6: NA, C7: NA, C8: NA, C9: NA, C10: NA, C11: NA, C12: NA, C13: NA, C14: NA, C15: NA, C16: NA, C17: NA, C18: NA, C19: NA, C20: NA, C21: NA, C22: NA, C23: NA, C24: NA, C25: NA}
exp:
  datasets: [GoStanford, RECON, CoryHall, Berkeley, SCAND-S, SCAND-J, Seattle, TartanDrive, NeBula, SACSoN, BDD]
  simulators: [CARLA (fine-tuning/adaptation)]
  robots: [LoCoBot, Unitree Go 1, Vizbot, Clearpath Jackal, (drone mentioned in text)]
  environment: indoor offices/hallways; outdoor campus/suburban; CARLA towns
  indoor_outdoor: both
  sensors: [monocular/fisheye RGB, wheel odometry / GPS / satellite images (heuristics)]
  humans: incidental pedestrians (one qualitative example)
  n_scenes: Not reported
  n_trajectories: 'CARLA: 181 train / 52 test trajectories'
  n_participants: NA
  split: CARLA Town01 train / Town02 test
  baselines: [End-to-End BC, End-to-End GCG, RECON, ViNT-R (random subgoals), ViKiNG, GNM, single-robot models, Scratch/ImageNet/SimCLR/VC-1 backbones]
  ablation: Yes (subgoal proposal, backbone, data size)
  real_robot_trials: 'Yes'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: ['dynamic pedestrians (qualitative, Fig.11)']
metrics: [NAV | Success | 0-1 | goal reached in coverage exploration / guided navigation | p.7, NAV | SPL | 0-1 | success weighted by path length | p.7, NAV | Distance | m | distance travelled before intervention/collision | p.7, NAV | Maximum displacement without intervention | m | coverage task proxy | p.8, NAV | In Lane | fraction | trajectories staying within driving lane (CARLA) | p.9]
deployment: {fm_model: ViNT, model_size: 31M, api_cloud_local: Local, onboard_offboard: Not reported, gpu: Not reported, cpu: Not reported, latency: Not reported, query_frequency: 4 Hz model, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Not reported, caching: NA, event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: Topological graph / A*-like search, safety_shield: 'No', emergency_behavior: Not reported, uncertainty: NA, hallucination_mitigation: ViNT robust to invalid diffusion subgoals (qualitative), real_time_claim_supported: Partial (4 Hz stated; heavier compute acknowledged)}
repro: {code: 'Yes', code_url: general-navigation-models.github.io, dataset: Yes (public sources), dataset_url: NA, checkpoints: Yes (stated), prompts_published: NA, hardware_specified: Partial, hyperparameters: Yes (appendix), protocol_described: Partial, project_page: general-navigation-models.github.io, concerns: Trial counts per environment not reported; inconsistent training-data hours.}
limitations_flags: [resource-requirements, limited-scenarios]
web_verification_required: []
cited_missing: ['SACSoN (Hirose 2023, social navigation dataset/policy)', ViKiNG, RT-1, I2O, VC-1, BDD100K]
adjacent: {mechanism: Transformer NavFM trained on 80-160 h of cross-robot data; diffusion-proposed subgoals; soft-prompt adaptation to new goal modalities., relevance: Base/backbone for several VLM social-navigation systems (used for low-level execution) and source of the 'emergent pedestrian avoidance' claim; training data includes SCAND and SACSoN (social navigation data)., why_not_direct: 'No language, no social model; pedestrian behaviour only anecdotal.', inherited_by: 'Cited by corpus VL-TGS, BehAV, Cai survey, SocialNav (CVPR 2026), ViLAM, Obstacles-to-Etiquette, G2-Nav.'}
coding: {latency_reported: Partial, safety_mechanism: 'No', uncertainty_treatment: NA, hallucination_treatment: Partial, code_released: 'Yes', new_dataset_released: NA, real_robot: Systematic, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2023
  authors: *id001
  venue: 7th Conference on Robot Learning (CoRL 2023), Atlanta (footer p.1); arXiv:2306.14846v2
  volume: NA
  issue: NA
  pages: 25 (PDF incl. appendix)
  doi: Not reported
  url: general-navigation-models.github.io
  pub_status: conference
  peer_reviewed: 'Yes'
  peer_review_basis: CoRL 2023 footer on p.1 of arXiv v2.
project_url: general-navigation-models.github.io
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: Proceedings of The 7th Conference on Robot Learning (CoRL 2023), PMLR 229
  verified_doi: Not found / not applicable
  verified_url: https://proceedings.mlr.press/v229/shah23a.html
  verified_pages: 711-733
  arxiv: 2306.14846v2
  version_relationship: Corpus copy is arXiv v2; PMLR version authoritative
  sources: ['PMLR proceedings page (https://proceedings.mlr.press/v229/shah23a.html)', arXiv abs page (2306.14846v2)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A6]
  C_capabilities: {SAF1: NA, SAF2: NA, SPA1: NA, SPA2: NA, SPA3: NA, SPA4: NA, HUM1: NA, HUM2: NA, NOR1: NA, NOR2: NA, NOR3: NA, NOR4: NA, EXP1: NA, EXP2: NA, EXP3: NA}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: systematic, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "03_Adjacent_Foundation_Model_Navigation"
analytical_category: "S3"
coding:
  latency_reported: "Partial"
  safety_mechanism: "No"
  uncertainty_treatment: "NA"
  hallucination_treatment: "Partial"
  code_released: "Yes"
  new_dataset_released: "NA"
  real_robot: "Systematic"
  human_subject_study: "No"
---

# ViNT (Shah et al., CoRL 2023)

Page convention: PDF index (p.N).

## A. Bibliographic — CoRL 2023 (footer p.1), arXiv v2 (24 Oct 2023). UC Berkeley.

## B. Position — S3 adjacent: navigation foundation model; frequently used as low-level navigator under VLM planners.

## C. Research problem — what is required of a foundation model for mobile robotics: zero-shot deployment and adaptation (p.1–2). Contributions: ViNT; diffusion-based exploration; adaptation via fine-tuning/prompt-tuning; emergent behaviours (p.2).

## D. Method — EfficientNet-B0 tokenises 5 past + current frames; goal-fusion encoder on stacked current+goal images; 4-layer, 4-head Transformer; predicts distance and H = 5 normalized waypoints (Eq.1); 4 Hz with PD tracking; diffusion subgoals grounded by ViNT distances and scored by heuristic in A*-like physical search (p.3–5).

## L. Quantitative results
- Table 1 (coverage exploration success, Indoor / Outdoor): End-to-End BC 0.72 / 0.44; GCG — / 0.61; RECON 0.19 / 0.23; ViNT-R 0.81 / —; ViNT 0.94 / 1.00.
- Table 2 (ViKiNG vs ViNT): Indoor position success 0.60 vs 0.90, distance 56 m vs 91 m; Outdoor GPS success 0.64 vs 0.95, SPL 0.42 vs 0.84, distance 720 m vs 1270 m; Outdoor satellite success 0.77 vs 1.00, SPL 0.68 vs 0.94, distance 780 m vs 1040 m.
- Table 3 (max displacement m; LoCoBot / Go1 / Vizbot / Jackal): single-robot 40 / 12 / 40 / 184; GNM 60 / 8 / 20 / 427; ViNT 120 / 45 / 110 / 438.
- Second "Table 3" (CARLA; Images success / in-lane; Positions success; Routing success): Scratch 0.45/0.74, 0.79, 0.43; ImageNet 0.22/0.71, 0.59, 0.45; SimCLR 0.21/0.63, 0.70, 0.64; VC-1 0.19/0.65, 0.49, 0.38; GNM 0.49/0.66, 0.45, 0.49; ViNT 0.82/0.82, 0.89, 0.72.
- Pedestrians: one qualitative example (Fig.11) of navigating around two pedestrians.
- **Data-quality notes:** two tables labelled "Table 3"; training data "over 100 hours" (p.4, App. C) vs Table 7 caption "over 150 hours" and table total 160 h (80 h used); Table 7 contains a leftover author note ("Remember to mention: total size…").

## N. Limitations
1. **Stated (p.11):** heavier inference compute (Transformer); assumes structural similarity of robots (no altitude control, no LiDAR).
2. **Observable:** trial counts not reported; pedestrian robustness anecdotal (single scene); no social metrics.
3. **Social relevance:** training includes SACSoN/SCAND, but social compliance not evaluated — "emergent" pedestrian avoidance should not be read as social awareness.

## P. Adjacent analysis — see `adjacent:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue Proceedings of The 7th Conference on Robot Learning (CoRL 2023), PMLR 229; DOI Not found / not applicable; pages 711-733; URL https://proceedings.mlr.press/v229/shah23a.html.
- Sources: PMLR proceedings page (https://proceedings.mlr.press/v229/shah23a.html); arXiv abs page (2306.14846v2).
- Version relationship: Corpus copy is arXiv v2; PMLR version authoritative.
- Changed field - venue: PDF-derived '7th Conference on Robot Learning (CoRL 2023), Atlanta (footer p.1); arXiv:2306.14846v2' -> externally verified 'Proceedings of The 7th Conference on Robot Learning (CoRL 2023), PMLR 229'
- Changed field - pages: PDF-derived '25 (PDF incl. appendix)' -> externally verified '711-733'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified 'Not found / not applicable'
- Changed field - url: PDF-derived 'general-navigation-models.github.io' -> externally verified 'https://proceedings.mlr.press/v229/shah23a.html'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

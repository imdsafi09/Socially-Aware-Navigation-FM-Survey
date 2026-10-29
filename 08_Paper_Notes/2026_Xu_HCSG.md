---
id: 2026_Xu_HCSG
source_pdfs: [05_Direct_VLM_SocialNav_Preprints/2605.13321v1.pdf]
duplicate_copies: []
related_versions: []
title: 'HCSG: Human-Centric Semantic-Geometric Reasoning for Vision-Language Navigation'
authors: &id001 [Haoxuan Xu, Tianfu Li, Wenbo Chen, Yi Liu, Jin Wu, Huashuo Lei, Yunfan Lou, Lujia Wang, Hesheng Wang, Haoang Li]
year: 2026
venue: arXiv:2605.13321v1 [cs.RO], 13 May 2026
volume: NA
issue: NA
pages: '11'
doi: Not found / not applicable
url: https://arxiv.org/abs/2605.13321
pub_status: preprint
peer_reviewed: 'No'
peer_review_basis: 'Publication status: Preprint; Peer reviewed: No verified peer-reviewed version found as of corpus freeze date (2026-10-19). Sources: arXiv abs page (2605.13321v1); Crossref title search: no match.'
category: S5
folder: 05_Direct_VLM_SocialNav_Preprints
folder_category_match: 'Yes'
category_rationale: 'Human-aware VLN: VLM (Qwen3-VL-2B) interprets detected humans'' actions/intentions; descriptions + pose/trajectory forecasts are fused into a topological map for learned waypoint selection with a social distance loss; evaluated on HA-VLN-CE and a real robot.'
paper_type: method
fm_used: 'Yes'
fm_class: [VLM, CLIP-style]
fm_models: [Qwen3-VL-2B-Instruct (semantic reasoning), CLIP text encoder (semantic feature encoding), YOLO-Pose (detection/pose)]
fm_size: 2B (VLM)
method_family: [imitation learning (VLN waypoint policy), cross-modal graph transformer, LSTM trajectory/pose forecasting, social distance loss]
roles: [F1, F2]
roles_evidence: {F1: 'VLM generates natural-language descriptions of human actions and social context from cropped human views (Eq.9, p.5-6).', F2: 'VLM infers human intentions (e.g., ''walking rapidly towards the corridor''); used to recognise interaction targets vs obstacles (p.5-6, Fig.1).'}
integration: I2
integration_rationale: VLM text -> CLIP text features fused with geometric features into topological graph nodes; a learned cross-modal graph transformer selects waypoints (Eq.4-5, p.5).
evidence: E3
evidence_rationale: Closed-loop simulation on HA-VLN-CE (val seen/unseen) plus real-robot evaluation on NXROBO Leo with 5 scenarios x 10 trials vs BEVBert; no human-subject study (p.7-10).
inputs: [RGB-D panoramic (12 views), natural language instruction, 'human tracks (pose keypoints, positions over 6 frames)']
outputs: [semantic description of human activity/intent, learned embedding, waypoint (selection)]
human_repr: [2D pose keypoints (17), 3D position from depth, forecast trajectory and pose (3 frames), natural-language activity/intent description, learned fused node embedding, proximity radius 1.0 m]
capabilities: {C1: 'Yes', C2: 'Yes', C3: Partial, C4: 'No', C5: 'Yes', C6: 'Yes', C7: Partial, C8: Partial, C9: Partial, C10: Partial, C11: Partial, C12: Partial, C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: 'No', C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: 'Yes', C24: Partial, C25: 'No'}
exp:
  datasets: ['HA-VLN-CE / HA-R2R (train 10,819; val seen 778; val unseen 1,839)']
  simulators: [Habitat (HA-VLN-CE)]
  robots: [NXROBO Leo mobile manipulator (RGB-D camera)]
  environment: indoor (Matterport scenes; real office)
  indoor_outdoor: indoor
  sensors: [RGB-D]
  humans: simulated SMPL humans; real pedestrians in office (count not reported)
  n_scenes: 90 scenes (sim); 5 real scenarios
  n_trajectories: 1,839 unseen val episodes; 10 real trials per scenario
  n_participants: Not reported
  split: HA-R2R official
  baselines: [HA-VLN-CMA, HA-VLN-CMA-DA, HA-VLN-VL, LAW-VLNCE, DUET, ETPNav, GridMM, BEVBert]
  ablation: Yes (pose/trajectory, VLM on/off, future vs past features, fine-tuning, social distance losses, RGB/depth)
  real_robot_trials: 'Yes'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [conversational group (approach and stop), pacing person on phone, crossing person, stationary person in hallway, blind corner]
metrics: [SAFETY | Total Collision Rate (TCR) | collisions per episode | overall frequency of human-related collisions | p.7, SAFETY | Collision Rate (CR) | ratio | episodes with >=1 human collision | p.7, NAV | Success Rate (SR) | ratio | episodes completed without collision | p.7, NAV | Navigation Error (NE) | m | included in protocol but not reported in main tables | p.7, NAV | Real-world success rate | count/10 | per scenario | p.9]
deployment: {fm_model: Qwen3-VL-2B-Instruct, model_size: 2B, api_cloud_local: Local, onboard_offboard: Not reported, gpu: 2x A6000 (training), cpu: Not reported, latency: Not reported, query_frequency: 'Event-triggered: only when humans detected at a waypoint; agent pauses to collect 6 frames', planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: No (stop-and-wait design), caching: Not reported, event_triggered: Yes (human detection), distillation: 'No', quantization: 'No', fallback_planner: 'No', safety_shield: No (social distance loss in training only), emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: 'No', real_time_claim_supported: No (stop-and-wait; future work on streaming)}
repro: {code: Project page, code_url: 'https://haoxuanxu1024.github.io/HCSG/', dataset: HA-VLN-CE (public), dataset_url: NA, checkpoints: Not reported, prompts_published: No (task-specific prompt described), hardware_specified: Partial, hyperparameters: 'Yes (iterations, batch, LR, loss coefficients)', protocol_described: 'Yes', project_page: 'https://haoxuanxu1024.github.io/HCSG/', concerns: Main table omits HA-VLN-CMA* (lower seen TCR 3.34 in HA-VLN 2.0); ablation full-model rows correspond to w/o-VLM setting.}
limitations_flags: [latency, limited-scenarios, no-human-study, sim-to-real]
web_verification_required: [Venue status; code release.]
cited_missing: [DRAGON (RA-L 2024), CoRI (CoRL 2025), MapGPT, P3Nav, DUET, GridMM, LAW-VLNCE, Social elastic band with prediction (IJSR 2025), Socially aware crowd navigation via uncertainty-driven risk adaptation (arXiv 2025), From cognition to precognition (ICRA 2025), MotionLLM, Legible and predictable navigation in multi-agent environments (ICRA 2023)]
coding: {latency_reported: 'No', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: 'No', code_released: Partial, new_dataset_released: NA, real_robot: Systematic, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2026
  authors: *id001
  venue: arXiv:2605.13321v1 [cs.RO], 13 May 2026
  volume: NA
  issue: NA
  pages: '11'
  doi: Not reported
  url: https://haoxuanxu1024.github.io/HCSG/
  pub_status: preprint
  peer_reviewed: 'No'
  peer_review_basis: arXiv v1; no venue statement.
project_url: https://haoxuanxu1024.github.io/HCSG/
external_verification:
  verified_on: '2026-10-19'
  status_class: 'C: preprint only'
  verified_venue: arXiv:2605.13321v1 [cs.RO], 13 May 2026
  verified_doi: Not found / not applicable
  verified_url: https://arxiv.org/abs/2605.13321
  verified_pages: NA
  arxiv: 2605.13321v1
  version_relationship: arXiv only
  sources: [arXiv abs page (2605.13321v1), 'Crossref title search: no match']
  peer_reviewed_note: No verified peer-reviewed version found as of corpus freeze date
  publication_status: Preprint
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A2, A5, A6]
  C_capabilities: {SAF1: 'Yes', SAF2: Partial, SPA1: Partial, SPA2: Partial, SPA3: Partial, SPA4: 'No', HUM1: Partial, HUM2: Partial, NOR1: Partial, NOR2: 'Yes', NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: [R2]
  D_interface: [D1]
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: systematic, EV4_real_humans_in_trials: present-type-unreported, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: '1,839 unseen val episodes; 10 real trials per scenario', statistical_testing: 'No', cross_environment: No/unclear, runtime_measured: 'No'}
  cross_cutting: {temporal_coupling: per-decision, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'No', uncertainty: 'No', hallucination_mitigation: 'No', privacy_constraint: 'No', inference_location: local/onboard or local server}
physical_source_folder: "05_Direct_VLM_SocialNav_Preprints"
analytical_category: "S5"
coding:
  latency_reported: "No"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "No"
  code_released: "Partial"
  new_dataset_released: "NA"
  real_robot: "Systematic"
  human_subject_study: "No"
---

# HCSG (Xu, Li et al., arXiv 2026)

Page convention: PDF index (p.N).

## A. Bibliographic — arXiv:2605.13321v1 (13 May 2026); HKUST(GZ), Tsinghua, USTB, NUS, SJTU. Project https://haoxuanxu1024.github.io/HCSG/. Preprint.

## B. Position — S5. Bridges VLN and social navigation: humans as task-relevant agents (interaction targets) rather than obstacles; VLM provides semantic human interpretation.

## C. Research problem — VLN assumes static scenes; human-aware VLN agents treat humans as obstacles; need semantic understanding (activities/intent) + geometric foresight (p.1–2). Claims: "first human-centric framework for VLN" (abstract); +14.3% SR, −34.5% CR (unseen) (p.2).

## D. Technical method — waypoint-based VLN-CE (ETPNav-style predictor); YOLO-Pose detection; on detection pause and collect 6 frames; Geometric stream: LSTM encoder–decoders forecasting pose (17 keypoints) and trajectory (3 future frames) with losses (Eq.7–8); Semantic stream: crop → Qwen3-VL-2B with task prompt → description → CLIP text features (Eq.9–10); fusion MLP into topological node features (Eq.4); cross-modal graph transformer + FFN selects waypoint (Eq.5); Social Distance Loss = collision penalty (δ = 3.0) + proximity loss within r_s = 1.0 m with front-facing weighting (Eq.11–12); total loss Eq.13. Training: pretrain 100k iters (batch 64, lr 5e-5), fine-tune 15k iters (batch 8, lr 1e-5), 2× A6000 (p.7).

## G. Social capabilities
C1, C2 Yes (TCR, CR; proximity loss) · C5, C6 Yes (pose/trajectory forecasting, ablations) · C23 Yes (instructions referencing people, e.g., stop in front of discussing pair) · C3 Partial (1 m proximity loss) · C7, C8 Partial (VLM intent/activity; ablation) · C9, C10 Partial (approach conversational pair, real scenario a) · C11, C12, C24 Partial (waits for person sorting clothes; yields at blind corner) · others No.

## H/I — I2; E3.

## L. Quantitative results
Table I (p.7; TCR / CR / SR): Val seen — HA-VLN-CMA 63.09/0.77/0.05; CMA-DA 17.45/0.61/0.17; HA-VLN-VL 4.44/0.52/0.20; LAW-VLNCE 4.31/0.54/0.21; DUET 4.18/0.48/0.22; ETPNav 4.07/0.43/0.24; GridMM 3.92/0.45/0.24; BEVBert 3.64/0.46/0.27; HCSG 3.63/0.34/0.29. Val unseen — 47.06/0.77/0.07; 27.25/0.69/0.09; 6.63/0.59/0.14; 5.88/0.65/0.15; 5.74/0.63/0.16; 6.94/0.58/0.17; 5.76/0.59/0.18; 4.71/0.55/0.21; HCSG 5.02/0.36/0.24.
- Note: unseen TCR of BEVBert (4.71) is lower than HCSG (5.02); HA-VLN-CMA* (seen TCR 3.34 in HA-VLN 2.0) is omitted from the comparison.
Ablations (unseen TCR/CR/SR): geometry none 6.09/0.48/0.20, pose 5.92/0.47/0.22, trajectory 5.31/0.41/0.22, both 5.21/0.40/0.23; VLM w/o 5.21/0.40/0.23 vs with 5.02/0.36/0.24; past- vs future-oriented 5.25/0.41/0.21 vs 5.21/0.40/0.23; fixed vs fine-tuned 5.27/0.42/0.22 vs 5.21/0.40/0.23; losses none 6.73/0.55/0.20, L_coll 6.35/0.52/0.21, L_prox 6.13/0.50/0.21, both 5.21/0.40/0.23; RGB only 7.31/0.56/0.15, depth only 7.02/0.46/0.21, both 5.21/0.40/0.23.
Table VIII real world (success, BEVBert vs HCSG): (a) stop in front of interacting pedestrians 3/10 vs 9/10; (b) avoid pacing pedestrian on phone 3/10 vs 7/10; (c) navigate to plant avoiding moving human 5/10 vs 9/10; (d) bypass standing human in hallway 6/10 vs 9/10; (e) corridor with corner pedestrian 2/10 vs 7/10; overall 19/50 (38%) vs 41/50 (82%).
- VLM contribution is modest in sim (unseen CR 0.40 → 0.36; SR 0.23 → 0.24).

## N. Limitations
1. **Stated:** stop-and-wait design (future: continuous streaming); fixed social distance priors (future: adaptive, context-conditioned) (p.10).
2. **Observable:** real-world "preliminary" (authors' word), single office, no human perception study; no latency reported; VLM queried only after pausing.

## P. Direct-paper questions (abridged)
1 Instruction-conditioned navigation among humans who may be targets or obstacles. 2 Interpret activities/intentions referenced in instructions. 3 Qwen3-VL-2B. 4 Cropped human images. 5 Task-specific prompt (not published). 6 Description text. 7 CLIP-encoded → fused graph features → learned waypoint selection. 8 No. 9 VLN policy + low-level navigation. 10 Training-time social loss only. 11 Socially intelligent human-centric navigation. 12 TCR/CR/SR; real SR. 13 Yes. 14 Partial. 15 Yes (language). 16 Yes (language). 17 Implicit. 18 6-frame window. 19 No. 20 No. 21 No. 22 Not reported. 23 Yes. 24 No. 25 Lower CR, higher SR; real 82% vs 38%. 26 Cannot conclude human comfort, social acceptability, or real-time viability.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: C: preprint only; venue arXiv:2605.13321v1 [cs.RO], 13 May 2026; DOI Not found / not applicable; pages NA; URL https://arxiv.org/abs/2605.13321.
- Sources: arXiv abs page (2605.13321v1); Crossref title search: no match.
- Version relationship: arXiv only.
- Changed field - doi: PDF-derived 'Not reported' -> externally verified 'Not found / not applicable'
- Changed field - url: PDF-derived 'https://haoxuanxu1024.github.io/HCSG/' -> externally verified 'https://arxiv.org/abs/2605.13321'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

---
id: 2026_Elnoor_ViLAM
source_pdfs: [05_Direct_VLM_SocialNav_Preprints/2503.09820v2.pdf]
duplicate_copies: []
related_versions: ['arXiv v1 (2025) titled ''Vi-LAD: Vision-Language Attention Distillation for Socially-Aware Robot Navigation in Dynamic Environments'' (as cited by GSON [45] and Cai 2026 [70]); not in corpus']
title: 'ViLAM: Distilling Vision-Language Reasoning into Attention Maps for Social Robot Navigation'
authors: &id001 [Mohamed Elnoor, Kasun Weerakoon, Gershom Seneviratne, Jing Liang, Vignesh Rajagopal, Dinesh Manocha]
year: 2026
venue: arXiv:2503.09820v2 [cs.RO], 6 Mar 2026
volume: NA
issue: NA
pages: '8'
doi: Not found / not applicable
url: https://arxiv.org/abs/2503.09820
pub_status: preprint
peer_reviewed: 'No'
peer_review_basis: 'Publication status: Preprint; Peer reviewed: No verified peer-reviewed version found as of corpus freeze date (2026-10-19). Sources: arXiv abs page (2503.09820v2); Crossref title search: no match.'
category: S5
folder: 05_Direct_VLM_SocialNav_Preprints
folder_category_match: 'Yes'
category_rationale: Distils GPT-4o social reasoning (frontier crowding likelihood) into attention maps of a vision-action model; the maps act as a social cost map for a DWA-style planner on a real robot among people.
paper_type: method
fm_used: 'Yes'
fm_class: [VLM]
fm_models: ['GPT-4o (offline annotation, CoT prompting)', 'VANP (self-supervised vision-action model, ResNet-50 + Transformer encoder) as base']
fm_size: Not reported
method_family: [distillation (attention-level), LoRA fine-tuning, chain-of-thought prompting, DWA-style local planning]
roles: [F2, F6, F8, F11]
roles_evidence: {F11: 'GPT-4o annotates ~10k SCAND images with likelihood of left/centre/right frontiers becoming crowded (Eq.2-3, p.4, p.5).', F8: 'VLM-derived attention-like maps supervise LoRA fine-tuning of VANP attention via SSIM/cosine loss (Eq.4, p.5).', F2: Teacher estimates where pedestrians are likely to move/crowd (frontier crowding likelihood) - anticipatory human-motion inference (p.4)., F6: 'Distilled attention map A_ViLAM is used as social cost soc(v,w) = max over projected trajectory (Eq.5-7, p.5).'}
integration: I4
integration_rationale: Distilled (student) attention map serves as social cost map in planner objective J = b1 goal + b2 soc (p.5).
evidence: E3
evidence_rationale: Real-world Husky experiments in 4 scenarios (2 outdoor, 2 indoor) with pedestrians, 10 trials per method; no human-subject evaluation (p.6-7).
inputs: [RGB (image sequence), goal, IMU]
outputs: [learned embedding/attention map, cost (social cost map), velocity/action]
human_repr: [attention-map saliency over regions likely occupied by pedestrians, VLM frontier crowding likelihood (training only)]
capabilities: {C1: 'Yes', C2: 'No', C3: Partial, C4: 'No', C5: Partial, C6: Partial, C7: Partial, C8: 'No', C9: 'No', C10: 'No', C11: Partial, C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: Partial, C18: 'No', C19: 'No', C20: Partial, C21: 'No', C22: 'No', C23: 'No', C24: Partial, C25: 'No'}
exp:
  datasets: ['SCAND outdoor subset, ~10k GPT-4o-annotated images (D_VLM)']
  simulators: []
  robots: [Clearpath Husky]
  environment: 2 outdoor and 2 indoor real scenarios
  indoor_outdoor: both
  sensors: [Intel RealSense D435i (RGB), IMU]
  humans: real dynamic and sitting people (counts not reported)
  n_scenes: 4 scenarios
  n_trajectories: 10 trials per method per scenario
  n_participants: Not reported
  split: Trained on outdoor trajectories only; tested indoor and outdoor
  baselines: [DWA (2D LiDAR), CoNVOI, VANP, ViLAM w/o image sequence]
  ablation: Yes (no image sequence)
  real_robot_trials: 'Yes'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [dynamic human + static obstacles, dynamic human + fence + low curb, multiple sitting/walking humans with furniture, multiple walking humans under lighting changes]
metrics: [NAV | Success Rate | % | goal reached without freezing or colliding | p.6, NAV | Time to Goal | s | average time in successful trials | p.6, OTHER | Frechet Distance | m (implied) | similarity to human teleoperated trajectory | p.6, DEPLOY | Inference rate | Hz | ~20 Hz on Intel i9 + RTX 2080 | p.7]
deployment: {fm_model: Distilled VANP+LoRA at runtime (no VLM queries), model_size: Not reported, api_cloud_local: Local (teacher GPT-4o offline), onboard_offboard: 'Onboard laptop (Intel i9, RTX 2080)', gpu: RTX 2080 (onboard); A6000 (training), cpu: Intel i9, latency: ~20 Hz inference, query_frequency: No VLM queries at runtime, planner_frequency: ~20 Hz (system), controller_frequency: Not reported, asynchronous: NA, caching: NA, event_triggered: NA, distillation: 'Yes', quantization: 'No', fallback_planner: 'No', safety_shield: Reduced velocity set V_r filters collision-prone trajectories (sensor for this not specified), emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: Offline annotation; teacher errors not audited, real_time_claim_supported: Yes (~20 Hz measured)}
repro: {code: Not reported, code_url: NA, dataset: Not released (stated), dataset_url: NA, checkpoints: NA, prompts_published: No (described only), hardware_specified: 'Yes', hyperparameters: 'No (lambda_VLM, beta not given)', protocol_described: Partial, project_page: Not reported, concerns: Prompt and lambda_VLM unreported; preprint.}
limitations_flags: [limited-scenarios, no-human-study, dataset-bias]
web_verification_required: [Check whether ViLAM/Vi-LAD has been accepted at a venue.]
cited_missing: [VANP (IROS 2024), 'Physically grounded VLMs outdoor navigation (arXiv:2409.20445)', Long-term human trajectory prediction with 3D dynamic scene graphs, Human-inspired multi-agent navigation via distillation (IROS 2021), CLIPSeg, F-VLM]
coding: {latency_reported: 'Yes', safety_mechanism: 'Yes', uncertainty_treatment: 'No', hallucination_treatment: 'No', code_released: 'No', new_dataset_released: 'No', real_robot: Systematic, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2026
  authors: *id001
  venue: arXiv:2503.09820v2 [cs.RO], 6 Mar 2026
  volume: NA
  issue: NA
  pages: '8'
  doi: Not reported
  url: Not reported
  pub_status: preprint
  peer_reviewed: 'No'
  peer_review_basis: arXiv v2 with no venue statement (p.1).
external_verification:
  verified_on: '2026-10-19'
  status_class: 'C: preprint only'
  verified_venue: arXiv:2503.09820v2 [cs.RO], 6 Mar 2026
  verified_doi: Not found / not applicable
  verified_url: https://arxiv.org/abs/2503.09820
  verified_pages: NA
  arxiv: 2503.09820v2
  version_relationship: arXiv only; no venue on UMD project page
  sources: [arXiv abs page (2503.09820v2), 'Crossref title search: no match']
  peer_reviewed_note: No verified peer-reviewed version found as of corpus freeze date
  publication_status: Preprint
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A3, A6]
  C_capabilities: {SAF1: Partial, SAF2: 'No', SPA1: Partial, SPA2: 'No', SPA3: 'No', SPA4: Partial, HUM1: Partial, HUM2: Partial, NOR1: Partial, NOR2: 'No', NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: Partial}
  B_roles: [R2]
  D_interface: [D7]
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'No', EV3_physical_robot: systematic, EV4_real_humans_in_trials: present-type-unreported, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: 10 trials per method per scenario, statistical_testing: 'No', cross_environment: 'Yes', runtime_measured: 'Yes'}
  cross_cutting: {temporal_coupling: training-only, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'Yes', uncertainty: 'No', hallucination_mitigation: 'No', privacy_constraint: 'No', inference_location: n/a (FM used at training time only)}
physical_source_folder: "05_Direct_VLM_SocialNav_Preprints"
analytical_category: "S5"
coding:
  latency_reported: "Yes"
  safety_mechanism: "Yes"
  uncertainty_treatment: "No"
  hallucination_treatment: "No"
  code_released: "No"
  new_dataset_released: "No"
  real_robot: "Systematic"
  human_subject_study: "No"
---

# ViLAM (Elnoor et al., arXiv v2 2026)

Page convention: PDF index (p.N).

## A. Bibliographic — arXiv:2503.09820v2 (6 Mar 2026), UMD GAMMA. Earlier version "Vi-LAD" cited by GSON and the Cai survey. Preprint; not peer-reviewed.

## B. Position — S5. FM-as-teacher distilled into a spatial cost representation; runtime contains no VLM.

## C. Research problem — VLM reasoning is valuable but too heavy for real-time onboard use; distil into attention maps (p.1–2). Claims: attention-level distillation (28.7% closer Fréchet), SSIM-style loss (14.2–50% success improvement), DWA-adapted planner (p.2).

## D. Technical method
- Data: SCAND subset; three frontiers (left/centre/right) overlaid as coloured rectangles; GPT-4o CoT estimates likelihood of each frontier becoming crowded → A_VLM; ~10k pairs (Eq.2–3, p.4).
- Model: VANP (ResNet-50 + Transformer, CLS + register tokens) frozen; copy with LoRA adapters fine-tuned; loss L = (1−λ)·L_SSIM(A_ViLAM, A_pretrained) + λ·L_SSIM(A_ViLAM, A_VLM), L_SSIM = cosine similarity of flattened maps (Eq.4, p.5).
- Planner: admissible → reduced velocity set; J(v,ω) = β1 goal + β2 soc; soc = max attention along homography-projected short-horizon unicycle trajectory (Eq.5–7).
- Hardware: train A6000; deploy Husky with D435i, laptop i9 + RTX 2080 (p.5).

## E. Human/social representation — implicit attention saliency; teacher's notion of regions likely to become crowded.

## F. Roles — F11, F8, F2, F6. ## H. Integration — I4. ## I. Evidence — E3.

## G. Social capabilities
C1 Yes (collisions count as failure) · C3 Partial (keeps away from humans; qualitative) · C5–C7 Partial (anticipation via attention; qualitative) · C11 Partial · C17 Partial (multiple humans) · C20 Partial (Fréchet to teleop) · C24 Partial · others No.

## J. Experimental evidence — 4 real scenarios × 10 trials; baselines DWA, CoNVOI, VANP, ablation; trained only on outdoor data, tested indoor too (p.6).

## L. Quantitative results (Table I, p.7; Success % / Time to Goal s / Fréchet)
- Scen.1: DWA 80/13.6/1.631; CoNVOI 80/21.4/0.537; VANP 70/16.3/1.321; ViLAM w/o seq 80/14.1/0.643; ViLAM 100/12.2/0.431.
- Scen.2: DWA 20/14.2/1.219; CoNVOI 60/21.4/0.755; VANP 40/17.9/1.446; w/o seq 60/18.3/1.256; ViLAM 90/15.5/0.732.
- Scen.3: DWA 30/16.6/1.521; CoNVOI 60/27.2/1.321; VANP 50/18.4/2.271; w/o seq 40/21.2/1.745; ViLAM 90/17.2/1.231.
- Scen.4: DWA 70/18.9/2.214; CoNVOI 50/32.4/1.452; VANP 40/19.2/2.821; w/o seq 60/27.6/2.139; ViLAM 80/22.4/1.034.
- Note: caption says metrics averaged over successful and unsuccessful trials, whereas Time to Goal defined over successful trials (p.6 vs p.7) — definitional inconsistency. ~20 Hz inference (p.7).

## M. Deployment — fully onboard at ~20 Hz; no runtime VLM.

## N. Limitations
1. **Stated (p.7):** distilled priors learned offline; may need tuning in highly crowded or unseen settings.
2. **Future work:** depth/LiDAR modalities; online adaptation; long-horizon navigation.
3. **Observable:** teacher signal is coarse (3 frontiers); no proxemic metric; λ unspecified; preprint.

## P. Direct-paper questions (abridged)
1 Socially aware local navigation without online VLM. 2 VLM commonsense about crowding/human motion. 3 GPT-4o (teacher). 4 Annotated RGB (teacher); RGB sequence (student). 5 CoT frontier-likelihood prompt (not published). 6 Frontier likelihoods → attention maps. 7 Student attention map → social cost in DWA-style planner. 8 No. 9 Planner. 10 Velocity filtering. 11 Social compliance, anticipation. 12 Success, time, Fréchet. 13 Implicit. 14 No. 15 Implicit. 16 No. 17 Implicit. 18 Image sequence. 19 No. 20 Not addressed. 21 ~20 Hz. 22 Yes. 23 Yes. 24 No. 25 Higher success and lower Fréchet. 26 Cannot conclude proxemic compliance or human comfort; teacher-label quality unknown.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: C: preprint only; venue arXiv:2503.09820v2 [cs.RO], 6 Mar 2026; DOI Not found / not applicable; pages NA; URL https://arxiv.org/abs/2503.09820.
- Sources: arXiv abs page (2503.09820v2); Crossref title search: no match.
- Version relationship: arXiv only; no venue on UMD project page.
- Changed field - doi: PDF-derived 'Not reported' -> externally verified 'Not found / not applicable'
- Changed field - url: PDF-derived 'Not reported' -> externally verified 'https://arxiv.org/abs/2503.09820'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

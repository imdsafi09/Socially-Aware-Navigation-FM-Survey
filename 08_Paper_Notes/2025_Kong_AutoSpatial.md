---
id: 2025_Kong_AutoSpatial
source_pdfs: [04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/auto_spatial.pdf]
duplicate_copies: []
related_versions: []
title: 'AutoSpatial: Visual-Language Reasoning for Social Robot Navigation through Efficient Spatial Reasoning Learning'
authors: &id001 [Yangzhe Kong, Daeun Song, Jing Liang, Dinesh Manocha, Ziyu Yao, Xuesu Xiao]
year: 2025
venue: 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
volume: NA
issue: NA
pages: 11298-11304
doi: 10.1109/IROS60139.2025.11245987
url: https://doi.org/10.1109/IROS60139.2025.11245987
pub_status: conference
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1109/IROS60139.2025.11245987); arXiv abs page (2503.07557v2). PDF-derived basis (Stage 1): IEEE IROS 2025 proceedings header with DOI (p.1).'
category: S4
folder: 04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core
folder_category_match: 'Yes'
category_rationale: Fine-tunes a 7B VLM for social-navigation reasoning (perception, prediction, CoT, final action, explanation) with structured spatial grounding; offline evaluation only.
paper_type: method
fm_used: 'Yes'
fm_class: [VLM]
fm_models: [LLaVA-1.6 OneVision-7B (fine-tuned), 'GPT-4o, Gemini 2.0 Flash, Claude 3.5 Sonnet (evaluators)']
fm_size: 7B
method_family: [supervised fine-tuning (instruction tuning), rule-based auto-labelling, two-round VQA, chain-of-thought]
roles: [F1, F2, F4, F11]
roles_evidence: {F1: 'Structured spatial perception of pedestrians: 5 angular zones x 5 distance bins, 8 directions + stationary (p.2).', F2: 'Movement prediction (started/continued motion, left/right turn, stop) and interaction descriptions (p.4); not intention in a deeper sense.', F4: 'CoT reasoning and final action referencing norms (e.g., ''first arrive, first cross'', Fig.2, p.3).', F11: 'GPT-4o, Gemini 2.0 Flash, Claude 3.5 Sonnet used as ''expert systems'' scoring outputs 1-10 (p.4) - evaluation role, not navigation.'}
integration: I1
integration_rationale: Outputs natural-language final action; no connection to a planner or robot is reported.
evidence: E1
evidence_rationale: 'Evaluation is offline: keyword-matched spatial accuracy on CODA test frames and LLM/human scoring of SNEI answers; no robot or simulation navigation (p.4-6).'
inputs: [RGB (single image), natural language question/system prompt with spatial grounding]
outputs: ['semantic labels (zone, distance, direction)', natural-language reasoning, natural-language high-level action, explanation, VQA answer]
human_repr: [discretised relative position (5 zones x 5 distance bins), discretised motion direction (8 + stationary), movement-pattern class, 'interaction pattern (conflict, crossing, pass-by)', group dynamics description (manual round-2), semantic description]
capabilities: {C1: 'No', C2: 'No', C3: 'No', C4: 'No', C5: Partial, C6: Partial, C7: Partial, C8: 'No', C9: Partial, C10: 'No', C11: Partial, C12: Partial, C13: Partial, C14: 'No', C15: Partial, C16: 'No', C17: Partial, C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: 'No', C24: Partial, C25: 'No'}
exp:
  datasets: ['CODA (UT Campus Object Dataset) auto-labelled VQA: 6,205 train frames (16,530 pedestrians) / 573 test frames (1,542 pedestrians)', 72 manually annotated CODA scenarios, SNEI benchmark (49 sampled scenarios for human eval)]
  simulators: []
  robots: []
  environment: urban campus images (CODA, SNEI)
  indoor_outdoor: both (dataset images)
  sensors: [RGB]
  humans: real (dataset images)
  n_scenes: 72 manual + CODA frames; 49 SNEI scenarios for human eval
  n_trajectories: NA
  n_participants: 7 human evaluators (mostly CS graduate students)
  split: CODA 90/10 after direction balancing
  baselines: [Vanilla LLaVA-1.6 OneVision-7B, LLaVA-M (fine-tuned on 72 manual annotations only)]
  ablation: Yes (data mixing ratios D1-D5; A72/A36/A0 manual annotations; P&P-only, R-only VQAs)
  real_robot_trials: 'No'
  human_study: No (evaluators rank text outputs)
  statistical_testing: 'No'
  scenarios: [crossing, pass-by, trajectory conflict, intersection, crowd/sidewalk (dataset)]
metrics: ['VLM | CODA Benchmark score | 0-1 | keyword-matched accuracy on movement direction and relative position; 1.0 exact, 0.5 approximately correct | p.4', 'VLM | Expert-system cross-validation score (P&P, R, A, E) | 1-10 | score by GPT-4o / Gemini 2.0 Flash / Claude 3.5 Sonnet | p.4', 'VLM | Human evaluator ranking (P&P, R, A, E) | rank (lower better) | relative ranking of 3 models by 7 evaluators | p.4-5']
deployment: {fm_model: LLaVA-1.6 OneVision-7B, model_size: 7B, api_cloud_local: Local (training on 4x A100 80GB), onboard_offboard: 'Not reported (7B chosen as onboard-feasible, claim only)', gpu: 4x A100 80GB (training), cpu: Not reported, latency: Not reported, query_frequency: NA, planner_frequency: NA, controller_frequency: NA, asynchronous: NA, caching: NA, event_triggered: NA, distillation: 'No', quantization: 'No', fallback_planner: NA, safety_shield: NA, emergency_behavior: NA, uncertainty: 'No', hallucination_mitigation: Structured spatial terminology reduces ambiguity (claim), real_time_claim_supported: NA}
repro: {code: Not reported, code_url: Not reported, dataset: Partial (built on public CODA and SNEI; auto-label rules described; generated data release not stated), dataset_url: Not reported, checkpoints: Not reported, prompts_published: Partial (VQA example Fig.2), hardware_specified: Yes (training), hyperparameters: 'Yes (AdamW, lr 2e-5, batch 8, grad accum 4)', protocol_described: 'Yes', project_page: Not reported, concerns: LLM-as-judge evaluation; inconsistency of AS-A72D1 GPT-4o E score between Table I (6.471) and Table II (6.065).}
limitations_flags: [spatial-reasoning-failure, intention-ambiguity, low-level-grounding]
web_verification_required: []
cited_missing: [CODA (UT Campus Object Dataset), Kamath 2023 What's up with VLMs, Zhang 2024 spatial frame of reference, APPLD, Daza 2021 proxemics crowded, Luber 2012 socially-aware navigation learning approach, 'TGS arXiv:2408.02454 (published as VL-TGS RA-L 2025 - in corpus)']
coding: {latency_reported: 'No', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: Partial, code_released: 'No', new_dataset_released: 'No', real_robot: 'No', human_subject_study: Text-raters/other}
pdf_metadata_stage1:
  year: 2025
  authors: *id001
  venue: 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2025), Hangzhou
  volume: Not reported
  issue: Not reported
  pages: 11298-11304
  doi: 10.1109/IROS60139.2025.11245987
  url: Not reported
  pub_status: conference
  peer_reviewed: 'Yes'
  peer_review_basis: IEEE IROS 2025 proceedings header with DOI (p.1).
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
  verified_doi: 10.1109/IROS60139.2025.11245987
  verified_url: https://doi.org/10.1109/IROS60139.2025.11245987
  verified_pages: 11298-11304
  arxiv: 2503.07557v2
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1109/IROS60139.2025.11245987)', arXiv abs page (2503.07557v2)]
snei_usage: {reported_quantity: '49', unit: scenarios (random sample for human evaluation), what_it_represents: Evaluation subset of SNEI, page: p.4, remark: Expert-system scoring on SNEI benchmark; size of full set used not stated, provenance_note: SNEI provenance (SCAND vs SCAND+MuSoHu) UNRESOLVED; see SNEI_DATASET_RECONCILIATION.md}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A5]
  C_capabilities: {SAF1: 'No', SAF2: 'No', SPA1: 'No', SPA2: Partial, SPA3: Partial, SPA4: Partial, HUM1: Partial, HUM2: Partial, NOR1: Partial, NOR2: 'No', NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: [R1, R2, R3]
  D_interface: [D0]
  E_evidence_profile: {EV1_offline: 'Yes', EV2_closed_loop_sim: 'No', EV3_physical_robot: none, EV4_real_humans_in_trials: none, EV5_human_evaluation: text-raters, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: NA, statistical_testing: 'No', cross_environment: No/unclear, runtime_measured: 'No'}
  cross_cutting: {temporal_coupling: offline, memory: 'No', continual_adaptation: 'No', explanation_output: 'Yes (text output, not delivered to people)', safety_guard: 'No', uncertainty: 'No', hallucination_mitigation: Partial, privacy_constraint: 'No', inference_location: n/a (offline evaluation only)}
physical_source_folder: "04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core"
analytical_category: "S4"
coding:
  latency_reported: "No"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "Partial"
  code_released: "No"
  new_dataset_released: "No"
  real_robot: "No"
  human_subject_study: "Text-raters/other"
---

# AutoSpatial (Kong et al., IROS 2025)

Page convention: PDF index (p.N); printed pp.11298–11304.

## A. Bibliographic
`04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/auto_spatial.pdf`. Kong, Song, Liang, Manocha, Yao, Xiao (GMU, UMD). IROS 2025, pp.11298–11304, DOI 10.1109/IROS60139.2025.11245987. Conference; peer-reviewed.

## B. Position — S4
Direct social-navigation VLM reasoning model (same group/protocol as Social-LLaVA/SNEI); targets the spatial-grounding weakness of VLMs. Evaluated only offline; no navigation.

## C. Research problem
- **Problem:** VLMs' poor spatial grounding (relative positions, movement) and lack of domain data for social navigation (p.1).
- **Key observation (authors):** VLMs "struggle with fundamental spatial reasoning, leading to incorrect actions even when high-level reasoning appears sound" (p.2).
- **Contributions:** AutoSpatial approach; automatic labelling with two-round VQA including individual and group motion understanding; evaluation with expert LLM systems and human rankings, improvements up to 10.71% (P&P), 16.26% (reasoning), 20.50% (action), 18.73% (explanation) vs models trained only on manual data (p.1–2).

## D. Technical method
- **Structured spatial grounding (p.2):** 5 angular zones by bbox centre pixel (on the left / slightly left / directly in front / slightly right / on the right); 5 distance bins (very close <3 m, close 3–6 m, moderate 6–9 m, far 9–12 m, very far >12 m); 8 compass directions + stationary in robot frame (forward = north).
- **Auto-labelling (p.3–4):** rule-based heuristics on CODA trajectories/bboxes (no VLMs): spatial perception; movement prediction via sliding-window velocity → 5 patterns; interaction description (trajectory conflict, path crossing W→E/E→W, pass-by, others).
- **Manual annotations:** 72 challenging CODA scenarios (high density, complex grouping) annotated per SNEI 5-task protocol with spatial guideline (p.4).
- **Two-round VQA:** round 1 auto-labelled per-pedestrian (P, Pr, CoT); round 2 (manual only) scene-level synthesis including group dynamics + Final Action + Explanation (Fig.2, p.3). Bounding boxes only provided in training.
- **Training (p.4):** LLaVA-1.6 OneVision-7B, default LLaVA instruction tuning, AdamW lr 2e-5, batch 8, grad-accum 4, 4× A100 80GB; 18,615 VQA pairs total (72 manual + CODA).
- INPUT: single RGB + question. OUTPUT: text (perception, prediction, CoT, final action, explanation).

## E. Human/social representation
Discretised position/distance/direction per pedestrian; movement pattern class; interaction class; scene-level group dynamics in language (manual round). No metric trajectories at inference.

## F. Roles — F1, F2 (movement prediction), F4; F11 for FMs used as evaluators.

## G. Social capabilities (OFFLINE only)
C5, C6 Partial (direction and movement prediction accuracy on CODA); C7 Partial (movement intent); C9 Partial (group dynamics in manual round-2 data, not separately evaluated); C11–C13, C15, C17 Partial (CoT/actions on sidewalk/crossing scenes, e.g. yielding to first-arriving pedestrian); C24 Partial; all others No.

## H. Integration — I1. ## I. Evidence — E1.

## J. Experimental evidence
CODA 90/10 split after directional balancing: 6,205 train frames (16,530 pedestrian instances), 573 test frames (1,542) (p.4). SNEI expert-system scoring (1–10) by Gemini 2.0 Flash, GPT-4o, Claude 3.5 Sonnet; human rankings by 7 evaluators on 49 SNEI scenarios (p.4). Baselines: vanilla LLaVA-1.6-OV-7B, LLaVA-M. Proprietary large models deliberately not compared as they "prohibit inference onboard a mobile robot" (p.5) — no onboard latency measured.

## K. Metrics — CODA keyword score; expert cross-validation scores; human rankings.

## L. Quantitative results (visually verified, p.5)
Table I (selected rows; P&P/R/A/E):
| Model | CODA | Gemini 2.0 Flash | GPT-4o | Claude 3.5 Sonnet |
|---|---|---|---|---|
| AS-A72D1 | 0.710 | 6.824 / 7.079 / 7.292 / 7.258 | 6.838 / 6.338 / 6.290 / 6.471 | 6.652 / 5.831 / 6.385 / 6.065 |
| AS-A72D2 | 0.582 | 6.883 / 7.070 / 7.272 / 7.264 | 6.862 / 6.221 / 6.302 / 6.413 | 6.677 / 5.671 / 6.351 / 6.000 |
| AS-A72D3 | 0.573 | 6.775 / 7.048 / 7.360 / 7.310 | 6.813 / 6.077 / 6.250 / 6.269 | 6.674 / 5.591 / 6.292 / 5.957 |
| AS-A72D5 | 0.483 | 6.627 / 6.878 / 7.280 / 7.270 | 6.739 / 5.947 / 6.114 / 6.139 | 6.504 / 5.490 / 6.151 / 5.831 |
| AS-A36D1 | 0.686 | 6.661 / 6.996 / 7.277 / 7.227 | 6.764 / 6.135 / 6.167 / 6.247 | 6.584 / 5.613 / 6.234 / 5.936 |
| AS-A0D1 | 0.680 | 6.484 / 6.660 / 6.859 / 6.756 | 6.582 / 5.517 / 5.733 / 5.920 | 6.551 / 5.415 / 4.831 / 5.375 |
| LLaVA-M | 0.404 | 6.246 / 6.089 / 6.108 / 6.157 | 6.662 / 5.815 / 5.791 / 6.351 | 6.031 / 5.065 / 5.342 / 5.302 |
| Vanilla-LLaVA | 0.376 | 6.243 / 6.083 / 6.102 / 6.154 | 6.486 / 5.492 / 5.458 / 6.092 | 5.809 / 4.815 / 4.803 / 5.409 |

Table II ablation (CODA; Gemini P&P/R/A/E; GPT-4o; Claude): AS-A72D1-P&P-VQA 0.709 | 6.781/7.014/7.203/7.153 | 6.832/6.194/6.185/6.004 | 6.652/5.717/6.375/6.010; AS-A72D1-R-VQA-1 0.518 | 6.717/7.008/7.246/7.206 | 6.601/5.541/5.767/5.542 | 6.621/5.684/6.323/5.982; AS-A72D1-R-VQA-2 0.520 | 6.751/7.126/7.287/7.246 | 6.835/6.231/6.287/6.010 | 6.584/5.853/6.397/6.050; AS-A72D1 0.710 | 6.824/7.079/7.292/7.258 | 6.838/6.338/6.290/**6.065** | 6.652/5.831/6.385/6.065.
- **Data-quality issue:** AS-A72D1 GPT-4o Explanation is 6.471 in Table I but 6.065 in Table II.
Table III human rankings (lower better, P&P/R/A/E): AS-A72D1 1.19/1.70/1.43/1.55; LLaVA-M 2.89/2.02/2.03/1.73; Vanilla LLaVA 2.93/2.03/2.55/2.53.
- Note: AS-A0D1 (no manual data) CODA 0.680 is close to AS-A72D1 (0.710) and *higher* than D2–D5 variants; authors say AS-A0D1 achieves "only a marginal improvement over Vanilla-LLaVA" in expert scores (p.6).

## M. Deployment — none measured; onboard suitability of 7B asserted only.

## N. Limitations
1. **Stated (p.6):** occasionally misinterprets subtle cues (gaze direction, body orientation) crucial for intent; sometimes reverts to ambiguous camera-relative descriptions, likely due to data limitations.
2. **Future work:** further refinement in human behaviour understanding (p.6–7).
3. **Observable:** offline-only; LLM-as-judge scoring (no correlation with human judgement reported); single-image input; no robot integration; table inconsistency noted.
4. Deferred.

## O. Reproducibility — training hyperparameters given; code/data release not stated.

## P. Direct-paper questions
1 Spatially grounded social reasoning for navigation decisions. 2 Commonsense social reasoning + language explanation. 3 LLaVA-1.6-OV-7B fine-tuned. 4 Single RGB image (bboxes only at training). 5 System prompt with spatial grounding + multi-task question. 6 Text perception/prediction/CoT/action/explanation. 7 Not converted. 8 No robot. 9 None. 10 None. 11 More accurate spatial perception, prediction, reasoning and socially appropriate actions. 12 Offline text quality. 13 Yes. 14 Partial (language group dynamics). 15 Partial (movement). 16 No. 17 Partial. 18 No (single frame at inference; temporal only in auto-labels). 19 No. 20 Not explicitly. 21 NA. 22 NA. 23 No. 24 No. 25 None for navigation. 26 Nothing about closed-loop navigation, safety, latency, or human-perceived behaviour can be concluded.

## Q. Cited works possibly missing
CODA dataset; Kamath et al. 2023 "What's up with VLMs"; Zhang et al. 2024 spatial frame-of-reference; APPLD.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS); DOI 10.1109/IROS60139.2025.11245987; pages 11298-11304; URL https://doi.org/10.1109/IROS60139.2025.11245987.
- Sources: Crossref (exact title match, DOI 10.1109/IROS60139.2025.11245987); arXiv abs page (2503.07557v2).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - venue: PDF-derived '2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2025), Hangzhou' -> externally verified '2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)'
- Changed field - volume: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - issue: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - url: PDF-derived 'Not reported' -> externally verified 'https://doi.org/10.1109/IROS60139.2025.11245987'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

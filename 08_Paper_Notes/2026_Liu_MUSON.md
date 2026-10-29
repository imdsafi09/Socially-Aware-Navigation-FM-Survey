---
id: 2026_Liu_MUSON
source_pdfs: [05_Direct_VLM_SocialNav_Preprints/2512.22867v2.pdf]
duplicate_copies: [06_Datasets_Benchmarks_Evaluation/2512.22867v2.pdf]
related_versions: [arXiv v1 Dec 2025 (cited as 2025 by Cai survey); v2 3 Jul 2026 in corpus]
title: 'MUSON: A Reasoning-oriented Multimodal Dataset for Socially Compliant Navigation in Urban Environments'
authors: &id001 [Zhuonan Liu, Xinyu Zhang, Zishuo Wang, Runji Cai, Tomohito Kawabata, Qianyi Li, Xuance Peng, Tianze Yu, Zhen Xiong, Xuesu Xiao, Ling Xiao]
year: 2026
venue: arXiv:2512.22867v2 [cs.CV], 3 Jul 2026
volume: NA
issue: NA
pages: '10'
doi: Not found / not applicable
url: https://arxiv.org/abs/2512.22867
pub_status: preprint
peer_reviewed: 'No'
peer_review_basis: 'Publication status: Preprint; Peer reviewed: No verified peer-reviewed version found as of corpus freeze date (2026-10-19). Sources: arXiv abs page (2512.22867v2); Crossref title search: no match.'
category: S6
folder: 05_Direct_VLM_SocialNav_Preprints (copy also in 06_Datasets_Benchmarks_Evaluation)
folder_category_match: Partial
category_rationale: Primary contribution is a reasoning-oriented egocentric dataset/benchmark (10,110 samples, 5-step CoT, 6 actions) with fine-tuned small-VLM baselines; offline.
paper_type: dataset; benchmark
fm_used: 'Yes'
fm_class: [VLM]
fm_models: [GPT-5.4-mini API (initial annotation), 'Benchmarked/fine-tuned: TinyLLaVA (Phi-2), NVILA, InternVL3-1B/2B/8B, Qwen2.5-VL-3B/7B, Qwen3-VL-2B/4B/8B']
fm_size: ~1B-8B (benchmarked SVLMs)
method_family: ['supervised fine-tuning (full-parameter, vision tower frozen)', chain-of-thought supervision, AI-assisted annotation + human verification]
roles: [F1, F2, F4, F11]
roles_evidence: {F11: 'GPT-5.4-mini generates preliminary five-step CoT annotations, verified/revised by nine human experts (p.4).', F1: Perception step evaluated by SBERT similarity (Table II)., F2: Prediction step forecasts pedestrian movement (p.3)., F4: Reasoning step weighs social norms and physical constraints; action from 6-class space (p.3).}
integration: I1
integration_rationale: Models output discrete high-level actions; no planner/robot integration.
evidence: E1
evidence_rationale: Offline action prediction on 2,022 test samples; collision rate is human-judged per image, not executed (p.5-8).
inputs: [RGB (single egocentric frame), system prompt]
outputs: [natural-language perception, prediction, reasoning, discrete action (6 classes), explanation]
human_repr: [language description of pedestrians with egocentric relative directions, language-predicted trajectories, static constraints]
capabilities: {C1: Partial, C2: 'No', C3: Partial, C4: 'No', C5: Partial, C6: Partial, C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: Partial, C12: Partial, C13: 'No', C14: 'No', C15: Partial, C16: 'No', C17: Partial, C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: 'No', C24: Partial, C25: 'No'}
exp:
  datasets: ['MUSON: 10,110 egocentric samples from MuSoHu (8 scenes: Street 3669, Mall 2902, Shopping Street 1275, Campus 664, Park 650, Supermarket 446, Plaza 379, Library 125)', SNEI (comparison)]
  simulators: []
  robots: []
  environment: urban indoor/outdoor public spaces (images)
  indoor_outdoor: both
  sensors: [RGB (egocentric human-collected)]
  humans: real (images)
  n_scenes: 10,110 samples
  n_trajectories: NA
  n_participants: 9 expert annotators; human evaluators for CR
  split: 8,088 train / 2,022 test (8:2)
  baselines: [10 SVLMs (see fm_models), Action-only vs CoT supervision]
  ablation: Yes (action-only vs CoT on SNEI and MUSON)
  real_robot_trials: 'No'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [streets, malls, shopping streets, campuses, parks, supermarkets, plazas, libraries; sparse to dense crowds]
metrics: [VLM | Accuracy | proportion | predicted action equals GT | p.5, VLM | Macro-F1 | 0-1 | class-balanced F1 over 6 actions | p.5-6, 'VLM | Per-action accuracy (MF, MFL, MFR, TL, TR, Stop) | proportion | accuracy per GT class | p.6', SAFETY | Collision rate (CR) | proportion | human evaluators judge whether predicted action would collide with pedestrians/walls/obstacles | p.5, 'VLM | SBERT rationale similarity (Perception, Prediction, Reasoning, Explanation) | cosine | similarity to expert annotation | p.5']
deployment: {fm_model: NA, model_size: NA, api_cloud_local: GPT-5.4-mini API for annotation, onboard_offboard: NA, gpu: 8x A100 (training), cpu: Not reported, latency: Not reported, query_frequency: NA, planner_frequency: NA, controller_frequency: NA, asynchronous: NA, caching: NA, event_triggered: NA, distillation: 'No', quantization: 'No', fallback_planner: NA, safety_shield: NA, emergency_behavior: NA, uncertainty: 'No', hallucination_mitigation: Human expert verification of AI annotations, real_time_claim_supported: NA}
repro: {code: Not reported, code_url: NA, dataset: 'Yes', dataset_url: 'https://github.com/MUSON-dataset/MUSON/releases/tag/v1.0', checkpoints: Not reported, prompts_published: No (described), hardware_specified: Yes (training), hyperparameters: 'Yes (AdamW, lr 2e-5, cosine, warm-up 0.03, 448x448, batch 32, 10 epochs)', protocol_described: 'Yes', project_page: NA, concerns: 'CR is subjective human judgement; small test counts for rare actions (TL ~8, TR ~16, Stop ~80 inferred from accuracy granularity).'}
limitations_flags: [intention-ambiguity, dataset-bias, low-level-grounding]
web_verification_required: [Dataset release contents.]
cited_missing: [JRDB, RxR, VLN-CE, Inner Monologue, ReAct, ChatGPT for robotics (Vemprala), MobileVLM, MoE-LLaVA, InternVL3, Qwen3-VL]
dataset: {kind: dataset/benchmark, real_synthetic: real, size: '10,110 samples', environments: '8 urban scene types, indoor/outdoor', sensors: 'RGB (egocentric, from MuSoHu human-worn sensors)', ego_view: 'Yes', rgb: 'Yes', rgbd: No (not used), lidar: No (not used), human_trajectories: No (language prediction only), dynamic_humans: Yes (images), group_ann: 'No', intention_ann: Partial (language prediction), activity_ann: Partial (perception text), language_ann: Yes (5-step CoT), social_rule_ann: Partial (reasoning text), preference_ann: 'No', multi_action_ann: No (single action per sample), personal_space_ann: 'No', site_diversity: 8 scene categories (source MuSoHu), closed_loop: 'No', vlm_suitability: High, real_robot_compat: No (offline), standard_metrics: 'Accuracy, Macro-F1, per-action accuracy, CR (human-judged), SBERT', known_limitations: Single-frame; discrete 6 actions; human-collected ego views (not robot); long-tailed actions}
coding: {latency_reported: 'No', safety_mechanism: NA, uncertainty_treatment: 'No', hallucination_treatment: Partial, code_released: 'No', new_dataset_released: 'Yes', real_robot: 'No', human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2026
  authors: *id001
  venue: arXiv:2512.22867v2 [cs.CV], 3 Jul 2026
  volume: NA
  issue: NA
  pages: '10'
  doi: Not reported
  url: https://github.com/MUSON-dataset/MUSON/releases/tag/v1.0
  pub_status: preprint; benchmark/dataset
  peer_reviewed: 'No'
  peer_review_basis: arXiv v2, no venue statement.
project_url: https://github.com/MUSON-dataset/MUSON/releases/tag/v1.0
external_verification:
  verified_on: '2026-10-19'
  status_class: 'C: preprint only'
  verified_venue: arXiv:2512.22867v2 [cs.CV], 3 Jul 2026
  verified_doi: Not found / not applicable
  verified_url: https://arxiv.org/abs/2512.22867
  verified_pages: NA
  arxiv: 2512.22867v2
  version_relationship: arXiv only; dataset on Hugging Face (MARSLab/MUSON)
  sources: [arXiv abs page (2512.22867v2), 'Crossref title search: no match']
  peer_reviewed_note: No verified peer-reviewed version found as of corpus freeze date
  publication_status: Preprint
snei_usage: {reported_quantity: '810', unit: five-turn conversations, what_it_represents: Size attributed to SNEI ("SNEI contains only 810 five-turn conversations"), page: p.4, remark: 'Matches the Hugging Face default config row count (810); not the 1,961 images / 2K scenarios of Social-LLaVA', provenance_note: SNEI provenance (SCAND vs SCAND+MuSoHu) UNRESOLVED; see SNEI_DATASET_RECONCILIATION.md}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A2, A5]
  C_capabilities: {SAF1: Partial, SAF2: 'No', SPA1: Partial, SPA2: 'No', SPA3: Partial, SPA4: Partial, HUM1: Partial, HUM2: 'No', NOR1: Partial, NOR2: 'No', NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'Yes', EV2_closed_loop_sim: 'No', EV3_physical_robot: none, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "05_Direct_VLM_SocialNav_Preprints"
analytical_category: "S6"
coding:
  latency_reported: "No"
  safety_mechanism: "NA"
  uncertainty_treatment: "No"
  hallucination_treatment: "Partial"
  code_released: "No"
  new_dataset_released: "Yes"
  real_robot: "No"
  human_subject_study: "No"
---

# MUSON (Liu et al., arXiv v2 2026)

Page convention: PDF index (p.N).

## A. Bibliographic — arXiv:2512.22867v2 (3 Jul 2026); Hokkaido Univ. + GMU; includes R. Cai (competing-survey first author). Dataset https://github.com/MUSON-dataset/MUSON/releases/tag/v1.0. Copy in 06 (identical). Preprint.

## B. Position — S6 (dataset/benchmark). Reasoning-oriented egocentric VQA/action dataset; complements SNEI and SocialNav-SUB.

## C. Research problem — untuned VLMs struggle with fine-grained social norms; no large-scale egocentric reasoning dataset (abstract). Contributions: dataset (10,110 samples, 5-step CoT); 6-action design; benchmark of 10 SVLMs (p.1–2).

## D. Method — source MuSoHu; local single-frame decisions; egocentric relative directions; 6 actions; GPT-5.4-mini preliminary annotation → 9 experts revise → consistency check (p.3–4). Fine-tuning: full-parameter SFT (vision tower frozen), 8× A100, 8:2 split (p.6).

## L. Quantitative results (Table II, p.8; Acc / Macro-F1 / MF / MFL / MFR / TL / TR / Stop / CR)
TinyLLaVA 0.5579/0.2652/0.7590/0.3012/0.3616/0.0000/0.0000/0.1500/0.0885; NVILA 0.2681/0.1617/0.0351/0.4938/0.6818/0/0/0.1750/0.3362; InternVL3-1B 0.5356/0.2526/0.7428/0.1988/0.3657/0/0/0.2000/0.1015; InternVL3-2B 0.5450/0.2792/0.7077/0.3137/0.4153/0/0.0625/0.1500/0.0955; InternVL3-8B 0.5776/0.2766/0.7725/0.2826/0.4277/0/0/0.1375/0.0891; Qwen2.5-VL-3B 0.6627/0.5980/0.6987/0.5932/0.6343/0.5000/0.4375/0.6750/0.0759; Qwen2.5-VL-7B 0.7520/0.6695/0.7815/0.6956/0.7438/0.7500/0.6875/0.6375/0.0645; Qwen3-VL-2B 0.6899/0.6370/0.6879/0.6832/0.7190/0.8750/0.4375/0.6000/0.0648; Qwen3-VL-4B 0.7483/0.6764/0.8076/0.6584/0.7273/0.2500/0.6250/0.4875/0.0623; Qwen3-VL-8B 0.7765/0.7490/0.8507/0.7050/0.6839/0.7500/0.6250/0.6250/0.0609.
Rationale SBERT (Perception / Prediction / Reasoning / Explanation): TinyLLaVA 0.8042/0.7722/0.7346/0.7612; NVILA 0.8124/0.7839/0.7321/0.7367; InternVL3-1B 0.8152/0.7890/0.7361/0.7651; InternVL3-2B 0.8172/0.7918/0.7392/0.7682; InternVL3-8B 0.8204/0.7993/0.7498/0.7720; Qwen2.5-VL-3B 0.7450/0.5980/0.5360/0.5960; Qwen2.5-VL-7B 0.8023/0.8051/0.7029/0.7657; Qwen3-VL-2B 0.7400/0.7070/0.7080/0.7140; Qwen3-VL-4B 0.8087/0.7469/0.6794/0.7364; Qwen3-VL-8B 0.8191/0.8160/0.7127/0.7783.
Table III (Qwen3-VL-2B accuracy; SNEI / MUSON): Action only 0.6235/0.5499; With CoT 0.5741/0.6899.
Action distribution (Table I): MF 5508 (54.48%), MFR 2300 (22.75%), MFL 1564 (15.47%), Stop 555 (5.49%), TR 107 (1.06%), TL 76 (0.75%).
- Observation: rationale similarity (SBERT ~0.7–0.8) is high even for models with near-zero accuracy on rare actions (e.g., NVILA) — text similarity decoupled from decision quality.

## N. Limitations
1. **Stated (p.9):** annotation granularity/supervision design to refine; six-action space may be refined for ambiguous decisions.
2. **Future:** RL and continual adaptation; benchmark-driven optimisation.
3. **Observable:** CR is a human judgement, not a physical collision; single-frame; rare-class test counts small; SNEI described as "810 five-turn conversations" (vs 325 in E-SocialNav/JSAI and 2K scenarios in Social-LLaVA).

## P. Dataset analysis — see `dataset:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: C: preprint only; venue arXiv:2512.22867v2 [cs.CV], 3 Jul 2026; DOI Not found / not applicable; pages NA; URL https://arxiv.org/abs/2512.22867.
- Sources: arXiv abs page (2512.22867v2); Crossref title search: no match.
- Version relationship: arXiv only; dataset on Hugging Face (MARSLab/MUSON).
- Changed field - doi: PDF-derived 'Not reported' -> externally verified 'Not found / not applicable'
- Changed field - url: PDF-derived 'https://github.com/MUSON-dataset/MUSON/releases/tag/v1.0' -> externally verified 'https://arxiv.org/abs/2512.22867'
- Changed field - pub_status: PDF-derived 'preprint; benchmark/dataset' -> externally verified 'preprint'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

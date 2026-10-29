---
id: 2026_Xiao_E-SocialNav
source_pdfs: [04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/E-Socialnav_Efficient_Socially_Compliant_Navigation_with_Language_Models.pdf]
duplicate_copies: []
related_versions: []
title: 'E-SocialNav: Efficient Socially Compliant Navigation with Language Models'
authors: &id001 [Ling Xiao, Daeun Song, Xuesu Xiao, Toshihiko Yamasaki]
year: 2026
venue: ICASSP 2026 - IEEE International Conference on Acoustics, Speech and Signal Processing
volume: NA
issue: NA
pages: 20077-20081
doi: 10.1109/ICASSP55912.2026.11462076
url: https://doi.org/10.1109/ICASSP55912.2026.11462076
pub_status: conference
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1109/ICASSP55912.2026.11462076); arXiv abs page (2603.20664v1). PDF-derived basis (Stage 1): IEEE ICASSP 2026 proceedings header with DOI (p.1).'
category: S4
folder: 04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core
folder_category_match: 'Yes'
category_rationale: Small VLM (SigLIP + Phi-2 2.7B) trained with SFT+DPO to produce socially compliant navigation descriptions and actions; offline evaluation on SNEI-derived data.
paper_type: method
fm_used: 'Yes'
fm_class: [VLM]
fm_models: [SigLIP + Phi-2-2.7B (E-SocialNav), 'variants: CLIP, DINO vision towers; TinyLlama-1.1B, StableLM-2-Zephyr-1.6B', 'baselines: Claude, GPT-4o (zero-shot), Social-LLaVA']
fm_size: 2.7B LM
method_family: [supervised fine-tuning (projector only), direct preference optimization (LoRA), multi-turn VQA]
roles: [F1, F2, F4]
roles_evidence: {F1: 'Perception turn (''What do you perceive from the image?'') (Fig.3).', F2: 'Prediction turn (''What do you predict these humans will do next?'') (Fig.3).', F4: 'Action turn (''What should the robot do?'') trained toward human-annotated socially compliant answers; DPO rejects modified (wrong) answers (p.2-3).'}
integration: I1
integration_rationale: Outputs language action recommendations evaluated against annotations; no planner or robot integration.
evidence: E1
evidence_rationale: Offline semantic-similarity and action-accuracy evaluation on 60 test samples; no simulation or robot (p.3-4).
inputs: [RGB (single image), natural language instruction]
outputs: [natural-language perception, prediction, natural-language action]
human_repr: [semantic description (language), language-predicted motion]
capabilities: {C1: 'No', C2: 'No', C3: 'No', C4: 'No', C5: Partial, C6: Partial, C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: Partial, C12: Partial, C13: 'No', C14: 'No', C15: Partial, C16: 'No', C17: 'No', C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: 'No', C24: Partial, C25: 'No'}
exp:
  datasets: ['325-sample multi-dialog dataset derived from SNEI (SCAND + MuSoHu), five-turn conversations; DPO pairs derived']
  simulators: []
  robots: []
  environment: SCAND/MuSoHu public spaces (images)
  indoor_outdoor: both
  sensors: [RGB]
  humans: real (images)
  n_scenes: 325 samples
  n_trajectories: NA
  n_participants: NA
  split: 265 train / 60 test (random)
  baselines: [Claude (zero-shot), GPT-4o (zero-shot), Social-LLaVA]
  ablation: Yes (trainable components; VT and SLM choices)
  real_robot_trials: 'No'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [sidewalk, crowd (images)]
metrics: [VLM | BERTScore-P / -R / -F1 | score | semantic similarity to human annotation | p.3-4, VLM | SBERT-cos | cosine | sentence-embedding similarity | p.4, VLM | Sentence Mover's Similarity (SMS) | score | semantic similarity | p.4, VLM | Action Accuracy (AA) | proportion | predicted action exactly matches GT action | p.4, DEPLOY | FPS | frames/s | inference speed (hardware not specified) | p.3]
deployment: {fm_model: SigLIP + Phi-2-2.7B, model_size: 2.7B, api_cloud_local: Local, onboard_offboard: Not reported, gpu: '4x A100 (training, <1 h)', cpu: Not reported, latency: 2.354 FPS (inference hardware not reported), query_frequency: NA, planner_frequency: NA, controller_frequency: NA, asynchronous: NA, caching: NA, event_triggered: NA, distillation: 'No', quantization: 'No', fallback_planner: NA, safety_shield: NA, emergency_behavior: NA, uncertainty: 'No', hallucination_mitigation: DPO with fact-modified rejected answers (implicit), real_time_claim_supported: No measurement on robot; efficiency claim only}
repro: {code: Yes (stated), code_url: 'https://github.com/Dr-LingXiao/ESocialNav', dataset: Derived from SNEI (release not stated), dataset_url: NA, checkpoints: Not reported, prompts_published: Partial (dialog questions in Fig.3), hardware_specified: Partial (training), hyperparameters: Yes (20 epochs SFT lr 5e-5 warm-up 0.03; DPO 5 epochs; beta 0.1), protocol_described: 'Yes', project_page: Not reported, concerns: 60-sample test set; FPS hardware unspecified.}
limitations_flags: [dataset-bias, no-human-study, low-level-grounding, cultural-bias]
web_verification_required: [Verify code repository availability.]
cited_missing: [Gesture2Path (ICSR 2024), 'LLM-Advisor (arXiv:2503.01236)', Kathuria 2025 deep IRL, TinyLLaVA, Phi-2]
coding: {latency_reported: 'Yes', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: Partial, code_released: 'Yes', new_dataset_released: 'No', real_robot: 'No', human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2026
  authors: *id001
  venue: ICASSP 2026 - IEEE International Conference on Acoustics, Speech and Signal Processing
  volume: Not reported
  issue: Not reported
  pages: 20077-20081
  doi: 10.1109/ICASSP55912.2026.11462076
  url: https://github.com/Dr-LingXiao/ESocialNav
  pub_status: conference
  peer_reviewed: 'Yes'
  peer_review_basis: IEEE ICASSP 2026 proceedings header with DOI (p.1).
project_url: https://github.com/Dr-LingXiao/ESocialNav
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: ICASSP 2026 - IEEE International Conference on Acoustics, Speech and Signal Processing
  verified_doi: 10.1109/ICASSP55912.2026.11462076
  verified_url: https://doi.org/10.1109/ICASSP55912.2026.11462076
  verified_pages: 20077-20081
  arxiv: 2603.20664v1
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1109/ICASSP55912.2026.11462076)', arXiv abs page (2603.20664v1)]
snei_usage: {reported_quantity: 325 (265 train / 60 test), unit: 'egocentric video-derived samples, each with five-turn conversations', what_it_represents: Subset constructed by the authors from SNEI, page: p.4, remark: 'States SNEI "is derived from SCAND [9] and MuSoHu [10]" (conflicts with Social-LLaVA)', provenance_note: SNEI provenance (SCAND vs SCAND+MuSoHu) UNRESOLVED; see SNEI_DATASET_RECONCILIATION.md}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A5]
  C_capabilities: {SAF1: 'No', SAF2: 'No', SPA1: 'No', SPA2: 'No', SPA3: Partial, SPA4: 'No', HUM1: Partial, HUM2: 'No', NOR1: Partial, NOR2: 'No', NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: [R1, R2, R3]
  D_interface: [D0]
  E_evidence_profile: {EV1_offline: 'Yes', EV2_closed_loop_sim: 'No', EV3_physical_robot: none, EV4_real_humans_in_trials: none, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: NA, statistical_testing: 'No', cross_environment: 'Yes', runtime_measured: 'Yes'}
  cross_cutting: {temporal_coupling: offline, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'No', uncertainty: 'No', hallucination_mitigation: Partial, privacy_constraint: 'No', inference_location: n/a (offline evaluation only)}
physical_source_folder: "04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core"
analytical_category: "S4"
coding:
  latency_reported: "Yes"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "Partial"
  code_released: "Yes"
  new_dataset_released: "No"
  real_robot: "No"
  human_subject_study: "No"
---

# E-SocialNav (Xiao, Song, Xiao, Yamasaki — ICASSP 2026)

Page convention: PDF index (p.N); printed pp.20077–20081.

## A. Bibliographic
ICASSP 2026, pp.20077–20081, DOI 10.1109/ICASSP55912.2026.11462076; code https://github.com/Dr-LingXiao/ESocialNav. Conference; peer-reviewed.

## B. Position — S4
Efficiency-oriented small VLM for socially compliant navigation reasoning; also the first systematic zero-shot evaluation of GPT-4o and Claude claimed by authors (p.1). Offline only.

## C. Research problem
- **Problem:** large LMs slow/energy-hungry; no systematic zero-shot evaluation of LLMs for socially aware navigation; little data (p.1).
- **Contributions (p.1):** evaluate GPT-4o and Claude; E-SocialNav for small-data settings; multi-dialog SFT dataset and single-dialog DPO dataset; identify suitable SLMs and vision towers.
- Note: authors state VLM-Social-Nav's GPT-4V has "inability to leverage GPU acceleration" (p.1) — characterisation, not measured here.

## D. Technical method
Vision tower (SigLIP) → 2-layer MLP projector → Phi-2-2.7B. Stage I SFT on multi-turn dialogues updates projector only (20 epochs, lr 5e-5, warm-up 0.03, FlashAttention-2). Stage II DPO updates LoRA only (5 epochs, β = 0.1); chosen = human annotation, rejected = annotation with localized factual modification (Fig.2). Trained on 4× A100 in <1 h (p.4).

## E. Human/social representation — language only.

## F. Roles — F1, F2, F4.

## G. Social capabilities (OFFLINE) — C5, C6 Partial (perception/prediction turns); C11, C12, C15, C24 Partial (sidewalk/stop-and-wait actions); rest No.

## H. Integration — I1. ## I. Evidence — E1.

## J. Experimental evidence
325 SNEI-derived samples (five-turn dialogues); 265 train / 60 test (random) (p.4). Baselines Claude, GPT-4o (GPT-4V deprecated), Social-LLaVA. Ablations over trainable components and VT/SLM combinations.

## K. Metrics — BERTScore-P/R/F1, SBERT-cos, SMS, AA, FPS.

## L. Quantitative results (Table 1, p.3, visually verified)
| Model | VT | LM | BS-P | BS-R | BS-F1 | SBERT | SMS | FPS | AA |
|---|---|---|---|---|---|---|---|---|---|
| Claude | – | – | −0.233 | 0.387 | 0.059 | 0.664 | 0.641 | 0.087 | 0.417 |
| GPT-4o | – | – | 0.076 | 0.443 | 0.254 | 0.672 | 0.651 | 0.212 | 0.450 |
| Social-LLaVA | CLIP ViT-L/14 | Vicuna-7B | 0.672 | 0.653 | 0.641 | 0.784 | 0.813 | 1.113 | 0.483 |
| SFT(proj+lora+vision) | SigLIP | Phi-2-2.7B | 0.585 | 0.434 | 0.509 | 0.744 | 0.802 | 0.978 | 0.383 |
| SFT(proj+lora) | SigLIP | Phi-2-2.7B | 0.640 | 0.545 | 0.592 | 0.756 | 0.813 | 1.553 | 0.400 |
| SFT(proj) | SigLIP | Phi-2-2.7B | 0.551 | 0.658 | 0.604 | 0.780 | 0.828 | 1.828 | 0.433 |
| SFT(proj)+DPO(lora) | SigLIP | Phi-2-2.7B | 0.706 | 0.671 | 0.688 | 0.814 | 0.846 | 2.354 | 0.550 |
Table 2 (VT/SLM; BS-P/R/F1/SBERT/SMS): CLIP+Phi-2 0.555/0.658/0.605/0.803/0.768; DINO+Phi-2 0.692/0.663/0.677/0.801/0.833; SigLIP+TinyLlama-1.1B 0.473/0.576/0.523/0.733/0.789; SigLIP+StableLM-2-Zephyr-1.6B 0.700/0.622/0.661/0.788/0.837; SigLIP+Phi-2 0.706/0.671/0.688/0.814/0.846.
- Observation: FPS differences between SFT variants with identical architecture (0.978 vs 2.354) are unexplained in the text.

## M. Deployment — 2.354 FPS (hardware unspecified); no robot.

## N. Limitations
1. **Stated (p.4):** failure cases reflect conservative bias in human annotation; difficulty of a universally valid social standard.
2. **Future work:** subjective user studies; fine-grained large-scale benchmark covering diverse cultural norms and contexts.
3. **Observable:** 60-sample test; single-image; no navigation; text-similarity metrics may not reflect action correctness; FPS hardware unknown.
4. Deferred.

## O. Reproducibility — code URL given; hyperparameters given.

## P. Direct-paper questions
1 Efficient generation of socially compliant navigation descriptions/actions. 2 Contextual/commonsense reasoning. 3 SigLIP+Phi-2-2.7B. 4 Single RGB image. 5 Multi-turn questions (perceive/predict/what should robot do). 6 Language. 7 Not converted. 8 No. 9–10 None. 11 Socially compliant, efficient. 12 Text similarity and action accuracy. 13 Language-level. 14 No. 15 No. 16 No. 17 Implicit. 18 No. 19 No. 20 No. 21 2.354 FPS model-only. 22 No. 23 No. 24 No. 25 None for navigation. 26 Nothing about robot behaviour.

## Q. Cited works possibly missing — Gesture2Path (ICSR 2024); LLM-Advisor; Kathuria 2025.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue ICASSP 2026 - IEEE International Conference on Acoustics, Speech and Signal Processing; DOI 10.1109/ICASSP55912.2026.11462076; pages 20077-20081; URL https://doi.org/10.1109/ICASSP55912.2026.11462076.
- Sources: Crossref (exact title match, DOI 10.1109/ICASSP55912.2026.11462076); arXiv abs page (2603.20664v1).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - volume: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - issue: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - url: PDF-derived 'https://github.com/Dr-LingXiao/ESocialNav' -> externally verified 'https://doi.org/10.1109/ICASSP55912.2026.11462076'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

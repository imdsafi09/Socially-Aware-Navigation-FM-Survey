---
id: 2026_Xiao_Prompting-VLMs-JSAI
source_pdfs: [04_Direct_VLM_SocialNav/B_Peer_Reviewed_Boundary/JSAI2026_2E5GS10o01.pdf]
duplicate_copies: []
related_versions: ['Possibly related: ''Probing prompt design for socially compliant robot navigation with vision language models'' arXiv:2601.14622 (cited by Cai 2026 [80]); not in corpus - WEB_VERIFICATION_REQUIRED']
title: Prompting Vision-Language Models for Socially Compliant Robot Navigation
authors: &id001 [Ling Xiao, Toshihiko Yamasaki]
year: 2026
venue: Proceedings of the Annual Conference of JSAI, JSAI2026 (40th Annual Conference of the Japanese Society for Artificial Intelligence)
volume: JSAI2026
issue: '0'
pages: 2E5GS10o01 (4 pp.)
doi: 10.11517/pjsai.JSAI2026.0_2E5GS10o01
url: https://doi.org/10.11517/pjsai.JSAI2026.0_2E5GS10o01
pub_status: conference paper (acceptance verified)
peer_reviewed: Not established
peer_review_basis: 'Externally verified (2026-10-19): J-STAGE record (DOI 10.11517/pjsai.JSAI2026.0_2E5GS10o01; published online 2026/07/17; Japanese title on record); JSAI 2026 call for papers: acceptance decided by the programme committee (no peer-review statement).'
category: S5
folder: 04_Direct_VLM_SocialNav/B_Peer_Reviewed_Boundary
folder_category_match: Partial
category_rationale: 'Direct social-navigation VLM prompting study (offline, SNEI). Placed in S5 because peer-review status is unclear (rule: S4 = peer-reviewed direct; S5 = preprint/unclear direct).'
paper_type: method
fm_used: 'Yes'
fm_class: [VLM]
fm_models: ['TinyLLaVA framework with SigLIP (frozen) + Phi(-2), StableLM(-2-1.6B), TinyLlama(-1.1B) language models (fully fine-tuned)']
fm_size: 1.1B-2.7B LMs
method_family: [supervised fine-tuning, prompt engineering (system guidance x motivational framing)]
roles: [F1, F2, F4]
roles_evidence: {F1: Perception turn (Q1) evaluated (Table 1)., F2: Prediction turn (Q2) evaluated., F4: 'Reasoning turn (Q3) and action selection; base prompt ''understand human behaviors, infer intentions, plan safe, smooth, socially appropriate paths'' (p.2).'}
integration: I1
integration_rationale: Outputs natural-language actions evaluated for action accuracy; no robot/planner integration.
evidence: E1
evidence_rationale: Offline evaluation on 60 SNEI test images (action accuracy and semantic similarity) (p.2-3).
inputs: [RGB (single image), natural language system prompt and questions]
outputs: [natural-language perception, prediction, reasoning, action]
human_repr: [semantic description (language)]
capabilities: {C1: 'No', C2: 'No', C3: 'No', C4: 'No', C5: Partial, C6: Partial, C7: Partial, C8: 'No', C9: 'No', C10: 'No', C11: Partial, C12: Partial, C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: 'No', C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: 'No', C24: Partial, C25: 'No'}
exp:
  datasets: ['SNEI subset: 325 egocentric images (265 train / 60 test), five-turn conversations']
  simulators: []
  robots: []
  environment: indoor and outdoor (dataset)
  indoor_outdoor: both
  sensors: [RGB]
  humans: real (images)
  n_scenes: 325 images
  n_trajectories: NA
  n_participants: NA
  split: 265/60
  baselines: [No system prompt (fine-tuned), Raw (shared base prompt only)]
  ablation: Yes (9 prompt variants x 3 LMs)
  real_robot_trials: 'No'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [hallway, open area, groups (images)]
metrics: [VLM | Action Accuracy (AA) | proportion | predicted action label equals GT action label | p.2, 'VLM | BERT-F1 | score | token-level semantic similarity (Q1 perception, Q2 prediction, Q3 reasoning) | p.2', VLM | SBERT | cosine | sentence-level semantic similarity per question | p.2]
deployment: {fm_model: TinyLLaVA (Phi/StableLM/TinyLlama), model_size: 1.1-2.7B, api_cloud_local: Local, onboard_offboard: NA, gpu: 4 NVIDIA GPUs (training; model not specified), cpu: Not reported, latency: Not reported, query_frequency: NA, planner_frequency: NA, controller_frequency: NA, asynchronous: NA, caching: NA, event_triggered: NA, distillation: 'No', quantization: No (FP16), fallback_planner: NA, safety_shield: NA, emergency_behavior: NA, uncertainty: 'No', hallucination_mitigation: 'No', real_time_claim_supported: NA}
repro: {code: Not reported, code_url: NA, dataset: SNEI (public per Social-LLaVA), dataset_url: NA, checkpoints: NA, prompts_published: 'Yes (prompt catalog, p.2)', hardware_specified: Partial, hyperparameters: 'Yes (5 epochs, batch 32, AdamW lr 2e-5, cosine, 3% warm-up)', protocol_described: 'Yes', project_page: NA, concerns: 60-sample test set; no variance or repeated runs.}
limitations_flags: [prompt-sensitivity, dataset-bias, limited-scenarios]
web_verification_required: ['JSAI review process; relation to arXiv:2601.14622.']
cited_missing: [Gesture2Path, Kathuria 2025 deep IRL, DiMenichi & Tricomi 2015 competition]
coding: {latency_reported: 'No', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: 'No', code_released: 'No', new_dataset_released: NA, real_robot: 'No', human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2026
  authors: *id001
  venue: The 40th Annual Conference of the Japanese Society for Artificial Intelligence (JSAI 2026), paper 2E5-GS-10o-01
  volume: Not reported
  issue: Not reported
  pages: '4'
  doi: Not reported
  url: Not reported
  pub_status: proceedings (national conference)
  peer_reviewed: Unclear
  peer_review_basis: JSAI annual conference paper (4 pages); PDF contains no review/acceptance statement. Review process of JSAI general sessions not verifiable from PDF.
external_verification:
  verified_on: '2026-10-19'
  status_class: 'D: conference paper; acceptance verified, peer review not established'
  verified_venue: Proceedings of the Annual Conference of JSAI, JSAI2026 (40th Annual Conference of the Japanese Society for Artificial Intelligence)
  verified_doi: 10.11517/pjsai.JSAI2026.0_2E5GS10o01
  verified_url: https://doi.org/10.11517/pjsai.JSAI2026.0_2E5GS10o01
  verified_pages: 2E5GS10o01 (4 pp.)
  arxiv: NA (related version arXiv 2601.14622 "Probing Prompt Design ...")
  version_relationship: Corpus copy is the JSAI proceedings PDF; arXiv 2601.14622 is a related, differently titled version
  sources: [J-STAGE record (DOI 10.11517/pjsai.JSAI2026.0_2E5GS10o01; published online 2026/07/17; Japanese title on record), 'JSAI 2026 call for papers: acceptance decided by the programme committee (no peer-review statement)']
  peer_review_note: Conference acceptance verified; peer-review status not independently established
snei_usage: {reported_quantity: 325 (265 train / 60 test), unit: egocentric images with five-turn conversational annotations, what_it_represents: Described as the SNEI dataset (not as a subset), page: p.2, remark: Same 325 split as E-SocialNav, provenance_note: SNEI provenance (SCAND vs SCAND+MuSoHu) UNRESOLVED; see SNEI_DATASET_RECONCILIATION.md}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A5]
  C_capabilities: {SAF1: 'No', SAF2: 'No', SPA1: 'No', SPA2: 'No', SPA3: Partial, SPA4: 'No', HUM1: Partial, HUM2: Partial, NOR1: Partial, NOR2: 'No', NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: [R1, R2, R3]
  D_interface: [D0]
  E_evidence_profile: {EV1_offline: 'Yes', EV2_closed_loop_sim: 'No', EV3_physical_robot: none, EV4_real_humans_in_trials: none, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: NA, statistical_testing: 'No', cross_environment: 'Yes', runtime_measured: 'No'}
  cross_cutting: {temporal_coupling: offline, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'No', uncertainty: 'No', hallucination_mitigation: 'No', privacy_constraint: 'No', inference_location: n/a (offline evaluation only)}
physical_source_folder: "04_Direct_VLM_SocialNav/B_Peer_Reviewed_Boundary"
analytical_category: "S5"
coding:
  latency_reported: "No"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "No"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "No"
  human_subject_study: "No"
---

# Prompting VLMs for Socially Compliant Robot Navigation (Xiao & Yamasaki, JSAI 2026)

Page convention: PDF index (p.N); 4 pages.

## A. Bibliographic
JSAI 2026 (40th Annual Conference), paper 2E5-GS-10o-01; Hokkaido Univ. & Univ. of Tokyo. Peer-reviewed: **Unclear**. Possibly the short version of arXiv:2601.14622 cited by Cai et al. (not in corpus).

## B. Position — S5 (direct, peer review unclear)
Prompt-design study for fine-tuned small VLMs on SNEI; offline; demonstrates **prompt sensitivity** quantitatively.

## C. Research problem
- **Problem:** principled prompt design for socially compliant behaviour is under-explored, esp. for small VLMs (abstract).
- **Two dimensions:** system guidance (action-only A, reasoning R, perception+reasoning PR) × motivational framing (vs humans / other AI / past self) (p.1–2).
- **Hypothesis:** PR prompts align representations with action selection; competitive framing increases decision confidence (p.2).
- **Findings (authors):** competition against past self best for fine-tuned small VLMs; inappropriate system prompts can degrade performance below direct fine-tuning; prompts mainly improve action accuracy rather than semantic metrics.

## D. Technical method
TinyLLaVA: SigLIP vision tower frozen; projector trained; LM fully fine-tuned (Phi, StableLM, TinyLlama); DeepSpeed ZeRO-3, 4 GPUs, FlashAttention-2, FP16, 5 epochs, batch 32, AdamW lr 2e-5, cosine, 3% warm-up (p.2). Shared base prompt + 9 additional instructions (A1–A3, R1–R3, PR1–PR3) (p.2).

## E–H. Language-only human representation; roles F1, F2, F4; integration I1.

## I. Evidence — E1.

## J. Experimental evidence — SNEI 325 images (265/60), five-turn conversations, two robot platforms, indoor/outdoor (p.2).

## K. Metrics — AA, BERT-F1, SBERT per Q1–Q3.

## L. Quantitative results (Table 1, p.3, visually verified; AA shown — full table has BERT-F1/SBERT for Q1–Q3)
- Phi: No prompt 0.450; Raw 0.433; A1 0.267; A2 0.267; A3 0.317; R1 0.300; R2 0.267; R3 0.350; PR1 0.383; PR2 0.317; PR3 **0.500**.
- StableLM: No 0.483; Raw 0.467; A1 0.450; A2 0.367; A3 0.467; R1 0.333; R2 0.317; R3 0.417; PR1 0.317; PR2 0.333; PR3 **0.517**.
- TinyLlama: No 0.417; Raw 0.433; A1 0.383; A2 0.383; A3 0.450; R1 0.467; R2 0.333; R3 0.483; PR1 0.433; PR2 0.317; PR3 **0.500**.
- Selected semantic values (Phi PR3): Q1 BERT-F1 0.376 / SBERT 0.668; Q2 0.500 / 0.630; Q3 0.402 / 0.734. Phi No-prompt: Q1 0.349/0.504; Q2 0.386/0.590; Q3 0.324/0.707.
- Observation: 8 of 9 prompt variants for Phi score below the no-prompt baseline in AA (only PR3 exceeds it) — evidence of strong prompt sensitivity on a 60-sample test set.

## M. Deployment — not addressed.

## N. Limitations
1. **Stated (p.3):** dataset may not cover complex conditions (weather, night, traffic signals); static text prompts only, no adaptive/learned prompting.
2. **Future work:** larger diverse datasets; online adaptation and RL.
3. **Observable:** n_test = 60 → one sample = 1.67 percentage points of AA; no repeated runs/variance; no statistical tests.
4. Deferred.

## O. Reproducibility — prompts and hyperparameters published; code not stated.

## P. Direct-paper questions (abridged)
1 Prompt design for VLM social-navigation decisions. 3 TinyLLaVA small VLMs. 4 Single image. 5 System prompt catalog. 6 Language action. 7–10 None (offline). 12 AA and text similarity. 18 No. 19 No. 20 No. 21–24 NA/No. 25 None for navigation. 26 Cannot conclude closed-loop benefit; differences may be within sampling noise.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: D: conference paper; acceptance verified, peer review not established; venue Proceedings of the Annual Conference of JSAI, JSAI2026 (40th Annual Conference of the Japanese Society for Artificial Intelligence); DOI 10.11517/pjsai.JSAI2026.0_2E5GS10o01; pages 2E5GS10o01 (4 pp.); URL https://doi.org/10.11517/pjsai.JSAI2026.0_2E5GS10o01.
- Sources: J-STAGE record (DOI 10.11517/pjsai.JSAI2026.0_2E5GS10o01; published online 2026/07/17; Japanese title on record); JSAI 2026 call for papers: acceptance decided by the programme committee (no peer-review statement).
- Version relationship: Corpus copy is the JSAI proceedings PDF; arXiv 2601.14622 is a related, differently titled version.
- Changed field - venue: PDF-derived 'The 40th Annual Conference of the Japanese Society for Artificial Intelligence (JSAI 2026), paper 2E5-GS-10o-01' -> externally verified 'Proceedings of the Annual Conference of JSAI, JSAI2026 (40th Annual Conference of the Japanese Society for Artificial Intelligence)'
- Changed field - volume: PDF-derived 'Not reported' -> externally verified 'JSAI2026'
- Changed field - issue: PDF-derived 'Not reported' -> externally verified '0'
- Changed field - pages: PDF-derived '4' -> externally verified '2E5GS10o01 (4 pp.)'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified '10.11517/pjsai.JSAI2026.0_2E5GS10o01'
- Changed field - url: PDF-derived 'Not reported' -> externally verified 'https://doi.org/10.11517/pjsai.JSAI2026.0_2E5GS10o01'
- Changed field - pub_status: PDF-derived 'proceedings (national conference)' -> externally verified 'conference paper (acceptance verified)'
- Changed field - peer_reviewed: PDF-derived 'Unclear' -> externally verified 'Not established'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

## Stage-7 status re-check (2026-10-19)
DOI resolves; JSAI 2026 programme lists an acceptance notification (18 Mar 2026) but official pages do not state the review type. Status unchanged: class D, peer review not independently established. See 09_Project_Reports/PUBLICATION_STATUS_FINAL_CHECK.md.

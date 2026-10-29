---
id: 2023_Driess_PaLM-E
source_pdfs: [03_Adjacent_Foundation_Model_Navigation/driess23a.pdf]
duplicate_copies: []
related_versions: []
title: 'PaLM-E: An Embodied Multimodal Language Model'
authors: &id001 [Danny Driess, Fei Xia, Mehdi S. M. Sajjadi, Corey Lynch, Aakanksha Chowdhery, Brian Ichter, Ayzaan Wahid, Jonathan Tompson, Quan Vuong, Tianhe Yu, Wenlong Huang, Yevgen Chebotar, Pierre Sermanet, Daniel Duckworth, Sergey Levine, Vincent Vanhoucke, Karol Hausman, Marc Toussaint, Klaus Greff, Andy Zeng, Igor Mordatch, Pete Florence]
year: 2023
venue: Proceedings of the 40th International Conference on Machine Learning (ICML 2023), PMLR 202
volume: NA
issue: NA
pages: 8469-8488
doi: Not found / not applicable
url: https://proceedings.mlr.press/v202/driess23a.html
pub_status: conference
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): PMLR proceedings page (https://proceedings.mlr.press/v202/driess23a.html); arXiv abs page (2303.03378v1). PDF-derived basis (Stage 1): ICML 2023 PMLR footer (p.1).'
category: S3
folder: 03_Adjacent_Foundation_Model_Navigation
folder_category_match: 'Yes'
category_rationale: Embodied multimodal LLM injecting continuous observations into PaLM for planning, VQA and captioning across manipulation and mobile-manipulation domains; no social navigation.
paper_type: model
fm_used: 'Yes'
fm_class: [VLM, LLM]
fm_models: [PaLM-E-12B (PaLM 8B + ViT-4B), PaLM-E-84B (PaLM 62B + ViT-22B), PaLM-E-562B (PaLM 540B + ViT-22B), OSRT / ViT+TokenLearner / state encoders]
fm_size: 12B-562B
method_family: [multimodal sentence encoding, end-to-end training with frozen or finetuned LLM, co-training on web VL data + robot data]
roles: [F1, F7]
roles_evidence: {F1: 'Embodied VQA, affordance prediction and failure detection from images (Tables 1, 4).', F7: 'Generates next plan step for low-level RT-1 / Language-Table policies in closed loop, including ''Go to the drawers'' navigation steps (p.7-8, Fig.4).'}
integration: I1
integration_rationale: Outputs discrete high-level skill/subgoal text executed by separate low-level policies (navigation as a named skill).
evidence: E2
evidence_rationale: Systematic closed-loop success rates only in simulation (TAMP, Language-Table, Tables 1-2); real-robot mobile manipulation and tabletop are qualitative demonstrations; affordance/failure detection are offline (Table 4).
inputs: [images (ViT tokens), state vectors, OSRT object slots, text prompt with step history]
outputs: ['text (answers, plan steps)']
human_repr: [none (human only as instruction giver / 'bring it to the user')]
capabilities: {C1: NA, C2: NA, C3: NA, C4: NA, C5: NA, C6: NA, C7: NA, C8: NA, C9: NA, C10: NA, C11: NA, C12: NA, C13: NA, C14: NA, C15: NA, C16: NA, C17: NA, C18: NA, C19: NA, C20: NA, C21: NA, C22: NA, C23: NA, C24: NA, C25: NA}
exp:
  datasets: ['TAMP (96,000 scenes; 1% = 320 examples per planning task)', Language-Table, SayCan mobile-manipulation runs (2912 sequences), 'WebLI, VQAv2, OK-VQA, COCO (full mixture; embodied data 8.9%)']
  simulators: [TAMP environment, Language-Table simulation]
  robots: [Everyday Robots mobile manipulator (kitchen), Language-Table tabletop robot]
  environment: kitchen; tabletop
  indoor_outdoor: indoor
  sensors: [RGB]
  humans: instruction giver; adversarial disturbance by human in demo
  n_scenes: Not reported
  n_trajectories: Not reported
  n_participants: NA
  split: in-distribution vs OOD object counts; OOD scenes for affordance/failure
  baselines: [SayCan (oracle affordances), PaLI zero-shot, CLIP-FT, CLIP-FT-hindsight, QT-OPT, Frozen (Tsimpoukelli)]
  ablation: Yes (encoders, pretraining, freezing, mixture, scale)
  real_robot_trials: Yes (qualitative)
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: []
metrics: [OTHER | Planning success rate | % | TAMP p1/p2; Language-Table tasks | p.7-8, VLM | Embodied VQA accuracy | % | TAMP q1-q4 | p.7, VLM | F1 score | 0-1 | failure detection / affordance prediction | p.8, 'VLM | VQAv2 / OK-VQA accuracy, COCO CIDEr | various | general VL benchmarks | p.8']
deployment: {fm_model: PaLM-E (12B-562B), model_size: 12B-562B, api_cloud_local: Not reported (Google infrastructure), onboard_offboard: Not reported, gpu: Not reported, cpu: Not reported, latency: Not reported, query_frequency: 1 Hz language subgoals (Language-Table real robot), planner_frequency: 1 Hz, controller_frequency: 5 Hz low-level policy (Lynch et al.), asynchronous: Not reported, caching: NA, event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: 'No', safety_shield: 'No', emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: 'No', real_time_claim_supported: NA}
repro: {code: 'No', code_url: NA, dataset: Partial (public VL datasets; robot data not stated as released), dataset_url: NA, checkpoints: 'No', prompts_published: Partial (prompt structures), hardware_specified: 'No', hyperparameters: Partial (appendix), protocol_described: Partial, project_page: 'https://palm-e.github.io', concerns: Proprietary model; not reproducible.}
limitations_flags: [resource-requirements]
web_verification_required: []
cited_missing: [PaLI, Inner Monologue, VIMA, Gato, Frozen (Tsimpoukelli 2021), OSRT, RT-1]
adjacent: {mechanism: 'Continuous sensor embeddings interleaved with text tokens in a pretrained LLM, trained end-to-end; LLM outputs plans/answers.', relevance: 'Archetype of VLM as high-level planner and scene interpreter (F1/F7) with discrete skill outputs, and of positive transfer from web-scale VL data.', why_not_direct: 'No humans as navigation agents, no social behaviour.', inherited_by: 'Cited by corpus PAD, MUSON, Cai survey; NavGPT; Pan review.'}
coding: {latency_reported: 'No', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: 'No', code_released: 'No', new_dataset_released: NA, real_robot: Demo, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2023
  authors: *id001
  venue: Proceedings of the 40th International Conference on Machine Learning (ICML 2023), PMLR 202, Honolulu
  volume: PMLR 202
  issue: NA
  pages: 20 (PDF incl. appendix)
  doi: Not reported
  url: https://palm-e.github.io
  pub_status: conference
  peer_reviewed: 'Yes'
  peer_review_basis: ICML 2023 PMLR footer (p.1).
project_url: https://palm-e.github.io
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: Proceedings of the 40th International Conference on Machine Learning (ICML 2023), PMLR 202
  verified_doi: Not found / not applicable
  verified_url: https://proceedings.mlr.press/v202/driess23a.html
  verified_pages: 8469-8488
  arxiv: 2303.03378v1
  version_relationship: Corpus copy is the PMLR published version; arXiv 2303.03378v1 alternate
  sources: ['PMLR proceedings page (https://proceedings.mlr.press/v202/driess23a.html)', arXiv abs page (2303.03378v1)]
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
  latency_reported: "No"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "No"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "Demo"
  human_subject_study: "No"
---

# PaLM-E (Driess et al., ICML 2023)

Page convention: PDF index (p.N).

## A. Bibliographic — ICML 2023, PMLR 202. Robotics at Google, TU Berlin, Google Research.

## B. Position — S3 adjacent: embodied multimodal LLM / high-level planner.

## C. Research problem — grounding LLMs in continuous sensor data for embodied reasoning (p.1–2). Contributions: generalist VL+robotics model; positive transfer; neural scene representations and entity-label tokens; VL generalist performance; less forgetting with scale (p.2).

## D. Method — encoders φ map observations into the LLM token space (Eq.3); variants: state MLP, ViT-4B/22B, ViT+TL, object-centric ViT, OSRT; entity referral tokens; cross-entropy on non-prefix tokens; frozen vs finetuned LLM; full mixture with 8.9% embodied data (p.3–5). Plans executed by low-level policies (RT-1; Lynch et al.) in closed loop (p.4, p.7).

## L. Quantitative results (visually verified p.8 for Tables 2/4)
- Table 1 (TAMP, 1% data; q1–q4 / p1 / p2): SayCan p1 38.7, p2 33.3; PaLI q2/q3 0.0/0.0; OSRT 99.7 / 98.2 / 100.0 / 93.7 / 82.5 / 76.2; ViT-4B full mixture – / 70.7 / 93.4 / 92.1 / 74.1 / 74.6 vs single robot – / 45.9 / 78.4 / 92.2 / 30.6 / 32.9.
- Table 2 (Language-Table; Task 1 with 10/20/40 demos): 12B finetuned full mixture 70.0 / 80.0 / 80.0 vs single robot 20.0 / 30.0 / 50.0; Task 3 (80 demos) 84B 64.4; SayCan and PaLI 0.0 on Task 1.
- Table 4 (F1, failure detection / affordance): PaLI 0.73 / 0.62; CLIP-FT 0.65 / –; CLIP-FT-hindsight 0.89 / –; QT-OPT – / 0.63; PaLM-E-12B scratch single robot 0.54 / 0.46; pretrained single robot 0.91 / 0.78; full mixture frozen 0.91 / 0.87; full mixture finetuned 0.77 / 0.91.
- Table 5: PaLM-E-562B OK-VQA 66.1, VQAv2 test-dev 80.0, COCO 138.7 (generalist).
- Fig.5: NLG relative performance drop 87.3% (12B) vs 3.9% (562B).

## N. Limitations
1. **Stated:** discussed in appendices B–C (not detailed in main text); frozen LLM occasionally struggled on robotics tasks (p.9).
2. **Observable:** real-robot evidence qualitative; navigation only as a named skill; proprietary and very large; no latency.
3. **Social relevance:** indirect (planner archetype).

## P. Adjacent analysis — see `adjacent:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue Proceedings of the 40th International Conference on Machine Learning (ICML 2023), PMLR 202; DOI Not found / not applicable; pages 8469-8488; URL https://proceedings.mlr.press/v202/driess23a.html.
- Sources: PMLR proceedings page (https://proceedings.mlr.press/v202/driess23a.html); arXiv abs page (2303.03378v1).
- Version relationship: Corpus copy is the PMLR published version; arXiv 2303.03378v1 alternate.
- Changed field - venue: PDF-derived 'Proceedings of the 40th International Conference on Machine Learning (ICML 2023), PMLR 202, Honolulu' -> externally verified 'Proceedings of the 40th International Conference on Machine Learning (ICML 2023), PMLR 202'
- Changed field - volume: PDF-derived 'PMLR 202' -> externally verified 'NA'
- Changed field - pages: PDF-derived '20 (PDF incl. appendix)' -> externally verified '8469-8488'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified 'Not found / not applicable'
- Changed field - url: PDF-derived 'https://palm-e.github.io' -> externally verified 'https://proceedings.mlr.press/v202/driess23a.html'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

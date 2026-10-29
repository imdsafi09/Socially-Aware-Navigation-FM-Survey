---
id: 2023_Brohan_RT-2
source_pdfs: [03_Adjacent_Foundation_Model_Navigation/zitkovich23a.pdf]
duplicate_copies: []
related_versions: ['arXiv:2307.15818 (not in corpus)']
title: 'RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control'
authors: &id001 [Brianna Zitkovich, Tianhe Yu, Sichun Xu, Peng Xu, Ted Xiao, Fei Xia, Jialin Wu, 'et al. (54 authors; PMLR v229 order, verified 2026-10-20; arXiv lists authors alphabetically from Anthony Brohan)']
year: 2023
venue: Proceedings of The 7th Conference on Robot Learning (CoRL 2023), PMLR 229
volume: NA
issue: NA
pages: 2165-2183
doi: Not found / not applicable
url: https://proceedings.mlr.press/v229/zitkovich23a.html
pub_status: conference
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): PMLR proceedings page (https://proceedings.mlr.press/v229/zitkovich23a.html); arXiv abs page (2307.15818v1). PDF-derived basis (Stage 1): CoRL 2023 footer (p.1).'
category: S3
folder: 03_Adjacent_Foundation_Model_Navigation
folder_category_match: 'Yes'
category_rationale: Vision-language-action model that co-fine-tunes PaLI-X/PaLM-E to output discretized manipulator actions; manipulation only; includes a 'person recognition' emergent-skill category but no social navigation.
paper_type: model
fm_used: 'Yes'
fm_class: [VLA, VLM]
fm_models: ['RT-2-PaLI-X (5B, 55B)', RT-2-PaLM-E (12B), RT-2-PaLI-3B (Language-Table)]
fm_size: 3B-55B
method_family: [co-fine-tuning on web VL data + robot trajectories, actions as text tokens (256 bins), constrained decoding, chain-of-thought plan + action]
roles: [F10]
roles_evidence: {F10: 'VLM directly outputs 6-DoF end-effector deltas, gripper and terminate tokens executed in closed loop (p.3-5).'}
integration: I7
integration_rationale: Direct action generation by the VLA; no separate planner.
evidence: E3
evidence_rationale: ~6,000 real-world evaluation trials on a 7-DoF mobile manipulator (seen tasks, unseen objects/backgrounds/environments, emergent skills; Tables 5-7) plus Language-Table simulation; no navigation and no human study.
inputs: [robot camera image, language instruction in VQA format]
outputs: ['action token string (terminate, Δpos xyz, Δrot xyz, gripper)', optional natural-language plan (CoT variant)]
human_repr: ['people as recognition targets in emergent-skill tasks (e.g., ''person with glasses'')']
capabilities: {C1: NA, C2: NA, C3: NA, C4: NA, C5: NA, C6: NA, C7: NA, C8: NA, C9: NA, C10: NA, C11: NA, C12: NA, C13: NA, C14: NA, C15: NA, C16: NA, C17: NA, C18: NA, C19: NA, C20: NA, C21: NA, C22: NA, C23: NA, C24: NA, C25: NA}
exp:
  datasets: ['RT-1 robot demonstrations (13 robots, 17 months, office kitchen)', WebLI / PaLI-X and PaLM-E web VL mixtures, Language-Table]
  simulators: [Language-Table simulation]
  robots: [7-DoF mobile manipulator (Everyday Robots), Language-Table robot]
  environment: office kitchen; unseen desk and sink environments
  indoor_outdoor: indoor
  sensors: [RGB]
  humans: people as visual recognition targets in some tasks
  n_scenes: Not reported
  n_trajectories: ~6,000 evaluation trials; >200 seen tasks; >280 unseen tasks
  n_participants: NA
  split: seen vs unseen objects/backgrounds/environments (easy/hard)
  baselines: [RT-1, VC-1, R3M, MOO, BC-Zero, LAVA]
  ablation: Yes (model size; scratch / fine-tune / co-fine-tune)
  real_robot_trials: 'Yes'
  human_study: 'No'
  statistical_testing: Partial (± in Language-Table; A/B testing protocol for emergent evals)
  scenarios: []
metrics: ['OTHER | Success rate | % | task success per category (seen, unseen, emergent) | p.6, App. H']
deployment: {fm_model: RT-2-PaLI-X-55B / 5B, model_size: 55B / 5B, api_cloud_local: Cloud (multi-TPU service queried over network), onboard_offboard: Offboard, gpu: TPU cloud, cpu: Not reported, latency: '1-3 Hz (55B); ~5 Hz (5B, PaLI-3B)', query_frequency: 1-5 Hz, planner_frequency: NA, controller_frequency: 1-5 Hz, asynchronous: Not reported, caching: NA, event_triggered: NA, distillation: No (future work), quantization: No (future work), fallback_planner: 'No', safety_shield: Output constrained to valid action tokens, emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: Constrained decoding for action tokens, real_time_claim_supported: Partial (1-3 Hz for 55B)}
repro: {code: 'No', code_url: NA, dataset: No (RT-1 data proprietary at time), dataset_url: NA, checkpoints: 'No', prompts_published: Partial (instruction lists in appendix), hardware_specified: Partial, hyperparameters: Partial (inherited from PaLI-X/PaLM-E), protocol_described: 'Yes', project_page: robotics-transformer2.github.io, concerns: Proprietary models and data; not reproducible.}
limitations_flags: [resource-requirements, cloud-dependence, latency]
web_verification_required: []
cited_missing: [RT-1, PaLI-X, MOO, VC-1, R3M, 'Open-source VLAs (later: OpenVLA, not cited)']
adjacent: {mechanism: Pretrained VLM fine-tuned jointly on web VL and robot data so that action tokens are generated like text (VLA)., relevance: Defines the VLA (I7/F10) end of the integration spectrum; latency (1-3 Hz cloud) and data needs frame the feasibility debate for VLA-style social navigation., why_not_direct: Manipulation only; humans only as recognition targets; no social navigation behaviour., inherited_by: 'Cited by corpus PAD, MUSON, Cai survey, SocialNav-SUB, Pan review.'}
coding: {latency_reported: 'Yes', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: Partial, code_released: 'No', new_dataset_released: NA, real_robot: Systematic, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2023
  authors: *id001
  venue: 7th Conference on Robot Learning (CoRL 2023), Atlanta (PMLR; file zitkovich23a)
  volume: Not reported
  issue: NA
  pages: 19+ (PDF incl. appendix)
  doi: Not reported
  url: robotics-transformer2.github.io
  pub_status: conference
  peer_reviewed: 'Yes'
  peer_review_basis: CoRL 2023 footer (p.1).
project_url: robotics-transformer2.github.io
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: Proceedings of The 7th Conference on Robot Learning (CoRL 2023), PMLR 229
  verified_doi: Not found / not applicable
  verified_url: https://proceedings.mlr.press/v229/zitkovich23a.html
  verified_pages: 2165-2183
  arxiv: 2307.15818v1
  version_relationship: Corpus copy is the PMLR published version; arXiv 2307.15818v1 alternate
  sources: ['PMLR proceedings page (https://proceedings.mlr.press/v229/zitkovich23a.html)', arXiv abs page (2307.15818v1)]
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
  latency_reported: "Yes"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "Partial"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "Systematic"
  human_subject_study: "No"
---

# RT-2 (Brohan et al., CoRL 2023)

Page convention: PDF index (p.N).

## A. Bibliographic — CoRL 2023 (footer p.1), PMLR file zitkovich23a; Google DeepMind; 54 authors alphabetical.

## B. Position — S3 adjacent: canonical VLA.

## C. Research problem — VLMs used only for high-level planning; can they be integrated directly into low-level control? (p.1). Contribution: RT-2 VLA family with co-fine-tuning (p.2).

## D. Method — 256-bin discretized actions mapped to tokens (PaLI-X integer tokens; PaLM-E overwrite least frequent tokens); VQA-format prompt; co-fine-tuning with up-weighted robot data; constrained decoding; cloud TPU serving at 1–3 Hz (55B) / ~5 Hz (5B) (p.3–5).

## L. Quantitative results (Appendix Table 5–6, visually verified p.18)
- Table 5 (seen; unseen objects easy/hard; backgrounds easy/hard; environments easy/hard; unseen avg): R3M 45; 32/14; 13/9; 0/2; 12 — VC-1 63; 34/10; 13/3; 0/0; 10 — RT-1 92; 31/43; 71/9; 26/14; 32 — MOO 75; 58/48; 38/41; 19/3; 35 — RT-2-PaLI-X-55B 91; 70/62; 96/48; 63/35; 62 — RT-2-PaLM-E-12B 93; 84/76; 75/71; 36/33; 62.
- Table 6 (emergent average): VC-1 11; RT-1 17; RT-2-PaLI-X-55B 60; RT-2-PaLM-E-12B 40. Person recognition average: VC-1 13, RT-1 20, PaLI-X 53, PaLM-E 43.
- Table 1 (Language-Table sim): BC-Zero 72 ± 3; RT-1 74 ± 13; LAVA 77 ± 4; RT-2-PaLI-3B 90 ± 10.
- **Data-quality note:** text states the PaLM-E variant "performs better … in harder versions … while under-performing on easier ones" (p.6), but Table 5 shows PaLM-E better on *easy* unseen objects (84 vs 70) and worse on *hard* unseen environments (33 vs 35).

## N. Limitations
1. **Stated (p.8):** no new motions beyond robot-data skills; high compute cost, real-time inference bottleneck; few VLMs available for fine-tuning.
2. **Future:** human videos for skills; quantization and distillation; open-source VLMs.
3. **Observable:** proprietary; cloud dependence; 1–3 Hz control too slow for dynamic crowds without additional safety layers.
4. **Social relevance:** "person recognition" emergent tasks are a minimal human-centric probe; no social behaviour.

## P. Adjacent analysis — see `adjacent:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue Proceedings of The 7th Conference on Robot Learning (CoRL 2023), PMLR 229; DOI Not found / not applicable; pages 2165-2183; URL https://proceedings.mlr.press/v229/zitkovich23a.html.
- Sources: PMLR proceedings page (https://proceedings.mlr.press/v229/zitkovich23a.html); arXiv abs page (2307.15818v1).
- Version relationship: Corpus copy is the PMLR published version; arXiv 2307.15818v1 alternate.
- Changed field - venue: PDF-derived '7th Conference on Robot Learning (CoRL 2023), Atlanta (PMLR; file zitkovich23a)' -> externally verified 'Proceedings of The 7th Conference on Robot Learning (CoRL 2023), PMLR 229'
- Changed field - volume: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - pages: PDF-derived '19+ (PDF incl. appendix)' -> externally verified '2165-2183'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified 'Not found / not applicable'
- Changed field - url: PDF-derived 'robotics-transformer2.github.io' -> externally verified 'https://proceedings.mlr.press/v229/zitkovich23a.html'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

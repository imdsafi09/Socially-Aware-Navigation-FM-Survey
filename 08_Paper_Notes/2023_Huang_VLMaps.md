---
id: 2023_Huang_VLMaps
source_pdfs: [03_Adjacent_Foundation_Model_Navigation/Visual_Language_Maps_for_Robot_Navigation.pdf]
duplicate_copies: []
related_versions: ['arXiv:2210.05714 (cited by NavGPT)']
title: Visual Language Maps for Robot Navigation
authors: &id001 [Chenguang Huang, Oier Mees, Andy Zeng, Wolfram Burgard]
year: 2023
venue: 2023 IEEE International Conference on Robotics and Automation (ICRA)
volume: NA
issue: NA
pages: 10608-10615
doi: 10.1109/ICRA48891.2023.10160969
url: https://doi.org/10.1109/ICRA48891.2023.10160969
pub_status: conference
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1109/ICRA48891.2023.10160969); arXiv abs page (2210.05714v4). PDF-derived basis (Stage 1): ICRA 2023 header with DOI (IEEE Xplore copy).'
category: S3
folder: 03_Adjacent_Foundation_Model_Navigation
folder_category_match: 'Yes'
category_rationale: Open-vocabulary spatial map fusing LSeg/CLIP pixel features into a 3D reconstruction, with LLM code generation for spatial-goal navigation; static scenes, no humans.
paper_type: method
fm_used: 'Yes'
fm_class: [CLIP-style, LLM]
fm_models: [LSeg (CLIP-space pixel embeddings), CLIP text encoder, code-writing LLM (Codex referenced; exact model not stated in main text)]
fm_size: Not reported
method_family: [open-vocabulary semantic mapping, LLM code generation (Code-as-Policies style), classical path planning]
roles: [F1, F6, F7]
roles_evidence: {F1: LSeg features fused into top-down map; landmarks localized by text-pixel similarity (Sec. III-A/B)., F6: Embodiment-specific obstacle maps generated from language lists of obstacle categories (Sec. III-C)., F7: LLM converts instructions into Python calls to parameterized navigation primitives (Sec. III-D).}
integration: I4
integration_rationale: FM-derived open-vocabulary obstacle maps and goal locations feed an off-the-shelf navigation stack; obstacle map is a constraint-generation role.
evidence: E3
evidence_rationale: Systematic simulation (Habitat/Matterport3D, AI2THOR) plus a real HSR robot trial set of 20 language goals with 10 successes; no human study.
inputs: [RGB-D video with odometry/poses, natural language instruction, obstacle category list]
outputs: [top-down open-vocabulary map, goal coordinates, obstacle maps, robot code]
human_repr: [none]
capabilities: {C1: NA, C2: NA, C3: NA, C4: NA, C5: NA, C6: NA, C7: NA, C8: NA, C9: NA, C10: NA, C11: NA, C12: NA, C13: NA, C14: NA, C15: NA, C16: NA, C17: NA, C18: NA, C19: NA, C20: NA, C21: NA, C22: NA, C23: NA, C24: NA, C25: NA}
exp:
  datasets: ['Matterport3D (10 scenes; 12,096 RGB-D frames)', 'AI2THOR (10 rooms; 1,826 frames)']
  simulators: [Habitat, AI2THOR]
  robots: [Toyota HSR (real), LoCoBot (sim), drone (sim)]
  environment: indoor homes; real indoor scene
  indoor_outdoor: indoor
  sensors: [RGB-D, odometry (RTAB-Map)]
  humans: none
  n_scenes: 10 + 10 sim; 1 real
  n_trajectories: 91 multi-object sequences; 21 spatial trajectories (7 scenes); >100 cross-embodiment sequences; 20 real goals
  n_participants: NA
  split: NA
  baselines: [LM-Nav, CLIP on Wheels (CoW), CLIP Map, GT semantic map (upper bound)]
  ablation: Yes (CLIP Map; LLM variants in appendix)
  real_robot_trials: 'Yes'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: []
metrics: [NAV | Success rate (N subgoals in a row) | % | consecutively reaching 1-4 subgoals within 1 m | p.5, NAV | Independent subgoal success | % | successful subgoals / 364 total | p.5, NAV | SPL | % | success weighted by normalized inverse path length | p.6]
deployment: {fm_model: LSeg + code LLM, model_size: Not reported, api_cloud_local: LLM via API (implied), onboard_offboard: Not reported, gpu: Not reported, cpu: Not reported, latency: Not reported, query_frequency: once per instruction, planner_frequency: NA, controller_frequency: Not reported, asynchronous: NA, caching: Map pre-built offline, event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: Off-the-shelf navigation stack, safety_shield: 'No', emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: 'No', real_time_claim_supported: NA}
repro: {code: Yes (stated), code_url: 'https://vlmaps.github.io', dataset: Simulator scenes public, dataset_url: NA, checkpoints: NA, prompts_published: Yes (appendix), hardware_specified: Partial, hyperparameters: Partial, protocol_described: 'Yes', project_page: 'https://vlmaps.github.io', concerns: Exact LLM not named in main text; real-robot evaluation small (20 goals).}
limitations_flags: [limited-scenarios]
web_verification_required: []
cited_missing: [CLIP on Wheels (CoW), NLMap, LSeg, Socratic Models, RTAB-Map]
adjacent: {mechanism: Spatially anchored open-vocabulary features enable language indexing of map locations and language-defined obstacle maps; LLM writes navigation code., relevance: 'Template for semantic/language maps that social systems extend with human/social layers (e.g., language-defined no-go or etiquette zones); authors explicitly list moving humans as future work.', why_not_direct: Static environments only; no human modelling., inherited_by: 'Cited by corpus CoNVOI, VL-TGS, ViLAM, Cai survey, NavGPT, G2-Nav (via search: ''Visual Language Maps'').'}
coding: {latency_reported: 'No', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: 'No', code_released: 'Yes', new_dataset_released: NA, real_robot: Systematic, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2023
  authors: *id001
  venue: 2023 IEEE International Conference on Robotics and Automation (ICRA 2023), London
  volume: NA
  issue: NA
  pages: 10608-10615
  doi: 10.1109/ICRA48891.2023.10160969
  url: https://vlmaps.github.io
  pub_status: conference
  peer_reviewed: 'Yes'
  peer_review_basis: ICRA 2023 header with DOI (IEEE Xplore copy).
project_url: https://vlmaps.github.io
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: 2023 IEEE International Conference on Robotics and Automation (ICRA)
  verified_doi: 10.1109/ICRA48891.2023.10160969
  verified_url: https://doi.org/10.1109/ICRA48891.2023.10160969
  verified_pages: 10608-10615
  arxiv: 2210.05714v4
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1109/ICRA48891.2023.10160969)', arXiv abs page (2210.05714v4)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A0]
  C_capabilities: {SAF1: NA, SAF2: NA, SPA1: NA, SPA2: NA, SPA3: NA, SPA4: NA, HUM1: NA, HUM2: NA, NOR1: NA, NOR2: NA, NOR3: NA, NOR4: NA, EXP1: NA, EXP2: NA, EXP3: NA}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: systematic, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "03_Adjacent_Foundation_Model_Navigation"
analytical_category: "S3"
coding:
  latency_reported: "No"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "No"
  code_released: "Yes"
  new_dataset_released: "NA"
  real_robot: "Systematic"
  human_subject_study: "No"
---

# VLMaps (Huang, Mees, Zeng, Burgard — ICRA 2023)

Page convention: PDF index (p.N).

## A. Bibliographic — ICRA 2023, pp.10608–10615, DOI 10.1109/ICRA48891.2023.10160969. Freiburg, Google Research, UTN.

## B. Position — S3 adjacent: open-vocabulary spatial maps for language navigation.

## C. Research problem — VLM-based navigation (CoW, LM-Nav) is disjoint from mapping and lacks spatial precision (p.1). Contributions: VLMaps; spatial goal localization via code-writing LLMs; open-vocabulary multi-embodiment obstacle maps (p.1).

## D. Method — back-project LSeg pixel embeddings to a top-down grid and average (Eq.1); text-to-cell similarity S = Q·Eᵀ + argmax for segmentation; obstacle map from height-filtered points ∩ language-specified categories (Eq.2); LLM-generated code calls primitives such as move_to_left('counter') with scripted offsets; off-the-shelf navigation stack (p.2–4).

## L. Quantitative results
- Table I (multi-object nav, % success for 1/2/3/4 subgoals in a row; independent): LM-Nav 26/4/1/1; 26 — CoW 42/15/7/3; 36 — CLIP Map 33/8/2/0; 30 — VLMaps 59/34/22/15; 59 — GT map 91/78/71/67; 85.
- Table II (spatial goals, 1/2/3/4 in a row): LM-Nav 5/5/0/0; CoW 33/5/0/0; CLIP Map 19/0/0/0; VLMaps 62/33/14/10; GT 76/48/33/29.
- Table III (SR / SPL for 1–4 in a row; independent SR): LoCoBot ground map 53/49.0, 28/17.8, 14/6.7, 6/2.5; 52.3 — Drone ground map 53/41.8, 28/15.5, 14/5.3, 6/2.0; 53.3 — Drone drone map 56/45.4, 30/16.3, 17/7.0, 7/2.5; 55.0.
- Real HSR: 10 of 20 language goals reached (6 spatial, 3 relative, 1 repetition); failures from depth noise and action noise (p.6).

## N. Limitations
1. **Stated (p.6):** sensitive to reconstruction noise and odometry drift; cannot resolve ambiguities among similar objects.
2. **Future (p.6):** better VLMs; **extend to dynamic objects and moving humans**.
3. **Observable:** map pre-built offline; small real-robot test; exact LLM unspecified in main text.
4. **Social relevance:** none evaluated; explicit future-work pointer to humans.

## P. Adjacent analysis — see `adjacent:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue 2023 IEEE International Conference on Robotics and Automation (ICRA); DOI 10.1109/ICRA48891.2023.10160969; pages 10608-10615; URL https://doi.org/10.1109/ICRA48891.2023.10160969.
- Sources: Crossref (exact title match, DOI 10.1109/ICRA48891.2023.10160969); arXiv abs page (2210.05714v4).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - venue: PDF-derived '2023 IEEE International Conference on Robotics and Automation (ICRA 2023), London' -> externally verified '2023 IEEE International Conference on Robotics and Automation (ICRA)'
- Changed field - url: PDF-derived 'https://vlmaps.github.io' -> externally verified 'https://doi.org/10.1109/ICRA48891.2023.10160969'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

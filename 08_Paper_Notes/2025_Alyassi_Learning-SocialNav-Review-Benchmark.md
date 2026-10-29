---
id: 2025_Alyassi_Learning-SocialNav-Review-Benchmark
source_pdfs: [00_Existing_Surveys/frobt-12-1658643.pdf]
duplicate_copies: []
related_versions: []
title: 'Social robot navigation: a review and benchmarking of learning-based methods'
authors: &id001 [Rashid Alyassi, Cesar Cadena, Robert Riener, Diego Paez-Granados]
year: 2025
venue: Frontiers in Robotics and AI
volume: '12'
issue: NA
pages: Article 1658643
doi: 10.3389/frobt.2025.1658643
url: https://doi.org/10.3389/frobt.2025.1658643
pub_status: journal; survey/review
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.3389/frobt.2025.1658643). PDF-derived basis (Stage 1): Frontiers review with editor/reviewers and received/revised/accepted dates (p.1).'
category: S0
folder: 00_Existing_Surveys
folder_category_match: 'Yes'
category_rationale: Review of learning-based social navigation (taxonomy, training components, evaluation) plus an own benchmark of representative planners; includes a subsection on language models and 'social vision-language navigation' as future direction.
paper_type: survey
fm_used: 'No'
fm_class: [None]
fm_models: []
fm_size: NA
method_family: [literature review, benchmarking study]
roles: []
roles_evidence: {}
integration: NA
integration_rationale: Survey.
evidence: NA
evidence_rationale: Survey with its own GPU-accelerated simulation benchmark (Habitat Sim + SFM/ORCA crowds) of 3 baselines and 6 learning-based planners over 6 scenarios (§4); results reported graphically only; not evidence for a proposed method.
inputs: []
outputs: []
human_repr: []
capabilities: {C1: NA, C2: NA, C3: NA, C4: NA, C5: NA, C6: NA, C7: NA, C8: NA, C9: NA, C10: NA, C11: NA, C12: NA, C13: NA, C14: NA, C15: NA, C16: NA, C17: NA, C18: NA, C19: NA, C20: NA, C21: NA, C22: NA, C23: NA, C24: NA, C25: NA}
exp:
  datasets: []
  simulators: []
  robots: []
  environment: NA
  indoor_outdoor: NA
  sensors: []
  humans: NA
  n_scenes: NA
  n_trajectories: NA
  n_participants: NA
  split: NA
  baselines: []
  ablation: NA
  real_robot_trials: NA
  human_study: NA
  statistical_testing: NA
  scenarios: []
metrics: []
deployment: {fm_model: NA, model_size: NA, api_cloud_local: NA, onboard_offboard: NA, gpu: NA, cpu: NA, latency: NA, query_frequency: NA, planner_frequency: NA, controller_frequency: NA, asynchronous: NA, caching: NA, event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: NA, safety_shield: NA, emergency_behavior: NA, uncertainty: NA, hallucination_mitigation: NA, real_time_claim_supported: NA}
repro: {code: 'Additional resources at https://socialnavigation.github.io (code release not explicitly stated)', code_url: NA, dataset: NA, dataset_url: NA, checkpoints: NA, prompts_published: NA, hardware_specified: NA, hyperparameters: NA, protocol_described: No literature-search protocol reported; benchmark protocol described (§4.1-4.3), project_page: 'https://socialnavigation.github.io', concerns: No systematic search method; benchmark results only in figures (no numeric tables); abstract says planners from 7 categories while §4.3 lists 3 baselines + 6 learning-based planners.}
limitations_flags: []
web_verification_required: []
cited_missing: [Okunevich 2025 online learning social cost, Ma 2023 Eureka (LLM reward design), Wang 2024 LLM preference-aligned navigation, Stratton 2024 crowd sim, Li 2024 VLN extended to social navigation, RGL (Chen 2020), GA3C-CADRL (Everett 2018), Fan 2020 DRL-Long (IJRR)]
survey:
  scope: 'Learning-based social navigation: problem types (independent/assistive/collaborative); algorithm taxonomy (end-to-end incl. LfD, model-based RL, perception, multi-objective/hierarchical RL, vision-based, language models, self-supervised; human-position-based; attention/GNN-based; prediction-based (MCTS, MPC); safety-aware (multi-policy, constrained RL)); training (reward taxonomy, simulators, crowd data, detection/tracking/prediction, scene understanding, training enhancements); evaluation; own benchmark; future directions incl. social vision-language navigation'
  years_covered: Not reported (recent learning-based work to 2025)
  search_strategy: Not reported
  inclusion: Not reported
  exclusion: Not reported
  n_papers: Not reported
  n_refs: ~310-360 (approximate count of author-year entries in text extraction)
  taxonomy: Algorithm families (end-to-end, human-position, attention, prediction, safety-aware) x training components
  taxonomy_dims: Method taxonomy + training-component taxonomy
  datasets_covered: Yes (crowd data section)
  simulators_covered: Yes (simulation platform section; CrowdNav, Habitat, Gazebo etc.)
  metrics_covered: Yes (§3.6.2)
  coverage: {classical: Partial, human_aware: 'Yes', proxemics: Partial, prediction: 'Yes', imitation_learning: 'Yes', drl: 'Yes', gnn_transformer: 'Yes', language_models: Partial, vlm: Partial, lvlm: Partial, foundation_models: 'No', vla: 'No', real_world_deployment: Partial, evaluation: 'Yes'}
  stage2_coverage: {classical_proxemics: Partial, learning_drl: 'Yes', gnn_transformer: 'Yes', llm: Partial, vlm: Partial, vla: 'No', social_capability_taxonomy: No (algorithm-family taxonomy), evidence_maturity_analysis: 'No', evaluation_audit: Yes (own benchmark), deployment_analysis: 'No', fm_reliability: 'No', human_subject_evidence: 'No', direct_overlap_with_our_survey: '4 of our 41 direct papers cited: 2024_Wang_SALM; 2025_Luo_GSON; 2025_Narasimhan_OLiVia-Nav; 2025_Song_VLM-Social-Nav', basis: Stage-2 manual coding from survey note coverage/taxonomy + extracted-text keyword checks (2026-10-19); overlap is a lower bound (title/arXiv-id string match + manual).}
coding: {latency_reported: NA, safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: NA, new_dataset_released: NA, real_robot: NA, human_subject_study: NA}
pdf_metadata_stage1:
  year: 2025
  authors: *id001
  venue: Frontiers in Robotics and AI, Vol. 12, Article 1658643 (published 11 Dec 2025)
  volume: '12'
  issue: NA
  pages: Article 1658643 (34 pages)
  doi: 10.3389/frobt.2025.1658643
  url: Not reported
  pub_status: journal; survey/review
  peer_reviewed: 'Yes'
  peer_review_basis: Frontiers review with editor/reviewers and received/revised/accepted dates (p.1).
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: Frontiers in Robotics and AI
  verified_doi: 10.3389/frobt.2025.1658643
  verified_url: https://doi.org/10.3389/frobt.2025.1658643
  verified_pages: Article 1658643
  arxiv: NA
  version_relationship: Corpus copy is the published version
  sources: ['Crossref (exact title match, DOI 10.3389/frobt.2025.1658643)']
final_coding: {status: NA (survey)}
physical_source_folder: "00_Existing_Surveys"
analytical_category: "S0"
coding:
  latency_reported: "NA"
  safety_mechanism: "NA"
  uncertainty_treatment: "NA"
  hallucination_treatment: "NA"
  code_released: "NA"
  new_dataset_released: "NA"
  real_robot: "NA"
  human_subject_study: "NA"
---

# Social Robot Navigation: A Review and Benchmarking of Learning-Based Methods (Alyassi et al., Front. Robot. AI 2025)


## A. Bibliographic — Front. Robot. AI 12:1658643, published 11 Dec 2025, DOI 10.3389/frobt.2025.1658643; ETH Zurich, Swiss Paraplegic Research.

## C. Structure (from headings) — §1 problem (independent/assistive/collaborative); §2 algorithms; §3 training (rewards, environments, perception, enhancement, evaluation); §4 own benchmark (baseline, end-to-end, IL, attention, prediction, safety-aware planners); §5 future directions (safety/realism, social alignment/preferences, transparency, social vision-language navigation).

## D. Language models (§2.1.6, p.6) — summarizes VLM-Social-Nav (Song 2024: VLM selects direction/speed, weights via second prompt), GSON (VLM group detection + MPC), OLiVia-Nav (distilled encoders + lifelong learning), Okunevich 2025 (online social-cost adaptation), LLM reward generation (Ma 2023; Wang 2024), Social-LLaVA (VLM maps to navigation primitives). States that slow inference and compute demands limit VLMs for reactive navigation, so they are mostly used as global planners, semantic encoders or social-context modules.

## E. Own benchmark (§4, p.21–25) — GPU kinematic simulation, Habitat Sim RGB/depth + ray-cast LiDAR, Habitat 3.0 humans (~600 FPS for 40 humans), SFM and ORCA crowds; curriculum learning; 6 scenarios (static, doorway, corridor, intersection, open-space random, open-space ETH/UCY data-driven); planners: ORCA, SFM, DWA (privileged), end-to-end RL (Fan 2020 + GRU), BC (35,000 episodes), GA3C-CADRL + LiDAR, SARL actor-critic + LiDAR, RGL-based prediction planner, safety-aware switcher (ORCA + attention). Results only in Figs.4–5: learning-based planners outperform model-based in success and safety, especially doorway/intersection; prediction-based planner highest overall success and velocity; IL weak in constrained settings.

## F. Future directions (§5) — safety/robustness, scenario diversity, physics/sensor realism, realistic crowd simulation (human–robot reactions), robust evaluation, social norms and preferences, explainability, and social vision-language navigation (§5.3.2: interpret intent, infer norms from language, communicate decisions).

## N. Limitations (of the survey) — no search protocol; benchmark in simulation with SFM/ORCA crowds only; numeric results not tabulated; VLM coverage brief (one subsection + future direction).

## P. Survey analysis — see `survey:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue Frontiers in Robotics and AI; DOI 10.3389/frobt.2025.1658643; pages Article 1658643; URL https://doi.org/10.3389/frobt.2025.1658643.
- Sources: Crossref (exact title match, DOI 10.3389/frobt.2025.1658643).
- Version relationship: Corpus copy is the published version.
- Changed field - venue: PDF-derived 'Frontiers in Robotics and AI, Vol. 12, Article 1658643 (published 11 Dec 2025)' -> externally verified 'Frontiers in Robotics and AI'
- Changed field - pages: PDF-derived 'Article 1658643 (34 pages)' -> externally verified 'Article 1658643'
- Changed field - url: PDF-derived 'Not reported' -> externally verified 'https://doi.org/10.3389/frobt.2025.1658643'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

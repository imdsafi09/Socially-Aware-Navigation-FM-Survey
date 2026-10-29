---
id: 2017_Charalampous_Social-Aware-Navigation-Survey
source_pdfs: [00_Existing_Surveys/1-s2.0-S0921889016302287-main.pdf]
duplicate_copies: []
related_versions: []
title: 'Recent trends in social aware robot navigation: A survey'
authors: &id001 [Konstantinos Charalampous, Ioannis Kostavelis, Antonios Gasteratos]
year: 2017
venue: Robotics and Autonomous Systems
volume: '93'
issue: NA
pages: 85-104
doi: 10.1016/j.robot.2017.03.002
url: https://doi.org/10.1016/j.robot.2017.03.002
pub_status: journal; survey/review
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1016/j.robot.2017.03.002). PDF-derived basis (Stage 1): Elsevier RAS ''Review'' with received/accepted dates (p.1).'
category: S0
folder: 00_Existing_Surveys
folder_category_match: 'Yes'
category_rationale: 'Survey of perception layers for social navigation: metric, semantic and social mapping, datasets, open issues.'
paper_type: survey
fm_used: 'No'
fm_class: [None]
fm_models: []
fm_size: NA
method_family: [literature review]
roles: []
roles_evidence: {}
integration: NA
integration_rationale: Survey.
evidence: NA
evidence_rationale: Survey; no experiments.
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
repro: {code: NA, code_url: NA, dataset: NA, dataset_url: NA, checkpoints: NA, prompts_published: NA, hardware_specified: NA, hyperparameters: NA, protocol_described: NA, project_page: NA, concerns: No search protocol.}
limitations_flags: []
web_verification_required: [DOI of RAS 93 (2017) 85-104.]
cited_missing: [Kruse 2013 (in corpus), Rios-Martinez proxemics survey (IJSR 2015), Kostavelis & Gasteratos semantic mapping survey (2015), Vasquez IRL comparison (IROS 2014)]
survey:
  scope: 'Perception hierarchy for human-robot symbiosis: metric mapping, semantic mapping, social mapping (indoor/outdoor, prediction, body information, context awareness); benchmarking, datasets, open issues'
  years_covered: Historical overview to 2016
  search_strategy: Not reported
  inclusion: Not reported
  exclusion: Not reported
  n_papers: Not reported (Table 3 summarizes social mapping methods)
  n_refs: 134
  taxonomy: Metric mapping (optimization, features, indoor/outdoor) -> semantic mapping (scale, topological, temporal) -> social mapping (indoor/outdoor, predictive mechanism, human body information, context awareness)
  taxonomy_dims: Hierarchical perception layers + attribute matrix (Table 3, Fig.13)
  datasets_covered: Mostly SLAM/semantic mapping datasets (RGB-D, urban stereo/laser); few social datasets
  simulators_covered: Minimal
  metrics_covered: Localization error (SLAM); questionnaire-based comfort/naturalness/sociability; trajectory comparison vs annotated human paths (noting non-uniqueness)
  coverage: {classical: 'Yes', human_aware: 'Yes', proxemics: 'Yes', prediction: 'Yes', imitation_learning: Partial, drl: 'No', gnn_transformer: 'No', language_models: 'No', vlm: 'No', lvlm: 'No', foundation_models: 'No', vla: 'No', real_world_deployment: Partial, evaluation: Partial}
  stage2_coverage: {classical_proxemics: 'Yes', learning_drl: 'No', gnn_transformer: 'No', llm: 'No', vlm: 'No', vla: 'No', social_capability_taxonomy: No (mapping-centred taxonomy), evidence_maturity_analysis: 'No', evaluation_audit: 'No', deployment_analysis: 'No', fm_reliability: NA (pre-FM), human_subject_evidence: Partial, direct_overlap_with_our_survey: 0 of our 41 direct papers cited, basis: Stage-2 manual coding from survey note coverage/taxonomy + extracted-text keyword checks (2026-10-19); overlap is a lower bound (title/arXiv-id string match + manual).}
coding: {latency_reported: NA, safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: NA, new_dataset_released: NA, real_robot: NA, human_subject_study: NA}
pdf_metadata_stage1:
  year: 2017
  authors: *id001
  venue: Robotics and Autonomous Systems
  volume: '93'
  issue: Not reported
  pages: 85-104
  doi: Not reported
  url: Not reported
  pub_status: journal; survey/review
  peer_reviewed: 'Yes'
  peer_review_basis: Elsevier RAS 'Review' with received/accepted dates (p.1).
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: Robotics and Autonomous Systems
  verified_doi: 10.1016/j.robot.2017.03.002
  verified_url: https://doi.org/10.1016/j.robot.2017.03.002
  verified_pages: 85-104
  arxiv: NA
  version_relationship: Corpus copy is the published version
  sources: ['Crossref (exact title match, DOI 10.1016/j.robot.2017.03.002)']
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

# Recent Trends in Social Aware Robot Navigation (Charalampous et al., RAS 2017)

Page convention: PDF index (p.N).

## A. Bibliographic — RAS 93 (2017) 85–104; Democritus University of Thrace.

## B. Position — S0; mapping/perception-centred survey ("social mapping").

## C. Scope — §2 history; §3 metric, semantic and social mapping; §4 benchmarking, datasets and norms; §5 open questions (need for social maps, evaluation, crowds, indoor/outdoor blending, readiness); §6 future work (reusable features, lifelong mapping, topological/temporal coherence); §7 coda (p.1–17).

## D. Key messages — sociability includes not passing through conversing groups (p.16); evaluation either against annotated human trajectories (non-unique) or questionnaires (not repeatable) (p.16); robots need semantic understanding of environment, human activity and behavioural models (p.16) — conceptually aligned with later VLM scene understanding.

## N. Limitations (of the survey) — no systematic method; predates DRL/FM; social datasets sparse.

## P. Survey analysis — see `survey:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue Robotics and Autonomous Systems; DOI 10.1016/j.robot.2017.03.002; pages 85-104; URL https://doi.org/10.1016/j.robot.2017.03.002.
- Sources: Crossref (exact title match, DOI 10.1016/j.robot.2017.03.002).
- Version relationship: Corpus copy is the published version.
- Changed field - issue: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified '10.1016/j.robot.2017.03.002'
- Changed field - url: PDF-derived 'Not reported' -> externally verified 'https://doi.org/10.1016/j.robot.2017.03.002'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

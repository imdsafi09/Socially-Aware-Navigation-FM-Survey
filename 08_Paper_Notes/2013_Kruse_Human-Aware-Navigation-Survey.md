---
id: 2013_Kruse_Human-Aware-Navigation-Survey
source_pdfs: [00_Existing_Surveys/1-s2.0-S0921889013001048-main.pdf]
duplicate_copies: []
related_versions: []
title: 'Human-aware robot navigation: A survey'
authors: &id001 [Thibault Kruse, Amit Kumar Pandey, Rachid Alami, Alexandra Kirsch]
year: 2013
venue: Robotics and Autonomous Systems
volume: '61'
issue: '12'
pages: 1726-1743
doi: 10.1016/j.robot.2013.05.007
url: https://doi.org/10.1016/j.robot.2013.05.007
pub_status: journal; survey/review
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1016/j.robot.2013.05.007). PDF-derived basis (Stage 1): Elsevier RAS journal layout with received/revised/accepted dates (p.1).'
category: S0
folder: 00_Existing_Surveys
folder_category_match: 'Yes'
category_rationale: Foundational survey of human-aware navigation (comfort, naturalness, sociability) and navigation-framework functions.
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
repro: {code: NA, code_url: NA, dataset: NA, dataset_url: NA, checkpoints: NA, prompts_published: NA, hardware_specified: NA, hyperparameters: NA, protocol_described: NA, project_page: NA, concerns: No search protocol; authors note publication list 'may not be exhaustive or objective' (Fig.1).}
limitations_flags: []
web_verification_required: []
cited_missing: [Sisbot human-aware motion planner (T-RO 2007), Pacchierotti passing studies, Lichtenthäler legibility, Walters proxemics studies, Hall proxemics]
survey:
  scope: 'Human-aware navigation for wheeled assistive robots: comfort, naturalness, sociability; navigation framework modules; evaluation'
  years_covered: ~1990s-2013 (Fig.1 publication counts)
  search_strategy: Not reported (no systematic protocol)
  inclusion: Not reported
  exclusion: Not reported
  n_papers: Not reported
  n_refs: 106
  taxonomy: 'Goals: comfort / naturalness / sociability; functions: prediction, pose selection, path planning (global costs, temporal), behaviour selection, local planning'
  taxonomy_dims: 2 (human-awareness feature category x navigation function)
  datasets_covered: None
  simulators_covered: Generic simulation-based evaluation only
  metrics_covered: Distance as discomfort proxy; questionnaires/Likert; video studies; long-term adaptation
  coverage: {classical: 'Yes', human_aware: 'Yes', proxemics: 'Yes', prediction: 'Yes', imitation_learning: Partial, drl: 'No', gnn_transformer: 'No', language_models: 'No', vlm: 'No', lvlm: 'No', foundation_models: 'No', vla: 'No', real_world_deployment: Partial, evaluation: 'Yes'}
  stage2_coverage: {classical_proxemics: 'Yes', learning_drl: 'No', gnn_transformer: 'No', llm: 'No', vlm: 'No', vla: 'No', social_capability_taxonomy: 'Partial (goals: comfort, naturalness, sociability)', evidence_maturity_analysis: 'No', evaluation_audit: Partial, deployment_analysis: 'No', fm_reliability: NA (pre-FM), human_subject_evidence: Partial (discusses user studies), direct_overlap_with_our_survey: 0 of our 41 direct papers cited, basis: Stage-2 manual coding from survey note coverage/taxonomy + extracted-text keyword checks (2026-10-19); overlap is a lower bound (title/arXiv-id string match + manual).}
coding: {latency_reported: NA, safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: NA, new_dataset_released: NA, real_robot: NA, human_subject_study: NA}
pdf_metadata_stage1:
  year: 2013
  authors: *id001
  venue: Robotics and Autonomous Systems
  volume: '61'
  issue: 12 (not printed; pages 1726-1743)
  pages: 1726-1743
  doi: 10.1016/j.robot.2013.05.007
  url: Not reported
  pub_status: journal; survey/review
  peer_reviewed: 'Yes'
  peer_review_basis: Elsevier RAS journal layout with received/revised/accepted dates (p.1).
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: Robotics and Autonomous Systems
  verified_doi: 10.1016/j.robot.2013.05.007
  verified_url: https://doi.org/10.1016/j.robot.2013.05.007
  verified_pages: 1726-1743
  arxiv: NA
  version_relationship: Corpus copy is the published version
  sources: ['Crossref (exact title match, DOI 10.1016/j.robot.2013.05.007)']
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

# Human-Aware Robot Navigation: A Survey (Kruse et al., RAS 2013)

Page convention: PDF index (p.N).

## A. Bibliographic — RAS 61 (2013) 1726–1743, DOI 10.1016/j.robot.2013.05.007; TUM, LAAS-CNRS, Tübingen.

## B. Position — S0, the canonical early survey; defines comfort, naturalness, sociability (p.2–3).

## C. Scope and structure — §2 challenges (comfort incl. user studies, natural motion, social constraints); §3 navigation framework (prediction—geometric vs ML; pose selection; path planning—global cost functions, temporal planning; behaviour selection; local planning; integration); §4 evaluation (simulation vs user studies); §5 conclusion (p.1–16).

## D. Key messages — no holistic theory of human-aware navigation; challenge is to unify methods semantically and ground encounters as interactions following social rules (p.16). Evaluation of comfort is the most problematic area; two strategies—model-based simulation or participant questionnaires (p.15–16).

## N. Limitations (of the survey)
1. **Stated:** publication list may not be exhaustive or objective (Fig.1).
2. **Observable:** no systematic search; predates DRL, datasets, benchmarks and all FM work.

## P. Survey analysis — see `survey:` block. Relevance to our survey: provides the comfort/naturalness/sociability vocabulary and the "semantic grounding of social rules" challenge that VLM approaches claim to address.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue Robotics and Autonomous Systems; DOI 10.1016/j.robot.2013.05.007; pages 1726-1743; URL https://doi.org/10.1016/j.robot.2013.05.007.
- Sources: Crossref (exact title match, DOI 10.1016/j.robot.2013.05.007).
- Version relationship: Corpus copy is the published version.
- Changed field - issue: PDF-derived '12 (not printed; pages 1726-1743)' -> externally verified '12'
- Changed field - url: PDF-derived 'Not reported' -> externally verified 'https://doi.org/10.1016/j.robot.2013.05.007'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

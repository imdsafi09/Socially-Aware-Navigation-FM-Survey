---
id: 2024_Karwowski_Requirements-Planning-Evaluation-Review
source_pdfs: [00_Existing_Surveys/sensors-24-02794-v2.pdf]
duplicate_copies: []
related_versions: []
title: 'Bridging Requirements, Planning, and Evaluation: A Review of Social Robot Navigation'
authors: &id001 [Jarosław Karwowski, Wojciech Szynkiewicz, Ewa Niewiadomska-Szynkiewicz]
year: 2024
venue: Sensors
volume: '24'
issue: '9'
pages: Article 2794
doi: 10.3390/s24092794
url: https://doi.org/10.3390/s24092794
pub_status: journal; survey/review
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.3390/s24092794). PDF-derived basis (Stage 1): MDPI Sensors with academic editor and received/revised/accepted/published dates (p.1).'
category: S0
folder: 00_Existing_Surveys
folder_category_match: 'Yes'
category_rationale: Requirements-grounded review (from user studies) of social navigation perception, motion planning and evaluation tools, classifying methods by fulfilled requirements.
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
repro: {code: NA, code_url: NA, dataset: NA, dataset_url: NA, checkpoints: NA, prompts_published: NA, hardware_specified: NA, hyperparameters: NA, protocol_described: 'Partial (databases, query, >600 hits, relevance-based selection; authors state not a systematic scoping process)', project_page: NA, concerns: Selection by relevance rather than explicit criteria.}
limitations_flags: []
web_verification_required: []
cited_missing: [SRPB benchmark (Karwowski & Szynkiewicz 2023), CORTEX cognitive architecture, Rios-Martinez proxemics survey, Elevator etiquette / queueing studies, Gaze modulation studies in robot navigation]
survey:
  scope: 'Requirements of social navigation derived from user studies (physical safety, perceived safety, naturalness, social norms); perception (environment representation, detection/tracking, prediction, contextual awareness: environmental, interpersonal, diversity, task); motion planning (global and local families incl. learning-based); evaluation (methods, studies, datasets, simulators, benchmarks); challenges'
  years_covered: Not limited by year; included publications shown 2014-2024 (Fig.1) plus older user studies
  search_strategy: IEEE Xplore, ScienceDirect, SpringerLink, ACM DL, Google Scholar, arXiv; query ('social' OR 'human-aware') AND 'navigation' AND 'robot' (>600 results) plus prior-survey bibliographies and cross-references of user studies
  inclusion: Relevance to requirements-driven social navigation and its evaluation (papers, software modules, datasets)
  exclusion: Explicit communication, negotiation, physical contact interaction, robot types other than ground-wheeled (de-emphasized)
  n_papers: Not reported
  n_refs: 391
  taxonomy: Requirements taxonomy (Req.1 physical safety, Req.2 perceived safety incl. proxemics, Req.3 naturalness, Req.4 social norms) mapped to perception and planning methods (Table 2)
  taxonomy_dims: Requirements x algorithm families
  datasets_covered: 'Yes'
  simulators_covered: Yes (extensive simulator review)
  metrics_covered: Yes (refers to Gao & Huang for metric details; proposes absolute social metrics)
  coverage: {classical: 'Yes', human_aware: 'Yes', proxemics: 'Yes', prediction: 'Yes', imitation_learning: 'Yes', drl: 'Yes', gnn_transformer: Partial, language_models: 'No', vlm: 'No', lvlm: 'No', foundation_models: 'No', vla: 'No', real_world_deployment: Partial, evaluation: 'Yes'}
  stage2_coverage: {classical_proxemics: 'Yes', learning_drl: 'Yes', gnn_transformer: Partial, llm: 'No', vlm: 'No', vla: 'No', social_capability_taxonomy: Yes (requirements Req.1-Req.4), evidence_maturity_analysis: 'No', evaluation_audit: 'Yes', deployment_analysis: 'No', fm_reliability: NA (pre-FM), human_subject_evidence: Yes (user studies grounding requirements), direct_overlap_with_our_survey: 0 of our 41 direct papers cited, basis: Stage-2 manual coding from survey note coverage/taxonomy + extracted-text keyword checks (2026-10-19); overlap is a lower bound (title/arXiv-id string match + manual).}
coding: {latency_reported: NA, safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: NA, new_dataset_released: NA, real_robot: NA, human_subject_study: NA}
pdf_metadata_stage1:
  year: 2024
  authors: *id001
  venue: Sensors (MDPI) 24(9):2794
  volume: '24'
  issue: '9'
  pages: 2794 (61 pages)
  doi: 10.3390/s24092794
  url: https://doi.org/10.3390/s24092794
  pub_status: journal; survey/review
  peer_reviewed: 'Yes'
  peer_review_basis: MDPI Sensors with academic editor and received/revised/accepted/published dates (p.1).
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: Sensors
  verified_doi: 10.3390/s24092794
  verified_url: https://doi.org/10.3390/s24092794
  verified_pages: Article 2794
  arxiv: NA
  version_relationship: Corpus copy is the published version
  sources: ['Crossref (exact title match, DOI 10.3390/s24092794)']
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

# Bridging Requirements, Planning, and Evaluation (Karwowski et al., Sensors 2024)

Page convention: PDF index (p.N).

## A. Bibliographic — Sensors 24(9):2794, published 27 Apr 2024, DOI 10.3390/s24092794; Warsaw University of Technology.

## B. Position — S0; the most requirement-grounded pre-FM survey; explicitly classifies algorithms by which social requirements they satisfy.

## C. Scope — §1 scope and materials collection (p.2–3); §2 related surveys; §3 requirements taxonomy (Fig.3) and discussion; §4 perception incl. contextual awareness; §5 motion planning (graph, potential field, roadmap, sampling; local sampling, fuzzy, force, VO, optimization, learning) with discussion; §6 evaluation (methods, studies, datasets, simulators, benchmarks); §7 discussion; §8 summary.

## D. Key messages (§7, p.42–44) — fewer recent user studies on norms; complex social conventions (queueing, elevator etiquette) rarely implemented and fragmentary; many DRL methods are collision avoidance with circular personal space rather than human-aware navigation; proposes a "social activity planner" layer above global/local planners, driven by knowledge bases and context, and a context-aware framework that weights multi-objective costs; need for context-aware benchmarks and absolute social metrics.

## N. Limitations (of the survey) — not a systematic scoping review (stated); pre-FM.

## P. Survey analysis — see `survey:` block. Relevance: its proposed context-driven social layer and cost re-weighting is architecturally what several VLM methods (e.g., VLM-Social-Nav, Etiquette, GSON) later implement; a defensible lineage, not a claim of influence.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue Sensors; DOI 10.3390/s24092794; pages Article 2794; URL https://doi.org/10.3390/s24092794.
- Sources: Crossref (exact title match, DOI 10.3390/s24092794).
- Version relationship: Corpus copy is the published version.
- Changed field - venue: PDF-derived 'Sensors (MDPI) 24(9):2794' -> externally verified 'Sensors'
- Changed field - pages: PDF-derived '2794 (61 pages)' -> externally verified 'Article 2794'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

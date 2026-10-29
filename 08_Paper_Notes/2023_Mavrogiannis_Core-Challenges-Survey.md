---
id: 2023_Mavrogiannis_Core-Challenges-Survey
source_pdfs: [00_Existing_Surveys/3583741.pdf]
duplicate_copies: []
related_versions: []
title: 'Core Challenges of Social Robot Navigation: A Survey'
authors: &id001 [Christoforos Mavrogiannis, Francesca Baldini, Allan Wang, Dapeng Zhao, Pete Trautman, Aaron Steinfeld, Jean Oh]
year: 2023
venue: ACM Transactions on Human-Robot Interaction
volume: '12'
issue: '3'
pages: 1-39 (Article 36)
doi: 10.1145/3583741
url: https://doi.org/10.1145/3583741
pub_status: journal; survey/review
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1145/3583741); arXiv abs page (2103.05668v2). PDF-derived basis (Stage 1): ACM THRI article with DOI (p.1).'
category: S0
folder: 00_Existing_Surveys
folder_category_match: 'Yes'
category_rationale: Critical survey of planning, behaviour-design and evaluation challenges in social navigation over three decades, with illustrative simulation analyses of evaluation conventions.
paper_type: survey
fm_used: 'No'
fm_class: [None]
fm_models: []
fm_size: NA
method_family: [literature review, illustrative simulation analysis]
roles: []
roles_evidence: {}
integration: NA
integration_rationale: Survey.
evidence: NA
evidence_rationale: Survey; illustrative simulation analyses of benchmark conventions (ORCA cooperativeness, OOD sensitivity) are not robot navigation evidence for a proposed method.
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
repro: {code: NA, code_url: NA, dataset: NA, dataset_url: NA, checkpoints: NA, prompts_published: NA, hardware_specified: NA, hyperparameters: NA, protocol_described: NA, project_page: NA, concerns: No systematic search protocol (perspective survey).}
limitations_flags: []
web_verification_required: []
cited_missing: [Rios-Martinez proxemics survey (IJSR 2015), Rudenko human motion prediction survey (IJRR 2020), Lasota safety in HRI survey, Thomaz computational HRI survey, Trautman IJRR 2015 cafeteria study, Ballbot social navigation, CROWDBOT / SPENCER projects, F-formation recognition works]
survey:
  scope: 'Social robot navigation in crowded public spaces: planning (coupled prediction and planning), behaviour design (proxemics, intentions, formations), evaluation (metrics, methodologies, simulation conventions, benchmarks), plus robot design, perception, novelty effects, robust autonomy'
  years_covered: ~1995-2022 (three decades)
  search_strategy: Not reported (expert perspective)
  inclusion: Not reported
  exclusion: Not reported
  n_papers: Not reported
  n_refs: 288
  taxonomy: 'Open challenges along three axes: planning, behaviour design, evaluation'
  taxonomy_dims: '3'
  datasets_covered: Partial (ETH/UCY and pedestrian datasets in prediction/evaluation)
  simulators_covered: Yes (ORCA-based CrowdNav-style environments, crowd simulators; critique of homogeneity, fixed attention/flexibility)
  metrics_covered: Yes (§4.1 metrics; §4.2 methodologies; calls for standardized benchmarks)
  coverage: {classical: 'Yes', human_aware: 'Yes', proxemics: 'Yes', prediction: 'Yes', imitation_learning: 'Yes', drl: 'Yes', gnn_transformer: Partial, language_models: 'No', vlm: 'No', lvlm: 'No', foundation_models: 'No', vla: 'No', real_world_deployment: 'Yes', evaluation: 'Yes'}
  stage2_coverage: {classical_proxemics: 'Yes', learning_drl: 'Yes', gnn_transformer: Partial, llm: 'No', vlm: 'No', vla: 'No', social_capability_taxonomy: Partial (behaviour-design challenges), evidence_maturity_analysis: 'No', evaluation_audit: Partial (evaluation as challenge axis), deployment_analysis: 'No', fm_reliability: NA (pre-FM), human_subject_evidence: Partial, direct_overlap_with_our_survey: 0 of our 41 direct papers cited, basis: Stage-2 manual coding from survey note coverage/taxonomy + extracted-text keyword checks (2026-10-19); overlap is a lower bound (title/arXiv-id string match + manual).}
coding: {latency_reported: NA, safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: NA, new_dataset_released: NA, real_robot: NA, human_subject_study: NA}
pdf_metadata_stage1:
  year: 2023
  authors: *id001
  venue: ACM Transactions on Human-Robot Interaction
  volume: '12'
  issue: '3'
  pages: Article 36 (39 pages)
  doi: 10.1145/3583741
  url: https://doi.org/10.1145/3583741
  pub_status: journal; survey/review
  peer_reviewed: 'Yes'
  peer_review_basis: ACM THRI article with DOI (p.1).
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: ACM Transactions on Human-Robot Interaction
  verified_doi: 10.1145/3583741
  verified_url: https://doi.org/10.1145/3583741
  verified_pages: 1-39 (Article 36)
  arxiv: 2103.05668v2
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1145/3583741)', arXiv abs page (2103.05668v2)]
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

# Core Challenges of Social Robot Navigation (Mavrogiannis et al., THRI 2023)

Page convention: PDF index (p.N).

## A. Bibliographic — ACM THRI 12(3), Article 36, April 2023, DOI 10.1145/3583741; UW, Honda Research Institute, Caltech, CMU.

## B. Position — S0; critical, perspective-driven survey; explicitly follows up Kruse 2013's call for a holistic theory.

## C. Scope — §2 planning (decoupled vs coupled prediction-planning; open problems); §3 behaviour design (proxemics, intentions/formations); §4 evaluation (metrics, methodologies, open problems); §5 conclusion with other challenges (robot design, perception, novelty effects, robust autonomy) and moving forward (p.2–27).

## D. Key messages (p.25–27) — planning in crowds is NP-hard and context-sensitive; no single behaviour theory stands out (proxemics accepted but integration unclear); ORCA-based evaluation is not necessarily informative (a naive agent can exploit cooperative ORCA agents); learning-based methods are highly sensitive to OOD testing; simulators assume homogeneity, fixed attention and flexibility; lack of standardized benchmarks; perception uncertainty and failures often ignored.

## N. Limitations (of the survey) — no systematic search; pre-FM (no language/VLM coverage).

## P. Survey analysis — see `survey:` block. Relevance: its evaluation critiques (ORCA exploitation, OOD fragility, perception assumptions) directly apply to how VLM social-navigation papers evaluate.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue ACM Transactions on Human-Robot Interaction; DOI 10.1145/3583741; pages 1-39 (Article 36); URL https://doi.org/10.1145/3583741.
- Sources: Crossref (exact title match, DOI 10.1145/3583741); arXiv abs page (2103.05668v2).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - pages: PDF-derived 'Article 36 (39 pages)' -> externally verified '1-39 (Article 36)'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

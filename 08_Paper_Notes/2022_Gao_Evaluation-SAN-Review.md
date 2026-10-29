---
id: 2022_Gao_Evaluation-SAN-Review
source_pdfs: [00_Existing_Surveys/frobt-08-721317.pdf]
duplicate_copies: []
related_versions: []
title: Evaluation of Socially-Aware Robot Navigation
authors: &id001 [Yuxiang Gao, Chien-Ming Huang]
year: 2022
venue: Frontiers in Robotics and AI
volume: '8'
issue: NA
pages: Article 721317
doi: 10.3389/frobt.2021.721317
url: https://doi.org/10.3389/frobt.2021.721317
pub_status: journal; survey/review
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.3389/frobt.2021.721317). PDF-derived basis (Stage 1): Frontiers review with editor/reviewers listed and received/accepted dates (p.1).'
category: S0
folder: 00_Existing_Surveys
folder_category_match: 'Yes'
category_rationale: Review of evaluation methods, scenarios, datasets and metrics for socially-aware navigation (177 papers).
paper_type: survey
fm_used: 'No'
fm_class: [None]
fm_models: []
fm_size: NA
method_family: [literature review, bibliometric keyword analysis]
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
repro: {code: NA, code_url: NA, dataset: NA, dataset_url: NA, checkpoints: NA, prompts_published: NA, hardware_specified: NA, hyperparameters: NA, protocol_described: 'Partial (keywords, databases, counts; not a full systematic scoping process)', project_page: NA, concerns: Authors state they did not follow a systematic-review scoping process.}
limitations_flags: []
web_verification_required: []
cited_missing: [Rios-Martinez proxemics survey (IJSR 2015), Pandey 2017 socially intelligent robots, Katyal 2021 group-aware navigation, Truong & Ngo 2018 social dynamics, Shiomi 2014 socially acceptable navigation in a mall]
survey:
  scope: 'Evaluation of socially-aware navigation: methods (case study, simulation/demonstration, lab study, field study), primitive scenarios, datasets, metrics (navigation performance, naturalness, discomfort incl. spatial models, physical and psychological safety, sociability); limitations and opportunities'
  years_covered: 2005-2021
  search_strategy: Keywords 'socially-aware navigation', 'socially-acceptable navigation', 'human-aware navigation', 'crowd-aware navigation' in ACM DL, IEEE Xplore, ScienceDirect; arXiv preprints via Google Scholar
  inclusion: Relevance to socially-aware navigation and its evaluation
  exclusion: 11 papers not addressing socially-aware robot navigation (title/abstract screening)
  n_papers: 177 (188 retrieved)
  n_refs: ~227 (author-year references counted)
  taxonomy: Evaluation methods x scenarios x datasets x metric families (performance, naturalness, discomfort, sociability)
  taxonomy_dims: '4'
  datasets_covered: Yes (pedestrian trajectory and robot datasets incl. SCAND, ETH/UCY)
  simulators_covered: Yes (CrowdNav, SocNavBench, others)
  metrics_covered: Yes (success rate, path metrics, movement similarity, smoothness, proxemic spatial models, physical/psychological safety, sociability)
  coverage: {classical: 'Yes', human_aware: 'Yes', proxemics: 'Yes', prediction: Partial, imitation_learning: Partial, drl: 'Yes', gnn_transformer: Partial, language_models: 'No', vlm: 'No', lvlm: 'No', foundation_models: 'No', vla: 'No', real_world_deployment: 'Yes', evaluation: 'Yes'}
  stage2_coverage: {classical_proxemics: 'Yes', learning_drl: 'Yes', gnn_transformer: Partial, llm: 'No', vlm: 'No', vla: 'No', social_capability_taxonomy: 'Partial (metric families: naturalness, discomfort, sociability)', evidence_maturity_analysis: 'Partial (evaluation methods: sim/lab/field, user studies)', evaluation_audit: 'Yes', deployment_analysis: 'No', fm_reliability: NA (pre-FM), human_subject_evidence: 'Yes (questionnaires, user studies)', direct_overlap_with_our_survey: 0 of our 41 direct papers cited, basis: Stage-2 manual coding from survey note coverage/taxonomy + extracted-text keyword checks (2026-10-19); overlap is a lower bound (title/arXiv-id string match + manual).}
coding: {latency_reported: NA, safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: NA, new_dataset_released: NA, real_robot: NA, human_subject_study: NA}
pdf_metadata_stage1:
  year: 2022
  authors: *id001
  venue: Frontiers in Robotics and AI, Vol. 8, Article 721317 (published 12 Jan 2022)
  volume: '8'
  issue: NA
  pages: Article 721317 (21 pages)
  doi: 10.3389/frobt.2021.721317
  url: Not reported
  pub_status: journal; survey/review
  peer_reviewed: 'Yes'
  peer_review_basis: Frontiers review with editor/reviewers listed and received/accepted dates (p.1).
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: Frontiers in Robotics and AI
  verified_doi: 10.3389/frobt.2021.721317
  verified_url: https://doi.org/10.3389/frobt.2021.721317
  verified_pages: Article 721317
  arxiv: NA
  version_relationship: Corpus copy is the published version
  sources: ['Crossref (exact title match, DOI 10.3389/frobt.2021.721317)']
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

# Evaluation of Socially-Aware Robot Navigation (Gao & Huang, Front. Robot. AI 2022)

Page convention: PDF index (p.N).

## A. Bibliographic — Frontiers in Robotics and AI 8:721317, published 12 Jan 2022, DOI 10.3389/frobt.2021.721317; Johns Hopkins University. (File label "2021" reflects volume year.)

## B. Position — S0; evaluation-focused review complementary to Francis et al.

## C. Scope — §2 methodology (keywords/databases; 188 → 177 papers; bibliometric co-occurrence network; venue table); §3 evaluation methods, primitive scenarios, datasets; §4 metrics (navigation performance, behavioural naturalness, human discomfort incl. spatial models, physical and psychological safety, sociability); §5 limitations and open problems (diverse dynamic human models; robots of different forms); §6 conclusion (p.2–16).

## D. Key messages — no agreed evaluation protocols; simulation enables agile comparison while lab/field studies reveal interaction insights; combine objective, subjective and behavioural metrics (p.15).

## N. Limitations (of the survey) — not a full systematic review (stated); pre-FM.

## P. Survey analysis — see `survey:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue Frontiers in Robotics and AI; DOI 10.3389/frobt.2021.721317; pages Article 721317; URL https://doi.org/10.3389/frobt.2021.721317.
- Sources: Crossref (exact title match, DOI 10.3389/frobt.2021.721317).
- Version relationship: Corpus copy is the published version.
- Changed field - venue: PDF-derived 'Frontiers in Robotics and AI, Vol. 8, Article 721317 (published 12 Jan 2022)' -> externally verified 'Frontiers in Robotics and AI'
- Changed field - pages: PDF-derived 'Article 721317 (21 pages)' -> externally verified 'Article 721317'
- Changed field - url: PDF-derived 'Not reported' -> externally verified 'https://doi.org/10.3389/frobt.2021.721317'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

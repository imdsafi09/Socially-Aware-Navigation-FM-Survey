---
id: 2024_Mirsky_Conflict-Avoidance-Survey
source_pdfs: [00_Existing_Surveys/reuth_hri2024.pdf]
duplicate_copies: []
related_versions: []
title: Conflict Avoidance in Social Navigation—a Survey
authors: &id001 [Reuth Mirsky, Xuesu Xiao, Justin Hart, Peter Stone]
year: 2024
venue: ACM Transactions on Human-Robot Interaction
volume: '13'
issue: '1'
pages: 1-36 (Article 13)
doi: 10.1145/3647983
url: https://doi.org/10.1145/3647983
pub_status: journal; survey/review
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1145/3647983); arXiv abs page (2106.12113v3). PDF-derived basis (Stage 1): ACM THRI article with DOI, March 2024 (p.1).'
category: S0
folder: 00_Existing_Surveys
folder_category_match: 'Yes'
category_rationale: Survey of conflict avoidance in human-centric social navigation with a 7-attribute taxonomy, model/algorithm tables and evaluation review.
paper_type: survey
fm_used: 'No'
fm_class: [None]
fm_models: []
fm_size: NA
method_family: [literature review, citation snowballing]
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
repro: {code: NA, code_url: NA, dataset: NA, dataset_url: NA, checkpoints: NA, prompts_published: NA, hardware_specified: NA, hyperparameters: NA, protocol_described: Partial (snowballing from Kruse 2013 and Charalampous 2017 via Google Scholar; study flow diagram Fig.1), project_page: NA, concerns: 'Snowballing only; inclusion requires real-world interaction (R3), so simulation-only work is de-emphasized.'}
limitations_flags: []
web_verification_required: []
cited_missing: [Rios-Martinez proxemics survey (IJSR 2015), Social Momentum (Mavrogiannis), Hoogendoorn & Bovy three-tier navigation model, López turn-prediction survey, Xiao et al. ML for motion planning survey (2022), Bartneck Godspeed questionnaire, Barchard perceived social intelligence (THRI 2020)]
survey:
  scope: Conflict avoidance (situations where robot and human would collide without a change in speed or direction) in human-centric social navigation, mostly at the operational level; models (multiagent, psychology-inspired, physics-based), algorithms (incl. inferring human trajectories), evaluation
  years_covered: Historical (Grey Walter) to ~2023
  search_strategy: Start from existing surveys (Kruse 2013; Charalampous 2017); collect their references and citing papers via Google Scholar; iterate forward/backward snowballing until no new papers met requirements
  inclusion: R1 autonomously navigating agent with reachable goal; R2 humans/animals present; R3 real-world interaction (63 of 175 citations do not meet all three but are included as fundamental or surveys)
  exclusion: Teleoperation, multi-robot-only, simulation-only and graphics crowds (unless fundamental)
  n_papers: Not reported as a single number (175 citations, 63 not meeting all criteria)
  n_refs: 175
  taxonomy: Robot role (reactor/initiator/both/neither); number of agents (absolute/density); observability; motion control (SFM/ORCA/ROS/human/other); communication (none/indirect/direct); experiment type (sim/lab/in-the-wild/survey); agent type
  taxonomy_dims: 7 attributes
  datasets_covered: Partial
  simulators_covered: Partial (benchmarks referenced in §5)
  metrics_covered: 'Yes (§5: interaction evaluation, algorithmic properties, user experience, missing/cursory evaluation)'
  coverage: {classical: 'Yes', human_aware: 'Yes', proxemics: 'Yes', prediction: 'Yes', imitation_learning: Partial, drl: 'Yes', gnn_transformer: 'No', language_models: 'No', vlm: 'No', lvlm: 'No', foundation_models: 'No', vla: 'No', real_world_deployment: 'Yes', evaluation: 'Yes'}
  stage2_coverage: {classical_proxemics: 'Yes', learning_drl: 'Yes', gnn_transformer: 'No', llm: 'No', vlm: 'No', vla: 'No', social_capability_taxonomy: Partial (conflict-scenario dimensions), evidence_maturity_analysis: Partial (per-paper experiment type sim/lab/field), evaluation_audit: 'Yes', deployment_analysis: 'No', fm_reliability: NA (pre-FM), human_subject_evidence: Partial, direct_overlap_with_our_survey: 0 of our 41 direct papers cited, basis: Stage-2 manual coding from survey note coverage/taxonomy + extracted-text keyword checks (2026-10-19); overlap is a lower bound (title/arXiv-id string match + manual).}
coding: {latency_reported: NA, safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: NA, new_dataset_released: NA, real_robot: NA, human_subject_study: NA}
pdf_metadata_stage1:
  year: 2024
  authors: *id001
  venue: ACM Transactions on Human-Robot Interaction (file name says 'hri2024' but the paper is the THRI journal article)
  volume: '13'
  issue: '1'
  pages: Article 13 (36 pages)
  doi: 10.1145/3647983
  url: https://doi.org/10.1145/3647983
  pub_status: journal; survey/review
  peer_reviewed: 'Yes'
  peer_review_basis: ACM THRI article with DOI, March 2024 (p.1).
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: ACM Transactions on Human-Robot Interaction
  verified_doi: 10.1145/3647983
  verified_url: https://doi.org/10.1145/3647983
  verified_pages: 1-36 (Article 13)
  arxiv: 2106.12113v3
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1145/3647983)', arXiv abs page (2106.12113v3)]
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

# Conflict Avoidance in Social Navigation—a Survey (Mirsky, Xiao, Hart, Stone — THRI 2024)

Page convention: PDF index (p.N).

## A. Bibliographic — ACM THRI 13(1), Article 13, March 2024, DOI 10.1145/3647983; Bar-Ilan, GMU, UT Austin. The corpus file name ("reuth_hri2024") suggests HRI 2024, but the PDF is the THRI journal article.

## B. Position — S0; narrower but more operational than other pre-FM surveys; same group as SCAND, VLM-Social-Nav and Social-LLaVA.

## C. Scope — definition of conflict (Def.1) and three requirements R1–R3 (p.2–3); related surveys (p.3–4); taxonomy (Table 1, p.6) and additional concepts (collision types, context awareness, semantic mapping, reactions to robots vs humans, social cues, groups) (§2.2); models (§3); algorithms (§4); evaluation (§5); discussion and checklist (§6, p.27–29).

## D. Key messages — checklist: place work in taxonomy, report reliability details, human familiarity, context, success definition, metrics (p.28). Open problems: standardized metrics/domains, context-aware navigation, group understanding, lifelong adaptive navigation; two gaps — user-experience evaluation is underused; no agreed criteria for what constitutes a conflict (p.28–29).

## N. Limitations (of the survey) — snowballing-only search; restricted to conflict avoidance; pre-FM.

## P. Survey analysis — see `survey:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue ACM Transactions on Human-Robot Interaction; DOI 10.1145/3647983; pages 1-36 (Article 13); URL https://doi.org/10.1145/3647983.
- Sources: Crossref (exact title match, DOI 10.1145/3647983); arXiv abs page (2106.12113v3).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - venue: PDF-derived 'ACM Transactions on Human-Robot Interaction (file name says 'hri2024' but the paper is the THRI journal article)' -> externally verified 'ACM Transactions on Human-Robot Interaction'
- Changed field - pages: PDF-derived 'Article 13 (36 pages)' -> externally verified '1-36 (Article 13)'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

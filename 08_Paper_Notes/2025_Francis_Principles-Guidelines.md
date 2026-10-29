---
id: 2025_Francis_Principles-Guidelines
source_pdfs: [00_Existing_Surveys/3700599.pdf]
duplicate_copies: []
related_versions: ['arXiv:2306.16740 (2023) cited by Arena 4.0; AAAI 2023 Spring Symposium excerpt (cited in paper)']
title: Principles and Guidelines for Evaluating Social Robot Navigation Algorithms
authors: &id001 [Anthony Francis, Claudia Pérez-D'Arpino, Chengshu Li, Fei Xia, Alexandre Alahi, Rachid Alami, Aniket Bera, Abhijat Biswas, Joydeep Biswas, Rohan Chandra, et al. (31 authors), Alexander Toshev, Roberto Martín-Martín]
year: 2025
venue: ACM Transactions on Human-Robot Interaction
volume: '14'
issue: '2'
pages: 1-65
doi: 10.1145/3700599
url: https://doi.org/10.1145/3700599
pub_status: journal; evaluation guidelines/review
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1145/3700599); arXiv abs page (2306.16740v4). PDF-derived basis (Stage 1): ACM THRI with DOI (p.1); corpus copy appears to be accepted/online-first version without volume/issue (year 2024 copyright vs 2025 file label).'
category: S0
folder: 00_Existing_Surveys
folder_category_match: Partial
category_rationale: Community consensus paper defining social navigation principles and evaluation guidelines (metrics, scenarios, benchmarks, datasets, simulators) with an extensive review; not a conventional literature survey.
paper_type: evaluation-guideline
fm_used: 'No'
fm_class: [None]
fm_models: []
fm_size: NA
method_family: [consensus guidelines, literature review, metrics API design]
roles: []
roles_evidence: {}
integration: NA
integration_rationale: Guidelines paper.
evidence: NA
evidence_rationale: No experiments.
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
repro: {code: Proposed common metrics API (described), code_url: Not reported, dataset: NA, dataset_url: NA, checkpoints: NA, prompts_published: NA, hardware_specified: NA, hyperparameters: NA, protocol_described: NA, project_page: 'https://sites.google.com/view/socialnavigationsymposium/home', concerns: Consensus-based; no systematic search.}
limitations_flags: []
web_verification_required: [Final THRI volume/issue/year (2024 vs 2025).]
cited_missing: [Social Navigation Symposium position papers, SEAN 2.0, HuNavSim, SocialGym 2.0, iGibson social nav challenge, Habitat 3.0, Pirk protocol for validating social navigation policies, Tsoi 'How do robot experts measure success of social navigation' (HRI 2024)]
survey:
  scope: Definition and principles of social navigation; scientific questions; taxonomy of evaluation; guidelines for metrics, scenarios, benchmarks, datasets, simulators; common metrics API
  years_covered: Literature to ~2023-2024
  search_strategy: Not reported (consensus from Social Navigation Symposium working groups)
  inclusion: Not reported
  exclusion: Not reported
  n_papers: Not reported
  n_refs: 173
  taxonomy: Principles P1-P8 (safety, comfort, legibility, politeness, social norms/competency, agent understanding, proactivity, contextual appropriateness); guideline sets R1-R4 (general), M1-M8 (metrics), N1-N8 (scenarios incl. scenario cards), B1-B6 (benchmarks), D1-D8 (datasets), S1-S9 (simulators)
  taxonomy_dims: Principles x evaluation instruments
  datasets_covered: Yes (SCAND, THOR, JRDB, ETH/UCY, others)
  simulators_covered: Yes (SEAN, SocNavBench, CrowdNav, Gazebo-based, Habitat, iGibson, others)
  metrics_covered: Yes (algorithmic, learned, human-survey metrics; parameterization in context; limitations of social metrics)
  coverage: {classical: 'Yes', human_aware: 'Yes', proxemics: 'Yes', prediction: Partial, imitation_learning: 'Yes', drl: 'Yes', gnn_transformer: 'No', language_models: 'No', vlm: 'No', lvlm: 'No', foundation_models: 'No', vla: 'No', real_world_deployment: 'Yes', evaluation: 'Yes'}
  stage2_coverage: {classical_proxemics: 'Yes', learning_drl: 'Yes', gnn_transformer: 'No', llm: 'No', vlm: 'No', vla: 'No', social_capability_taxonomy: Yes (principles P1-P8), evidence_maturity_analysis: 'No', evaluation_audit: Yes (metric guidelines M1-M8), deployment_analysis: 'No', fm_reliability: NA (pre-FM), human_subject_evidence: Yes (human-study guidelines), direct_overlap_with_our_survey: 0 of our 41 direct papers cited, basis: Stage-2 manual coding from survey note coverage/taxonomy + extracted-text keyword checks (2026-10-19); overlap is a lower bound (title/arXiv-id string match + manual).}
coding: {latency_reported: NA, safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: NA, new_dataset_released: NA, real_robot: NA, human_subject_study: NA}
pdf_metadata_stage1:
  year: 2025
  authors: *id001
  venue: ACM Transactions on Human-Robot Interaction (DOI 10.1145/3700599; copyright 2024; volume/issue not printed in corpus copy)
  volume: Not reported
  issue: Not reported
  pages: 63 (PDF)
  doi: 10.1145/3700599
  url: https://doi.org/10.1145/3700599
  pub_status: journal; evaluation guidelines/review
  peer_reviewed: 'Yes'
  peer_review_basis: ACM THRI with DOI (p.1); corpus copy appears to be accepted/online-first version without volume/issue (year 2024 copyright vs 2025 file label).
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: ACM Transactions on Human-Robot Interaction
  verified_doi: 10.1145/3700599
  verified_url: https://doi.org/10.1145/3700599
  verified_pages: 1-65
  arxiv: 2306.16740v4
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1145/3700599)', arXiv abs page (2306.16740v4)]
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

# Principles and Guidelines for Evaluating Social Robot Navigation (Francis, Pérez-D'Arpino et al., THRI)

Page convention: PDF index (p.N).

## A. Bibliographic — ACM THRI, DOI 10.1145/3700599 (© 2024; corpus copy lacks volume/issue); 31 authors from academia and industry; outcome of the Social Navigation Symposium; arXiv 2306.16740 cited by Arena 4.0.

## B. Position — S0 (guidelines). The de facto community standard for social navigation evaluation; directly provides the yardstick for assessing VLM social-navigation evaluation practice.

## C. Content — definition: a robot that achieves its goals while modifying behaviour to enable others to achieve theirs (p.54); principles P1–P8; guideline sets R, M, N, B, D, S (Fig.1, p.3); benchmark strengths/limitations (scalable benchmarks not grounded in human data vs human-data benchmarks hard to scale) (p.~45); limitations of social metrics (§6.2.4); common metrics API (conclusions, p.54).

## D. Key recommendations relevant to VLM work — report widely used metrics (M1); validate algorithmically first (M2); parameterize metrics in context (M3); use validated human surveys (M5); scenario cards (N8); ground human evaluations in human data (B5); validate instruments (B6); use robots and diverse platforms for datasets (D4–D5); privacy (D8).

## N. Limitations (of the paper) — consensus-driven, not a systematic review; does not address language/foundation-model navigation.

## P. Survey analysis — see `survey:` block. Folder_category_match Partial because it is primarily a guidelines paper.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue ACM Transactions on Human-Robot Interaction; DOI 10.1145/3700599; pages 1-65; URL https://doi.org/10.1145/3700599.
- Sources: Crossref (exact title match, DOI 10.1145/3700599); arXiv abs page (2306.16740v4).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - venue: PDF-derived 'ACM Transactions on Human-Robot Interaction (DOI 10.1145/3700599; copyright 2024; volume/issue not printed in corpus copy)' -> externally verified 'ACM Transactions on Human-Robot Interaction'
- Changed field - volume: PDF-derived 'Not reported' -> externally verified '14'
- Changed field - issue: PDF-derived 'Not reported' -> externally verified '2'
- Changed field - pages: PDF-derived '63 (PDF)' -> externally verified '1-65'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

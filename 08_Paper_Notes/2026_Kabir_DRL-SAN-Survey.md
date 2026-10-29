---
id: 2026_Kabir_DRL-SAN-Survey
source_pdfs: [00_Existing_Surveys/s10489-025-06982-5.pdf]
duplicate_copies: []
related_versions: []
title: 'Socially aware navigation for mobile robots: a survey on deep reinforcement learning approaches'
authors: &id001 [Ibrahim Khalil Kabir, Muhammad Faizan Mysorewala]
year: 2026
venue: Applied Intelligence
volume: '56'
issue: '1'
pages: Article 38
doi: 10.1007/s10489-025-06982-5
url: https://doi.org/10.1007/s10489-025-06982-5
pub_status: journal; survey/review
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1007/s10489-025-06982-5); arXiv abs page (2512.00049v1). PDF-derived basis (Stage 1): Springer Applied Intelligence with received/accepted/published dates and DOI (p.1).'
category: S0
folder: 00_Existing_Surveys
folder_category_match: 'Yes'
category_rationale: Survey of DRL-based socially aware navigation by RL family and network architecture, with evaluation mechanisms and challenges; no FM coverage.
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
repro: {code: NA, code_url: NA, dataset: NA, dataset_url: NA, checkpoints: NA, prompts_published: NA, hardware_specified: NA, hyperparameters: NA, protocol_described: Partial (databases and search string; no screening counts), project_page: NA, concerns: Search string mixes OR/AND without parentheses; no inclusion/exclusion counts; 'first unified taxonomy' claim not verifiable.}
limitations_flags: []
web_verification_required: []
cited_missing: [SocialGym (Holtz & Biswas 2022), DS-RNN (Liu 2021), RGL (Chen 2020), LSTM-RL (Everett 2018), Intention-aware DRL navigation works, SRPB benchmark (Karwowski)]
survey:
  scope: 'DRL-based socially aware navigation: reactive/proactive/learning approaches; value-, policy- and actor-critic DRL; reward design; discrete vs continuous spaces; multi-robot; network architectures (MLP, GNN, RNN, CNN, Transformer); metrics, datasets, simulators, benchmarks; standardization; challenges and future directions'
  years_covered: Not explicitly stated (DRL era ~2016-2025)
  search_strategy: Google Scholar, IEEE Xplore, Scopus; terms 'Socially-aware' OR 'Human-aware' OR 'crowd-aware' AND 'Deep reinforcement learning' AND 'Mobile Robot'
  inclusion: Not reported beyond search terms
  exclusion: Not reported
  n_papers: '''over 100 DRL-based SAN works'' (stated)'
  n_refs: ~160 (numbered list)
  taxonomy: Algorithmic (value-based / policy-based / actor-critic) x neural architecture (FF, GNN, RNN, CNN, Transformer); comparison attributes incl. comfort, attention, physical input, context awareness, intention prediction
  taxonomy_dims: 2 primary + comparison attributes
  datasets_covered: Yes (ETH, UCY, SCAND, others)
  simulators_covered: Yes (CrowdNav, Gazebo, SocialGym, SEAN etc.)
  metrics_covered: Yes (§4.1; calls for standardized social metrics)
  coverage: {classical: Partial, human_aware: 'Yes', proxemics: 'Yes', prediction: 'Yes', imitation_learning: Partial, drl: 'Yes', gnn_transformer: 'Yes', language_models: 'No', vlm: 'No', lvlm: 'No', foundation_models: 'No', vla: 'No', real_world_deployment: Partial, evaluation: 'Yes'}
  stage2_coverage: {classical_proxemics: Partial, learning_drl: 'Yes', gnn_transformer: 'Yes', llm: Partial (incidental), vlm: 'No', vla: 'No', social_capability_taxonomy: 'Partial (comparison attributes: comfort, intention, context)', evidence_maturity_analysis: 'No', evaluation_audit: Partial, deployment_analysis: 'No', fm_reliability: 'No', human_subject_evidence: 'No', direct_overlap_with_our_survey: '1 of our 41 direct papers cited: 2024_Wang_SALM', basis: Stage-2 manual coding from survey note coverage/taxonomy + extracted-text keyword checks (2026-10-19); overlap is a lower bound (title/arXiv-id string match + manual).}
coding: {latency_reported: NA, safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: NA, new_dataset_released: NA, real_robot: NA, human_subject_study: NA}
pdf_metadata_stage1:
  year: 2026
  authors: *id001
  venue: Applied Intelligence (Springer), 56:38 (published online 9 Jan 2026; accepted 27 Oct 2025)
  volume: '56'
  issue: NA
  pages: Article 38 (31 pages)
  doi: 10.1007/s10489-025-06982-5
  url: https://doi.org/10.1007/s10489-025-06982-5
  pub_status: journal; survey/review
  peer_reviewed: 'Yes'
  peer_review_basis: Springer Applied Intelligence with received/accepted/published dates and DOI (p.1).
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: Applied Intelligence
  verified_doi: 10.1007/s10489-025-06982-5
  verified_url: https://doi.org/10.1007/s10489-025-06982-5
  verified_pages: Article 38
  arxiv: 2512.00049v1
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1007/s10489-025-06982-5)', arXiv abs page (2512.00049v1)]
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

# Socially Aware Navigation for Mobile Robots: A Survey on DRL Approaches (Kabir & Mysorewala, Applied Intelligence 2026)

Page convention: PDF index (p.N).

## A. Bibliographic — Applied Intelligence 56:38 (2026), DOI 10.1007/s10489-025-06982-5; received 21 Feb 2025, accepted 27 Oct 2025, published online 9 Jan 2026; KFUPM.

## B. Position — S0; most recent DRL-focused survey; contains no LLM/VLM/foundation-model coverage (keyword hits for "foundation" are generic usage).

## C. Scope — §1 intro and prior surveys (Table 1); §2 learning in SAN (approaches, DRL evolution, value/policy/actor-critic classification, reward design, state/action discreteness, multi-robot); §3 neural architectures; §4 evaluation (metrics, datasets, simulators, benchmarks, standardization); §5 challenges (uncertainty, real-world applicability, computational complexity, generalization, scalability, reproducibility) and 11 future directions; §6 conclusion (p.1–26).

## D. Key messages — non-uniform evaluation, lack of standardized social metrics, computational burden and sim-to-real gap hinder DRL SAN; future: efficiency, generalization, scalability, heterogeneous human models (age, personality, gender, culture), uncertainty-aware reward inference, cross-embodiment transfer, cooperative navigation, realistic simulators, interpretable hybrid methods, ethics/HRI principles (p.24–25).

## N. Limitations (of the survey) — weak search protocol; no FM coverage despite 2025–2026 publication.

## P. Survey analysis — see `survey:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue Applied Intelligence; DOI 10.1007/s10489-025-06982-5; pages Article 38; URL https://doi.org/10.1007/s10489-025-06982-5.
- Sources: Crossref (exact title match, DOI 10.1007/s10489-025-06982-5); arXiv abs page (2512.00049v1).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - venue: PDF-derived 'Applied Intelligence (Springer), 56:38 (published online 9 Jan 2026; accepted 27 Oct 2025)' -> externally verified 'Applied Intelligence'
- Changed field - issue: PDF-derived 'NA' -> externally verified '1'
- Changed field - pages: PDF-derived 'Article 38 (31 pages)' -> externally verified 'Article 38'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

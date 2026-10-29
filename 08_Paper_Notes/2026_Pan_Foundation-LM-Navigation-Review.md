---
id: 2026_Pan_Foundation-LM-Navigation-Review
source_pdfs: [00_Existing_Surveys/3802539.pdf]
duplicate_copies: []
related_versions: []
title: 'Robot Navigation via Foundation Language Models: A Review'
authors: &id001 [Haotian Pan, Shibo Huang, Jian Yang, Jinpeng Mi, Ke Li, Xiong You, Peidong Liang, Jinbo Yang, Yingjie Liu, Jianfeng Zhang, Muyu Wang, Jie Yang, Xinyu Zhang, Lijun Zhao, Mingsong Chen, Jie Zhou, Xian Wei]
year: 2026
venue: ACM Computing Surveys
volume: '58'
issue: '11'
pages: 1-38 (Article 291)
doi: 10.1145/3802539
url: https://doi.org/10.1145/3802539
pub_status: journal; survey/review
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1145/3802539). PDF-derived basis (Stage 1): ACM Computing Surveys article with DOI, April 2026 (p.1).'
category: S0
folder: 00_Existing_Surveys
folder_category_match: 'Yes'
category_rationale: Systematic review of LLM-based robot navigation (perception, planning, control, interaction, coordination), datasets, simulators and metrics; social navigation essentially absent.
paper_type: survey
fm_used: 'No'
fm_class: [None]
fm_models: []
fm_size: NA
method_family: [systematic literature review]
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
repro: {code: NA, code_url: NA, dataset: NA, dataset_url: NA, checkpoints: NA, prompts_published: NA, hardware_specified: NA, hyperparameters: NA, protocol_described: 'Yes (databases, keywords, time range, inclusion/exclusion, counts)', project_page: NA, concerns: Abstract lists five taxonomy themes (incl. coordination) while methodology lists four dimensions; arXiv inclusion based on 'widely cited' (subjective).}
limitations_flags: []
web_verification_required: []
cited_missing: [NavGPT (in corpus), LM-Nav (in corpus), VLMaps (in corpus), SayCan (in corpus), VoxPoser (in corpus), PaLM-E (in corpus), RT-2 (in corpus), ESC, L3MVN, NaVid, Uni-NaVid, NavCoT, MapGPT]
survey:
  scope: LLM-based robot navigation across perception (semantic mapping), planning, control, interaction (instruction/HRI), and multi-robot coordination; datasets, simulators, metrics; challenges
  years_covered: 2018-2026
  search_strategy: ACM DL, IEEE Xplore, Web of Science; keywords incl. 'large language model', 'robot navigation', 'embodied intelligence', 'instruction following', 'semantic mapping', 'multi-robot coordination', 'navigation under uncertainty' combined with Boolean operators
  inclusion: Uses LLMs or comparable pre-trained LMs; navigation behaviour (sim or real); natural language/semantic comprehension; well-defined metrics
  exclusion: Pure NLP; theory without validation; standard-simulation results without task details; non-peer-reviewed except widely cited arXiv
  n_papers: 70 (39 method papers + 31 dataset/benchmark papers; ~300 records -> 240 after deduplication)
  n_refs: 168
  taxonomy: Perception / planning / control / interaction (+ coordination per abstract); RQ1-RQ4
  taxonomy_dims: 4-5 functional themes x traditional vs LLM comparison
  datasets_covered: 'Yes (VLN/ObjectNav datasets: R2R, RxR, REVERIE, HM3D etc.)'
  simulators_covered: Yes (Habitat, Matterport3D, AI2-THOR, Gazebo, etc.)
  metrics_covered: Yes (SR, SPL, NE, etc.; success rate vs environment type)
  coverage: {classical: Partial, human_aware: 'No', proxemics: 'No', prediction: 'No', imitation_learning: Partial, drl: Partial, gnn_transformer: Partial, language_models: 'Yes', vlm: 'Yes', lvlm: Partial, foundation_models: 'Yes', vla: Partial, real_world_deployment: Partial, evaluation: 'Yes'}
  stage2_coverage: {classical_proxemics: Partial (classical only; no proxemics), learning_drl: Partial, gnn_transformer: Partial, llm: 'Yes', vlm: 'Yes', vla: Partial, social_capability_taxonomy: No (not social-navigation specific), evidence_maturity_analysis: 'No', evaluation_audit: Partial, deployment_analysis: Partial (latency discussed), fm_reliability: Partial (hallucination discussed), human_subject_evidence: 'No', direct_overlap_with_our_survey: '2 of our 41 direct papers cited: 2024_Wang_SALM; 2025_Weerakoon_BehAV', basis: Stage-2 manual coding from survey note coverage/taxonomy + extracted-text keyword checks (2026-10-19); overlap is a lower bound (title/arXiv-id string match + manual).}
coding: {latency_reported: NA, safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: NA, new_dataset_released: NA, real_robot: NA, human_subject_study: NA}
pdf_metadata_stage1:
  year: 2026
  authors: *id001
  venue: ACM Computing Surveys
  volume: '58'
  issue: '11'
  pages: Article 291 (38 pages)
  doi: 10.1145/3802539
  url: https://doi.org/10.1145/3802539
  pub_status: journal; survey/review
  peer_reviewed: 'Yes'
  peer_review_basis: ACM Computing Surveys article with DOI, April 2026 (p.1).
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: ACM Computing Surveys
  verified_doi: 10.1145/3802539
  verified_url: https://doi.org/10.1145/3802539
  verified_pages: 1-38 (Article 291)
  arxiv: NA
  version_relationship: Corpus copy is the published version
  sources: ['Crossref (exact title match, DOI 10.1145/3802539)']
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

# Robot Navigation via Foundation Language Models: A Review (Pan et al., ACM CSUR 2026)

Page convention: PDF index (p.N).

## A. Bibliographic — ACM Computing Surveys 58(11), Article 291, April 2026, DOI 10.1145/3802539; ECNU and others.

## B. Position — S0; the only systematic FM-navigation review in folder 00, but it does not address social navigation (only six mentions of social/crowd/pedestrian; "socially aware motion planning based on RL" appears once in background, p.~6).

## C. Scope — §2 background (LLMs, robot navigation); §3 methodology (search, inclusion/exclusion, RQ1–RQ4); §4 LLMs in navigation (perception, planning, control, interaction); §5 datasets/simulators; §6 statistical comparisons and challenges; §7 conclusion (p.2–6 and beyond).

## D. Key messages — LLMs improve generalization in perception, reasoning, planning and instruction following; challenges include inference latency/real-time limits on edge devices, lack of safety/feasibility guarantees requiring external optimizers, hallucination, sim-to-real (text p.~13–25).

## N. Limitations (of the survey) — social navigation essentially out of scope; taxonomy count inconsistent between abstract and methodology.

## P. Survey analysis — see `survey:` block. Relevance: establishes that FM-navigation reviews and social-navigation surveys remained largely disjoint until the Cai 2026 survey.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue ACM Computing Surveys; DOI 10.1145/3802539; pages 1-38 (Article 291); URL https://doi.org/10.1145/3802539.
- Sources: Crossref (exact title match, DOI 10.1145/3802539).
- Version relationship: Corpus copy is the published version.
- Changed field - pages: PDF-derived 'Article 291 (38 pages)' -> externally verified '1-38 (Article 291)'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

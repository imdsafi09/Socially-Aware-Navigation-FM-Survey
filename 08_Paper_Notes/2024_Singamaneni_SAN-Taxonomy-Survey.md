---
id: 2024_Singamaneni_SAN-Taxonomy-Survey
source_pdfs: [00_Existing_Surveys/2807-A-survey-on-socially-aware-robot-navigation_-taxonomy-and-future-challenges.pdf]
duplicate_copies: []
related_versions: ['Published: The International Journal of Robotics Research, 2024, article 02783649241230562 (per Arena 4.0 reference list); corpus copy is arXiv:2311.06922v3 (12 Feb 2024)']
title: 'A Survey on Socially Aware Robot Navigation: Taxonomy and Future Challenges'
authors: &id001 [Phani Teja Singamaneni, Pilar Bachiller-Burgos, Luis J. Manso, Anaís Garrell, Alberto Sanfeliu, Anne Spalanzani, Rachid Alami]
year: 2024
venue: The International Journal of Robotics Research
volume: '43'
issue: '10'
pages: 1533-1572
doi: 10.1177/02783649241230562
url: https://doi.org/10.1177/02783649241230562
pub_status: journal; survey/review (corpus copy preprint)
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1177/02783649241230562); arXiv abs page (2311.06922v4). PDF-derived basis (Stage 1): Corpus copy arXiv v3; Arena 4.0 (corpus) cites IJRR 2024. File name prefix ''2807-'' unexplained. WEB_VERIFICATION_REQUIRED.'
category: S0
folder: 00_Existing_Surveys
folder_category_match: 'Yes'
category_rationale: Large taxonomy-based survey (193 articles, past 10 years) of socially aware navigation across ground, aerial and aquatic robots, planning, situation awareness, evaluation/tools.
paper_type: survey
fm_used: 'No'
fm_class: [None]
fm_models: []
fm_size: NA
method_family: [literature review, deductive thematic analysis]
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
repro: {code: NA, code_url: NA, dataset: NA, dataset_url: NA, checkpoints: NA, prompts_published: NA, hardware_specified: NA, hyperparameters: NA, protocol_described: 'Partial (search query, sources, exclusion criteria, thematic coding)', project_page: NA, concerns: No PRISMA flow counts beyond '>200 collected' and 193 retained.}
limitations_flags: []
web_verification_required: [IJRR 2024 volume/issue/DOI; meaning of file name prefix '2807-'.]
cited_missing: [Rios-Martinez proxemics survey (IJSR 2015), Rudenko human motion prediction survey (IJRR 2020), Honig person-following review (2018), Perception-Intention-Action model (Dominguez-Vidal 2023), CoHAN, SEAN 2.0, SocNavBench (in corpus), Francis principles (in corpus as THRI 2025)]
survey:
  scope: Socially aware navigation for ground, aerial and aquatic robots incl. AVs and PMVs; planning and decision-making; situation awareness; evaluation and tools; prediction; future challenges
  years_covered: ~2013-2023 (past 10 years)
  search_strategy: IEEE Xplore, ACM DL, Google Scholar; query ('social' OR 'human-aware') AND 'navigation' AND ('robot' OR 'autonomous vehicle' OR 'drone')
  inclusion: Socially aware navigation as core topic; distinctive contributions; last 10 years
  exclusion: (a) SAN not core topic; (b) small incremental contribution over covered work
  n_papers: 193 tagged articles (>200 collected)
  n_refs: 247
  taxonomy: 'Four faceted taxonomies: robot type; planning and decision-making (communication, task types, negotiation, local motion, global decisions); situation awareness and assessment (environment, methods, agents, social norms); evaluation and tools'
  taxonomy_dims: '4'
  datasets_covered: Yes (pedestrian/robot datasets incl. SCAND, ETH/UCY)
  simulators_covered: Yes (SEAN, SocNavBench, Gazebo, others)
  metrics_covered: Yes (objective and subjective metrics, user studies)
  coverage: {classical: 'Yes', human_aware: 'Yes', proxemics: 'Yes', prediction: 'Yes', imitation_learning: 'Yes', drl: 'Yes', gnn_transformer: Partial, language_models: 'No', vlm: 'No', lvlm: 'No', foundation_models: 'No', vla: 'No', real_world_deployment: 'Yes', evaluation: 'Yes'}
  stage2_coverage: {classical_proxemics: 'Yes', learning_drl: 'Yes', gnn_transformer: Partial, llm: 'No', vlm: 'No', vla: 'No', social_capability_taxonomy: Partial (situation-awareness / planning facets), evidence_maturity_analysis: 'No', evaluation_audit: Partial, deployment_analysis: 'No', fm_reliability: NA (pre-FM), human_subject_evidence: Partial, direct_overlap_with_our_survey: 0 of our 41 direct papers cited, basis: Stage-2 manual coding from survey note coverage/taxonomy + extracted-text keyword checks (2026-10-19); overlap is a lower bound (title/arXiv-id string match + manual).}
coding: {latency_reported: NA, safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: NA, new_dataset_released: NA, real_robot: NA, human_subject_study: NA}
pdf_metadata_stage1:
  year: 2024
  authors: *id001
  venue: IJRR 2024 (per citation); corpus copy arXiv v3
  volume: Not reported
  issue: Not reported
  pages: 34 (PDF)
  doi: Not printed (IJRR id 02783649241230562 per citation)
  url: Not reported
  pub_status: journal; survey/review (corpus copy preprint)
  peer_reviewed: 'Yes'
  peer_review_basis: Corpus copy arXiv v3; Arena 4.0 (corpus) cites IJRR 2024. File name prefix '2807-' unexplained. WEB_VERIFICATION_REQUIRED.
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: The International Journal of Robotics Research
  verified_doi: 10.1177/02783649241230562
  verified_url: https://doi.org/10.1177/02783649241230562
  verified_pages: 1533-1572
  arxiv: 2311.06922v4
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1177/02783649241230562)', arXiv abs page (2311.06922v4)]
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

# A Survey on Socially Aware Robot Navigation: Taxonomy and Future Challenges (Singamaneni et al., IJRR 2024)

Page convention: PDF index (p.N).

## A. Bibliographic — corpus copy arXiv:2311.06922v3 (12 Feb 2024); LAAS-CNRS, Extremadura, Aston, IRI-CSIC-UPC, Inria; cited as IJRR 2024.

## B. Position — S0; most systematic pre-FM survey in corpus (explicit query and exclusion criteria, 193 articles).

## C. Scope — definition of socially aware navigation (minimal: detect humans as special agents; minimize disturbance) (p.2); article collection (p.2); previous surveys (p.2–3); four taxonomies (p.3+); robots, planning, situation awareness, evaluation/tools; research opportunities; future challenges (p.24–25); conclusions (p.25).

## D. Key messages (p.24–25) — future challenges: cultural differences in norms; individual preferences; acceptability, safety, trust, privacy; intention estimation; abnormal behaviour (vandalism/obstruction); urban design and regulation; situation comprehension and conflict detection; evaluation of subjective aspects. No mention of LLMs/VLMs (the keyword hits are false positives "Kollmitz").

## N. Limitations (of the survey) — mobile-robot-heavy corpus (acknowledged); pre-FM; no quantitative evidence synthesis.

## P. Survey analysis — see `survey:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue The International Journal of Robotics Research; DOI 10.1177/02783649241230562; pages 1533-1572; URL https://doi.org/10.1177/02783649241230562.
- Sources: Crossref (exact title match, DOI 10.1177/02783649241230562); arXiv abs page (2311.06922v4).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - venue: PDF-derived 'IJRR 2024 (per citation); corpus copy arXiv v3' -> externally verified 'The International Journal of Robotics Research'
- Changed field - volume: PDF-derived 'Not reported' -> externally verified '43'
- Changed field - issue: PDF-derived 'Not reported' -> externally verified '10'
- Changed field - pages: PDF-derived '34 (PDF)' -> externally verified '1533-1572'
- Changed field - doi: PDF-derived 'Not printed (IJRR id 02783649241230562 per citation)' -> externally verified '10.1177/02783649241230562'
- Changed field - url: PDF-derived 'Not reported' -> externally verified 'https://doi.org/10.1177/02783649241230562'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

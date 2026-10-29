---
id: 2024_Raj_Hybrid-Social-Nav
source_pdfs: [02_Learning_Based_Social_Navigation/hybrid_social_nav.pdf]
duplicate_copies: []
related_versions: []
title: 'Rethinking Social Robot Navigation: Leveraging the Best of Two Worlds'
authors: &id001 [Amir Hossain Raj, Zichao Hu, Haresh Karnan, Rohan Chandra, Amirreza Payandeh, Luisa Mao, Peter Stone, Joydeep Biswas, Xuesu Xiao]
year: 2024
venue: 2024 IEEE International Conference on Robotics and Automation (ICRA)
volume: NA
issue: NA
pages: 16330-16337
doi: 10.1109/ICRA57147.2024.10611710
url: https://doi.org/10.1109/ICRA57147.2024.10611710
pub_status: conference
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1109/ICRA57147.2024.10611710); arXiv abs page (2309.13466v2). PDF-derived basis (Stage 1): ICRA 2024 header with DOI (IEEE Xplore copy).'
category: S2
folder: 02_Learning_Based_Social_Navigation
folder_category_match: 'Yes'
category_rationale: Case study of geometric planners on SCAND plus a hybrid geometric/behaviour-cloning planner with a learned gating classifier; no foundation model.
paper_type: method
fm_used: 'No'
fm_class: [None]
fm_models: []
fm_size: NA
method_family: [geometric planning (move_base/DWA), behaviour cloning, learned gating classifier, hybrid switching with hysteresis]
roles: []
roles_evidence: {}
integration: NA
integration_rationale: No foundation model.
evidence: E4
evidence_rationale: Physical experiments on Jackal (GMU) and Spot (UT) in three scenarios, 5 repetitions x 3 methods, 10 participants per scenario rating each run on 4-5 Likert items, with one-way ANOVA reported (p.5-6).
inputs: ['robot sensor observations over past 2 s (LiDAR/costmap, RGB per SCAND)', navigation goal 10 m ahead]
outputs: [planned trajectory / velocity commands (geometric or BC)]
human_repr: [humans as obstacles in costmap (move_base); implicit in BC inputs]
capabilities: {C1: Partial, C2: 'Yes', C3: Partial, C4: Partial, C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: Partial, C12: 'Yes', C13: Partial, C14: 'Yes', C15: 'No', C16: Partial, C17: 'No', C18: 'Yes', C19: 'No', C20: 'No', C21: Partial, C22: 'No', C23: 'No', C24: Partial, C25: 'No'}
exp:
  datasets: [SCAND (playback; train/test), manually curated out-of-distribution lab demonstrations]
  simulators: []
  robots: [Clearpath Jackal (GMU), Boston Dynamics Spot (UT Austin)]
  environment: university campuses (GMU, UT Austin)
  indoor_outdoor: Not reported
  sensors: [LiDAR, RGB, odometry]
  humans: real participants (10 per scenario)
  n_scenes: 3 scenarios x 2 robots
  n_trajectories: 5 repetitions x 3 methods per participant (15 interactions per individual)
  n_participants: 10 per scenario
  split: SCAND in-distribution train/test; OOD lab test set
  baselines: [move_base, move_base with social layer, Human-Aware Planner, CoHAN, Behaviour Cloning]
  ablation: Partial (geometric vs BC vs hybrid)
  real_robot_trials: 'Yes'
  human_study: 'Yes'
  statistical_testing: Yes (one-way ANOVA claimed; statistics not reported)
  scenarios: [frontal approach, intersection, narrow doorway, 'queue (illustrative, Fig.1)']
metrics: [SOCIAL | Social compliance (undirected Hausdorff distance to human demonstration) | m | Def.1; compliant if < epsilon | p.3, SOCIAL | CDF of scenarios vs Hausdorff threshold | % | share of SCAND scenarios below distance threshold | p.3-4, 'HUMAN | Likert questionnaire (4-5 items per scenario) | 1-5 | e.g., ''robot moved to avoid me'', ''nearly collided'' (reverse-coded), ''clear what robot wanted to do'', ''slowed down and stopped to let me pass'', ''made room for me'' | p.5']
deployment: {fm_model: NA, model_size: Not reported, api_cloud_local: NA, onboard_offboard: Not reported, gpu: Not reported, cpu: Not reported, latency: Not reported, query_frequency: NA, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: NA, caching: NA, event_triggered: Gating classifier with hysteresis voting over n steps, distillation: NA, quantization: NA, fallback_planner: Yes (switch to geometric planner within p m of obstacles for t s), safety_shield: Yes (proximity-triggered fallback), emergency_behavior: Manual intervention noted for BC, uncertainty: NA, hallucination_mitigation: NA, real_time_claim_supported: NA}
repro: {code: Not reported, code_url: NA, dataset: SCAND public; OOD set not stated as released, dataset_url: NA, checkpoints: NA, prompts_published: NA, hardware_specified: Partial, hyperparameters: 'No (n, r, p, t set empirically per location/robot)', protocol_described: Partial, project_page: NA, concerns: Deployment thresholds tuned per site; ANOVA statistics not reported.}
limitations_flags: [limited-scenarios, dataset-bias]
web_verification_required: []
cited_missing: [CoHAN (Singamaneni IROS 2021), Human-Aware Planner (Kollmitz), move_base social layer (Lu), Protocol for validating social navigation policies (Pirk 2022), APPLD / learned planner parameters, Francis principles and guidelines]
learning: {type: IL (behaviour cloning) + supervised gating classifier, state_repr: 2 s of robot sensor observations (SCAND), human_repr: implicit, reward_design: NA (supervised); classifier labels from Hausdorff distance d <= epsilon, social_reward: 'No', prediction_model: 'No', group_modeling: 'No', training_env: SCAND real demonstrations, sim_dependence: None (real data), interpretability: Medium (switching between explainable geometric planner and BC), generalization: Tested OOD lab set and two robots/campuses, real_world_validation: Yes (human study), social_metrics: Hausdorff alignment to demonstrations; Likert ratings}
coding: {latency_reported: 'No', safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: 'No', new_dataset_released: NA, real_robot: Systematic, human_subject_study: 'Yes'}
pdf_metadata_stage1:
  year: 2024
  authors: *id001
  venue: 2024 IEEE International Conference on Robotics and Automation (ICRA), Yokohama
  volume: NA
  issue: NA
  pages: 16330-16336
  doi: 10.1109/ICRA57147.2024.10611710
  url: Not reported
  pub_status: conference
  peer_reviewed: 'Yes'
  peer_review_basis: ICRA 2024 header with DOI (IEEE Xplore copy).
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: 2024 IEEE International Conference on Robotics and Automation (ICRA)
  verified_doi: 10.1109/ICRA57147.2024.10611710
  verified_url: https://doi.org/10.1109/ICRA57147.2024.10611710
  verified_pages: 16330-16337
  arxiv: 2309.13466v2
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1109/ICRA57147.2024.10611710)', arXiv abs page (2309.13466v2)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A6]
  C_capabilities: {SAF1: Partial, SAF2: 'Yes', SPA1: Partial, SPA2: 'No', SPA3: 'Yes', SPA4: 'No', HUM1: 'No', HUM2: 'No', NOR1: Partial, NOR2: 'No', NOR3: Partial, NOR4: 'No', EXP1: Partial, EXP2: 'Yes', EXP3: 'No'}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'No', EV3_physical_robot: systematic, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: robot-behaviour evaluation (type not differentiated), EV6_open_world_deployment: 'No'}
physical_source_folder: "02_Learning_Based_Social_Navigation"
analytical_category: "S2"
coding:
  latency_reported: "No"
  safety_mechanism: "NA"
  uncertainty_treatment: "NA"
  hallucination_treatment: "NA"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "Systematic"
  human_subject_study: "Yes"
---

# Rethinking Social Robot Navigation — Hybrid Planner (Raj, Hu et al., ICRA 2024)

Page convention: PDF index (p.N).

## A. Bibliographic — ICRA 2024, pp.16330–16336, DOI 10.1109/ICRA57147.2024.10611710. GMU, UT Austin, Sony AI. Same group as SCAND, VLM-Social-Nav, Social-LLaVA.

## B. Position — S2: argues for hybrid (geometric + learned) social navigation; empirical basis for "geometric planners already handle most SCAND scenarios", directly motivating later VLM-as-specialist designs (e.g., VLM invoked only in hard social scenarios).

## C. Research problem — learning-based social navigation discards safe, testable geometric systems; is that necessary? (p.1–2). Contributions: demonstration-alignment definition of social compliance; SCAND case study; hybrid paradigm validated in playback and on two robots (p.2).

## D. Method — Def.1 compliance by undirected Hausdorff distance to 10 m demonstrated path (p.3); benchmark move_base, move_base(s), Human-Aware Planner, CoHAN on SCAND playback (Fig.3); BC trained on SCAND; classifier M_ϕ labels whether geometric output is compliant (d ≤ ϵ); BC trained only on non-compliant subset; deployment with hysteresis voting and proximity fallback (p.4–5).

## L. Quantitative results
- SCAND case study: move_base aligns with demonstrations within ϵ = 1.0 m in >80% of scenarios; ~5% of scenarios >3 m Hausdorff (50 inspected) (p.4); BC better in-distribution but degrades OOD; hybrid tracks best planner on each set (Fig.4; numbers only graphical).
- Table I (human study average scores, visually verified p.5; Frontal / Intersection / Doorway): Jackal — move_base 2.66 ± 0.64 / 3.98 ± 0.10 / 4.08 ± 0.38; BC 3.63 ± 0.40 / 2.49 ± 0.11 / 2.84 ± 0.25; Hybrid 4.04 ± 0.39 / 4.06 ± 0.20 / 3.89 ± 0.36. Spot — move_base 3.73 ± 0.22 / 2.72 ± 0.17 / 3.29 ± 0.19; BC 3.41 ± 0.19 / 3.13 ± 0.12 / 3.54 ± 0.49; Hybrid 3.70 ± 0.26 / 3.48 ± 0.15 / 3.82 ± 0.14.
- **Data-quality note:** paper states a one-way ANOVA "confirms the statistical significance" for each question (p.6) but reports no F or p values; several comparisons have overlapping means (e.g., Jackal intersection move_base 3.98 vs Hybrid 4.06; Spot frontal move_base 3.73 vs Hybrid 3.70), so significance for every question cannot be verified.

## N. Limitations
1. **Stated (p.6):** engineering challenges for robust deployment; BC is a simple representative; preliminary effort.
2. **Observable:** compliance defined as similarity to one demonstrator path (acknowledged footnote p.3); per-site tuning of switching thresholds; small participant pool; statistics unreported.
3. **Social relevance:** clear scenario-specific human items (yielding, doorway, legibility).

## P. Learning-based analysis — see `learning:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue 2024 IEEE International Conference on Robotics and Automation (ICRA); DOI 10.1109/ICRA57147.2024.10611710; pages 16330-16337; URL https://doi.org/10.1109/ICRA57147.2024.10611710.
- Sources: Crossref (exact title match, DOI 10.1109/ICRA57147.2024.10611710); arXiv abs page (2309.13466v2).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - venue: PDF-derived '2024 IEEE International Conference on Robotics and Automation (ICRA), Yokohama' -> externally verified '2024 IEEE International Conference on Robotics and Automation (ICRA)'
- Changed field - pages: PDF-derived '16330-16336' -> externally verified '16330-16337'
- Changed field - url: PDF-derived 'Not reported' -> externally verified 'https://doi.org/10.1109/ICRA57147.2024.10611710'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

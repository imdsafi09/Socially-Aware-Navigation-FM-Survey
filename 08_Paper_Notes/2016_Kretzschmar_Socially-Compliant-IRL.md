---
id: 2016_Kretzschmar_Socially-Compliant-IRL
source_pdfs: [01_Classical_Social_Navigation/kretzschmar-ijrr2016-socially.pdf]
duplicate_copies: []
related_versions: ['Builds on Kuderer et al. RSS 2012 (in corpus) and Kuderer et al. 2013/2014, Kretzschmar et al. 2014 (not in corpus)']
title: Socially Compliant Mobile Robot Navigation via Inverse Reinforcement Learning
authors: &id001 [Henrik Kretzschmar, Markus Spies, Christoph Sprunk, Wolfram Burgard]
year: 2016
venue: The International Journal of Robotics Research
volume: '35'
issue: '11'
pages: 1289-1307
doi: 10.1177/0278364915619772
url: https://doi.org/10.1177/0278364915619772
pub_status: journal (corpus copy author manuscript)
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1177/0278364915619772). PDF-derived basis (Stage 1): File name indicates IJRR 2016; CADRL (corpus) cites ''The International Journal of Robotics Research, Jan. 2016''. Corpus copy is single-column manuscript. WEB_VERIFICATION_REQUIRED.'
category: S2
folder: 01_Classical_Social_Navigation
folder_category_match: Partial
category_rationale: Maximum-entropy IRL mixture model over homotopy classes and continuous trajectories (HMC sampling) for cooperative pedestrian modelling and robot navigation; learning-based, pre-deep-learning, in the classical folder.
paper_type: method
fm_used: 'No'
fm_class: [None]
fm_models: []
fm_size: NA
method_family: [maximum entropy IRL, Hybrid (Hamiltonian) Monte Carlo, homotopy classes via Voronoi graph, spline trajectory optimization (RPROP), shared autonomy]
roles: []
roles_evidence: {}
integration: NA
integration_rationale: No foundation model.
evidence: E2
evidence_rationale: Systematic evaluation via cross-validation on two pedestrian datasets and a 10-scenario comparison against A* with recorded pedestrian trajectories (Table 1); robotic-wheelchair encounters and a Turing test of trajectory animations are qualitative/perceptual and do not evaluate robot behaviour with participants.
inputs: [laser-tracked pedestrian positions/velocities, static map, target positions (assumed known or inferred via Bayes)]
outputs: [mixture distribution over composite trajectories, 'robot''s most likely trajectory (replanned at 5 Hz, 10 s horizon)']
human_repr: ['continuous spline trajectories with features (time, acceleration, velocity, clearance to agents, clearance to obstacles)', 'homotopy features: passing side (winding angles), moving through groups, most-likely-trajectory cost']
capabilities: {C1: Partial, C2: 'Yes', C3: Partial, C4: 'No', C5: 'Yes', C6: 'Yes', C7: Partial, C8: 'No', C9: Partial, C10: 'No', C11: Partial, C12: Partial, C13: 'Yes', C14: 'No', C15: 'No', C16: 'No', C17: 'No', C18: 'No', C19: Partial, C20: 'Yes', C21: 'No', C22: 'No', C23: 'No', C24: 'No', C25: Partial}
exp:
  datasets: ['Motion capture: 4 persons, 1 h, 81 composite trajectories (11x8 m)', 'Pellegrini et al. 2009 hotel entrance: 12 min, 71 composite trajectories (3-5 pedestrians)']
  simulators: [replay with recorded pedestrian trajectories (A* comparison)]
  robots: [autonomous robotic wheelchair (laser range finders)]
  environment: office corridor/hallway
  indoor_outdoor: indoor
  sensors: [laser range finders, motion capture (dataset)]
  humans: real pedestrians (datasets; robot encounters)
  n_scenes: two datasets; 10 A*-comparison scenarios; several robot encounters
  n_trajectories: 81 + 71 composite trajectories
  n_participants: 10 subjects in Turing test (40 runs each)
  split: 5-fold cross-validation
  baselines: [Kuderer et al. 2012, Social forces, RVO, A* in configuration-time space (r_min 0.2 / 0.8 m)]
  ablation: 'No'
  real_robot_trials: Partial (qualitative encounters)
  human_study: Partial (Turing test on trajectory animations, not robot interaction)
  statistical_testing: Partial (one-sided paired t-test at 95% for Turing test; values not reported)
  scenarios: [frontal encounter with obstacle, two pedestrians side by side in hallway, shared-autonomy corridor]
metrics: ['OTHER | Feature discrepancy |E_P[f] - f_D| | norm | cross-validation | p.27-28', NAV | Prediction error | m | Euclidean error vs prediction horizon Delta t | p.28, HUMAN | Perceived as human | % | Turing test on animations (10 subjects) | p.29-30, SAFETY | min dist | m | minimum distance to pedestrians (A* comparison) | p.33, NAV | avg velocity | m/s | | p.33, NAV | % blocked | % of time steps | planner unable to find path / stopped | p.33]
deployment: {fm_model: NA, model_size: NA, api_cloud_local: NA, onboard_offboard: Onboard (implied; on-board sensors), gpu: NA, cpu: Not reported, latency: Not reported, query_frequency: NA, planner_frequency: '5 Hz replanning, 10 s horizon', controller_frequency: Not reported, asynchronous: NA, caching: Maintains set of optimized homotopically distinct trajectories across cycles, event_triggered: New homotopy classes added when environment changes, distillation: NA, quantization: NA, fallback_planner: Global A* paths beyond horizon, safety_shield: Not reported, emergency_behavior: Not reported, uncertainty: Probabilistic mixture over homotopy classes, hallucination_mitigation: NA, real_time_claim_supported: Partial (5 Hz stated)}
repro: {code: Not reported, code_url: NA, dataset: Partial (Pellegrini public; mocap not stated), dataset_url: NA, checkpoints: NA, prompts_published: NA, hardware_specified: Partial, hyperparameters: Partial, protocol_described: Partial, project_page: NA, concerns: A* comparison capped at 0.5 m/s while learned policy averages 0.56 m/s.}
limitations_flags: [limited-scenarios, no-human-study]
web_verification_required: [IJRR 2016 volume/issue/pages/DOI.]
cited_missing: [Ziebart et al. 2008/2009, Kitani et al. 2012 activity forecasting, Kim & Pineau 2015 socially adaptive path planning, Trautman et al. 2013 cafeteria, Pellegrini 2009, Vernaza 2012 homotopy, Bhattacharya 2012 H-signature]
learning: {type: IRL (maximum entropy) with mixture over homotopy classes, state_repr: composite spline trajectories of all agents, human_repr: joint trajectories; group membership feature when available, reward_design: 'theta^T f with physical features (time, acceleration, velocity, distance to agents, distance to obstacles) and theta_hom^T f_hom (passing side, group crossing, ML cost)', social_reward: Yes (learned from demonstrations or teleoperation), prediction_model: Yes (joint mixture distribution; goal inference via Bayes), group_modeling: Partial (group-crossing feature if groups recognized), training_env: real pedestrian datasets, sim_dependence: Low, interpretability: High, generalization: 5-fold cross-validation on two datasets, real_world_validation: Qualitative wheelchair experiments, social_metrics: Turing-test human-likeness; min distance}
classical: {human_is: cooperative utility-optimizing agent, social_repr: learned costs over trajectory dynamics and topological decisions, hand_rules: Partial (features), math_model: p(x) = P(psi_x) p_psi(x); p_psi(x) ∝ exp(-theta^T f(x)); P(psi) ∝ exp(-theta_hom^T f_hom(psi)), planner: most likely composite trajectory in most likely homotopy class; Voronoi-based homotopy enumeration; global A* beyond horizon, interpretability: High, strengths: Captures discrete and continuous decisions and stochasticity; learns cultural side preferences and group avoidance in principle; teachable by teleoperation, limitations: Assumes cooperative agents and known goals; small datasets; computational complexity with many agents, later_improvement: DRL (SA-CADRL) and VLM methods; SCAND-based learning}
coding: {latency_reported: 'No', safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: 'No', new_dataset_released: NA, real_robot: Demo, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2016
  authors: *id001
  venue: The International Journal of Robotics Research (IJRR), 2016 (per corpus citations; corpus PDF is an author manuscript without journal layout)
  volume: Not reported
  issue: Not reported
  pages: 42 (manuscript PDF)
  doi: Not reported
  url: Not reported
  pub_status: journal (corpus copy author manuscript)
  peer_reviewed: 'Yes'
  peer_review_basis: File name indicates IJRR 2016; CADRL (corpus) cites 'The International Journal of Robotics Research, Jan. 2016'. Corpus copy is single-column manuscript. WEB_VERIFICATION_REQUIRED.
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: The International Journal of Robotics Research
  verified_doi: 10.1177/0278364915619772
  verified_url: https://doi.org/10.1177/0278364915619772
  verified_pages: 1289-1307
  arxiv: NA
  version_relationship: Corpus copy is an author manuscript; journal version authoritative
  sources: ['Crossref (exact title match, DOI 10.1177/0278364915619772)']
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A2, A4]
  C_capabilities: {SAF1: Partial, SAF2: 'Yes', SPA1: Partial, SPA2: Partial, SPA3: 'Yes', SPA4: 'No', HUM1: 'Yes', HUM2: Partial, NOR1: Partial, NOR2: 'No', NOR3: 'No', NOR4: Partial, EXP1: 'No', EXP2: Partial, EXP3: 'Yes'}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: demo, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "01_Classical_Social_Navigation"
analytical_category: "S2"
coding:
  latency_reported: "No"
  safety_mechanism: "NA"
  uncertainty_treatment: "NA"
  hallucination_treatment: "NA"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "Demo"
  human_subject_study: "No"
---

# Socially Compliant Navigation via IRL (Kretzschmar, Spies, Sprunk, Burgard — IJRR 2016)

Page convention: PDF index (p.N) of the 42-page author manuscript.

## A. Bibliographic — IJRR 2016 (author manuscript in corpus); Univ. of Freiburg.

## B. Position — classical-era IRL (coded S2, folder 01); the most complete pre-deep-learning learned social navigation model in the corpus.

## C. Research problem — model cooperative pedestrian behaviour with discrete (passing side) and continuous decisions plus stochasticity, and use it for robot navigation (p.1–3). Contributions: mixture-distribution max-ent IRL with HMC feature expectations; Voronoi-based homotopy exploration; navigation integration; experiments including a Turing test (p.3–4).

## D. Method — max-ent distribution Eq.9; features Eq.17–21; HMC acceptance Eq.22; mixture over homotopy classes (Eq.25–26) with passing-side (Eq.27) and group-crossing features; Voronoi graph with k-shortest homotopically distinct paths O(k(o log o)) (Eq.30–39); winding-angle fingerprints (Eq.42); goal inference (Eq.43); 5 Hz replanning with 10 s horizon (p.8–25).

## L. Results
- Cross-validation (Fig.8): lower feature discrepancy and Euclidean prediction error than Kuderer 2012, social forces and RVO on both datasets (graphical only); authors note feature-discrepancy comparison favours their method; Euclidean error is the fair comparison (p.28).
- Turing test (10 subjects × 40 runs): humans identified 79% of human demonstrations; mistook 68% of this method's predictions, 40% of Kuderer 2012 and 35% of social forces for human; one-sided paired t-test at 95% (statistic not reported) (p.29).
- Table 1 (A* comparison, 10 scenarios; min dist m / avg velocity m/s / % blocked): ours 0.34 / 0.56 / 0; A* r_min 0.2: 0.16 / 0.49 / 1; A* r_min 0.8: 0.38 / 0.27 / 60 (p.33).
- **Data-quality note:** text says the learned policy reached targets at "an average velocity of 0.5 m/s" while Table 1 lists 0.56 m/s; A* maximum velocity was set to 0.5 m/s, so the comparison caps the baseline below the learned policy's average speed (p.35).
- Wheelchair encounters (Figs.11–14) and shared-autonomy corridor (Fig.16) are qualitative.

## N. Limitations
1. **Stated (p.3, p.22):** cooperative-agent assumption fails in e.g. evacuation; sampling not feasible online, so most-likely trajectories used.
2. **Observable:** known targets assumed in robot experiments; small datasets; no participant evaluation of robot behaviour.
3. **Social relevance:** passing-side (cultural) and group features (C13, C25, C9) are explicit, though group behaviour is not evaluated separately.

## P. Classical / learning analysis — see blocks.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue The International Journal of Robotics Research; DOI 10.1177/0278364915619772; pages 1289-1307; URL https://doi.org/10.1177/0278364915619772.
- Sources: Crossref (exact title match, DOI 10.1177/0278364915619772).
- Version relationship: Corpus copy is an author manuscript; journal version authoritative.
- Changed field - venue: PDF-derived 'The International Journal of Robotics Research (IJRR), 2016 (per corpus citations; corpus PDF is an author manuscript without journal layout)' -> externally verified 'The International Journal of Robotics Research'
- Changed field - volume: PDF-derived 'Not reported' -> externally verified '35'
- Changed field - issue: PDF-derived 'Not reported' -> externally verified '11'
- Changed field - pages: PDF-derived '42 (manuscript PDF)' -> externally verified '1289-1307'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified '10.1177/0278364915619772'
- Changed field - url: PDF-derived 'Not reported' -> externally verified 'https://doi.org/10.1177/0278364915619772'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

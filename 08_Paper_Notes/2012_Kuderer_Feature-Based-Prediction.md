---
id: 2012_Kuderer_Feature-Based-Prediction
source_pdfs: [01_Classical_Social_Navigation/p25.pdf]
duplicate_copies: []
related_versions: ['Extended in Kretzschmar et al., IJRR 2016 (in corpus: 2016_Kretzschmar_Socially-Compliant-IRL)']
title: Feature-Based Prediction of Trajectories for Socially Compliant Navigation
authors: &id001 [Markus Kuderer, Henrik Kretzschmar, Christoph Sprunk, Wolfram Burgard]
year: 2012
venue: 'Robotics: Science and Systems VIII (RSS 2012)'
volume: NA
issue: NA
pages: Not paginated (RSS)
doi: 10.15607/RSS.2012.VIII.025
url: https://doi.org/10.15607/RSS.2012.VIII.025
pub_status: conference
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.15607/RSS.2012.VIII.025). PDF-derived basis (Stage 1): Corpus PDF lacks venue header; CADRL (corpus) cites it as Robotics: Science and Systems 2012. WEB_VERIFICATION_REQUIRED.'
category: S2
folder: 01_Classical_Social_Navigation
folder_category_match: Partial
category_rationale: Maximum-entropy IRL over continuous joint trajectories with topological variants, learned from motion-capture data and used for robot navigation; pre-deep-learning learning-based method in the classical folder.
paper_type: method
fm_used: 'No'
fm_class: [None]
fm_models: []
fm_size: NA
method_family: [maximum entropy IRL (continuous), spline trajectory optimization (RPROP), topological variants (homotopy classes), joint human-robot trajectory prediction]
roles: []
roles_evidence: {}
integration: NA
integration_rationale: No foundation model.
evidence: E1
evidence_rationale: Quantitative evaluation is offline (10-fold cross-validation of feature discrepancy on mocap data; synthetic recovery); real-robot human-passing encounters are two qualitative examples.
inputs: [poses of humans and robot (motion capture), target positions]
outputs: [probability over topological variants, most likely joint trajectories (incl. robot's own)]
human_repr: [continuous spline trajectory per agent, 'features: travel time, acceleration, velocity, distance-based collision avoidance, passing side']
capabilities: {C1: Partial, C2: Partial, C3: Partial, C4: 'No', C5: 'Yes', C6: 'Yes', C7: Partial, C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: 'No', C13: 'Yes', C14: 'No', C15: 'No', C16: 'No', C17: 'No', C18: Partial, C19: Partial, C20: 'Yes', C21: 'No', C22: 'No', C23: 'No', C24: 'No', C25: 'No'}
exp:
  datasets: ['Motion capture: 3 subjects, 8 locations in 7x7 m, 1 h, 96 runs (12 per scenario)', 'Synthetic: 100 random 3-agent scenarios in 10x10 m']
  simulators: [synthetic data generation]
  robots: [mobile robot (unnamed)]
  environment: lab area with motion capture
  indoor_outdoor: indoor
  sensors: [visual motion capture]
  humans: 'real subjects (cover task: reading newspaper articles)'
  n_scenes: 8 scenarios
  n_trajectories: 96 runs
  n_participants: 3 subjects (data collection)
  split: 10-fold cross-validation
  baselines: [Social forces (parameters fitted by SGD)]
  ablation: Partial (training set size n = 10-100 in synthetic study)
  real_robot_trials: Partial (qualitative encounters)
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [pairwise passing / crossing among three agents, robot-human frontal passing]
metrics: [OTHER | Feature discrepancy ||f_D - f_theta||_2 | norm | difference between empirical and predicted feature values | p.6, OTHER | KL divergence between true and estimated topological-variant distribution | nats (implied) | synthetic recovery | p.7, DEPLOY | Optimization iteration time | ms | ~1 ms per iteration for 60 spline control points | p.7]
deployment: {fm_model: NA, model_size: NA, api_cloud_local: NA, onboard_offboard: Not reported, gpu: NA, cpu: standard desktop, latency: ~1 ms per optimization iteration, query_frequency: NA, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: NA, caching: NA, event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: NA, safety_shield: NA, emergency_behavior: NA, uncertainty: Probability over topological variants, hallucination_mitigation: NA, real_time_claim_supported: Partial}
repro: {code: Not reported, code_url: NA, dataset: Not reported, dataset_url: NA, checkpoints: NA, prompts_published: NA, hardware_specified: 'No', hyperparameters: Partial, protocol_described: 'Yes', project_page: NA, concerns: Small mocap dataset (3 subjects).}
limitations_flags: [no-human-study, limited-scenarios]
web_verification_required: [RSS 2012 publication details.]
cited_missing: [Ziebart maximum entropy IRL (AAAI 2008), Ziebart planning-based prediction (IROS 2009), Pellegrini 'You'll never walk alone', Mombaur inverse optimal control of human locomotion, Hoogendoorn & Bovy pedestrian behaviour]
learning: {type: 'IRL (maximum entropy, continuous trajectories)', state_repr: cubic spline control points of all agents' joint trajectories, human_repr: joint trajectories with interaction features, reward_design: 'cost theta^T f with features: travel time, squared acceleration, squared velocity, inverse-squared-distance weighted by speed, (optional) passing side', social_reward: Yes (learned weights reproducing human cooperative avoidance), prediction_model: Yes (joint trajectory distribution over homotopy classes), group_modeling: No (suggested as possible feature), training_env: real mocap data, sim_dependence: Low, interpretability: High, generalization: 10-fold CV across 8 scenarios, real_world_validation: Qualitative robot encounters, social_metrics: Feature matching to human behaviour}
classical: {human_is: utility-optimizing cooperative agent, social_repr: learned cost over trajectory features + passing-side topology, hand_rules: Partial (feature design), math_model: p_theta(x) = exp(-theta^T f(x)) / Z(theta); modes approximated per topological variant, planner: robot plans its own trajectory as part of most likely joint trajectory, interpretability: High, strengths: Models cooperation and passing decisions probabilistically; human-like smooth trajectories, limitations: Small data; requires known goals; computational growth with agents (variants grow combinatorially), later_improvement: 'Kretzschmar IJRR 2016 (larger study, robot experiments); later DRL and VLM methods'}
coding: {latency_reported: 'Yes', safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: 'No', new_dataset_released: NA, real_robot: Demo, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2012
  authors: *id001
  venue: 'Robotics: Science and Systems (RSS) 2012 (per CADRL reference list; corpus PDF has no venue header, file name p25)'
  volume: NA
  issue: NA
  pages: 8 (PDF)
  doi: Not reported
  url: Not reported
  pub_status: conference
  peer_reviewed: 'Yes'
  peer_review_basis: 'Corpus PDF lacks venue header; CADRL (corpus) cites it as Robotics: Science and Systems 2012. WEB_VERIFICATION_REQUIRED.'
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: 'Robotics: Science and Systems VIII (RSS 2012)'
  verified_doi: 10.15607/RSS.2012.VIII.025
  verified_url: https://doi.org/10.15607/RSS.2012.VIII.025
  verified_pages: Not paginated (RSS)
  arxiv: NA
  version_relationship: Corpus copy is the published version
  sources: ['Crossref (exact title match, DOI 10.15607/RSS.2012.VIII.025)']
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A2]
  C_capabilities: {SAF1: Partial, SAF2: Partial, SPA1: Partial, SPA2: 'No', SPA3: 'Yes', SPA4: 'No', HUM1: 'Yes', HUM2: Partial, NOR1: 'No', NOR2: 'No', NOR3: 'No', NOR4: 'No', EXP1: 'No', EXP2: Partial, EXP3: 'Yes'}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'Yes', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: demo, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "01_Classical_Social_Navigation"
analytical_category: "S2"
coding:
  latency_reported: "Yes"
  safety_mechanism: "NA"
  uncertainty_treatment: "NA"
  hallucination_treatment: "NA"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "Demo"
  human_subject_study: "No"
---

# Feature-Based Prediction of Trajectories (Kuderer, Kretzschmar, Sprunk, Burgard — RSS 2012)

Page convention: PDF index (p.N).

## A. Bibliographic — corpus PDF without venue header (file "p25"); cited as RSS 2012 by CADRL. Univ. of Freiburg.

## B. Position — classical-era IRL (coded S2, folder 01). Introduces topological-variant reasoning (passing left/right) as a learned probabilistic decision — a precursor of multi-modal social action prediction.

## C. Research problem — reactive methods yield unnatural evasive movements; need models of cooperative human navigation for prediction and planning (p.1). Contribution: maximum-entropy learning of human navigation over continuous joint trajectories (p.1).

## D. Method — joint trajectory x (Eq.2); topological variants partition (Eq.3); max-ent distribution p_θ(x) ∝ exp(−θᵀf(x)) (Eq.10); feature expectations approximated by mode of each variant (Eq.14–15); spline representation (Eq.16–17); features Eq.19–22; RPROP with hierarchical refinement; variant constraint via κ (Eq.23) (p.3–5).

## L. Results
- 10-fold CV on mocap data: ‖f_D − f_θ‖₂ = 1.7 (ours) vs 7.2 (social forces) (p.6).
- Synthetic recovery with n = 10/25/50/75/100 samples: 0.64 / 0.44 / 0.33 / 0.25 / 0.21 (p.7).
- Unique maximum per variant (deviation < 2 cm); ~1 ms per iteration (60 control points) (p.7).
- Real robot: two qualitative encounters where the robot keeps or switches passing side (Figs.4–5).
- Note: text describes eight scenarios (p.6) while Fig.3 caption mentions six.

## N. Limitations
1. **Stated (p.5):** humans may react differently to robots than to humans; would need data with robots or teleoperation.
2. **Observable:** three subjects; known goals assumed; real-robot evidence qualitative.

## P. Classical / learning analysis — see blocks.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue Robotics: Science and Systems VIII (RSS 2012); DOI 10.15607/RSS.2012.VIII.025; pages Not paginated (RSS); URL https://doi.org/10.15607/RSS.2012.VIII.025.
- Sources: Crossref (exact title match, DOI 10.15607/RSS.2012.VIII.025).
- Version relationship: Corpus copy is the published version.
- Changed field - venue: PDF-derived 'Robotics: Science and Systems (RSS) 2012 (per CADRL reference list; corpus PDF has no venue header, file name p25)' -> externally verified 'Robotics: Science and Systems VIII (RSS 2012)'
- Changed field - pages: PDF-derived '8 (PDF)' -> externally verified 'Not paginated (RSS)'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified '10.15607/RSS.2012.VIII.025'
- Changed field - url: PDF-derived 'Not reported' -> externally verified 'https://doi.org/10.15607/RSS.2012.VIII.025'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

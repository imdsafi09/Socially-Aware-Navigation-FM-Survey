---
id: 2010_Trautman_Unfreezing-IGP
source_pdfs: [01_Classical_Social_Navigation/Unfreezing_the_robot_Navigation_in_dense_interacting_crowds.pdf]
duplicate_copies: []
related_versions: ['Extended journal version: Trautman et al., ''Robot navigation in dense human crowds: Statistical models and experimental studies of human-robot cooperation'', IJRR 34(3) 2015 (cited in corpus; not in corpus)']
title: 'Unfreezing the Robot: Navigation in Dense, Interacting Crowds'
authors: &id001 [Peter Trautman, Andreas Krause]
year: 2010
venue: 2010 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
volume: NA
issue: NA
pages: 797-803
doi: 10.1109/IROS.2010.5654369
url: https://doi.org/10.1109/IROS.2010.5654369
pub_status: conference
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1109/IROS.2010.5654369). PDF-derived basis (Stage 1): IROS 2010 header and IEEE copyright (IEEE Xplore copy).'
category: S1
folder: 01_Classical_Social_Navigation
folder_category_match: 'Yes'
category_rationale: 'Model-based cooperative planning: interacting Gaussian processes (IGP) jointly modelling robot and crowd trajectories; formalizes the freezing robot problem.'
paper_type: method
fm_used: 'No'
fm_class: [None]
fm_models: []
fm_size: NA
method_family: [Gaussian processes, interaction potential, importance sampling / particle inference, MAP joint trajectory planning, receding horizon]
roles: []
roles_evidence: {}
integration: NA
integration_rationale: No foundation model.
evidence: E2
evidence_rationale: Closed-loop replanning of a virtual agent through recorded (non-reactive) ETH pedestrian crowds, 10 runs, compared with the actual pedestrian and PCLRHC (Table I, Fig.4); no physical robot.
inputs: [tracked pedestrian positions over time (overhead video), robot start and goal]
outputs: [robot trajectory (next waypoint from MAP joint assignment)]
human_repr: ['trajectory as GP sample (non-Markov, goal as final measurement)', pairwise interaction potential 1 - alpha*exp(-d^2/(2h^2))]
capabilities: {C1: Partial, C2: 'Yes', C3: Partial, C4: 'No', C5: 'Yes', C6: 'Yes', C7: Partial, C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: 'Yes', C18: 'No', C19: 'No', C20: Partial, C21: 'No', C22: 'No', C23: 'No', C24: 'No', C25: 'No'}
exp:
  datasets: [ETH overhead video of pedestrians at a university building doorway (>8 min)]
  simulators: [replay of recorded pedestrian trajectories]
  robots: []
  environment: building entrance with dense crowds
  indoor_outdoor: outdoor
  sensors: [overhead camera (dataset)]
  humans: real recorded pedestrians (non-reactive to virtual robot)
  n_scenes: variations of crowd-crossing scenarios
  n_trajectories: 10 runs
  n_participants: NA
  split: NA
  baselines: [actual pedestrian, PCLRHC (partially closed-loop receding horizon control)]
  ablation: 'No'
  real_robot_trials: 'No'
  human_study: 'No'
  statistical_testing: Partial (standard error bars, Fig.4)
  scenarios: [crowd crossing (person/group through counter-flow crowd)]
metrics: [NAV | Path length | pixels | Euclidean path length start to finish | p.6, SAFETY | Safety margin | pixels | nearest distance to any pedestrian during run; >13 px considered safe | p.6, DEPLOY | Inference time | s | ~0.1 s for 100 particles; ~5 s for 5000 particles (Matlab) | p.5]
deployment: {fm_model: NA, model_size: NA, api_cloud_local: NA, onboard_offboard: NA, gpu: NA, cpu: Not reported, latency: 0.1 s (100 particles) to 5 s (5000 particles) in Matlab, query_frequency: NA, planner_frequency: per observation (receding horizon), controller_frequency: NA, asynchronous: NA, caching: NA, event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: NA, safety_shield: NA, emergency_behavior: NA, uncertainty: Yes (probabilistic joint trajectory distribution), hallucination_mitigation: NA, real_time_claim_supported: 'Partial (argued, not demonstrated on robot)'}
repro: {code: Not reported, code_url: NA, dataset: 'Yes (ETH data, ref [18])', dataset_url: NA, checkpoints: NA, prompts_published: NA, hardware_specified: 'No', hyperparameters: 'Partial (h ~ 10 px, alpha chosen to enforce h)', protocol_described: Partial, project_page: NA, concerns: Pixel units; non-reactive replay; only 10 runs.}
limitations_flags: [no-human-study, sim-to-real, limited-scenarios]
web_verification_required: []
cited_missing: [PCLRHC (Du Toit & Burdick), Ziebart planning-based prediction (IROS 2009), Pellegrini 'You'll never walk alone' (ETH tracking), van den Berg RVO/ORCA]
classical: {human_is: interacting stochastic agent whose trajectory is a GP coupled to others, social_repr: joint collision avoidance via multiplicative interaction potential among all agents including robot, hand_rules: 'Partial (potential form and h, alpha hand-set)', math_model: 'p_IGP(f_R, f | z) = (1/Z) psi(f_R, f) prod_i p(f_i | z); MAP via importance sampling', planner: 'MAP joint trajectory, receding horizon', interpretability: High, strengths: Formalizes freezing robot problem; models cooperation; goals as GP measurements; handles multimodality via sampling, limitations: Assumes cooperative humans; computational cost grows with particles; offline replay validation, later_improvement: IJRR 2015 real-robot cafeteria study; DRL methods (CADRL/SARL) learn cooperation implicitly; VLM approaches add semantic context}
coding: {latency_reported: 'Yes', safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: 'No', new_dataset_released: NA, real_robot: 'No', human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2010
  authors: *id001
  venue: 2010 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Taipei
  volume: NA
  issue: NA
  pages: 797-803
  doi: Not reported
  url: http://www.cds.caltech.edu/~trautman (videos)
  pub_status: conference
  peer_reviewed: 'Yes'
  peer_review_basis: IROS 2010 header and IEEE copyright (IEEE Xplore copy).
project_url: http://www.cds.caltech.edu/~trautman (videos)
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: 2010 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
  verified_doi: 10.1109/IROS.2010.5654369
  verified_url: https://doi.org/10.1109/IROS.2010.5654369
  verified_pages: 797-803
  arxiv: NA
  version_relationship: Corpus copy is the published version
  sources: ['Crossref (exact title match, DOI 10.1109/IROS.2010.5654369)']
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A2, A4]
  C_capabilities: {SAF1: Partial, SAF2: 'Yes', SPA1: Partial, SPA2: 'No', SPA3: 'No', SPA4: 'Yes', HUM1: Partial, HUM2: Partial, NOR1: 'No', NOR2: 'No', NOR3: 'No', NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: Partial}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: none, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "01_Classical_Social_Navigation"
analytical_category: "S1"
coding:
  latency_reported: "Yes"
  safety_mechanism: "NA"
  uncertainty_treatment: "NA"
  hallucination_treatment: "NA"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "No"
  human_subject_study: "No"
---

# Unfreezing the Robot — IGP (Trautman & Krause, IROS 2010)

Page convention: PDF index (p.N).

## A. Bibliographic — IROS 2010, Taipei, pp.797–803 (IEEE Xplore copy); Caltech.

## B. Position — S1 classical: defines the freezing robot problem (FRP), the central motivation reused across social-navigation literature (incl. VLM papers' "frozen robot" framing).

## C. Research problem — independent agent prediction leads to freezing in dense crowds even with perfect prediction (Eq.II.4) (p.2–3). Contributions: FRP formalization; cooperation insight; IGP model; approximate inference; evaluation on real crowd data (p.2).

## D. Method — independent GP priors per agent (Eq.III.1–2), goal as noisy final measurement; coupling by interaction potential ψ (Eq.III.4); importance sampling with weights = ψ (Eq.IV.3–5); MAP joint assignment, execute next robot step, replan (p.4–5).

## L. Quantitative results (Table I, p.6; pixels)
- Per-run path length / safety: pedestrian mean 378.1 / 20.9; IGP 370.3 / 22.6; PCLRHC 402.6 / 28.3 (means computed from Table I).
- **Data-quality notes:** text reports IGP "mean path length of around 362" (p.7) but Table I averages 370.3; claimed "fairly large margin" over pedestrians corresponds to ~2% shorter paths and +1.7 px safety (within standard error); IGP run 1 safety 12 px is below the paper's 13 px "safe" threshold; PCLRHC described as keeping large safety margins but run 2 has 8 px.

## N. Limitations
1. **Stated (p.6–7):** true validation needs live interaction with humans; infeasible at the time; cafeteria experiment planned.
2. **Observable:** replayed non-reactive pedestrians; 10 runs; pixel units; hand-set interaction parameters.
3. **Social relevance:** cooperation in crowds; no norms, groups or perceived comfort.

## P. Classical analysis — see `classical:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue 2010 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS); DOI 10.1109/IROS.2010.5654369; pages 797-803; URL https://doi.org/10.1109/IROS.2010.5654369.
- Sources: Crossref (exact title match, DOI 10.1109/IROS.2010.5654369).
- Version relationship: Corpus copy is the published version.
- Changed field - venue: PDF-derived '2010 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Taipei' -> externally verified '2010 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified '10.1109/IROS.2010.5654369'
- Changed field - url: PDF-derived 'http://www.cds.caltech.edu/~trautman (videos)' -> externally verified 'https://doi.org/10.1109/IROS.2010.5654369'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

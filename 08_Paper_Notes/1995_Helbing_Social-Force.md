---
id: 1995_Helbing_Social-Force
source_pdfs: [01_Classical_Social_Navigation/PhysRevE.51.4282.pdf]
duplicate_copies: []
related_versions: []
title: Social force model for pedestrian dynamics
authors: &id001 [Dirk Helbing, Péter Molnár]
year: 1995
venue: Physical Review E
volume: '51'
issue: '5'
pages: 4282-4286
doi: 10.1103/PhysRevE.51.4282
url: https://doi.org/10.1103/PhysRevE.51.4282
pub_status: journal
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1103/PhysRevE.51.4282); arXiv abs page (cond-mat/9805244v1). PDF-derived basis (Stage 1): Physical Review E journal layout with received/revised dates (p.1).'
category: S1
folder: 01_Classical_Social_Navigation
folder_category_match: 'Yes'
category_rationale: Foundational physics-based pedestrian interaction model (social forces); basis of many classical social navigation planners, simulators (PedSim, HuNavSim) and expert demonstrators.
paper_type: model
fm_used: 'No'
fm_class: [None]
fm_models: []
fm_size: NA
method_family: [social force model, nonlinearly coupled Langevin equations, potential fields]
roles: []
roles_evidence: {}
integration: NA
integration_rationale: No foundation model.
evidence: NA
evidence_rationale: Pedestrian crowd simulation model with qualitative comparison to empirical phenomena; no robot navigation evaluated, so the robot evidence scale does not apply.
inputs: ['pedestrian positions, velocities, destinations', border/obstacle locations, attractive objects/persons]
outputs: [acceleration / preferred velocity of each pedestrian]
human_repr: [pedestrian as point agent with desired speed/direction, elliptical repulsive potential oriented along motion (private sphere), 'attractive potentials (friends, displays) producing groups', 'anisotropic perception (angle of sight 2φ = 200°, rear weight c = 0.5)']
capabilities: {C1: Partial, C2: 'No', C3: Partial, C4: 'No', C5: Partial, C6: 'No', C7: 'No', C8: 'No', C9: Partial, C10: 'No', C11: 'No', C12: 'No', C13: 'No', C14: Partial, C15: 'No', C16: 'No', C17: Partial, C18: 'No', C19: 'No', C20: 'No', C21: Partial, C22: 'No', C23: 'No', C24: 'No', C25: 'No'}
exp:
  datasets: []
  simulators: [custom pedestrian simulation]
  robots: []
  environment: 10 m wide, 50 m long walkway; narrow door between two groups
  indoor_outdoor: NA
  sensors: []
  humans: simulated pedestrians (desired speed N(1.34, 0.26) m/s)
  n_scenes: 2 phenomena (lane formation, door oscillation)
  n_trajectories: Not reported
  n_participants: NA
  split: NA
  baselines: []
  ablation: 'No'
  real_robot_trials: 'No'
  human_study: 'No'
  statistical_testing: No (linear fit of lane number vs width)
  scenarios: [counter-flow walkway (lane formation), narrow doorway (oscillating passing direction)]
metrics: [OTHER | Average number of lanes N | count | lanes emerging vs walkway width; fit N(W) = 0.36 m^-1 W + 0.59 at density 0.3 m^-2 | p.4]
deployment: {fm_model: NA, model_size: NA, api_cloud_local: NA, onboard_offboard: NA, gpu: NA, cpu: NA, latency: NA, query_frequency: NA, planner_frequency: NA, controller_frequency: NA, asynchronous: NA, caching: NA, event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: NA, safety_shield: NA, emergency_behavior: NA, uncertainty: NA, hallucination_mitigation: NA, real_time_claim_supported: NA}
repro: {code: 'No', code_url: NA, dataset: NA, dataset_url: NA, checkpoints: NA, prompts_published: NA, hardware_specified: NA, hyperparameters: 'Yes (V0 = 2.1 m^2/s^2, sigma = 0.3 m, U0 = 10 m^2/s^2, R = 0.2 m, tau = 0.5 s, dt = 2 s, 2phi = 200 deg, c = 0.5)', protocol_described: Partial, project_page: NA, concerns: Validation is qualitative against observed phenomena.}
limitations_flags: []
web_verification_required: [DOI confirmation.]
cited_missing: [Henderson 1971/1974 fluid models, Helbing 1992 gas-kinetic model, Lewin field theory (1951)]
classical: {human_is: self-driven particle subject to social forces, social_repr: 'repulsive elliptical potentials (personal space/territory), border repulsion, attraction to persons/objects, anisotropic perception', hand_rules: Yes (force terms and parameters), math_model: dw/dt = F_driving + sum F_repulsive(peds) + sum F_border + sum F_attractive + fluctuations; speed capped at v_max = 1.3 v0, planner: None (descriptive pedestrian model); later used as robot controller/planner, interpretability: High, strengths: 'Simple, interpretable, reproduces lane formation and doorway oscillation', limitations: Hand-tuned parameters; no intention/context; reactive; groups only via attraction, later_improvement: 'Extended SFM for robots and groups (Moussaid 2010; Ferrer); used in simulators (PedSim, HuNavSim) and as demonstrator (GAIL-Depth); learned and VLM-based methods target context and norms it lacks'}
coding: {latency_reported: 'No', safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: 'No', new_dataset_released: NA, real_robot: 'No', human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 1995
  authors: *id001
  venue: Physical Review E
  volume: '51'
  issue: '5'
  pages: 4282-4286
  doi: Not printed (10.1103/PhysRevE.51.4282 implied by file name; WEB_VERIFICATION_REQUIRED)
  url: Not reported
  pub_status: journal
  peer_reviewed: 'Yes'
  peer_review_basis: Physical Review E journal layout with received/revised dates (p.1).
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: Physical Review E
  verified_doi: 10.1103/PhysRevE.51.4282
  verified_url: https://doi.org/10.1103/PhysRevE.51.4282
  verified_pages: 4282-4286
  arxiv: cond-mat/9805244v1
  version_relationship: arXiv copy posted 1998 after journal publication; journal version authoritative
  sources: ['Crossref (exact title match, DOI 10.1103/PhysRevE.51.4282)', arXiv abs page (cond-mat/9805244v1)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A3, A4]
  C_capabilities: {SAF1: Partial, SAF2: 'No', SPA1: Partial, SPA2: Partial, SPA3: Partial, SPA4: Partial, HUM1: Partial, HUM2: 'No', NOR1: 'No', NOR2: 'No', NOR3: 'No', NOR4: 'No', EXP1: Partial, EXP2: 'No', EXP3: 'No'}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'No', EV3_physical_robot: none, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "01_Classical_Social_Navigation"
analytical_category: "S1"
coding:
  latency_reported: "No"
  safety_mechanism: "NA"
  uncertainty_treatment: "NA"
  hallucination_treatment: "NA"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "No"
  human_subject_study: "No"
---

# Social Force Model (Helbing & Molnár, Phys. Rev. E 1995)

Page convention: PDF index (p.N).

## A. Bibliographic — Phys. Rev. E 51(5):4282–4286, May 1995; Univ. of Stuttgart.

## B. Position — S1 classical: canonical human-motion model underlying social navigation simulators and baselines (SocNavBench's Social Forces, GAIL-Depth expert, Group-Estimation's eSFM).

## C. Research problem — describe pedestrian motion in simple situations as automatic reactions representable by "social forces" (Lewin) (p.1–2).

## D. Method — desired direction e toward polygon edges; relaxation to desired velocity (Eq.2); repulsive elliptical potentials V(b) with semi-minor axis b including step s = vΔt (Eq.3–4); border repulsion (Eq.5); time-decaying attraction (Eq.6); anisotropic weighting w (Eq.7); total force (Eq.9) + fluctuations (Eq.10); speed limit (Eq.11–12); exponential potentials (Eq.13) (p.2–3).

## L. Results — lane formation in counter-flow (Fig.2), lane count N(W) = 0.36 m⁻¹ W + 0.59 (Fig.3), oscillating passing direction at narrow doors (Figs.4–5); qualitative agreement with observations (p.4).

## N. Limitations
1. **Stated:** fluctuations capture ambiguous situations; route choice not yet modeled (p.5).
2. **Observable:** no quantitative validation against trajectory data; hand-set parameters; social behaviour limited to distance-keeping and attraction.
3. **Relevance:** source of "proxemics as repulsion" representations that VLM approaches contrast with semantic/contextual reasoning.

## P. Classical analysis — see `classical:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue Physical Review E; DOI 10.1103/PhysRevE.51.4282; pages 4282-4286; URL https://doi.org/10.1103/PhysRevE.51.4282.
- Sources: Crossref (exact title match, DOI 10.1103/PhysRevE.51.4282); arXiv abs page (cond-mat/9805244v1).
- Version relationship: arXiv copy posted 1998 after journal publication; journal version authoritative.
- Changed field - doi: PDF-derived 'Not printed (10.1103/PhysRevE.51.4282 implied by file name; WEB_VERIFICATION_REQUIRED)' -> externally verified '10.1103/PhysRevE.51.4282'
- Changed field - url: PDF-derived 'Not reported' -> externally verified 'https://doi.org/10.1103/PhysRevE.51.4282'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

---
id: 2017_Chen_SA-CADRL
source_pdfs: [02_Learning_Based_Social_Navigation/1703.08862v2.pdf]
duplicate_copies: []
related_versions: ['Published: IEEE/RSJ IROS 2017, pp. 1343-1350 (per SocNavBench and Arena-Rosnav reference lists); corpus copy arXiv:1703.08862v2 (4 May 2018)']
title: Socially Aware Motion Planning with Deep Reinforcement Learning
authors: &id001 [Yu Fan Chen, Michael Everett, Miao Liu, Jonathan P. How]
year: 2017
venue: 2017 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
volume: NA
issue: NA
pages: 1343-1350
doi: 10.1109/IROS.2017.8202312
url: https://doi.org/10.1109/IROS.2017.8202312
pub_status: conference (corpus copy preprint)
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1109/IROS.2017.8202312); arXiv abs page (1703.08862v2). PDF-derived basis (Stage 1): Corpus copy arXiv v2 without venue; cited as IROS 2017 pp.1343-1350 in SocNavBench and Arena-Rosnav. WEB_VERIFICATION_REQUIRED.'
category: S2
folder: 02_Learning_Based_Social_Navigation
folder_category_match: 'Yes'
category_rationale: Deep RL with norm-inducing reward (passing/crossing/overtaking penalties) for socially aware multiagent navigation, with real-robot deployment.
paper_type: method
fm_used: 'No'
fm_class: [None]
fm_models: []
fm_size: NA
method_family: [DRL (deep V-learning), reward shaping for social norms, symmetric network with weight sharing + max-pooling]
roles: []
roles_evidence: {}
integration: NA
integration_rationale: No foundation model.
evidence: E3
evidence_rationale: Simulation on 200 random test cases (Table I) plus 10 real-world autonomous runs (>50 m between goals) among naturally occurring pedestrians with zero safety-driver interventions; no human-subject evaluation.
inputs: [own state, 'up to 3 nearby agents'' observable states (position, velocity, radius, heading, real/virtual flag)', subgoal from diffusion-map global planner, feasible directions from occupancy map]
outputs: [velocity vector]
human_repr: ['pedestrian as disc (position, velocity, radius incl. comfort buffer) from Lidar+camera detection/tracking']
capabilities: {C1: 'Yes', C2: Partial, C3: Partial, C4: 'No', C5: Partial, C6: Partial, C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: 'Yes', C12: 'No', C13: 'Yes', C14: 'No', C15: 'No', C16: 'No', C17: Partial, C18: 'No', C19: 'No', C20: 'No', C21: Partial, C22: 'No', C23: 'No', C24: 'No', C25: Partial}
exp:
  datasets: [n-agent trajectory dataset for initialization (details not given)]
  simulators: [custom 2D multiagent simulation]
  robots: ['differential-drive robotic vehicle (Lidar, 3 RealSense, 4 webcams; Gigabyte Brix)']
  environment: indoor campus building with regular pedestrian traffic
  indoor_outdoor: indoor
  sensors: [Lidar, RGB-D (RealSense), webcams]
  humans: simulated agents (r 0.2-0.5 m, v_pref 0.3-1.8 m/s); real naturally occurring pedestrians (avg 10.2 persons within 2 m per minute)
  n_scenes: 200 random sim test cases; 10 real runs
  n_trajectories: 200 sim cases (x2 agent-count settings); 10 real runs
  n_participants: NA
  split: random training cases vs evaluation cases
  baselines: [ORCA, CADRL (minimax), SA-CADRL (none)]
  ablation: Yes (none / left-handed / right-handed norm reward)
  real_robot_trials: 'Yes'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [passing, crossing, overtaking]
metrics: [NAV | Extra time to goal (t_e) | s | avg / 75th / 90th percentile | p.6-7, SAFETY | Min separation distance | m | 10th percentile / average | p.7, 'SOCIAL | Norm preference | % left / right | share of trajectories violating left- or right-handed penalty sets for >0.5 s, per passing/crossing/overtaking | p.6-7', SAFETY | Safety-driver interventions | count | real runs | p.7, 'DEPLOY | Query time | ms | 8.7 ms per value-network query (4-agent) on i7-5820K; 10 Hz onboard cycle | p.5, p.7']
deployment: {fm_model: NA, model_size: Not reported, api_cloud_local: NA, onboard_offboard: Onboard (Gigabyte Brix), gpu: Not reported, cpu: i7-5820K (sim timing); Gigabyte Brix onboard, latency: 8.7 ms per query; 10 Hz sense-plan-execute, query_frequency: 10 Hz, planner_frequency: 10 Hz, controller_frequency: Not reported, asynchronous: NA, caching: NA, event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: Diffusion-map global planner for subgoals, safety_shield: Feasible-direction filtering from occupancy map; safety driver, emergency_behavior: Human safety driver, uncertainty: NA, hallucination_mitigation: NA, real_time_claim_supported: 'Yes'}
repro: {code: Not reported, code_url: NA, dataset: NA, dataset_url: NA, checkpoints: NA, prompts_published: NA, hardware_specified: 'Yes', hyperparameters: Partial (penalty sets Eq.10-12), protocol_described: Partial, project_page: NA, concerns: Real-world evaluation lacks quantitative social metrics.}
limitations_flags: [no-human-study, limited-scenarios]
web_verification_required: [IROS 2017 details.]
cited_missing: [Kretzschmar IJRR 2016 (in corpus), Pfeiffer IRL teleoperation, Kuderer RSS 2012, Diffusion map algorithm (Chen 2016), Helbing extended social force (Ferrer)]
learning: {type: DRL (deep V-learning) with reward shaping, state_repr: agent-centric own state + n-1 neighbours (with virtual-agent padding flag), human_repr: discs with observable states; comfort buffer added to radius on robot, reward_design: 'R = R_col (CADRL) + R_norm: penalty q_n when another agent is in passing/overtaking/crossing penalty regions (Eq.9-12)', social_reward: Yes (explicit norm-violation penalties for right- or left-handed rules), prediction_model: Implicit via value function (reciprocity), group_modeling: 'No', training_env: '2D simulation, self-play, mirrored trajectories, separate bad-experience set', sim_dependence: High, interpretability: Medium (norm regions explicit), generalization: Four-agent network generalizes to fewer agents via virtual agents, real_world_validation: 'Yes (10 runs, qualitative + intervention count)', social_metrics: Norm preference (%)}
coding: {latency_reported: 'Yes', safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: 'No', new_dataset_released: NA, real_robot: Systematic, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2017
  authors: *id001
  venue: IEEE/RSJ IROS 2017 (per citations); corpus copy arXiv v2
  volume: NA
  issue: NA
  pages: 8 (PDF); 1343-1350 (per citations)
  doi: Not reported
  url: https://youtu.be/CK1szio7PyA (video)
  pub_status: conference (corpus copy preprint)
  peer_reviewed: 'Yes'
  peer_review_basis: Corpus copy arXiv v2 without venue; cited as IROS 2017 pp.1343-1350 in SocNavBench and Arena-Rosnav. WEB_VERIFICATION_REQUIRED.
project_url: https://youtu.be/CK1szio7PyA (video)
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: 2017 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
  verified_doi: 10.1109/IROS.2017.8202312
  verified_url: https://doi.org/10.1109/IROS.2017.8202312
  verified_pages: 1343-1350
  arxiv: 1703.08862v2
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1109/IROS.2017.8202312)', arXiv abs page (1703.08862v2)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1]
  C_capabilities: {SAF1: 'Yes', SAF2: Partial, SPA1: Partial, SPA2: 'No', SPA3: 'Yes', SPA4: Partial, HUM1: Partial, HUM2: 'No', NOR1: 'Yes', NOR2: 'No', NOR3: 'No', NOR4: Partial, EXP1: Partial, EXP2: 'No', EXP3: 'No'}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: systematic, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "02_Learning_Based_Social_Navigation"
analytical_category: "S2"
coding:
  latency_reported: "Yes"
  safety_mechanism: "NA"
  uncertainty_treatment: "NA"
  hallucination_treatment: "NA"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "Systematic"
  human_subject_study: "No"
---

# SA-CADRL (Chen, Everett, Liu, How — IROS 2017)

Page convention: PDF index (p.N).

## A. Bibliographic — corpus copy arXiv:1703.08862v2 (4 May 2018); MIT, IBM; cited as IROS 2017 pp.1343–1350.

## B. Position — S2: canonical DRL social-norm method (reward shaping "what not to do"); widely used baseline (e.g., SocNavBench).

## C. Research problem — social norms hard to quantify by feature matching; specifying violations is easier (p.1–2). Contributions: SA-CADRL; symmetric multiagent network; hardware demonstration at walking speed (p.2).

## D. Method — CADRL formulation (Eq.1–6) + norm reward R_norm on penalty sets S_pass, S_ovtk, S_cross (Eq.9–12); symmetric weight-sharing layers + max-pooling for 4-agent input; experience sets E and E_b (bad); random mirroring for topology exploration (Alg.1); real robot: Lidar+camera pedestrian tracking, diffusion-map subgoals within 5 m, 10 Hz (p.3–7).

## L. Quantitative results (Table I, p.7, visually verified; t_e avg/75th/90th s; min sep 10th pctl/avg m; norm preference L/R % passing, crossing, overtaking)
- 2 agents: ORCA 0.46/0.49/0.82; 0.108/0.131; 45/55, 51/49, 50/50 — CADRL 0.25/0.30/0.47; 0.153/0.189; 37/63, 38/62, 43/57 — SA-CADRL(none) 0.27/0.28/0.54; 0.169/0.189; 10/90, 32/68, 63/37 — SA-CADRL(lh) 0.30/0.36/0.67; 0.163/0.192; 98/2, 85/15, 86/14 — SA-CADRL(rh) 0.31/0.38/0.69; 0.168/0.199; 2/98, 15/85, 17/83.
- 4 agents: ORCA 0.86/1.14/1.80; 0.106/0.125; 46/54, 50/50, 48/52 — CADRL(minimax) 0.41/0.54/0.76; 0.096/0.173; 31/69, 41/59, 46/54 — SA-CADRL(none) 0.44/0.63/0.85; 0.162/0.183; 33/67, 33/67, 62/38 — SA-CADRL(lh) 0.49/0.69/1.00; 0.155/0.178; 83/17, 67/33, 73/27 — SA-CADRL(rh) 0.46/1.63/1.02; 0.155/0.180; 12/88, 29/71, 30/70.
- Real robot: 10 runs, goals >50 m apart, 1.2 m/s, 10.2 persons within 2 m per minute on average, zero safety-driver interventions (p.7).
- **Data-quality note:** 4-agent SA-CADRL(rh) 75th-percentile t_e (1.63 s) exceeds its 90th percentile (1.02 s) — internally impossible, likely a typo (0.63?).

## N. Limitations
1. **Stated:** trade-off between time-optimality and norm compliance (~20% larger t_e) (p.6); emerging CADRL conventions not consistent with human norms (p.3).
2. **Observable:** norms limited to handedness; real-world evaluation without social metrics or human ratings; reciprocity assumption.
3. **Social relevance:** first explicit learned passing-convention controller; cultural adaptation reduced to left/right handedness.

## P. Learning-based analysis — see `learning:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue 2017 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS); DOI 10.1109/IROS.2017.8202312; pages 1343-1350; URL https://doi.org/10.1109/IROS.2017.8202312.
- Sources: Crossref (exact title match, DOI 10.1109/IROS.2017.8202312); arXiv abs page (1703.08862v2).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - venue: PDF-derived 'IEEE/RSJ IROS 2017 (per citations); corpus copy arXiv v2' -> externally verified '2017 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)'
- Changed field - pages: PDF-derived '8 (PDF); 1343-1350 (per citations)' -> externally verified '1343-1350'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified '10.1109/IROS.2017.8202312'
- Changed field - url: PDF-derived 'https://youtu.be/CK1szio7PyA (video)' -> externally verified 'https://doi.org/10.1109/IROS.2017.8202312'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

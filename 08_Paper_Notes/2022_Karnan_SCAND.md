---
id: 2022_Karnan_SCAND
source_pdfs: [06_Datasets_Benchmarks_Evaluation/scand.pdf]
duplicate_copies: []
related_versions: ['Published: IEEE RA-L 7(4):11807-11814, Oct. 2022 (per multiple corpus citations); arXiv:2203.15041 (cited in corpus); corpus PDF has no journal header']
title: 'Socially CompliAnt Navigation Dataset (SCAND): A Large-Scale Dataset Of Demonstrations For Social Navigation'
authors: &id001 [Haresh Karnan, Anirudh Nair, Xuesu Xiao, Garrett Warnell, Soren Pirk, Alexander Toshev, Justin Hart, Joydeep Biswas, Peter Stone]
year: 2022
venue: IEEE Robotics and Automation Letters
volume: '7'
issue: '4'
pages: 11807-11814
doi: 10.1109/LRA.2022.3184025
url: https://doi.org/10.1109/LRA.2022.3184025
pub_status: journal; benchmark/dataset (corpus copy preprint)
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1109/LRA.2022.3184025); arXiv abs page (2203.15041v2). PDF-derived basis (Stage 1): Corpus PDF lacks venue header; multiple peer-reviewed corpus papers (e.g., VLM-Social-Nav, Fang 2026) cite it as RA-L 7(4) 2022. WEB_VERIFICATION_REQUIRED.'
category: S6
folder: 06_Datasets_Benchmarks_Evaluation
folder_category_match: 'Yes'
category_rationale: Large-scale real-world dataset of socially compliant teleoperated robot navigation demonstrations with social-interaction tags; source of SNEI, SocialNav-SUB, Etiquette fine-tuning data, ViLAM, G2-Nav evaluation.
paper_type: dataset
fm_used: 'No'
fm_class: [None]
fm_models: []
fm_size: NA
method_family: [behavior cloning (validation), demonstrator classification (CNN+MLP)]
roles: []
roles_evidence: {}
integration: NA
integration_rationale: No foundation model.
evidence: E4
evidence_rationale: BC local planner trained on SCAND deployed on Spot and rated by 14 participants (social compliance, safety; one-way ANOVA p<0.001) in static and dynamic indoor scenarios (p.6-7).
inputs: [3D LiDAR, RGB (Kinect), stereo, monocular (Spot), odometry, IMU, joystick commands]
outputs: ['velocity/action (joystick v, omega)']
human_repr: [none annotated (no detection/tracking labels); social interaction tags per trajectory]
capabilities: {C1: Partial, C2: 'No', C3: 'No', C4: 'Yes', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: Partial, C10: Partial, C11: Partial, C12: Partial, C13: Partial, C14: Partial, C15: Partial, C16: Partial, C17: Partial, C18: 'No', C19: 'No', C20: 'No', C21: Partial, C22: 'No', C23: 'No', C24: Partial, C25: 'No'}
exp:
  datasets: ['SCAND: 8.7 h, 138 trajectories, 25 miles (40 km), 2 robots, 4 demonstrators']
  simulators: []
  robots: [Boston Dynamics Spot, Clearpath Jackal]
  environment: UT Austin campus indoor and outdoor; football game days
  indoor_outdoor: both
  sensors: [Velodyne VLP-16 LiDAR (10 Hz), Azure Kinect RGB (20 Hz), IMU (16 Hz), Jackal stereo + wheel odometry, Spot 5 monocular cameras + visual odometry]
  humans: real, naturally occurring pedestrians
  n_scenes: 138 trajectories; 12 interaction tags
  n_trajectories: 138
  n_participants: 4 demonstrators; 14 evaluation participants
  split: Demonstrator classification 12/4 trajectories; BC held-out test (size not given)
  baselines: [move_base (ROS)]
  ablation: 'No'
  real_robot_trials: 'Yes'
  human_study: 'Yes'
  statistical_testing: Yes (one-way ANOVA)
  scenarios: [against traffic, with traffic, street crossing, overtaking, sidewalk, passing conversational groups, blind corner, narrow doorway, crossing stationary queue, stairs, vehicle interaction, large crowds]
metrics: [OTHER | Demonstrator classification accuracy | % | held-out accuracy distinguishing two demonstrators from 10-s sequences | p.5, OTHER | Average Hausdorff distance | m (implied) | between predicted global path and demonstrated path | p.6, HUMAN | Social compliance rating | 1-5 | 'how considerate the robot was of your presence' | p.6, HUMAN | Perceived safety rating | 1-5 | 'how safe did you feel around the robot' | p.6]
deployment: {fm_model: NA, model_size: NA, api_cloud_local: NA, onboard_offboard: Not reported, gpu: Not reported, cpu: Not reported, latency: Not reported, query_frequency: NA, planner_frequency: NA, controller_frequency: NA, asynchronous: NA, caching: NA, event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: NA, safety_shield: NA, emergency_behavior: NA, uncertainty: NA, hallucination_mitigation: NA, real_time_claim_supported: NA}
repro: {code: Not reported, code_url: NA, dataset: Yes (public), dataset_url: www.cs.utexas.edu/~xiao/SCAND/SCAND.html, checkpoints: NA, prompts_published: NA, hardware_specified: 'Yes', hyperparameters: Partial, protocol_described: Partial, project_page: www.cs.utexas.edu/~xiao/SCAND/SCAND.html, concerns: Demonstrators include first two authors; single campus; no human tracks.}
limitations_flags: [dataset-bias, limited-scenarios]
web_verification_required: [RA-L publication details.]
cited_missing: [JRDB, THOR, CoBots dataset, L-CAS, FLOBOT, NCLT, CA-DRL (Everett 2018), APPLD]
dataset: {kind: dataset, real_synthetic: real, size: '8.7 h, 138 trajectories, 25 miles', environments: 'university campus indoor/outdoor (sidewalks, roads, lawns, buildings, stadium area)', sensors: '3D LiDAR, RGB, stereo, monocular, IMU, odometry, joystick', ego_view: 'Yes', rgb: 'Yes', rgbd: Partial (Kinect RGB; depth not stated), lidar: 'Yes', human_trajectories: No (no human annotations), dynamic_humans: Yes (natural), group_ann: 'Partial (tag: passing conversational groups)', intention_ann: 'No', activity_ann: 'No', language_ann: Partial (textual interaction tags), social_rule_ann: Partial (tags such as with/against traffic), preference_ann: 'No', multi_action_ann: 'No (but authors show >1 valid strategy exists: 74.48% demonstrator classification)', personal_space_ann: 'No', site_diversity: 'Single campus (Austin, TX)', closed_loop: No (offline demonstrations), vlm_suitability: Medium-High (egocentric RGB; basis of SNEI/SocialNav-SUB), real_robot_compat: Yes (robot data), standard_metrics: Not
    defined (Hausdorff used for BC), known_limitations: Single city/campus; teleoperated style of few demonstrators; no human labels}
coding: {latency_reported: 'No', safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: 'No', new_dataset_released: 'Yes', real_robot: Systematic, human_subject_study: 'Yes'}
pdf_metadata_stage1:
  year: 2022
  authors: *id001
  venue: IEEE Robotics and Automation Letters (per citing papers); corpus copy is preprint layout
  volume: 7 (per citations)
  issue: 4 (per citations)
  pages: 8 (PDF); 11807-11814 (per citations)
  doi: Not reported
  url: www.cs.utexas.edu/~xiao/SCAND/SCAND.html
  pub_status: journal; benchmark/dataset (corpus copy preprint)
  peer_reviewed: 'Yes'
  peer_review_basis: Corpus PDF lacks venue header; multiple peer-reviewed corpus papers (e.g., VLM-Social-Nav, Fang 2026) cite it as RA-L 7(4) 2022. WEB_VERIFICATION_REQUIRED.
project_url: www.cs.utexas.edu/~xiao/SCAND/SCAND.html
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: IEEE Robotics and Automation Letters
  verified_doi: 10.1109/LRA.2022.3184025
  verified_url: https://doi.org/10.1109/LRA.2022.3184025
  verified_pages: 11807-11814
  arxiv: 2203.15041v2
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1109/LRA.2022.3184025)', arXiv abs page (2203.15041v2)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A6]
  C_capabilities: {SAF1: Partial, SAF2: 'No', SPA1: 'No', SPA2: Partial, SPA3: Partial, SPA4: Partial, HUM1: 'No', HUM2: 'No', NOR1: Partial, NOR2: 'No', NOR3: Partial, NOR4: 'No', EXP1: 'Yes', EXP2: 'No', EXP3: 'No'}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'No', EV3_physical_robot: systematic, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: robot-behaviour evaluation (type not differentiated), EV6_open_world_deployment: 'No'}
physical_source_folder: "06_Datasets_Benchmarks_Evaluation"
analytical_category: "S6"
coding:
  latency_reported: "No"
  safety_mechanism: "NA"
  uncertainty_treatment: "NA"
  hallucination_treatment: "NA"
  code_released: "No"
  new_dataset_released: "Yes"
  real_robot: "Systematic"
  human_subject_study: "Yes"
---

# SCAND (Karnan et al., RA-L 2022)

Page convention: PDF index (p.N).

## A. Bibliographic — Corpus PDF (8 pp.) without journal header; cited across corpus as RA-L 7(4):11807–11814, 2022. UT Austin, Google, ARL, Sony AI. Dataset at www.cs.utexas.edu/~xiao/SCAND/SCAND.html. IRB STUDY00002561/2562 (p.7).

## B. Position — S6 (dataset). Foundational *data source* for the VLM social-navigation line: SNEI (Social-LLaVA), SocialNav-SUB, Etiquette's fine-tuning set, ViLAM, G2-Nav, BC baselines (VLM-Social-Nav). (AutoSpatial uses CODa, not SCAND.).

## C. Research problem — lack of large-scale in-the-wild datasets of socially compliant robot demonstrations for IL/IRL (p.1–2). Contributions: SCAND; evidence of multiple socially compliant strategies; BC global+local planner learned from SCAND (p.2).

## D. Method — 4 demonstrators teleoperate from ~2 m behind robot; campus peak hours; Spot v ∈ [0,1.6] m/s, Jackal [0,2.0] m/s; 12 social interaction tags (Table II) (p.3–4). Demonstrator classifier (12/4 trajectories) and BC (BEV LiDAR + odometry + IMU + move_base prior → 200-point global path + 20-step (v,ω)) (p.5–6).

## L. Quantitative results
- Table I comparison (p.3): SCAND 138 traj., 40 km, 522 min, teleoperated, 2 robots, indoor+outdoor; JRDB 54 traj., 64 min; THÖR 60 min, autonomous, indoor; CoBot 1082 traj., 131 km, 15,600 min.
- Tags (Table II): Against Traffic 22; With Traffic 74; Street Crossing 34; Overtaking 14; Sidewalk 57; Passing Conversational Groups 38; Blind Corner 6; Narrow Doorway 15; Crossing Stationary Queue 6; Stairs 22; Vehicle Interaction 21; Large Crowds 27.
- Demonstrator classification accuracy 74.48% (chance 50%) (p.5).
- Average Hausdorff: move_base 1.25 vs BC 0.26 (p.6).
- User study (14 participants; static and dynamic scenarios): social compliance BC mean 4.39 (sd 0.99) vs move_base 2.86 (sd 0.82); safety 4.71 (0.70) vs 2.89 (1.18); one-way ANOVA safe F(1,55) = 47.87, p < 0.001; compliant F(1,55) = 38.67, p < 0.001 (p.6).

## N. Limitations — 1. Stated: BC handles simple scenarios only; rarer interactions; representation learning and real-to-sim future work (p.7). 2. Observable: demonstrators include authors; single campus; no human annotations; baseline move_base not socially designed.

## P. Dataset analysis — see `dataset:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue IEEE Robotics and Automation Letters; DOI 10.1109/LRA.2022.3184025; pages 11807-11814; URL https://doi.org/10.1109/LRA.2022.3184025.
- Sources: Crossref (exact title match, DOI 10.1109/LRA.2022.3184025); arXiv abs page (2203.15041v2).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - venue: PDF-derived 'IEEE Robotics and Automation Letters (per citing papers); corpus copy is preprint layout' -> externally verified 'IEEE Robotics and Automation Letters'
- Changed field - volume: PDF-derived '7 (per citations)' -> externally verified '7'
- Changed field - issue: PDF-derived '4 (per citations)' -> externally verified '4'
- Changed field - pages: PDF-derived '8 (PDF); 11807-11814 (per citations)' -> externally verified '11807-11814'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified '10.1109/LRA.2022.3184025'
- Changed field - url: PDF-derived 'www.cs.utexas.edu/~xiao/SCAND/SCAND.html' -> externally verified 'https://doi.org/10.1109/LRA.2022.3184025'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

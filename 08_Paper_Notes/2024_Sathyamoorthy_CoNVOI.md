---
id: 2024_Sathyamoorthy_CoNVOI
source_pdfs: [04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/2403.15637v1.pdf]
duplicate_copies: []
related_versions: ['Published version: IEEE/RSJ IROS 2024, pp.13837-13844 (as cited by Fang et al. RA-L 2026 [7] and Wang et al. MAction [5]); NOT in corpus']
title: 'CoNVOI: Context-aware Navigation using Vision Language Models in Outdoor and Indoor Environments'
authors: &id001 [Adarsh Jagan Sathyamoorthy, Kasun Weerakoon, Mohamed Elnoor, Anuj Zore, Brian Ichter, Fei Xia, Jie Tan, Wenhao Yu, Dinesh Manocha]
year: 2024
venue: 2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
volume: NA
issue: NA
pages: 13837-13844
doi: 10.1109/IROS58592.2024.10802716
url: https://doi.org/10.1109/IROS58592.2024.10802716
pub_status: conference (corpus copy is preprint)
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1109/IROS58592.2024.10802716); arXiv abs page (2403.15637v1). PDF-derived basis (Stage 1): Corpus PDF is arXiv v1 (22 Mar 2024) with no venue. Two peer-reviewed corpus papers cite it as IROS 2024 pp.13837-13844. Treat published version as authoritative; numbers here are from the preprint. WEB_VERIFICATION_REQUIRED.'
category: S4
folder: 04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core
folder_category_match: Partial
category_rationale: VLM generates context-dependent reference paths including social behaviours (do not pass between people, keep right in corridors, use crosswalks) on real robots; however much of the evaluation concerns terrain/crosswalk context rather than human interaction (boundary case).
paper_type: method
fm_used: 'Yes'
fm_class: [VLM, CLIP-style]
fm_models: ['CLIP (context classification, local)', GPT-4V (API), Gemini (API)]
fm_size: Not reported
method_family: [zero-shot prompting, visual prompting (marked numbers), context classification, DWA-based local planning]
roles: [F1, F4, F9]
roles_evidence: {F1: 'CLIP zero-shot classifies context (indoor corridor, people, outdoor terrain, crosswalk) (p.4).', F4: 'Context-specific behaviour text prompts (''keep close to the right wall'', ''move on pavement'') chosen per context (p.4).', F9: 'Large VLM selects marker numbers in free space -> reference path waypoints (Eq.4, p.5).'}
integration: I5
integration_rationale: VLM outputs a reference path (sequence of marked free-space points) that a modified DWA follows via a lateral reference cost (Eq.5-6, p.5).
evidence: E3
evidence_rationale: Closed-loop navigation on Turtlebot 2 (indoor) and Spot (outdoor) compared with human teleoperation and baselines; no human-subject study (p.5-7).
inputs: [RGB, 2D/3D LiDAR, occupancy/grid map, natural language behaviour prompt]
outputs: [semantic labels (context class), waypoint/reference path (marker list), velocity/action (via DWA)]
human_repr: [obstacle in occupancy grid, implicit semantic interpretation of people in image (VLM)]
capabilities: {C1: Partial, C2: 'No', C3: 'No', C4: 'No', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: Partial, C10: Partial, C11: Partial, C12: 'No', C13: Partial, C14: 'No', C15: 'Yes', C16: 'No', C17: 'No', C18: 'No', C19: 'No', C20: Partial, C21: 'No', C22: 'No', C23: Partial, C24: 'Yes', C25: 'No'}
exp:
  datasets: []
  simulators: []
  robots: [Turtlebot 2 (indoor), Boston Dynamics Spot (outdoor)]
  environment: indoor corridors, indoor scenes with people, outdoor multi-terrain, outdoor crosswalks, detour-sign scenario
  indoor_outdoor: both
  sensors: [Velodyne VLP16 LiDAR, Zed 2i camera]
  humans: real people in some scenes (number not reported)
  n_scenes: 4 scenario types + novel detour scenario
  n_trajectories: Not reported
  n_participants: Not reported
  split: NA
  baselines: [DWA, Frozone (enhanced with right-side corridor cost), GA-Nav, PSP-Net, human teleoperation (reference)]
  ablation: Yes (without multi-modal visual marking; without context-based prompting; GPT-4V vs Gemini)
  real_robot_trials: 'Yes'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [narrow corridor, conversational group/people (not moving between), crosswalk, sidewalk/pavement, outdoor terrain, detour sign]
metrics: [OTHER | Frechet Distance w.r.t. Human Teleoperation | m (implied) | Frechet distance between method and teleoperated trajectories | p.6, NAV | Normalized Trajectory Length | ratio (~1 ideal) | trajectory length / straight-line distance | p.6, NAV | Mean Velocity | m/s | robot linear velocity averaged over trials | p.6, VLM | Reference Path Error | m (implied) | distance between mean points of GT and VLM reference path | p.6, VLM | Cosine Similarity | unitless | orientation alignment of GT and VLM reference path | p.6, 'VLM | % Unacceptable Paths | fraction | reference path on unacceptable terrain/location (obstacle, road with traffic) | p.6', DEPLOY | Inference Time | s | query-to-reference-path time incl. network latency | p.6]
deployment: {fm_model: GPT-4V / Gemini (API) + CLIP (local), model_size: Not reported, api_cloud_local: Cloud API for large VLM; CLIP local, onboard_offboard: 'Laptop (Intel i7 11th gen, RTX 3060) on robot + remote VLM', gpu: RTX 3060 (laptop), cpu: Intel i7 11th gen, latency: Inference time 3.28-6.36 s across configurations (Table I); t_query assumed 5 s, query_frequency: Re-query only on context change or failed extrapolation; extrapolation reduces requerying by ~50% in static-context environments (p.7), planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Partial (DWA follows last reference path while waiting), caching: Reference path extrapolation, event_triggered: Yes (CLIP context change), distillation: 'No', quantization: 'No', fallback_planner: Baseline DWA when no reference path received (p.8), safety_shield: DWA collision-free velocity set; markers only in free space, emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: 'Prompt
    phrase instructing VLM to treat each query as new task, after observing pattern hallucinations (p.8)', real_time_claim_supported: 'Partial: v_max limited to 0.3 m/s because of 3-6 s VLM latency'}
repro: {code: Stated available on project site, code_url: 'http://gamma.umd.edu/convoi/', dataset: NA, dataset_url: NA, checkpoints: NA, prompts_published: Partial (prompt template p.4), hardware_specified: 'Yes', hyperparameters: 'Yes (n=200, alpha1..4, l, m, d_row, d_col, k=5, v_max, t_query, d_thresh, n_pat)', protocol_described: Partial (number of trials not reported), project_page: 'http://gamma.umd.edu/convoi/', concerns: Trials count unreported; closed APIs; preprint vs published numbers may differ.}
limitations_flags: [latency, cloud-dependence, hallucination, prompt-sensitivity, spatial-reasoning-failure, limited-scenarios, no-human-study]
web_verification_required: [Confirm IROS 2024 publication details and whether results changed from arXiv v1.]
cited_missing: [Frozone (RA-L 2020), CoMet group cohesion (RA-L 2022), GA-Nav, Semantic guesswork LFG (CoRL 2023), A2Nav, OK-Robot, CLIP-Nav, PIVOT, Lu & Smart 2013, Guzzi 2013 human-friendly navigation, Mehta 2016 MPDM]
coding: {latency_reported: 'Yes', safety_mechanism: 'Yes', uncertainty_treatment: 'No', hallucination_treatment: Partial, code_released: 'Yes', new_dataset_released: NA, real_robot: Systematic, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2024
  authors: *id001
  venue: arXiv:2403.15637v1 (corpus copy); published IROS 2024 per citing papers
  volume: Not reported
  issue: Not reported
  pages: 9 (arXiv PDF); 13837-13844 (IROS, per citations)
  doi: Not reported
  url: http://gamma.umd.edu/convoi/
  pub_status: conference (corpus copy is preprint)
  peer_reviewed: 'Yes'
  peer_review_basis: Corpus PDF is arXiv v1 (22 Mar 2024) with no venue. Two peer-reviewed corpus papers cite it as IROS 2024 pp.13837-13844. Treat published version as authoritative; numbers here are from the preprint. WEB_VERIFICATION_REQUIRED.
project_url: http://gamma.umd.edu/convoi/
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: 2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
  verified_doi: 10.1109/IROS58592.2024.10802716
  verified_url: https://doi.org/10.1109/IROS58592.2024.10802716
  verified_pages: 13837-13844
  arxiv: 2403.15637v1
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1109/IROS58592.2024.10802716)', arXiv abs page (2403.15637v1)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A6]
  C_capabilities: {SAF1: Partial, SAF2: 'No', SPA1: 'No', SPA2: Partial, SPA3: 'Yes', SPA4: 'No', HUM1: 'No', HUM2: 'No', NOR1: Partial, NOR2: Partial, NOR3: 'Yes', NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: Partial}
  B_roles: [R1, R3]
  D_interface: [D4]
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'No', EV3_physical_robot: systematic, EV4_real_humans_in_trials: present-type-unreported, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: Not reported, statistical_testing: 'No', cross_environment: 'Yes', runtime_measured: 'Yes'}
  cross_cutting: {temporal_coupling: per-decision, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'Yes', uncertainty: 'No', hallucination_mitigation: Partial, privacy_constraint: 'No', inference_location: hybrid (local + cloud)}
physical_source_folder: "04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core"
analytical_category: "S4"
coding:
  latency_reported: "Yes"
  safety_mechanism: "Yes"
  uncertainty_treatment: "No"
  hallucination_treatment: "Partial"
  code_released: "Yes"
  new_dataset_released: "NA"
  real_robot: "Systematic"
  human_subject_study: "No"
---

# CoNVOI (Sathyamoorthy et al., arXiv 2024 / IROS 2024)

Page convention: PDF index (p.N) of arXiv v1.

## A. Bibliographic
Corpus file `04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/2403.15637v1.pdf` = arXiv v1 (22 Mar 2024). Authors UMD + Google DeepMind. Published at IROS 2024 pp.13837–13844 per two citing corpus papers — authoritative version not in corpus (WEB_VERIFICATION_REQUIRED). Project page http://gamma.umd.edu/convoi/.

## B. Position — S4 (boundary)
Uses VLMs to choose *how* to navigate in context, including social behaviours (not moving between people, keeping right) as well as terrain/crosswalk behaviours. The social component is one of several contexts; evaluation does not isolate social metrics. Our classification: direct but terrain-heavy; useful as an early (2024) example of VLM path generation in human environments.

## C. Research problem
- **Problem (authors):** "what navigation behaviors should a robot exhibit in its current local environmental context" (p.3); existing VLM work focuses on *where* (targets), not *how* (p.3).
- **Contributions (p.2):** context-based prompting (CLIP context → behaviour prompt → large VLM); multi-modal visual marking of obstacle-free regions from occupancy grid; reference trajectory extrapolation to reduce queries; real-robot integration without fine-tuning.

## D. Technical method
- CLIP classifies context among k=5 contexts with "This is a picture of c_i"; behaviour b_max selected (p.4).
- Free-space candidate grid points (l rows × m columns; l = 2 outdoors / 3 indoors, m = 6; d_row 2.5 m, d_col 2 m) with line-of-sight check against obstacles; projected to image and numbered (Eq.2–3) (p.4–5, p.5 params).
- Large VLM (GPT-4V or Gemini, online API) given marked image + prompt "You are navigating a robot in this scenario... Pick a list of numbers ... such that the robot ___" → marker list M_ref → reference path (Eq.4).
- Path following: DWA objective Q1 (heading, obstacle, velocity) + α4·lateral reference cost when goal within camera FOV (Eq.5–6).
- Extrapolation: if context unchanged and close to path end, linearly extend; CLIP checks patch "paved/unpaved"; otherwise re-query (p.5).

## E. Human/social representation — humans only as occupancy obstacles plus VLM image understanding; no tracking or prediction.

## F. Roles — F1 (CLIP), F4, F9.

## G. Social capabilities
C1 Partial (DWA collision-free set; collisions not reported) · C9/C10 Partial (qualitative: not moving between people, Fig.3; % unacceptable paths in Scenario 2) · C11, C13 Partial (keep to right side in corridor) · C15 Yes (crosswalk/pavement scenarios with metrics) · C20 Partial (Fréchet similarity to human teleoperation) · C23 Partial (new behaviours via prompt, e.g., detour sign) · C24 Yes (context-dependent behaviour is the core) · others No.

## H. Integration — I5. ## I. Evidence — E3.

## J. Experimental evidence
Turtlebot 2 (indoor), Spot (outdoor), VLP16 + Zed 2i, laptop i7-11th + RTX 3060; GPT-4V/Gemini via online API (p.5). Scenarios: 1 indoor corridors; 2 indoor with people; 3 outdoor multi-terrain; 4 outdoor crosswalks; plus detour-sign demo. Baselines: DWA, Frozone (enhanced), GA-Nav, PSP-Net. Number of trials not reported.

## K. Metrics — see front matter.

## L. Quantitative results
Table I (p.7) ablation — Reference Path Error / Cosine / % Unacceptable / Inference Time (s):
- Scen.1: Gemini w/o MMVM 1.442/0.926/0.857/5.24; GPT4 w/o MMVM 1.576/0.913/0.913/4.86; Gemini w/o CbP 0.315/0.995/0.0/4.78; GPT4 w/o CbP 0.335/0.993/0.0/4.10; Gemini CoNVOI 0.202/0.996/0.0/3.76; GPT4 CoNVOI 0.187/0.995/0.0/3.48.
- Scen.2: 1.425/0.914/0.786/5.11; 2.325/0.802/0.798/4.69; 0.484/0.989/0.278/4.91; 0.589/0.988/0.223/4.46; Gemini CoNVOI 0.444/0.981/0.111/3.55; GPT4 CoNVOI 0.456/0.991/0.167/3.28.
- Scen.3: 0.891/0.973/0.433/6.35; 0.865/0.977/0.366/5.60; 0.817/0.978/0.291/6.28; 0.872/0.971/0.125/5.46; Gemini CoNVOI 0.979/0.970/0.125/4.88; GPT4 CoNVOI 0.785/0.975/0.083/4.15.
- Scen.4: 1.210/0.957/0.285/6.36; 1.205/0.966/0.190/4.89; 1.229/0.938/0.223/5.98; 1.159/0.962/0.166/4.95; Gemini CoNVOI 1.205/0.977/0.055/5.26; GPT4 CoNVOI 0.819/0.978/0.055/4.83.
- (Row order within each scenario: Gemini w/o MMVM w. CbP; GPT4 w/o MMVM w. CbP; Gemini w. MMVM w/o CbP; GPT4 w. MMVM w/o CbP; Gemini CoNVOI; GPT4 CoNVOI.)
- Note: text claims "lowest path errors ... highest cosine similarity for CoNVOI ... in all cases" (p.7), but e.g. Scen.2 Gemini CoNVOI error 0.444 vs GPT4 CoNVOI 0.456 and Scen.3 Gemini CoNVOI 0.979 > ablations; claim holds per-model-best only loosely.
Table II (p.7) — Fréchet / Norm. traj. length / Mean velocity (m/s):
- Scen.1: DWA 0.864/1.082/0.395; Frozone 0.577/1.239/0.392; CoNVOI 0.521/1.207/0.289.
- Scen.2: DWA 1.087/1.105/0.390; Frozone 0.866/1.187/0.388; CoNVOI 0.709/1.194/0.276.
- Scen.3: DWA 2.475/1.067/0.485; PSP-Net 2.188/1.121/0.458; GA-Nav 1.957/1.160/0.473; CoNVOI 1.083/1.213/0.238.
- Scen.4: DWA 2.095/1.091/0.491; PSP-Net 2.068/1.089/0.455; GA-Nav 2.157/1.112/0.466; CoNVOI 0.863/1.237/0.243.
Abstract summary: 9.7–58.2% closer Fréchet; up to 88.13% lower path error; up to 86.09% fewer unacceptable paths. Requery reduction ~50% (p.7).

## M. Deployment — remote API, 3.3–6.4 s inference, v_max capped 0.3 m/s; fallback to DWA when network fails (p.8).

## N. Limitations
1. **Stated (p.8):** remote VLM processing + network latency limit velocity; outdoor network failures → fallback planner; limits use in highly dynamic crowded environments; sensitivity to vague prompt terms; no global information (e.g., crosswalk not visible); VLM hallucination patterns with similar sequential images; wavy trajectories from multiple valid paths and marker spacing; current VLMs cannot reliably do zero-shot obstacle avoidance (p.7).
2. **Future work:** long-range navigation; global information (p.8).
3. **Observable:** trial counts unreported; no per-scenario human-proximity metric; social scenario evaluated via path similarity to teleoperation only.
4. Deferred.

## O. Reproducibility — parameters listed; code/video at project site (to verify).

## P. Direct-paper questions
1 Context-appropriate local behaviour (social and terrain). 2 Generalisable semantic reasoning across contexts (p.2). 3 CLIP + GPT-4V/Gemini. 4 Marked RGB image. 5 Context-specific behaviour prompt. 6 List of marker numbers. 7 Markers → grid points → reference path → DWA lateral cost. 8 No. 9 DWA. 10 DWA collision-free velocities; markers in free space. 11 Social rules (not passing between people, keep right, crosswalks). 12 Path similarity to teleop; unacceptable paths. 13 No. 14 Implicitly. 15 No. 16 No. 17 Prompted. 18 No (single image). 19 No. 20 Observed and mitigated by prompt. 21 3–6 s; v_max 0.3 m/s. 22 Partly (laptop + cloud). 23 Yes (people present). 24 No. 25 Fréchet/unacceptable-path reductions. 26 Cannot conclude: human comfort, proxemic compliance, behaviour among moving crowds.

## Q. Cited works possibly missing — Frozone; CoMet; LFG semantic guesswork; A2Nav; OK-Robot; CLIP-Nav; PIVOT.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue 2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS); DOI 10.1109/IROS58592.2024.10802716; pages 13837-13844; URL https://doi.org/10.1109/IROS58592.2024.10802716.
- Sources: Crossref (exact title match, DOI 10.1109/IROS58592.2024.10802716); arXiv abs page (2403.15637v1).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - venue: PDF-derived 'arXiv:2403.15637v1 (corpus copy); published IROS 2024 per citing papers' -> externally verified '2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)'
- Changed field - volume: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - issue: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - pages: PDF-derived '9 (arXiv PDF); 13837-13844 (IROS, per citations)' -> externally verified '13837-13844'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified '10.1109/IROS58592.2024.10802716'
- Changed field - url: PDF-derived 'http://gamma.umd.edu/convoi/' -> externally verified 'https://doi.org/10.1109/IROS58592.2024.10802716'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

---
id: 2026_Fang_Obstacles-to-Etiquette
source_pdfs: [04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/From_Obstacles_to_Etiquette_Robot_Social_Navigation_With_VLM-Informed_Path_Selection.pdf]
duplicate_copies: []
related_versions: []
title: 'From Obstacles to Etiquette: Robot Social Navigation With VLM-Informed Path Selection'
authors: &id001 [Zilin Fang, Anxing Xiao, David Hsu, Gim Hee Lee]
year: 2026
venue: IEEE Robotics and Automation Letters
volume: '11'
issue: '4'
pages: 3947-3954
doi: 10.1109/LRA.2026.3662586
url: https://doi.org/10.1109/LRA.2026.3662586
pub_status: journal
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1109/LRA.2026.3662586); arXiv abs page (2602.09002v1). PDF-derived basis (Stage 1): Received 23 Aug 2025; accepted 18 Jan 2026; recommended by AE upon evaluation of reviewers'' comments (p.1).'
category: S4
folder: 04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core
folder_category_match: 'Yes'
category_rationale: A fine-tuned VLM selects the most socially compliant of several geometrically feasible candidate paths projected into the image; closed-loop on a Spot robot.
paper_type: method
fm_used: 'Yes'
fm_class: [VLM]
fm_models: ['Qwen-2.5(-VL) 7B fully fine-tuned (deployed, 4-bit vLLM)', GPT-4o (teacher/labeler)]
fm_size: 7B (student)
method_family: [visual prompting, supervised fine-tuning, distillation (GPT-4o -> Qwen), trajectory prediction (NMRF), A* with anchors, ORCA-based reactive control]
roles: [F1, F2, F4, F5, F8]
roles_evidence: {F5: VLM evaluates 3-6 projected candidate paths and selects one via multiple-choice with justification (p.5)., F8: 'GPT-4o labels SCAND frames (4,851 train / 574 val image-selection pairs) to fine-tune Qwen-2.5 7B - distillation of social reasoning (p.5).', F1: 'VLM interprets the scene (ladder worker, photographers, queue) (Fig.7).', F2: Prompt asks VLM to infer likely human motions and interactions from posture and context (p.5)., F4: 'Output includes social-norm justification of path choice (p.5, Fig.6).'}
integration: I3
integration_rationale: VLM ranks/selects among planner-generated candidate paths; selected path is a reference from which the closest current candidate is retrieved and tracked by a modified ORCA controller (p.4-6).
evidence: E3
evidence_rationale: Closed-loop real-robot (Boston Dynamics Spot) experiments in 4 controlled scenarios with human actors, 3 trials per method, 5 baselines; no human-subject perception study (p.6-7).
inputs: [RGB (fisheye), LiDAR point cloud, odometry, human tracks, predicted trajectories, candidate paths (projected into image), natural language prompt]
outputs: [path ranking/selection, natural-language reasoning (path descriptions + justification), velocity/action (via ORCA)]
human_repr: [2D detection + ByteTrack track, 3D position via LiDAR registration, dynamic vs pseudo-static human, 'stochastic predicted trajectories (20 samples, 2.4 s)', prediction-fused costmap, ORCA velocity-obstacle agent, VLM semantic interpretation of activity/relationship]
capabilities: {C1: 'Yes', C2: Partial, C3: 'Yes', C4: 'No', C5: 'Yes', C6: 'Yes', C7: Partial, C8: 'Yes', C9: 'Yes', C10: 'Yes', C11: 'Yes', C12: Partial, C13: 'No', C14: 'No', C15: 'No', C16: 'Yes', C17: 'No', C18: Partial, C19: Not reported, C20: Not reported, C21: Not reported, C22: Not reported, C23: 'No', C24: 'Yes', C25: 'No'}
exp:
  datasets: ['SCAND (fine-tuning data: 4,851 train / 574 val image-selection pairs, labelled by GPT-4o)']
  simulators: []
  robots: [Boston Dynamics Spot]
  environment: indoor controlled scenes (glass wall, corridor, vending machine)
  indoor_outdoor: indoor
  sensors: [ELP fisheye monocular RGB, Hesai JT16 LiDAR, robot odometry]
  humans: real actors at pre-designed positions/directions
  n_scenes: 4 scenarios
  n_trajectories: 3 trials per method per scenario
  n_participants: Not reported
  split: 4,851/574 train/val for fine-tuning
  baselines: [G-MPC, AttnGraph-RL (Attention-based interaction graph), ViNT, VLM-Social-Nav, GSON]
  ablation: Yes (shortest visible path vs VLM-Social-Nav decision alignment; prediction horizon vs group interruption)
  real_robot_trials: 'Yes'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [static person (ladder / fall hazard), conversational group walking (walking-talk), photography (line of sight), queue]
metrics: [NAV | Navigation Time (NT) | s | total time to reach goal; 90 s if goal not reached within 90 s | p.6, SOCIAL | Personal Space Violation duration (PSV) | s | time within 0.25 m of any person | p.6, SOCIAL | Time Facing Pedestrians (TFP) | s | duration robot faces pedestrian within 30 deg cone and 3 m | p.6, SOCIAL | Social-zone Interruption Time (SIT) | s | total time robot occupies any social zone | p.7, SOCIAL | Maximum Social-zone Interruption Ratio (Max. SIR) | % | largest overlap area of Spot footprint (0.5x1.1 m) to social-zone area; zone = 1.8 m square (ladder) or area between interacting people | p.7, OTHER | Path/Direction alignment | count | agreement of shortest-visible-path selections with VLM-Social-Nav action decisions | p.7, SOCIAL | Group Interrupt. | % | fraction of 36 sampled pre-clustering paths intersecting group regions per prediction horizon | p.7]
deployment: {fm_model: Qwen-2.5 7B fine-tuned, model_size: 7B, api_cloud_local: Local network server (H100) via vLLM, onboard_offboard: Offboard VLM (H100 server); onboard NVIDIA Jetson Orin for rest of navigation, gpu: H100 (VLM inference); 2x H100 (training); Jetson Orin onboard, cpu: Not reported, latency: Not reported numerically, query_frequency: Not reported, planner_frequency: Not reported (continuous replanning), controller_frequency: Not reported ('high-frequency low-level controller'), asynchronous: Yes (path selection decoupled from velocity control; selected path used as reference to retrieve closest current candidate), caching: Selected path reused as reference, event_triggered: Not reported, distillation: Yes (GPT-4o -> Qwen-2.5 7B), quantization: Yes (4-bit at inference), fallback_planner: Candidates always collision-free from prediction-fused costmap; ORCA reactive control, safety_shield: Geometric feasibility enforced before VLM; modified ORCA with velocity-guided responsibility,
  emergency_behavior: Not reported, uncertainty: Stochastic trajectory prediction (20 samples) in costmap; no VLM uncertainty, hallucination_mitigation: VLM can only choose among collision-free candidates; constrained output format, real_time_claim_supported: 'Partial: claims real-time adaptation; no latency or rate measurements'}
repro: {code: Not reported in paper, code_url: Not reported, dataset: 'No (fine-tuning pairs derived from SCAND, release not stated)', dataset_url: NA, checkpoints: Not reported, prompts_published: Partial (Fig.6 example), hardware_specified: 'Yes', hyperparameters: 'Partial (prediction horizon, anchors, 3-6 candidates; training hyperparameters not given)', protocol_described: 'Yes (scenarios, metrics defined)', project_page: path-etiquette.github.io, concerns: 3 trials per scenario; approximate LiDAR-camera calibration for SCAND labels; latency not measured.}
limitations_flags: [temporal-inconsistency, intention-ambiguity, limited-scenarios, no-human-study, resource-requirements]
web_verification_required: [Check project page for code release.]
cited_missing: [PIVOT, Pedestrian VLM for intention prediction (Munir 2025), MOSU (ISER 2025), SicNAV, Mixed strategy Nash equilibrium crowd navigation, Winding through (topological invariance), DenseCAvoid, Decentralized structural-RNN, SELFI, Multi-agent dynamic relational reasoning (Li 2024), DR-MPC, Hierarchical open-vocabulary 3D scene graphs, Interactive navigation traversable obstacles LLM/VLM (Zhang 2024), Neuralized MRF trajectory prediction (ICLR 2025), Arena 3.0, Attention-based interaction graph (Liu ICRA 2023), GMPC]
coding: {latency_reported: 'No', safety_mechanism: 'Yes', uncertainty_treatment: Partial, hallucination_treatment: 'Yes', code_released: 'No', new_dataset_released: 'No', real_robot: Systematic, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2026
  authors: *id001
  venue: IEEE Robotics and Automation Letters
  volume: '11'
  issue: '4'
  pages: 3947-3954
  doi: 10.1109/LRA.2026.3662586
  url: path-etiquette.github.io
  pub_status: journal
  peer_reviewed: 'Yes'
  peer_review_basis: Received 23 Aug 2025; accepted 18 Jan 2026; recommended by AE upon evaluation of reviewers' comments (p.1).
project_url: path-etiquette.github.io
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: IEEE Robotics and Automation Letters
  verified_doi: 10.1109/LRA.2026.3662586
  verified_url: https://doi.org/10.1109/LRA.2026.3662586
  verified_pages: 3947-3954
  arxiv: 2602.09002v1
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1109/LRA.2026.3662586)', arXiv abs page (2602.09002v1)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A2, A3, A5]
  C_capabilities: {SAF1: 'Yes', SAF2: Partial, SPA1: 'Yes', SPA2: 'Yes', SPA3: 'Yes', SPA4: 'No', HUM1: Partial, HUM2: 'Yes', NOR1: 'Yes', NOR2: 'No', NOR3: 'Yes', NOR4: 'No', EXP1: 'No', EXP2: Partial, EXP3: 'No'}
  B_roles: [R2, R3]
  D_interface: [D2, D7]
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'No', EV3_physical_robot: systematic, EV4_real_humans_in_trials: staged, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: 3 trials per method per scenario, statistical_testing: 'No', cross_environment: No/unclear, runtime_measured: 'No'}
  cross_cutting: {temporal_coupling: asynchronous, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'Yes', uncertainty: Partial, hallucination_mitigation: 'Yes', privacy_constraint: 'No', inference_location: remote server}
physical_source_folder: "04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core"
analytical_category: "S4"
coding:
  latency_reported: "No"
  safety_mechanism: "Yes"
  uncertainty_treatment: "Partial"
  hallucination_treatment: "Yes"
  code_released: "No"
  new_dataset_released: "No"
  real_robot: "Systematic"
  human_subject_study: "No"
---

# From Obstacles to Etiquette (Fang, Xiao, Hsu, Lee — RA-L 2026)

Page convention: PDF index (p.N); printed pp.3947–3954.

## A. Bibliographic
`04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/From_Obstacles_to_Etiquette_...pdf`. IEEE RA-L 11(4):3947–3954, Apr 2026. DOI 10.1109/LRA.2026.3662586. Received 23 Aug 2025, accepted 18 Jan 2026. Project page path-etiquette.github.io. Journal; peer-reviewed.

## B. Position — S4
Propose-then-select architecture: geometric planner proposes collision-free paths; a fine-tuned VLM acts as a socially informed path critic. Explicitly compared against VLM-Social-Nav and GSON on a real robot — one of few direct head-to-head comparisons among FM social-navigation methods.

## C. Research problem
- **Problem:** collision-free paths may still interfere with ongoing activities or norms; need common-sense social reasoning integrated into planning (abstract).
- **Critique of prior VLM work (authors, p.1, p.3):** symbolic-level reasoning (group relationships, image goals, intention, action scoring) fails to capture execution effects; frequent large-VLM queries are slow; CoNVOI prompt-specific; VLM-Social-Nav immediate actions only; GSON overlooks norms when explicit groups absent; OLiVia-Nav coarse alignment.
- **Formulation (Eq.1, p.3):** multi-objective path optimisation over c(τ) and c_social(τ, {τ̃_j}); assumption that objective is decomposable and semantic optima form a "well-covered subset of the geometric-optimal set".
- **Claims:** best overall performance, lowest PSV duration, minimal TFP, no social-zone intrusions (abstract).
- **Our check of Table I:** "no social-zone intrusions" (SIT = 0, Max SIR = 0 in all four scenarios) is supported. "Lowest PSV" and "minimal TFP" are not uniformly true: Queuing PSV VLM-Social-Nav 0.00 < Ours 0.33 (but VLM-Social-Nav failed to reach goal, NT 90); Walking-talk TFP AttnGraph-RL 1.66 < Ours 1.80; Queuing TFP GSON 2.36 < Ours 2.70.

## D. Technical method
- **Human motion extraction (p.4):** YOLOv10 on RGB → ByteTrack (40-frame buffer) → LiDAR depth registration (project points, KMeans k=3 on box mask, dominant cluster) → dynamic vs pseudo-static humans; temporal smoothing with max-velocity constraint.
- **Prediction-fused costmap (p.4):** Neuralized MRF stochastic trajectory predictor [39] (ego robot as graph node), 2.4-s horizon, 20 samples; temporal decay weights 0.8→0.1; bin counting + Gaussian smoothing overlaid on LiDAR obstacle map.
- **Path planning (p.4):** A* via Poisson-disk-sampled anchors in a rectangle toward goal; cluster by Hausdorff distance, keep 3–6 candidates; project onto RGB image; continuous replanning; VLM selection used as reference → retrieve closest current candidate.
- **Social-compliance selection (p.5):** visual prompting; output = one-sentence description per path + explicit choice + justification (structured CoT). GPT-4o with rich instructions; Qwen-2.5 with simplified prompts, RGB only.
- **Distillation/fine-tuning (p.5):** SCAND frames; goal direction from future 6-s trajectory ±10°, goal 13–14.5 m; paths planned on Velodyne Puck maps, projected with approximate calibration; 1 Hz downsampling, frames without humans removed → 4,851 train / 574 val; full-model SFT of Qwen-2.5 7B on 2× H100; inference via vLLM 4-bit on H100 server.
- **Local reactive controller (p.6):** ORCA with velocity-vector-guided responsibility (robot takes >½ responsibility when pedestrian approaches along line connecting agents).
- INPUT/OUTPUT: see front matter.

## E. Human/social representation
Tracked 3D humans; stochastic multi-sample predicted trajectories rasterised into costmap (implicit personal space/future blocking); ORCA agents; VLM's implicit understanding of activities (ladder work, photography, conversation, queue) and relationships; social zones defined only for evaluation.

## F. Roles — F5 (primary), F8, F1, F2, F4.

## G. Social capabilities
C1 Yes (collision-free; AttnGraph-RL collided, p.7) · C2 Partial (PSV <0.25 m is effectively near-contact) · C3 Yes (PSV) · C5, C6 Yes (prediction-fused costmap; horizon ablation) · C7 Partial (prompted posture/context inference) · C8 Yes (ladder wiping, photography, queuing activities drive behaviour) · C9, C10 Yes (walking-talk group, photographer–model line of sight; SIT/SIR) · C11 Yes · C12 Partial · C16 Yes (queue scenario) · C18 Partial (TFP as proxy for not confronting pedestrians) · C24 Yes (context-specific expected behaviours) · C4, C13–C15, C17, C23, C25 No · C19–C22 Not reported.

## H. Integration — I3. ## I. Evidence — E3.

## J. Experimental evidence
Spot robot; Jetson Orin onboard (VLM excluded); Qwen served on H100 (p.6). Four scenarios with expected behaviours: (a) wiping glass wall on ladder — wide detour (social zone 1.8 m square); (b) walking-talk — not pass between conversing pair; (c) photography — do not cross photographer–model line of sight; (d) queuing — do not cut line. 3 trials per method; official implementations of baselines where available; VLM-Social-Nav reimplemented with authors' perception module (p.6).

## K. Metrics — NT, PSV, TFP, SIT, Max SIR (definitions in front matter); ablation metrics.

## L. Quantitative results (Table I, p.6, visually verified; average of 3 trials; NT=90 if goal not reached in 90 s)
| Scenario | Method | NT↓ | PSV↓ | TFP↓ | SIT↓ | Max SIR↓ (%) |
|---|---|---|---|---|---|---|
| (a) Wiping glass-wall | G-MPC | 54.55 | 0.00 | 0.00 | 8.41 | 13.22 |
| | AttnGraph-RL | 29.11 | 3.81 | 1.75 | 5.65 | 16.97 |
| | ViNT | 46.24 | 0.00 | 0.00 | 12.32 | 16.97 |
| | VLM-Social-Nav | 32.21 | 0.00 | 0.00 | 0.71 | 2.86 |
| | GSON | 30.42 | 0.00 | 0.00 | 8.28 | 16.97 |
| | Ours | 28.48 | 0.00 | 0.00 | 0.00 | 0.00 |
| (b) Walking-talk | G-MPC | 68.13 | 1.73 | 5.69 | 2.63 | 44.10 |
| | AttnGraph-RL | *90.00 | 0.20 | 1.66 | 0.00 | 0.00 |
| | ViNT | 47.14 | 1.54 | 4.01 | 1.43 | 42.80 |
| | VLM-Social-Nav | *90.00 | 4.99 | 7.57 | 0.00 | 0.00 |
| | GSON | 38.25 | 0.00 | 6.59 | 1.35 | 39.70 |
| | Ours | 28.49 | 0.00 | 1.80 | 0.00 | 0.00 |
| (c) Photography | G-MPC | 36.14 | 3.68 | 8.07 | 3.67 | 27.66 |
| | AttnGraph-RL | *90.00 | 1.71 | 5.28 | 0.00 | 0.00 |
| | ViNT | 36.82 | 2.91 | 9.28 | 3.43 | 27.66 |
| | VLM-Social-Nav | 27.01 | 7.15 | 13.03 | 3.89 | 26.46 |
| | GSON | 46.54 | 2.41 | 5.72 | 0.68 | 6.77 |
| | Ours | 40.15 | 0.0 | 4.32 | 0.00 | 0.00 |
| (d) Queuing | G-MPC | 47.11 | 5.22 | 21.26 | 20.26 | 20.46 |
| | AttnGraph-RL | 17.18 | 1.25 | 5.45 | 2.81 | 21.03 |
| | ViNT | *90.00 | 1.45 | 6.25 | 0.00 | 0.00 |
| | VLM-Social-Nav | *90.00 | 0.00 | 4.25 | 0.00 | 0.00 |
| | GSON | 29.10 | 0.38 | 2.36 | 0.00 | 0.00 |
| | Ours | 26.14 | 0.33 | 2.70 | 0.00 | 0.00 |

Table II (p.7): (a) shortest-visible-path direction alignment with VLM-Social-Nav decisions: (a) 12/12, (b) 8/9, (c) 7/9, (d) 6/7. (b) prediction horizon → Group Interrupt. (%): 2.4 s 8.89; 2.0 s 12.50; 1.6 s 15.83; 1.2 s 21.11; 0.8 s 26.39; 0.4 s 29.44; 0 s 39.17 (10 scenes, 36 paths, 50 trials per horizon).
Fig.8: non-compliance time ratios (bar chart; not tabulated).

## M. Deployment — see front matter. VLM off-board on H100 with 4-bit vLLM; **no latency numbers reported** despite real-time claim.

## N. Limitations
1. **Stated (failure analysis, p.7):** (i) no memory — VLM sees only current frame, misses context beyond view (e.g., long queues); (ii) confounding activities/ambiguous intents confuse prioritisation of norms; (iii) non-optimal candidates — post-processing may exclude ideal path → minimal clearance or overly conservative detours. Also focus on low-to-moderate crowd density (p.3).
2. **Future work:** not explicitly listed.
3. **Observable:** 3 trials; actors at scripted positions; no human-perception study; off-board GPU dependency; no latency; fine-tuning labels from GPT-4o (teacher errors propagate; no label-quality audit); baseline VLM-Social-Nav reimplemented.
4. Deferred.

## O. Reproducibility — project page; hardware specified; code/data release not stated in the paper.

## P. Direct-paper questions
1 Choosing among collision-free paths the one that respects ongoing human activities (ladder, conversation, photography, queue). 2 Implicit context-dependent norms not captured by geometry (p.1). 3 Qwen-2.5 7B fine-tuned (GPT-4o teacher). 4 Fisheye RGB with projected candidate paths (depth info for GPT-4o). 5 Structured prompt: describe each path, choose, justify. 6 Path selection + reasoning. 7 Selected path → reference → retrieve closest current candidate → ORCA sub-goals. 8 No. 9 Detection/tracking, trajectory predictor, costmap, A*-anchors planner, ORCA. 10 Geometric pre-filtering + ORCA. 11 Socially compliant, context-adaptive, real-time. 12 NT, PSV, TFP, SIT, Max SIR in 4 scenarios. 13 Yes. 14 Yes (implicitly via VLM). 15 Partial. 16 Yes (implicitly). 17 Yes (implicitly). 18 Trajectory history/prediction yes; VLM single frame. 19 Prediction uncertainty only. 20 Mitigated structurally. 21 Not measured. 22 VLM off-board. 23 Yes (actors). 24 No. 25 Zero SIT/Max SIR across all scenarios; low PSV/TFP. 26 Cannot conclude: human-perceived comfort; statistical significance; performance in dense crowds; real-time bounds; robustness when VLM errs.

## Q. Cited works possibly missing — see front matter (PIVOT, MOSU, Munir pedestrian VLM, SicNAV, SELFI, DR-MPC, AttnGraph, GMPC, Arena 3.0).

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue IEEE Robotics and Automation Letters; DOI 10.1109/LRA.2026.3662586; pages 3947-3954; URL https://doi.org/10.1109/LRA.2026.3662586.
- Sources: Crossref (exact title match, DOI 10.1109/LRA.2026.3662586); arXiv abs page (2602.09002v1).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - url: PDF-derived 'path-etiquette.github.io' -> externally verified 'https://doi.org/10.1109/LRA.2026.3662586'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

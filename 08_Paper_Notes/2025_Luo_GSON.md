---
id: 2025_Luo_GSON
source_pdfs: [04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/GSON_A_Group-Based_Social_Navigation_Framework_With_Large_Multimodal_Model.pdf]
duplicate_copies: []
related_versions: []
title: 'GSON: A Group-Based Social Navigation Framework With Large Multimodal Model'
authors: &id001 [Shangyi Luo, Peng Sun, Ji Zhu, Yuhong Deng, Cunjun Yu, Anxing Xiao, Xueqian Wang]
year: 2025
venue: IEEE Robotics and Automation Letters
volume: '10'
issue: '10'
pages: 9646-9653
doi: 10.1109/LRA.2025.3595038
url: https://doi.org/10.1109/LRA.2025.3595038
pub_status: journal
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1109/LRA.2025.3595038); arXiv abs page (2409.18084v3). PDF-derived basis (Stage 1): Received 7 Apr 2025; accepted 21 Jul 2025; recommended by AE upon evaluation of reviewers'' comments (p.1).'
category: S4
folder: 04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core
folder_category_match: 'Yes'
category_rationale: An LMM (GPT-4o) infers social groups from visually prompted egocentric images; groups become social spaces avoided by a mid-level planner on a real robot.
paper_type: method
fm_used: 'Yes'
fm_class: [LVLM/LMM]
fm_models: [gpt-4o-2024-08-06 (deployed); compared Gemini 2.0 Flash, Gemini 2.5 Pro, Claude 3.7 Sonnet, Qwen2.5-VL-32B, Qwen2.5-VL-7B; Qwen2.5-VL-32B used in dense-crowd tests]
fm_size: Qwen2.5-VL 7B/32B; commercial models not reported
method_family: [visual prompting, zero-shot, 'detection+tracking (DR-SPAAM, YOLOv5, Kalman, Hungarian)', A*/JPS, BIT*, NMPC-CBF]
roles: [F1, F3]
roles_evidence: {F3: 'LMM outputs social-group assignments G = LMM(A(I,H_track),T) from images annotated with masks/boxes/IDs (Eq.2, p.4); evaluated on 100 annotated scenarios (p.5).', F1: 'LMM reasons about interactions (queuing, talking, photographing) to define groups (p.3-5); scene semantics used only to output grouping.'}
integration: I2
integration_rationale: LMM output (group membership) is a semantic representation; geometry (convex hull + ellipse social space) and replanning (BIT*) are computed by the classical stack (p.4).
evidence: E3
evidence_rationale: Closed-loop real-robot experiments with real people (4 scenarios x 3 runs, long-range ~100 m demo, 3 dense-crowd sites) plus offline LMM grouping evaluation; no human-subject questionnaire (p.5-7).
inputs: [RGB (two cameras merged), 2D LiDAR, occupancy map, SLAM pose, human tracks, natural language prompt]
outputs: [social state (group assignment), constraint (social space via planner), waypoint/path (via BIT*), velocity/action (via NMPC-CBF)]
human_repr: [detected pedestrian position, constant-velocity track (Kalman), predicted trajectory (CV extrapolation), group membership, social space (convex hull + fitted ellipse), CBF safety disc]
capabilities: {C1: Partial, C2: Partial, C3: 'Yes', C4: 'No', C5: Partial, C6: Partial, C7: 'No', C8: Partial, C9: 'Yes', C10: 'Yes', C11: Partial, C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'Yes', C17: Partial, C18: Not reported, C19: Not reported, C20: Partial, C21: Partial, C22: Not reported, C23: 'No', C24: Partial, C25: 'No'}
exp:
  datasets: ['100 scenarios from SCAND, SiT dataset and city-walk videos (group labels by human annotators)']
  simulators: []
  robots: [two-wheeled nonholonomic mobile robot with 2D LiDAR + two RGB cameras (model not named)]
  environment: indoor building halls/corridors/elevator; outdoor square; university canteen, building entrance, campus gate
  indoor_outdoor: both
  sensors: [2D LiDAR, 2x RGB camera]
  humans: real participants (scripted interactions) + real dense crowds (>13 pedestrians avg)
  n_scenes: 4 short-range scenarios; 1 long-range route; 3 dense-crowd sites
  n_trajectories: 3 runs per scenario
  n_participants: Not reported
  split: NA
  baselines: [TEB, TEB+GROUP ESTIMATE, SACSoN, GMPC, RLCA, DBSCAN 2D/3D (grouping)]
  ablation: Partial (TEB+our group estimation isolates mid-level planner; LMM comparison)
  real_robot_trials: 'Yes'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [queue, conversational group, photographing, talking & walking, narrow corridor, elevator entrance, crowd, outdoor square]
metrics: [VLM | Accurate / Miss / Extra / Error grouping rate | % | match / omits members (acceptable) / includes non-members / both | p.5, DEPLOY | LMM inference time | s | per query | p.5, 'NAV | Curvature | m^-1 | Not defined (cites [9],[55]) | p.5-6', NAV | Jerk | m/s^3 | Not defined | p.6, NAV | Roughness | unitless | Not defined | p.6, DEPLOY | Runtime | s | Not defined (appears to be traversal time) | p.6, SOCIAL | Time of Disturbing Individuals | s | robot within 1.2 m directly in front of an individual | p.5, SOCIAL | Time of Disturbing Groups | s | robot inside convex hull of group members | p.5, SOCIAL | Comfort Distance | m | average minimum distance between robot and social groups | p.6]
deployment: {fm_model: gpt-4o-2024-08-06; Qwen2.5-VL-32B in dense-crowd tests, model_size: Not reported (GPT-4o); 32B (Qwen), api_cloud_local: GPT-4o commercial (cloud implied); Qwen local/host not stated, onboard_offboard: Not reported, gpu: Not reported, cpu: Not reported, latency: GPT-4o ~4 s; Qwen2.5-VL-32B ~2 s (offline test); 1.5-2 s in dense-crowd tests; LMM adds at least 1 s response time (p.5-7), query_frequency: 'Keyframe-based: queried when keyframe updated (more people visible) or expires after 1 s (p.4)', planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: 'Yes (LMM low-frequency; tracking/planning high-frequency without LMM, p.2)', caching: Group labels stored in tracking data structure across time (p.4), event_triggered: Partial (keyframe update), distillation: Planned (Qwen2.5-VL-3B) - future work, quantization: 'No', fallback_planner: Global A*/JPS + NMPC-CBF operate independently of LMM, safety_shield: NMPC with discrete-time CBF constraints
    around CV-predicted pedestrians (Eq.3-8), emergency_behavior: Not reported, uncertainty: No (binary group labels), hallucination_mitigation: Visual prompting with masks/IDs; parsing script; no explicit check, real_time_claim_supported: 'Partial: LMM decoupled from control; control rates not reported'}
repro: {code: Not reported, code_url: Not reported, dataset: No (100-scenario grouping set not stated as released), dataset_url: NA, checkpoints: NA, prompts_published: 'No (prompt content described, Fig.4)', hardware_specified: Partial (sensors only), hyperparameters: 'Partial (d_safe, h not given numerically)', protocol_described: Partial, project_page: Not reported (supplementary material at DOI), concerns: Metric values only in bar charts; 3 runs/scenario; LMM-based baselines excluded.}
limitations_flags: [latency, group-detection-error, limited-scenarios, no-human-study, cloud-dependence]
web_verification_required: []
cited_missing: [SiT dataset (NeurIPS 2023), GMPC group-based motion prediction (CoRL 2022), RLCA (Long 2018), Taylor robot-centric group perception (THRI 2020), Lu 2025 group-aware STGAT DRL, Katyal 2022 group-aware policy, Barua 2024 F-formation overview, Eirale 2024 learning social cost functions, Arena-Rosnav 2.0, DR-SPAAM]
coding: {latency_reported: 'Yes', safety_mechanism: 'Yes', uncertainty_treatment: 'No', hallucination_treatment: Partial, code_released: 'No', new_dataset_released: 'No', real_robot: Systematic, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2025
  authors: *id001
  venue: IEEE Robotics and Automation Letters
  volume: '10'
  issue: '10'
  pages: 9646-9653
  doi: 10.1109/LRA.2025.3595038
  url: Not reported
  pub_status: journal
  peer_reviewed: 'Yes'
  peer_review_basis: Received 7 Apr 2025; accepted 21 Jul 2025; recommended by AE upon evaluation of reviewers' comments (p.1).
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: IEEE Robotics and Automation Letters
  verified_doi: 10.1109/LRA.2025.3595038
  verified_url: https://doi.org/10.1109/LRA.2025.3595038
  verified_pages: 9646-9653
  arxiv: 2409.18084v3
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1109/LRA.2025.3595038)', arXiv abs page (2409.18084v3)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A2, A3, A4]
  C_capabilities: {SAF1: Partial, SAF2: Partial, SPA1: 'Yes', SPA2: 'Yes', SPA3: 'Yes', SPA4: Partial, HUM1: Partial, HUM2: Partial, NOR1: Partial, NOR2: 'No', NOR3: Partial, NOR4: 'No', EXP1: Partial, EXP2: 'No', EXP3: Partial}
  B_roles: [R2]
  D_interface: [D1]
  E_evidence_profile: {EV1_offline: 'Yes', EV2_closed_loop_sim: 'No', EV3_physical_robot: systematic, EV4_real_humans_in_trials: unscripted, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: 3 runs per scenario, statistical_testing: 'No', cross_environment: 'Yes', runtime_measured: 'Yes'}
  cross_cutting: {temporal_coupling: per-decision, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'Yes', uncertainty: 'No', hallucination_mitigation: Partial, privacy_constraint: 'No', inference_location: hybrid (local + cloud)}
physical_source_folder: "04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core"
analytical_category: "S4"
coding:
  latency_reported: "Yes"
  safety_mechanism: "Yes"
  uncertainty_treatment: "No"
  hallucination_treatment: "Partial"
  code_released: "No"
  new_dataset_released: "No"
  real_robot: "Systematic"
  human_subject_study: "No"
---

# GSON: A Group-Based Social Navigation Framework With Large Multimodal Model (Luo et al., RA-L 2025)

Page convention: PDF page index (p.N); PDF pp.1–8 = printed 9646–9653.

## A. Bibliographic
`04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/GSON_...pdf`. Luo, Sun, Zhu (co-first), Deng, Yu, A. Xiao, X. Wang (Tsinghua SIGS; NUS). IEEE RA-L 10(10):9646–9653, Oct 2025. DOI 10.1109/LRA.2025.3595038. Journal, peer-reviewed (received 7 Apr 2025, accepted 21 Jul 2025, p.1).

## B. Position — S4
LMM used zero-shot to infer *social groups* (a social-relation representation) that are injected into a hierarchical planner, evaluated on a real robot among real people. It is the corpus's clearest example of an FM used for group/relationship inference (F3).

## C. Research problem
- **Problem (authors):** navigate to goal safely while minimising time trespassing on social groups; robot must infer groups from limited egocentric observation (p.2).
- **Motivation:** rule- or in-domain-learned group detection struggles in open-world scenes; local planners get stuck in local minima; prior LMM methods (OLiVia-Nav, VLM-Social-Nav, Social-LLaVA, AutoSpatial, Vi-LAD) query LMM every planning step and are not interpretable (p.1–2).
- **Contributions (authors):** zero-shot LMM social-group reasoning via visual prompting, combined with robust detection/tracking; mid-level planner between global and local planning; real-world experiments (queue, conversation, photo) (p.1–2).
- **Research questions (p.5):** (1) can LMMs identify social groups? (2) how well does GSON perform in real-world scenarios requiring social awareness?
- **Our interpretation:** the LMM's role is narrow and well-isolated (group labelling); all motion generation is classical and geometric.

## D. Technical method
- **Detection/tracking (p.3):** DR-SPAAM 2D-LiDAR person detection, filtered by YOLOv5 boxes (Eq.1 projection-centre matching); Kalman filter (CV model, state [x,y,ẋ,ẏ]) + Hungarian association.
- **Group detection (p.3–4):** annotate image with YOLO masks, boxes, track IDs (visual prompting) → query gpt-4o-2024-08-06 with text prompt (expected behaviour, format, cues) → parse group relationships (Eq.2). Keyframe = frame with most people within 1-s window; LMM queried when keyframe updated or expires after 1 s.
- **Planning (p.4–5):** global A* with JPS on inflated cost map; mid-level: convex hull of each group → fitted ellipse = social space S; if global path intersects S, replan segment S_s→S_g (fixed arc-length h beyond S) with BIT* → "CrowdFreePath"; local: NMPC with discrete-time CBF h_i(x) = (x−x_p)²+(y−y_p)²−d_safe² against CV-predicted pedestrians (Eq.3–8).
- No fine-tuning, RL or IL in GSON itself.
- **INPUT:** merged RGB, 2D LiDAR, SLAM pose, occupancy map, tracks, prompt. **OUTPUT:** group assignment → social-space constraint → path → controls.

## E. Human/social representation
Individuals: LiDAR/YOLO detection, CV Kalman track, CV-predicted position as CBF obstacle with d_safe. Groups: LMM-inferred membership (binary), convex hull, fitted ellipse social space. Activities (queuing, photographing, talking) are *not* labelled; they only inform grouping.

## F. Functional roles — F3 (primary), F1 (supporting). Not F4/F6: LMM does not generate rules or costs; geometry is derived by the pipeline.

## G. Social capabilities
C1 Partial (CBF safety by design; collisions not reported) · C2 Partial (individual disturbance within 1.2 m in front) · C3 Yes (individual 1.2 m zone, comfort distance) · C4 No · C5 Partial (CV tracking) · C6 Partial (CV extrapolation) · C7 No · C8 Partial (activities implicit in grouping; not labelled) · C9 Yes (grouping accuracy + group disturbance time) · C10 Yes (talking groups / photo sessions not traversed; convex-hull intrusion) · C11 Partial · C12–C15 No · C16 Yes (queue scenarios, elevator queue) · C17 Partial (dense crowds, qualitative only) · C18/C19/C22 Not reported · C20 Partial (curvature/jerk/roughness smoothness) · C21 Partial (comfort distance geometric proxy) · C23 No · C24 Partial (binary group label; authors note lack of nuance) · C25 No.

## H. Integration — I2. ## I. Evidence — E3 (no human-subject evaluation).

## J. Experimental evidence
- **Offline LMM grouping (p.5):** 100 scenarios from SCAND [52], SiT [53] and city-walk videos; queuing/walking/talking/photographing; avg 6.0 pedestrians, 3.5 groups per scenario; ground truth = most-agreed human annotation; 6 LMMs × 10 trials per scenario; DBSCAN 2D/3D baselines.
- **Real-world (p.5–6):** two-wheeled nonholonomic robot, 2D LiDAR, two RGB cameras; scenarios queuing, photographing, talking, talking & walking (Fig.9); 3 runs each with varied start, path, speed. Baselines TEB, TEB+GROUP ESTIMATE, SACSoN, GMPC, RLCA; LMM-based methods [25–28] excluded (not open source; unreliable in pilot reimplementations).
- **Long-range demo (p.6–7):** ~100 m route, hall/corridor/elevator queue/outdoor square, four embedded scenarios (qualitative keyframes).
- **Dense crowds (p.6–7):** canteen at lunch, building entrance near elevator, campus gate; >13 pedestrians avg; all tasks completed (qualitative).

## K. Metrics — see front matter (grouping categories, curvature, jerk, roughness, runtime, time disturbing individuals/groups, comfort distance, inference time).

## L. Quantitative results
- **Grouping (p.5, text):** all four commercial LMMs "acceptable grouping rates above 67%"; lowest Qwen2.5-VL-7B 53.6% Accurate + 14.8% Miss; highest GPT-4o 86.6% acceptable (77.8% Accurate + 8.8% Miss). DBSCAN: accuracy 10.8–14.8%, extra-grouping errors 41.9–46.5%.
  - *Data-quality note:* the text says "All four LMMs ... above 67%" but six LMMs were evaluated and Qwen2.5-VL-7B's acceptable rate (53.6+14.8 = 68.4%) — the sentence is ambiguous; values preserved as written.
- **Inference time (p.5):** Gemini 2.5 Pro and Claude 3.7 Sonnet ~8 s; GPT-4o and Gemini 2.0 Flash ~4 s; Qwen2.5-VL-32B ~2 s; Qwen2.5-VL-7B ~1 s. Dense-crowd: Qwen2.5-VL-32B 1.5–2 s (p.7).
- **Real-world (Fig.8, p.6):** bar charts only (no numeric table). Text: GSON lowest Time of Disturbing Individuals and Groups, highest Comfort Distance; comparable curvature/roughness; slightly higher jerk and runtime ("LMM adds at least 1 s"). Exact values NOT extractable without reading bar heights — not recorded to avoid fabrication.

## M. Deployment — see front matter. LMM decoupled from high-rate loop (keyframe ≤1 Hz); compute platform not reported.

## N. Limitations
1. **Stated:** LMM latency 1.5–2 s (Qwen2.5-VL-32B) reduces responsiveness in rapidly changing contexts; occlusion/partial observability causes incomplete/inaccurate grouping; binary group labels → conservative avoidance of all groups, cannot express that traversing a queue may be more acceptable than interrupting a chat (p.7). Speed slightly lower than baselines (p.6).
2. **Future work:** distil to Qwen2.5-VL-3B; predicted bird's-eye views for relationships beyond egocentric view; LMM-generated costs per interaction type; denser interactions; compact state representation (p.7).
3. **Observable:** results only as bar charts; 3 runs per scenario; no participant count; no human-perception study; LMM-based baselines not compared; compute hardware unreported.
4. Survey-level interpretation: deferred.

## O. Reproducibility — no code/prompt/dataset release stated; supplementary material at DOI.

## P. Direct-paper questions
1 Avoid disturbing individuals and social groups (queues, conversations, photo sessions) while navigating. 2 Semantic grouping beyond proximity/velocity; open-world (p.1–2). 3 GPT-4o (deployed); 6 LMMs compared. 4 Merged egocentric RGB annotated with masks/boxes/track IDs. 5 Annotated image + text prompt with role, format, cues (content not published). 6 Group assignments. 7 Groups → convex hull → ellipse social space → BIT* replanning of the intersecting segment → NMPC-CBF tracking. 8 No. 9 Detection/tracking, A*/JPS, BIT*, NMPC-CBF. 10 CBF constraints around predicted pedestrians. 11 Group-aware, socially compliant navigation in open-world scenes. 12 Grouping accuracy (offline), disturbance time for individuals/groups, comfort distance (real robot). 13 Yes. 14 Yes. 15 No. 16 Implicit only. 17 Group-respect norm (implicit). 18 Tracks over time; LMM uses single keyframe. 19 No. 20 No explicit treatment. 21 LMM ~1–4 s, decoupled. 22 Not reported. 23 Yes (participants and real crowds). 24 No. 25 Lower disturbance times and higher comfort distance (bar charts, 3 runs). 26 Cannot conclude: statistical reliability; human-perceived comfort; performance when LMM errs (no failure analysis beyond limitations); generality beyond tested sites.

## Q. Cited works possibly missing
SiT dataset; GMPC (Wang, Mavrogiannis, Steinfeld CoRL 2022); Taylor & Riek group perception; Lu et al. 2025 group-aware STGAT-DRL; Katyal 2022; Barua F-formation overview (THRI 2024); Eirale 2024 social cost learning; Arena-Rosnav 2.0.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue IEEE Robotics and Automation Letters; DOI 10.1109/LRA.2025.3595038; pages 9646-9653; URL https://doi.org/10.1109/LRA.2025.3595038.
- Sources: Crossref (exact title match, DOI 10.1109/LRA.2025.3595038); arXiv abs page (2409.18084v3).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - url: PDF-derived 'Not reported' -> externally verified 'https://doi.org/10.1109/LRA.2025.3595038'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

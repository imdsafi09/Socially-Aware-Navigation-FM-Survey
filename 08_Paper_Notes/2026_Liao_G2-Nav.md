---
id: 2026_Liao_G2-Nav
source_pdfs: [05_Direct_VLM_SocialNav_Preprints/2607.16956v1.pdf]
duplicate_copies: []
related_versions: []
title: 'G2-Nav: Grounded and Guarded Vision-Language Costmaps for Robot Social Navigation'
authors: &id001 [Yuwen Liao, Yihang Lan, Yizhuo Yang, Ruimeng Liu, Xinhang Xu, Shenghai Yuan, Lihua Xie]
year: 2026
venue: arXiv:2607.16956v1 [cs.RO], 18 Jul 2026
volume: NA
issue: NA
pages: '12'
doi: Not found / not applicable
url: https://arxiv.org/abs/2607.16956
pub_status: accepted per author statement; not yet indexed
peer_reviewed: Accepted (not yet indexed)
peer_review_basis: 'Externally verified (2026-10-19): arXiv abs page (2607.16956v2): v2 (1 Oct 2026) comment "CoRL 2026"; Crossref title search: no match; Not located on OpenReview CoRL 2026 listing at freeze date; acceptance is author-reported.'
category: S5
folder: 05_Direct_VLM_SocialNav_Preprints
folder_category_match: 'Yes'
category_rationale: VLM reasons over open-set detections to identify traversable regions, score social agents (incl. 'social leaders'), and verify tracking; outputs are grounded into a BEV costmap with a LiDAR reflex safety layer; evaluated on SCAND and real-robot campus deployment.
paper_type: method
fm_used: 'Yes'
fm_class: [VLM]
fm_models: ['Qwen3.5-2B (local, recorded setting)', 'GPT-5.4-Nano (online, interactive setting)', RAM++ (open-set tagging), GroundingDINO (detection), SAM (segmentation)]
fm_size: 2B (Qwen3.5); GPT-5.4-Nano not reported
method_family: [prompting, zero-shot, open-set perception, Kalman tracking, costmap optimisation (gradient descent), pure pursuit, safety reflex layer]
roles: [F1, F2, F4, F6]
roles_evidence: {F1: Traversability identification among open-set ground-region tags; SAM mask of traversable region (p.4)., F2: 'VLM verifies whether tracked object''s heading/motion matches visual observation (''Is this person moving towards us?''); flags uncertain motion (p.4, App.A).', F4: 'Social scoring: removes irrelevant objects, scores danger, assigns negative scores to ''social leaders'' moving in robot''s direction to follow unspoken norms (p.4).', F6: 'Scores become elliptical Gaussian costs C_obj and traversability mask C_trav in BEV costmap (Eq.1-2, p.4-5).', Other: Perception verification role (VLM checks upstream depth/heading plausibility) - not covered by F1-F11.}
integration: I4
integration_rationale: VLM outputs (traversable mask, social scores, verification) are converted into costmap terms; gradient-descent trajectory generation + pure pursuit execute (p.4-5).
evidence: E3
evidence_rationale: Offline open-loop evaluation on 83 SCAND trials plus interactive real-robot (Unitree Go2-W) deployment in a crowded 150 m campus corridor, 6 trials per method vs 5 baselines; no human-subject study (p.5-8).
inputs: [RGB (history), LiDAR point cloud, odometry, goal, open-set detections/tracks]
outputs: [semantic labels (traversable regions), social scores, cost (BEV costmap), trajectory (waypoints), velocity/action (pure pursuit)]
human_repr: [open-set detected agent with 2D box, 3D location, velocity (Kalman), VLM social score, elliptical Gaussian cost oriented by velocity, social leader (negative score), reflex-zone unregistered points]
capabilities: {C1: 'Yes', C2: 'Yes', C3: Partial, C4: 'No', C5: Partial, C6: 'No', C7: Partial, C8: Partial, C9: Partial, C10: 'No', C11: Partial, C12: Partial, C13: Partial, C14: 'No', C15: Partial, C16: 'No', C17: Partial, C18: 'No', C19: 'No', C20: Partial, C21: 'No', C22: 'No', C23: 'No', C24: Partial, C25: 'No'}
exp:
  datasets: ['SCAND: 83 of 138 trials (5.6 h) after filtering']
  simulators: []
  robots: ['Unitree Go2-W (Jetson AGX Orin, RGB camera, Livox Mid-360)']
  environment: 150 m crowded campus corridor connecting buildings; SCAND campus
  indoor_outdoor: outdoor
  sensors: [RGB camera, Livox Mid-360 LiDAR]
  humans: real crowds (uncontrolled campus pedestrians)
  n_scenes: SCAND 83 trials; 1 real corridor
  n_trajectories: 6 trials per method (real)
  n_participants: NA
  split: Costmap weights grid-searched on longest SCAND trial
  baselines: [DWA, Social Force, PeopleAsPlanner (PAP), CityWalker, path-etiquette (Fang et al. 2026)]
  ablation: Yes (w/o traversability, scoring, verification, safeguard)
  real_robot_trials: 'Yes'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [crowd corridor, approaching group (giving way), following traffic flow, swinging bag/tool, narrow pathway, runner passing]
metrics: [OTHER | L2 Distance | m | distance between planned and human-operated trajectory (SCAND) | p.6, OTHER | Maximum Average Orientation Error (MAOE) | deg | per CityWalker | p.6, SAFETY | Safety Violation Time (SVT) | s | time within 0.3 m of any obstacle (robot paused to avoid actual collision) | p.6, NAV | Average Time (T_avg) | s | time to goal | p.6, NAV | Average Distance (D_avg) | m | distance to goal | p.6, 'DEPLOY | VLM query time | s | 1.5 s (Qwen3.5-2B, 2x RTX2080); 4 s (GPT-5.4-Nano online) | p.5']
deployment: {fm_model: Qwen3.5-2B (local) / GPT-5.4-Nano (online), model_size: 2B / not reported, api_cloud_local: Local vLLM (recorded) / cloud API (interactive), onboard_offboard: Jetson AGX Orin onboard for ROS; VLM online in interactive setting, gpu: 2x RTX2080 (local VLM); Jetson AGX Orin (robot), cpu: Not reported, latency: avg query 1.5 s (local) / 4 s (online), query_frequency: Every VLM inference cycle (asynchronous), planner_frequency: Not reported (costmap updated asynchronously), controller_frequency: Not reported, asynchronous: Yes (default score for new objects until analysed), caching: Object dictionary retains scores, event_triggered: 'No', distillation: Future work, quantization: 'No', fallback_planner: Costmap with default scores + occupancy term, safety_shield: 'High-frequency reflex zone (T=1.5 s, W=0.8 m) injecting penalties for unregistered LiDAR points', emergency_behavior: Reflex penalty forces immediate response (safety brake), uncertainty: Partial (heading mismatch
    raises social score), hallucination_mitigation: VLM produces bounded scores instead of numeric trajectories; upstream verification; reflex layer, real_time_claim_supported: Partial (asynchronous design; control rate not reported)}
repro: {code: Promised, code_url: NA, dataset: SCAND (public), dataset_url: NA, checkpoints: NA, prompts_published: 'No', hardware_specified: 'Yes', hyperparameters: 'Partial (reflex T, W, eps; lambda by grid search)', protocol_described: Partial, project_page: Not reported (supplementary video), concerns: 6 real trials; same campus; human supervisor pauses robot (SVT).}
limitations_flags: [latency, cloud-dependence, resource-requirements, limited-scenarios, no-human-study]
web_verification_required: [Venue status; code release.]
cited_missing: ['Following is all you need: people as planners (RA-L 2025)', CityWalker (CVPR 2025), OpenNav (IROS 2025), HEIGHT (T-ASE 2025), Navigation world models (CVPR 2025), CATNav (arXiv 2026), LISN language-instructed social navigation (arXiv 2025), SocialNav-Map (arXiv 2025), Contextual safety reasoning and grounding (arXiv 2026), AsyncVLA (arXiv 2026), Trust in LLM-controlled robotics survey, VLA safety survey (arXiv 2026), Papadakis 2013 social mapping]
coding: {latency_reported: 'Yes', safety_mechanism: 'Yes', uncertainty_treatment: Partial, hallucination_treatment: 'Yes', code_released: Promised, new_dataset_released: NA, real_robot: Systematic, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2026
  authors: *id001
  venue: arXiv:2607.16956v1 [cs.RO], 18 Jul 2026
  volume: NA
  issue: NA
  pages: '12'
  doi: Not reported
  url: Not reported
  pub_status: preprint
  peer_reviewed: 'No'
  peer_review_basis: arXiv v1; 'Code will be made publicly available'; no venue (CoRL-style template).
external_verification:
  verified_on: '2026-10-19'
  status_class: 'B: accepted per authors/arXiv; proceedings not yet available'
  verified_venue: arXiv:2607.16956v1 [cs.RO], 18 Jul 2026
  verified_doi: Not found / not applicable
  verified_url: https://arxiv.org/abs/2607.16956
  verified_pages: NA
  arxiv: 2607.16956v2
  version_relationship: arXiv only; published version not yet available
  sources: ['arXiv abs page (2607.16956v2): v2 (1 Oct 2026) comment "CoRL 2026"', 'Crossref title search: no match', Not located on OpenReview CoRL 2026 listing at freeze date; acceptance is author-reported]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A3, A5]
  C_capabilities: {SAF1: 'Yes', SAF2: 'Yes', SPA1: Partial, SPA2: Partial, SPA3: Partial, SPA4: Partial, HUM1: Partial, HUM2: Partial, NOR1: Partial, NOR2: 'No', NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: Partial}
  B_roles: [R1, R2]
  D_interface: [D3]
  E_evidence_profile: {EV1_offline: 'Yes', EV2_closed_loop_sim: 'No', EV3_physical_robot: systematic, EV4_real_humans_in_trials: present-type-unreported, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: 6 trials per method (real), statistical_testing: 'No', cross_environment: No/unclear, runtime_measured: 'Yes'}
  cross_cutting: {temporal_coupling: asynchronous, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'Yes', uncertainty: Partial, hallucination_mitigation: 'Yes', privacy_constraint: 'No', inference_location: hybrid (local + cloud)}
physical_source_folder: "05_Direct_VLM_SocialNav_Preprints"
analytical_category: "S5"
coding:
  latency_reported: "Yes"
  safety_mechanism: "Yes"
  uncertainty_treatment: "Partial"
  hallucination_treatment: "Yes"
  code_released: "Promised"
  new_dataset_released: "NA"
  real_robot: "Systematic"
  human_subject_study: "No"
---

# G2-Nav (Liao et al., arXiv Jul 2026)

Page convention: PDF index (p.N).

## A. Bibliographic — arXiv:2607.16956v1 (18 Jul 2026), NTU Singapore. Preprint. **Published after the Cai et al. survey cut-off (27 Jun 2026).**

## B. Position — S5. VLM as social-context interpreter whose outputs are *grounded into a costmap* and *guarded* by a geometric reflex layer; explicitly compares against VLM path-selection (path-etiquette) and end-to-end (CityWalker).

## C. Research problem — "How to effectively and safely ground VLM social reasoning into reliable real-world robot navigation?" (p.1). Critiques: end-to-end VLM black boxes lack safety; VLM trajectory selection limited by sampling quality; VLM costmaps from detailed instructions unsuitable for autonomy (p.1–2). Contributions: vision-language costmap; upstream verification + safety reflex; real-world experiments (p.2).

## D. Technical method — RAM++ tags → GroundingDINO boxes → LiDAR depth registration (DBSCAN) → Kalman tracking (state b, x, v) (p.3–4); VLM prompts: traversability identification (+ SAM mask), social scoring (incl. negative 'social leader' scores; default score for new objects), upstream verification (depth/heading plausibility; re-registration) (p.4); costmap C = λ1 C_goal + λ2 C_obs + λ3 C_obj + C_trav with C_obj = Σ s_j N(x_j, Σ(v_j)) (Eq.1–2); reflex zone (rectangle/arc with T = 1.5 s, W = 0.8 m) (App.B); gradient-descent trajectory + pure pursuit (p.5).

## G. Social capabilities
C1, C2 Yes (SVT within 0.3 m; robot paused by supervisor to avoid contact) · C3 Partial · C5, C7 Partial (velocity tracking; VLM heading verification) · C8 Partial (swinging bag/tool) · C9, C12 Partial (giving way to approaching group, qualitative) · C11, C13 Partial (following traffic/'social leaders') · C15 Partial (stay on pathway) · C17 Partial (crowded corridor) · C20 Partial (L2/MAOE to human operator) · C24 Partial · others No.

## H/I — I4; E3.

## L. Quantitative results
Table 1 (SCAND recorded, 83 trials; L2 m / MAOE °): CityWalker 0.60/16.81; path-etiquette 0.97/20.14; G2-Nav 0.55/15.64; w/o traversability 0.84/18.10; w/o scoring 1.12/21.08; w/o verification 0.57/16.37; w/o safeguard 0.48/15.90.
Table 2 (interactive, 6 trials; SVT s / T_avg s / D_avg m): DWA 11.9/392/181.6; Social Force 4.4/352/165.4; PAP 8.1/322/180.9; CityWalker 16.6/403/179.1; path-etiquette 10.2/518/198.4; G2-Nav 6.9/278/172.3.
- Observations: Social Force has lower SVT (4.4) and D_avg (165.4) than G2-Nav (authors argue SF behaviour was socially inappropriate, qualitative); "w/o safeguard" has better L2 (0.48) than full (0.55) on recorded data.

## M. Deployment — local 2B VLM 1.5 s; online GPT-5.4-Nano 4 s on robot; asynchronous costmap updates; reflex safety layer.

## N. Limitations
1. **Stated (p.8):** noticeable latency on edge devices; multi-step perception could be compacted; distillation future work; safeguard only checks unregistered points — CBFs or local-minima avoidance future work.
2. **Observable:** 6 real trials in one corridor; no human perception study; supervisor pauses confound time metrics.

## P. Direct-paper questions (abridged)
1 Socially compliant autonomous navigation without detailed instructions. 3 Qwen3.5-2B / GPT-5.4-Nano. 4 Image history + detections. 6 Region labels, scores, verification flags. 7 Costmap terms. 8 No. 9 Gradient-descent planner + pure pursuit. 10 Reflex zone. 12 L2/MAOE, SVT, time, distance. 18 Image history. 19 Heading uncertainty only. 20 Mitigated structurally. 21 Asynchronous; VLM 1.5–4 s. 22 Partly (online VLM). 23 Yes (uncontrolled crowd). 24 No. 25 Lower SVT than most baselines, best time. 26 Cannot conclude human comfort or significance (n = 6).

## R. Stage-2 external verification (2026-10-19)
- Externally verified: B: accepted per authors/arXiv; proceedings not yet available; venue arXiv:2607.16956v1 [cs.RO], 18 Jul 2026; DOI Not found / not applicable; pages NA; URL https://arxiv.org/abs/2607.16956.
- Sources: arXiv abs page (2607.16956v2): v2 (1 Oct 2026) comment "CoRL 2026"; Crossref title search: no match; Not located on OpenReview CoRL 2026 listing at freeze date; acceptance is author-reported.
- Version relationship: arXiv only; published version not yet available.
- Changed field - doi: PDF-derived 'Not reported' -> externally verified 'Not found / not applicable'
- Changed field - url: PDF-derived 'Not reported' -> externally verified 'https://arxiv.org/abs/2607.16956'
- Changed field - pub_status: PDF-derived 'preprint' -> externally verified 'accepted per author statement; not yet indexed'
- Changed field - peer_reviewed: PDF-derived 'No' -> externally verified 'Accepted (not yet indexed)'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

## Stage-7 status re-check (2026-10-19)
arXiv v2 (1 Oct 2026) still states CoRL 2026; no Crossref/PMLR record. Status unchanged: accepted, not yet indexed. See 09_Project_Reports/PUBLICATION_STATUS_FINAL_CHECK.md.

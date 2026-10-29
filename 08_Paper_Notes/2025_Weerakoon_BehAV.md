---
id: 2025_Weerakoon_BehAV
source_pdfs: [04_Direct_VLM_SocialNav/B_Peer_Reviewed_Boundary/2409.16484v2.pdf]
duplicate_copies: []
related_versions: ['Published version: IEEE ICRA 2025, pp.7044-7051 (as cited by Wang et al. MAction [8]); NOT in corpus']
title: 'BehAV: Behavioral Rule Guided Autonomy Using VLMs for Robot Navigation in Outdoor Scenes'
authors: &id001 [Kasun Weerakoon, Mohamed Elnoor, Gershom Seneviratne, Vignesh Rajagopal, Senthil Hariharan Arul, Jing Liang, Mohamed Khalid M Jaffar, Dinesh Manocha]
year: 2025
venue: 2025 IEEE International Conference on Robotics and Automation (ICRA)
volume: NA
issue: NA
pages: 7044-7051
doi: 10.1109/ICRA55743.2025.11127890
url: https://doi.org/10.1109/ICRA55743.2025.11127890
pub_status: conference (corpus copy is preprint)
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1109/ICRA55743.2025.11127890); arXiv abs page (2409.16484v2). PDF-derived basis (Stage 1): Corpus PDF arXiv v2 without venue; cited by MAction-SocialNav (RA-L 2026) as ICRA 2025 pp.7044-7051. WEB_VERIFICATION_REQUIRED.'
category: S4
folder: 04_Direct_VLM_SocialNav/B_Peer_Reviewed_Boundary
folder_category_match: Partial
category_rationale: 'Boundary: language-specified behavioural rules (incl. ''stop for stop hand gesture'', ''yield to people wearing black shirts'', ''avoid cyclists'') grounded by VLM/LLM into a behavioural cost map for an MPC planner on a real quadruped; most rules concern terrain/traffic objects rather than social interaction.'
paper_type: method
fm_used: 'Yes'
fm_class: [LLM, VLM, CLIP-style]
fm_models: ['GPT-4 (instruction decomposition, action desirability)', 'CLIPSeg (behavioural target segmentation, onboard)', 'GPT-4o (landmark goal pixel estimation); GPT4v, Gemini compared']
fm_size: Not reported
method_family: [prompting, zero-shot, open-vocabulary segmentation, unconstrained MPC, gait switching]
roles: [F1, F4, F6, F7, F9]
roles_evidence: {F7: 'GPT-4 decomposes instruction into navigation actions, landmarks, behavioural actions and targets (Eq.2, p.4).', F4: 'LLM assigns desirability probabilities to behavioural actions (''stay on'' ~1, ''stop'' ~0) (Eq.3-4, p.5).', F1: 'CLIPSeg segments behavioural targets per pixel (Eq.5, p.5).', F6: 'Behavioural cost map C_behav = max_i p_i * S_i used in MPC objective and velocity cap (Eq.6-7, 10-12, p.5-6).', F9: 'GPT-4o predicts landmark pixel -> goal heading in odometry frame (Eq.8, p.5).'}
integration: I4
integration_rationale: FM outputs are converted into a behavioural cost map and velocity constraint used by an unconstrained MPC planner (p.5-6).
evidence: E3
evidence_rationale: Real-world closed-loop experiments on Ghost Vision 60 quadruped in 5 outdoor scenarios (>=10 trials each) vs 5 baselines; offline landmark detection on 250 images; no human-subject study (p.6-8).
inputs: [RGB, LiDAR (OS1-32), odometry, natural language instruction]
outputs: [semantic labels (segmentation), cost (behavioural cost map), constraint (velocity cap), waypoint (landmark goal), velocity/action (MPC), gait mode]
human_repr: ['segmented behavioural object (e.g., people wearing red shirts; stop hand gesture; cyclists) with language-specified action cost', LiDAR obstacle]
capabilities: {C1: Partial, C2: 'No', C3: 'No', C4: 'No', C5: 'No', C6: 'No', C7: Partial, C8: 'No', C9: 'No', C10: 'No', C11: Partial, C12: 'Yes', C13: 'No', C14: 'No', C15: 'Yes', C16: 'No', C17: 'No', C18: 'No', C19: 'No', C20: Partial, C21: 'No', C22: 'No', C23: 'Yes', C24: 'Yes', C25: 'No'}
exp:
  datasets: ['250 images, 7 landmarks (landmark detection evaluation)']
  simulators: []
  robots: [Ghost Robotics Vision 60 quadruped]
  environment: 'outdoor campus: sidewalks, crosswalk/road, sand, grass, water puddles, vegetation, concrete, stairs'
  indoor_outdoor: outdoor
  sensors: [Ouster OS1-32 LiDAR, Realsense L515 camera, odometry]
  humans: real pedestrians (gestures; coloured shirts) in scenarios 1 and 3
  n_scenes: 5 scenarios
  n_trajectories: at least 10 trials per scenario
  n_participants: Not reported
  split: NA
  baselines: [GA-Nav, CoNVOI, ViNT, NoMaD, BehAV with DWA (ablation)]
  ablation: Yes (planner -> DWA; VLM choice for landmarks)
  real_robot_trials: 'Yes'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [crosswalk, sidewalk, stop gesture, yielding to pedestrians, multi-terrain, stairs]
metrics: [NAV | Success Rate | % | reached goal while avoiding collisions and following behavioural rules | p.7, NAV | Avg. Goal Heading Error | rad | average angle between goal line of sight and robot heading | p.7, OTHER | Frechet Dist. w.r.t. Human | m | Frechet distance to human-teleoperated path | p.7, SOCIAL | Behavior Following Accuracy (BFA) | % | percentage of path length adhering to behavioural rules | p.7, VLM | Pixel Error | pixels | landmark location error | p.7-8, VLM | F-score | 0-1 | predicted landmark within GT region | p.7-8, DEPLOY | Infer. Rate | s | VLM landmark query time | p.8, DEPLOY | System rate | Hz | overall system ~9.5 Hz on Intel NUC 11 | p.8]
deployment: {fm_model: CLIPSeg onboard; GPT-4/GPT-4o via internet, model_size: Not reported, api_cloud_local: 'Hybrid: CLIPSeg local; GPT-4/GPT-4o cloud', onboard_offboard: Onboard Intel NUC 11 (i7 + RTX 2060) for CLIPSeg/planner; cloud LLM/VLM, gpu: NVIDIA RTX 2060 (NUC 11), cpu: Intel i7 (NUC 11), latency: GPT-4o landmark inference ~6 s via internet (p.5); 3.59 s in Table II; overall system ~9.5 Hz (p.8), query_frequency: LLM decomposition once per instruction; GPT-4o landmark queries continuous until reached; CLIPSeg every frame, planner_frequency: ~9.5 Hz overall, controller_frequency: Not reported, asynchronous: Yes (slow landmark VLM vs fast CLIPSeg cost map), caching: Goal direction locked and re-evaluated, event_triggered: Velocity cap when max(C_behav) >= c_th, distillation: 'No', quantization: 'No', fallback_planner: 'No', safety_shield: Obstacle cost from LiDAR; velocity cap for highly undesirable actions, emergency_behavior: 'Velocity reduced to near zero for highly undesirable
    actions (e.g., stop sign)', uncertainty: Segmentation likelihoods propagate into cost, hallucination_mitigation: No (hallucination acknowledged as limitation), real_time_claim_supported: Yes for cost-map loop (~9.5 Hz measured); landmark VLM slower}
repro: {code: Stated (code and video at project page), code_url: 'http://gamma.umd.edu/behav/', dataset: NA, dataset_url: NA, checkpoints: NA, prompts_published: Partial (decomposition prompt example p.4), hardware_specified: 'Yes', hyperparameters: Partial (defaults on webpage), protocol_described: Partial, project_page: 'http://gamma.umd.edu/behav/', concerns: Preprint version; trial counts '>=10' not exact.}
limitations_flags: [hallucination, latency, cloud-dependence, limited-scenarios, no-human-study]
web_verification_required: [Confirm ICRA 2025 publication details.]
cited_missing: [CLIPSeg, SocioSense (Tai 2018), Social momentum (Mavrogiannis HRI 2018), Unconstrained MPC under uncertainty (Arul 2024), IVLMap, SayTap, NavGPT-2, 'Think, act and ask', ZSON, OVExp, Navi2Gaze, GA-Nav]
coding: {latency_reported: 'Yes', safety_mechanism: 'Yes', uncertainty_treatment: Partial, hallucination_treatment: 'No', code_released: 'Yes', new_dataset_released: NA, real_robot: Systematic, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2025
  authors: *id001
  venue: arXiv:2409.16484v2 (corpus copy, 2 Oct 2024); published ICRA 2025 per citing paper
  volume: Not reported
  issue: Not reported
  pages: 10 (arXiv PDF); 7044-7051 (ICRA 2025 per citation)
  doi: Not reported
  url: http://gamma.umd.edu/behav/
  pub_status: conference (corpus copy is preprint)
  peer_reviewed: 'Yes'
  peer_review_basis: Corpus PDF arXiv v2 without venue; cited by MAction-SocialNav (RA-L 2026) as ICRA 2025 pp.7044-7051. WEB_VERIFICATION_REQUIRED.
project_url: http://gamma.umd.edu/behav/
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: 2025 IEEE International Conference on Robotics and Automation (ICRA)
  verified_doi: 10.1109/ICRA55743.2025.11127890
  verified_url: https://doi.org/10.1109/ICRA55743.2025.11127890
  verified_pages: 7044-7051
  arxiv: 2409.16484v2
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1109/ICRA55743.2025.11127890)', arXiv abs page (2409.16484v2)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A3, A5]
  C_capabilities: {SAF1: Partial, SAF2: 'No', SPA1: 'No', SPA2: 'No', SPA3: 'Yes', SPA4: 'No', HUM1: 'No', HUM2: Partial, NOR1: Partial, NOR2: 'Yes', NOR3: 'Yes', NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: Partial}
  B_roles: [R1, R3, R4]
  D_interface: [D3, D4]
  E_evidence_profile: {EV1_offline: 'Yes', EV2_closed_loop_sim: 'No', EV3_physical_robot: systematic, EV4_real_humans_in_trials: staged, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: at least 10 trials per scenario, statistical_testing: 'No', cross_environment: No/unclear, runtime_measured: 'Yes'}
  cross_cutting: {temporal_coupling: per-decision, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'Yes', uncertainty: Partial, hallucination_mitigation: 'No', privacy_constraint: 'No', inference_location: hybrid (local + cloud)}
physical_source_folder: "04_Direct_VLM_SocialNav/B_Peer_Reviewed_Boundary"
analytical_category: "S4"
coding:
  latency_reported: "Yes"
  safety_mechanism: "Yes"
  uncertainty_treatment: "Partial"
  hallucination_treatment: "No"
  code_released: "Yes"
  new_dataset_released: "NA"
  real_robot: "Systematic"
  human_subject_study: "No"
---

# BehAV (Weerakoon et al., arXiv 2024 / ICRA 2025)

Page convention: PDF index (p.N) of arXiv v2.

## A. Bibliographic
Corpus file arXiv v2 (2 Oct 2024), UMD GAMMA. ICRA 2025 pp.7044–7051 per MAction-SocialNav reference — published version not in corpus (WEB_VERIFICATION_REQUIRED). Project http://gamma.umd.edu/behav/.

## B. Position — S4 (boundary)
Language-instructed behavioural rules → behavioural cost map. Social content: stop for stop hand gesture, yield to/stop for specified people, avoid cyclists, use crosswalks. Primary focus is outdoor rule-following incl. terrain; included as boundary direct paper because human-directed rules are evaluated on a real robot.

## C. Research problem
- **Problem:** follow scene-specific behaviours (yield to cyclists, stay on paved paths, obey traffic signals) in dynamic outdoor scenes; prior VLM methods (CoNVOI, VLM-Social-Nav) have low inference rates for dynamic changes (p.1–2).
- **Contributions:** behavioural cost map from language rules via lightweight VLM on edge computer (+15.3% behaviour-following accuracy); VLM landmark goal estimation (+31.25% F-score, −37.19% pixel error); behaviour-aware unconstrained MPC planner (+40% success, 22.49% closer Fréchet) (p.2).

## D. Technical method
GPT-4 decomposes instruction into A_nav, L_nav, A_behav, L_behav (Eq.2); GPT-4 maps behavioural actions to desirability probabilities (Eq.3–4); CLIPSeg per-target segmentation S_i (Eq.5); c(x,y) = p_i · S_i(x,y) (Eq.6); C_behav = max_i C_i (Eq.7); GPT-4o landmark pixel → odom goal (Eq.8), ~6 s internet query; unconstrained MPC over z = (r, θ, δ, v_max) with pose-following control law (Eq.1) minimising J = w_goal ψ_goal + w_obs ψ_obs + w_behav ψ_behav (Eq.9–12); velocity cap v'_max = (1 − max C_behav)·v_max if max C_behav ≥ c_th; gait switching for "watch your step/use caution" (p.6). NLopt optimizer; Intel NUC 11 (i7, RTX 2060) (p.6).

## E. Human/social representation — humans only as segmented behavioural targets (e.g., "people wearing red shirts", "stop hand gesture") with language-specified action cost; LiDAR obstacles.

## F. Roles — F7, F4, F1, F6, F9.

## G. Social capabilities
C12 Yes (stop/yield to people and gestures; BFA, success requires following rules) · C15 Yes (sidewalk, crosswalk) · C23 Yes (explicit language behavioural instructions) · C24 Yes · C7 Partial (stop gesture) · C1 Partial (success requires collision avoidance; no collision metric) · C11 Partial · C20 Partial (Fréchet to teleop) · others No.

## H. Integration — I4. ## I. Evidence — E3.

## J. Experimental evidence
Ghost Vision 60, OS1-32 LiDAR, L515 camera, NUC 11. 5 real outdoor scenarios (S1 human gestures + sidewalk + crosswalk; S2 sand/grass/puddles; S3 sidewalk/grass/vegetation + pedestrians in coloured shirts; S4–S5 concrete/stairs/grass), ≥10 trials each; baselines GA-Nav, CoNVOI, ViNT, NoMaD (given goal location), BehAV+DWA (p.7).

## K. Metrics — Success Rate, Avg. Goal Heading Error, Fréchet, BFA, Pixel Error, F-score, inference rate, system Hz.

## L. Quantitative results (Table I, p.7; S1 / S2 / S3 / S4 / S5)
- Success Rate (%): GA-Nav 0/70/0/50/20; CoNVOI 20/50/10/60/50; ViNT 0/40/0/50/30; NoMaD 0/30/0/40/20; BehAV+DWA 80/70/60/60/50; BehAV 90/90/80/80/70.
- Avg Goal Heading Error (rad): GA-Nav 0.652/0.598/0.964/1.325/1.345; CoNVOI 0.863/0.743/0.859/1.396/1.184; ViNT 0.746/0.654/0.687/1.257/1.267; NoMaD 0.659/0.684/0.755/1.238/1.279; BehAV+DWA 0.636/0.765/0.861/1.241/1.155; BehAV 0.616/0.732/0.835/1.262/1.137.
- Fréchet (m): GA-Nav 2.188/1.015/1.584/4.251/12.357; CoNVOI 1.965/1.196/1.792/6.820/8.398; ViNT 2.235/1.258/1.458/5.783/13.774; NoMaD 2.291/1.234/1.522/6.207/16.247; BehAV+DWA 1.698/1.083/1.238/3.855/6.721; BehAV 1.621/0.987/1.195/3.762/5.473.
- BFA (%): GA-Nav 48.56/81.43/65.72/73.55/42.16; CoNVOI 66.32/54.11/56.02/62.84/65.32; ViNT 55.86/65.36/45.32/75.68/38.67; NoMaD 49.63/61.08/49.71/72.43/43.55; BehAV+DWA 82.90/85.72/69.65/84.67/74.63; BehAV 86.22/89.65/76.14/88.07/78.69.
Table II (p.8; landmark detection, 250 images, 7 landmarks; pixel error / F-score / inference s): Gemini 274.41/0.44/10.65; GPT4v 245.49/0.433/3.37; GPT4o 178.94/0.64/3.59. System ~9.5 Hz on NUC 11.
- Note: text says GPT-4o has "a higher inference rate" while Table II shows GPT4v faster (3.37 s vs 3.59 s); also p.5 states GPT-4o inference ~6 s.

## M. Deployment — see front matter.

## N. Limitations
1. **Stated (p.8):** lighting sensitivity of scene understanding; LLM/VLM prediction errors due to hallucinations.
2. **Future work:** more robust perception with advanced multimodal models.
3. **Observable:** social rules tested only as identifiable visual targets (shirts, gestures); no proxemic metric; ≥10 trials unspecified exact; preprint numbers.
4. Deferred.

## O. Reproducibility — code stated on project page; parameters partly.

## P. Direct-paper questions
1 Following user-specified behavioural rules (incl. yielding/stopping for people) while reaching landmarks outdoors. 2 Zero-shot grounding of arbitrary language rules. 3 GPT-4, GPT-4o, CLIPSeg. 4 RGB frames (CLIPSeg, GPT-4o); instruction text (GPT-4). 5 Decomposition, desirability, landmark prompts. 6 Structured rule sets, probabilities, segmentation, goal pixel. 7 Cost map + velocity cap in MPC. 8 No. 9 Unconstrained MPC, control law. 10 Obstacle cost + velocity cap. 11 Behaviour-aware navigation in dynamic scenes. 12 BFA, success, Fréchet. 13 As segmented targets. 14 No. 15 Gesture only. 16 No. 17 Explicit user rules. 18 No. 19 Segmentation likelihood only. 20 Acknowledged. 21 ~9.5 Hz (cost map loop). 22 Partly. 23 Yes. 24 No. 25 BFA and success gains. 26 Cannot conclude social comfort, proxemic compliance, or performance in crowds.

## Q. Cited works possibly missing — CLIPSeg; SocioSense; Social Momentum; IVLMap; NavGPT-2.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue 2025 IEEE International Conference on Robotics and Automation (ICRA); DOI 10.1109/ICRA55743.2025.11127890; pages 7044-7051; URL https://doi.org/10.1109/ICRA55743.2025.11127890.
- Sources: Crossref (exact title match, DOI 10.1109/ICRA55743.2025.11127890); arXiv abs page (2409.16484v2).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - venue: PDF-derived 'arXiv:2409.16484v2 (corpus copy, 2 Oct 2024); published ICRA 2025 per citing paper' -> externally verified '2025 IEEE International Conference on Robotics and Automation (ICRA)'
- Changed field - volume: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - issue: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - pages: PDF-derived '10 (arXiv PDF); 7044-7051 (ICRA 2025 per citation)' -> externally verified '7044-7051'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified '10.1109/ICRA55743.2025.11127890'
- Changed field - url: PDF-derived 'http://gamma.umd.edu/behav/' -> externally verified 'https://doi.org/10.1109/ICRA55743.2025.11127890'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

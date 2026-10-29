---
id: 2026_Payandeh_Narrate2Nav
source_pdfs: [04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/Narrate2Nav_arXiv2506.14233v1.pdf]
duplicate_copies: []
related_versions: ['arXiv:2506.14233v1 (17 Jun 2025) = corpus copy; published version ICRA 2026 (IEEE)']
title: 'Narrate2Nav: Real-Time Visual Navigation with Implicit Language Reasoning in Human-Centric Environments'
authors: [Amirreza Payandeh, Anuj Pokhrel, Daeun Song, Marcos Zampieri, Xuesu Xiao]
year: 2026
venue: 2026 IEEE International Conference on Robotics and Automation (ICRA)
volume: NA
issue: NA
pages: 21696-21703
doi: 10.1109/ICRA57385.2026.11696112
url: https://doi.org/10.1109/ICRA57385.2026.11696112
pub_status: conference (corpus copy is arXiv author version)
peer_reviewed: 'Yes'
peer_review_basis: 'Crossref record: ICRA 2026 proceedings, pp. 21696-21703, DOI 10.1109/ICRA57385.2026.11696112 (verified 2026-10-19). Corpus PDF is arXiv v1 (no venue printed).'
category: S4
folder: 04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core
folder_category_match: 'Yes'
category_rationale: A large VLM (Qwen2-VL-72B) generates textual narrations of humans, intentions and CoT reasoning that are distilled (with CLIP text features) into an RGB-only student policy for human-centric navigation; evaluated offline and on a real robot in social scenarios.
paper_type: method
fm_used: 'Yes'
fm_class: [VLM, vision-language encoder, vision foundation encoder]
fm_models: [Qwen2-VL-72B-Instruct (offline narration/CoT labelling), CLIP text encoder (teacher), DINOv2 (frozen teacher vision encoder)]
fm_size: 72B labeller; teacher ~330M; deployed student ~29M (ResNet50)
method_family: [self-supervised representation learning (Barlow Twins), teacher-student distillation, behaviour cloning, VLM labelling, chain-of-thought text supervision]
roles: [F1, F2, F8, F11]
roles_evidence: {F1: VLM narrates the egocentric scene and spatial relations to humans (p.4)., F2: Narrations include predictions of surrounding human movements and intentions (p.4)., F8: Teacher embeddings with text are distilled into an RGB-only student via Barlow Twins loss (p.1)., F11: VLM used as automatic annotator of training data (narrations over SCAND frames).}
integration: I6
integration_rationale: FM knowledge enters only through training (labels + teacher); the deployed student maps RGB+goal to waypoints tracked by Pure Pursuit; no FM call at inference (p.6).
evidence: E3
evidence_rationale: 'Offline unseen-dataset evaluation (AOE/ADE/FDE) plus real-robot trials: 4 scenarios x 10 trials per method on an AgileX Scout Mini (Table 2, p.8); no human-subject study.'
inputs: ['RGB history (5 frames, 2.5 s)', 'goal (x, y)']
outputs: [waypoints (short-horizon trajectory)]
human_repr: [implicit in learned visual embedding, textual narration of human positions/intentions (training only)]
capabilities: {C1: 'Yes', C2: Partial, C3: 'No', C4: 'No', C5: Partial, C6: Partial, C7: Partial, C8: 'No', C9: 'No', C10: 'No', C11: Partial, C12: Partial, C13: Partial, C14: Partial, C15: 'No', C16: 'No', C17: Partial, C18: 'No', C19: 'No', C20: Partial, C21: 'No', C22: 'No', C23: 'No', C24: Partial, C25: 'No'}
exp:
  datasets: [SCAND subset (training), new unseen dataset collected with AgileX Scout Mini (test)]
  simulators: []
  robots: [AgileX Scout Mini with ZED2 stereo camera]
  environment: indoor and outdoor campus spaces
  indoor_outdoor: both
  sensors: [RGB (ZED2), visual odometry]
  humans: real pedestrians (recruitment not described)
  n_scenes: 5 offline scenario types; 4 real-world scenarios
  n_trajectories: 10 real trials per scenario per method
  n_participants: Not reported
  split: unseen self-collected dataset as test set
  baselines: [GNM, ViNT, NoMaD, CityWalker]
  ablation: Yes (text module removed, Table 3)
  real_robot_trials: 'Yes'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [Navigation in Crowds (offline only), Frontal Approach, Human Following, Narrow Passageway, Intersection]
metrics: [OTHER | AOE | rad | average orientation error between predicted and ground-truth trajectory vectors | p.7, OTHER | ADE / FDE | m | average / final displacement error vs. demonstration | p.7, SAFETY | Collision | count/10 | any instance where the human must yield to the robot | p.8, NAV | Success rate | count/10 | reaching the goal | p.8]
deployment: {fm_model: None at inference (student ResNet50), model_size: ~29M student; ~330M teacher, api_cloud_local: Local, onboard_offboard: Not reported, gpu: 8x A100 40 GB (training), cpu: Not reported, latency: 'Not reported (real-time claimed, no rate given)', query_frequency: Not reported, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Not reported, caching: Not reported, event_triggered: Not reported, distillation: Yes (teacher-student), quantization: Not reported, fallback_planner: Not reported, safety_shield: No (Pure Pursuit tracking only), emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: Not addressed (VLM narrations not verified), real_time_claim_supported: Partial (small student; no measured rate)}
repro: {code: Not reported, code_url: Not reported, dataset: New test dataset; release not stated, dataset_url: Not reported, checkpoints: Not reported, prompts_published: Not reported, hardware_specified: Partial, hyperparameters: Partial, protocol_described: Partial, project_page: Not reported, concerns: Real-world evaluation omits the Navigation-in-Crowds scenario where all models degraded; collision definition is human-must-yield.}
limitations_flags: [limited-scenarios, no-human-study, dataset-bias]
web_verification_required: []
cited_missing: [OLiVia-Nav (in corpus), CityWalker (CVPR 2025), LeLaN, VANP, CAHSOR]
external_verification: {verified_on: '2026-10-19', status_class: 'A: published, peer-reviewed', source: Crossref DOI 10.1109/ICRA57385.2026.11696112, arxiv_id: 2506.14233v1}
stage2: {added: true, download_source: 'https://arxiv.org/pdf/2506.14233v1', source_type: arXiv (author version), inclusion_reason: Direct FM social navigation; criteria A+B+C met; peer-reviewed; not cited by Cai 2026 though published on arXiv before its cut-off.}
coding: {latency_reported: 'No', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: 'No', code_released: 'No', new_dataset_released: 'No', real_robot: Systematic, human_subject_study: 'No'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A5, A6]
  C_capabilities: {SAF1: 'Yes', SAF2: Partial, SPA1: 'No', SPA2: 'No', SPA3: Partial, SPA4: Partial, HUM1: Partial, HUM2: Partial, NOR1: Partial, NOR2: 'No', NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: Partial}
  B_roles: [R1, R2]
  D_interface: [D7]
  E_evidence_profile: {EV1_offline: 'Yes', EV2_closed_loop_sim: 'No', EV3_physical_robot: systematic, EV4_real_humans_in_trials: present-type-unreported, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: 10 real trials per scenario per method, statistical_testing: 'No', cross_environment: 'Yes', runtime_measured: 'No'}
  cross_cutting: {temporal_coupling: training-only, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'No', uncertainty: 'No', hallucination_mitigation: 'No', privacy_constraint: 'No', inference_location: n/a (FM used at training time only)}
physical_source_folder: "04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core"
analytical_category: "S4"
coding:
  latency_reported: "No"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "No"
  code_released: "No"
  new_dataset_released: "No"
  real_robot: "Systematic"
  human_subject_study: "No"
---

# Narrate2Nav (Payandeh et al., ICRA 2026)

Page convention: PDF index of the corpus copy (arXiv v1).

## A. Bibliographic
ICRA 2026, pp. 21696-21703, DOI 10.1109/ICRA57385.2026.11696112 (externally verified via Crossref, 2026-10-19). Corpus copy: arXiv:2506.14233v1. George Mason University. Peer-reviewed: Yes.

## B. Position
S4 direct. A VLM is used as a training-time narrator/teacher rather than an online planner: implicit language reasoning is distilled into an RGB-only vision-action student (I6). Added in Stage 2 (targeted search); not cited by Cai et al. 2026 although on arXiv since June 2025.

## C. Research problem
How to exploit human-like language reasoning (social cues, human intentions) in real-time navigation without large-VLM latency (p.2). Contributions: Narrate2Nav model; SSL framework aligning visual features with textual signals; real-world and offline comparison.

## D. Method
Teacher (~330M): frozen DINOv2 vision, CLIP text, linear waypoint encoder, cross-modal transformer; trained to reconstruct future trajectories from future frames, actions and text (narration, CoT, trajectory description generated by Qwen2-VL-72B on images with overlaid future waypoints) (p.4). Student (~29M, ResNet50): past RGB + goal; Barlow Twins alignment of context tokens with the teacher's future multimodal embedding; goal masking; MSE-trained decoder; Pure Pursuit execution.

## G. Social capabilities
C1 Yes (collisions counted as human-must-yield events, 10 trials) · C2 Partial · C5/C6/C7 Partial (human motion and intent appear only in training narrations and attention maps) · C12 Partial (qualitative yielding, Fig. 4) · C13 Partial (frontal approach) · C14 Partial (narrow passageway) · C17 Partial (crowd scenario offline only) · C20 Partial (displacement errors to human demonstrations) · C24 Partial · others No.

## H/I. Integration I6; Evidence E3.

## L. Quantitative results
Offline unseen set, All: AOE/ADE/FDE 0.04/0.16/0.24 vs NoMaD 0.09/0.34/0.61 (Table 1). Real world (per 10 trials, All): collision 3.25 vs GNM 4.3, ViNT 5.25, NoMaD 5; success 8.5 vs 6, 5.75, 5.75 (Table 2). Narrow Passageway: Narrate2Nav success 4/10 vs baselines 8-10/10. Ablation without text: ADE 0.19 vs 0.16.

## M. Deployment
Student-only inference from 5 RGB frames; no FM at runtime; rate not reported.

## N. Limitations
1. Stated: crowd scenario degraded for all models (excluded from real-world table) (p.8).
2. Observable: abstract assigns 52.94% to offline and 41.67% to real-world improvement, while the contribution list states the reverse (data-quality issue); no human study; collision metric is human-yield events; narrow-passage success is the lowest of all methods.

## P. Direct-paper questions (abridged)
1 Real-time human-aware visual navigation. 3 Qwen2-VL-72B (offline), CLIP, DINOv2. 6 Narrations, CoT, trajectory descriptions (training). 7 Distillation into a student policy. 8 Student outputs waypoints. 10 No safety layer. 12 AOE/ADE/FDE; collisions and success per 10 trials. 23 Real robot yes. 24 No human study. 26 Cannot conclude anything about crowd navigation (excluded) or human perception.

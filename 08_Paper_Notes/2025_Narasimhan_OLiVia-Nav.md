---
id: 2025_Narasimhan_OLiVia-Nav
source_pdfs: [04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/2409.13675v2.pdf]
duplicate_copies: []
related_versions: ['Published version: ICRA 2025, pp.9130-9137 (as cited by Cai 2026 [71], Fang 2026 [35], GSON [25]); NOT in corpus']
title: 'OLiVia-Nav: An Online Lifelong Vision Language Approach for Mobile Robot Social Navigation'
authors: &id001 [Siddarth Narasimhan, Aaron Hao Tan, Daniel Choi, Goldie Nejat]
year: 2025
venue: 2025 IEEE International Conference on Robotics and Automation (ICRA)
volume: NA
issue: NA
pages: 9130-9137
doi: 10.1109/ICRA55743.2025.11128004
url: https://doi.org/10.1109/ICRA55743.2025.11128004
pub_status: conference (corpus copy is preprint)
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1109/ICRA55743.2025.11128004); arXiv abs page (2409.13675v2). PDF-derived basis (Stage 1): Corpus PDF is arXiv v2 without venue. Cited by three peer-reviewed/preprint corpus papers as ICRA 2025 pp.9130-9137. Published version authoritative; WEB_VERIFICATION_REQUIRED.'
category: S4
folder: 04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core
folder_category_match: 'Yes'
category_rationale: Distils GPT-4o social-context captions into lightweight CLIP-style encoders whose embeddings condition a learned trajectory planner and selector; real-robot social navigation evaluation.
paper_type: method
fm_used: 'Yes'
fm_class: [VLM, CLIP-style]
fm_models: [GPT-4o (caption teacher; also GPT4 in LLU), 'SC-CLIP: ViT-L/14 image encoder + transformer text encoder (Long-CLIP style)']
fm_size: Not reported (ViT-L/14 backbone)
method_family: [distillation (contrastive), imitation learning (WTA trajectory loss), multi-head cross-attention, GRU trajectory heads, online lifelong learning, PID control]
roles: [F1, F4, F5, F8, F11]
roles_evidence: {F8: 'GPT-4o captions (20,000 MuSoHu images) used to train SC-CLIP encoders = distillation of social reasoning (p.3-4).', F11: GPT-4o used as annotator to generate long/short captions and in LLU to label new images online (p.4)., F1: 'Captions describe social scenario, objects and people (Fig.2).', F4: Long caption includes high-level socially compliant navigation action (Fig.2)., F5: 'Text embedding retrieved from caption database guides Trajectory Selection Module to pick among K=5 trajectories (Eq.7, p.4) - learned selector, not the VLM itself.'}
integration: I6
integration_rationale: Distilled VLM image embedding conditions a learned trajectory planning network (IL from MuSoHu expert trajectories) and text embedding conditions a learned selector; PID tracks the selected trajectory (p.3-4).
evidence: E3
evidence_rationale: Real-robot (Clearpath Jackal) experiments in a university building with 4 scenarios x 3 trials vs VLM-Social-Nav and MultiSoc, with Friedman/Wilcoxon tests; no human-perception study; ablation offline on MuSoHu hold-out (p.5-6).
inputs: [RGB, 3D LiDAR, goal pose, text caption database (embeddings)]
outputs: [learned embedding, trajectory (K=5 candidates), path ranking/selection, velocity/action (PID)]
human_repr: [learned embedding (social context image embedding), LiDAR voxel features, natural-language caption (training/LLU only)]
capabilities: {C1: Partial, C2: 'No', C3: 'Yes', C4: 'No', C5: Partial, C6: 'No', C7: 'No', C8: 'No', C9: Partial, C10: 'No', C11: Partial, C12: 'No', C13: Partial, C14: 'No', C15: 'No', C16: 'No', C17: Partial, C18: 'No', C19: 'No', C20: Partial, C21: 'No', C22: 'No', C23: 'No', C24: Partial, C25: 'No'}
exp:
  datasets: ['MuSoHu: Social Context Dataset 20,000 images + GPT-4o captions; Trajectory Planning Dataset 5,000 expert trajectories; Trajectory Selection Dataset 20,000 predicted trajectories']
  simulators: []
  robots: [Clearpath Jackal]
  environment: University of Toronto building (hallway, blind corner, open space)
  indoor_outdoor: indoor
  sensors: [RGB camera, 3D LiDAR]
  humans: 'real dynamic people and static/dynamic groups (counts per scenario: 2; 1; 2 static groups + 3 dynamic; 2 dynamic groups + 2 dynamic)'
  n_scenes: 4 scenarios
  n_trajectories: 3 trials per scenario
  n_participants: Not reported
  split: MuSoHu hold-out test set for ablation (size not reported)
  baselines: [VLM-Social-Nav (reimplemented with GPT4o), MultiSoc (GNN + DRL)]
  ablation: Yes (w/o E_I, w/o E_T, w/o E_L; before/after LLU update)
  real_robot_trials: 'Yes'
  human_study: 'No'
  statistical_testing: Yes (Friedman p<0.001; post-hoc Wilcoxon signed-rank with Bonferroni p<0.025)
  scenarios: [narrow corridor (frontal), blind corner, static groups + dynamic people, dynamic groups + dynamic people]
metrics: [OTHER | Mean squared error (MSE) | m^2 (implied) | positional error between robot trajectory and teleoperated ground truth | p.5, OTHER | Hausdorff loss | m (implied) | shape similarity between actual and GT trajectory | p.5, SOCIAL | Personal space violation duration (PSV) | s | time robot is within personal space of a person (<0.25 m) | p.5, 'DEPLOY | Planning rate | Hz | average 5 Hz (OLiVia-Nav, MultiSoc) vs 0.6 Hz (VLM-Social-Nav) | p.6']
deployment: {fm_model: SC-CLIP lightweight encoders at runtime; GPT-4o offline and in LLU, model_size: Not reported, api_cloud_local: Runtime local encoders; GPT-4o cloud for caption generation/LLU, onboard_offboard: Not reported, gpu: NVIDIA H100 80GB (training), cpu: Not reported, latency: average 5 Hz planning (OLiVia-Nav); VLM-Social-Nav with GPT4o average 0.6 Hz (p.6), query_frequency: GPT-4o only in LLU batch updates (|B| = 50 images), planner_frequency: ~5 Hz average, controller_frequency: Not reported, asynchronous: Yes (LLU update decoupled from navigation), caching: Caption embedding database D_T for retrieval, event_triggered: LLU triggered when buffer fills, distillation: Yes (SC-CLIP), quantization: 'No', fallback_planner: No separate planner described, safety_shield: Not reported (LiDAR embedding in TPN; no explicit shield), emergency_behavior: Not reported, uncertainty: No (K=5 multimodal trajectories), hallucination_mitigation: 'No', real_time_claim_supported: 'Partial: 5
    Hz average reported'}
repro: {code: Not reported, code_url: Not reported, dataset: Derived from MuSoHu (release not stated), dataset_url: NA, checkpoints: Not reported, prompts_published: No (example captions only), hardware_specified: Partial (training GPU), hyperparameters: 'Yes (batch sizes, LR, WD, epochs, C=128, 32 heads, K=5)', protocol_described: Partial, project_page: Video link only, concerns: Ground truth teleoperated by one researcher; trajectory similarity metrics favour IL methods; no collision metric.}
limitations_flags: [limited-scenarios, no-human-study, dataset-bias]
web_verification_required: [Confirm ICRA 2025 publication details.]
cited_missing: [MultiSoc (Escudie 2024), SRLM (Wang 2024 LLM+DRL), THOR-MAGNI, Okunevich 2024 online context learning, Weinrich 2013 lifelong learning, Long-CLIP, EWareNet, CoMet, SafeCrowdNav, Panigrahi 2023 multimodal perception study, VLMs provide promptable representations for RL]
coding: {latency_reported: 'Yes', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: 'No', code_released: 'No', new_dataset_released: 'No', real_robot: Systematic, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2025
  authors: *id001
  venue: arXiv:2409.13675v2 (corpus copy); published IEEE ICRA 2025 per citing papers
  volume: Not reported
  issue: Not reported
  pages: 8 (arXiv PDF); 9130-9137 (ICRA 2025, per citations)
  doi: Not reported
  url: https://youtu.be/eyFJiOIITO0 (video)
  pub_status: conference (corpus copy is preprint)
  peer_reviewed: 'Yes'
  peer_review_basis: Corpus PDF is arXiv v2 without venue. Cited by three peer-reviewed/preprint corpus papers as ICRA 2025 pp.9130-9137. Published version authoritative; WEB_VERIFICATION_REQUIRED.
project_url: https://youtu.be/eyFJiOIITO0 (video)
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: 2025 IEEE International Conference on Robotics and Automation (ICRA)
  verified_doi: 10.1109/ICRA55743.2025.11128004
  verified_url: https://doi.org/10.1109/ICRA55743.2025.11128004
  verified_pages: 9130-9137
  arxiv: 2409.13675v2
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1109/ICRA55743.2025.11128004)', arXiv abs page (2409.13675v2)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A5, A6]
  C_capabilities: {SAF1: Partial, SAF2: 'No', SPA1: 'Yes', SPA2: Partial, SPA3: Partial, SPA4: Partial, HUM1: Partial, HUM2: 'No', NOR1: Partial, NOR2: 'No', NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: Partial}
  B_roles: [R1]
  D_interface: [D5, D7]
  E_evidence_profile: {EV1_offline: 'Yes', EV2_closed_loop_sim: 'No', EV3_physical_robot: systematic, EV4_real_humans_in_trials: staged, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: 3 trials per scenario, statistical_testing: Yes (Friedman p<0.001; post-hoc Wilcoxon signed-rank with Bonferroni p<0.025), cross_environment: No/unclear, runtime_measured: 'Yes'}
  cross_cutting: {temporal_coupling: per-decision, memory: lifelong caption/embedding database, continual_adaptation: online lifelong update, explanation_output: 'No', safety_guard: 'No', uncertainty: 'No', hallucination_mitigation: 'No', privacy_constraint: 'No', inference_location: hybrid (local + cloud)}
physical_source_folder: "04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core"
analytical_category: "S4"
coding:
  latency_reported: "Yes"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "No"
  code_released: "No"
  new_dataset_released: "No"
  real_robot: "Systematic"
  human_subject_study: "No"
---

# OLiVia-Nav (Narasimhan, Tan, Choi, Nejat — arXiv 2024 / ICRA 2025)

Page convention: PDF index (p.N) of arXiv v2.

## A. Bibliographic
Corpus `04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/2409.13675v2.pdf` (arXiv v2; no venue on PDF). Univ. of Toronto ASBLab. Cited in corpus as ICRA 2025 pp.9130–9137 → treat as peer-reviewed; published version not in corpus (WEB_VERIFICATION_REQUIRED). Video https://youtu.be/eyFJiOIITO0.

## B. Position — S4
First corpus method to *distil* large-VLM social reasoning into lightweight encoders that condition a learned trajectory generator (IL), plus online lifelong adaptation. Representative of the "FM as teacher / representation provider" pattern.

## C. Research problem
- **Problem:** HMB and HMF methods ignore social/environment context and cannot adapt to new scenarios; LLM/VLM methods have slow response times causing collisions (p.1–2).
- **Claims:** "first architecture to leverage both the social reasoning capabilities of large VLMs, and the smaller size and faster response time of lightweight VLMs" (p.1); contributions SC-CLIP distillation and trajectory planning network with multi-head attention; online lifelong learning.
- Formulation: predict K socially compliant trajectories minimising WTA loss to expert trajectory (Eq.1–2).

## D. Technical method
- **SC-CLIP (p.3):** GPT-4o generates long and short captions (social scenario, objects/people, high-level action); train image encoder F_I (ViT-L/14) and text encoder F_T jointly with Long-CLIP style loss incl. Principal Component Extraction (Eq.3).
- **LLU (p.4):** buffer |B| images during navigation → GPT4 captions → symmetric image–text fine-tuning (Eq.4); i_t = 1, |B| = 50 in ablation.
- **TPN (p.4):** LiDAR voxel encoder (5 residual blocks), goal FFN, cross-attention over E_I, E_L, E_G (Eq.5–6), K = 5 GRU heads; trained by WTA on MuSoHu expert trajectories (10 future poses).
- **TSM (p.4):** text embedding retrieved from D_T by cosine similarity with E_I; FFN+GRU; CE loss on index of trajectory matching caption's action (Eq.7).
- **NC:** PID to follow selected trajectory.
- Training: H100 80 GB; SC-CLIP batch 256, LR 1e-4 cosine, AdamW WD 0.01, 100 epochs; TPN batch 10, LR 8e-4, WD 1e-4, 500 epochs, C = 128, 32 heads; TSM batch 128, LR 1e-5, WD 1e-5, 500 epochs (p.5).

## E. Human/social representation — implicit learned embedding (from image + distilled captions) and LiDAR geometry; no explicit human states, predictions, or groups.

## F. Roles — F8 (primary), F11, F1, F4, F5 (via learned selector).

## G. Social capabilities
C1 Partial (LiDAR embedding; w/o E_L ablation collided offline; collisions not reported in real tests) · C3 Yes (PSV) · C5 Partial (implicit) · C9 Partial (static/dynamic group scenarios, no group metric) · C11/C13 Partial (GT teleoperated "using North American social navigation rules") · C17 Partial (up to 6 people) · C20 Partial (similarity to teleop trajectories) · C24 Partial · others No.

## H. Integration — I6. ## I. Evidence — E3 (with statistics).

## J. Experimental evidence
Clearpath Jackal; Univ. of Toronto building; 4 scenarios × 3 trials: narrow hallway (2 people head-on), blind corner (1 dynamic person), 2 static groups + 3 dynamic people, 2 dynamic groups + 2 dynamic people (p.5). GT teleoperated by one researcher. Baselines VLM-Social-Nav (GPT4o) and MultiSoc. Statistics: Friedman p < 0.001; Wilcoxon with Bonferroni p < 0.025 (p.6).

## K. Metrics — MSE, Hausdorff, PSV (<0.25 m), planning rate.

## L. Quantitative results (Table I, p.6; MSE / Haus / PSV s)
| Scenario | OLiVia-Nav | VLM-Social-Nav | MultiSoc |
|---|---|---|---|
| Narrow Hallway | 0.1075 / 0.7348 / 1.2 | 0.1915 / 0.8785 / 1.9 | 0.2968 / 0.9095 / 2.1 |
| Blind Corner | 0.0236 / 0.2572 / 0.4 | 0.0755 / 0.5384 / 2.6 | 0.1021 / 0.4596 / 2.8 |
| Static Groups + Dynamic People | 0.2195 / 0.7563 / 2.1 | 0.4361 / 1.5579 / 3.5 | 0.2747 / 1.1081 / 3.2 |
| Dynamic Groups + Dynamic People | 0.0733 / 0.4813 / 3.3 | 0.1459 / 0.6832 / 4.7 | 0.1154 / 0.7929 / 4.5 |
Rates: VLM-Social-Nav avg 0.6 Hz; OLiVia-Nav and MultiSoc avg 5 Hz (p.6).
Table II ablation (MSE / Haus, before → after LLU): OLiVia-Nav 0.2981/1.8087 → 0.2521/1.4893; w/o E_I 0.4412/2.3772 → 0.3701/2.0839; w/o E_T 0.3838/2.1063 → 0.3791/2.0349; w/o E_L 0.4382/2.3681 → 0.4180/2.1894.

## M. Deployment — 5 Hz average planning; onboard compute not specified; GPT-4o only offline/LLU.

## N. Limitations
1. **Stated:** future work on larger environments with crowds (p.6). No explicit limitation section.
2. **Future work:** larger environments with crowds.
3. **Observable:** GT from single teleoperator; 3 trials; similarity-to-teleop metrics; no collision or group-intrusion metrics; LLU effect only offline; PSV threshold 0.25 m (very small personal space).
4. Deferred.

## O. Reproducibility — hyperparameters given; code/data not stated.

## P. Direct-paper questions
1 Socially compliant trajectory generation with context awareness and online adaptation. 2 Large-VLM social reasoning but too slow → distil. 3 GPT-4o teacher; SC-CLIP encoders. 4 RGB (encoders); LiDAR + goal (planner). 5 Teacher prompted for long/short captions (prompt not published). 6 Captions (teacher); embeddings (student). 7 Embeddings condition TPN/TSM → trajectory → PID. 8 No (distilled encoder conditions learned policy). 9 TPN/TSM networks, PID. 10 None explicit. 11 Socially compliant, adaptive. 12 Trajectory similarity to teleop + PSV. 13 Implicitly. 14 Implicitly (scenarios with groups). 15 No. 16 No. 17 Via teacher captions. 18 No. 19 No. 20 No. 21 5 Hz. 22 Not stated. 23 Yes. 24 No. 25 Lower PSV and trajectory errors with significance tests. 26 Cannot conclude human comfort, generalisation beyond one building, or that lower trajectory error = more social behaviour.

## Q. Cited works possibly missing — MultiSoc; SRLM; THÖR-MAGNI; Okunevich 2024; Long-CLIP; EWareNet; CoMet.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue 2025 IEEE International Conference on Robotics and Automation (ICRA); DOI 10.1109/ICRA55743.2025.11128004; pages 9130-9137; URL https://doi.org/10.1109/ICRA55743.2025.11128004.
- Sources: Crossref (exact title match, DOI 10.1109/ICRA55743.2025.11128004); arXiv abs page (2409.13675v2).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - venue: PDF-derived 'arXiv:2409.13675v2 (corpus copy); published IEEE ICRA 2025 per citing papers' -> externally verified '2025 IEEE International Conference on Robotics and Automation (ICRA)'
- Changed field - volume: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - issue: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - pages: PDF-derived '8 (arXiv PDF); 9130-9137 (ICRA 2025, per citations)' -> externally verified '9130-9137'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified '10.1109/ICRA55743.2025.11128004'
- Changed field - url: PDF-derived 'https://youtu.be/eyFJiOIITO0 (video)' -> externally verified 'https://doi.org/10.1109/ICRA55743.2025.11128004'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

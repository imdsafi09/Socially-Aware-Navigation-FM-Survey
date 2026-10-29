---
id: 2024_Shcherbyna_Arena-4.0
source_pdfs: [06_Datasets_Benchmarks_Evaluation/2409.12471v1.pdf]
duplicate_copies: []
related_versions: [Arena-Rosnav 1.0 (IROS 2021) - in corpus (2021_Kastner_Arena-Rosnav), Arena-Bench (RA-L 2022) - not in corpus, Arena-Rosnav 2.0 (IROS 2023) - not in corpus, Arena 3.0 (RSS 2024) - not in corpus]
title: 'Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation'
authors: &id001 [Volodymyr Shcherbyna, Linh Kästner, Diego Diaz, Huu Giang Nguyen, Maximilian Ho-Kyoung Schreff, Tim Seeger, Jonas Kreutz, Ahmed Martban, Zhengcheng Shen, Huajian Zeng, Harold Soh]
year: 2025
venue: 2025 IEEE International Conference on Robotics and Automation (ICRA)
volume: NA
issue: NA
pages: 9138-9144
doi: 10.1109/ICRA55743.2025.11127635
url: https://doi.org/10.1109/ICRA55743.2025.11127635
pub_status: conference (corpus copy is arXiv author version)
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1109/ICRA55743.2025.11127635); arXiv abs page (2409.12471v1). PDF-derived basis (Stage 1): arXiv v1; no venue printed; no corpus paper cites a published version. WEB_VERIFICATION_REQUIRED.'
category: S6
folder: 06_Datasets_Benchmarks_Evaluation
folder_category_match: 'Yes'
category_rationale: ROS2 development/benchmarking platform for social navigation; LLM+GNN+diffusion world generation; host platform of SocialNav2025 competition (p.1, p.5).
paper_type: simulator
fm_used: 'Yes'
fm_class: [LLM]
fm_models: [Not reported (unnamed LLM), diffusion model (unnamed)]
fm_size: Not reported
method_family: [benchmark platform, LLM text-to-3D-scene-graph, GNN floor-plan generation, semantic vector model database, HuNavSim pedestrian simulation]
roles: [F11]
roles_evidence: {F11: 'LLM converts text prompts into 3D scene graphs used to generate benchmark worlds of graded difficulty (Arena-gen, p.3-4); FM supports benchmark construction, not navigation.'}
integration: NA
integration_rationale: FM used only for environment generation; no FM in the navigation loop.
evidence: NA
evidence_rationale: 'No navigation evaluation reported: only a usability user study (20 participants) and world-generation statistics over 5000 generated worlds (p.5-6); E-scale not applicable.'
inputs: [text prompt or 2D floor plan (for world generation)]
outputs: [3D simulation worlds and scenarios (Gazebo/Unity)]
human_repr: [HuNavSim simulated pedestrians with social states and human-human/human-object interactions (p.4-5)]
capabilities: {C1: Not reported, C2: Not reported, C3: Not reported, C4: 'No', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: 'No', C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: 'No', C24: 'No', C25: 'No'}
exp:
  datasets: [CubiCasa5K (~5000 floor plans) for GNN training]
  simulators: [Gazebo Garden, Unity]
  robots: ['not evaluated (supports ROS2 robots, e.g. Unitree Go2)']
  environment: generated indoor worlds (hospital, residential, office)
  indoor_outdoor: indoor
  sensors: []
  humans: simulated (HuNavSim); not evaluated
  n_scenes: 5000 generated worlds (statistics); 100 batches for latency
  n_trajectories: NA
  n_participants: 20 (usability study)
  split: NA
  baselines: []
  ablation: 'No'
  real_robot_trials: 'No'
  human_study: Yes (platform usability questionnaire, not robot behaviour)
  statistical_testing: 'No'
  scenarios: []
metrics: [OTHER | Room/leaf-room/asset/doorway counts vs LLM-estimated difficulty | count | scene-graph statistics of generated worlds | p.6, OTHER | Graph edges and diameter | count | connectivity of generated scene graphs | p.6, 'DEPLOY | Generation component latency | s (Fig.7) | per generated world on RTX 4080, 100 cold-cache batches | p.6', HUMAN | Usability questionnaire | qualitative | 20 participants; responses published online | p.5]
deployment: {fm_model: Not reported, model_size: Not reported, api_cloud_local: Not reported, onboard_offboard: NA, gpu: RTX 4080 (generation benchmark), cpu: Not reported, latency: Fig.7 only (values not in text), query_frequency: NA, planner_frequency: NA, controller_frequency: NA, asynchronous: NA, caching: NA, event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: NA, safety_shield: NA, emergency_behavior: NA, uncertainty: NA, hallucination_mitigation: NA, real_time_claim_supported: NA}
repro: {code: Yes (stated), code_url: 'https://github.com/Arena-Rosnav', dataset: Model database released (stated), dataset_url: 'https://github.com/Arena-Rosnav', checkpoints: Not reported, prompts_published: Partial (example prompts), hardware_specified: Partial, hyperparameters: 'No', protocol_described: Partial, project_page: Not reported, concerns: LLM not named; no navigation benchmarking results; user-study results described only qualitatively.}
limitations_flags: [no-human-study]
web_verification_required: [Publication status of Arena 4.0; identity of LLM/diffusion models.]
cited_missing: [Arena 3.0 (RSS 2024), Arena-Bench (RA-L 2022), Arena-Rosnav 2.0 (IROS 2023), HuNavSim (RA-L 2023), SocialGym 2.0 (AAAI 2024), SEAN 2.0 (RA-L 2022), Habitat 3.0, CoNav benchmark, DynaBARN, MRPB 1.0, SACSoN (RA-L 2023), SiT dataset (NeurIPS 2023), Language and sketching LLM navigation (ICRA 2024), Principles and guidelines for evaluating social robot navigation (Francis)]
dataset: {kind: simulator/benchmark platform, real_synthetic: synthetic, size: procedurally generated (e.g. 5000 worlds); >100 obstacle and >15 human models, environments: 'indoor hospital, residential, office', sensors: simulator-dependent (not specified), ego_view: Not reported, rgb: Not reported, rgbd: Not reported, lidar: Not reported, human_trajectories: Simulated (HuNavSim), dynamic_humans: 'Yes', group_ann: Partial (human-human interactions simulated), intention_ann: 'No', activity_ann: Partial (human-object interactions), language_ann: Partial (text-to-world prompts; semantic asset annotations), social_rule_ann: 'No', preference_ann: 'No', multi_action_ann: 'No', personal_space_ann: 'No', site_diversity: High (generated), closed_loop: Yes (simulator), vlm_suitability: Medium (language interface for world generation; rendering fidelity not evaluated), real_robot_compat: Partial (ROS2/Nav2; sim-to-real pipeline future work), standard_metrics: Universal metrics recorder mentioned (p.4)
    but metrics not listed, known_limitations: 'Users requested more realistic simulators (Isaac, Habitat); evaluation pipeline found counterintuitive (p.5-6)'}
coding: {latency_reported: Partial, safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: 'Yes', new_dataset_released: 'Yes', real_robot: 'No', human_subject_study: Text-raters/other}
pdf_metadata_stage1:
  year: 2024
  authors: *id001
  venue: arXiv:2409.12471v1 [cs.RO], 19 Sep 2024
  volume: NA
  issue: NA
  pages: '7'
  doi: Not reported
  url: https://github.com/Arena-Rosnav
  pub_status: preprint; benchmark/dataset (platform)
  peer_reviewed: 'No'
  peer_review_basis: arXiv v1; no venue printed; no corpus paper cites a published version. WEB_VERIFICATION_REQUIRED.
project_url: https://github.com/Arena-Rosnav
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: 2025 IEEE International Conference on Robotics and Automation (ICRA)
  verified_doi: 10.1109/ICRA55743.2025.11127635
  verified_url: https://doi.org/10.1109/ICRA55743.2025.11127635
  verified_pages: 9138-9144
  arxiv: 2409.12471v1
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1109/ICRA55743.2025.11127635)', arXiv abs page (2409.12471v1)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A4]
  C_capabilities: {SAF1: 'No', SAF2: 'No', SPA1: 'No', SPA2: 'No', SPA3: 'No', SPA4: 'No', HUM1: 'No', HUM2: 'No', NOR1: 'No', NOR2: 'No', NOR3: 'No', NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'No', EV3_physical_robot: none, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: text-raters, EV6_open_world_deployment: 'No'}
physical_source_folder: "06_Datasets_Benchmarks_Evaluation"
analytical_category: "S6"
coding:
  latency_reported: "Partial"
  safety_mechanism: "NA"
  uncertainty_treatment: "NA"
  hallucination_treatment: "NA"
  code_released: "Yes"
  new_dataset_released: "Yes"
  real_robot: "No"
  human_subject_study: "Text-raters/other"
---

# Arena 4.0 (Shcherbyna, Kästner et al., arXiv 2024)

Page convention: PDF index (p.N).

## A. Bibliographic — arXiv:2409.12471v1 (19 Sep 2024); TU Berlin, NUS, TUM. Preprint; no venue. Host platform for SocialNav2025 competition (p.1, p.5).

## B. Position — S6 platform; the only corpus simulator using a foundation model (LLM) — but for **world generation**, not navigation.

## C. Research problem — sim2real gap from ROS1 dependence, fragmentation, limited environment variety (p.1–2). Contributions: ROS2 migration; generative world/scenario pipeline; semantic 3D model database; HuNavSim extension and usability features (p.2).

## D. Method — Arena-gen: LLM transforms text prompt into a 2-level 3D scene graph (rooms + assets with NL descriptions); GNN trained on CubiCasa5K-derived (3DSG, floor plan) pairs produces annotated floor plans and asset regions; population stage fills zones from a prompt-queriable vector model database with a Fitter algorithm (p.3–4). Abstract mentions diffusion models but their role is not described in the body. Scenario generation samples HuNavSim pedestrians in semantic zones (p.4–5).

## F. Roles — F11 only (benchmark construction).

## I. Evidence — NA: no navigation algorithm is evaluated.

## L. Quantitative results — Fig.6: linear growth of rooms/assets/doorways with LLM-estimated difficulty up to 25-room worlds (5000 worlds) — values only graphical; Fig.7 latency per component on RTX 4080 — values only graphical. User study (20 participants, 7 countries): qualitative positive feedback; criticism of evaluation/plotting pipeline (p.5–6).

## N. Limitations
1. **Stated:** feedback that evaluation pipeline counterintuitive; requests for Isaac Gym/Habitat (p.5–6).
2. **Future (p.6):** Isaac Gym/Habitat, MARL, real-robot deployment pipelines, Arena-web v2.
3. **Observable:** no navigation benchmark results; generation "difficulty" is LLM-estimated and validated only by structural counts; LLM/diffusion models unnamed; usability study has no quantitative results in paper.
4. **Relevance:** demonstrates FMs as benchmark-construction tools (generative scenario design), a role distinct from FM-in-the-loop navigation.

## P. Platform analysis — see `dataset:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue 2025 IEEE International Conference on Robotics and Automation (ICRA); DOI 10.1109/ICRA55743.2025.11127635; pages 9138-9144; URL https://doi.org/10.1109/ICRA55743.2025.11127635.
- Sources: Crossref (exact title match, DOI 10.1109/ICRA55743.2025.11127635); arXiv abs page (2409.12471v1).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - year: PDF-derived '2024' -> externally verified '2025'
- Changed field - venue: PDF-derived 'arXiv:2409.12471v1 [cs.RO], 19 Sep 2024' -> externally verified '2025 IEEE International Conference on Robotics and Automation (ICRA)'
- Changed field - pages: PDF-derived '7' -> externally verified '9138-9144'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified '10.1109/ICRA55743.2025.11127635'
- Changed field - url: PDF-derived 'https://github.com/Arena-Rosnav' -> externally verified 'https://doi.org/10.1109/ICRA55743.2025.11127635'
- Changed field - pub_status: PDF-derived 'preprint; benchmark/dataset (platform)' -> externally verified 'conference (corpus copy is arXiv author version)'
- Changed field - peer_reviewed: PDF-derived 'No' -> externally verified 'Yes'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

---
id: 2023_Huang_VoxPoser
source_pdfs: [03_Adjacent_Foundation_Model_Navigation/huang23b.pdf]
duplicate_copies: []
related_versions: []
title: 'VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models'
authors: &id001 [Wenlong Huang, Chen Wang, Ruohan Zhang, Yunzhu Li, Jiajun Wu, Li Fei-Fei]
year: 2023
venue: Proceedings of The 7th Conference on Robot Learning (CoRL 2023), PMLR 229
volume: NA
issue: NA
pages: 540-562
doi: Not found / not applicable
url: https://proceedings.mlr.press/v229/huang23b.html
pub_status: conference
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): PMLR proceedings page (https://proceedings.mlr.press/v229/huang23b.html); arXiv abs page (2307.05973v2). PDF-derived basis (Stage 1): CoRL 2023 footer (p.1); PMLR file name huang23b.'
category: S3
folder: 03_Adjacent_Foundation_Model_Navigation
folder_category_match: 'Yes'
category_rationale: LLM writes code that queries VLM perception to compose 3D affordance/avoidance value maps used as objectives for MPC trajectory synthesis in manipulation; no navigation among humans.
paper_type: method
fm_used: 'Yes'
fm_class: [LLM, VLM]
fm_models: [GPT-4 (OpenAI API), OWL-ViT (open-vocabulary detector), Segment Anything, XMem tracker]
fm_size: Not reported
method_family: [LLM code generation (Code-as-Policies LMPs), value-map composition, model predictive control (random shooting / greedy search), online dynamics learning]
roles: [F6, F7]
roles_evidence: {F6: 'LLM composes affordance, avoidance, velocity, rotation and gripper voxel maps that define the planner''s cost (e.g., ''watch out for the vase'' -> repulsion) (p.4-6).', F7: 'Planner LMP decomposes instructions into sub-tasks (p.3, p.6).'}
integration: I4
integration_rationale: FM output is a cost/constraint map consumed by a motion planner (weighted affordance 2 / avoidance 1), replanned at 5 Hz with cached code.
evidence: E3
evidence_rationale: 'Real-world manipulation: 5 tasks x 10 trials, static and with disturbances (Table 1); simulation 13 tasks x 20 episodes (Table 2); manipulation (not navigation), no human study.'
inputs: [RGB-D (multi-camera), free-form language instruction]
outputs: [3D value maps (100^3 voxels), 6-DoF end-effector trajectories via MPC]
human_repr: [none]
capabilities: {C1: NA, C2: NA, C3: NA, C4: NA, C5: NA, C6: NA, C7: NA, C8: NA, C9: NA, C10: NA, C11: NA, C12: NA, C13: NA, C14: NA, C15: NA, C16: NA, C17: NA, C18: NA, C19: NA, C20: NA, C21: NA, C22: NA, C23: NA, C24: NA, C25: NA}
exp:
  datasets: []
  simulators: ['simulated tabletop mirroring real setup (13 tasks, 2766 instructions)', door/window/fridge contact-rich sim tasks]
  robots: [real manipulator (Appendix A.3; not named in main text)]
  environment: tabletop / household objects
  indoor_outdoor: indoor
  sensors: [RGB-D]
  humans: none (human disturbances in some trials)
  n_scenes: 5 real tasks; 13 sim tasks
  n_trajectories: 10 trials per real task per condition; 20 episodes per sim task; 3 seeds (dynamics learning)
  n_participants: NA
  split: seen/unseen instructions (SI/UI) and attributes (SA/UA)
  baselines: [LLM + Primitives (Code as Policies variant), 'U-Net + MP (learned costmaps, Sharma et al.)', No prior exploration]
  ablation: Yes (error breakdown by component)
  real_robot_trials: 'Yes'
  human_study: 'No'
  statistical_testing: Partial (± over 3 seeds)
  scenarios: []
metrics: ['OTHER | Success rate | % or k/10 | task success (real: static and with disturbances; sim: 20 episodes) | p.7', OTHER | Time | s | online learning time to success; TLE = >12 h | p.8, OTHER | Error breakdown | % | dynamics / perception / specification errors | p.8]
deployment: {fm_model: GPT-4 (API), model_size: Not reported, api_cloud_local: Cloud API, onboard_offboard: Offboard, gpu: Not reported, cpu: Not reported, latency: Not reported, query_frequency: once per sub-task (code cached), planner_frequency: 5 Hz replanning, controller_frequency: Operational space controller (rate not reported), asynchronous: NA, caching: Yes (LLM-generated code reused throughout sub-task), event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: NA, safety_shield: 'No', emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: 'No', real_time_claim_supported: Partial (closed-loop 5 Hz via caching)}
repro: {code: Project page (code availability not stated in main text), code_url: voxposer.github.io, dataset: NA, dataset_url: NA, checkpoints: NA, prompts_published: Yes (appendix), hardware_specified: Partial (appendix), hyperparameters: Partial, protocol_described: 'Yes', project_page: voxposer.github.io, concerns: Manual prompt engineering; GPT-4 API dependence.}
limitations_flags: [cloud-dependence, prompt-sensitivity]
web_verification_required: []
cited_missing: [Sharma et al. language to 2D costmaps, Socratic Models, OWL-ViT, Segment Anything, XMem, Inner Monologue]
adjacent: {mechanism: 'LLM-generated code builds dense affordance/avoidance cost maps grounded by VLM perception, optimized by MPC with fast replanning.', relevance: 'Direct methodological precedent for VLM/LLM-generated cost or constraint maps (F6/I4) used by social navigation planners (e.g., keep away from groups expressed as avoidance maps).', why_not_direct: Manipulation only; no humans or social norms., inherited_by: Cited by corpus MUSON and Pan foundation-language-models navigation review.}
coding: {latency_reported: 'No', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: 'No', code_released: Partial, new_dataset_released: NA, real_robot: Systematic, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2023
  authors: *id001
  venue: 7th Conference on Robot Learning (CoRL 2023), Atlanta (PMLR)
  volume: Not reported
  issue: NA
  pages: 23 (PDF incl. appendix)
  doi: Not reported
  url: voxposer.github.io
  pub_status: conference
  peer_reviewed: 'Yes'
  peer_review_basis: CoRL 2023 footer (p.1); PMLR file name huang23b.
project_url: voxposer.github.io
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: Proceedings of The 7th Conference on Robot Learning (CoRL 2023), PMLR 229
  verified_doi: Not found / not applicable
  verified_url: https://proceedings.mlr.press/v229/huang23b.html
  verified_pages: 540-562
  arxiv: 2307.05973v2
  version_relationship: Corpus copy is the PMLR published version; arXiv 2307.05973v2 alternate
  sources: ['PMLR proceedings page (https://proceedings.mlr.press/v229/huang23b.html)', arXiv abs page (2307.05973v2)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A0]
  C_capabilities: {SAF1: NA, SAF2: NA, SPA1: NA, SPA2: NA, SPA3: NA, SPA4: NA, HUM1: NA, HUM2: NA, NOR1: NA, NOR2: NA, NOR3: NA, NOR4: NA, EXP1: NA, EXP2: NA, EXP3: NA}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: systematic, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "03_Adjacent_Foundation_Model_Navigation"
analytical_category: "S3"
coding:
  latency_reported: "No"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "No"
  code_released: "Partial"
  new_dataset_released: "NA"
  real_robot: "Systematic"
  human_subject_study: "No"
---

# VoxPoser (Huang et al., CoRL 2023)

Page convention: PDF index (p.N).

## A. Bibliographic — CoRL 2023 (footer p.1); Stanford, UIUC.

## B. Position — S3 adjacent: LLM as cost/constraint generator (F6, I4).

## C. Research problem — LLM-based robot systems depend on predefined motion primitives; can LLM knowledge be used at fine-grained action level without training? (p.2). Contributions: value-map composition via LLM code + VLM grounding; zero-shot closed-loop trajectory synthesis; online dynamics learning with LLM priors (p.1–2).

## D. Method — Eq.1: min F_task + F_control s.t. dynamics; F_task = −Σ V(p_j) over voxel value map (p.4). LMPs (5–20 examples each) generate affordance/avoidance/rotation/velocity/gripper maps; Euclidean distance transform and Gaussian smoothing; planner cost = −(2·affordance + 1·avoidance); greedy search for collision-free positions; replanning at 5 Hz; code cached per sub-task (p.5–6).

## L. Quantitative results (visually verified p.7–8)
- Table 1 (real; LLM+Prim. static / dist. vs VoxPoser static / dist.): Move & Avoid 0/10, 0/10 vs 9/10, 8/10; Set Up Table 7/10, 0/10 vs 9/10, 7/10; Close Drawer 0/10, 0/10 vs 10/10, 7/10; Open Bottle 5/10, 0/10 vs 7/10, 5/10; Sweep Trash 0/10, 0/10 vs 9/10, 8/10; Total 24.0%, 0.0% vs 88.0%, 70.0%.
- Table 2 (sim; U-Net+MP / LLM+Prim. / VoxPoser): SI-SA object 21.0 / 41.0 / 64.0; SI-SA composition 53.8 / 43.8 / 77.5; SI-UA object 3.0 / 46.0 / 60.0; SI-UA composition 3.8 / 25.0 / 58.8; UI-UA object 0.0 / 17.5 / 65.0; UI-UA composition 0.0 / 25.0 / 76.7 (%).
- Table 3 (zero-shot / no prior success & time / with prior success & time): Door 6.7% / 58.3% TLE / 88.3% 142.3 s; Window 3.3% / 36.7% TLE / 80.0% 137.0 s; Fridge 18.3% / 70.0% TLE / 91.7% 71.0 s.
- **Data-quality note:** text says exploration without prior "all exceed the maximum 12-hour limit", but Table 3 still lists non-zero "No Prior" success rates (58.3%, 36.7%, 70.0%) alongside TLE — the meaning of these values is not explained.

## N. Limitations
1. **Stated (p.8):** relies on external perception; needs general dynamics models for contact-rich tasks; end-effector-only planning; manual prompt engineering.
2. **Future:** multimodal LLMs for direct grounding; alignment/prompting methods; better trajectory optimization.
3. **Observable:** GPT-4 API dependence; perception main error source in real world.
4. **Social relevance:** mechanism (avoidance value maps from language) transferable to social constraints; not tested with people.

## P. Adjacent analysis — see `adjacent:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue Proceedings of The 7th Conference on Robot Learning (CoRL 2023), PMLR 229; DOI Not found / not applicable; pages 540-562; URL https://proceedings.mlr.press/v229/huang23b.html.
- Sources: PMLR proceedings page (https://proceedings.mlr.press/v229/huang23b.html); arXiv abs page (2307.05973v2).
- Version relationship: Corpus copy is the PMLR published version; arXiv 2307.05973v2 alternate.
- Changed field - venue: PDF-derived '7th Conference on Robot Learning (CoRL 2023), Atlanta (PMLR)' -> externally verified 'Proceedings of The 7th Conference on Robot Learning (CoRL 2023), PMLR 229'
- Changed field - volume: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - pages: PDF-derived '23 (PDF incl. appendix)' -> externally verified '540-562'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified 'Not found / not applicable'
- Changed field - url: PDF-derived 'voxposer.github.io' -> externally verified 'https://proceedings.mlr.press/v229/huang23b.html'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

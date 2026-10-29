---
id: 2026_Chen_SocialNav-CVPR
source_pdfs: [04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/Chen_SocialNav_Training_Human-Inspired_Foundation_Model_for_Socially-Aware_Embodied_Navigation_CVPR_2026_paper.pdf]
duplicate_copies: [06_Datasets_Benchmarks_Evaluation/Chen_SocialNav_Training_Human-Inspired_Foundation_Model_for_Socially-Aware_Embodied_Navigation_CVPR_2026_paper.pdf]
related_versions: []
title: 'SocialNav: Training Human-Inspired Foundation Model for Socially-Aware Embodied Navigation'
authors: [Ziyi Chen, Yingnan Guo, Zedong Chu, Minghua Luo, Yanfen Shen, Mingchao Sun, Junjun Hu, Shichao Xie, Kuan Yang, Pei Shi, Zhining Gu, Lu Liu, Honglin Han, Xiaolong Wu, Mu Xu, Yu Zhang]
year: 2026
venue: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2026)
volume: NA
issue: NA
pages: 28796-28806
doi: Not found / not applicable
url: https://openaccess.thecvf.com/content/CVPR2026/html/Chen_SocialNav_Training_Human-Inspired_Foundation_Model_for_Socially-Aware_Embodied_Navigation_CVPR_2026_paper.html
pub_status: conference; benchmark/dataset
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): CVF Open Access page (author list, pages); arXiv abs page (2511.21135v2). PDF-derived basis (Stage 1): CVF open-access watermark: ''identical to the accepted version'' of CVPR paper (p.1).'
category: S4
folder: 04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core (copy also in 06_Datasets_Benchmarks_Evaluation)
folder_category_match: 'Yes'
category_rationale: Hierarchical VLM 'brain' + flow-matching action expert (VLA-style foundation model) trained with IL + flow-based RL for socially compliant point-goal navigation; also contributes SocNav Dataset and Benchmark.
paper_type: method; dataset; benchmark
fm_used: 'Yes'
fm_class: [VLA, VLM, NavFM]
fm_models: [Qwen2.5-VL 3B (brain), 'Diffusion Transformer flow-matching action expert (12 layers, 12 heads, D=1536)', Qwen2.5-VL-72B (CoT data generation)]
fm_size: 3B VLM + DiT action expert
method_family: [imitation learning, flow matching, 'reinforcement learning (SAFE-GRPO, flow-based GRPO)', chain-of-thought, VQA, 3DGS simulation]
roles: [F1, F4, F10, F11]
roles_evidence: {F1: 'Brain predicts socially traversable region polygons (sidewalks, crosswalks, stairs) and VQA answers (p.5).', F4: Brain produces navigation CoT explanations (p.5); CAD includes 825K CoT samples., F10: 'Action expert conditioned on VLM last-layer latent Z_VLM generates future actions/trajectory end-to-end (Eq.2-3, p.5).', F11: Qwen2.5-VL-72B prompted to generate 825K CoT training samples (p.4).}
integration: I7
integration_rationale: VLM latent features directly condition a flow-matching action head that outputs future actions (VLA-style direct action generation); a locomotion policy executes on the quadruped (p.4-5, p.8).
evidence: E3
evidence_rationale: Closed-loop simulation benchmark (Isaac Sim + 3DGS) and real-robot deployment on Unitree Go2 in three environments x 20 trials (SR only); no human-subject evaluation (p.6-8).
inputs: ['RGB (monocular history, n=5)', 2D positions history, point goal]
outputs: [semantic labels (socially traversable polygons), natural-language reasoning (CoT), VQA answer, trajectory/actions (m=5 future)]
human_repr: [learned embedding (VLM latent), digital humans as collision obstacles in benchmark (evaluation only)]
capabilities: {C1: Partial, C2: 'No', C3: 'No', C4: 'No', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: 'Yes', C12: 'No', C13: 'No', C14: 'No', C15: 'Yes', C16: 'No', C17: Partial, C18: 'No', C19: 'No', C20: Partial, C21: 'No', C22: 'No', C23: 'No', C24: Partial, C25: 'No'}
exp:
  datasets: ['SocNav Dataset (>7M samples): ETP D_video 2.0M pseudo-trajectories; D_sim 1.7M (SocialGS 3,400 3DGS scenes 4.5 km^2; SocCity 3.37 km^2 dynamic city); D_real 340K (SCAND, HuRoN, RECON, CityWalker teleop); CAD: 1.2M social traversability, 825K CoT, 1M general VQA', CityWalker open-loop benchmark]
  simulators: ['Isaac Sim + 3DGS (SocNav Bench: 9 scenes, 73K m^2)']
  robots: [Unitree Go2]
  environment: parks, streets, offices, campus (bench); street crossing, office park, shopping mall (real)
  indoor_outdoor: both
  sensors: [monocular RGB, positions]
  humans: digital humans randomly introduced (sim); real-world presence of humans not explicitly reported
  n_scenes: 9 benchmark scenes x 20 cases (10 start-goal pairs at 20 m and 100 m); 3 real environments
  n_trajectories: 180 benchmark cases; 20 real trials per environment per method
  n_participants: NA
  split: Benchmark environments unseen in training
  baselines: [GNM, ViNT, NoMaD (retrained for point goals; * = trained on D_real only), CityWalker]
  ablation: Yes (data composition D_video, D_sim, D_cog; IL vs RL; RL without D_cog)
  real_robot_trials: 'Yes'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [crosswalk, sidewalk, park trails, turn, detour, proximity, crowd (open-loop categories), shopping mall, office]
metrics: [OTHER | Maximum Average Orientation Error (MAOE) | deg (implied) | open-loop orientation error per CityWalker | p.6, NAV | Success rate (SR) | % | reach within 3 m of goal with fewer than three collisions | p.6, NAV | Route completion (RC) | % | Not defined in detail | p.6, NAV | SPL | % | success weighted by path length | p.6, SOCIAL | Distance Compliance Rate (DCR) | % | d_compliant/d_actual if success else 0 (distance travelled within socially compliant regions) | p.6, SOCIAL | Time Compliance Rate (TCR) | % | analogous time fraction within compliant regions | p.6, DEPLOY | Control rate | Hz | 'over 5 Hz' during deployment | p.8]
deployment: {fm_model: Qwen2.5-VL-3B + DiT flow action expert, model_size: 3B + DiT, api_cloud_local: Cloud server (NVIDIA A10 GPU) guiding robot, onboard_offboard: Offboard (cloud server A10), gpu: NVIDIA A10 (inference); 96/32/16 H20 GPUs (training stages), cpu: Not reported, latency: Operates at over 5 Hz (p.8), query_frequency: '>5 Hz', planner_frequency: '>5 Hz', controller_frequency: Not reported (consistent locomotion policy), asynchronous: Not reported, caching: Not reported, event_triggered: 'No', distillation: 'No', quantization: 'No', fallback_planner: 'No', safety_shield: No explicit shield, emergency_behavior: Not reported, uncertainty: No (flow models multimodal action distribution), hallucination_mitigation: 'No', real_time_claim_supported: 'Partial: >5 Hz reported on cloud A10'}
repro: {code: Not reported in paper, code_url: Not reported, dataset: Not stated as released, dataset_url: NA, checkpoints: Not reported, prompts_published: 'No', hardware_specified: 'Yes', hyperparameters: 'Partial (lr, batch, epochs, GPUs; reward weights in appendix not in PDF)', protocol_described: Partial, project_page: 'https://amap-eai.github.io/SocialNav/', concerns: Appendix (reward formulation) not included; industrial-scale compute; 'social compliance' operationalised as staying in socially traversable regions.}
limitations_flags: [resource-requirements, cloud-dependence, no-human-study, limited-scenarios]
web_verification_required: [Check project page for dataset/code release and appendix.]
cited_missing: [CityWalker, NaVILA, pi0 / pi0.5, Flow-GRPO, ABot-N0, AstraNav-World, NavForesee, MBRA, Seeing to experiencing (scaling navigation FMs with RL), ViPlanner, TrackVLA, NaVid, Urban-Sim micromobility, Aux-Think, Discuss before moving, SayNav, NavCoT, RECON]
coding: {latency_reported: 'Yes', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: 'No', code_released: 'No', new_dataset_released: 'No', real_robot: Systematic, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2026
  authors: [Zedong Chu, Ziyi Chen, Yingnan Guo, Minghua Luo, Yanfen Shen, Junjun Hu, Shichao Xie, Kuan Yang, Pei Shi, Zhining Gu, Honglin Han, Xiaolong Wu, Mu Xu, Mingchao Sun, Lu Liu, Yu Zhang]
  venue: IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) 2026 (CVF open-access version)
  volume: Not reported
  issue: Not reported
  pages: 28796-28806
  doi: Not reported
  url: https://amap-eai.github.io/SocialNav/
  pub_status: conference; benchmark/dataset
  peer_reviewed: 'Yes'
  peer_review_basis: 'CVF open-access watermark: ''identical to the accepted version'' of CVPR paper (p.1).'
project_url: https://amap-eai.github.io/SocialNav/
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2026)
  verified_doi: Not found / not applicable
  verified_url: https://openaccess.thecvf.com/content/CVPR2026/html/Chen_SocialNav_Training_Human-Inspired_Foundation_Model_for_Socially-Aware_Embodied_Navigation_CVPR_2026_paper.html
  verified_pages: 28796-28806
  arxiv: 2511.21135v2
  version_relationship: Corpus copy is the CVF open-access version; arXiv 2511.21135v2 alternate. IEEE Xplore DOI not found as of freeze date.
  sources: ['CVF Open Access page (author list, pages)', arXiv abs page (2511.21135v2)]
stage2_id_change: Renamed from 2026_Chu_SocialNav-CVPR (Stage 1 mis-attributed first author; CVF lists Ziyi Chen first)
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A6]
  C_capabilities: {SAF1: Partial, SAF2: 'No', SPA1: 'No', SPA2: 'No', SPA3: 'Yes', SPA4: Partial, HUM1: 'No', HUM2: 'No', NOR1: Partial, NOR2: 'No', NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: Partial}
  B_roles: [R1, R3]
  D_interface: [D6, D7]
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: systematic, EV4_real_humans_in_trials: not-reported, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: 180 benchmark cases; 20 real trials per environment per method, statistical_testing: 'No', cross_environment: 'Yes', runtime_measured: 'Yes'}
  cross_cutting: {temporal_coupling: per-decision, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'No', uncertainty: 'No', hallucination_mitigation: 'No', privacy_constraint: 'No', inference_location: remote server}
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

# SocialNav (Chen et al., CVPR 2026)

Page convention: PDF index (p.N); printed pp.28796–28806. Filename says "Chen_SocialNav" (author list begins Zedong Chu; Ziyi Chen co-first) — we name the note by first listed author.

## A. Bibliographic
CVPR 2026 CVF open-access version ("identical to the accepted version", p.1). Amap/Alibaba + Zhejiang Univ. Project https://amap-eai.github.io/SocialNav/. Peer-reviewed: Yes. Identical copy in 06 folder (md5 match).

## B. Position — S4 (also S6 dataset/benchmark contribution)
Most "foundation-model-native" direct paper in corpus: VLA-style brain–action model trained on 7M samples with flow-based RL. However, its operational notion of "social compliance" is primarily semantic traversability (sidewalks, crosswalks, avoiding lawns/driveways), not interaction with humans.

## C. Research problem
- **Problem:** embodied navigation that adheres to social norms; geometrically optimal trajectories may be socially inappropriate (jaywalking, crossing lawns) (p.1).
- **Claims:** first flow-based RL framework for embodied navigation that rewards socially compliant behaviour (SAFE-GRPO) (p.2); +38% SR and +46% social compliance vs SOTA (abstract).
- **Contributions:** SocialNav foundation model; SAFE-GRPO; SocNav Dataset & Benchmark (p.2).

## D. Technical method
- Problem: history-conditioned point-goal navigation A_{t+1:t+m} = π(O_{t−n:t}, P_{t−n:t}, g), n = m = 5 (Eq.1).
- Brain: Qwen2.5-VL 3B outputs socially traversable polygons, CoT, VQA; last-layer latent Z_VLM (Eq.3).
- Action expert: DiT (12 layers, 12 heads, D = 1536) conditional flow matching, K = 5 denoising steps (p.6).
- Training: Stage 1 pre-train on D_video + D_sim + D_cog (96 H20, batch 192, lr 5e-5, 3 epochs); Stage 2 fine-tune action expert only on D_real (VLM frozen; 32 H20, batch 256, lr 1e-5); Stage 3 SAFE-GRPO on SocCity expert trajectories (16 H20, rollout batch 128, lr 5e-7): ODE→SDE exploration (Eq.4), reward R = R_social + λ R_expert + λ R_smooth + λ R_eff (Eq.5), R_social from semantic occupancy map (clearance from non-traversable areas). Reward is hand-crafted (p.8).
- Data generation: internet-video pseudo-trajectories via π³ reconstruction + MoGe metric alignment; 1.2M manually annotated traversable polygons; 825K CoT generated by Qwen2.5-VL-72B.

## E. Human/social representation
No explicit human model; social norms encoded as traversable regions and CoT; digital humans only as obstacles in benchmark.

## F. Roles — F10 (primary), F1, F4, F11.

## G. Social capabilities
C11 Yes (norm-compliant region use) · C15 Yes (sidewalk/crosswalk; DCR/TCR; street-crossing real trials) · C1 Partial (SR allows <3 collisions; collisions not separately reported) · C17 Partial (open-loop "Crowd" category MAOE) · C20 Partial (smoothness reward; human-like CityWalker GT) · C24 Partial · all human-interaction capabilities (C3–C10, C12–C14, C16, C18, C19, C21–C23, C25) No.

## H. Integration — I7. ## I. Evidence — E3.

## J. Experimental evidence
Open-loop CityWalker benchmark; closed-loop SocNav Bench (Isaac Sim + 3DGS, 9 scenes: 3 parks, 3 streets, 2 offices, 1 campus; 73K m²; Unitree Go2 model; random digital humans; 10 start–goal pairs at 20 m and 100 m → 20 cases/scene; unseen environments); real Unitree Go2 via cloud A10, 3 environments × 20 trials (p.4, 6, 8).

## K. Metrics — MAOE, SR, RC, SPL, DCR, TCR, Hz.

## L. Quantitative results
Table 1 (open-loop MAOE, lower better; Mean / Turn / Crossing / Detour / Proximity / Crowd / Other / All): GNM 16.2/31.1/14.8/12.5/14.7/12.8/11.0/12.1; ViNT 16.5/31.1/15.4/12.9/14.8/13.3/11.6/12.6; NoMaD 19.1/35.1/18.5/15.6/18.1/14.3/12.8/12.1; CityWalker 15.2/26.6/14.1/13.9/14.3/12.0/10.4/11.5; SocialNav (Full) 10.2/20.1/8.8/8.4/8.9/7.6/7.2/7.8.
Table 2 (closed-loop SocNav Bench; SR / RC / SPL / DCR / TCR): GNM* 43.3/62.4/37.0/26.5/28.7; ViNT* 45.6/66.2/39.5/31.4/33.8; NoMaD* 41.1/60.5/35.4/29.5/31.6; CityWalker 47.8/64.7/44.7/36.1/36.6; SocialNav* 65.0/78.4/62.3/58.0/56.7; SocialNav (Full) 86.1/91.2/77.4/82.5/82.9.
Table 3 (real-world success, Street Crossing / Office Park / Shopping Mall / Avg SR %): GNM* 9/20, 10/20, 8/20, 45.0; ViNT* 7/20, 12/20, 8/20, 45.0; NoMaD* 9/20, 11/20, 10/20, 50.0; CityWalker 12/20, 13/20, 12/20, 62.5; SocialNav (Full) 18/20, 16/20, 17/20, 85.0.
Table 4 ablation (SR/RC/SPL/DCR/TCR): 1 SocialNav* (D_real, IL) 65.0/78.4/62.3/58.0/56.7; 2 +D_video 76.7/84.8/70.1/62.9/64.6; 3 +D_sim 82.2/86.0/77.8/69.8/68.2; 4 +D_cog 84.4/88.1/79.4/78.2/78.4; 5 +RL (no D_cog) 80.0/89.1/78.9/68.1/66.9; 6 +RL (full) 86.1/91.2/77.4/82.5/82.9.
- Abstract "+38% SR / +46% social compliance" corresponds to absolute point gains vs CityWalker (86.1 vs 47.8 SR; 82.5 vs 36.1 DCR) on SocNav Bench.

## M. Deployment — cloud A10 inference, >5 Hz; locomotion policy on Go2.

## N. Limitations
1. **Stated (p.8):** RL extends only to semantic traversability; broader context-dependent conventions not captured; reward relies on hand-crafted rules.
2. **Future work:** VLM-provided richer adaptive rewards; broader conventions.
3. **Observable:** "social compliance" = region compliance; no proxemic/human-interaction metric; real-world only SR; real humans' presence/behaviour unreported; benchmark created by authors; massive compute.
4. Deferred.

## O. Reproducibility — project page; training details; reward details in appendix (not in PDF).

## P. Direct-paper questions
1 Socially compliant point-goal navigation respecting walkway/crosswalk norms. 2 Semantic understanding of social norms beyond geometry; generalisation from large data. 3 Qwen2.5-VL-3B + DiT flow expert. 4 Monocular image history + positions + goal. 5 Learned (no runtime prompt). 6 Actions/trajectory (and optional polygons/CoT). 7 Direct (VLA). 8 Yes (via action expert; locomotion policy executes). 9 Unitree locomotion policy. 10 None explicit. 11 Social norm compliance, human-aligned navigation. 12 Region compliance (DCR/TCR), SR, MAOE. 13 No. 14 No. 15 No. 16 No. 17 Yes (traversability norms). 18 Short history (5 frames). 19 No. 20 No. 21 >5 Hz (cloud). 22 No. 23 Not reported. 24 No. 25 Large DCR/TCR gains. 26 Cannot conclude anything about proxemics, yielding, group behaviour, or human-perceived social acceptability.

## Q. Cited works possibly missing — CityWalker (CVPR 2025), NaVILA, π0/π0.5, Flow-GRPO, NaVid, TrackVLA, ABot-N0, MBRA, ViPlanner.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2026); DOI Not found / not applicable; pages 28796-28806; URL https://openaccess.thecvf.com/content/CVPR2026/html/Chen_SocialNav_Training_Human-Inspired_Foundation_Model_for_Socially-Aware_Embodied_Navigation_CVPR_2026_paper.html.
- Sources: CVF Open Access page (author list, pages); arXiv abs page (2511.21135v2).
- Version relationship: Corpus copy is the CVF open-access version; arXiv 2511.21135v2 alternate. IEEE Xplore DOI not found as of freeze date..
- Changed field - authors: PDF-derived '['Zedong Chu', 'Ziyi Chen', 'Yingnan Guo', 'Minghua Luo', 'Yanfen Shen', 'Junjun Hu', 'Shichao Xie', 'Kuan Yang', 'Pei Shi', 'Zhining Gu', 'Honglin Han', 'Xiaolong Wu', 'Mu Xu', 'Mingchao Sun', 'Lu Liu', 'Yu Zhang']' -> externally verified '['Ziyi Chen', 'Yingnan Guo', 'Zedong Chu', 'Minghua Luo', 'Yanfen Shen', 'Mingchao Sun', 'Junjun Hu', 'Shichao Xie', 'Kuan Yang', 'Pei Shi', 'Zhining Gu', 'Lu Liu', 'Honglin Han', 'Xiaolong Wu', 'Mu Xu', 'Yu Zhang']'
- Changed field - venue: PDF-derived 'IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) 2026 (CVF open-access version)' -> externally verified 'Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2026)'
- Changed field - volume: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - issue: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified 'Not found / not applicable'
- Changed field - url: PDF-derived 'https://amap-eai.github.io/SocialNav/' -> externally verified 'https://openaccess.thecvf.com/content/CVPR2026/html/Chen_SocialNav_Training_Human-Inspired_Foundation_Model_for_Socially-Aware_Embodied_Navigation_CVPR_2026_paper.html'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

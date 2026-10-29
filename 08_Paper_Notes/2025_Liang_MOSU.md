---
id: 2025_Liang_MOSU
source_pdfs: [05_Direct_VLM_SocialNav_Preprints/MOSU_arXiv2507.04686v1.pdf]
duplicate_copies: []
related_versions: ['arXiv:2507.04686v1 (7 Jul 2025) = corpus copy (Springer LNCS-style template)']
title: 'MOSU: Autonomous Long-range Robot Navigation with Multi-modal Scene Understanding'
authors: [Jing Liang, Kasun Weerakoon, Daeun Song, Senthurbavan Kirubaharan, Xuesu Xiao, Dinesh Manocha]
year: 2025
venue: International Symposium on Experimental Robotics (ISER) 2025 - per citation in Fang et al. (RA-L 2026, ref. [11]); proceedings not located
volume: Not reported
issue: Not reported
pages: 10 (PDF)
doi: Not found / not applicable
url: https://arxiv.org/abs/2507.04686
pub_status: accepted/presented per citing paper; proceedings not yet indexed
peer_reviewed: Accepted (not yet indexed)
peer_review_basis: Fang et al. (RA-L 2026, in corpus) cite it as "Proc. Int. Symp. Exp. Robot., 2025"; no Crossref/DOI record found (2026-10-19); arXiv v1 has no journal_ref.
category: S5
folder: 05_Direct_VLM_SocialNav_Preprints
folder_category_match: 'Yes'
category_rationale: Gemini ranks CVAE-generated candidate trajectories by social cues (keep away from pedestrian groups, slow when people approach) alongside traversability analysis for long-range outdoor navigation.
paper_type: method
fm_used: 'Yes'
fm_class: [VLM]
fm_models: [Gemini (version not reported)]
fm_size: Not reported
method_family: [CVAE trajectory generation, semantic segmentation, VLM trajectory ranking with visual prompting, GPS/QGIS routing]
roles: [F1, F4, F5]
roles_evidence: {F1: VLM reads social cues from overlaid images (p.4)., F4: 'Prompt encodes social rules: keep away from pedestrian groups; slow/stop when people approach (p.5).', F5: VLM outputs a ranking of numbered candidate trajectories and a speed mode.}
integration: I3
integration_rationale: VLM ranks geometric candidates; the selected trajectory is executed by the motion planner.
evidence: E1
evidence_rationale: Quantitative evaluation offline on the GND dataset (traversability, distance-to-target, Table 1); real-world on-road runs claimed but no real-world metrics or social metrics reported (p.1).
inputs: [RGB with overlaid numbered trajectories, LiDAR, GPS, velocity]
outputs: [trajectory ranking, speed mode (normal/slow/stop), reasoning text]
human_repr: [visual (VLM reads pedestrians and groups in image)]
capabilities: {C1: 'No', C2: 'No', C3: 'No', C4: 'No', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: Partial, C10: 'No', C11: Partial, C12: Partial, C13: 'No', C14: 'No', C15: Partial, C16: 'No', C17: 'No', C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: 'No', C24: Partial, C25: 'No'}
exp:
  datasets: ['GND (Global Navigation Dataset, 10 campuses)']
  simulators: []
  robots: [Not reported in text read (real-world on-road runs claimed)]
  environment: outdoor campuses
  indoor_outdoor: outdoor
  sensors: [RGB, 3D LiDAR, GPS]
  humans: pedestrians in dataset images
  n_scenes: GND scenarios (count not reported)
  n_trajectories: Not reported
  n_participants: NA
  split: NA
  baselines: [MTG, DTG, VL-TGS, NoMaD, ViNT, PIVOT]
  ablation: 'No'
  real_robot_trials: Partial (claimed in text; no metrics reported)
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [narrow space, off-road terrain, crosswalks, social scenarios with pedestrians]
metrics: [OTHER | Traversability | % | fully traversable waypoints over trajectory (GND map) | p.1, NAV | Distance to Target | % | 1 - (d_tau - d_o)/|tau| | p.7, 'DEPLOY | Inference time | s | 2.30 s per query (MOSU), RTX 3060 | p.8']
deployment: {fm_model: Gemini, model_size: Not reported, api_cloud_local: Cloud API (implied), onboard_offboard: Not reported, gpu: RTX 3060 (6.4 GB), cpu: Intel i9, latency: 2.30 s per trajectory-generation cycle, query_frequency: Not reported, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Not reported, caching: Not reported, event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: Not reported, safety_shield: LiDAR geometric confidence in candidate generation (not an independent shield), emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: Partial (selection among geometric candidates), real_time_claim_supported: 'No'}
repro: {code: Not reported, code_url: Not reported, dataset: Not reported, dataset_url: Not reported, checkpoints: Not reported, prompts_published: Not reported, hardware_specified: Not reported, hyperparameters: Not reported, protocol_described: Not reported, project_page: Not reported, concerns: Social behaviour only shown qualitatively; real-world results not quantified.}
limitations_flags: [latency, cloud-dependence, no-human-study, limited-scenarios]
web_verification_required: [ISER 2025 proceedings (Springer SPAR) publication and DOI.]
cited_missing: [GND dataset (ICRA 2025), MTG, DTG]
external_verification: {verified_on: '2026-10-19', status_class: 'B: accepted/presented per citing paper; proceedings not indexed', source: 'Citation in Fang et al. RA-L 2026 ref [11]; no Crossref record', arxiv_id: 2507.04686v1}
stage2: {added: true, download_source: 'https://arxiv.org/pdf/2507.04686v1', source_type: arXiv, inclusion_reason: 'Direct VLM social trajectory ranking; cited by corpus paper (Etiquette); before Cai cut-off, not cited by Cai.'}
coding: {latency_reported: 'Yes', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: Partial, code_released: 'No', new_dataset_released: NA, real_robot: Demo, human_subject_study: 'No'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A6]
  C_capabilities: {SAF1: 'No', SAF2: 'No', SPA1: 'No', SPA2: Partial, SPA3: Partial, SPA4: 'No', HUM1: 'No', HUM2: 'No', NOR1: Partial, NOR2: 'No', NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: [R1, R3]
  D_interface: [D2, D3]
  E_evidence_profile: {EV1_offline: 'Yes', EV2_closed_loop_sim: 'No', EV3_physical_robot: demo, EV4_real_humans_in_trials: none, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: Not reported, statistical_testing: 'No', cross_environment: No/unclear, runtime_measured: 'Yes'}
  cross_cutting: {temporal_coupling: per-decision, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'No', uncertainty: 'No', hallucination_mitigation: Partial, privacy_constraint: 'No', inference_location: cloud API}
physical_source_folder: "05_Direct_VLM_SocialNav_Preprints"
analytical_category: "S5"
coding:
  latency_reported: "Yes"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "Partial"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "Demo"
  human_subject_study: "No"
---

# MOSU (Liang et al., ISER 2025 per citation)

Page convention: PDF index of the corpus copy (arXiv v1).

## A. Bibliographic
arXiv:2507.04686v1. Cited as ISER 2025 by Fang et al. (RA-L 2026, in corpus); no DOI or proceedings record found as of 2026-10-19 -> status B (accepted per citing paper, not yet indexed). University of Maryland / George Mason University.

## B. Position
S5. VLM as **social trajectory ranker** (I3) within a long-range outdoor system; social contribution explicit in method but weakly evaluated.

## C-D. Problem and method
Long-range outdoor navigation must respect traversability, social norms and traffic rules. CVAE candidates + segmentation-based traversability + Gemini ranking of numbered trajectories with speed mode.

## G. Social capabilities
C9, C11, C12, C15, C24 Partial (prompted rules; qualitative examples only) · others No.

## H/I. I3; E1.

## L. Results
GND: traversability 77% vs PIVOT 70%, VL-TGS 65%; distance-to-target 73% vs 70% (VL-TGS); inference 2.30 s (Table 1).

## N. Limitations
Stated: small cliffs, out-of-distribution trajectory noise. Observable: no social metric; real-world evaluation not quantified.

## Stage-7 status re-check (2026-10-19)
ISER 2025 held 6-10 Jul 2025 (Santa Fe); no proceedings volume or Crossref record found; arXiv single version without venue comment. Evidence remains the independent citation in Fang et al. RA-L 2026. Status unchanged (class B, third-party evidence). See 09_Project_Reports/PUBLICATION_STATUS_FINAL_CHECK.md.

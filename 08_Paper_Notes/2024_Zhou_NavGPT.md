---
id: 2024_Zhou_NavGPT
source_pdfs: [03_Adjacent_Foundation_Model_Navigation/14075-AAAI24.ZhouG.pdf]
duplicate_copies: []
related_versions: []
title: 'NavGPT: Explicit Reasoning in Vision-and-Language Navigation with Large Language Models'
authors: &id001 [Gengze Zhou, Yicong Hong, Qi Wu]
year: 2024
venue: Proceedings of the AAAI Conference on Artificial Intelligence (AAAI-24)
volume: '38'
issue: '7'
pages: 7641-7649
doi: 10.1609/aaai.v38i7.28597
url: https://doi.org/10.1609/aaai.v38i7.28597
pub_status: conference
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1609/aaai.v38i7.28597); arXiv abs page (2305.16986v3). PDF-derived basis (Stage 1): AAAI-24 header, copyright notice and proceedings page numbers (p.1).'
category: S3
folder: 03_Adjacent_Foundation_Model_Navigation
folder_category_match: 'Yes'
category_rationale: LLM-based zero-shot vision-and-language navigation in static Matterport3D scenes; no humans or social behaviour.
paper_type: method
fm_used: 'Yes'
fm_class: [LLM, VLM]
fm_models: [GPT-4, GPT-3.5 (summaries; ablations), BLIP-2 ViT-G FlanT5-XL (captioning), 'Fast-RCNN (detector, not FM)']
fm_size: Not reported
method_family: [zero-shot prompting, ReAct-style reasoning + acting, visual-to-language translation via VFMs]
roles: [F1, F7, F9]
roles_evidence: {F1: BLIP-2 captions 24 views per viewpoint; GPT-3.5 summarises per direction; detections + depth turned into text (p.3-4)., F7: 'GPT-4 decomposes instructions into sub-goals, tracks progress, adjusts plans (Fig.3, p.5-6).', F9: 'LLM selects the next navigable viewpoint ID on the navigation graph (action_maker) (p.3, Fig.3).'}
integration: I5
integration_rationale: LLM directly selects the next waypoint (viewpoint) on a pre-defined graph; no low-level control.
evidence: E2
evidence_rationale: Closed-loop zero-shot navigation in Matterport3D simulator on R2R val-unseen (783 trajectories); no physical robot.
inputs: [text descriptions of 8-direction views (from BLIP-2), object classes/relative heading/depth within 3 m, instruction, summarised history]
outputs: [reasoning trace, next viewpoint ID]
human_repr: [none]
capabilities: {C1: NA, C2: NA, C3: NA, C4: NA, C5: NA, C6: NA, C7: NA, C8: NA, C9: NA, C10: NA, C11: NA, C12: NA, C13: NA, C14: NA, C15: NA, C16: NA, C17: NA, C18: NA, C19: NA, C20: NA, C21: NA, C22: NA, C23: NA, C24: NA, C25: NA}
exp:
  datasets: ['R2R (val unseen: 11 scenes, 783 trajectories)', 'ablation split: 216 instructions from 72 scenes (train + val unseen)']
  simulators: [Matterport3D simulator]
  robots: []
  environment: indoor houses (Matterport3D)
  indoor_outdoor: indoor
  sensors: [simulated RGB panorama, simulator depth]
  humans: none
  n_scenes: 11 (val unseen); 72 (ablation)
  n_trajectories: 783 (x3 instructions) val unseen; 216 instructions ablation
  n_participants: NA
  split: R2R val unseen
  baselines: [Seq2Seq, Speaker-Follower, EnvDrop, PREVALENT, VLN-BERT, HAMT, DuET, 'DuET (init. LXMERT, no training)']
  ablation: Yes (view granularity, object info, depth)
  real_robot_trials: 'No'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: []
metrics: [NAV | Trajectory Length (TL) | m | average distance travelled | p.5, NAV | Navigation Error (NE) | m | mean distance from final location to goal | p.5, NAV | Success Rate (SR) | % | within 3 m of goal | p.5, NAV | Oracle Success Rate (OSR) | % | success at closest point on trajectory | p.5, NAV | SPL | % | success weighted by path length | p.5]
deployment: {fm_model: GPT-4 / GPT-3.5 (API), model_size: Not reported, api_cloud_local: Cloud API, onboard_offboard: NA, gpu: Not reported, cpu: Not reported, latency: Not reported, query_frequency: per navigation step, planner_frequency: NA, controller_frequency: NA, asynchronous: NA, caching: NA, event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: NA, safety_shield: NA, emergency_behavior: NA, uncertainty: NA, hallucination_mitigation: 'Prompt rule: do not fabricate nonexistent viewpoint IDs (p.3)', real_time_claim_supported: NA}
repro: {code: 'Yes', code_url: 'https://github.com/GengzeZhou/NavGPT', dataset: R2R (public), dataset_url: NA, checkpoints: NA, prompts_published: Yes (appendix referenced; not in corpus PDF), hardware_specified: 'No', hyperparameters: NA, protocol_described: 'Yes', project_page: NA, concerns: Closed API models; appendix not included in corpus PDF.}
limitations_flags: [cloud-dependence, spatial-reasoning-failure]
web_verification_required: []
cited_missing: [LGX (Dorbala 2023 LLM zero-shot ObjectNav), CLIP-Nav, ESC (zero-shot ObjectNav with commonsense), ReAct, DuET, HAMT]
adjacent: {mechanism: 'LLM as zero-shot sequential decision maker over text-translated observations, with explicit reasoning traces and summarised history.', relevance: Template for LLM-in-the-loop navigation with explainable reasoning (F7/F9) and for the 'vision-to-language bottleneck' later inherited by text-based social reasoning pipelines., why_not_direct: 'No humans, no social behaviour, static scenes.', inherited_by: 'Cited by corpus HA-VLN (2024), HA-VLN 2.0, HCSG; also by Pan foundation-language-models navigation review (00).'}
coding: {latency_reported: 'No', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: Partial, code_released: 'Yes', new_dataset_released: NA, real_robot: 'No', human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2024
  authors: *id001
  venue: The Thirty-Eighth AAAI Conference on Artificial Intelligence (AAAI-24)
  volume: Not reported
  issue: Not reported
  pages: 7641-7649
  doi: Not reported
  url: https://github.com/GengzeZhou/NavGPT
  pub_status: conference
  peer_reviewed: 'Yes'
  peer_review_basis: AAAI-24 header, copyright notice and proceedings page numbers (p.1).
project_url: https://github.com/GengzeZhou/NavGPT
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: Proceedings of the AAAI Conference on Artificial Intelligence (AAAI-24)
  verified_doi: 10.1609/aaai.v38i7.28597
  verified_url: https://doi.org/10.1609/aaai.v38i7.28597
  verified_pages: 7641-7649
  arxiv: 2305.16986v3
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1609/aaai.v38i7.28597)', arXiv abs page (2305.16986v3)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A0]
  C_capabilities: {SAF1: NA, SAF2: NA, SPA1: NA, SPA2: NA, SPA3: NA, SPA4: NA, HUM1: NA, HUM2: NA, NOR1: NA, NOR2: NA, NOR3: NA, NOR4: NA, EXP1: NA, EXP2: NA, EXP3: NA}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: none, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "03_Adjacent_Foundation_Model_Navigation"
analytical_category: "S3"
coding:
  latency_reported: "No"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "Partial"
  code_released: "Yes"
  new_dataset_released: "NA"
  real_robot: "No"
  human_subject_study: "No"
---

# NavGPT (Zhou, Hong, Wu — AAAI 2024)

Page convention: PDF index (p.N).

## A. Bibliographic — AAAI-24, pp.7641–7649. Adelaide / ANU. Code public.

## B. Position — S3 adjacent: LLM reasoning for VLN.

## C. Research problem — can LLMs understand interactive world, actions and consequences in text and solve navigation? (p.2). Contributions: LLM VLN agent with history/prompt management; analysis of LLM navigational reasoning; explainable high-level planning (p.2).

## D. Method — Eq.1: ⟨R_{t+1}, A_{t+1}⟩ = LLM(M(P), M(W), M(F(O_t)), M(H_{<t+1})) (p.3). 24 views (8 headings × 3 elevations, FoV 45°) captioned by BLIP-2, summarised by GPT-3.5; Fast-RCNN objects within 3 m with heading and depth; ReAct reasoning + action; history summariser (p.3–5).

## L. Quantitative results
- Table 1 (R2R val unseen; TL / NE / OSR / SR / SPL; visually verified p.7): NavGPT 11.45 / 6.46 / 42 / 34 / 29; DuET (init. LXMERT, no train) 22.03 / 9.74 / 7 / 1 / 0; Seq2Seq 8.39 / 7.81 / 28 / 21 / –; Speaker-Follower – / 6.62 / 45 / 35 / –; EnvDrop 10.70 / 5.22 / – / 52 / 48; PREVALENT 10.19 / 4.71 / – / 58 / 53; VLN-BERT 12.01 / 3.93 / 69 / 63 / 57; HAMT 11.46 / 2.29 / 73 / 66 / 61; DuET 13.94 / 3.31 / 81 / 72 / 60.
- Table 2 (granularity, GPT-3.5, 216 samples): FoV@45 SR 16.67 / SPL 13.00 vs FoV@60 10.19 / 6.52 and FoV@30 13.89 / 9.12.
- Table 3: baseline SR 11.11 → +Obj 15.97 → +Obj+Dis 16.67; SPL 6.92 → 11.71 → 13.00.
- Authors: zero-shot performance still below trained models; bottleneck is information loss in vision-to-language translation and history summarisation (p.6).

## N. Limitations
1. **Stated (p.6–7):** caption quality and object-tracking limits; summariser loses information.
2. **Future:** multimodal LLMs; use LLM reasoning to benefit learned models.
3. **Observable:** discrete graph navigation only; cloud LLM; no latency reported; which LLM produced Table 1 not stated explicitly.
4. **Social relevance:** none directly.

## P. Adjacent analysis — see `adjacent:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue Proceedings of the AAAI Conference on Artificial Intelligence (AAAI-24); DOI 10.1609/aaai.v38i7.28597; pages 7641-7649; URL https://doi.org/10.1609/aaai.v38i7.28597.
- Sources: Crossref (exact title match, DOI 10.1609/aaai.v38i7.28597); arXiv abs page (2305.16986v3).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - venue: PDF-derived 'The Thirty-Eighth AAAI Conference on Artificial Intelligence (AAAI-24)' -> externally verified 'Proceedings of the AAAI Conference on Artificial Intelligence (AAAI-24)'
- Changed field - volume: PDF-derived 'Not reported' -> externally verified '38'
- Changed field - issue: PDF-derived 'Not reported' -> externally verified '7'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified '10.1609/aaai.v38i7.28597'
- Changed field - url: PDF-derived 'https://github.com/GengzeZhou/NavGPT' -> externally verified 'https://doi.org/10.1609/aaai.v38i7.28597'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

---
id: 2026_Park_TACET
source_pdfs: [05_Direct_VLM_SocialNav_Preprints/TACET_arXiv2610.03828v1.pdf]
duplicate_copies: []
related_versions: ['arXiv:2610.03828v1 = corpus copy']
title: 'TACET: Context-Appropriate Acoustic-Social Navigation for Quadrupeds'
authors: [Sungsan Park, Young-Sik Shin, Sanghyun Kim]
year: 2026
venue: arXiv preprint (arXiv:2610.03828v1)
volume: NA
issue: NA
pages: NA
doi: Not found / not applicable
url: https://arxiv.org/abs/2610.03828
pub_status: preprint
peer_reviewed: 'No'
peer_review_basis: 'arXiv 2610.03828v1 only (posted 2026-10-02, latest version 2026-10-02); arXiv comment: 8 pages. No verified peer-reviewed version found as of corpus freeze date (2026-10-19) via Crossref title search.'
category: S5
folder: 05_Direct_VLM_SocialNav_Preprints
folder_category_match: 'Yes'
category_rationale: Fine-tuned VLM (Qwen2.5-VL-7B, QLoRA, labels from Gemini 2.5 Flash) infers context-appropriate behaviour tokens (gait, speed, social cost) for a quadruped, driving a social costmap and a quiet-locomotion RL policy; adds an acoustic social dimension (noise near people).
paper_type: method
fm_used: 'Yes'
fm_class: [VLM]
fm_models: [Qwen2.5-VL-7B (QLoRA), Gemini 2.5 Flash (label generation)]
fm_size: 7B
method_family: [VLM fine-tuning (QLoRA), behaviour token, social costmap, PPO quiet-locomotion policy]
roles: [F1, F4, F6, F11]
roles_evidence: {F1: 'VLM reads context (library, hospital, people resting).', F4: 'Infers context-appropriate conduct (quiet, slow).', F6: Social-cost token shapes costmap; speed/gait parameters., F11: Gemini used as label generator.}
integration: I4
integration_rationale: Behaviour token sets costmap and locomotion-policy parameters.
evidence: E4
evidence_rationale: Real Unitree Go2 trials (10 per condition) plus blinded video study with N=15 raters of robot behaviour appropriateness.
inputs: [RGB]
outputs: ['behaviour token <gait, speed, social_cost>']
human_repr: [implicit in VLM context]
capabilities: {C1: 'Yes', C2: 'No', C3: Partial, C4: Partial, C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: 'Yes', C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: 'No', C18: 'No', C19: 'No', C20: 'No', C21: Partial, C22: 'No', C23: 'No', C24: 'Yes', C25: 'No'}
exp:
  datasets: Not reported
  simulators: Not reported
  robots: [Unitree Go2]
  environment: Not reported
  indoor_outdoor: indoor
  sensors: Not reported
  humans: real people; 15 video raters
  n_scenes: Not reported
  n_trajectories: 10 trials per condition
  n_participants: '15'
  split: Not reported
  baselines: [context-agnostic navigation, VLM without fine-tuning]
  ablation: 'Yes'
  real_robot_trials: 'Yes'
  human_study: Yes (blinded video ratings)
  statistical_testing: Not reported
  scenarios: Not reported
metrics: [SOCIAL | Personal-space compliance (PSC) | % | 100% for TACET | p.6, OTHER | Acoustic noise | dBA | up to 9.3 dBA reduction | p.1, HUMAN | Appropriateness ratings | Likert | blinded video study N=15 | p.7]
deployment: {fm_model: Qwen2.5-VL-7B, model_size: 7B, api_cloud_local: Local, onboard_offboard: Local desktop GPU (Sec. IV-A); on-robot execution not reported, gpu: RTX A6000, cpu: Not reported, latency: '2.6 s median reasoner query, 95th percentile 3.5 s (p3)', query_frequency: 'about 0.25 Hz, tokens cached between queries (p3)', planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: 'Yes (high-rate controller never blocked by VLM latency, p3)', caching: 'Yes (tokens cached between queries, p3)', event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: Not reported, safety_shield: Costmap-based planner, emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: Partial (structured token output), real_time_claim_supported: Not reported}
repro: {code: Not reported, code_url: Not reported, dataset: Not reported, dataset_url: Not reported, checkpoints: Not reported, prompts_published: Not reported, hardware_specified: Not reported, hyperparameters: Not reported, protocol_described: Not reported, project_page: Not reported, concerns: Not reported}
limitations_flags: [limited-scenarios, resource-requirements]
web_verification_required: []
cited_missing: []
external_verification: {verified_on: '2026-10-19', status_class: 'C: preprint only', source: arXiv abs page + Crossref title search (no match), arxiv_id: 2610.03828v1, publication_status: Preprint, peer_reviewed_note: No verified peer-reviewed version found as of corpus freeze date}
stage2: {added: true, download_source: 'https://arxiv.org/pdf/2610.03828v1', source_type: arXiv, inclusion_reason: 'Direct: VLM context-appropriate social/acoustic quadruped navigation with human ratings; after Cai cut-off.', relative_to_cai_cutoff: after Cai cut-off (27 Jun 2026), taxonomy_review_required: Acoustic social appropriateness not represented in C1-C25.}
coding: {latency_reported: 'Yes', safety_mechanism: 'Yes', uncertainty_treatment: 'No', hallucination_treatment: Partial, code_released: 'No', new_dataset_released: 'No', real_robot: Systematic, human_subject_study: 'Yes'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A6]
  C_capabilities: {SAF1: 'Yes', SAF2: 'No', SPA1: 'Yes', SPA2: 'No', SPA3: 'No', SPA4: 'No', HUM1: 'No', HUM2: 'No', NOR1: 'Yes', NOR2: 'No', NOR3: 'Yes', NOR4: 'No', EXP1: Partial, EXP2: 'No', EXP3: 'No'}
  B_roles: [R1, R3]
  D_interface: [D3, D7]
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'No', EV3_physical_robot: systematic, EV4_real_humans_in_trials: staged, EV5_human_evaluation: observers/video, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: 10 trials per condition, statistical_testing: Not reported, cross_environment: No/unclear, runtime_measured: 'Yes'}
  cross_cutting: {temporal_coupling: asynchronous, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'Yes', uncertainty: 'No', hallucination_mitigation: Partial, privacy_constraint: 'No', inference_location: local/onboard or local server}
physical_source_folder: "05_Direct_VLM_SocialNav_Preprints"
analytical_category: "S5"
coding:
  latency_reported: "Yes"
  safety_mechanism: "Yes"
  uncertainty_treatment: "No"
  hallucination_treatment: "Partial"
  code_released: "No"
  new_dataset_released: "No"
  real_robot: "Systematic"
  human_subject_study: "Yes"
---

# TACET (Park, Shin, Kim; arXiv 2026)

## A. Bibliographic
arXiv:2610.03828v1 (2 Oct 2026). Publication status: Preprint; Peer reviewed: No verified peer-reviewed version found as of corpus freeze date. After Cai cut-off.

## B. Position
S5. **TAXONOMY_REVIEW_REQUIRED**: introduces an *acoustic* social dimension (noise appropriate to context) not represented in C1-C25 (closest C11 etiquette, C24 context-dependence). No new class created.

## G. Capabilities
C1 Yes · C11 Yes · C24 Yes · C3, C4, C21 Partial · others No.

## H/I. I4; E4 (blinded video raters).

## L. Results
PSC 100%; noise reduced by up to 9.3 dBA; 10 trials per condition.

## N. Limitations
Observable: video-based rating (N = 15) rather than co-present participants; latency quantified only for the reasoner query (2.6 s median); end-to-end latency on the robot not reported. [Corrected 2026-10-27 after the claim-citation integrity audit.]

---
id: 2026_Sethuraman_Context-Aware-Preferences
source_pdfs: [05_Direct_VLM_SocialNav_Preprints/Context-Aware-Preferences-MORL_arXiv2603.17510v2.pdf]
duplicate_copies: []
related_versions: ['arXiv:2603.17510v2 = corpus copy']
title: Interpreting Context-Aware Human Preferences for Multi-Objective Robot Navigation
authors: [Tharun Sethuraman, Subham Agrawal, Nils Dengler, Jorge de Heuvel, Teena Hassan, Maren Bennewitz]
year: 2026
venue: arXiv preprint (arXiv:2603.17510v2)
volume: NA
issue: NA
pages: NA
doi: Not found / not applicable
url: https://arxiv.org/abs/2603.17510
pub_status: preprint
peer_reviewed: 'No'
peer_review_basis: 'arXiv 2603.17510v2 only (posted 2026-03-18, latest version 2026-05-12); arXiv comment: none. No verified peer-reviewed version found as of corpus freeze date (2026-10-19) via Crossref title search.'
category: S5
folder: 05_Direct_VLM_SocialNav_Preprints
folder_category_match: 'Yes'
category_rationale: VLM predicts context (office/home/supermarket, people present) and LLMs translate user rules into preference weights for a multi-objective RL navigation policy (incl. distance-to-humans objectives); robot experiments and a user study rating rules/explanations.
paper_type: method
fm_used: 'Yes'
fm_class: [VLM, LLM]
fm_models: [Gemini 2.0 Flash (context predictor), 'Mistral-Large-2.1 / GPT-4o (rule updater, preference translator)']
fm_size: Not reported (API)
method_family: [multi-objective RL (preference-conditioned policy), LLM preference translation, VLM context prediction]
roles: [F1, F4, F6]
roles_evidence: {F1: VLM predicts environment context from images., F4: LLM updates context-dependent behaviour rules from user feedback., F6: Preference translator outputs objective weights for MORL.}
integration: I4
integration_rationale: FM outputs preference weights conditioning a pre-trained MORL policy.
evidence: E3
evidence_rationale: Real robot experiments in office, home and supermarket settings; user study N=24 rated rules/explanations (not robot behaviour) -> not E4.
inputs: [RGB, user language rules]
outputs: [context label, preference weights]
human_repr: [distance-to-human objective in MORL]
capabilities: {C1: 'No', C2: 'No', C3: Partial, C4: 'No', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: 'No', C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: 'No', C18: 'No', C19: 'No', C20: 'No', C21: Partial, C22: 'No', C23: 'Yes', C24: 'Yes', C25: 'No'}
exp:
  datasets: Not reported
  simulators: Not reported
  robots: [real mobile robot (office/home/supermarket)]
  environment: Not reported
  indoor_outdoor: indoor
  sensors: Not reported
  humans: real people in environment; 24 study participants
  n_scenes: Not reported
  n_trajectories: Not reported
  n_participants: '24'
  split: Not reported
  baselines: [fixed preferences]
  ablation: Yes (LLM choice)
  real_robot_trials: 'Yes'
  human_study: Text-raters/other (rules and explanations rated)
  statistical_testing: Not reported
  scenarios: Not reported
metrics: [DEPLOY | Module latency | s | context predictor 9.59+-3.12 s; rule updater 5.94+-0.94 s; preference translation 3.34+-0.89 s | p.16, HUMAN | Rule/explanation ratings | Likert | N=24 (within-subjects) | p.13]
deployment: {fm_model: Gemini 2.0 Flash + Mistral-Large / GPT-4o, model_size: Not reported, api_cloud_local: Cloud API, onboard_offboard: Not reported, gpu: Not reported, cpu: Not reported, latency: 'context 9.59 s, rule update 5.94 s, translation 3.34 s (asynchronous)', query_frequency: Not reported, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: 'Yes', caching: Not reported, event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: MORL policy with last weights, safety_shield: Not reported, emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: Partial (rules confirmed by user), real_time_claim_supported: Not reported}
repro: {code: Yes (GitHub), code_url: Not reported, dataset: Not reported, dataset_url: Not reported, checkpoints: Not reported, prompts_published: Not reported, hardware_specified: Not reported, hyperparameters: Not reported, protocol_described: Not reported, project_page: Not reported, concerns: Not reported}
limitations_flags: [cloud-dependence, latency]
web_verification_required: []
cited_missing: [de Heuvel et al. (preference navigation)]
external_verification: {verified_on: '2026-10-19', status_class: 'C: preprint only', source: arXiv abs page + Crossref title search (no match), arxiv_id: 2603.17510v2, publication_status: Preprint, peer_reviewed_note: No verified peer-reviewed version found as of corpus freeze date}
stage2: {added: true, download_source: 'https://arxiv.org/pdf/2603.17510v2', source_type: arXiv, inclusion_reason: 'Direct: VLM/LLM context-dependent social preferences for navigation; before Cai cut-off, not cited by Cai.', relative_to_cai_cutoff: before Cai cut-off (27 Jun 2026); not cited by Cai}
coding: {latency_reported: 'Yes', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: Partial, code_released: 'Yes', new_dataset_released: NA, real_robot: Systematic, human_subject_study: Text-raters/other}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1]
  C_capabilities: {SAF1: 'No', SAF2: 'No', SPA1: Partial, SPA2: 'No', SPA3: 'No', SPA4: 'No', HUM1: 'No', HUM2: 'No', NOR1: 'No', NOR2: 'Yes', NOR3: 'Yes', NOR4: 'No', EXP1: Partial, EXP2: 'No', EXP3: 'No'}
  B_roles: [R1, R4]
  D_interface: [D3]
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'No', EV3_physical_robot: systematic, EV4_real_humans_in_trials: present-type-unreported, EV5_human_evaluation: text-raters, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: Not reported, statistical_testing: Not reported, cross_environment: No/unclear, runtime_measured: 'Yes'}
  cross_cutting: {temporal_coupling: asynchronous, memory: persistent rule memory updated from user feedback, continual_adaptation: rule updating from user feedback, explanation_output: 'No', safety_guard: 'No', uncertainty: 'No', hallucination_mitigation: Partial, privacy_constraint: 'No', inference_location: cloud API}
physical_source_folder: "05_Direct_VLM_SocialNav_Preprints"
analytical_category: "S5"
coding:
  latency_reported: "Yes"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "Partial"
  code_released: "Yes"
  new_dataset_released: "NA"
  real_robot: "Systematic"
  human_subject_study: "Text-raters/other"
---

# Context-aware human preferences for MORL navigation (Sethuraman et al., arXiv 2026)

## A. Bibliographic
arXiv:2603.17510v2 (Mar-May 2026). University of Bonn (Bennewitz group). Publication status: Preprint; Peer reviewed: No verified peer-reviewed version found as of corpus freeze date.

## B. Position
S5. FMs translate context and user rules into **preference weights** for a multi-objective policy (I4).

## G. Capabilities
C23, C24 Yes · C3, C21 Partial · others No.

## H/I. I4; E3 (user study rated text, not robot behaviour).

## N. Limitations
Observable: human evaluation does not concern robot motion; cloud FMs with 3-10 s module latencies (asynchronous).

---
id: 2026_Fang_Group-Joining
source_pdfs: [05_Direct_VLM_SocialNav_Preprints/Robot-Group-Joining-Language-Guided_arXiv2609.28467v1.pdf]
duplicate_copies: []
related_versions: ['arXiv:2609.28467v1 = corpus copy']
title: Where Should I Join? Robot Group Joining via Language-Guided Goal Prediction
authors: [Zilin Fang, Zishuo Wang, Gim Hee Lee, David Hsu]
year: 2026
venue: arXiv preprint (arXiv:2609.28467v1)
volume: NA
issue: NA
pages: NA
doi: Not found / not applicable
url: https://arxiv.org/abs/2609.28467
pub_status: preprint
peer_reviewed: 'No'
peer_review_basis: 'arXiv 2609.28467v1 only (posted 2026-09-23, latest version 2026-09-23); arXiv comment: none. No verified peer-reviewed version found as of corpus freeze date (2026-10-19) via Crossref title search.'
category: S5
folder: 05_Direct_VLM_SocialNav_Preprints
folder_category_match: 'Yes'
category_rationale: 'Language-guided group joining: a fine-tuned SigLIP2 grounding model identifies the referred group from language and an F-formation-aware goal predictor chooses the joining position; offline benchmark and real-robot trials vs NaVILA/OmniVLA.'
paper_type: method + benchmark
fm_used: 'Yes'
fm_class: [vision-language model (contrastive)]
fm_models: [SigLIP2 (fine-tuned grounding)]
fm_size: Not reported (SigLIP2 family)
method_family: [vision-language grounding, F-formation goal prediction]
roles: [F1, F3, F9]
roles_evidence: {F1: Grounds the language-referred group., F3: Group/F-formation reasoning for joining., F9: Outputs joining goal position.}
integration: I5
integration_rationale: Predicted joining goal (waypoint) passed to the local planner.
evidence: E3
evidence_rationale: '42-scenario offline benchmark (JRDB/SCAND) plus real robot: 4 scenarios x 5 trials (5/5, 5/5, 4/5, 4/5) with NaVILA and OmniVLA baselines failing.'
inputs: [RGB, language instruction]
outputs: [group grounding, joining goal]
human_repr: [person detections grouped into F-formations]
capabilities: {C1: 'No', C2: 'No', C3: Partial, C4: 'No', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: 'Yes', C10: 'Yes', C11: 'No', C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'Yes', C17: 'No', C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: 'Yes', C24: 'No', C25: 'No'}
exp:
  datasets: [42-scenario benchmark from JRDB and SCAND]
  simulators: Not reported
  robots: [Boston Dynamics Spot (onboard Jetson Orin)]
  environment: Not reported
  indoor_outdoor: both
  sensors: Not reported
  humans: real groups
  n_scenes: 42 offline; 4 real
  n_trajectories: 5 per real scenario
  n_participants: Not reported
  split: Not reported
  baselines: [NaVILA, OmniVLA]
  ablation: 'Yes'
  real_robot_trials: 'Yes'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: Not reported
metrics: [NAV | Success rate (SR) | count/5 | final pose satisfying interaction-specific validity criteria | p.6, SOCIAL | Personal-space violation duration (PSV) | s | time within 0.25 m of any person | p.6, DEPLOY | Grounding inference time | s | 0.936 s (agreement-weighted F1 0.8125) | p.6]
deployment: {fm_model: SigLIP2 (fine-tuned), model_size: Not reported, api_cloud_local: Local, onboard_offboard: Onboard, gpu: NVIDIA Jetson Orin (onboard Spot), cpu: Not reported, latency: 0.936 s grounding, query_frequency: Not reported, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: 'Yes (full inference <0.7 s runs continuously and asynchronously with DWA control, p6; corrected 2026-10-27)', caching: Not reported, event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: Not reported, safety_shield: Local planner, emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: NA (contrastive grounding), real_time_claim_supported: Not reported}
repro: {code: Not reported, code_url: Not reported, dataset: Not reported, dataset_url: Not reported, checkpoints: Not reported, prompts_published: Not reported, hardware_specified: Not reported, hyperparameters: Not reported, protocol_described: Not reported, project_page: Not reported, concerns: Not reported}
limitations_flags: [limited-scenarios, no-human-study]
web_verification_required: []
cited_missing: [Fang et al. Etiquette (in corpus)]
external_verification: {verified_on: '2026-10-19', status_class: 'C: preprint only', source: arXiv abs page + Crossref title search (no match), arxiv_id: 2609.28467v1, publication_status: Preprint, peer_reviewed_note: No verified peer-reviewed version found as of corpus freeze date}
stage2: {added: true, download_source: 'https://arxiv.org/pdf/2609.28467v1', source_type: arXiv, inclusion_reason: 'Direct: language-guided group joining (F-formation); after Cai cut-off.', relative_to_cai_cutoff: after Cai cut-off (27 Jun 2026)}
coding: {latency_reported: 'Yes', safety_mechanism: 'Yes', uncertainty_treatment: 'No', hallucination_treatment: NA, code_released: 'No', new_dataset_released: 'No', real_robot: Systematic, human_subject_study: 'No'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A3, A4]
  C_capabilities: {SAF1: 'No', SAF2: 'No', SPA1: 'Yes', SPA2: 'Yes', SPA3: 'Yes', SPA4: 'No', HUM1: 'No', HUM2: 'No', NOR1: 'No', NOR2: 'Yes', NOR3: 'No', NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: [R2, R4]
  D_interface: [D4]
  E_evidence_profile: {EV1_offline: 'Yes', EV2_closed_loop_sim: 'No', EV3_physical_robot: systematic, EV4_real_humans_in_trials: present-type-unreported, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: 5 per real scenario, statistical_testing: 'No', cross_environment: 'Yes', runtime_measured: 'Yes'}
  cross_cutting: {temporal_coupling: asynchronous, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'Yes', uncertainty: 'No', hallucination_mitigation: NA, privacy_constraint: 'No', inference_location: local/onboard or local server}
physical_source_folder: "05_Direct_VLM_SocialNav_Preprints"
analytical_category: "S5"
coding:
  latency_reported: "Yes"
  safety_mechanism: "Yes"
  uncertainty_treatment: "No"
  hallucination_treatment: "NA"
  code_released: "No"
  new_dataset_released: "No"
  real_robot: "Systematic"
  human_subject_study: "No"
---

# Where Should I Join? (Fang, Wang, Lee, Hsu; arXiv 2026)

## A. Bibliographic
arXiv:2609.28467v1 (23 Sep 2026). National University of Singapore. Publication status: Preprint; Peer reviewed: No verified peer-reviewed version found as of corpus freeze date. After Cai cut-off.

## B. Position
S5. Covers **group joining / F-formation** (C9, C10) - rare in FM social navigation. FM is a contrastive vision-language model (criterion B satisfied via language grounding).

## G. Capabilities
C9, C10, C16 (queue-joining scenario), C23 Yes · C3 Partial (PSV metric).

## H/I. I5; E3.

## L. Results
Grounding F1 0.8125 in 0.936 s (Table I). Real robot (Boston Dynamics Spot): per-scenario successes 5/5, 5/5, 4/5, 4/5 (18/20); NaVILA and OmniVLA 0/5 in reported scenarios.

## N. Limitations
Observable: no rating by group members; small trial counts.

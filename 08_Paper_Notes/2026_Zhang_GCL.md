---
id: 2026_Zhang_GCL
source_pdfs: [05_Direct_VLM_SocialNav_Preprints/2603.11447v1.pdf]
duplicate_copies: []
related_versions: ['''GCL: Group competitive learning for socially aware robot navigation'', IEICE Tech. Rep. 125(356):55-60 (2026) cited by Cai survey [83] - likely related short version; not in corpus']
title: Enhancing Lightweight Vision Language Models through Group Competitive Learning for Socially Compliant Navigation
authors: &id001 [Xinyu Zhang, Atsushi Konno, Toshihiko Yamasaki, Ling Xiao]
year: 2026
venue: arXiv:2603.11447v1 [cs.RO], 12 Mar 2026 (LNCS-style template)
volume: NA
issue: NA
pages: '20'
doi: Not found / not applicable
url: https://arxiv.org/abs/2603.11447
pub_status: preprint
peer_reviewed: 'No'
peer_review_basis: 'Publication status: Preprint; Peer reviewed: No verified peer-reviewed version found as of corpus freeze date (2026-10-19). Sources: arXiv abs page (2603.11447v1); Crossref title search: no match.'
category: S5
folder: 05_Direct_VLM_SocialNav_Preprints
folder_category_match: 'Yes'
category_rationale: Training strategy (mutual/competitive online distillation between two small VLMs) for socially compliant navigation reports; offline evaluation on SNEI and MUSON.
paper_type: method
fm_used: 'Yes'
fm_class: [VLM]
fm_models: ['Qwen2.5-VL-3B, Qwen2.5-VL-7B, Qwen3-VL-2B, Qwen3-VL-4B, Qwen3-VL-8B']
fm_size: 2B-8B
method_family: [supervised fine-tuning, online mutual distillation (contrastive InfoNCE + Jensen-Shannon), asymmetric learning-rate/temperature optimisation]
roles: [F1, F2, F4, F8]
roles_evidence: {F1: Prompt requests Perception section (Fig.1)., F2: Prediction section., F4: Reasoning/Action/Explanation sections for socially compliant actions., F8: '''Guide'' VLM transfers knowledge to ''Learner'' VLM via GSL+DRL losses (online distillation) (Sec.3).'}
integration: I1
integration_rationale: Outputs high-level navigation intentions in text; authors state these would be executed by DWA/TEB but no integration is performed (p.8).
evidence: E1
evidence_rationale: Offline evaluation of action/perception/reasoning text similarity on SNEI and MUSON test splits; explicitly no robot experiments (p.8).
inputs: [RGB (single image), natural language system prompt]
outputs: [natural-language perception, prediction, reasoning, action, explanation]
human_repr: [semantic description (language)]
capabilities: {C1: 'No', C2: 'No', C3: 'No', C4: 'No', C5: Partial, C6: Partial, C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: Partial, C12: Partial, C13: 'No', C14: Partial, C15: 'No', C16: 'No', C17: Partial, C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: 'No', C24: Partial, C25: 'No'}
exp:
  datasets: ['SNEI: 265/60 train/test scenarios, 1,625 image-text pairs', 'MUSON: 640/160 scenarios, 4,000 pairs']
  simulators: []
  robots: []
  environment: dataset images
  indoor_outdoor: both
  sensors: [RGB]
  humans: real (images)
  n_scenes: 325 (SNEI) / 800 (MUSON subset)
  n_trajectories: NA
  n_participants: NA
  split: SNEI 265/60; MUSON 640/160 (no validation split described)
  baselines: [vanilla SFT per model, loss-component ablations]
  ablation: Yes (GSL/DRL weights, LR ratio, temperature grids)
  real_robot_trials: 'No'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [door interaction, crowded pedestrian scenes (qualitative)]
metrics: [VLM | Action-F1 | 0-1 | BERTScore-style F1 between generated and GT action text (Eq.8-9) | p.7, VLM | Perception-cos | cosine | SBERT similarity of perception text | p.7, VLM | Reasoning-cos | cosine | SBERT similarity of reasoning text | p.7]
deployment: {fm_model: Qwen2.5-VL/Qwen3-VL 2B-8B, model_size: 2B-8B, api_cloud_local: Local, onboard_offboard: NA, gpu: 8x RTX 8000 (training), cpu: NA, latency: Not reported, query_frequency: NA, planner_frequency: NA, controller_frequency: NA, asynchronous: NA, caching: NA, event_triggered: NA, distillation: Yes (online mutual), quantization: 'No', fallback_planner: NA, safety_shield: NA, emergency_behavior: NA, uncertainty: 'No', hallucination_mitigation: 'No', real_time_claim_supported: 'No (efficiency argued, not measured)'}
repro: {code: Not reported, code_url: NA, dataset: 'SNEI, MUSON (public)', dataset_url: NA, checkpoints: NA, prompts_published: Yes (system prompt Fig.1), hardware_specified: Partial (training), hyperparameters: 'Yes (lambda weights, LR, temperatures)', protocol_described: Partial, project_page: NA, concerns: 'Hyperparameter grids (temperature, LR ratio) reported on test data; no validation split; ''Qwen2.5-VL-8B'' model does not match known family sizes.'}
limitations_flags: [spatial-reasoning-failure, temporal-inconsistency, low-level-grounding]
web_verification_required: [Relation to IEICE GCL tech report; venue status.]
cited_missing: [Social reasoning-aware trajectory prediction via MLLM (Bae TPAMI 2025), ImpedanceGPT, 'Towards proactive social robots: distilling visual knowledge from VLMs (ICCV 2025)', VL2Lite, PromptKD, On-policy distillation of LMs (Agarwal ICLR 2024), SocialCounterfactuals, VisBias, Interactive navigation traversable obstacles LLM/VLM]
coding: {latency_reported: 'No', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: 'No', code_released: 'No', new_dataset_released: NA, real_robot: 'No', human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2026
  authors: *id001
  venue: arXiv:2603.11447v1 [cs.RO], 12 Mar 2026 (LNCS-style template)
  volume: NA
  issue: NA
  pages: '20'
  doi: Not reported
  url: Not reported
  pub_status: preprint
  peer_reviewed: 'No'
  peer_review_basis: arXiv v1; header 'Abbreviated paper title' placeholder indicates submission draft; no venue.
external_verification:
  verified_on: '2026-10-19'
  status_class: 'C: preprint only'
  verified_venue: arXiv:2603.11447v1 [cs.RO], 12 Mar 2026 (LNCS-style template)
  verified_doi: Not found / not applicable
  verified_url: https://arxiv.org/abs/2603.11447
  verified_pages: NA
  arxiv: 2603.11447v1
  version_relationship: arXiv only; an IEICE technical report is a related (non-archival) version
  sources: [arXiv abs page (2603.11447v1), 'Crossref title search: no match']
  peer_reviewed_note: No verified peer-reviewed version found as of corpus freeze date
  publication_status: Preprint
snei_usage: {reported_quantity: '265/60 scenarios; 1,625 image-text pairs', unit: scenarios / image-text pairs, what_it_represents: SNEI as used in GCL, page: p.7, remark: '1,625 = 325 x 5 arithmetically; the paper does not state this derivation (not assumed)', provenance_note: SNEI provenance (SCAND vs SCAND+MuSoHu) UNRESOLVED; see SNEI_DATASET_RECONCILIATION.md}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A5]
  C_capabilities: {SAF1: 'No', SAF2: 'No', SPA1: 'No', SPA2: 'No', SPA3: Partial, SPA4: Partial, HUM1: Partial, HUM2: 'No', NOR1: Partial, NOR2: 'No', NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: [R1, R2, R3]
  D_interface: [D0]
  E_evidence_profile: {EV1_offline: 'Yes', EV2_closed_loop_sim: 'No', EV3_physical_robot: none, EV4_real_humans_in_trials: none, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: NA, statistical_testing: 'No', cross_environment: 'Yes', runtime_measured: 'No'}
  cross_cutting: {temporal_coupling: offline, memory: 'No', continual_adaptation: 'No', explanation_output: 'Yes (text output, not delivered to people)', safety_guard: 'No', uncertainty: 'No', hallucination_mitigation: 'No', privacy_constraint: 'No', inference_location: n/a (offline evaluation only)}
physical_source_folder: "05_Direct_VLM_SocialNav_Preprints"
analytical_category: "S5"
coding:
  latency_reported: "No"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "No"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "No"
  human_subject_study: "No"
---

# GCL: Group Competitive Learning for Lightweight VLMs (Zhang, Konno, Yamasaki, Xiao — arXiv 2026)

Page convention: PDF index (p.N).

## A. Bibliographic — arXiv:2603.11447v1 (12 Mar 2026); Hokkaido / Tokyo. Running header "Abbreviated paper title" (template placeholder). Preprint. A related IEICE technical report ("GCL", 2026) is cited by the Cai survey.

## B. Position — S5; offline training-strategy paper.

## C. Research problem — trade-off between VLM size (reasoning) and efficiency; KD focuses on visual features and neglects reasoning consistency (p.1–2). Contributions: GCL; GCO (supervised + global semantic InfoNCE + Jensen–Shannon distribution regularisation, λ = 1.0/0.5/0.4); AGO (performance-based learning-rate roles, capacity-based temperatures τ = 2.0 large / 3.0 small) (p.2–6).

## L. Quantitative results
- SFT baselines (SNEI Action-F1): Qwen2.5-VL-3B 0.692 < Qwen3-VL-8B 0.755 < Qwen2.5-VL-7B 0.777 < Qwen3-VL-2B 0.797 < Qwen3-VL-4B 0.816 (Table 1 caption).
- Table 1 Regime A (learner/guide; GCL F1_L / F1_G): Qwen3-VL-2B/Qwen3-VL-4B 0.954/0.910; Qwen2.5-VL-3B/Qwen3-VL-4B 0.968/0.914; Qwen2.5-VL-3B/Qwen2.5-VL-7B 0.869/0.915; Qwen2.5-VL-3B/"Qwen2.5-VL-8B" 0.964/0.811; Qwen3-VL-2B/Qwen3-VL-2B 0.841/0.884; Qwen2.5-VL-3B/Qwen2.5-VL-3B 0.793/0.876. Regime B: Qwen2.5-VL-3B/Qwen3-VL-2B 0.949/0.941; Qwen2.5-VL-7B/Qwen3-VL-2B 0.907/0.862; Qwen3-VL-8B/Qwen3-VL-2B 0.884/0.945; Qwen2.5-VL-7B/Qwen3-VL-4B 0.879/0.988; Qwen3-VL-8B/Qwen3-VL-4B 0.795/0.976; Qwen3-VL-8B/Qwen2.5-VL-7B 0.799/0.955.
- Table 2 (SNEI F1 / Per-cos / Rea-cos | MUSON F1 / Per-cos / Rea-cos): SFT 3B 0.692/0.834/0.767 | 0.811/0.810/0.803; SFT 4B 0.816/0.773/0.775 | 0.863/0.855/0.849; +GSL 3B 0.818/0.880/0.846 | 0.877/0.872/0.864; 4B 0.821/0.806/0.838 | 0.905/0.879/0.874; +DRL 3B 0.832/0.903/0.851 | 0.851/0.840/0.837; 4B 0.722/0.779/0.761 | 0.887/0.869/0.879; +GSL+DRL 3B 0.908/0.947/0.917 | 0.937/0.936/0.922; 4B 0.857/0.847/0.851 | 0.943/0.949/0.950; GCO w/ AGO 3B 0.968/0.970/0.972 | 0.975/0.963/0.978; 4B 0.914/0.926/0.927 | 0.961/0.969/0.980.
- MUSON Table 3 (supplement): best learner 0.989 (Qwen3-VL-2B learner with Qwen2.5-VL-3B guide).
- Observations: "Action-F1" is a BERTScore similarity of action text (not a classification F1); "Qwen2.5-VL-8B" pairing has baseline 0.755 = Qwen3-VL-8B's value → likely a naming error; dataset sizes for SNEI (1,625 pairs) and MUSON (800 scenarios, 4,000 pairs) differ from those in the dataset papers.

## N. Limitations
1. **Stated (p.14):** fine-grained spatiotemporal reasoning in dynamic scenes; reflective surfaces and subtle human–object interactions (door case, Fig.6).
2. **Future:** more VLM families; smaller models.
3. **Observable:** no robot (stated deliberately, p.8); configuration selection reported on test data; text-similarity metrics only.

## P. Direct-paper questions (abridged) — offline action-language generation; nothing about closed-loop social behaviour can be concluded.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: C: preprint only; venue arXiv:2603.11447v1 [cs.RO], 12 Mar 2026 (LNCS-style template); DOI Not found / not applicable; pages NA; URL https://arxiv.org/abs/2603.11447.
- Sources: arXiv abs page (2603.11447v1); Crossref title search: no match.
- Version relationship: arXiv only; an IEICE technical report is a related (non-archival) version.
- Changed field - doi: PDF-derived 'Not reported' -> externally verified 'Not found / not applicable'
- Changed field - url: PDF-derived 'Not reported' -> externally verified 'https://arxiv.org/abs/2603.11447'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

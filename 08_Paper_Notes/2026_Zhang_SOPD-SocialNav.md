---
id: 2026_Zhang_SOPD-SocialNav
source_pdfs: [05_Direct_VLM_SocialNav_Preprints/2607.19850v1.pdf]
duplicate_copies: []
related_versions: []
title: 'SOPD-SocialNav: Selective On-Policy Distillation for Vision-Language Social Navigation'
authors: &id001 [Xinyu Zhang, Zishuo Wang, Ling Xiao]
year: 2026
venue: arXiv:2607.19850v1 [cs.RO], 22 Jul 2026
volume: NA
issue: NA
pages: '7'
doi: Not found / not applicable
url: https://arxiv.org/abs/2607.19850
pub_status: accepted per author statement; not yet indexed
peer_reviewed: Accepted (not yet indexed)
peer_review_basis: 'Externally verified (2026-10-19): arXiv abs page (2607.19850v1): comment "accepted to 2026 WRC Symposium on Advanced Robotics and Automation (WRC SARA)"; Crossref title search: no match; Symposium held 21 Aug 2026; IEEE Xplore record pending.'
category: S5
folder: 05_Direct_VLM_SocialNav_Preprints
folder_category_match: 'Yes'
category_rationale: Distils social-navigation reasoning from a fine-tuned Qwen3-VL-8B teacher into a Qwen2.5-VL-3B student via entropy-selective on-policy distillation; offline evaluation plus qualitative robot deployment.
paper_type: method
fm_used: 'Yes'
fm_class: [VLM]
fm_models: ['Teacher: Qwen3-VL-8B (SFT, frozen)', 'Student: Qwen2.5-VL-3B']
fm_size: 8B teacher / 3B student
method_family: [supervised fine-tuning, on-policy distillation, entropy-based token selection, temperature-controlled Jensen-Shannon divergence]
roles: [F1, F4, F8]
roles_evidence: {F8: 'Teacher VLM supervises student on student-generated responses (OPD) with entropy-selected tokens (Eq.1-7, p.3-4).', F1: Perception text evaluated (Per-cos)., F4: 'Reasoning and action outputs (Rea-cos, Acc); social conventions in qualitative real-world cases (p.6).'}
integration: I1
integration_rationale: Student outputs discrete navigation actions (e.g., 'move forward left'); execution mechanism on robot not described.
evidence: E1
evidence_rationale: Quantitative evaluation offline on SNEI and MUSON; real-world Scout Mini deployment reported only as two qualitative decision examples plus latency (p.6).
inputs: [RGB (single egocentric image), prompt]
outputs: [natural-language perception, reasoning, discrete action]
human_repr: [semantic description (language)]
capabilities: {C1: 'No', C2: 'No', C3: Partial, C4: 'No', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: Partial, C10: Partial, C11: Partial, C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: Partial, C17: 'No', C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: 'No', C24: Partial, C25: 'No'}
exp:
  datasets: [SNEI, MUSON]
  simulators: []
  robots: [AgileX Scout Mini (qualitative)]
  environment: dataset images; real-world conversational and queuing scenes
  indoor_outdoor: Not reported
  sensors: [RGB]
  humans: real (images; two pedestrians in real demos)
  n_scenes: Not reported
  n_trajectories: NA
  n_participants: NA
  split: random 8:2 per dataset
  baselines: [SFT, SKD (off-policy), VL-KD (off-policy), OPD (on-policy), OPSD (on-policy)]
  ablation: Yes (entropy mask, JSD, divergence functions)
  real_robot_trials: Partial (qualitative)
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [conversational group (face-to-face pair), queue]
metrics: [VLM | Action Accuracy (Acc) | proportion | predicted action exactly matches GT action | p.4, VLM | Perception Cosine Similarity (Per-cos) | cosine | SBERT similarity of perception text | p.4, VLM | Reasoning Cosine Similarity (Rea-cos) | cosine | SBERT similarity of reasoning text | p.4, DEPLOY | Inference throughput | FPS | 0.984 FPS model; 0.365 FPS end-to-end (2.74 s incl. network/image transfer) | p.6]
deployment: {fm_model: Qwen2.5-VL-3B (distilled student), model_size: 3B, api_cloud_local: Remote server (network communication and image upload/download in pipeline), onboard_offboard: Offboard (implied by network transfer), gpu: 8x A100 (training); inference hardware not reported, cpu: Not reported, latency: 0.984 FPS model; 2.74 s end-to-end (0.365 FPS), query_frequency: Not reported, planner_frequency: NA, controller_frequency: Not reported, asynchronous: Not reported, caching: NA, event_triggered: NA, distillation: 'Yes (on-policy, entropy-selective)', quantization: 'No', fallback_planner: Not reported, safety_shield: Not reported, emergency_behavior: Not reported, uncertainty: Teacher entropy used for token selection only (training), hallucination_mitigation: 'No', real_time_claim_supported: No (2.74 s end-to-end)}
repro: {code: Not reported, code_url: NA, dataset: 'SNEI, MUSON (public)', dataset_url: NA, checkpoints: NA, prompts_published: 'No', hardware_specified: Partial (training), hyperparameters: 'Yes (5 epochs, lr 1e-5, cosine, warm-up 0.1, lambda 2.0, tau 1.5)', protocol_described: Partial, project_page: NA, concerns: 'SFT baseline values identical to GCL paper''s ''Action-F1'' (BERTScore) values but labelled exact-match Acc here; random 8:2 split vs fixed 265/60 elsewhere.'}
limitations_flags: [latency, cloud-dependence, low-level-grounding, no-human-study]
web_verification_required: []
cited_missing: [MiniLLM, Speculative KD (ICLR 2025), 'On-policy self-distillation (OPSD, arXiv 2026)', Survey of on-policy distillation for LLMs (arXiv 2026), Adaptive proxemics based on emotions (Bilen 2024), Yildirim 2024 learning social navigation from demonstrations]
coding: {latency_reported: 'Yes', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: 'No', code_released: 'No', new_dataset_released: NA, real_robot: Demo, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2026
  authors: *id001
  venue: arXiv:2607.19850v1 [cs.RO], 22 Jul 2026
  volume: NA
  issue: NA
  pages: '7'
  doi: Not reported
  url: Not reported
  pub_status: preprint
  peer_reviewed: 'No'
  peer_review_basis: arXiv v1; no venue.
external_verification:
  verified_on: '2026-10-19'
  status_class: 'B: accepted per authors/arXiv; proceedings not yet available'
  verified_venue: arXiv:2607.19850v1 [cs.RO], 22 Jul 2026
  verified_doi: Not found / not applicable
  verified_url: https://arxiv.org/abs/2607.19850
  verified_pages: NA
  arxiv: 2607.19850v1
  version_relationship: arXiv only; published version not yet available
  sources: ['arXiv abs page (2607.19850v1): comment "accepted to 2026 WRC Symposium on Advanced Robotics and Automation (WRC SARA)"', 'Crossref title search: no match', Symposium held 21 Aug 2026; IEEE Xplore record pending]
snei_usage: {reported_quantity: Not stated, unit: 'random 8:2 train/test split', what_it_represents: SNEI as used in SOPD, page: p.4, remark: Size of the SNEI version used not reported, provenance_note: SNEI provenance (SCAND vs SCAND+MuSoHu) UNRESOLVED; see SNEI_DATASET_RECONCILIATION.md}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A5]
  C_capabilities: {SAF1: 'No', SAF2: 'No', SPA1: Partial, SPA2: Partial, SPA3: Partial, SPA4: 'No', HUM1: 'No', HUM2: 'No', NOR1: Partial, NOR2: 'No', NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: [R1, R3]
  D_interface: [D0]
  E_evidence_profile: {EV1_offline: 'Yes', EV2_closed_loop_sim: 'No', EV3_physical_robot: demo, EV4_real_humans_in_trials: none, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: NA, statistical_testing: 'No', cross_environment: No/unclear, runtime_measured: 'Yes'}
  cross_cutting: {temporal_coupling: offline, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'No', uncertainty: 'No', hallucination_mitigation: 'No', privacy_constraint: 'No', inference_location: n/a (offline evaluation only)}
physical_source_folder: "05_Direct_VLM_SocialNav_Preprints"
analytical_category: "S5"
coding:
  latency_reported: "Yes"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "No"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "Demo"
  human_subject_study: "No"
---

# SOPD-SocialNav (Zhang, Wang, Xiao — arXiv Jul 2026)

Page convention: PDF index (p.N).

## A. Bibliographic — arXiv:2607.19850v1 (22 Jul 2026), Hokkaido Univ. Preprint. **After the Cai survey cut-off.**

## B. Position — S5. FM-to-FM distillation for lightweight social-navigation VLMs.

## C. Research problem — large VLMs undeployable; small VLMs lack social reasoning; standard OPD uses mode-seeking reverse KL and treats all tokens equally (p.1). Contributions: entropy-selective OPD (SOPD); systematic comparison of distillation paradigms and divergences; Scout Mini deployment (p.1–2).

## D. Method — teacher Qwen3-VL-8B SFT then frozen; student samples responses y ~ π_S(x) (Eq.1); temperature-softened distributions (λ = 2.0) (Eq.2–3); JSD loss (Eq.4); teacher entropy H_i (Eq.5); mask m_i = 1(H_i > τ), τ = 1.5 (Eq.6); L_SOPD = Σ m_i JSD (Eq.7); 5 epochs, lr 1e-5, 8× A100 (p.3–4).

## L. Quantitative results (Table I, p.4, visually verified; SNEI Acc/Per-cos/Rea-cos | MUSON Acc/Per-cos/Rea-cos)
SFT 0.692/0.834/0.767 | 0.811/0.810/0.803; SKD 0.831/0.828/0.819 | 0.932/0.936/0.934; VL-KD 0.799/0.777/0.784 | 0.916/0.910/0.897; OPD 0.792/0.795/0.797 | 0.886/0.920/0.896; OPSD 0.863/0.851/0.872 | 0.895/0.907/0.903; SOPD 0.889/0.901/0.894 | 0.953/0.938/0.955.
Table II (MUSON ablation; Acc/Per/Rea): SFT 0.811/0.810/0.803; w/o m_i (JSD only) 0.893/0.892/0.884; w/o L_JSD (mask only) 0.836/0.834/0.829; full 0.953/0.938/0.955.
Table III (divergence): Reverse KL 0.885/0.837/0.824; Forward KL 0.853/0.856/0.835; Weighted JSD 0.861/0.826/0.843; Temperature JSD 0.953/0.938/0.955.
Real world: 0.984 FPS inference; 2.74 s end-to-end (0.365 FPS) incl. network; qualitative: SOPD outputs "move forward left" around a conversing pair and a queue where SKD/OPSD output "move forward" (Figs.3–4).
- **Data-quality issue:** SFT rows (SNEI 0.692/0.834/0.767; MUSON 0.811/0.810/0.803) are numerically identical to the GCL paper's SFT Qwen2.5-VL-3B rows, where the first column is "Action-F1" (BERTScore of action text); here it is exact-match "Acc". Also splits differ (random 8:2 here vs SNEI 265/60 in GCL).

## N. Limitations
1. **Stated (p.6):** future adaptive entropy thresholds, longer horizons, more diverse real-world HRI.
2. **Observable:** real-world evidence is two qualitative frames; offboard inference with 2.74 s latency; no closed-loop metrics.

## P. Direct-paper questions (abridged) — offline action decisions; demo shows queue/conversation avoidance qualitatively; cannot conclude closed-loop safety, comfort, or reliability.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: B: accepted per authors/arXiv; proceedings not yet available; venue arXiv:2607.19850v1 [cs.RO], 22 Jul 2026; DOI Not found / not applicable; pages NA; URL https://arxiv.org/abs/2607.19850.
- Sources: arXiv abs page (2607.19850v1): comment "accepted to 2026 WRC Symposium on Advanced Robotics and Automation (WRC SARA)"; Crossref title search: no match; Symposium held 21 Aug 2026; IEEE Xplore record pending.
- Version relationship: arXiv only; published version not yet available.
- Changed field - doi: PDF-derived 'Not reported' -> externally verified 'Not found / not applicable'
- Changed field - url: PDF-derived 'Not reported' -> externally verified 'https://arxiv.org/abs/2607.19850'
- Changed field - pub_status: PDF-derived 'preprint' -> externally verified 'accepted per author statement; not yet indexed'
- Changed field - peer_reviewed: PDF-derived 'No' -> externally verified 'Accepted (not yet indexed)'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

## Stage-7 status re-check (2026-10-19)
arXiv v1 still states acceptance to 2026 WRC SARA; no Crossref/proceedings record. Status unchanged: accepted, not yet indexed. See 09_Project_Reports/PUBLICATION_STATUS_FINAL_CHECK.md.

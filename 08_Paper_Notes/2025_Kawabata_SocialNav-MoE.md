---
id: 2025_Kawabata_SocialNav-MoE
source_pdfs: [05_Direct_VLM_SocialNav_Preprints/2512.14757v1.pdf]
duplicate_copies: []
related_versions: []
title: 'SocialNav-MoE: A Mixture-of-Experts Vision Language Model for Socially Compliant Navigation with Reinforcement Fine-Tuning'
authors: &id001 [Tomohito Kawabata, Xinyu Zhang, Ling Xiao]
year: 2025
venue: arXiv:2512.14757v1 [cs.CV], 15 Dec 2025
volume: NA
issue: NA
pages: '8'
doi: Not found / not applicable
url: https://arxiv.org/abs/2512.14757
pub_status: preprint
peer_reviewed: 'No'
peer_review_basis: 'Publication status: Preprint; Peer reviewed: No verified peer-reviewed version found as of corpus freeze date (2026-10-19). Sources: arXiv abs page (2512.14757v1); Crossref title search: no match.'
category: S5
folder: 05_Direct_VLM_SocialNav_Preprints
folder_category_match: 'Yes'
category_rationale: Small MoE VLM (SigLIP + Phi-2, MoE layers) trained with SFT, reinforcement fine-tuning (GSPO + semantic similarity reward) and MoE fine-tuning to output socially compliant navigation actions; offline SNEI evaluation.
paper_type: method
fm_used: 'Yes'
fm_class: [VLM]
fm_models: ['SocialNav-MoE: SigLIP + Phi-2-2.7B with sparse MoE layers (5.74B total params)', 'variants: Qwen-1.8B, StableLM-1.6B; CLIP encoder', 'baselines GPT-4o, Claude (zero-shot)']
fm_size: 5.74B total parameters
method_family: [supervised fine-tuning, 'reinforcement fine-tuning (GSPO, GRPO, DPO)', mixture-of-experts, multi-turn VQA]
roles: [F1, F2, F4]
roles_evidence: {F1: 'Multi-turn questions include ''What do you perceive from the image?'' (Fig.1-2).', F2: '''What do you predict these humans will do next?'' turn (Fig.2).', F4: '''Why do you think that?'' / ''What should the robot do?'' / ''Explain your decision.'' turns; RFT aligns outputs with GT and ''human subjective preferences'' (p.2-3).'}
integration: I1
integration_rationale: Outputs language navigation actions evaluated by semantic similarity; no robot integration (future work, p.6-7).
evidence: E1
evidence_rationale: Offline evaluation on 60 SNEI test images using semantic-similarity metrics and FPS; no simulation or robot.
inputs: [RGB (single image), natural language multi-turn questions]
outputs: [natural-language perception, prediction, reasoning, action, explanation]
human_repr: [semantic description (language), language-predicted human movement]
capabilities: {C1: 'No', C2: 'No', C3: 'No', C4: 'No', C5: Partial, C6: Partial, C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: Partial, C12: Partial, C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: Partial, C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: 'No', C24: Partial, C25: 'No'}
exp:
  datasets: ['SNEI subset: 325 images (265 train augmented to 530 / 60 test)']
  simulators: []
  robots: []
  environment: dataset images
  indoor_outdoor: both
  sensors: [RGB]
  humans: real (images)
  n_scenes: 325 images
  n_trajectories: NA
  n_participants: NA
  split: 265 (aug. 530) / 60
  baselines: [GPT-4o, Claude, DPO, GRPO+SSR, hard-level reward, character-level reward]
  ablation: Yes (SLM type, experts 1-4 and top-k, vision encoder, frozen/trained encoder, RFT methods, reward type, single/multi-turn)
  real_robot_trials: 'No'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [stationary crowds, moving obstructions, clear path (images)]
metrics: [VLM | BERTScore-P / -R / -F1 | score | token-level semantic similarity to GT action | p.4-5, VLM | SBERT-cos | cosine | sentence-level similarity | p.4, VLM | SMS (Sentence Mover's Similarity) | score | holistic semantic similarity | p.4, DEPLOY | Parameter count | B | total parameters | p.5, DEPLOY | FPS | frames/s | inference speed for action-generation phase only (hardware not reported) | p.4-5]
deployment: {fm_model: SocialNav-MoE (SigLIP + Phi-2 MoE), model_size: 5.74B, api_cloud_local: 'Local (baselines via API, implied)', onboard_offboard: Not reported, gpu: Not reported, cpu: Not reported, latency: '1.709 FPS (vs GPT-4o 0.212, Claude 0.087); hardware not reported', query_frequency: NA, planner_frequency: NA, controller_frequency: NA, asynchronous: NA, caching: NA, event_triggered: NA, distillation: 'No', quantization: 'No', fallback_planner: NA, safety_shield: NA, emergency_behavior: NA, uncertainty: 'No', hallucination_mitigation: 'No', real_time_claim_supported: No (efficiency claim; no robot)}
repro: {code: Promised upon acceptance, code_url: NA, dataset: SNEI (public), dataset_url: NA, checkpoints: NA, prompts_published: Partial (question set Fig.1), hardware_specified: 'No', hyperparameters: 'Yes (learning rates, epochs, group size 8)', protocol_described: Partial, project_page: NA, concerns: 60-sample test; FPS hardware not specified; GPT-4o/Claude parameter counts taken from a medical-NLP paper estimate.}
limitations_flags: [intention-ambiguity, dataset-bias, low-level-grounding]
web_verification_required: [Acceptance status; code release.]
cited_missing: [VLM-GroNav (ICRA 2025), Nav-R1, VLN-R1, GSPO, Visual-RFT, Reason-RFT, SG-Nav, UniGoal, Stranger danger (ICRA 2024), Characterizing complexity of social navigation scenarios (Stratton RA-L 2024), SocialGAIL]
coding: {latency_reported: 'Yes', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: 'No', code_released: Promised, new_dataset_released: NA, real_robot: 'No', human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2025
  authors: *id001
  venue: arXiv:2512.14757v1 [cs.CV], 15 Dec 2025
  volume: NA
  issue: NA
  pages: '8'
  doi: Not reported
  url: Not reported
  pub_status: preprint
  peer_reviewed: 'No'
  peer_review_basis: arXiv v1; 'Source code will be released upon acceptance' (abstract) - not yet accepted.
external_verification:
  verified_on: '2026-10-19'
  status_class: 'C: preprint only'
  verified_venue: arXiv:2512.14757v1 [cs.CV], 15 Dec 2025
  verified_doi: Not found / not applicable
  verified_url: https://arxiv.org/abs/2512.14757
  verified_pages: NA
  arxiv: 2512.14757v1
  version_relationship: arXiv only
  sources: [arXiv abs page (2512.14757v1), 'Crossref title search: no match']
  peer_reviewed_note: No verified peer-reviewed version found as of corpus freeze date
  publication_status: Preprint
snei_usage: {reported_quantity: 325 (265 train / 60 test); augmented to 530, unit: images, what_it_represents: Described as SNEI ("consists of 325 images"), page: p.4, remark: Augmentation count from note, provenance_note: SNEI provenance (SCAND vs SCAND+MuSoHu) UNRESOLVED; see SNEI_DATASET_RECONCILIATION.md}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A5]
  C_capabilities: {SAF1: 'No', SAF2: 'No', SPA1: 'No', SPA2: 'No', SPA3: Partial, SPA4: Partial, HUM1: Partial, HUM2: 'No', NOR1: Partial, NOR2: 'No', NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: [R1, R2, R3]
  D_interface: [D0]
  E_evidence_profile: {EV1_offline: 'Yes', EV2_closed_loop_sim: 'No', EV3_physical_robot: none, EV4_real_humans_in_trials: none, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: NA, statistical_testing: 'No', cross_environment: 'Yes', runtime_measured: 'Yes'}
  cross_cutting: {temporal_coupling: offline, memory: 'No', continual_adaptation: 'No', explanation_output: 'Yes (text output, not delivered to people)', safety_guard: 'No', uncertainty: 'No', hallucination_mitigation: 'No', privacy_constraint: 'No', inference_location: n/a (offline evaluation only)}
physical_source_folder: "05_Direct_VLM_SocialNav_Preprints"
analytical_category: "S5"
coding:
  latency_reported: "Yes"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "No"
  code_released: "Promised"
  new_dataset_released: "NA"
  real_robot: "No"
  human_subject_study: "No"
---

# SocialNav-MoE (Kawabata, Zhang, Xiao — arXiv 2025)

Page convention: PDF index (p.N).

## A. Bibliographic — arXiv:2512.14757v1 (15 Dec 2025), Hokkaido Univ. (same group as competing survey). Preprint.

## B. Position — S5. Efficiency-oriented small MoE VLM with reinforcement fine-tuning for socially compliant navigation decisions; offline.

## C. Research problem — large VLMs too slow/energy-intensive; general VLMs weak at fine-grained social reasoning (p.1). Contributions: SocialNav-MoE (MoE + RFT); semantic similarity reward (SSR = BERTScore-F1) for GSPO; analysis of SLMs, experts, routing, encoders (p.1).

## D. Technical method — SigLIP + Phi-2-2.7B; half of transformer FFN layers replaced by sparse MoE (alternating); stages: image–text alignment (init LLaVA-1.5-58K, lr 1e-3), SFT on augmented SNEI (20 cycles, lr 2e-5), RFT (GSPO or GRPO + SSR, 3 epochs, lr 2e-6, group 8), MoE fine-tuning (20 epochs, lr 2e-6), multi-turn (p.2–4). GSPO objective Eq.2–5; SSR Eq.8–10.

## G. Social capabilities (OFFLINE) — C5, C6 Partial (prediction turn); C11, C12, C17, C24 Partial (stopping for moving obstructions, slow turns around stationary crowds — qualitative Fig.3); rest No.

## H/I — I1; E1.

## L. Quantitative results
Table I: GPT-4o ~200B params (as cited), 0.212 FPS; Claude ~175B, 0.087 FPS; SocialNav-MoE 5.74B, 1.709 FPS.
Table II (BS-P / BS-R / BS-F1 / SBERT / SMS): GPT-4o 0.076/0.443/0.254/0.557/0.376; Claude −0.233/0.387/0.059/0.509/0.417; SocialNav-MoE (original data) 0.445/0.410/0.427/0.594/0.489; (augmented) 0.520/0.492/0.506/0.671/0.551.
Table III (SLM): Phi-2-2.7B 0.486/0.466/0.476/0.642/0.523; Qwen-1.8B 0.486/0.456/0.472/0.636/0.520; StableLM-1.6B 0.419/0.378/0.399/0.566/0.461.
Table IV (experts/top-k; SMS): 1/1 0.473; 2/1 0.519; 2/2 0.479; 3/1 0.517; 3/2 0.494; 3/3 0.478; 4/1 0.523; 4/2 0.475; 4/3 0.473; 4/4 0.471.
Table V: CLIP 0.473/0.457/0.465/0.638/0.514; SigLIP 0.486/0.466/0.476/0.642/0.523. Table VI: frozen 0.486/0.466/0.476/0.642/0.523; trained 0.487/0.468/0.478/0.641/0.515.
Table VII (RFT): DPO 0.481/0.463/0.472/0.649/0.527; GRPO+SSR 0.499/0.467/0.483/0.655/0.531; GSPO+SSR 0.520/0.492/0.506/0.671/0.551.
Table VIII (reward): hard 0.488/0.466/0.477/0.645/0.532; character 0.453/0.435/0.444/0.627/0.510; SSR 0.520/0.492/0.506/0.671/0.551.
Table IX (train/inference; w/o RFT multi 0.486/0.466/0.476/0.642/0.523; single 0.466/0.453/0.460/0.624/0.510; w/ RFT multi 0.520/0.492/0.506/0.671/0.551; single 0.468/0.457/0.463/0.637/0.514).
- **Cross-paper inconsistency:** GPT-4o and Claude BERTScore values and FPS are identical to E-SocialNav's Table 1 (same group, same 60-sample split), but SBERT/SMS differ (E-SocialNav: GPT-4o SBERT 0.672, SMS 0.651; here 0.557, 0.376). Not explained.
- Note: reward = BERTScore-F1 and evaluation includes BERTScore-F1 → the training reward and evaluation metric coincide (risk of metric optimisation).

## N. Limitations
1. **Stated (p.6–7):** lack of universally accepted social norms complicates learning and evaluation; ambiguous GT (Fig.5); data scarcity (expert degradation).
2. **Future:** deploy on real robots; lighter models.
3. **Observable:** offline only; 60 test images; reward = evaluation metric; no hardware for FPS.

## P. Direct-paper questions (abridged) — offline action-language generation; no robot, safety layer, temporal context, uncertainty or human study; cannot conclude anything about navigation behaviour.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: C: preprint only; venue arXiv:2512.14757v1 [cs.CV], 15 Dec 2025; DOI Not found / not applicable; pages NA; URL https://arxiv.org/abs/2512.14757.
- Sources: arXiv abs page (2512.14757v1); Crossref title search: no match.
- Version relationship: arXiv only.
- Changed field - doi: PDF-derived 'Not reported' -> externally verified 'Not found / not applicable'
- Changed field - url: PDF-derived 'Not reported' -> externally verified 'https://arxiv.org/abs/2512.14757'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

---
id: 2022_Shah_LM-Nav
source_pdfs: [03_Adjacent_Foundation_Model_Navigation/shah23b.pdf]
duplicate_copies: []
related_versions: ['arXiv:2207.04429 (cited in corpus)']
title: 'LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action'
authors: &id001 [Dhruv Shah, Błażej Osiński, Brian Ichter, Sergey Levine]
year: 2022
venue: Proceedings of The 6th Conference on Robot Learning (CoRL 2022), PMLR 205
volume: NA
issue: NA
pages: 492-504
doi: Not found / not applicable
url: https://proceedings.mlr.press/v205/shah23b.html
pub_status: conference
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): PMLR proceedings page (https://proceedings.mlr.press/v205/shah23b.html); arXiv abs page (2207.04429v2). PDF-derived basis (Stage 1): CoRL 2022 footer (p.1).'
category: S3
folder: 03_Adjacent_Foundation_Model_Navigation
folder_category_match: 'Yes'
category_rationale: Composes GPT-3 (landmark extraction), CLIP (landmark grounding) and ViNG (visual navigation) for zero-shot outdoor instruction following; no social behaviour.
paper_type: method
fm_used: 'Yes'
fm_class: [LLM, CLIP-style]
fm_models: [GPT-3 (landmark parsing), CLIP ViT-L (grounding), ViNG (pre-trained visual navigation model; not a large FM)]
fm_size: Not reported
method_family: [zero-shot composition of pre-trained models, few-shot prompting (2 examples), topological graph, dynamic-programming graph search]
roles: [F1, F7]
roles_evidence: {F1: 'CLIP computes P(v_i | l_j) between graph-node images and landmark text (p.3, p.5).', F7: GPT-3 decomposes free-form instructions into an ordered list of landmarks (p.4).}
integration: I2
integration_rationale: FM outputs (landmark sequence and node-landmark probabilities) are inputs to a graph-search objective (Eq.3) whose walk is executed by ViNG.
evidence: E3
evidence_rationale: 20 real-world instructions on a Clearpath Jackal across two outdoor environments (>6 km total) with success, efficiency and disengagement metrics (Table 1); no human study.
inputs: [free-form instruction, graph-node RGB images from prior traversal, GPS (graph construction)]
outputs: [landmark list, node probabilities, walk on topological graph]
human_repr: [none]
capabilities: {C1: NA, C2: NA, C3: NA, C4: NA, C5: NA, C6: NA, C7: NA, C8: NA, C9: NA, C10: NA, C11: NA, C12: NA, C13: NA, C14: NA, C15: NA, C16: NA, C17: NA, C18: NA, C19: NA, C20: NA, C21: NA, C22: NA, C23: NA, C24: NA, C25: NA}
exp:
  datasets: [20 instructions, 100 images x 30 landmarks (VLM retrieval test)]
  simulators: []
  robots: [Clearpath Jackal UGV]
  environment: suburban outdoor (EnvSmall, EnvLarge)
  indoor_outdoor: outdoor
  sensors: [RGB, GPS]
  humans: none in evaluation
  n_scenes: 2 environments
  n_trajectories: 20 instructions (10 per environment); >6 km total
  n_participants: NA
  split: NA
  baselines: [GPS-Nav (no VNM), Max-likelihood planner, 'LLM alternatives (noun chunks, fairseq, GPT-J, GPT-NeoX)', 'VLM alternatives (Faster-RCNN, ViLD)']
  ablation: Yes (each component)
  real_robot_trials: 'Yes'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: []
metrics: [NAV | Net Success | fraction | walk matches intended path or visits described landmarks | p.6-7, 'NAV | Efficiency | ratio | described / executed route length, clipped at 1 | p.7', 'SAFETY | # Disengagements | count per experiment | human interventions due to unsafe maneuvers | p.7', NAV | Planning success / efficiency | fraction / ratio | graph-search output quality | p.7, OTHER | Avg. extraction success | fraction | LLM landmark parsing | p.7, VLM | Detection rate | fraction | top-3 landmark retrieval | p.7-8]
deployment: {fm_model: GPT-3 + CLIP, model_size: Not reported, api_cloud_local: GPT-3 via API (cloud), onboard_offboard: Not reported, gpu: Not reported, cpu: Not reported, latency: Not reported, query_frequency: once per instruction (offline planning), planner_frequency: NA, controller_frequency: Not reported, asynchronous: NA, caching: NA, event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: 'No', safety_shield: 'No', emergency_behavior: Human disengagement, uncertainty: Probabilistic objective over landmarks/traversability, hallucination_mitigation: 'No', real_time_claim_supported: NA}
repro: {code: Yes (Colab notebook), code_url: sites.google.com/view/lmnav, dataset: Not reported, dataset_url: NA, checkpoints: NA, prompts_published: Yes (Appendix A), hardware_specified: Partial (Appendix C), hyperparameters: Partial, protocol_described: 'Yes', project_page: sites.google.com/view/lmnav, concerns: Requires pre-built topological graph from manual driving.}
limitations_flags: [cloud-dependence, limited-scenarios]
web_verification_required: []
cited_missing: [ViNG (Shah ICRA 2021), RECON, ViKiNG, CLIP, GPT-J, GPT-NeoX]
adjacent: {mechanism: 'Modular zero-shot pipeline: LLM -> landmarks; VLM -> node grounding; VNM -> traversability and control; DP graph search.', relevance: Canonical 'compose pre-trained models' navigation architecture reused by VLM social navigation pipelines (VLM semantic layer + learned navigator)., why_not_direct: 'No humans, no social reasoning; ignores verbs/adverbs such as ''drive past the dog very slowly''.', inherited_by: 'Cited by corpus VLM-Social-Nav, VL-TGS, PAD, ViLAM, Code as Policies, VLMaps, GNM, Pan review.'}
coding: {latency_reported: 'No', safety_mechanism: 'No', uncertainty_treatment: Partial, hallucination_treatment: 'No', code_released: 'Yes', new_dataset_released: NA, real_robot: Systematic, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2022
  authors: *id001
  venue: 6th Conference on Robot Learning (CoRL 2022), Auckland (PMLR; file shah23b)
  volume: Not reported
  issue: NA
  pages: 13 (PDF incl. appendix)
  doi: Not reported
  url: sites.google.com/view/lmnav
  pub_status: conference
  peer_reviewed: 'Yes'
  peer_review_basis: CoRL 2022 footer (p.1).
project_url: sites.google.com/view/lmnav
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: Proceedings of The 6th Conference on Robot Learning (CoRL 2022), PMLR 205
  verified_doi: Not found / not applicable
  verified_url: https://proceedings.mlr.press/v205/shah23b.html
  verified_pages: 492-504
  arxiv: 2207.04429v2
  version_relationship: Corpus copy is the PMLR published version; arXiv 2207.04429v2 alternate
  sources: ['PMLR proceedings page (https://proceedings.mlr.press/v205/shah23b.html)', arXiv abs page (2207.04429v2)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A0]
  C_capabilities: {SAF1: NA, SAF2: NA, SPA1: NA, SPA2: NA, SPA3: NA, SPA4: NA, HUM1: NA, HUM2: NA, NOR1: NA, NOR2: NA, NOR3: NA, NOR4: NA, EXP1: NA, EXP2: NA, EXP3: NA}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'No', EV3_physical_robot: systematic, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "03_Adjacent_Foundation_Model_Navigation"
analytical_category: "S3"
coding:
  latency_reported: "No"
  safety_mechanism: "No"
  uncertainty_treatment: "Partial"
  hallucination_treatment: "No"
  code_released: "Yes"
  new_dataset_released: "NA"
  real_robot: "Systematic"
  human_subject_study: "No"
---

# LM-Nav (Shah et al., CoRL 2022)

Page convention: PDF index (p.N).

## A. Bibliographic — CoRL 2022 (footer p.1); UC Berkeley, Univ. of Warsaw, Robotics at Google.

## B. Position — S3 adjacent: modular language-conditioned navigation from pre-trained models.

## C. Research problem — language-annotated navigation data are expensive; goal-image interfaces are unnatural (p.1). Contribution: LM-Nav combining LLM, VLM and VNM without fine-tuning (p.2).

## D. Method — Eq.1–2: P(success | v̄, ℓ̄) ∝ Π λ^D(v_j,v_j+1) · Π P(v_ti | ℓ_i); Eq.3 R = Σ CLIP(v_ti, ℓ_i) − α Σ D(v_j, v_j+1); DP search (Algorithm 1, Eq.4–5); CLIP prompt "This is a photo of a [ℓ]"; GPT-3 with 2-example prompt (p.3–5).

## L. Quantitative results (visually verified p.7)
- Table 1: GPS-Nav (no VNM) EnvSmall: net success 0.23, efficiency 0.93, disengagements 0.75, planning 0.9; LM-Nav EnvSmall: 0.8 / 0.96 / 0.1 / 0.9; EnvLarge: 0.8 / 0.89 / 0 / 0.8 (planning 85% overall; 1 intervention per 6.4 km).
- Table 2 (extraction success): noun chunks 0.88; fairseq-1.3B 0.52; fairseq-13B 0.76; GPT-J-6B 0.80; GPT-NeoX-20B 0.72; GPT-3 1.0.
- Table 3 (detection rate): Faster-RCNN 0.07; ViLD 0.38; CLIP-ViT 0.87.
- Table 4 (planning success / efficiency): Max likelihood EnvSmall 0.6 / 0.69, EnvLarge 0.2 / 0.17; LM-Nav 0.9 / 0.80 and 0.8 / 0.99.

## N. Limitations
1. **Stated (p.8):** landmark-only reasoning discards verbs/adverbs (e.g., "drive past the dog very slowly"); VNM specific to Jackal outdoors.
2. **Future:** general navigation model (→ GNM).
3. **Observable:** pre-built graph required; 20 instructions only; failures from undetectable landmarks and lighting.
4. **Social relevance:** the paper's own example of an unhandled instruction ("past the dog very slowly") is a social/behavioural modifier — a gap later VLM social-navigation work targets.

## P. Adjacent analysis — see `adjacent:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue Proceedings of The 6th Conference on Robot Learning (CoRL 2022), PMLR 205; DOI Not found / not applicable; pages 492-504; URL https://proceedings.mlr.press/v205/shah23b.html.
- Sources: PMLR proceedings page (https://proceedings.mlr.press/v205/shah23b.html); arXiv abs page (2207.04429v2).
- Version relationship: Corpus copy is the PMLR published version; arXiv 2207.04429v2 alternate.
- Changed field - venue: PDF-derived '6th Conference on Robot Learning (CoRL 2022), Auckland (PMLR; file shah23b)' -> externally verified 'Proceedings of The 6th Conference on Robot Learning (CoRL 2022), PMLR 205'
- Changed field - volume: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - pages: PDF-derived '13 (PDF incl. appendix)' -> externally verified '492-504'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified 'Not found / not applicable'
- Changed field - url: PDF-derived 'sites.google.com/view/lmnav' -> externally verified 'https://proceedings.mlr.press/v205/shah23b.html'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

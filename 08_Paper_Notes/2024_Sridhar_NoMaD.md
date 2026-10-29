---
id: 2024_Sridhar_NoMaD
source_pdfs: [03_Adjacent_Foundation_Model_Navigation/2310.07896v1.pdf]
duplicate_copies: []
related_versions: ['Published: IEEE ICRA 2024, pp. 63-70 (per Arena 4.0 reference list); corpus copy arXiv:2310.07896v1 (11 Oct 2023)']
title: 'NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration'
authors: &id001 [Ajay Sridhar, Dhruv Shah, Catherine Glossop, Sergey Levine]
year: 2024
venue: 2024 IEEE International Conference on Robotics and Automation (ICRA)
volume: NA
issue: NA
pages: 63-70
doi: 10.1109/ICRA57147.2024.10610665
url: https://doi.org/10.1109/ICRA57147.2024.10610665
pub_status: conference (corpus copy preprint)
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1109/ICRA57147.2024.10610665); arXiv abs page (2310.07896v1). PDF-derived basis (Stage 1): Corpus copy arXiv v1 without venue; Arena 4.0 (corpus) cites ICRA 2024 pp.63-70. WEB_VERIFICATION_REQUIRED.'
category: S3
folder: 03_Adjacent_Foundation_Model_Navigation
folder_category_match: 'Yes'
category_rationale: Unified goal-masked diffusion navigation policy (exploration + image-goal navigation) built on ViNT encoder; trained on GNM + SACSoN data including pedestrian-rich environments, but no social evaluation.
paper_type: model
fm_used: 'Yes'
fm_class: [NavFM]
fm_models: [NoMaD (19M params; EfficientNet-B0 + 4-layer Transformer + 1D conditional U-Net diffusion head)]
fm_size: 19M
method_family: [diffusion policy, goal masking, imitation learning, topological graph + frontier exploration]
roles: [F9, F10]
roles_evidence: {F9: 'Diffusion head samples sequences of 8 future actions (waypoints) (Fig.2, p.3-4).', F10: 'End-to-end visuomotor policy running onboard (p.2, p.5).'}
integration: I6
integration_rationale: Learned navigation policy (multimodal action diffusion) within a topological-graph exploration framework.
evidence: E3
evidence_rationale: Real-world exploration and navigation experiments on LoCoBot in 5-6 indoor/outdoor environments with success and collision counts (Tables I-III); no human study.
inputs: [current + past RGB frames (96x96), optional goal image (masked or unmasked)]
outputs: [8 future actions (waypoints) via 10 denoising steps, temporal distance]
human_repr: [none explicit]
capabilities: {C1: NA, C2: NA, C3: NA, C4: NA, C5: NA, C6: NA, C7: NA, C8: NA, C9: NA, C10: NA, C11: NA, C12: NA, C13: NA, C14: NA, C15: NA, C16: NA, C17: NA, C18: NA, C19: NA, C20: NA, C21: NA, C22: NA, C23: NA, C24: NA, C25: NA}
exp:
  datasets: [GNM dataset, SACSoN dataset (pedestrian-rich)]
  simulators: []
  robots: [LoCoBot]
  environment: indoor and outdoor (unspecified)
  indoor_outdoor: both
  sensors: [RGB]
  humans: not evaluated
  n_scenes: 6 environments (Sec. V) / 5 (Table I text)
  n_trajectories: Not reported
  n_participants: NA
  split: NA
  baselines: [VIB, Masked ViNT, Autoregressive, Random Subgoals (ViNT), Subgoal Diffusion (ViNT), Diffusion Policy, ViNT Policy]
  ablation: Yes (visual encoder, goal masking, unified vs dedicated)
  real_robot_trials: 'Yes'
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: []
metrics: [NAV | Success | % | mean success rate per method | p.4-5, SAFETY | Coll. (# collisions) | count per experiment | mean collisions per experiment | p.4-5]
deployment: {fm_model: NoMaD, model_size: 19M, api_cloud_local: Local, onboard_offboard: Onboard ('running entirely on-the-edge'; Jetson Orin mentioned), gpu: 'NVIDIA Jetson Orin (mentioned as target, p.2)', cpu: Not reported, latency: Not reported, query_frequency: Not reported, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Not reported, caching: NA, event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: Topological graph / frontier exploration, safety_shield: 'No', emergency_behavior: Not reported, uncertainty: Multimodal action distribution (not calibrated), hallucination_mitigation: NA, real_time_claim_supported: Partial (onboard claim; no latency numbers)}
repro: {code: 'Yes', code_url: general-navigation-models.github.io, dataset: 'Yes (GNM, SACSoN public)', dataset_url: NA, checkpoints: Not reported in paper, prompts_published: NA, hardware_specified: Partial, hyperparameters: 'Yes (AdamW 1e-4, 30 epochs, batch 256, K=10, pm=0.5, lambda 1e-4)', protocol_described: Partial, project_page: general-navigation-models.github.io, concerns: Number of trials per environment unreported; environment count inconsistent (6 vs 5).}
limitations_flags: [limited-scenarios]
web_verification_required: [ICRA 2024 publication details.]
cited_missing: [SACSoN (Hirose 2023), ViKiNG, Diffusion Policy (Chi RSS 2023), VIB latent goal exploration (Shah CoRL 2021), Navigating to objects in the real world (Gervet 2023)]
adjacent: {mechanism: Goal-masked Transformer context + conditional action diffusion yields one policy for undirected exploration and goal-conditioned navigation., relevance: Common low-level navigator / baseline in VLM social-navigation work; demonstrates multimodal action modelling relevant to socially ambiguous multi-action scenes., why_not_direct: 'No language, no human modelling, no social metrics.', inherited_by: 'Cited by corpus SocialNav-MoE, VL-TGS, BehAV, SocialNav (CVPR 2026); Arena 4.0.'}
coding: {latency_reported: 'No', safety_mechanism: 'No', uncertainty_treatment: Partial, hallucination_treatment: NA, code_released: 'Yes', new_dataset_released: NA, real_robot: Systematic, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2024
  authors: *id001
  venue: IEEE ICRA 2024 (per citation); corpus copy arXiv v1
  volume: NA
  issue: NA
  pages: 8 (PDF); 63-70 (per citation)
  doi: Not reported
  url: general-navigation-models.github.io
  pub_status: conference (corpus copy preprint)
  peer_reviewed: 'Yes'
  peer_review_basis: Corpus copy arXiv v1 without venue; Arena 4.0 (corpus) cites ICRA 2024 pp.63-70. WEB_VERIFICATION_REQUIRED.
project_url: general-navigation-models.github.io
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: 2024 IEEE International Conference on Robotics and Automation (ICRA)
  verified_doi: 10.1109/ICRA57147.2024.10610665
  verified_url: https://doi.org/10.1109/ICRA57147.2024.10610665
  verified_pages: 63-70
  arxiv: 2310.07896v1
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1109/ICRA57147.2024.10610665)', arXiv abs page (2310.07896v1)]
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
  hallucination_treatment: "NA"
  code_released: "Yes"
  new_dataset_released: "NA"
  real_robot: "Systematic"
  human_subject_study: "No"
---

# NoMaD (Sridhar et al., ICRA 2024)

Page convention: PDF index (p.N).

## A. Bibliographic — corpus copy arXiv:2310.07896v1 (11 Oct 2023); UC Berkeley; cited as ICRA 2024 pp.63–70.

## B. Position — S3 adjacent NavFM (successor of GNM/ViNT).

## C. Research problem — separate models for exploration and goal-reaching add complexity; can one expressive policy do both? (p.1). Contributions: goal-masked diffusion policy; real-world evaluation vs 6 baselines; 15× fewer parameters than ViNT+subgoal diffusion (p.1–2).

## D. Method — ViNT-style encoder (EfficientNet-B0, 256-d tokens, 4-layer/4-head Transformer); goal mask m ~ Bernoulli(0.5) during training; 1D conditional U-Net denoiser, K = 10 steps, square-cosine schedule; loss MSE(ε) + λ·MSE(distance), λ = 1e-4 (Eq.1–2, p.3–4). Training data GNM + SACSoN (>100 h, "including pedestrian-rich environments").

## L. Quantitative results
- Table I (Params; Exploration success / collisions; Navigation success): Masked ViNT 15M, 50% / 1.0, 30%; VIB 6M, 30% / 4.0, 15%; Autoregressive 19M, 90% / 2.0, 60%; Random Subgoals 30M, 70% / 2.7, 90%; Subgoal Diffusion 335M, 77% / 1.7, 90%; NoMaD 19M, 98% / 0.2, 90%.
- Table II: Diffusion Policy 15M undirected 98% / goal ✗; ViNT Policy 16M ✗ / 92%; NoMaD 19M 98% / 92%.
- Table III (encoder; success / collisions): Late-fusion CNN 52% / 3.2; Early-fusion CNN 68% / 1.5; ViT 32% / 2.5; NoMaD 98% / 0.2.
- **Data-quality notes:** "6 distinct environments" (p.4) vs Table I text "5 challenging environments" (p.5); "outperforms by over 25%" corresponds to 98% vs 77% (21 points absolute, ~27% relative); trial counts per environment not stated though percentages imply multiple trials; Table I navigation success for NoMaD (90%) differs from Table II goal-conditioned (92%).

## N. Limitations
1. **Stated (p.6):** goal images not natural for users (language/coordinates future); frontier-based high-level exploration could use semantics.
2. **Observable:** single robot platform evaluated; no dynamic-human evaluation despite pedestrian-rich training data; no latency numbers.
3. **Social relevance:** indirect (low-level policy reused by social systems).

## P. Adjacent analysis — see `adjacent:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue 2024 IEEE International Conference on Robotics and Automation (ICRA); DOI 10.1109/ICRA57147.2024.10610665; pages 63-70; URL https://doi.org/10.1109/ICRA57147.2024.10610665.
- Sources: Crossref (exact title match, DOI 10.1109/ICRA57147.2024.10610665); arXiv abs page (2310.07896v1).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - venue: PDF-derived 'IEEE ICRA 2024 (per citation); corpus copy arXiv v1' -> externally verified '2024 IEEE International Conference on Robotics and Automation (ICRA)'
- Changed field - pages: PDF-derived '8 (PDF); 63-70 (per citation)' -> externally verified '63-70'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified '10.1109/ICRA57147.2024.10610665'
- Changed field - url: PDF-derived 'general-navigation-models.github.io' -> externally verified 'https://doi.org/10.1109/ICRA57147.2024.10610665'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

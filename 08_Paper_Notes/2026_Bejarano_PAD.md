---
id: 2026_Bejarano_PAD
source_pdfs: [04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/3776734.3794394.pdf]
duplicate_copies: []
related_versions: []
title: 'Perception-Awareness-Decision: Socially-Aware Robot Navigation and Interaction'
authors: &id001 [Edison Jair Bejarano Sepulveda, Valerio Bo, Alberto Sanfeliu, Anais Garrell]
year: 2026
venue: Companion Proceedings of the 21st ACM/IEEE International Conference on Human-Robot Interaction (HRI 2026 Companion)
volume: NA
issue: NA
pages: 258-262
doi: 10.1145/3776734.3794394
url: https://doi.org/10.1145/3776734.3794394
pub_status: proceedings (HRI companion short paper)
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1145/3776734.3794394). PDF-derived basis (Stage 1): ACM HRI Companion ''26; received 8 Dec 2025, revised 12 Jan 2026, accepted 13 Jan 2026 (p.5). Short (5-page) companion paper; review depth of companion track unknown.'
category: S4
folder: 04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core
folder_category_match: 'Yes'
category_rationale: Uses VLM-based perception and LLM-based speech understanding/dialogue inside a situational-awareness map to decide between replanning and verbal negotiation in a corridor-blocking social navigation task, with a small participant study.
paper_type: method
fm_used: 'Yes'
fm_class: [VLM, LLM]
fm_models: ['Not reported (unnamed VLM, unnamed LLM, ASR)']
fm_size: Not reported
method_family: [SLAM, VLM perception, LLM dialogue, meta-controller (layered), Social Force Model / DWA local control]
roles: [F1, F2]
roles_evidence: {F1: 'VLM-based perception detects humans, objects, gestures and high-level scene semantics fused into a semantic contextual map (p.2).', F2: LLM-based language perception transcribes/interprets spoken input to extract intentions (p.2)., Other: LLM-driven Social Interaction Module performs clarification/negotiation dialogue (communication role).}
integration: I2
integration_rationale: FM outputs populate a semantic contextual map; a meta-controller (not stated to be an FM) selects between dialogue and navigation; motion by global planner + SFM/DWA (p.2-3).
evidence: E4
evidence_rationale: Real TIAGo++ robot in a corridor-blocking task with 8 participants (counterbalanced, informed consent) rating clarity/naturalness and preference; no statistical tests due to small sample (p.3-4).
inputs: [LiDAR, RGB (implied for VLM), speech/text, mission metadata]
outputs: [semantic labels, social state (contextual map), behaviour mode (navigate vs interact), natural-language dialogue, velocity/action (via SFM/DWA)]
human_repr: [detected human (VLM), gesture, linguistic intention, occupancy/obstacle (SLAM), projected human motion (stated in awareness layer)]
capabilities: {C1: Partial, C2: Partial, C3: Partial, C4: 'No', C5: Partial, C6: Not reported, C7: Partial, C8: 'No', C9: 'No', C10: 'No', C11: Partial, C12: Partial, C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: 'No', C18: Partial, C19: 'No', C20: 'Yes', C21: 'No', C22: Partial, C23: Partial, C24: Partial, C25: 'No'}
exp:
  datasets: []
  simulators: []
  robots: [TIAGo++ (IVO)]
  environment: indoor corridor
  indoor_outdoor: indoor
  sensors: [LiDAR, camera (implied), microphone]
  humans: real participants blocking corridor
  n_scenes: 1 scenario (corridor blocking)
  n_trajectories: 1 trial per condition per participant (3 conditions x 8)
  n_participants: '8'
  split: NA
  baselines: [P0 SLAM-only navigation (replanning)]
  ablation: Partial (P1 conservative vs P2 assertive interaction)
  real_robot_trials: 'Yes'
  human_study: 'Yes'
  statistical_testing: No (explicitly not run due to small sample)
  scenarios: [narrow corridor blocking, negotiation of passage]
metrics: [NAV | Success rate | count/8 | task success (dialogue capped at 8 turns) | p.3, NAV | Re-planning attempts (avg.) | count | number of replans | p.3, SAFETY | Stopping distance (avg.) | m | robot-human stopping distance | p.3, NAV | Trial duration (avg.) | s | trial time | p.3, OTHER | Dialogue turns (avg.) | count | dialogue turns | p.3, OTHER | Tokens per turn (avg.) | tokens | robot verbosity proxy | p.3, HUMAN | Perceived clarity | rating (scale not specified) | clarity of robot's explanation | p.3-4, HUMAN | Perceived naturalness | rating (scale not specified) | naturalness of interaction style | p.3-4, HUMAN | Preferred strategy | preference counts | preferred strategy for real-life behaviour | p.4]
deployment: {fm_model: Not reported, model_size: Not reported, api_cloud_local: Not reported, onboard_offboard: Not reported, gpu: Not reported, cpu: Not reported, latency: Not reported (VLM updates at lower frequency due to latency), query_frequency: Lower-frequency VLM updates; ASR and SLAM continuous, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Yes (stated), caching: Contextual map as compact representation, event_triggered: Dialogue triggered on sustained blockage, distillation: 'No', quantization: 'No', fallback_planner: Navigation module always available, safety_shield: LiDAR-based safety checks in navigation module, emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: No (grounding via SLAM map claimed), real_time_claim_supported: Not claimed with measurements}
repro: {code: Not reported, code_url: NA, dataset: NA, dataset_url: NA, checkpoints: NA, prompts_published: 'No', hardware_specified: Partial (robot only), hyperparameters: 'No', protocol_described: Partial, project_page: Not reported, concerns: FM models unnamed; rating scales unspecified; n=8; single scenario.}
limitations_flags: [limited-scenarios, no-human-study]
web_verification_required: []
cited_missing: ['NaviWM: Deductive CoT augmented socially-aware navigation world model (arXiv:2510.23509)', Perception-Intention-Action cycle (Dominguez-Vidal 2025), Ferrer 2017 robot companion side-by-side, Endsley 1995 situation awareness]
coding: {latency_reported: 'No', safety_mechanism: 'Yes', uncertainty_treatment: 'No', hallucination_treatment: 'No', code_released: 'No', new_dataset_released: NA, real_robot: Systematic, human_subject_study: 'Yes'}
pdf_metadata_stage1:
  year: 2026
  authors: *id001
  venue: Companion Proceedings of the 21st ACM/IEEE International Conference on Human-Robot Interaction (HRI Companion '26), Edinburgh
  volume: Not reported
  issue: Not reported
  pages: 258-262
  doi: 10.1145/3776734.3794394
  url: Not reported
  pub_status: proceedings (HRI companion short paper)
  peer_reviewed: 'Yes'
  peer_review_basis: ACM HRI Companion '26; received 8 Dec 2025, revised 12 Jan 2026, accepted 13 Jan 2026 (p.5). Short (5-page) companion paper; review depth of companion track unknown.
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: Companion Proceedings of the 21st ACM/IEEE International Conference on Human-Robot Interaction (HRI 2026 Companion)
  verified_doi: 10.1145/3776734.3794394
  verified_url: https://doi.org/10.1145/3776734.3794394
  verified_pages: 258-262
  arxiv: NA
  version_relationship: Corpus copy is the published version
  sources: ['Crossref (exact title match, DOI 10.1145/3776734.3794394)']
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A2, A5]
  C_capabilities: {SAF1: Partial, SAF2: 'Yes', SPA1: Partial, SPA2: 'No', SPA3: Partial, SPA4: 'No', HUM1: Partial, HUM2: Partial, NOR1: Partial, NOR2: Partial, NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: Partial, EXP3: 'Yes'}
  B_roles: [R1, R2, R5]
  D_interface: [D1, D8]
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'No', EV3_physical_robot: systematic, EV4_real_humans_in_trials: staged, EV5_human_evaluation: co-present participants, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: 1 trial per condition per participant (3 conditions x 8), statistical_testing: No (explicitly not run due to small sample), cross_environment: No/unclear, runtime_measured: 'No'}
  cross_cutting: {temporal_coupling: per-decision, memory: 'No', continual_adaptation: 'No', explanation_output: Yes (human-facing), safety_guard: 'Yes', uncertainty: 'No', hallucination_mitigation: 'No', privacy_constraint: 'No', inference_location: not reported}
physical_source_folder: "04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core"
analytical_category: "S4"
coding:
  latency_reported: "No"
  safety_mechanism: "Yes"
  uncertainty_treatment: "No"
  hallucination_treatment: "No"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "Systematic"
  human_subject_study: "Yes"
---

# Perception–Awareness–Decision (PAD) (Bejarano Sepulveda et al., HRI Companion 2026)

Page convention: PDF index (p.N); printed pp.258–262.

## A. Bibliographic
ACM HRI Companion '26, DOI 10.1145/3776734.3794394; IRI (UPC-CSIC) Barcelona. Received 8 Dec 2025, accepted 13 Jan 2026. Short companion paper; peer-reviewed (companion track).

## B. Position — S4 (short/preliminary)
VLM/LLM perception and dialogue embedded in a situational-awareness layer that chooses between replanning and verbal negotiation. Notable as one of few corpus papers with a participant study, but with n = 8 and unnamed models.

## C. Research problem
- **Problem:** pipelines lack semantics and fail when progress depends on human cooperation (abstract).
- **Claim:** PAD "systematically combines" SLAM with VLMs, speech recognition and LLMs "rather than simply stacking modules" (abstract); explicit intermediate representation lacking in NaviWM and SocialNav (p.2).
- **Hypotheses (p.3):** H1 higher completion/fewer proxemic violations vs geometric; H2 context-grounded dialogue → more cooperation; H3 PAD perceived more natural/appropriate.

## D. Technical method
Perception (SLAM pose/occupancy; VLM detection of humans, objects, gestures, scene semantics; LLM language perception) → Situation-awareness semantic contextual map (perception, comprehension, projection incl. human motion) → layered meta-controller → Social Interaction Module (LLM dialogue + TTS) or Navigation module (global planner + SFM or DWA with LiDAR safety checks). Asynchronous: VLM lower frequency (p.2–3). Model identities not reported.

## E. Human/social representation — detected humans, gestures, linguistic intentions in a contextual map; human-motion projection mentioned but not specified.

## F. Roles — F1, F2; communication role.

## G. Social capabilities
C20 Yes (perceived naturalness ratings) · C1/C2/C3 Partial (stopping distance; "safer distances") · C5, C7 Partial · C11, C12, C22, C23 Partial (negotiation; conservative vs assertive dialogue) · C18 Partial (clarity of explanation) · C24 Partial · others No / Not reported.

## H. Integration — I2. ## I. Evidence — E4 (small n; no statistics).

## J. Experimental evidence
TIAGo++ indoor corridor; 8 participants; one trial per condition (P0 SLAM-only; P1 conservative interaction; P2 assertive interaction), counterbalanced; dialogue capped at 8 turns; logs + post-trial ratings (p.3).

## K. Metrics — see front matter.

## L. Quantitative results (Table 1, p.3; P0 / P1 / P2)
Success rate 2/8 / 8/8 / 8/8; Re-planning attempts 7.25 / 4.71 / 4.29; Stopping distance (m) 0.70 / 0.83 / 0.79; Trial duration (s) 105.94 / 99.95 / 162.21; Dialogue turns – / 3.4 / 6.2; Tokens per turn – / 35.45 / 21.36. Subjective results only in Fig.3 bar charts (values not tabulated). Authors: "We did not run statistical tests due to the small sample size" (p.4).

## M. Deployment — models, hardware, latency not reported.

## N. Limitations
1. **Stated:** small participant sample; preliminary evidence (abstract, p.4).
2. **Future work:** richer multi-party interactions; broader decision-making behaviours (p.4).
3. **Observable:** single scenario; unnamed FMs; rating scale unspecified; H1 "proxemic violations" not directly measured (stopping distance only).
4. Deferred.

## O. Reproducibility — insufficient (models, prompts, parameters unreported).

## P. Direct-paper questions
1 Resolving a corridor blockage requiring human cooperation. 2 Semantic context and linguistic intent beyond geometry. 3 Not reported. 4 Camera + speech. 5 Not reported. 6 Semantic map entries; dialogue. 7 Meta-controller switches modes; navigation by planner+SFM/DWA. 8 No. 9 Global planner, SFM/DWA. 10 LiDAR safety checks. 11 Socially appropriate negotiation. 12 Success, replans, stopping distance, subjective clarity/naturalness/preference. 13 Yes. 14 No. 15 Yes (speech). 16 No. 17 Implicit (politeness styles). 18 Map accumulates context. 19 No. 20 No. 21 Not reported. 22 Not reported. 23 Yes. 24 Yes (n=8, no stats). 25 8/8 vs 2/8 success; larger stopping distance. 26 Cannot conclude statistical significance, generality, or which FM components matter.

## Q. Cited works possibly missing — NaviWM (arXiv:2510.23509); Perception–Intention–Action cycle; Ferrer 2017.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue Companion Proceedings of the 21st ACM/IEEE International Conference on Human-Robot Interaction (HRI 2026 Companion); DOI 10.1145/3776734.3794394; pages 258-262; URL https://doi.org/10.1145/3776734.3794394.
- Sources: Crossref (exact title match, DOI 10.1145/3776734.3794394).
- Version relationship: Corpus copy is the published version.
- Changed field - venue: PDF-derived 'Companion Proceedings of the 21st ACM/IEEE International Conference on Human-Robot Interaction (HRI Companion '26), Edinburgh' -> externally verified 'Companion Proceedings of the 21st ACM/IEEE International Conference on Human-Robot Interaction (HRI 2026 Companion)'
- Changed field - volume: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - issue: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - url: PDF-derived 'Not reported' -> externally verified 'https://doi.org/10.1145/3776734.3794394'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

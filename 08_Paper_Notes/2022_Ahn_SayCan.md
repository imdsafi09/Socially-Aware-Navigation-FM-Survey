---
id: 2022_Ahn_SayCan
source_pdfs: [03_Adjacent_Foundation_Model_Navigation/ichter23a.pdf]
duplicate_copies: []
related_versions: ['arXiv:2204.01691 (cited widely in corpus)']
title: 'Do As I Can, Not As I Say: Grounding Language in Robotic Affordances'
authors: &id001 [Brian Ichter, Anthony Brohan, Yevgen Chebotar, Chelsea Finn, Karol Hausman, Alexander Herzog, Daniel Ho, 'et al. (45 authors; PMLR v205 order, verified 2026-10-20; arXiv lists authors alphabetically from Michael Ahn)']
year: 2022
venue: Proceedings of The 6th Conference on Robot Learning (CoRL 2022), PMLR 205
volume: NA
issue: NA
pages: 287-318
doi: Not found / not applicable
url: https://proceedings.mlr.press/v205/ichter23a.html
pub_status: conference
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): PMLR proceedings page (https://proceedings.mlr.press/v205/ichter23a.html); arXiv abs page (2204.01691v2). PDF-derived basis (Stage 1): CoRL 2022 footer (p.1).'
category: S3
folder: 03_Adjacent_Foundation_Model_Navigation
folder_category_match: 'Yes'
category_rationale: LLM task planning grounded by skill value functions for a mobile manipulator (navigation + manipulation skills) in kitchens; humans only as instruction givers/recipients.
paper_type: method
fm_used: 'Yes'
fm_class: [LLM]
fm_models: [PaLM 540B (main), Universal Sentence Encoder (skill embeddings), 'FLAN / smaller PaLM variants (ablation, appendix)']
fm_size: 540B
method_family: [LLM scoring of skill descriptions, affordance grounding via RL value functions (MT-Opt), BC-Z low-level policies, few-shot prompting]
roles: [F7]
roles_evidence: {F7: 'LLM scores skill descriptions p(l|i), multiplied by affordance p(c|s,l), to select the next skill iteratively (p.2-3).'}
integration: I1
integration_rationale: FM selects among discrete skills (including 'go to <location>' navigation skills) executed by learned low-level policies.
evidence: E3
evidence_rationale: 101 real-world instructions on a mobile manipulator in mock and real office kitchens, with plan and execution success judged by three human raters (Table 2); raters judge task success, not social perception.
inputs: [natural language instruction, skill descriptions, value-function affordances from robot RGB observation]
outputs: [sequence of skills (text)]
human_repr: [user as instruction giver and delivery target ('bring it to you')]
capabilities: {C1: NA, C2: NA, C3: NA, C4: NA, C5: NA, C6: NA, C7: NA, C8: NA, C9: NA, C10: NA, C11: NA, C12: NA, C13: NA, C14: NA, C15: NA, C16: NA, C17: NA, C18: NA, C19: NA, C20: NA, C21: NA, C22: NA, C23: NA, C24: NA, C25: NA}
exp:
  datasets: [101 instructions in 7 families (crowd-sourced and designed)]
  simulators: ['Everyday Robots simulator (RL skill training, RetinaGAN sim-to-real)']
  robots: [Everyday Robots mobile manipulator (7-DoF arm)]
  environment: real office kitchen and mock kitchen; 5 locations, 15 objects
  indoor_outdoor: indoor
  sensors: [RGB]
  humans: user present as instruction giver/recipient
  n_scenes: 2 environments
  n_trajectories: 101 instructions (+21 drawer queries)
  n_participants: 3 human raters for success
  split: NA
  baselines: [No VF (LLM only), Generative (LLM + USE projection), BC NL, BC USE]
  ablation: Yes (language, value function, LLM size, prompt examples)
  real_robot_trials: 'Yes'
  human_study: No (raters judge success only)
  statistical_testing: 'No'
  scenarios: []
metrics: [OTHER | Plan success rate | % | selected skills correct for instruction (3 human raters) | p.5, OTHER | Execution success rate | % | full system performs instruction (3 human raters) | p.5]
deployment: {fm_model: PaLM 540B, model_size: 540B, api_cloud_local: Not reported (Google infrastructure), onboard_offboard: Offboard (implied), gpu: Not reported, cpu: Not reported, latency: Not reported, query_frequency: once per skill step, planner_frequency: NA, controller_frequency: Not reported, asynchronous: NA, caching: NA, event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: 'No', safety_shield: 'No', emergency_behavior: Not reported, uncertainty: Affordance probabilities (value functions) gate LLM proposals, hallucination_mitigation: Constrained scoring over admissible skills instead of free generation, real_time_claim_supported: NA}
repro: {code: 'Partial (open-sourced tabletop version, Appendix F)', code_url: say-can.github.io, dataset: 'No', dataset_url: NA, checkpoints: 'No', prompts_published: Yes (Appendix D.4), hardware_specified: Partial, hyperparameters: Partial (appendix), protocol_described: 'Yes', project_page: say-can.github.io, concerns: Proprietary LLM and robot fleet.}
limitations_flags: [resource-requirements, dataset-bias]
web_verification_required: []
cited_missing: [BC-Z, MT-Opt, PI-QT-Opt, Language models as zero-shot planners (Huang 2022), ALFRED, BEHAVIOR, Chain of Thought]
adjacent: {mechanism: Product of LLM usefulness score and learned affordance value selects next skill; iterative planning in language., relevance: 'Foundational ''LLM proposes, grounding module disposes'' architecture; analogous to VLM social reasoning filtered by feasibility/safety modules.', why_not_direct: 'No social navigation, no human-aware behaviour.', inherited_by: 'Cited by corpus VLM-Social-Nav (Song 2025), PaLM-E, NavGPT, Code as Policies, Pan review.'}
coding: {latency_reported: 'No', safety_mechanism: 'No', uncertainty_treatment: Partial, hallucination_treatment: 'Yes', code_released: Partial, new_dataset_released: NA, real_robot: Systematic, human_subject_study: Text-raters/other}
pdf_metadata_stage1:
  year: 2022
  authors: *id001
  venue: 6th Conference on Robot Learning (CoRL 2022), Auckland (PMLR; file ichter23a)
  volume: Not reported
  issue: NA
  pages: 32 (PDF incl. appendix)
  doi: Not reported
  url: say-can.github.io
  pub_status: conference
  peer_reviewed: 'Yes'
  peer_review_basis: CoRL 2022 footer (p.1).
project_url: say-can.github.io
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: Proceedings of The 6th Conference on Robot Learning (CoRL 2022), PMLR 205
  verified_doi: Not found / not applicable
  verified_url: https://proceedings.mlr.press/v205/ichter23a.html
  verified_pages: 287-318
  arxiv: 2204.01691v2
  version_relationship: Corpus copy is the PMLR published version; arXiv 2204.01691v2 alternate
  sources: ['PMLR proceedings page (https://proceedings.mlr.press/v205/ichter23a.html)', arXiv abs page (2204.01691v2)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A0]
  C_capabilities: {SAF1: NA, SAF2: NA, SPA1: NA, SPA2: NA, SPA3: NA, SPA4: NA, HUM1: NA, HUM2: NA, NOR1: NA, NOR2: NA, NOR3: NA, NOR4: NA, EXP1: NA, EXP2: NA, EXP3: NA}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: systematic, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: text-raters, EV6_open_world_deployment: 'No'}
physical_source_folder: "03_Adjacent_Foundation_Model_Navigation"
analytical_category: "S3"
coding:
  latency_reported: "No"
  safety_mechanism: "No"
  uncertainty_treatment: "Partial"
  hallucination_treatment: "Yes"
  code_released: "Partial"
  new_dataset_released: "NA"
  real_robot: "Systematic"
  human_subject_study: "Text-raters/other"
---

# SayCan (Ahn et al., CoRL 2022)

Page convention: PDF index (p.N).

## A. Bibliographic — CoRL 2022 (footer p.1); PMLR file "ichter23a". Robotics at Google, Everyday Robots. 45 authors alphabetical.

## B. Position — S3 adjacent: LLM high-level planner grounded by affordances.

## C. Research problem — LLMs lack real-world grounding; their plans may be infeasible for a given robot (p.1–2). Contribution: SayCan — combine LLM task-grounding with value-function world-grounding (p.2–3).

## D. Method — π = argmax p(c_π|s, ℓ_π)·p(ℓ_π|i); iterate until "done"; 551 skills in 7 families incl. navigation to locations; BC-Z policies and MT-Opt value functions; sparse reward; success by 2/3 human raters (p.3–5).

## L. Quantitative results (Table 2, p.7)
- Mock kitchen (plan / execute): total 84% / 74%; Real kitchen: 81% / 60%.
- By family (mock plan / execute; kitchen plan / execute): NL Single 100/100; 93/87 — NL Nouns 67/47; 60/40 — NL Verbs 100/93; 93/73 — Structured 93/87; 93/47 — Embodiment 64/55; 64/55 — Crowd-sourced 87/87; 73/60 — Long-horizon 73/47; 73/47.
- Ablations (plan): No VF 67%, Generative 74%; (execute) BC NL 0%, BC USE 9% (60% single primitives only).
- Errors: 65% LLM failures, 35% affordance failures; drawer extension 21 queries: plan 100%, execution 33% (p.7).

## N. Limitations
1. **Stated (p.8):** inherits LLM biases; bottleneck in skill range; relies on reliable affordances; LLM receives limited environment feedback.
2. **Observable:** struggles with negation and ambiguity (p.7); proprietary system; no latency reporting.
3. **Social relevance:** none directly; humans only as task recipients.

## P. Adjacent analysis — see `adjacent:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue Proceedings of The 6th Conference on Robot Learning (CoRL 2022), PMLR 205; DOI Not found / not applicable; pages 287-318; URL https://proceedings.mlr.press/v205/ichter23a.html.
- Sources: PMLR proceedings page (https://proceedings.mlr.press/v205/ichter23a.html); arXiv abs page (2204.01691v2).
- Version relationship: Corpus copy is the PMLR published version; arXiv 2204.01691v2 alternate.
- Changed field - venue: PDF-derived '6th Conference on Robot Learning (CoRL 2022), Auckland (PMLR; file ichter23a)' -> externally verified 'Proceedings of The 6th Conference on Robot Learning (CoRL 2022), PMLR 205'
- Changed field - volume: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - pages: PDF-derived '32 (PDF incl. appendix)' -> externally verified '287-318'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified 'Not found / not applicable'
- Changed field - url: PDF-derived 'say-can.github.io' -> externally verified 'https://proceedings.mlr.press/v205/ichter23a.html'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

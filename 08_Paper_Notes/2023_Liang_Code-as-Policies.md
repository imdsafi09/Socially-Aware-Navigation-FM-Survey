---
id: 2023_Liang_Code-as-Policies
source_pdfs: [03_Adjacent_Foundation_Model_Navigation/2209.07753v4.pdf]
duplicate_copies: []
related_versions: ['Published: IEEE ICRA 2023, pp. 9493-9500 (per corpus citations); corpus copy arXiv:2209.07753v4 (25 May 2023)']
title: 'Code as Policies: Language Model Programs for Embodied Control'
authors: &id001 [Jacky Liang, Wenlong Huang, Fei Xia, Peng Xu, Karol Hausman, Brian Ichter, Pete Florence, Andy Zeng]
year: 2023
venue: 2023 IEEE International Conference on Robotics and Automation (ICRA)
volume: NA
issue: NA
pages: 9493-9500
doi: 10.1109/ICRA48891.2023.10160591
url: https://doi.org/10.1109/ICRA48891.2023.10160591
pub_status: conference (corpus copy preprint)
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1109/ICRA48891.2023.10160591); arXiv abs page (2209.07753v4). PDF-derived basis (Stage 1): Corpus copy is arXiv v4 without venue; multiple corpus references cite ICRA 2023 pp.9493-9500. WEB_VERIFICATION_REQUIRED.'
category: S3
folder: 03_Adjacent_Foundation_Model_Navigation
folder_category_match: 'Yes'
category_rationale: Code-writing LLM generates robot policy code (perception-to-control logic) for manipulation, drawing and mobile navigation; no humans/social behaviour.
paper_type: method
fm_used: 'Yes'
fm_class: [LLM]
fm_models: ['OpenAI Codex code-davinci-002 (main, temperature 0)', code-cushman-001, GPT-3 6.7B, InstructGPT 175B, ViLD and MDETR (open-vocabulary detectors)]
fm_size: 6.7B-175B (Codex sizes not public)
method_family: [few-shot prompting, hierarchical code generation, language model programs]
roles: [F7, F9, F10]
roles_evidence: {F7: 'High-level LMP parses commands and sequences API calls (p.3-5, App. J).', F9: 'LMPs compute waypoint sequences/2D positions with NumPy/Shapely, e.g. move in a rectangle around a chair, follow convex hull of chairs (App. J p.14).', F10: 'LMPs can directly parameterize low-level controls (set_velocity, PD/impedance controllers; App. F).'}
integration: I5
integration_rationale: For navigation, generated code computes positions passed to goto_pos (robot's internal motion planner); direct velocity control shown only in toy/reactive examples.
evidence: E2
evidence_rationale: Quantitative evaluation only in simulated table-top manipulation (50 trials/task, Table III) and code benchmarks; real-robot drawing, manipulation and mobile navigation are qualitative demonstrations (authors state no quantitative evaluation, p.5).
inputs: [natural language command (as code comment), perception API outputs (object names/positions)]
outputs: [Python policy code calling perception/control APIs]
human_repr: [none]
capabilities: {C1: NA, C2: NA, C3: NA, C4: NA, C5: NA, C6: NA, C7: NA, C8: NA, C9: NA, C10: NA, C11: NA, C12: NA, C13: NA, C14: NA, C15: NA, C16: NA, C17: NA, C18: NA, C19: NA, C20: NA, C21: NA, C22: NA, C23: NA, C24: NA, C25: NA}
exp:
  datasets: ['RoboCodeGen (37 problems, new)', HumanEval]
  simulators: [simulated table-top (UR5e + Robotiq 2F85; from Socratic Models/Inner Monologue)]
  robots: ['UR5e (drawing, pick-and-place)', Everyday Robots mobile manipulator (office kitchen)]
  environment: table-top; real office kitchen
  indoor_outdoor: indoor
  sensors: [RGB-D (RealSense D435; robot RGBD 640x512)]
  humans: none
  n_scenes: Not reported
  n_trajectories: 50 trials per task (simulation)
  n_participants: NA
  split: seen/unseen attributes (SA/UA) and instructions (SI/UI)
  baselines: [CLIPort (30k demos), NL Planner (few-shot LLM planner in language), Flat code-gen]
  ablation: Yes (flat vs hierarchical; model size)
  real_robot_trials: Yes (qualitative only)
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: []
metrics: [OTHER | Pass rate | % | generated code passing human-written unit tests (RoboCodeGen) | p.5, OTHER | HumanEval Greedy / P@1 / P@10 / P@100 | % | code correctness | p.5, 'NAV | Task success rate | % | per task family, 50 trials per task (sim manipulation) | p.6']
deployment: {fm_model: Codex code-davinci-002 (API), model_size: Not reported, api_cloud_local: Cloud API, onboard_offboard: NA, gpu: Not reported, cpu: Not reported, latency: Not reported, query_frequency: per command, planner_frequency: NA, controller_frequency: NA, asynchronous: NA, caching: NA, event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: Robot's internal motion planner executes goto_pos, safety_shield: 'Code safety check: no imports, no __ variables, no exec/eval before exec (p.3)', emergency_behavior: Not reported, uncertainty: 'No (assumes instructions feasible; cannot tell correctness a priori, p.6)', hallucination_mitigation: 'No', real_time_claim_supported: NA}
repro: {code: 'Yes (Colab notebooks, website)', code_url: 'https://code-as-policies.github.io', dataset: RoboCodeGen (stated released), dataset_url: 'https://code-as-policies.github.io', checkpoints: NA, prompts_published: Yes (full prompts in appendix/website), hardware_specified: Partial, hyperparameters: Yes (temperature 0), protocol_described: Partial, project_page: 'https://code-as-policies.github.io', concerns: Codex API deprecated; real-robot results unquantified.}
limitations_flags: [cloud-dependence, low-level-grounding]
web_verification_required: [ICRA 2023 final version/DOI.]
cited_missing: [Socratic Models, Inner Monologue, Language models as zero-shot planners (Huang 2022), CLIPort, ViLD, MDETR]
adjacent: {mechanism: 'LLM writes executable policy code composing perception and control APIs, with hierarchical function generation.', relevance: 'Precedent for LLMs producing parameterised constraints/costs/waypoints programmatically (e.g., translating ''a bit to the left'' into numbers) — directly analogous to LLM-generated social cost/constraint code.', why_not_direct: No humans or social norms; navigation shown only qualitatively., inherited_by: Cited by corpus Cai survey and VoxPoser (adjacent); not cited by direct social-navigation notes found so far.}
coding: {latency_reported: 'No', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: 'No', code_released: 'Yes', new_dataset_released: 'Yes', real_robot: Demo, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2023
  authors: *id001
  venue: IEEE International Conference on Robotics and Automation (ICRA) 2023 (per citations); corpus copy arXiv v4
  volume: NA
  issue: NA
  pages: 16 (PDF incl. appendix); 9493-9500 (per citations)
  doi: Not reported
  url: https://code-as-policies.github.io
  pub_status: conference (corpus copy preprint)
  peer_reviewed: 'Yes'
  peer_review_basis: Corpus copy is arXiv v4 without venue; multiple corpus references cite ICRA 2023 pp.9493-9500. WEB_VERIFICATION_REQUIRED.
project_url: https://code-as-policies.github.io
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: 2023 IEEE International Conference on Robotics and Automation (ICRA)
  verified_doi: 10.1109/ICRA48891.2023.10160591
  verified_url: https://doi.org/10.1109/ICRA48891.2023.10160591
  verified_pages: 9493-9500
  arxiv: 2209.07753v4
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1109/ICRA48891.2023.10160591)', arXiv abs page (2209.07753v4)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A0]
  C_capabilities: {SAF1: NA, SAF2: NA, SPA1: NA, SPA2: NA, SPA3: NA, SPA4: NA, HUM1: NA, HUM2: NA, NOR1: NA, NOR2: NA, NOR3: NA, NOR4: NA, EXP1: NA, EXP2: NA, EXP3: NA}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: demo, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "03_Adjacent_Foundation_Model_Navigation"
analytical_category: "S3"
coding:
  latency_reported: "No"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "No"
  code_released: "Yes"
  new_dataset_released: "Yes"
  real_robot: "Demo"
  human_subject_study: "No"
---

# Code as Policies (Liang et al., ICRA 2023)

Page convention: PDF index (p.N).

## A. Bibliographic — corpus copy arXiv:2209.07753v4 (25 May 2023), Robotics at Google; cited as ICRA 2023 pp.9493–9500.

## B. Position — S3 adjacent: LLM-as-programmer for embodied control.

## C. Research problem — LLM planning over fixed skills cannot express feedback loops, commonsense control parameters or spatial relations (p.1). Contributions: CaP formulation; hierarchical code-gen (HumanEval P@1 39.8%); RoboCodeGen benchmark; generalisation/scaling ablations (p.2).

## D. Method — prompts = Hints (imports/APIs) + Examples (instruction→code); hierarchical generation of undefined functions via AST parsing; execution via exec with restricted globals after a safety check (p.3–4). Mobile robot APIs: goto_pos, goto_loc, pick_obj, say, etc. (App. J).

## L. Quantitative results
- Table I (RoboCodeGen pass rate %, Flat → Hierarchical): GPT-3 6.7B 3 → 5; GPT-3 175B 68 → 84; Codex cushman 54 → 57; Codex davinci 81 → 95.
- Table II (HumanEval, Flat → Hierarchical): Greedy 45.7 → 53.0; P@1 34.9 → 39.8; P@10 75.1 → 80.6; P@100 90.9 → 95.7.
- Table III (sim success %, CLIPort / NL Planner / CaP): SA-SI long-horizon 78.80 / 86.40 / 97.20; SA-SI spatial-geometric 97.33 / N/A / 89.30; UA-SI LH 36.80 / 88.00 / 97.60; UA-SI SG 0.00 / N/A / 73.33; UA-UI LH 0.00 / 64.00 / 80.00; UA-UI SG 0.01 / N/A / 62.00.
- Mobile navigation (App. J): qualitative commands (rectangle around chair, convex hull of chairs, search loop until banana seen) — no metrics.

## N. Limitations
1. **Stated (p.6):** limited by perception API expressiveness and available primitives; struggles with longer/different-abstraction commands; assumes feasibility; correctness unknown a priori; cross-embodiment brittle.
2. **Observable:** navigation unevaluated quantitatively; cloud-only model; no latency reporting.
3. **Social relevance:** none directly; mechanism relevant to social cost/constraint generation.

## P. Adjacent analysis — see `adjacent:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue 2023 IEEE International Conference on Robotics and Automation (ICRA); DOI 10.1109/ICRA48891.2023.10160591; pages 9493-9500; URL https://doi.org/10.1109/ICRA48891.2023.10160591.
- Sources: Crossref (exact title match, DOI 10.1109/ICRA48891.2023.10160591); arXiv abs page (2209.07753v4).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - venue: PDF-derived 'IEEE International Conference on Robotics and Automation (ICRA) 2023 (per citations); corpus copy arXiv v4' -> externally verified '2023 IEEE International Conference on Robotics and Automation (ICRA)'
- Changed field - pages: PDF-derived '16 (PDF incl. appendix); 9493-9500 (per citations)' -> externally verified '9493-9500'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified '10.1109/ICRA48891.2023.10160591'
- Changed field - url: PDF-derived 'https://code-as-policies.github.io' -> externally verified 'https://doi.org/10.1109/ICRA48891.2023.10160591'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

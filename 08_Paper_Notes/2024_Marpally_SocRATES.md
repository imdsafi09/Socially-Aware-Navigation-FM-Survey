---
id: 2024_Marpally_SocRATES
source_pdfs: [06_Datasets_Benchmarks_Evaluation/SocRATES_arXiv2412.19595v1.pdf]
duplicate_copies: []
related_versions: ['arXiv:2412.19595v1 (27 Dec 2024), title "SocRATES: Towards Automated Scenario-based Testing of Social Navigation Algorithms" = corpus copy; published version IEEE RA-L 11(11), Nov 2026 (retitled)']
title: 'SocRATES: Language-Driven Scenario Generation for Evaluating Social Navigation Algorithms'
authors: [Shashank Rao Marpally, Pranav Goyal, Harold Soh]
year: 2026
venue: IEEE Robotics and Automation Letters
volume: '11'
issue: '11'
pages: 13429-13436
doi: 10.1109/LRA.2026.3737041
url: https://doi.org/10.1109/LRA.2026.3737041
pub_status: journal (corpus copy is arXiv preprint with different title)
peer_reviewed: 'Yes'
peer_review_basis: 'Crossref record: IEEE RA-L 11(11):13429-13436 (Nov 2026), DOI 10.1109/LRA.2026.3737041, same three authors, retitled (verified 2026-10-19). Found via Crossref author+title query in Stage 2.'
category: S6
folder: 06_Datasets_Benchmarks_Evaluation
folder_category_match: 'Yes'
category_rationale: LLM/VLM pipeline (GPT-4o) that generates scenario-based tests (scenario description, behaviour trees for simulated humans, trajectories) for evaluating social-navigation algorithms in Gazebo; FM serves evaluation infrastructure.
paper_type: benchmark / evaluation tool
fm_used: 'Yes'
fm_class: [LLM, VLM]
fm_models: [GPT-4o]
fm_size: Not reported (API)
method_family: [structured prompting, behaviour-tree generation, scenario-based testing]
roles: [F11]
roles_evidence: {F11: LLM generates social-navigation test scenarios and human behaviours (p.4).}
integration: I1
integration_rationale: FM used offline to author test scenarios; not in the robot control loop.
evidence: E2
evidence_rationale: Generated scenarios executed in simulation (Gazebo/HuNavSim) against navigation stacks; usability study with five researchers.
inputs: [map image, rough scenario description]
outputs: [scenario specification, behaviour trees, human trajectories]
human_repr: [simulated humans driven by behaviour trees]
capabilities: {C1: 'No', C2: 'No', C3: 'No', C4: 'No', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: Partial, C12: 'No', C13: 'No', C14: 'No', C15: 'No', C16: 'No', C17: 'No', C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: 'No', C24: Partial, C25: 'No'}
exp:
  datasets: Not reported
  simulators: [Gazebo with HuNavSim-style humans]
  robots: Not reported
  environment: Not reported
  indoor_outdoor: Not reported
  sensors: Not reported
  humans: Not reported
  n_scenes: 20 scenarios per location (unguided); 5 scenarios x 10 (guided)
  n_trajectories: Not reported
  n_participants: 5 researchers (usability)
  split: Not reported
  baselines: [naive prompting system]
  ablation: Yes (structured prompting)
  real_robot_trials: 'No'
  human_study: Usability study of the tool (not robot behaviour)
  statistical_testing: 'No'
  scenarios: Not reported
metrics: ['OTHER | Scenario generation success | % | simulable, appropriate, aligned: 55% unguided / 73% guided | p.4', DEPLOY | Generation time / cost | s / USD | 43 s per scenario; <0.30 USD per trial | p.4]
deployment: {fm_model: GPT-4o, model_size: Not reported, api_cloud_local: Cloud API, onboard_offboard: Not reported, gpu: Not reported, cpu: Not reported, latency: 43 s per generated scenario (offline), query_frequency: Not reported, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Not reported, caching: Not reported, event_triggered: Not reported, distillation: Not reported, quantization: Not reported, fallback_planner: Not reported, safety_shield: Not reported, emergency_behavior: Not reported, uncertainty: Not reported, hallucination_mitigation: Not reported, real_time_claim_supported: Not reported}
repro: {code: Not reported, code_url: Not reported, dataset: Not reported, dataset_url: Not reported, checkpoints: Not reported, prompts_published: Not reported, hardware_specified: Not reported, hyperparameters: Not reported, protocol_described: Not reported, project_page: Not reported, concerns: Not reported}
limitations_flags: [cloud-dependence]
web_verification_required: []
cited_missing: [HuNavSim]
dataset: {kind: benchmark/evaluation tool, real_synthetic: synthetic, closed_loop: Yes (simulation), language_ann: Yes (scenario text), vlm_suitability: NA (FM is the generator), known_limitations: Scenario validity checked manually; LLM behaviour-tree errors.}
external_verification: {verified_on: '2026-10-19', status_class: 'A: published, peer-reviewed', source: Crossref DOI 10.1109/LRA.2026.3737041 (title differs from arXiv v1), arxiv_id: 2412.19595v1, version_relationship: arXiv v1 (different title) is the corpus copy; RA-L version authoritative}
stage2: {added: true, download_source: 'https://arxiv.org/pdf/2412.19595v1', source_type: arXiv, inclusion_reason: FM-based evaluation infrastructure for social navigation (F11).}
coding: {latency_reported: 'Yes', safety_mechanism: NA, uncertainty_treatment: 'No', hallucination_treatment: Partial, code_released: 'No', new_dataset_released: NA, real_robot: 'No', human_subject_study: 'No'}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1]
  C_capabilities: {SAF1: 'No', SAF2: 'No', SPA1: 'No', SPA2: 'No', SPA3: 'No', SPA4: 'No', HUM1: 'No', HUM2: 'No', NOR1: Partial, NOR2: 'No', NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: none, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "06_Datasets_Benchmarks_Evaluation"
analytical_category: "S6"
coding:
  latency_reported: "Yes"
  safety_mechanism: "NA"
  uncertainty_treatment: "No"
  hallucination_treatment: "Partial"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "No"
  human_subject_study: "No"
---

# SocRATES (Marpally, Goyal, Soh; IEEE RA-L 2026)

## A. Bibliographic
Externally verified: IEEE RA-L 11(11):13429-13436 (Nov 2026), DOI 10.1109/LRA.2026.3737041, published under the title "SocRATES: Language-Driven Scenario Generation for Evaluating Social Navigation Algorithms". PDF-derived: corpus copy is arXiv:2412.19595v1 (27 Dec 2024) with the title "SocRATES: Towards Automated Scenario-based Testing of Social Navigation Algorithms". National University of Singapore. Peer-reviewed: Yes. Results below are from the arXiv copy; the published version may differ.

## B. Position
S6 (FM for evaluation, F11): LLMs automate scenario-based testing of social navigation. Before Cai cut-off; not cited by Cai.

## L. Results
55% (unguided) / 73% (guided) first-response success vs naive system lower; 43 s per scenario; five researchers preferred SocRATES to manual scenario authoring.

## N. Limitations
Observable: manual validity judgement; no comparison of resulting navigation rankings with human judgement.

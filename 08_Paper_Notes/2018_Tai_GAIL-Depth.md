---
id: 2018_Tai_GAIL-Depth
source_pdfs: [02_Learning_Based_Social_Navigation/1710.02543v2.pdf]
duplicate_copies: []
related_versions: ['Published: IEEE ICRA 2018 (per SEAN reference list); corpus copy arXiv:1710.02543v2 (26 Feb 2018)']
title: Socially Compliant Navigation through Raw Depth Inputs with Generative Adversarial Imitation Learning
authors: &id001 [Lei Tai, Jingwei Zhang, Ming Liu, Wolfram Burgard]
year: 2018
venue: 2018 IEEE International Conference on Robotics and Automation (ICRA)
volume: NA
issue: NA
pages: 1111-1117
doi: 10.1109/ICRA.2018.8460968
url: https://doi.org/10.1109/ICRA.2018.8460968
pub_status: conference (corpus copy preprint)
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1109/ICRA.2018.8460968); arXiv abs page (1710.02543v2). PDF-derived basis (Stage 1): Corpus copy arXiv v2; SEAN (corpus) cites it as ICRA 2018; dataset URL ''tai_18icra_dataset''. WEB_VERIFICATION_REQUIRED.'
category: S2
folder: 02_Learning_Based_Social_Navigation
folder_category_match: 'Yes'
category_rationale: Behaviour cloning + WGAN-GAIL policy from raw depth images imitating social-force-model demonstrations; released Gazebo pedestrian plugin and dataset.
paper_type: method; dataset
fm_used: 'No'
fm_class: [None]
fm_models: []
fm_size: NA
method_family: [behaviour cloning, GAIL (WGAN + TRPO), multi-task learning (social-force prediction), asynchronous multi-scenario training]
roles: []
roles_evidence: {}
integration: NA
integration_rationale: No foundation model.
evidence: E2
evidence_rationale: Quantitative evaluation in Gazebo (10 test episodes per scenario, six scenarios; normalized min-dist and travel-time box plots); real-world Turtlebot deployment shown only qualitatively/video.
inputs: [raw depth image (400x250), desired-force vector to goal]
outputs: [velocity command (2-D), auxiliary social-force prediction]
human_repr: [implicit in depth image; expert labels from social force model]
capabilities: {C1: Partial, C2: Partial, C3: Partial, C4: 'No', C5: 'No', C6: 'No', C7: 'No', C8: 'No', C9: Partial, C10: 'No', C11: 'No', C12: 'No', C13: Partial, C14: 'No', C15: 'No', C16: 'No', C17: 'No', C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: 'No', C24: 'No', C25: 'No'}
exp:
  datasets: ['Released dataset: 10,000 state-action pairs from social-force simulation (2,000 held out)']
  simulators: [Gazebo with social-force pedestrian plugin (released)]
  robots: [Turtlebot3 waffle (sim and real; RealSense R200; Jetson TX2)]
  environment: simulated scenarios; real indoor office
  indoor_outdoor: indoor
  sensors: [depth camera, 'low-cost laser (localization, real)']
  humans: simulated social-force pedestrians (reactive to robot); real office occupants (qualitative)
  n_scenes: 6 scenarios (passing, overtaking, crossing; passing out of group, passing between group, crossing with group)
  n_trajectories: 10 test episodes per scenario per policy
  n_participants: NA
  split: 8,000 / 2,000 samples for BC
  baselines: [Behaviour cloning (BC)]
  ablation: 'No'
  real_robot_trials: Partial (demonstration)
  human_study: 'No'
  statistical_testing: 'No'
  scenarios: [passing, overtaking, crossing, group passing, group crossing]
metrics: ['SAFETY | min-dist (average minimum distance ratio) | ratio to BC mean | minimal robot-pedestrian distance per episode, normalized by BC | p.6-7', NAV | travel-time (average travel time ratio) | ratio to BC mean | start-to-target time normalized by BC | p.6-7]
deployment: {fm_model: NA, model_size: Not reported, api_cloud_local: NA, onboard_offboard: Onboard (Jetson TX2), gpu: 'Jetson TX2 (deploy); Tesla P100 (training, 10 h)', cpu: Not reported, latency: 15 Hz control cycle, query_frequency: 15 Hz, planner_frequency: NA, controller_frequency: 15 Hz, asynchronous: NA, caching: NA, event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: 'No', safety_shield: 'No', emergency_behavior: Not reported, uncertainty: NA, hallucination_mitigation: NA, real_time_claim_supported: 'Yes'}
repro: {code: Yes (simulator plugin), code_url: 'https://github.com/onlytailei/gym_ped_sim', dataset: 'Yes', dataset_url: 'https://ram-lab.com/file/tailei/tai_18icra_dataset.html', checkpoints: Not reported, prompts_published: NA, hardware_specified: 'Yes', hyperparameters: 'Partial (RMSprop lrs, 300 GAIL iterations)', protocol_described: Partial, project_page: NA, concerns: Expert is the social force model itself; results only normalized box plots.}
limitations_flags: [sim-to-real, no-human-study, limited-scenarios]
web_verification_required: [ICRA 2018 publication details.]
cited_missing: [Pfeiffer IROS 2016 predicting actions to act predictably, InfoGAIL, GAIL (Ho & Ermon), Tai virtual-to-real DRL (IROS 2017)]
learning: {type: IL (BC pretraining + WGAN-GAIL with TRPO), state_repr: raw depth image + desired-force vector, human_repr: implicit (pixels); social force as auxiliary label, reward_design: discriminator score as cost + augmented collision penalty, social_reward: Implicit (imitating social-force expert), prediction_model: 'No', group_modeling: Partial (group passing scenarios in data; no explicit group model), training_env: 'Gazebo social-force simulation, 6 scenarios sampled asynchronously', sim_dependence: High, interpretability: Low, generalization: Six scripted scenarios; real office demo, real_world_validation: Qualitative only, social_metrics: Normalized min distance only}
coding: {latency_reported: 'Yes', safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: 'Yes', new_dataset_released: 'Yes', real_robot: Demo, human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2018
  authors: *id001
  venue: IEEE ICRA 2018 (per citation); corpus copy arXiv v2
  volume: NA
  issue: NA
  pages: 7 (PDF)
  doi: Not reported
  url: https://github.com/onlytailei/gym_ped_sim
  pub_status: conference (corpus copy preprint)
  peer_reviewed: 'Yes'
  peer_review_basis: Corpus copy arXiv v2; SEAN (corpus) cites it as ICRA 2018; dataset URL 'tai_18icra_dataset'. WEB_VERIFICATION_REQUIRED.
project_url: https://github.com/onlytailei/gym_ped_sim
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: 2018 IEEE International Conference on Robotics and Automation (ICRA)
  verified_doi: 10.1109/ICRA.2018.8460968
  verified_url: https://doi.org/10.1109/ICRA.2018.8460968
  verified_pages: 1111-1117
  arxiv: 1710.02543v2
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1109/ICRA.2018.8460968)', arXiv abs page (1710.02543v2)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A6]
  C_capabilities: {SAF1: Partial, SAF2: Partial, SPA1: Partial, SPA2: Partial, SPA3: Partial, SPA4: 'No', HUM1: 'No', HUM2: 'No', NOR1: 'No', NOR2: 'No', NOR3: 'No', NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: NA (not a direct FM social-navigation method)
  D_interface: NA
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'Yes', EV3_physical_robot: demo, EV4_real_humans_in_trials: not coded (non-direct work), EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
physical_source_folder: "02_Learning_Based_Social_Navigation"
analytical_category: "S2"
coding:
  latency_reported: "Yes"
  safety_mechanism: "NA"
  uncertainty_treatment: "NA"
  hallucination_treatment: "NA"
  code_released: "Yes"
  new_dataset_released: "Yes"
  real_robot: "Demo"
  human_subject_study: "No"
---

# GAIL from Raw Depth (Tai, Zhang, Liu, Burgard — ICRA 2018)

Page convention: PDF index (p.N).

## A. Bibliographic — corpus copy arXiv:1710.02543v2 (26 Feb 2018); HKUST, Univ. Freiburg; cited as ICRA 2018 by SEAN.

## B. Position — S2: early end-to-end perception-to-action social navigation; expert = social force model.

## C. Research problem — prior social navigation requires precise pedestrian state from expensive sensors; BC ignores temporal correlation (p.1–2). Contributions: GAIL approach from raw depth; Gazebo social-force plugin and 10k-pair dataset (p.2).

## D. Method — social force model (Eq.3) labels depth frames; generator: three-stream conv network (incl. pretrained ResNet-50) with action + social-force heads; discriminator: conv stream + desired force + action; WGAN objective (Eq.2), TRPO updates, weight clipping ±0.01; asynchronous sampling over six scenarios; collision penalty added (p.2–5).

## L. Quantitative results — Fig.7 only (box plots normalized by BC mean; no numeric tables): GAIL larger average min-dist in all six scenarios; travel time lower in most scenarios but slightly slower in two easy scenarios (p.7). Real robot: 15 Hz on Jetson TX2, qualitative video.
- **Data-quality note:** scenario definitions (p.3: (d) passing *out of* a group, (e) passing *between* a group) are swapped in the qualitative discussion (p.5: "pass in between (d) and travel out of (e)").

## N. Limitations
1. **Stated (p.7):** limited max speed and FOV of Turtlebot; future evaluation on other platforms; RGB via real-to-sim adaptation.
2. **Observable:** expert is a hand-crafted model, so "social compliance" is bounded by social-force behaviour; no absolute metrics; no statistics; real-world unquantified.
3. **Social relevance:** includes group scenarios, but group handling is not quantified.

## P. Learning-based analysis — see `learning:` block.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue 2018 IEEE International Conference on Robotics and Automation (ICRA); DOI 10.1109/ICRA.2018.8460968; pages 1111-1117; URL https://doi.org/10.1109/ICRA.2018.8460968.
- Sources: Crossref (exact title match, DOI 10.1109/ICRA.2018.8460968); arXiv abs page (1710.02543v2).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - venue: PDF-derived 'IEEE ICRA 2018 (per citation); corpus copy arXiv v2' -> externally verified '2018 IEEE International Conference on Robotics and Automation (ICRA)'
- Changed field - pages: PDF-derived '7 (PDF)' -> externally verified '1111-1117'
- Changed field - doi: PDF-derived 'Not reported' -> externally verified '10.1109/ICRA.2018.8460968'
- Changed field - url: PDF-derived 'https://github.com/onlytailei/gym_ped_sim' -> externally verified 'https://doi.org/10.1109/ICRA.2018.8460968'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

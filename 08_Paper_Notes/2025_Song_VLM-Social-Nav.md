---
id: 2025_Song_VLM-Social-Nav
source_pdfs: [04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/vlm_social_nav.pdf]
duplicate_copies: []
related_versions: ['arXiv:2404.00210 technical report (cited as [20], p.8) - not in corpus']
title: 'VLM-Social-Nav: Socially Aware Robot Navigation Through Scoring Using Vision-Language Models'
authors: &id001 [Daeun Song, Jing Liang, Amirreza Payandeh, Amir Hossain Raj, Xuesu Xiao, Dinesh Manocha]
year: 2025
venue: IEEE Robotics and Automation Letters
volume: '10'
issue: '1'
pages: 508-515
doi: 10.1109/LRA.2024.3511409
url: https://doi.org/10.1109/LRA.2024.3511409
pub_status: journal
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1109/LRA.2024.3511409); arXiv abs page (2404.00210v3). PDF-derived basis (Stage 1): Received 6 Jul 2024, accepted 21 Nov 2024, recommended by Associate Editor upon evaluation of reviewers'' comments (p.1).'
category: S4
folder: 04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core
folder_category_match: 'Yes'
category_rationale: Peer-reviewed method in which a VLM (GPT-4V) reasons about a social scene and its output becomes a social cost in a closed-loop local planner on a real robot.
paper_type: method
fm_used: 'Yes'
fm_class: [VLM]
fm_models: [GPT-4V]
fm_size: Not reported
method_family: [prompting, zero-shot, cost-based local planning (DWA), object detection (YOLO)]
roles: [F1, F2, F4, F6]
roles_evidence: {F1: VLM describes the scene (e.g. person walking toward camera on sidewalk) before recommending action (p.7)., F2: 'Only for explicit hand gestures: VLM interprets a stop gesture and robot yields (p.5-6); no general intention inference.', F4: 'Prompt includes walking-etiquette rules (''Move to the right when passing by a person'', ''Do not obstruct others'' paths''); VLM outputs rule-consistent action (Fig.3, p.4).', F6: 'VLM answer ''Move DIRECTION with SPEED'' is mapped to (v_h, w_h) and converted into C_social = w_l|v-v_h| + w_a|w-w_h| added to DWA cost (Eq.1-4, p.3-4).'}
integration: I4
integration_rationale: VLM output is converted to a social cost term inside the optimisation-based local planner (DWA); the planner selects (v*,w*) (Eq.1-4, Alg.1, p.3-4).
evidence: E4
evidence_rationale: Closed-loop real-robot experiments (Turtlebot 2, 4 indoor scenarios, 21 runs each) with a participant questionnaire study (7 participants per scenario, 5-point Likert) (p.5-7); no statistical testing.
inputs: [RGB, LiDAR, odometry, goal pose, current robot action, natural language prompt]
outputs: [natural-language action (direction+speed), cost, velocity/action (via DWA)]
human_repr: [moving obstacle (LiDAR), 'detected social entity (YOLO bounding box: human/gesture/door)', semantic description (VLM text), natural-language social rule (prompt)]
capabilities: {C1: 'Yes', C2: Partial, C3: Partial, C4: Partial, C5: Partial, C6: 'No', C7: Partial, C8: 'No', C9: 'No', C10: 'No', C11: 'Yes', C12: 'Yes', C13: 'Yes', C14: 'Yes', C15: 'No', C16: 'No', C17: 'No', C18: Partial, C19: Not reported, C20: Not reported, C21: Partial, C22: Not reported, C23: Partial, C24: Partial, C25: 'No'}
exp:
  datasets: [MuSoHu image used for prompt example only (Fig.3), SCAND (to train BC baseline)]
  simulators: []
  robots: [Turtlebot 2]
  environment: indoor lab/building (frontal approach, intersection, doorway)
  indoor_outdoor: indoor
  sensors: [Velodyne VLP16 LiDAR, Zed 2i camera, odometry]
  humans: real participants (single human per scenario)
  n_scenes: 4 scenarios
  n_trajectories: 21 runs per method per scenario
  n_participants: 7 per scenario
  split: NA
  baselines: [DWA (no social cost), Behavior Cloning trained on SCAND]
  ablation: 'No'
  real_robot_trials: 'Yes'
  human_study: 'Yes'
  statistical_testing: No (means ± std/SE only)
  scenarios: [frontal approach (passing), frontal approach with stop gesture, intersection (crossing), narrow doorway]
metrics: [NAV | Success Rate | % | reaches goal; for gesture scenario success = robot reacts to gesture | p.5, 'SAFETY | Collision Rate | % | collision with human/objects, including manual intervention to avoid imminent collision | p.5', HUMAN | User Study Score | 5-point Likert (reverse-coded negatives) | average agreement over scenario-specific social-compliance questionnaire (Table II) | p.6-7]
deployment: {fm_model: GPT-4V, model_size: Not reported, api_cloud_local: 'Cloud (GPT-4V; API use implied, not explicitly stated)', onboard_offboard: 'Laptop on robot (Intel i7, RTX 2080) runs perception/planner; VLM remote', gpu: Nvidia GeForce RTX 2080 (laptop), cpu: Intel i7, latency: '~3 s average VLM inference; 2-3 s average response after prompt formatting (p.5, p.7)', query_frequency: Event-triggered only when YOLO detects social entities, planner_frequency: Not reported, controller_frequency: Not reported, asynchronous: Not reported, caching: Not reported, event_triggered: Yes (YOLO social-cue trigger), distillation: 'No', quantization: 'No', fallback_planner: DWA goal+obstacle cost always active; social cost zero when no social entity, safety_shield: DWA obstacle cost (LiDAR); VLM only adds a cost term, emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: 'Partial: VLM output used only as cost term because ''VLMs can still make mistakes'' (p.7); constrained
    answer format', real_time_claim_supported: 'Partial: claims real-time decisions; measured VLM latency 2-3 s; no control-loop rate reported'}
repro: {code: Not reported, code_url: Not reported, dataset: No new dataset, dataset_url: NA, checkpoints: NA, prompts_published: 'Partial (one example prompt, Fig.3)', hardware_specified: 'Yes', hyperparameters: 'No (cost weights alpha,beta,gamma,w_l,w_a not given)', protocol_described: Partial (scenarios + questionnaire given), project_page: Not reported (supplementary video at DOI), concerns: Closed commercial model; cost weights unreported; 7 participants; no statistics.}
limitations_flags: [latency, cloud-dependence, limited-scenarios, hallucination, spatial-reasoning-failure]
web_verification_required: []
cited_missing: [SACSoN, MuSoHu, THOR, Pirk 2022 protocol for validating social navigation policies, PIVOT, MOKA, Tsoi 2024 How do robot experts measure success, OF-VO, Crowd-steer]
coding: {latency_reported: 'Yes', safety_mechanism: 'Yes', uncertainty_treatment: 'No', hallucination_treatment: Partial, code_released: 'No', new_dataset_released: NA, real_robot: Systematic, human_subject_study: 'Yes'}
pdf_metadata_stage1:
  year: 2025
  authors: *id001
  venue: IEEE Robotics and Automation Letters
  volume: '10'
  issue: '1'
  pages: 508-515
  doi: 10.1109/LRA.2024.3511409
  url: Not reported
  pub_status: journal
  peer_reviewed: 'Yes'
  peer_review_basis: Received 6 Jul 2024, accepted 21 Nov 2024, recommended by Associate Editor upon evaluation of reviewers' comments (p.1).
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: IEEE Robotics and Automation Letters
  verified_doi: 10.1109/LRA.2024.3511409
  verified_url: https://doi.org/10.1109/LRA.2024.3511409
  verified_pages: 508-515
  arxiv: 2404.00210v3
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1109/LRA.2024.3511409)', arXiv abs page (2404.00210v3)]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A1, A5]
  C_capabilities: {SAF1: 'Yes', SAF2: Partial, SPA1: Partial, SPA2: 'No', SPA3: 'Yes', SPA4: 'No', HUM1: Partial, HUM2: Partial, NOR1: 'Yes', NOR2: Partial, NOR3: Partial, NOR4: 'No', EXP1: 'Yes', EXP2: Partial, EXP3: 'No'}
  B_roles: [R1, R3]
  D_interface: [D3]
  E_evidence_profile: {EV1_offline: 'No', EV2_closed_loop_sim: 'No', EV3_physical_robot: systematic, EV4_real_humans_in_trials: staged, EV5_human_evaluation: co-present participants, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: 21 runs per method per scenario, statistical_testing: No (means ± std/SE only), cross_environment: No/unclear, runtime_measured: 'Yes'}
  cross_cutting: {temporal_coupling: per-decision, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'Yes', uncertainty: 'No', hallucination_mitigation: Partial, privacy_constraint: 'No', inference_location: cloud API}
physical_source_folder: "04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core"
analytical_category: "S4"
coding:
  latency_reported: "Yes"
  safety_mechanism: "Yes"
  uncertainty_treatment: "No"
  hallucination_treatment: "Partial"
  code_released: "No"
  new_dataset_released: "NA"
  real_robot: "Systematic"
  human_subject_study: "Yes"
---

# VLM-Social-Nav: Socially Aware Robot Navigation Through Scoring Using Vision-Language Models (Song et al., RA-L 2025)

Page convention: PDF page index (p.N). PDF pages 1–8 = printed pp. 508–515.

## A. Bibliographic information
- Source: `04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/vlm_social_nav.pdf`
- Song, Liang, Payandeh, Raj, Xiao, Manocha. IEEE RA-L 10(1):508–515, Jan 2025. DOI 10.1109/LRA.2024.3511409. Received 6 Jul 2024; accepted 21 Nov 2024 (p.1).
- Journal; **peer-reviewed: Yes**. Technical report version arXiv:2404.00210 cited as [20] (not in corpus).

## B. Position
**S4 — direct VLM social navigation.** A VLM is queried about a human-populated scene and its socially motivated recommendation is converted into a cost term executed closed-loop on a real robot. One of the earliest peer-reviewed VLM-in-the-loop social-navigation systems in the corpus.

## C. Research problem
- **Problem:** socially compliant, context-appropriate navigation without large training datasets/reward engineering (p.1–2).
- **Motivation (authors):** IL/RL need large datasets and generalise poorly; LLMs/VLMs have contextual/commonsense reasoning but high latency (p.2).
- **Claimed novelty:** "VLMs have not yet been applied to the social navigation problem" (p.2); VLM-based scoring module translating observation + instructions into a social cost (p.2).
- **Contributions (authors):** (1) VLM-Social-Nav integrating VLMs with optimisation/scoring planners + perception model for efficiency; (2) VLM-based scoring module → social cost; (3) real-world evaluation in 4 indoor scenarios + user study vs DWA and BC (SCAND) (p.2).
- **Our interpretation:** the VLM produces a discrete heading/speed recommendation; "social cost" is deviation from that recommendation, i.e. the VLM acts as a reference-action generator whose influence is mediated by cost weighting.

## D. Technical method
- **Pipeline (Fig.2, Alg.1, p.4):** RGB → YOLO detects social entities (humans, gestures, doors) → if detected, query GPT-4V with image I_t, prompt P, current action a_t → answer "Move DIRECTION with SPEED" (DIRECTION ∈ {left, straight, right}; SPEED ∈ {slow down, speed up, constant, stop}) → map to (v_h, w_h): v_h = v_t + δ_s, w_h = δ_d → C_social = w_l‖v − v_h‖ + w_a‖w − w_h‖ (Eq.4) → DWA minimises C = α C_goal + β C_obst + γ C_social (Eq.1) over sampled (v,w).
- Problem as MDP ⟨S,A,T,C⟩, s=(x,y,θ), a=(v,w) (p.3). C_social = B − B_h, B_h behaviour humans would adopt (Eq.2).
- **Model:** GPT-4V (chosen after a preliminary comparison with other large/small VLMs — details not given, p.5). Zero-shot prompting with etiquette reminders ("in-context learning ... through zero-shot examples", p.3). No fine-tuning, no RL/IL for the proposed method.
- **Perception:** YOLO; LiDAR for obstacles. Localization/mapping: odometry (Fig.2); no mapping detail. Human tracking/trajectory prediction: none. Global planner: not described. Local planner: DWA. Controller: DWA velocity output.
- **INPUT:** RGB, 3D LiDAR, odometry, goal pose, current (v,w), language prompt. **OUTPUT:** natural-language action (direction/speed) → cost → velocity.

## E. Human/social representation
LiDAR obstacle (geometric) for collision avoidance; YOLO detection of humans/gestures/doors as event trigger; VLM's implicit semantic interpretation of the image; prompt-encoded natural-language social rules (keep right, do not obstruct). No personal-space model, no trajectory prediction, no group model.

## F. Functional roles
F1, F2 (gesture only), F4, F6 — see front matter evidence. Not F5 (no candidate scoring), not F9/F10 (output only biases DWA).

## G. Social capabilities (evaluated vs claimed)
| C | Status | Evidence |
|---|---|---|
| C1 collision | Yes | Collision Rate, Table I (p.6) |
| C2 near-collision | Partial | manual interventions counted as collisions (p.5) |
| C3 proxemics | Partial | questionnaire "safe and comfortable distance" only (Table II) |
| C4 perceived safety | Partial | same questionnaire items |
| C5 human motion understanding | Partial | qualitative (passes behind crossing human, p.5) |
| C6 prediction | No | |
| C7 intention | Partial | stop-gesture only |
| C11 etiquette | Yes | keep-right / do-not-obstruct evaluated qualitatively + questionnaire |
| C12 yielding | Yes | gesture stop, doorway waiting, intersection |
| C13 passing convention | Yes | keep right in frontal approach (p.5) |
| C14 doorway | Yes | narrow doorway scenario |
| C18 legibility | Partial | Q "It was clear what the robot wanted to do" |
| C21 comfort | Partial | "comfortable distance" item |
| C23 social instruction | Partial | gesture command followed; prompt-rule switching claimed, not tested |
| C24 context-dependent | Partial | different behaviour per scenario |
| C25 cultural adaptation | No | rephrasing for left-walking countries claimed (p.4, p.8), not evaluated |
| C9/C10 group | No | only anecdotal remark (p.7) |
| C15–C17 | No | indoor single-person only |
| C19, C20, C22 | Not reported | |

## H. Integration level — I4 (cost generation). See front matter.

## I. Evidence maturity — E4. Real robot + participant questionnaire; small scale (7 participants/scenario), no statistics, single-person indoor scenarios.

## J. Experimental evidence
- Robot: Turtlebot 2; Velodyne VLP16, Zed 2i; laptop i7 + RTX 2080 (p.5). Indoor. Real humans (participants walking predefined trajectories).
- Scenarios: frontal approach; frontal approach with gesture; intersection; narrow doorway (p.5).
- Baselines: DWA without C_social; BC [ALVINN-style] trained on SCAND (p.5).
- 21 runs per method per scenario (p.5). User study: 7 participants per scenario, 3 methods randomly shuffled, repeated 3 times, 5-point Likert (p.6).
- No ablation (e.g., no VLM vs smaller VLM, no prompt ablation). No statistical tests.

## K. Metrics — Success Rate (%), Collision Rate (%), User Study Score (Likert). Definitions p.5.

## L. Quantitative results (Table I, p.6; values visually verified from rendered page)
| Metric | Method | Frontal | Frontal+Gesture | Intersection | Narrow Doorway |
|---|---|---|---|---|---|
| Success Rate (%) ↑ | BC | 38.10 | 0 | 33.33 | 42.86 |
| | DWA | 100 | 0 | 90.48 | 100 |
| | VLM-Social-Nav | 100 | 100 | 100 | 100 |
| Collision Rate (%) ↓ | BC | 42.86 | 66.67 | 28.57 | 38.10 |
| | DWA | 28.57 | 19.05 | 19.05 | 38.10 |
| | VLM-Social-Nav | 14.29 | 0 | 4.76 | 9.52 |
| User Study Score ↑ | BC | 2.80 ± 1.45 | 2.23 ± 1.54 | 2.80 ± 1.40 | 2.60 ± 1.33 |
| | DWA | 3.99 ± 0.80 | 3.38 ± 0.64 | 3.57 ± 0.62 | 3.59 ± 0.83 |
| | VLM-Social-Nav | 4.31 ± 0.72 | 4.28 ± 0.56 | 4.35 ± 0.70 | 4.04 ± 0.74 |
- Abstract/text: "at least 27.38% improvement in the average success rate and 19.05% improvement in the average collision rate" (p.1, p.6). Per-question averages in Fig.5 (p.7).
- Note: the gesture scenario success definition (reacts to gesture) differs from goal reaching; DWA and BC cannot by construction react to gestures.

## M. Deployment
GPT-4V (cloud; size not reported); ~3 s average inference; 2–3 s average response after prompt formatting and predefined choices (p.5, p.7); event-triggered querying via YOLO; DWA always active; no async scheme, caching, quantization or uncertainty estimate described. "Real-time" claim is not supported by a control-loop timing measurement; VLM latency is several seconds.

## N. Limitations
1. **Stated by authors:** large VLMs need several seconds — problematic in more dynamic scenarios (p.7); VLMs "can still make mistakes", so relying solely on VLMs is not safe (p.7); experiments indoor only (p.7); with multiple groups, left/right directions may not suffice (p.7); interpreting social rules from raw perception remains complex (p.8).
2. **Future work:** outdoor/global navigation; multiple individuals/groups; visual prompting (PIVOT, MOKA) for spatial reasoning; open-source VLMs (LLaVA) using log-probabilities to detect hallucinations; CoT high-level instruction VLM (p.7–8).
3. **Observable constraints:** single-person scenarios; 7 participants; no statistical testing; cost weights unreported; no prompt/VLM ablation; collision rates for DWA (up to 38.10%) are high for an indoor lab baseline — tuning of baseline not described; closed model.
4. **Survey-level interpretation:** deferred.

## O. Reproducibility
Code: not reported. Prompt: one example (Fig.3). Hardware: yes. Weights: not given. Supplementary video at DOI.

## P. Direct-paper questions (26)
1. Problem: socially compliant local navigation in single-human indoor encounters (passing, gesture, crossing, doorway).
2. Why FM: contextual/common-sense interpretation without large datasets (p.2).
3. Model: GPT-4V.
4. Observes: robot-view RGB image + current action.
5. Prompt: task + ego state (heading, linear velocity) + "Remember" etiquette rules + answer format (Fig.3).
6. Output: "Move DIRECTION with SPEED".
7. Conversion: mapped to (v_h, w_h) → cost deviation term in DWA.
8. Direct control: No.
9. Outside model: YOLO, DWA local planner, LiDAR obstacle cost.
10. Safety layer: DWA obstacle cost; VLM only biases cost.
11. Claimed: socially compliant, context-aware, culturally adaptable via prompt.
12. Evaluated: success, collision, questionnaire-rated compliance in 4 single-person indoor scenarios.
13. Individual humans: yes (single). 14. Groups: no. 15. Intention: gesture only. 16. Activity: no. 17. Norms: yes (prompted). 18. Temporal context: no (single image). 19. Uncertainty: no. 20. Hallucination: acknowledged, mitigated only by cost-term design. 21. Real-time: VLM 2–3 s; event-triggered. 22. Onboard: perception/planning onboard laptop; VLM cloud. 23. Real humans: yes. 24. Formal human study: questionnaire, 7 participants/scenario, no statistics.
25. Quantitative support: higher success, lower collision, higher Likert vs DWA/BC (Table I).
26. Cannot conclude: generalisation to crowds/groups/outdoor; statistical significance of user-study differences; contribution of GPT-4V vs prompt rules (no ablation); real-time suitability in dynamic scenes; cultural adaptation.

## Q. Cited works possibly missing
SACSoN (RA-L 2024), MuSoHu (IROS 2023), THÖR (RA-L 2020), Pirk et al. 2022 protocol, PIVOT, MOKA, Tsoi et al. HRI'24 LBR.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue IEEE Robotics and Automation Letters; DOI 10.1109/LRA.2024.3511409; pages 508-515; URL https://doi.org/10.1109/LRA.2024.3511409.
- Sources: Crossref (exact title match, DOI 10.1109/LRA.2024.3511409); arXiv abs page (2404.00210v3).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - url: PDF-derived 'Not reported' -> externally verified 'https://doi.org/10.1109/LRA.2024.3511409'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

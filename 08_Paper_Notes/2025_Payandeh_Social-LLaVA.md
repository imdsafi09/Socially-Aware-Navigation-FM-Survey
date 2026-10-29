---
id: 2025_Payandeh_Social-LLaVA
source_pdfs: [04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/Social-LLaVA_Enhancing_Social_Robot_Navigation_through_Human-Language_Reasoning.pdf]
duplicate_copies: [06_Datasets_Benchmarks_Evaluation/Social-LLaVA_Enhancing_Social_Robot_Navigation_through_Human-Language_Reasoning.pdf]
related_versions: []
title: 'Social-LLaVA: Enhancing Social Robot Navigation through Human-Language Reasoning'
authors: &id001 [Amirreza Payandeh, Daeun Song, Mohammad Nazeri, Jing Liang, Praneel Mukherjee, Amir Hossain Raj, Yangzhe Kong, Dinesh Manocha, Xuesu Xiao]
year: 2025
venue: 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
volume: NA
issue: NA
pages: 17192-17198
doi: 10.1109/IROS60139.2025.11247618
url: https://doi.org/10.1109/IROS60139.2025.11247618
pub_status: conference; benchmark/dataset
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1109/IROS60139.2025.11247618); arXiv abs page (2501.09024 (different title)). PDF-derived basis (Stage 1): IEEE IROS 2025 proceedings with IEEE DOI and page numbers (p.1).'
category: S4
folder: 04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core (copy also in 06_Datasets_Benchmarks_Evaluation)
folder_category_match: 'Yes'
category_rationale: Fine-tuned VLM producing perception, prediction, CoT reasoning and high-level social-navigation actions; also contributes SNEI VQA dataset (secondary S6 role).
paper_type: method; dataset
fm_used: 'Yes'
fm_class: [VLM]
fm_models: [LLaVA-v1.5-7B + LoRA (Social-LLaVA), GPT-4V (baseline), Gemini 1.5 Pro (baseline)]
fm_size: 7B
method_family: [supervised fine-tuning (LoRA), chain-of-thought, VQA]
roles: [F1, F2, F4]
roles_evidence: {F1: 'Perception outputs describing humans'' position, distance, action, crowd density (p.3, Fig.3).', F2: 'Categorical ''Predicted Intention'' (action type + relative direction) evaluated (Table III, p.5); free-form prediction of agent movement.', F4: CoT reasoning producing socially compliant high-level action and explanation (p.3-6).}
integration: I1
integration_rationale: Outputs a natural-language high-level action (e.g. 'Stop and wait for clear path'); grounding to motion only a hard-coded proof-of-concept mapping to go straight/turn left/turn right (p.6).
evidence: E1
evidence_rationale: Quantitative evaluation is offline VQA (categorical similarity on test subset; 15 human judges rating free-form answers); the real-robot part is a single qualitative proof-of-concept with no metrics (p.6).
inputs: [RGB (single front-facing image), natural language question]
outputs: [semantic labels, natural-language reasoning, VQA answer, natural-language high-level action, explanation]
human_repr: ['semantic description (clothing, position, distance, action)', 'categorical agent attributes (type incl. groups, proximity, relative position, action, heading)', language-predicted future movement, natural-language social rule/reasoning]
capabilities: {C1: 'No', C2: 'No', C3: Partial, C4: 'No', C5: Partial, C6: Partial, C7: Partial, C8: Partial, C9: Partial, C10: Partial, C11: Partial, C12: Partial, C13: Partial, C14: Partial, C15: Partial, C16: Partial, C17: Partial, C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: 'No', C24: Partial, C25: 'No'}
exp:
  datasets: [SNEI (2K scenarios from SCAND; >40K VQA pairs)]
  simulators: []
  robots: [unnamed robot in Fig.2 proof-of-concept]
  environment: SCAND public spaces (campus indoor/outdoor)
  indoor_outdoor: both
  sensors: [front-facing RGB]
  humans: real (dataset images)
  n_scenes: 2K scenarios (Table II counts sum to 1961)
  n_trajectories: NA
  n_participants: 15 human judges (expert raters of VQA outputs over 50 VQA tasks)
  split: Test subset; size 'over 400 VQA samples' quantitatively (p.2); split ratio not reported
  baselines: [GPT-4V, Gemini 1.5 Pro]
  ablation: 'No'
  real_robot_trials: Partial (single qualitative demo)
  human_study: No (judges rated model text, not robot behaviour)
  statistical_testing: 'No'
  scenarios: [against traffic, with traffic, street crossing, overtaking, narrow doorway, crossing stationary queue, stairs, vehicle interaction, large crowds, conversational group (demo)]
metrics: [VLM | Relative Position similarity | 0-1 | avg similarity of degree/clock position after Hungarian agent matching | p.5, VLM | Predicted Intention similarity | 0-1 | avg similarity of action type + relative direction | p.5, VLM | Overall (average agent similarity) | 0-1 | average per-attribute match over matched agent pairs | p.5, 'VLM | Human judge score per task (Perception, Prediction, CoT, Final Action, Explanation) | 1-5 | average over 15 judges | p.6']
deployment: {fm_model: LLaVA-v1.5-7B LoRA, model_size: 7B, api_cloud_local: Local (open model) - inference hardware not reported, onboard_offboard: Not reported, gpu: Not reported, cpu: Not reported, latency: Not reported, query_frequency: Not reported, planner_frequency: NA, controller_frequency: NA, asynchronous: Not reported, caching: Not reported, event_triggered: Not reported, distillation: 'No', quantization: 'No', fallback_planner: Not reported, safety_shield: Not reported, emergency_behavior: Not reported, uncertainty: 'No', hallucination_mitigation: Fine-tuning on human-curated data; hallucinations of GPT-4V/Gemini shown qualitatively (Fig.3), real_time_claim_supported: NA (no real-time claim)}
repro: {code: Not reported, code_url: Not reported, dataset: Yes (website listed), dataset_url: 'https://cs.gmu.edu/~xiao/Research/SNEI/', checkpoints: Not reported, prompts_published: 'No', hardware_specified: 'No', hyperparameters: No (LoRA settings not given), protocol_described: Partial, project_page: 'https://cs.gmu.edu/~xiao/Research/SNEI/', concerns: Train/test split size unclear; all annotations reviewed by a single person; baseline prompts not published.}
limitations_flags: [intention-ambiguity, dataset-bias, low-level-grounding, hallucination, spatial-reasoning-failure, limited-scenarios]
web_verification_required: [Verify SNEI dataset/code availability at project website.]
cited_missing: [JRDB-Social, SACSoN, MuSoHu, DriveLM, LingoQA, SpatialVLM, SpatialRGPT, Mumm & Mutlu proxemics HRI 2011, Ferrer 2013 social-aware navigation urban, LIMA]
dataset: {kind: dataset (VQA) - SNEI, real_synthetic: real, size: 'See separate snei_* fields (scenarios, images, QA pairs, public release, subsets are distinct quantities)', environments: 'SCAND-derived scenes (9 interaction types, Table II)', sensors: front-facing robot RGB image (from SCAND), ego_view: 'Yes', rgb: 'Yes', rgbd: No (not used), lidar: No (not used), human_trajectories: 'No', dynamic_humans: Yes (images), group_ann: Partial (agent type includes groups), intention_ann: Yes (robot intention; agent action/heading; 'agent intention recognition' per Table I), activity_ann: Partial (agent current action), language_ann: 'Yes (categorical labels + free-form perception, prediction, CoT reasoning, final action, explanation)', social_rule_ann: Not reported (implicit in CoT text), preference_ann: 'No', multi_action_ann: No (single final action), personal_space_ann: Not reported, site_diversity: 'Limited to SCAND scenarios (authors, p.6)', closed_loop: 'No', vlm_suitability: 'Yes', real_robot_compat: Partial
    (robot egocentric images; no grounding of language actions to motion), standard_metrics: No (categorical similarity on test subset; 15 human judges), known_limitations: All annotations reviewed by one person; split sizes not reported; dataset size reported inconsistently by later papers (DATA_QUALITY_ISSUES section 9), snei_original_scenarios: '~2K unique social scenarios ("over 40K VQA pairs across 2K unique social scenarios", p.1; "based on 2K social scenarios ... from SCAND [5]", p.2)', snei_original_images: '1,961 = sum of Table II "# Images" per interaction type (p.4): Against 161, With 358, Street Crossing 75, Overtaking 20, Narrow Doorway 31, Queue 25, Stairs 30, Vehicle 28, Crowds 1233', snei_qa_pairs: '>40K VQA pairs (p.1)', snei_test_subset: '>400 VQA samples (quantitative); 50 VQA tasks rated by 15 human judges (p.2); split sizes not reported', snei_public_release_images: 'Hugging Face amir-pyh/SNEI (MIT; created 2025-10-25, modified 2026-03-11): config default 810 rows (803
    distinct custom_ids, 7 rows without id) + config batch2 698 rows (696 with id, 676 distinct) = 1,508 rows, 1,479 distinct non-null ids, 0 shared ids; harvested 2026-10', snei_dialogue_turns: 'Five free-text Description fields per released row (Perception, Prediction, Chain of Thought Reasoning, Final Action, Explain); later papers describe these as five-turn conversations', snei_paper_specific_subsets: '325 images / dialogues (265 train / 60 test) in E-SocialNav, JSAI, SocialNav-MoE, MAction; 810 conversations in MUSON; 49 scenarios in AutoSpatial human evaluation; 8:2 random split (size unstated) in SOPD; 1,625 image-text pairs in GCL', snei_provenance: 'UNRESOLVED: Social-LLaVA states SCAND only (p.2); E-SocialNav states SCAND and MuSoHu (p.4); HUMA states "the SCAN benchmark" (p.6). Not inferred.', snei_website: 'https://cs.gmu.edu/~xiao/Research/SNEI/ (printed p.1) redirects to the department homepage as of 2026-10 (dead link)'}
coding: {latency_reported: 'No', safety_mechanism: 'No', uncertainty_treatment: 'No', hallucination_treatment: Partial, code_released: 'No', new_dataset_released: 'Yes', real_robot: Demo, human_subject_study: Text-raters/other}
pdf_metadata_stage1:
  year: 2025
  authors: *id001
  venue: 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2025), Hangzhou
  volume: Not reported
  issue: Not reported
  pages: 17192-17198
  doi: 10.1109/IROS60139.2025.11247618
  url: https://cs.gmu.edu/~xiao/Research/SNEI/
  pub_status: conference; benchmark/dataset
  peer_reviewed: 'Yes'
  peer_review_basis: IEEE IROS 2025 proceedings with IEEE DOI and page numbers (p.1).
project_url: https://cs.gmu.edu/~xiao/Research/SNEI/
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
  verified_doi: 10.1109/IROS60139.2025.11247618
  verified_url: https://doi.org/10.1109/IROS60139.2025.11247618
  verified_pages: 17192-17198
  arxiv: 2501.09024 (different title)
  version_relationship: Corpus copy is the published IROS version; arXiv 2501.09024 carries a different title (alternate version)
  sources: ['Crossref (exact title match, DOI 10.1109/IROS60139.2025.11247618)', arXiv abs page (2501.09024 (different title))]
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A5]
  C_capabilities: {SAF1: 'No', SAF2: 'No', SPA1: Partial, SPA2: Partial, SPA3: Partial, SPA4: Partial, HUM1: Partial, HUM2: Partial, NOR1: Partial, NOR2: 'No', NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: [R1, R2, R3]
  D_interface: [D0]
  E_evidence_profile: {EV1_offline: 'Yes', EV2_closed_loop_sim: 'No', EV3_physical_robot: demo, EV4_real_humans_in_trials: none, EV5_human_evaluation: text-raters, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: NA, statistical_testing: 'No', cross_environment: 'Yes', runtime_measured: 'No'}
  cross_cutting: {temporal_coupling: offline, memory: 'No', continual_adaptation: 'No', explanation_output: 'Yes (text output, not delivered to people)', safety_guard: 'No', uncertainty: 'No', hallucination_mitigation: Partial, privacy_constraint: 'No', inference_location: n/a (offline evaluation only)}
physical_source_folder: "04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core"
analytical_category: "S4"
coding:
  latency_reported: "No"
  safety_mechanism: "No"
  uncertainty_treatment: "No"
  hallucination_treatment: "Partial"
  code_released: "No"
  new_dataset_released: "Yes"
  real_robot: "Demo"
  human_subject_study: "Text-raters/other"
---

# Social-LLaVA: Enhancing Social Robot Navigation through Human-Language Reasoning (Payandeh et al., IROS 2025)

Page convention: PDF index (p.N); printed pp.17192–17198.

## A. Bibliographic
Primary copy `04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/Social-LLaVA_...pdf`; second copy in `06_Datasets_Benchmarks_Evaluation/` differs only in IEEE download-timestamp watermark (text diff verified). IROS 2025, pp.17192–17198, DOI 10.1109/IROS60139.2025.11247618. Conference; peer-reviewed. Website https://cs.gmu.edu/~xiao/Research/SNEI/.

## B. Position — S4 (with S6 dataset contribution)
Fine-tuned VLM for social-navigation reasoning plus the SNEI VQA dataset. Classified S4 because the model outputs social-navigation actions; evidence is offline. The authors state: "our focus lies in dataset development rather than algorithmic innovation" (p.4).

## C. Research problem
- **Question (authors):** "How can we leverage VLMs to use human language reasoning to navigate social environments?" (p.1).
- **Hypothesis:** robots can follow a human-like object-centric perception → prediction → planning process expressed in language (inspired by DriveLM) (p.3).
- **Motivation:** off-the-shelf VLMs weak in spatial reasoning (relative positions, intent, trajectory prediction); AV datasets not applicable; (semi-)automatic VQA data noisy (p.3).
- **Claims:** SNEI is "the first VQA dataset specifically designed for social robot navigation" (p.3); Social-LLaVA outperforms GPT-4V and Gemini 1.5 Pro "in overall performance" (p.2).
- **Our observation:** on the categorical part (Table III) Social-LLaVA's Overall (0.29) and Relative Position (0.36) are *lower* than Gemini 1.5 Pro (0.32, 0.43) and GPT-4V (0.30, 0.42); it is best only on Predicted Intention (0.26) and on the human-judged free-form part (Table IV). The "outperforms" claim is supported by Table IV, not Table III.

## D. Technical method
- **SNEI construction (p.3–4):** 2K scenarios hand-selected from SCAND; annotators see a front-facing robot image; categorical labels (Context: environment type, crowd density, indoor/outdoor, terrain; Robot: goal, direction, speed, intention; Obstacles: type, proximity, position; Agents: type incl. individuals/groups/bicycles, proximity, relative position, current action, heading); free-form (Perception, Prediction, CoT reasoning, Final Action, Explanation). All annotations reviewed by the same person (p.4). >40K VQA pairs.
- **Model:** LLaVA-v1.5-7B fine-tuned with LoRA = Social-LLaVA (p.4). Supervised fine-tuning only.
- **Evaluation (p.5):** agent-level Hungarian matching (cost = 1 − similarity, Eq.1) over ≤5 agents; similarity for relative position (degree & clock position) and intention (action type & relative direction).
- **Real robot (p.6):** hard-coded mapping from high-level language to {go straight, turn left, turn right}; Fig.2 proof-of-concept of avoiding a conversation between two people.
- **INPUT:** single RGB image + question. **OUTPUT:** perception/prediction/CoT text, final high-level action, explanation.

## E. Human/social representation
Language descriptions and categorical attributes of agents (type including groups, proximity, relative position, action, heading); language prediction of future movement; CoT social reasoning. No geometric human model, no trajectory forecasting in metric space.

## F. Roles — F1, F2, F4 (front matter). Not F6/F9: no costs or waypoints.

## G. Social capabilities (all Partial entries are OFFLINE reasoning only)
C3 Partial (annotators prioritise comfort/distance in reasoning) · C5–C7 Partial (perception/prediction/intention VQA) · C8 Partial (current action labels) · C9 Partial (group agent type) · C10 Partial (conversation avoidance only in qualitative demo) · C11–C17 Partial (interaction types in Table II include against/with traffic, street crossing, overtaking, doorway, queue, crowds; evaluated only as language outputs, not per type) · C24 Partial · C1/C2/C4/C18–C23/C25 No (not evaluated).

## H. Integration — I1. ## I. Evidence — E1 (offline action prediction; qualitative robot demo).

## J. Experimental evidence
Dataset SNEI (Table II, p.4): Against Traffic 161; With Traffic 358; Street Crossing 75; Overtaking 20; Narrow Doorway 31; Crossing Stationary Queue 25; Stairs 30; Vehicle Interaction 28; Navigating Through Large Crowds 1233 (sum 1961). Baselines GPT-4V, Gemini 1.5 Pro (original LLaVA 1.5 excluded because it needed fine-tuning to follow prompts, p.5). Quantitative on "over 400 VQA samples"; qualitative by 15 human judges across 50 VQA tasks (p.2). No ablation; no statistical tests.

## K. Metrics — Relative Position / Predicted Intention / Overall similarity (0–1); judge scores 1–5 per task.

## L. Quantitative results (visually verified, p.5–6)
Table III (categorical, avg similarity):
| Metric | GPT-4V | Gemini 1.5 Pro | Social-LLaVA |
|---|---|---|---|
| Relative Position | 0.42 | **0.43** | 0.36 |
| Predicted Intention | 0.21 | 0.22 | **0.26** |
| Overall | 0.30 | **0.32** | 0.29 |

Table IV (free-form, mean of 15 judges, 1–5):
| Task | GPT4-V | Gemini 1.5 Pro | Social-LLaVA |
|---|---|---|---|
| Perception | 3.11 | 3.45 | 4.0 |
| Prediction | 3.18 | 3.87 | 4.06 |
| CoT | 3.41 | 3.79 | 4.08 |
| Final Action | 2.77 | 3.46 | 4.19 |
| Explanation | 3.16 | 3.66 | 3.95 |

Table I (p.4): SNEI is the only listed dataset with robot action, social context, agent intention recognition, CoT reasoning and manual annotation (vs SACSoN/MuSoHu/SCAND and JRDB-Social).

## M. Deployment — not reported (no latency, hardware or rates).

## N. Limitations
1. **Stated (§V, p.6):** ambiguity of social navigation and human motion; no agreed-upon compliant behaviour; ground-truth variation by labeller; data limited to SCAND scenarios (may not generalise to unseen environments); grounding language actions to robot motion "is still an open problem and is not a trivial task".
2. **Future work:** implied — addressing ambiguity in annotation/training; more and diverse data; grounding.
3. **Observable:** single-image input (no temporal context); single reviewer for all labels; split sizes not reported; baselines zero-shot vs fine-tuned model; no closed-loop navigation metrics; Social-LLaVA not best on categorical overall.
4. Survey-level: deferred.

## O. Reproducibility — dataset website given (availability needs verification); code, checkpoints, prompts, LoRA hyperparameters not reported.

## P. Direct-paper questions
1 Translating egocentric social scenes into human-like reasoning and high-level actions. 2 Language reasoning as bridge between perception and socially aware action (p.1). 3 LLaVA-v1.5-7B LoRA. 4 Single robot RGB image. 5 VQA questions per annotation category (prompt text not published). 6 Text: perception, prediction, CoT, final action, explanation. 7 Only hard-coded mapping to straight/left/right in demo. 8 Not in evaluated system; in demo, effectively yes via hard-coded mapping (no safety layer described). 9 None described. 10 None described. 11 Human-like socially compliant reasoning and actions. 12 Offline VQA similarity and judge ratings. 13 Yes (agent-level). 14 Partial (agent type "groups"). 15 Yes (offline). 16 Partial (current action). 17 Implicit via CoT. 18 No (single image). 19 No. 20 Discussed for baselines (Fig.3). 21 Not reported. 22 Not reported. 23 Only in demo. 24 No. 25 None for navigation; only offline reasoning scores. 26 Cannot conclude anything about closed-loop social navigation performance, safety or human perception of robot behaviour.

## Q. Cited works possibly missing
JRDB-Social (CVPR 2024), SACSoN, MuSoHu, DriveLM, LingoQA, SpatialVLM, SpatialRGPT, Mumm & Mutlu 2011.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS); DOI 10.1109/IROS60139.2025.11247618; pages 17192-17198; URL https://doi.org/10.1109/IROS60139.2025.11247618.
- Sources: Crossref (exact title match, DOI 10.1109/IROS60139.2025.11247618); arXiv abs page (2501.09024 (different title)).
- Version relationship: Corpus copy is the published IROS version; arXiv 2501.09024 carries a different title (alternate version).
- Changed field - venue: PDF-derived '2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2025), Hangzhou' -> externally verified '2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)'
- Changed field - volume: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - issue: PDF-derived 'Not reported' -> externally verified 'NA'
- Changed field - url: PDF-derived 'https://cs.gmu.edu/~xiao/Research/SNEI/' -> externally verified 'https://doi.org/10.1109/IROS60139.2025.11247618'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

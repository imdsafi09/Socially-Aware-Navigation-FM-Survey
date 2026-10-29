---
id: 2026_Wang_MAction-SocialNav
source_pdfs: [04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/maction_socialnav.pdf]
duplicate_copies: []
related_versions: []
title: 'MAction-SocialNav: Multi-Action Socially Compliant Navigation via Reasoning-enhanced Prompt Tuning'
authors: &id001 [Zishuo Wang, Xinyu Zhang, Zhuonan Liu, Tomohito Kawabata, Daeun Song, Xuesu Xiao, Ling Xiao]
year: 2026
venue: IEEE Robotics and Automation Letters
volume: '11'
issue: '8'
pages: 9747-9754
doi: 10.1109/LRA.2026.3706951
url: https://doi.org/10.1109/LRA.2026.3706951
pub_status: journal
peer_reviewed: 'Yes'
peer_review_basis: 'Externally verified (2026-10-19): Crossref (exact title match, DOI 10.1109/LRA.2026.3706951); arXiv abs page (2512.21722v1). PDF-derived basis (Stage 1): Manuscript received 25 Dec 2025, revised 8 Mar 2026, accepted 31 May 2026; recommended by Editor upon evaluation of AE and reviewers'' comments (p.1). PDF is accepted preprint version.'
category: S4
folder: 04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core
folder_category_match: 'Yes'
category_rationale: Small VLM (NVILA-Lite-2B) fine-tuned to output ranked sets of socially acceptable discrete navigation actions; offline evaluation.
paper_type: method; dataset
fm_used: 'Yes'
fm_class: [VLM]
fm_models: ['NVILA-Lite-2B (fine-tuned: vision projector + LoRA)', 'GPT-4o, Claude (zero-shot baselines; Claude version not specified)']
fm_size: 2B
method_family: [supervised fine-tuning (LoRA + projector), prompt tuning (meta-cognitive prompt), multi-turn VQA, action ranking]
roles: [F1, F2, F4]
roles_evidence: {F1: 'Turn 1: scene observation of surroundings and pedestrians (Fig.3, p.3).', F2: 'Turn 2: prediction of pedestrian behaviour/movement (Fig.3).', F4: 'Turn 3: ranked actions following Feasibility -> Social norms -> Efficiency hierarchy; MCP prompt ''infer intentions, plan safe, smooth, and socially appropriate paths'' (Table I, p.5).'}
integration: I1
integration_rationale: Outputs ranked discrete actions from {Move forward, forward-left, forward-right, Turn left, Turn right, Stop}; integration with a local planner is explicitly future work (p.7-8).
evidence: E1
evidence_rationale: Offline multi-action prediction on a 79-sample test set (plus six random splits); no simulation or robot execution (p.5-8).
inputs: [RGB (single image), natural language multi-turn questions, system prompt]
outputs: [natural-language scene description, natural-language prediction, ranked discrete action set]
human_repr: [semantic description (language), predicted pedestrian behaviour (language)]
capabilities: {C1: Partial, C2: 'No', C3: Partial, C4: 'No', C5: Partial, C6: Partial, C7: 'No', C8: 'No', C9: 'No', C10: 'No', C11: Partial, C12: Partial, C13: 'No', C14: 'No', C15: Partial, C16: 'No', C17: Partial, C18: 'No', C19: 'No', C20: 'No', C21: 'No', C22: 'No', C23: 'No', C24: Partial, C25: 'No'}
exp:
  datasets: ['Curated multi-action dataset: 789 samples (710 train / 79 test, random), three-turn conversations, dual human annotations; libraries, malls, plazas, streets, campuses, parks; image source not stated']
  simulators: []
  robots: []
  environment: indoor and outdoor public spaces (images)
  indoor_outdoor: both
  sensors: [RGB]
  humans: real (images)
  n_scenes: 789 samples
  n_trajectories: NA
  n_participants: 2 annotators
  split: 710/79 random; six random splits for cross-validation
  baselines: [MAction w/o MCP, w/ Causal Reasoning, 'GPT-4o (Raw, CoT, Ruled)', 'Claude (Raw, CoT, Ruled)']
  ablation: Yes (MCSE, CSR human/self/AI combinations; difficulty levels)
  real_robot_trials: 'No'
  human_study: 'No'
  statistical_testing: 'Yes (p-values vs GPT-4o and Claude: 4.0e-20 to 1.4e-3; test not named)'
  scenarios: [crowd density levels, sidewalk/street, indoor corridors, seated people, easy/medium/difficult]
metrics: [VLM | Pred@1 | 0-1 | top-ranked predicted action in GT acceptable set | p.4, 'VLM | Pred@n | -1 to 1 | mean over predicted actions of (+1 if in GT, -1 if not) | p.4', VLM | All-Pred-in-GT (APG) | 0/1 mean | all predicted actions within GT set | p.4, 'VLM | Multi-action accuracy (MAA) | weighted score | sum of weights [6..1] for correct ranked actions / |a|; 0 if |pred|>|GT| | p.4', VLM | Error rate (ER) | 0-1 | fraction of predicted actions outside GT set | p.4, VLM | Recall (R) and Avg. predicted set size | ratio / count | Table V | p.6, DEPLOY | Inference speed | FPS | frames per second of model inference | p.6]
deployment: {fm_model: NVILA-Lite-2B fine-tuned, model_size: 2B, api_cloud_local: Local (open model); GPT-4o/Claude via API (implied), onboard_offboard: Not reported, gpu: 4x NVIDIA RTX 8000 48GB (training); inference GPU not reported, cpu: Not reported, latency: '1.524 FPS (vs GPT-4o CoT 0.314 FPS, Claude CoT 0.452 FPS)', query_frequency: NA, planner_frequency: NA, controller_frequency: NA, asynchronous: NA, caching: NA, event_triggered: NA, distillation: 'No', quantization: No (BF16 training), fallback_planner: NA, safety_shield: No (Stop included as fallback action in annotation), emergency_behavior: NA, uncertainty: 'Partial: multiple acceptable actions modelled as ranked set (action ambiguity), no probabilistic calibration', hallucination_mitigation: 'No', real_time_claim_supported: 'Partial: claims ''real-time efficiency'' at 1.524 FPS on unspecified hardware; no control loop'}
repro: {code: Not reported, code_url: Not reported, dataset: Not stated as released, dataset_url: NA, checkpoints: Not reported, prompts_published: Yes (MCP Table I; baseline prompts Fig.4), hardware_specified: Partial (training only), hyperparameters: 'Yes (lr 1e-4, batch 2/GPU, grad accum 4, global 64, 10 epochs, ZeRO-2, BF16)', protocol_described: 'Yes', project_page: Not reported, concerns: Small test set (79); image source not stated; Claude version unspecified; GPT-4o refused in 31/79 cases.}
limitations_flags: [dataset-bias, low-level-grounding, limited-scenarios, intention-ambiguity]
web_verification_required: [Final RA-L volume/issue/pages/DOI.]
cited_missing: [NVILA (CVPR 2025), Mobility VLA (CoRL 2024), Language and sketching LLM navigation (ICRA 2024), SocialGAIL, Kathuria 2025 deep IRL implicit social navigation, Salzmann 2023 human pose trajectory prediction, Bachiller GNN disruption, Takayama & Pantofaru 2009 proxemics, Tree of Thoughts, Large language models are human-level prompt engineers]
coding: {latency_reported: 'Yes', safety_mechanism: 'No', uncertainty_treatment: Partial, hallucination_treatment: 'No', code_released: 'No', new_dataset_released: 'No', real_robot: 'No', human_subject_study: 'No'}
pdf_metadata_stage1:
  year: 2026
  authors: *id001
  venue: IEEE Robotics and Automation Letters (accepted; preprint version)
  volume: Not reported
  issue: Not reported
  pages: 1-8 (preprint pagination)
  doi: Not reported in PDF ('see top of this page')
  url: Not reported
  pub_status: journal
  peer_reviewed: 'Yes'
  peer_review_basis: Manuscript received 25 Dec 2025, revised 8 Mar 2026, accepted 31 May 2026; recommended by Editor upon evaluation of AE and reviewers' comments (p.1). PDF is accepted preprint version.
external_verification:
  verified_on: '2026-10-19'
  status_class: 'A: published, peer-reviewed'
  verified_venue: IEEE Robotics and Automation Letters
  verified_doi: 10.1109/LRA.2026.3706951
  verified_url: https://doi.org/10.1109/LRA.2026.3706951
  verified_pages: 9747-9754
  arxiv: 2512.21722v1
  version_relationship: Corpus copy is the arXiv author version; published version authoritative
  sources: ['Crossref (exact title match, DOI 10.1109/LRA.2026.3706951)', arXiv abs page (2512.21722v1)]
snei_usage: {reported_quantity: '325', unit: multi-turn dialogues, what_it_represents: Described as SNEI scale ("limited scale (325 multi-turn dialogues)"), page: p.2, remark: 'Own MAction dataset: 789 samples (710/79), three-turn', provenance_note: SNEI provenance (SCAND vs SCAND+MuSoHu) UNRESOLVED; see SNEI_DATASET_RECONCILIATION.md}
final_coding:
  taxonomy_version: Stage-3 final (2026-10-19)
  A_social_representation: [A5]
  C_capabilities: {SAF1: Partial, SAF2: 'No', SPA1: Partial, SPA2: 'No', SPA3: Partial, SPA4: Partial, HUM1: Partial, HUM2: 'No', NOR1: Partial, NOR2: 'No', NOR3: Partial, NOR4: 'No', EXP1: 'No', EXP2: 'No', EXP3: 'No'}
  B_roles: [R1, R2, R3]
  D_interface: [D0]
  E_evidence_profile: {EV1_offline: 'Yes', EV2_closed_loop_sim: 'No', EV3_physical_robot: none, EV4_real_humans_in_trials: none, EV5_human_evaluation: none, EV6_open_world_deployment: 'No'}
  E_quality_attributes: {trials: NA, statistical_testing: 'Yes (p-values vs GPT-4o and Claude: 4.0e-20 to 1.4e-3; test not named)', cross_environment: 'Yes', runtime_measured: 'Yes'}
  cross_cutting: {temporal_coupling: offline, memory: 'No', continual_adaptation: 'No', explanation_output: 'No', safety_guard: 'No', uncertainty: Partial, hallucination_mitigation: 'No', privacy_constraint: 'No', inference_location: n/a (offline evaluation only)}
physical_source_folder: "04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core"
analytical_category: "S4"
coding:
  latency_reported: "Yes"
  safety_mechanism: "No"
  uncertainty_treatment: "Partial"
  hallucination_treatment: "No"
  code_released: "No"
  new_dataset_released: "No"
  real_robot: "No"
  human_subject_study: "No"
---

# MAction-SocialNav (Wang et al., RA-L accepted 2026)

Page convention: PDF index (p.N) = preprint pages 1–8.

## A. Bibliographic
`04_Direct_VLM_SocialNav/A_Peer_Reviewed_Core/maction_socialnav.pdf`. Wang, Zhang, Liu, Kawabata, Song, X. Xiao, L. Xiao (Hokkaido; Ewha; GMU). IEEE RA-L, accepted 31 May 2026 (preprint version; volume/pages/DOI not in PDF → WEB_VERIFICATION_REQUIRED). Peer-reviewed: Yes (acceptance statement p.1).

## B. Position — S4
Direct social-navigation VLM producing ranked socially acceptable actions; first in corpus to explicitly model *action ambiguity* (multiple acceptable actions). Evidence offline only. Same author group as the competing survey (Cai/Yamasaki/L. Xiao).

## C. Research problem
- **Problem:** social norms are ambiguous; multiple actions may be equally acceptable; existing methods assume a single correct action; large VLMs too slow (p.1).
- **Claims:** "first work to explicitly model and evaluate action ambiguity in socially compliant navigation" (p.2); MCP method; multi-action dataset; five metrics; outperforms zero-shot large VLMs.
- Critique of SNEI (authors): single response per scenario; "limited scale (325 multi-turn dialogues)" (p.2). *Note:* Social-LLaVA paper itself reports 2K scenarios/40K VQA; the "325" figure is the authors' characterisation and is not reconcilable from our corpus — flagged in DATA_QUALITY_ISSUES.

## D. Technical method
- Backbone NVILA-Lite-2B (ViT + projector + LLM); fine-tune vision projector + LoRA; full SFT objective = autoregressive next-token loss conditioned on system prompt S_MCP (Eq.1, p.3).
- Three-turn protocol: Scene Observation → Motion Prediction → Ranked Action Generation (Fig.3).
- Discrete action space A = {Move forward, Move forward-left, Move forward-right, Turn left, Turn right, Stop}; annotation hierarchy Feasibility → Social norms (comfortable interpersonal distance) → Efficiency (forward > forward-diagonal > turns; Stop as necessary/fallback) (p.4).
- **MCP (Table I, p.5):** MCSE — silent recursive self-evaluation with 90-point threshold (scores may exceed 100); CSR — "compete against {humans, other AI models, other AI models like you}"; S_MCP = S_meta ∥ S_com (Eq.2).
- Training: 4× RTX 8000 (48 GB), lr 1e-4, batch 2/GPU, grad-accum 4 (global 64), 10 epochs, DeepSpeed ZeRO-2, BF16 (p.5).
- INPUT: single image + multi-turn questions. OUTPUT: description, prediction, ranked action list.

## E. Human/social representation — only language descriptions/predictions; no geometric human model.

## F. Roles — F1, F2, F4.

## G. Social capabilities (OFFLINE)
C1 Partial (feasibility = no collision in annotation; ER as action validity) · C3 Partial (comfortable distance ranking criterion) · C5/C6 Partial (language prediction turn, not evaluated separately) · C11, C12, C15, C17, C24 Partial (rule-guided baselines mention vehicle lanes, grass, zebra crossings; density-dependent scenes) · others No.

## H. Integration — I1. ## I. Evidence — E1.

## J. Experimental evidence — dataset 789 (710/79); dual annotators; 6 random splits; GPT-4o and Claude zero-shot with Raw/Rule-guided/CoT prompts (Fig.4); difficulty stratification (rule-based: road network, pedestrian, environmental complexity). p-values reported (test unnamed).

## K. Metrics — Pred@1, Pred@n, APG, MAA, ER, Recall, avg set size, FPS (definitions front matter).

## L. Quantitative results
Table II (p.5): w/o MCP 0.734 / 0.389 / 0.532 / 3.048 / 0.306; w/ Causal Reasoning 0.747 / 0.351 / 0.532 / 3.202 / 0.325; w/ MCP 0.760 / 0.473 / 0.595 / 3.571 / 0.264 (Pred@1 / Pred@n / APG / MAA / ER).
Table III six random splits: w/o MCP 0.823±0.059 / 0.385±0.119 / 0.502±0.101 / 2.998±0.464 / 0.307±0.059; w/ MCP 0.831±0.059 / 0.426±0.059 / 0.536±0.059 / 3.163±0.275 / 0.287±0.039.
Table IV zero-shot (Pred@1 / Pred@n / APG / MAA / ER): GPT-4o Raw 0.570 / −0.349 / 0.025 / 0.230 / 0.668; Claude Raw 0.405 / −0.424 / 0.000 / 0.059 / 0.642; GPT-4o CoT 0.620 / −0.384 / 0.013 / 0.057 / 0.692; Claude CoT 0.760 / −0.298 / 0.013 / 0.095 / 0.649; GPT-4o Ruled 0.646 / −0.273 / 0.013 / 0.149 / 0.637; Claude Ruled 0.443 / −0.658 / 0.000 / 0.000 / 0.829; MAction-SocialNav 0.760 / 0.473 / 0.595 / 3.571 / 0.264.
Table V recall / avg predicted set size (GT avg 1.81): GPT-4o Raw 0.634/3.79; Claude Raw 0.769/4.06; GPT-4o CoT 0.973/5.22; Claude CoT 0.921/4.10; GPT-4o ruled 0.532/2.67; Claude ruled 0.874/3.76; MAction 0.726/1.53.
GPT-4o refusals: 31 of 79 cases (~39%) (p.6). Speed: Claude CoT 0.452 FPS, GPT-4o CoT 0.314 FPS, MAction 1.524 FPS (p.6). p-values 4.0×10⁻²⁰ to 1.4×10⁻³ vs Claude/GPT-4o (p.6).
Table VI ablation (rows: baseline; MCSE; CSR-human; CSR-self; CSR-AI; MCSE+human; MCSE+self; MCSE+AI — row-to-check mapping per p.7 text): Pred@1 0.734/0.785/0.785/0.760/0.760/0.722/0.747/0.760; Pred@n 0.389/0.395/0.356/0.367/0.392/0.392/0.378/0.473; APG 0.532/0.544/0.468/0.468/0.494/0.494/0.506/0.595; MAA 3.048/3.137/2.772/3.052/3.135/3.103/3.012/3.571; ER 0.306/0.303/0.322/0.317/0.304/0.304/0.311/0.264. (Exact checkmark-to-row mapping for rows 3–7 inferred from text "Rows 3-5" CSR in isolation; WEB/visual recheck optional.)
Table VII difficulty (w/o MCP → w/ MCP): Easy Pred@1 0.966→0.931, MAA 5.690→5.483; Medium Pred@1 0.621→0.621, Pred@n 0.193→0.276, APG 0.414→0.483, MAA 1.724→2.702, ER 0.403→0.362; Difficult Pred@1 0.571→0.714, Pred@n −0.041→0.159, APG 0.143→0.286, MAA 1.226→2.131, ER 0.521→0.421; Easy Pred@n 0.897 both, APG 0.931 both, ER 0.052 both.

## M. Deployment — 2B model, 1.524 FPS (hardware for inference unspecified). Not integrated with robot.

## N. Limitations
1. **Stated (p.7–8):** dataset modest (789 samples); model focuses on high-level semantic reasoning/action selection only.
2. **Future work:** enlarge/diversify dataset and fine-grained annotations; integrate with conventional local planners for real-world execution.
3. **Observable:** 79-sample test set; discrete 6-action space; inference hardware unspecified for FPS comparison against API models (network latency included for API models?) — not stated; baselines zero-shot vs fine-tuned; image source unstated.
4. Deferred.

## O. Reproducibility — prompts published (Table I, Fig.4); hyperparameters given; code/data release not stated.

## P. Direct-paper questions
1 Choosing among multiple socially acceptable discrete actions under ambiguity. 2 Social reasoning over images; efficiency via small VLM. 3 NVILA-Lite-2B. 4 Single image. 5 MCP system prompt + 3-turn questions. 6 Ranked action set. 7 Not converted (future work). 8 No. 9 None. 10 None. 11 Socially compliant, efficient, real-time. 12 Offline set-prediction accuracy. 13 Implicit (language). 14 No. 15 No. 16 No. 17 Partial. 18 No (single frame). 19 Ambiguity via sets, no calibration. 20 No. 21 1.524 FPS (model only). 22 Not reported. 23 No. 24 No. 25 None for navigation; offline metrics only. 26 Nothing about closed-loop social behaviour, safety, or human perception.

## Q. Cited works possibly missing — Mobility VLA; NVILA; SocialGAIL; Kathuria 2025 deep IRL; Salzmann 2023; Bachiller GNN disruption; Takayama & Pantofaru 2009.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: A: published, peer-reviewed; venue IEEE Robotics and Automation Letters; DOI 10.1109/LRA.2026.3706951; pages 9747-9754; URL https://doi.org/10.1109/LRA.2026.3706951.
- Sources: Crossref (exact title match, DOI 10.1109/LRA.2026.3706951); arXiv abs page (2512.21722v1).
- Version relationship: Corpus copy is the arXiv author version; published version authoritative.
- Changed field - venue: PDF-derived 'IEEE Robotics and Automation Letters (accepted; preprint version)' -> externally verified 'IEEE Robotics and Automation Letters'
- Changed field - volume: PDF-derived 'Not reported' -> externally verified '11'
- Changed field - issue: PDF-derived 'Not reported' -> externally verified '8'
- Changed field - pages: PDF-derived '1-8 (preprint pagination)' -> externally verified '9747-9754'
- Changed field - doi: PDF-derived 'Not reported in PDF ('see top of this page')' -> externally verified '10.1109/LRA.2026.3706951'
- Changed field - url: PDF-derived 'Not reported' -> externally verified 'https://doi.org/10.1109/LRA.2026.3706951'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

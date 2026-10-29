---
id: 2026_Cai_VLM-Deployable-SRN-Survey
source_pdfs: [00_Existing_Surveys/2606.28760v1.pdf]
duplicate_copies: []
related_versions: []
title: 'Vision-Language Models for Deployable Social Robot Navigation: Bridging Semantic Reasoning and Low-Level Control'
authors: &id001 [Runji Cai, Toshihiko Yamasaki, Ling Xiao]
year: 2026
venue: arXiv preprint (arXiv:2606.28760v1 [cs.RO], 27 Jun 2026)
volume: Not reported
issue: Not reported
pages: 24 (PDF)
doi: Not found / not applicable
url: https://arxiv.org/abs/2606.28760
pub_status: preprint
peer_reviewed: 'No'
peer_review_basis: 'Publication status: Preprint; Peer reviewed: No verified peer-reviewed version found as of corpus freeze date (2026-10-19). Sources: arXiv abs page (2606.28760v1); Crossref title search: no match.'
category: S0
folder: 00_Existing_Surveys
folder_category_match: 'Yes'
category_rationale: Narrative survey of VLM-based social robot navigation (SRN); the closest competing survey to our project.
paper_type: survey
fm_used: 'No'
fm_class: []
fm_models: []
fm_size: NA
method_family: []
roles: []
roles_evidence: {}
integration: NA
integration_rationale: Survey; no method.
evidence: NA
evidence_rationale: Survey; no experiments.
inputs: []
outputs: []
human_repr: []
capabilities: {C1: NA, C2: NA, C3: NA, C4: NA, C5: NA, C6: NA, C7: NA, C8: NA, C9: NA, C10: NA, C11: NA, C12: NA, C13: NA, C14: NA, C15: NA, C16: NA, C17: NA, C18: NA, C19: NA, C20: NA, C21: NA, C22: NA, C23: NA, C24: NA, C25: NA}
exp:
  datasets: []
  simulators: []
  robots: []
  environment: NA
  indoor_outdoor: NA
  sensors: []
  humans: NA
  n_scenes: NA
  n_trajectories: NA
  n_participants: NA
  split: NA
  baselines: []
  ablation: NA
  real_robot_trials: NA
  human_study: NA
  statistical_testing: NA
  scenarios: []
metrics: []
deployment: {fm_model: NA, model_size: NA, api_cloud_local: NA, onboard_offboard: NA, gpu: NA, cpu: NA, latency: NA, query_frequency: NA, planner_frequency: NA, controller_frequency: NA, asynchronous: NA, caching: NA, event_triggered: NA, distillation: NA, quantization: NA, fallback_planner: NA, safety_shield: NA, emergency_behavior: NA, uncertainty: NA, hallucination_mitigation: NA, real_time_claim_supported: NA}
repro: {code: NA, code_url: NA, dataset: NA, dataset_url: NA, checkpoints: NA, prompts_published: NA, hardware_specified: NA, hyperparameters: NA, protocol_described: NA, project_page: Not reported, concerns: No literature-search protocol; paper counts in Fig.1 are raw Google Scholar hit counts.}
limitations_flags: []
web_verification_required: [Check whether the survey has since been accepted at a journal (Springer-style template).]
cited_missing: [NaVILA, OmniVLA, NaVid, OpenVLA, Octo, LeLaN, SpatialVLM, SpatialRGPT, VLM-RMs, 'Probing prompt design for socially compliant robot navigation (Xiao & Yamasaki arXiv:2601.14622)', GCL IEICE tech report, 'Walk with me (arXiv:2604.26839)', GazeNav (AAAI 2026), SACSoN/HuRoN, SELFI, DR-MPC, MuSoHu, THOR, JRDB, SocNav2, DynaBARN, Social Navigation Protocol (Pirk 2022), Human Empowerment (HRI 2025), HuNavSim, SEAN 2.0, Habitat 3.0, SocialGym 2.0, SocNavGym, Dragan legibility 2013, Trautman IJRR 2015, Mavrogiannis HRI 2019 effects of navigation strategies, Wang 2022 metrics social conformity, ConceptGraphs, Xiao 2022 motion planning ML survey, Firoozi 2025 foundation models in robotics, Rios-Martinez 2015 proxemics survey]
survey:
  scope: VLM-based social robot navigation, organised by how high-level VLM reasoning is bridged to low-level planning/control for deployment.
  years_covered: Bulk of cited VLM work 2022-2026; classical background back to 1995 (Helbing). Not stated explicitly.
  search_strategy: None reported. Fig.1 (p.2) gives raw Google Scholar hit counts for SRN and VLM-based SRN 2022-2025 as motivation only.
  inclusion: Not reported
  exclusion: Not reported
  n_papers: Not reported
  n_refs: 124
  taxonomy: 'Five integration paradigms: (a) VLMs as high-level reasoners and proposal selectors; (b) VLMs as evaluators; (c) VLMs for semantic map grounding; (d) VLMs as intermediate representations; (e) VLMs as action interfaces; plus subsection 3.6 efficient VLMs for deployable SRN.'
  taxonomy_dims: 'Single dimension: interface/coupling type between VLM output and planner/controller (Sec.3, Fig.2 p.7).'
  datasets_covered: [SDD, EgoMotion, WILDTRACK, JRDB, THOR, SocNav2, DynaBARN, SCAND, MuSoHu, SG-LSTM, HuRoN, SNEI, MUSON, GazeNav]
  simulators_covered: [gym-collision-avoidance, iGibson 2.0, Intelligent Human Avatar, SocialGym, SEAN 2.0, HuNavSim, Habitat 3.0, DynaBARN, SocNavBench, Arena-Bench, Social Navigation Protocol, Human Empowerment Evaluation, SocialNav-SUB, SocNavGym, SocialGym 2.0]
  metrics_covered: Listed per platform in Table 3 (collisions, stuck, extra time, success rate, human time to goal, force, blame, path efficiency, time not moving, following rate, path/motion quality, pedestrian disruption, human-rated compliance, probability of agreement). No metric taxonomy.
  coverage: {classical: Partial, human_aware: Partial, proxemics: Partial, prediction: Partial, imitation_learning: Partial, drl: Partial, gnn_transformer: Partial, language_models: 'Yes', vlm: 'Yes', lvlm: Partial, foundation_models: 'Yes', vla: 'Yes', real_world_deployment: Partial, evaluation: Partial}
  stage2_coverage: {classical_proxemics: Partial, learning_drl: Partial, gnn_transformer: Partial, llm: 'Yes', vlm: 'Yes', vla: 'Yes', social_capability_taxonomy: 'No', evidence_maturity_analysis: No (claimed on p.2; not located in text), evaluation_audit: Partial (metric lists per platform), deployment_analysis: Partial (qualitative latency; efficient VLMs), fm_reliability: 'Partial (inconsistent inference, grounding gaps; no hallucination keyword)', human_subject_evidence: No (calls for user studies), direct_overlap_with_our_survey: '11 of our 41 direct papers cited: 2025_Kawabata_SocialNav-MoE; 2025_Narasimhan_OLiVia-Nav; 2025_Payandeh_Social-LLaVA; 2025_Song_VLM-Social-Nav; 2026_Elnoor_ViLAM; 2026_Fang_Obstacles-to-Etiquette; 2026_Wang_MAction-SocialNav; 2026_Xiao_E-SocialNav; 2026_Zhang_Walk-With-Me; 2026_Zhang_GCL (related version [83]); 2026_Xiao_Prompting-VLMs-JSAI (related version [80])', basis: Stage-2 manual coding from survey note coverage/taxonomy + extracted-text keyword checks
      (2026-10-19); overlap is a lower bound (title/arXiv-id string match + manual).}
coding: {latency_reported: NA, safety_mechanism: NA, uncertainty_treatment: NA, hallucination_treatment: NA, code_released: NA, new_dataset_released: NA, real_robot: NA, human_subject_study: NA}
pdf_metadata_stage1:
  year: 2026
  authors: *id001
  venue: arXiv preprint (arXiv:2606.28760v1 [cs.RO], 27 Jun 2026)
  volume: Not reported
  issue: Not reported
  pages: 24 (PDF)
  doi: Not reported
  url: Not reported
  pub_status: preprint; survey/review
  peer_reviewed: 'No'
  peer_review_basis: PDF is arXiv v1 with no venue, acceptance statement or DOI (p.1). Status of any journal submission unknown.
external_verification:
  verified_on: '2026-10-19'
  status_class: 'C: preprint only'
  verified_venue: arXiv preprint (arXiv:2606.28760v1 [cs.RO], 27 Jun 2026)
  verified_doi: Not found / not applicable
  verified_url: https://arxiv.org/abs/2606.28760
  verified_pages: NA
  arxiv: 2606.28760v1
  version_relationship: arXiv only; v1 only
  sources: [arXiv abs page (2606.28760v1), 'Crossref title search: no match']
  peer_reviewed_note: No verified peer-reviewed version found as of corpus freeze date
  publication_status: Preprint
snei_usage: {reported_quantity: Not stated, unit: dataset entry (Table 2), what_it_represents: 'SNEI listed as robot-egocentric dataset [4]', page: p.12, remark: No size given, provenance_note: SNEI provenance (SCAND vs SCAND+MuSoHu) UNRESOLVED; see SNEI_DATASET_RECONCILIATION.md}
final_coding: {status: NA (survey)}
physical_source_folder: "00_Existing_Surveys"
analytical_category: "S0"
coding:
  latency_reported: "NA"
  safety_mechanism: "NA"
  uncertainty_treatment: "NA"
  hallucination_treatment: "NA"
  code_released: "NA"
  new_dataset_released: "NA"
  real_robot: "NA"
  human_subject_study: "NA"
---

# Vision-Language Models for Deployable Social Robot Navigation: Bridging Semantic Reasoning and Low-Level Control (Cai, Yamasaki, Xiao, 2026)

Page convention throughout: PDF page index (p.N), 1-based.

## A. Bibliographic information
- **Source PDF:** `00_Existing_Surveys/2606.28760v1.pdf` (24 pages)
- **Authors:** Runji Cai (Hokkaido Univ.), Toshihiko Yamasaki (Univ. of Tokyo), Ling Xiao (Hokkaido Univ., corresponding) (p.1)
- **Year:** 2026 (arXiv v1 dated 27 Jun 2026, p.1)
- **Venue / volume / issue / pages / DOI:** none stated; arXiv preprint only.
- **Publication status:** preprint; survey/review. **Peer-reviewed:** No (for this version). WEB_VERIFICATION_REQUIRED for later acceptance.
- **Note on author group:** Ling Xiao and T. Yamasaki are also authors of several direct papers in our corpus (E-SocialNav, SocialNav-MoE, GCL, MAction-SocialNav, MUSON, SOPD-SocialNav, JSAI 2026 prompting paper). The survey cites its own group's work extensively in §3.6 (p.10) and §5.

## B. Position within this survey
**S0 — Existing survey/review.** It is the most directly overlapping prior survey: it is the only survey in the corpus whose central object is VLM-based social robot navigation. It is the "critical competing survey" named in the Stage-1 brief. See `09_Project_Reports/COMPETING_SURVEY_DEEP_ANALYSIS.md` for the full comparison.

## C. Research problem (authors' claims)
- **Problem:** how to integrate VLMs into real-time, safety-critical navigation and translate high-level reasoning into grounded actions (abstract, p.1).
- **Claimed gap:** existing social-navigation surveys and VLM surveys address motion generation and vision-language reasoning "in isolation"; few examine the *bridging interface* (p.2, Table 1 p.3).
- **Stated contributions (p.2–3):** (1) working definition of VLM-based SRN as translating VLM reasoning into executable, safe, socially compliant behaviour, with roles of high-level reasoning, low-level planning/control and bridging (§2); (2) a taxonomy of five paradigms organised by interface, "explicitly annotating each paradigm with its level of supporting evidence" (§3); (3) analysis of datasets, evaluation platforms and open challenges (§4–5).
- **Our interpretation (flagged as ours):** Contribution (2)'s "evidence-level annotation" is not realised as an explicit label, table or figure annotation. Fig. 2 (p.7, visually inspected) shows five schematic paradigms without evidence labels; §3 prose describes example papers without an evidence scale. This is an observable absence, not a judgement of quality.

## D. Content — formal framework (§2, p.3–5)
- High-level module: B_t^h = Φ_θ(I_t, ρ_t) (Eq.1), with B_t^h = (r_t, q_t, M_t, z_t, a_t^h) — language reasoning/social-norm explanation, score/selector over candidates, semantic/queryable map, intermediate representation (waypoints/attention maps), high/mid-level action (Eq.2, p.4).
- Bridge: η_t = Γ_ω(B_t^h, o_t) = (g_t, ψ_t, u_t^h, λ_t, K_t): semantic subgoal, social-context descriptor (human occupancy, predicted motion, interaction graphs, passing preferences, norms), reference behaviour, adaptive cost weights, hard constraints (Eq.3, p.4).
- Bridge described as asynchronous: VLM latency "hundreds of milliseconds to several seconds" vs ≥~10 Hz control (p.4, citing FastVLM [33], [34], [35]).
- Low-level: receding-horizon trajectory optimisation (Eq.4–6), feasible set with obstacle clearance d_obs, social clearance d_min to predicted human states, and bridge constraints (Eq.5, p.5); cost = goal + obstacle + social + VLM-reference + legibility + naturalness terms with six adaptive weights (Eq.7–8, p.5).
- Principle stated: "keeps VLM reasoning separate from direct actuation" (p.3).

## E. Section structure (complete)
1 Introduction (p.1–3; Fig.1 Google-Scholar counts p.2; Table 1 positioning vs 12 prior surveys p.3)
2 A System-Level Formulation of VLM-Based SRN — 2.1 High-Level VLM Reasoning; 2.2 Bridging Definition; 2.3 Low-Level Planning and Control; 2.4 Closed-Loop Receding-Horizon Execution (p.3–5)
3 Coupling VLMs with SRN Systems (p.6–11) — 3.1 VLMs as High-Level Reasoners and Proposal Selectors; 3.2 VLMs as Evaluators; 3.3 VLMs for Semantic Map Grounding; 3.4 VLMs as Intermediate Representations; 3.5 VLMs as Action Interfaces; 3.6 Efficient VLMs in Deployable SRN. Figures: Fig.2 five paradigms (p.7); Fig.3 VLM-Social-Nav (p.7); Fig.4 VLMaps (p.9).
4 Datasets and Evaluation Platforms — 4.1 Datasets (Table 2, 14 datasets, p.12); 4.2 Evaluation Platforms (Table 3, 13 platforms, p.13)
5 Challenges and Future Directions — 5.1 High-Quality SRN Datasets; 5.2 Robust Social and Spatial Reasoning; 5.3 Reasoning to Control Grounding; 5.4 Real-Time Embodied Control; 5.5 Continual Adaptation; 5.6 Evaluation Beyond Success and Collision; 5.7 Generalization and Sim-to-Real (p.13–15)
6 Conclusion (p.15–16); References [1]–[124] (p.16–24)

## F. Papers discussed (as located in text)
**Direct VLM/LLM social-navigation papers explicitly discussed:** Social-LLaVA/SNEI [4] (p.6, p.11); Fang et al. "From Obstacles to Etiquette" [54] (p.7); VLM-Social-Nav [38] (p.7, Fig.3); ViLAM (cited as "Vi-LAD", arXiv:2503.09820) [70] (p.9); OLiVia-Nav [71] (p.9); Xiao & Yamasaki prompt design [80] (p.10); E-SocialNav [81] (p.10); SocialNav-MoE [82] (p.10); GCL [83] (IEICE tech. report; p.10); MAction-SocialNav [84] (p.10, "achieving 1.524 FPS"); MUSON [96] (dataset, p.11); SocialNav-SUB [110] (benchmark, p.12); Walk with me [78] (p.10); GazeNav [97] (dataset, p.11).
**Adjacent foundation-model works:** LLaMA-Adapter, TPVQA, VLM-PC, SpatialVLM, SpatialRGPT, LeLaN, Navi2Gaze, Mem2Ego (§3.1); Kwon reward design, VLM-RMs, LIV (§3.2); CLIP-Fields, cross-modal map learning, LM-Nav, VLMaps, OpenScene, ConceptGraphs, ConceptFusion, VLFM, multimodal spatial language maps (§3.3); NaviLLM, Octopus, Chen et al. affordance-oriented VLN, Stadler (§3.4); RT-2, OpenVLA, Octo, NaVid, Code as Policies, PaLM-E, NaVILA, ViNT, OmniVLA (§3.5); VILA, FastVLM (§3.6).
**Learning/classical background:** Helbing social force [44], DWA, TEB, RRT, PRM, Kretzschmar IRL [15], Social-LSTM [31], Social-STGCNN [32], DR-MPC [116], SELFI [117], ProxEmo [118].
**Not cited although in our corpus (observation, our check):** GSON, CoNVOI, BehAV, VL-TGS, AutoSpatial, Bidirectional NL conversation LLM navigation (IROS 2025), Perception–Awareness–Decision (HRI 2026 companion), SocialNav (Chen, CVPR 2026), HA-VLN (NeurIPS 2024), HA-VLN 2.0, NaviSTAR, HCSG (arXiv May 2026); and post-cut-off G2-Nav (arXiv 18 Jul 2026), SOPD-SocialNav (arXiv 22 Jul 2026).

## G–M. (Not applicable: survey has no experiments, metrics, results or deployment.)

## N. Limitations
1. **Authors' explicitly stated limitations of the survey itself:** none stated.
2. **Authors' future directions (§5):** datasets jointly aligning perception, social annotation, planning representation, action labels and human feedback; robust spatial/temporal/social reasoning with uncertainty; explicit validated bridging representations (cost maps, rewards, waypoints, constraints, attention maps, interaction graphs); lightweight real-time control (quantization, distillation, action chunking, hybrid architectures); continual/online adaptation; evaluation beyond success/collision (proxemics, comfort, compliance, preference, rationale–action consistency, instruction-following); cultural/embodiment generalization and sim-to-real.
3. **Directly observable methodological constraints:** no search protocol, inclusion/exclusion criteria or paper counts (only raw Google-Scholar hits, p.2); no per-paper classification table of VLM-SRN methods; claimed per-paradigm evidence annotation not found as an explicit annotation (p.2 vs §3/Fig.2); taxonomy has a single (interface) dimension; social capabilities are not systematically tabulated; real-robot vs simulation vs offline evaluation not tabulated per paper; many §3 exemplars are non-social (manipulation, VLN, object-nav).
4. **Our survey-level interpretation:** deferred to Stage 2 / COMPETING_SURVEY_DEEP_ANALYSIS.md.

## O. Reproducibility
Not applicable (survey). No supplementary table or paper list released.

## P. Special survey analysis
- **Exact scope:** VLM-based SRN with focus on the high-level-to-low-level bridging interface and deployability.
- **Years:** prior-survey table spans 2013–2025; VLM-SRN citations 2023–2026.
- **Databases/search strategy/inclusion/exclusion:** not reported.
- **Number of references:** 124.
- **Taxonomy:** five interface paradigms + efficiency subsection (one dimension).
- **Major figures:** Fig.1 raw Google-Scholar counts (visually verified, p.2): stacked-bar totals 177 (2022), 199 (2023), 290 (2024), 431 (2025); of which "VLM-related SRN records" 30, 37, 104, 245 respectively. These are search hits, not screened papers; Fig.2 five paradigms; Fig.3 VLM-Social-Nav; Fig.4 VLMaps.
- **Major tables:** Table 1 positioning vs 12 surveys (Kruse 2013, Rios-Martinez 2015, Chik 2016, Charalampous 2017, Cheng 2018, Lambert 2020, Möller 2021, Wang 2022, Mavrogiannis 2023, Mirsky 2024, Singamaneni 2024, Francis 2025); Table 2 14 datasets (viewpoint, horizon, language, social context, output annotation); Table 3 13 platforms (type, target, social factors, metrics, scenario).
- **Main conclusions:** hierarchical hybrid architectures are "among the most practical directions" (p.16); key challenge is translating VLM reasoning into real-time, safe, executable actions.
- **Coverage:** classical (Partial — one paragraph p.6), human-aware/proxemics (Partial — mentioned in intro/§5.7), prediction (Partial — in formulation), IL/DRL/GNN (Partial — background only), LLM/VLM/FM/VLA (Yes), LVLM (Partial — not distinguished), real-world deployment (Partial — discussed as challenge, not tabulated), evaluation (Partial — Table 3 and §5.6).

## Q. Cited works possibly missing from our corpus
See `cited_missing` in front matter; highest relevance: "Probing prompt design..." (arXiv:2601.14622), Walk with me (arXiv:2604.26839), GazeNav (AAAI 2026), NaVILA, OmniVLA, NaVid, SACSoN, SELFI, DR-MPC, Social Navigation Protocol (Pirk 2022), SocialGym 2.0, HuNavSim, SEAN 2.0, Habitat 3.0.

## R. Stage-2 external verification (2026-10-19)
- Externally verified: C: preprint only; venue arXiv preprint (arXiv:2606.28760v1 [cs.RO], 27 Jun 2026); DOI Not found / not applicable; pages NA; URL https://arxiv.org/abs/2606.28760.
- Sources: arXiv abs page (2606.28760v1); Crossref title search: no match.
- Version relationship: arXiv only; v1 only.
- Changed field - doi: PDF-derived 'Not reported' -> externally verified 'Not found / not applicable'
- Changed field - url: PDF-derived 'Not reported' -> externally verified 'https://arxiv.org/abs/2606.28760'
- Changed field - pub_status: PDF-derived 'preprint; survey/review' -> externally verified 'preprint'
- PDF-derived values are preserved in `pdf_metadata_stage1`; publisher metadata supersedes PDF metadata for bibliographic fields only. Methods and results remain sourced from the paper itself.

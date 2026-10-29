# Supplementary Material

**From Proxemics to Foundation Models: A Survey of Socially Aware Robot Navigation**

This supplement contains the screening records, per-work coding tables and supporting analyses underlying the survey. The main manuscript presents condensed summaries, while the supplementary tables provide the corresponding detailed records. Each table is also provided as a machine-readable CSV file (`Supplementary_Data_tables_CSV.zip`). The discussion is in the main manuscript and is not repeated here.

**Literature cut-off:** 19 October 2026. The final coverage search was conducted on 26 October 2026 and restricted to works dated up to the literature cut-off.

| Corpus component | n |
|---|---|
| Unique works | 98 |
| Direct foundation-model (FM) social-navigation papers | 45 |
| Classical and learning-based works | 12 |
| Adjacent FM navigation works | 13 |
| Datasets, simulators and benchmarks | 15 |
| Surveys | 13 |
| Representative pre-FM comparison set (not exhaustive; outside the corpus count; includes the 12 classical and learning works) | 40 |

## Contents

| Item | Content | Relation to the manuscript |
|---|---|---|
| Table S1, part A (`S1_screening_record.csv`) | Part A: all 284 candidates identified in the expansion search and the final cut-off check (three arXiv search passes, general web search, backward citation chasing; arXiv, Crossref and proceedings at the cut-off), each with its screening level, decision and reason | Section 2.2 |
| Table S1, part B (`S1b_final_search_record.csv`) | Part B: all 270 unique works of the final coverage search (IEEE Xplore, OpenAlex, forward citation chasing, and a limited manual Google Scholar check of one results page; Google Scholar was not searched systematically), with retrieval source, decision and reason; lists the 3 unresolved works | Section 2.2 |
| Table S2 (`S2_publication_status.csv`) | Publication status of all 98 corpus works: venue, status class, peer review, DOI and relation of the analysed copy to the published version | Section 2.4; Table S11 |
| Table S3 (`S3_adjacent_foundation_models.csv`) | The 13 adjacent FM navigation works: mechanism, task, concept inherited by social-navigation methods, and why each is *not* evidence of social competence | Section 4 |
| Table S4 (`S4_full_final_coding.csv`) | Final coding of the 85 non-survey corpus works on Dimensions A, B, D and E, with evaluated (Yes) and addressed-only (Partial) capability leaves | Sections 5-9 |
| Table S5 (`S5_prefm_comparison_set.csv`) | The 40-work representative pre-FM comparison set: selection, coding source, links and coding (part A); summary by paradigm (part B, `S5b_prefm_by_paradigm.csv`; formerly main-text Table 4) | Sections 2.3, 3 and 7 |
| Table S6 (`S6_robustness.csv`) | Headline counts for all direct papers, the peer-reviewed subset and papers public before the Cai et al. cut-off | Section 10.5 |
| Table S7 (`S7_capability_coverage.csv`) | Capability counts per leaf: direct evaluated and addressed, pre-FM evaluated, datasets evaluated | Section 7; Fig. 7 |
| Table S8 (`S8_code_dictionary.csv`) | Full code dictionary of the five coding dimensions and the cross-cutting attributes | Section 5; Fig. 4 |
| Table S9 (`S9_interface_evidence.csv`) | Counts behind Fig. 6: papers per interface and, within them, systematic robot evaluation, FM-independent safety guard and remote inference; evidence by publication year | Sections 5 and 9; Fig. 6 |
| Table S10 (`S10_metric_families.csv`) | Full metric-family table (formerly a main-text table): metric names found, level, what each family measures and fails to measure, direct papers using it | Section 8; Fig. 8 |
| Table S11 (`S11_direct_architecture.csv`) | Per-paper architecture of every direct paper: publication status, FM models, inputs, Dimensions A, B and D, planner or controller, temporal coupling, FM-independent safety guard, other attributes and main contribution (formerly main-text Table 5) | Sections 5 and 6; Table 4 |
| Table S12 (`S12_direct_evidence.csv`) | Per-paper evaluated capabilities and evidence: EV1-EV6, trials, statistics, key metrics, runtime, uncertainty, hallucination mitigation, code/data release and key limitation (formerly main-text Table 6) | Sections 6, 7 and 9 |
| Table S13 (`S13_datasets_benchmarks.csv`) | Per-resource inventory of datasets, simulators and benchmarks: size, sensors, human trajectories, group/intention, preference and multi-action labels, closed loop, VLM-readiness, FM role and limitations (the main-text Table 5 groups them into families) | Section 8; Table 5 |
| Fig. S1 | FM roles (Dimension B) per direct paper, grouped by primary interface | Section 5.2; Table S11 |
| Fig. S2 | Evidence profile (Dimension E) per direct paper, grouped by primary interface | Section 9; Table S12 |
| Fig. S3 | Capability coding (Dimension C) per direct paper | Section 7 |
| Fig. S4 | Dated timeline of the paradigms of social representation (overlapping bands; no causal ordering) | Section 3; Table 3 |

## Notation

**Publication status (S2; Status column of S11):**

| Class | Meaning |
|---|---|
| A | Published and peer-reviewed, verified against a publisher record |
| B | Accepted according to the authors (or, for one work, a citing paper); proceedings not yet indexed at the cut-off |
| C | Preprint only |
| D | Conference paper; acceptance verified, peer-review status not independently established |

Classes B and D are never counted as peer-reviewed.

**Screening (Table S1):** part A records the expansion search and the final cut-off check (19 October 2026); part B records the final coverage search (26 October 2026). The two records are kept separate and their counts are not merged.
- *First found* and *Found in passes* (part A): P1–P3 are the three arXiv search passes, plus "web", "citation" and "final check" (the final cut-off check).
- *Screening level*: title/abstract or full text.
- *Decision* (part A): INCLUDE; EXCLUDE; BACKGROUND ONLY (cited but not coded); RELATED VERSION (an alternative version of a corpus work); EXCLUDE (WITHDRAWN). For included works, *Corpus entry* gives the citation key used in the manuscript.
- *Decision* (part B): INCLUDE; EXCLUDE; UNRESOLVED (not coded: full text not accessible); ALREADY KNOWN (already in the corpus or the part A record); ALREADY SCREENED (screened in part A under a title variant).
- Exclusion reasons (parts A and B; criteria A–C as defined in manuscript Section 2.1). Many records give a specific reason in place of, or after, the code:

| Code | Reason |
|---|---|
| R1 | Not robot/embodied navigation (fails A) |
| R2 | Autonomous driving, UAV or other non-ground-robot domain (fails A) |
| R3 | Robot manipulation / HRI / perception without mobile-navigation behaviour (fails A) |
| R4 | Embodied/robot navigation without an explicit social-navigation capability (fails C) |
| R5 | Social navigation without an FM role in the navigation method (fails B) |
| R6 | Navigation assistance for people: the person navigates, not a robot (fails A) |
| R7 | Survey, review, position paper or thesis outside the screening scope; surveys enter the corpus only through the seed set (part B only) |
| R8 | Central claims or data not verifiable after full-text assessment, irrespective of publication status (exclusion rule in manuscript Section 2.2; one record, part B only) |

**Taxonomy abbreviations (S4, S11, S12):**

| Dimension / attribute | Codes |
|---|---|
| A, social representation (multi-label) | A0 not represented · A1 kinematic agent · A2 predicted motion · A3 social-space field · A4 relational structure · A5 symbolic/linguistic · A6 implicit/latent |
| B, FM role (multi-label) | R1 scene/context interpretation · R2 human-state/relation inference · R3 social-norm reasoning and behaviour selection · R4 instruction/preference grounding · R5 human-facing communication |
| C, social capability (15 leaves) | SAF1 collision · SAF2 near-collision/risk margin · SPA1 personal space · SPA2 group/conversation space · SPA3 encounter conventions · SPA4 crowd navigation · HUM1 motion understanding/prediction · HUM2 intention/activity · NOR1 etiquette/politeness · NOR2 explicit social-instruction following · NOR3 context-dependent conduct · NOR4 cultural/norm adaptation · EXP1 perceived safety/comfort · EXP2 legibility/predictability · EXP3 naturalness |
| C values | **Yes:** evaluated using a dedicated metric or a systematic scenario-specific success criterion that required the capability. **Partial:** addressed without such a measure. An evaluated capability is also addressed, so addressed counts comprise Yes and Partial. |
| D, navigation interface (categorical, not a maturity order) | D0 non-executed decision · D1 semantic/social state · D2 candidate selection · D3 objective/constraint/parameter shaping · D4 goal/waypoint/trajectory · D5 runtime latent conditioning · D6 direct action · D7 training-time supervision · D8 human-facing channel |
| E, evidence profile (one dimension represented through six separately coded attributes; not combined into a score) | EV1 offline evaluation · EV2 closed-loop simulation · EV3 physical-robot evidence (none/demo/systematic) · EV4 real people in robot trials (none/simulated-only/staged/unscripted/present-type-unreported/not-reported) · EV5 human evaluation (none/text raters/observers-video/co-present participants) · EV6 open-world or long-duration deployment. EV3, EV4 and EV5 record different forms of evidence and are not interchangeable |
| Cross-cutting attributes (S11, S12) | temporal coupling · FM-independent safety guard · uncertainty treatment · hallucination mitigation · inference location · memory · privacy constraint |

**Reporting conventions:**
- Details a paper does not report are coded "Not reported". Counts are therefore lower bounds.
- Runtime, trial and metric entries are given as the papers report them, and are not comparable across papers.
- Table S10 counts studies reporting a runtime or latency evaluation metric (21/45). In addition, 2 direct studies report numeric runtime or latency in their system descriptions or discussion but not as an evaluation metric; these are included in the 23/45 overall runtime-reporting count (Table S12, *Runtime reported*) but not in this metric-family count.

## Note on the SNEI dataset (main-text Table 5; Tables S4 and S13)

SNEI quantities differ across sources and are not interchangeable:
- the originating paper reports about 2K social scenarios, 1,961 images (summed over interaction types) and more than 40K question–answer pairs;
- the public release contains 1,508 annotated rows in two batches;
- one paper reports 810 conversations, which equals the first public batch;
- several papers use a 325-image subset (265 training / 60 test).

Its source data are reported inconsistently: the originating paper describes it as built from SCAND, while a later paper by a different group states SCAND and MuSoHu. This discrepancy could not be resolved from the available records. The sensor entry "front-facing robot RGB image (from SCAND)" in Table S13 records the originating paper's statement.

**Pre-FM comparison set (S5):** "Not determinable" marks evidence that the reference-survey descriptions used for coding do not establish; such works are excluded from evidence denominators. Every work in Table S5 (parts A and B) is cited by its key and listed in full in the reference list at the end of this supplement.

## Reproducibility

- Every table in this supplement, like every count in the manuscript, is generated from the per-paper records.
- Coding followed the five-dimensional scheme defined in the main manuscript (Section 5). Repeat-coding and metric-based consistency checks (Section 2.5) were used to assess internal consistency; these checks do not constitute inter-rater reliability.

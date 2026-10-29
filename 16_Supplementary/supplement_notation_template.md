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
- Table S10 counts studies reporting a runtime or latency evaluation metric (@QF25_metric@). In addition, @QF25_textonly:n@ direct studies report numeric runtime or latency in their system descriptions or discussion but not as an evaluation metric; these are included in the @QF25@ overall runtime-reporting count (Table S12, *Runtime reported*) but not in this metric-family count.

## Note on the SNEI dataset (main-text Table 5; Tables S4 and S13)

SNEI quantities differ across sources and are not interchangeable:
- the originating paper reports about 2K social scenarios, 1,961 images (summed over interaction types) and more than 40K question–answer pairs;
- the public release contains 1,508 annotated rows in two batches;
- one paper reports 810 conversations, which equals the first public batch;
- several papers use a 325-image subset (265 training / 60 test).

Its source data are reported inconsistently: the originating paper describes it as built from SCAND, while a later paper by a different group states SCAND and MuSoHu. This discrepancy could not be resolved from the available records. The sensor entry "front-facing robot RGB image (from SCAND)" in Table S13 records the originating paper's statement.


# Stage-1 analysis pipeline

Notes (`08_Paper_Notes/*.md`, YAML front matter) are the single source of truth. Everything else is generated.

| Step | Script | Output |
|---|---|---|
| 0 | `extract.py` (pdftotext, already run) | `extracted_text/*.txt`, `pdf_inventory.json` |
| 1 | `parse_test.py` | sanity check: all 67 notes parse |
| 2 | `add_coding.py` | `coding:` block in each note + `coding_rules.json` (idempotent) |
| 3 | `build_matrices.py` | the 12 CSV matrices in `07_Literature_Analysis/` |
| 4 | `compute_counts.py` | `07_Literature_Analysis/corpus_counts.json` (reads CSVs only) |
| 5 | `gen_summary.py`, `gen_inventory.py` | `09_Project_Reports/CORPUS_SUMMARY.md`, `CORPUS_INVENTORY.md` |
| 6 | `cai_overlap.py` | `cai_citation_overlap.csv`, `cai_overlap_summary.json` |
| 7 | `missing_lit_scan.py` → `gen_missing_lit.py` | `missing_lit_citers.csv` → `09_Project_Reports/POTENTIAL_MISSING_LITERATURE.md` |
| 8 | `gen_findings.py` | `09_Project_Reports/PRELIMINARY_EVIDENCE_FINDINGS.md` |

Hand-written reports (they cite the generated numbers): `DATA_QUALITY_ISSUES.md`, `COMPETING_SURVEY_DEEP_ANALYSIS.md`, `VALIDATION_AUDIT.md`.

Other files:
- `dq_log_raw.md`: running data-quality log.
- `cited_missing_raw.tsv`: raw `cited_missing` entries from the notes.
- `note_progress_log.md`: extraction log.

## Stage 2 (corpus freeze 2026-10-19)

Scripts live in `stage2/`; run from that directory unless noted.

1. **Metadata and search** (network; cached; re-run not required):
   - `harvest_meta.py` → `cache/`
   - `arxiv_search.py`, `arxiv_search_pass2.py`, `arxiv_search_pass3.py` → `search/`
   - `fetch_arxiv_text.py` → `fulltext/`
   - `candidate_lookup.py` → `cache_candidates.json`
2. **New notes and metadata application:**
   - `notes_batch1.py` … `notes_batch4.py` use `notes_lib.write_note`.
   - `apply_verified_metadata.py` writes `verified_metadata.yaml`, the `pdf_metadata_stage1` blocks and body section R.
   - `survey_coverage.py` writes `survey.stage2_coverage`.
   - `snei_fields.py` writes the `snei_*` fields and the `snei_usage` blocks.
   - `extract_new.py` extracts text for the downloaded PDFs (`downloads_log.csv`).
3. **Shared pipeline** (from `_tools/`), in order:
   `add_coding.py` → `build_matrices.py` → `compute_counts.py` → `gen_summary.py` → `gen_inventory.py` → `cai_overlap.py` → `missing_lit_scan.py` → `gen_missing_lit.py` → `gen_findings.py` → `parse_test.py`.
4. **Stage-2 reports** (from `stage2/`):
   `screening.py` → `gen_stage2_reports.py` (MISSING_LITERATURE_DECISIONS, TARGETED_SEARCH_LOG, SEARCH_SATURATION_REPORT, PUBLICATION_STATUS_AUDIT) → `gen_freeze.py` (STAGE2_CORPUS_FREEZE).
5. **Hand-written reports**, which cite the generated numbers: SNEI_DATASET_RECONCILIATION, DATA_QUALITY_ISSUES (§12 status table), COMPETING_SURVEY_DEEP_ANALYSIS (§S), SURVEY_POSITIONING_EVIDENCE, EXCLUDED_WITHDRAWN_WORKS.
6. **Backups:**
   - `stage2/backup_notes_stage1/` (the 67 Stage-1 notes before metadata application);
   - `stage2/pdf_inventory_stage1.json`;
   - `stage2/*_stage1.md` (previous report versions).

## Stage 3 (taxonomy freeze 2026-10-19)

**Scripts in `stage3/`:**
- `load.py`
- `recode.py`: blind first recode, R/X/V
- `second_pass.py`: stratified second pass
- `final_codes.py`: authoritative definitions and manual codes (Axis A, roles, interfaces, evidence)
- `propagate.py`: writes `final_coding` to notes

**Mapping:** `stage3/legacy_to_final_mapping.csv`.

**Re-run order after any change:**
`stage3/propagate.py` → `add_coding.py` → `build_matrices.py` → `compute_counts.py` → `gen_summary.py` → the remaining Stage-2 generators.

**Columns:**
- Matrices expose `final_*` columns (authoritative) and `legacy_*` columns (provenance).
- `corpus_counts.json` → `final` holds the authoritative counts.

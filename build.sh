#!/usr/bin/env bash
# Rebuild every generated record, table and figure and the supplementary material from the coding records.
#   ./build.sh
# The supplement PDF is rebuilt only if XeLaTeX is installed.
set -euo pipefail
cd "$(dirname "$0")"
for s in 07_Literature_Analysis/_tools/stage9/build_prefm_set.py 07_Literature_Analysis/_tools/stage9/prefm_analysis.py 13_References/build_bib.py 10_PreWriting/build_findings.py 11_Tables/build_tables.py; do
  python3 "$s" > /dev/null
done
for s in F1_publication_evolution/make_f1.py F8_screening_flow/make_f8.py F9_evolution_timeline/make_f9.py F12_interface_evidence/make_f12.py F13_metric_prevalence/make_f13.py F6_taxonomy/make_f6.py F7_pipeline/make_f7.py \
         F10_fm_prefm_comparison/make_f10.py F2_functional_roles/make_f2.py F3_social_capabilities/make_f3.py F4_evidence_profile/make_f4.py; do
  python3 "12_Figures/$s" > /dev/null
done
python3 16_Supplementary/build_supplement.py > /dev/null
if command -v xelatex > /dev/null; then python3 16_Supplementary/build_supplement_pdf.py; else echo "xelatex not found: supplement PDF not rebuilt"; fi
python3 tools/make_readme.py

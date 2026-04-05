# Ingestion Log

Append-only record of what was processed and when.

---

## [2026-04-04] calibration | VACE wiki page compiled from all 15 wan extraction files

**Type:** Calibration test — topic-focused compilation (not standard file-by-file ingestion)

**Sources scanned:** All 15 wan_*_knowledge.md files (4,667 VACE mentions total)

**Pages created:**
- `wiki/wan/models/vace.md` (538 lines)

**Method:** Extracted all VACE-related items across all files, deduplicated, synthesized into single comprehensive page. This was a calibration test to validate the wiki compilation approach before beginning standard chronological ingestion.

---

## [2026-04-05] topic | Wan 2.1 wiki page compiled from all 17 wan extraction files

**Type:** Topic-focused compilation

**Sources scanned:** All 17 wan_*_knowledge.md files (1,098 explicit Wan 2.1 mentions + implicit content from pre-2.2 months)

**Pages created:**
- `wiki/wan/models/wan-2.1.md` (614 lines)

**Method:** Extracted Wan 2.1 foundation content across all files. Early months (Feb-June 2025) treated as implicitly-2.1 since 2.2 didn't exist yet. Later months filtered for "still use 2.1" insights and 2.1 vs 2.2 comparisons. Covers architecture, variants, settings, precision, optimization, quirks, derived models, and timeline.

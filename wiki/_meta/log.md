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

---

## [2026-04-05] topic | Wan 2.2 wiki page compiled from 14 wan extraction files

**Type:** Topic-focused compilation

**Sources scanned:** 14 wan_*_knowledge.md files with 2.2 content (~5,000+ mentions, heaviest in Jul-Sep 2025 post-launch months)

**Pages created:**
- `wiki/wan/models/wan-2.2.md` (456 lines)

**Method:** Extracted Wan 2.2 content from launch (Jul 2025) through Feb 2026. Covers MoE architecture (high-noise/low-noise experts), A14B and TI2V-5B variants, settings tables, 2.1 vs 2.2 comparison, speed LoRAs (LightX2V versions, Lightning, Dyno, rCM), LoRA compatibility matrix, quirks (VAE mismatch, CLIP vision removed), hardware, and derivative ecosystem. Resolved contradictions: 16fps native for 14B (not 24), LN works reliably with 2.1 LoRAs, HN is "soul" of 2.2.

---

## [2026-04-05] topic | WanAnimate wiki page compiled from wan extraction files

**Type:** Topic-focused compilation

**Sources scanned:** 14 wan_*_knowledge.md files, 683 mentions (heaviest in Sep 2025 launch month, 216 mentions)

**Pages created:**
- `wiki/wan/models/wananimate.md` (401 lines)

**Method:** Extracted WanAnimate content from Sep 2025 launch through Feb 2026. Covers animation + replacement modes, pose/canny/face/mask inputs, block scaling (0-15), CFG/Chinese prompt quirk, 12 vs 16 vs 24fps debate, VitPose for animals, pupil tracking, long video dimensions (÷16), LoRA compat, and comparisons to VACE/Phantom/SCAIL/commercial tools. Validated all CLAUDE.md research notes against raw extractions. Flagged unresolved contradictions: 12 vs 24fps (Kijai vs NC17z), Phantom vs WanAnimate likeness quality.

---

## [2026-04-06] topic | Phantom wiki page compiled from wan extraction files

**Type:** Topic-focused compilation

**Sources scanned:** 16 of 17 wan_*_knowledge.md files, 967 mentions (heaviest May-Aug 2025)

**Pages created:**
- `wiki/wan/models/phantom.md` (325 lines)

**Method:** Extracted Phantom content across full timeline. Covers temporal latent encoding architecture, 1-4 reference images, key settings (CFG 5, 20 steps, 121 frames), VACE merge technique, comparison to MAGREF/WanAnimate/VACE ref/IP-Adapter/LoRA approaches, 15 quirks, 17 troubleshooting entries, LoRA compat (CausVid/LightX2V/FusionX), hardware benchmarks, timeline Apr-Dec 2025.

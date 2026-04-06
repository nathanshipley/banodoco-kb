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

---

## [2026-04-06] PIVOT | Fact-checking error discovered, switching to verified weekly pipeline

**Type:** Process change

**What happened:** During spot-checking of the WanAnimate page, Nathan identified that the "Inputs" section incorrectly attributed canny and depth map capabilities to WanAnimate. These are actually VACE features. The extraction summaries had conflated the two because Discord conversations often discuss multi-model workflows (e.g., "I used VACE canny with my WanAnimate pipeline") and the Sonnet extraction step stripped that context, producing bullet points like "WanAnimate: inverted canny required" — which is wrong.

**Verification with NotebookLM confirmed:** WanAnimate only accepts pose data (DWPose/OpenPose) and face control signals. Canny, depth, and line art are strictly VACE/Fun Control features.

**Root cause:** The extraction files (data/wan_*_knowledge.md) are lossy Sonnet summaries of 400-message chunks. When conversations span multiple models, the extraction step can strip the context about which capability belongs to which model. The wiki compilation agents — working only from these summaries — lack the domain knowledge to catch the conflation. This isn't just a WanAnimate problem; the same error pattern could exist in any compiled page.

**Decision: pivot to a verified, weekly, raw-message pipeline.** Inspired by pom's brain-of-bndc pattern (Claude generates, GPT-5.2 with high reasoning fact-checks against raw sources).

**New pipeline:**
1. Pull raw Discord messages from Supabase, store locally by channel/week
2. Process chronologically in weekly chunks (not monthly, not topic-focused) — this matches Karpathy's "work it in stages" advice and how knowledge actually accumulates
3. Each weekly pass updates relevant wiki pages
4. GPT-5.2 verification pass checks every claim against the raw messages for that week
5. Corrections applied before moving to next week

**Why weekly:** Monthly is too coarse — model launch weeks can have 10x normal traffic and knowledge changes rapidly. Weekly matches how a real person would follow along.

**Why raw messages:** The extraction summaries are where context gets lost. Verification against summaries won't catch errors introduced at the extraction step. Raw messages preserve the full conversation context needed to determine which model a capability belongs to.

**Status of existing pages:** VACE, Wan 2.1, Wan 2.2, WanAnimate, and Phantom pages remain in the wiki but are flagged as UNVERIFIED. They were compiled from extraction summaries and may contain similar conflation errors. They will be re-verified (and corrected) once the new pipeline is operational.

**Blocked on:** Updated Supabase API key (legacy keys disabled April 2) and OpenAI API key for GPT-5.2 verification.

---

## [2026-04-06] infrastructure | Raw message pull + GPT-5.4 verification pipeline built

**Type:** Pipeline infrastructure

**Raw messages pulled:** 286,616 messages across 5 Wan channels, stored as 246 weekly JSON files in `data/raw/`. Each message includes content, author name, reply reference (reference_id), emoji reactions with reactor names, edit history, attachments, pins, thread IDs. Deleted messages filtered out.

| Channel | Messages | Weeks |
|---------|----------|-------|
| wan_chatter | 220,500 | 59 |
| wan_gens | 23,476 | 58 |
| wan_training | 21,358 | 56 |
| wan_comfyui | 11,582 | 28 |
| wan_resources | 9,700 | 45 |

**Verification pipeline built:** `scripts/verify_wiki.py` — cross-checks wiki pages against raw Discord messages using GPT-5.4. Automatically finds the densest weeks for a topic, loads relevant messages + reply context, sends to GPT-5.4 with a structured prompt checking for 6 error types (capability conflation, model confusion, unsupported claims, misinterpretation, invented details, opinion as consensus). Outputs JSON report to `wiki/_meta/verification/`.

**First verification test — WanAnimate page:**
- Checked against top 3 weeks (W38, W39, W45 — 573 relevant messages)
- Found 8 high-severity issues, 32 medium, 1 low
- Confirmed the known canny/depth conflation error (flagged as capability_conflation in all 3 weeks)
- Also caught: unsupported trajectory/ATI claims, invented attribution quotes, depth maps incorrectly attributed to WanAnimate
- 46 claims verified OK (core architecture, 77-frame chunking, replacement mode, face tracking)
- Cost: ~$0.28 for 3-week verification
- GPT-5.4 selected over GPT-5.2 (latest model, marginal price increase, better reasoning)

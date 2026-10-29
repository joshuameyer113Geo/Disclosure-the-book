---
name: disclosure-historian-research
description: Research pass for the documentary book Disclosure. Use when adding or verifying entries in history/.
---
1. Use live web, archive, government, and press sources only. Never cite from memory. Give 2 or more URLs per claim, preferring primary, government, and major-press sources. Label Wikipedia and fan sites "(supporting)".
2. Every entry has a date, a place, the people (named only as the sources name them), and a Tag: **Reported fact** / **In between** / **Lore**. An entry only needs to be part of the recorded record, not proven ("X testified" is a fact; what X claimed is recorded as a claim). Mark claims DISPUTED or UNCONFIRMED where needed.
3. Add a `Motive/credibility note (Writer's territory)`: analysis, not fact.
4. **Source-log rule: every new claim must add or reuse an S- entry in history/SOURCES.csv** (S-NNNN IDs are permanent and append-only; reuse the existing S- ID for the same URL). Then regenerate SOURCES.md and CLAIMS_REGISTER.* with build_registers.py, keeping existing S- numbers stable. Record the date consulted and the verification status.
5. Log gaps in OPEN_QUESTIONS.md. Never delete a claim; mark it RETIRED instead.

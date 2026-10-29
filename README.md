# Disclosure

A realistic historical documentary book on the UFO phenomenon: a sociological read on ufology, from ancient lore to modern military cases and the government disclosure debate, followed by labeled projections.

## Structure: 45 chapters in five parts
- **Part I: Ancient History** (chapters 1-9)
- **Part II: Modern and Military Cases** (chapters 10-26)
- **Part III: Sociology and Culture** (chapters 27-32)
- **Part IV: Government Disclosure** (chapters 33-41)
- **Part V: Projections** (chapters 42-45), each labeled PROJECTION and grounded in the Part IV record

All chapters are currently lineouts (purpose + sources), not drafted.

## Repository layout
- `outline/OUTLINE.md`: the 45-chapter lineout; source of truth for chapter order
- `manuscript/part-1..part-5/chNN.md`: chapter stubs matching the outline numbering
- `history/`: Eden Historian's research. `TIMELINE.md` entries carry claim IDs `T-NNN`; `MODERN_CASES_FACTS.md` entries carry `MC-NNN`. Also `ID_INDEX.md`, `ANCIENT_LORE.md`, and `OPEN_QUESTIONS.md` (remaining research items)
- `research/`: research briefs (ANCIENT_TIMELINE.md, MODERN_CASES.md)
- `rules/STORY_RULES.md`: canon rules and footnote convention
- `notes/`: REUSE_REVIEW.md, PUBLISHING_PLAN.md
- `imagery/`: timeline images

## Context harness
- `CONTEXT.md`: project state file (structure, constraints, book state, flagged ambiguities)
- `AGENTS.md`, `NOW.md`: agent instructions and current focus
- Verify with `node scripts/context-index.js check`

## Footnotes and claim IDs
Footnote only claims that need it, as `[^T-NNN]` or `[^MC-NNN]` keyed to the historian IDs in `history/`. No historian entry means a research gap, not a footnote.

## Canon rules
Real people keep real names. Real reported events and established UFO lore are canon. Nothing is invented: no fake names or places. Artistic symbolism and creative filling-in are allowed only when grounded in researched context, with sources cited.

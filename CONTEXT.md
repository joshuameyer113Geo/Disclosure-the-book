# Context
<!-- context-harness:schema v3 -->

## Project
Disclosure: a realistic documentary history of the UFO phenomenon, from ancient texts to the October 2026 disclosure record, then labeled projections. Plain markdown book; no build.

## Structure
- outline/OUTLINE.md: 45-chapter lineout (purpose + sources per chapter); source of truth for order
- manuscript/part-1..part-5/chNN.md: chapter stubs (lineout only, no prose yet)
- history/TIMELINE.md [T-NNN], history/MODERN_CASES_FACTS.md [MC-NNN]: historian claim files (IDs used in footnotes)
- research/ANCIENT_TIMELINE.md, research/MODERN_CASES.md: research briefs
- rules/STORY_RULES.md: canon rules + footnote convention
- QUESTIONS-LOG.md, notes/: questions, reuse review, publishing plan

## Operating Constraints
- Real people keep real names; real reported events and established lore only; nothing invented; symbolism only when grounded in cited research.
- Nordic and reptilian beings are modern lore: always name the originators (contactee era / George Adamski; David Icke) and never present them as ancient fact.
- Projection chapters (Part V) must be labeled PROJECTION and grounded in the Part IV record.
- Footnote only claims that need it, as [^T-NNN]/[^MC-NNN] keyed to historian IDs; no historian entry = research gap, not a footnote.
- research/MODERN_CASES.md may be under edit by another worker: coordinate before touching; pull --rebase before pushing.

## Workflow
- Setup: none (plain markdown)
- Run: none
- Verify: node scripts/context-index.js check

### Verification
- Every chapter stub lists sources; every footnote ID exists in history/.

## Language
- **Claim ID**: historian entry ID, T-NNN (history/TIMELINE.md) or MC-NNN (history/MODERN_CASES_FACTS.md). Avoid: raw URL as footnote key.
- **Lineout**: chapter title + one-line purpose + sources, no prose.

## Relationships
- OUTLINE.md order == manuscript chNN numbering.

## Book State
- Chapters: 45 (Part I ancient history 9 = 20%; II modern/military 17; III sociology/culture 6; IV government arc 9; V projections 4). All status: lineout, not drafted.
- Decisions: 2026-10-28 documentary (not dramatization); chronological order ancient to present then projections; history ~20%; footnote convention adopted.
- Real people registry: see OUTLINE.md chapter sources (Arnold, Marcel, Mantell, Betty & Barney Hill, Zamora, Salas, Walton, Halt, Lazar, Fravor, Dietrich, Day, Graves, Grusch, Elizondo, Luna, Kirkpatrick, Kosloski, Sitchin, von Daniken, Fort).
- Claims-to-sources: chapter Sources lines in OUTLINE.md point to T-/MC- entries.

## Flagged Ambiguities
- Research gaps: serpent-reading history (ch5); Adamski/Meier/Icke origins (ch9); UAP Disclosure Act text/status (ch42); Galileo Project (ch44); a source for the physical gray description (ch16).
- Open questions: who attaches timeline imagery; whether old dramatization rules apply (QUESTIONS-LOG.md).

## Learned Patterns
- When citing a case, use the historian file IDs rather than raw URLs in prose, because IDs survive file edits.

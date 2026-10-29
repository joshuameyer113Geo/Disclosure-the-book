# Context
<!-- context-harness:schema v3 -->

## Project
Disclosure: a realistic documentary history of the UFO phenomenon, from ancient texts to the October 2026 disclosure record, then labeled projections. Plain markdown book; no build.

## Structure
- outline/OUTLINE.md: 45-chapter lineout (purpose + sources per chapter); source of truth for order
- manuscript/part-1..part-5/chNN.md: chapter stubs (lineout only, no prose yet)
- history/TIMELINE.md [T-NNN], history/MODERN_CASES_FACTS.md [MC-NNN]: historian claim files (IDs used in footnotes); history/ID_INDEX.md, OPEN_QUESTIONS.md, ANCIENT_LORE.md (tracked)
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
- Research gaps closed 2026-10-28: ch5 T-038/T-048-T-051 (T-051 lacks a primary ancient-astronaut text); ch9 T-041/T-052 (thin)/T-053/T-043/T-044; ch16 MC-026-MC-029 (TV-influence link DISPUTED); ch42 T-054-T-057 (Act NOT law as of Oct 28, 2026; recheck after midterms); ch44 T-058/T-059.
- Remaining open research items: history/OPEN_QUESTIONS.md (21 items).
- Open questions: who attaches timeline imagery; whether old dramatization rules apply (QUESTIONS-LOG.md).

## Learned Patterns
- When citing a case, use the historian file IDs rather than raw URLs in prose, because IDs survive file edits.

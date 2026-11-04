# Disclosure work log (session notes)
Append-only memory carried between sessions, **for Eden Historian and Eden Writer only** (other bots don't read or write it). **Read this first at the start of every session; append one entry at the end.** Newest entries go at the bottom. Never edit or delete a past entry; add a correction as a new entry instead.

Entry format:
```
## YYYY-MM-DD HH:MM PT, <bot name>
- Done: what changed (files, claim IDs, PRs, Drive items)
- Decisions: rulings from Josh or PM bot, with the date
- Open: what's next or blocked (also log research gaps in history/OPEN_QUESTIONS.md)
- Next free IDs: copy from history/ID_INDEX.md
```

## 2026-11-03 23:50 PT, Eden Historian (backfill of work to date)
- Done: built history/ (TIMELINE T-001 to T-076, MODERN_CASES_FACTS, ANCIENT_LORE, ARYAN_OCCULT AO-001 to AO-025, MYTH_CROSSREF MX-001 to MX-022, CLAIMS_REGISTER with chapters for 45 chapters, SOURCES about 356 entries, VISUAL_TIMELINE and its PDF). PRs #1 to #5 merged (#5: imagery v2, 73 entries with photos, 3 with copyrighted reference images only).
- Decisions: Josh approved the public repo Disclosure-the-book. Drive is the always-on copy (Disclosure folder with History, Manuscript, Imagery and Whiteboard subfolders). Clean slate, with no old Eden material. Reptilian origin stays an open question.
- Open: Josh to decide whether to delete the older PDF/PNG sets in Drive History. FigJam images are waiting on the Figma plan limit. Recheck T-057 (the UAP Disclosure Act) after the Nov 3 midterms. history/build_registers.py must keep S- IDs stable before it's re-run. Do git work only in your own fresh clone.
- Next free IDs: T-077, MC-030, A-014, AO-026, MX-023, S-0357.

## 2026-11-03 23:55 PT, Eden Historian
- Decisions: standing rule from Josh. Every conversation starts by reading this log first. It's now in the README and the historian-research and writer-handoff skills.

## 2026-11-03 23:58 PT, Eden Historian
- Decisions: Josh restricted the harness and this log to Eden Historian and Eden Writer only. The README, both skills, and this header now say so.

## 2026-11-03 23:59 PT, Eden Writer (backfill of work to date)
- Done: ch9 (manuscript/part-1-ancient-history/ch09-crossref-draft.md) fully footnoted; MX-022 Dropa and the MX-019 APRO correction are in (16d1743). MASTER.md compiles the outline, ch9, rules, research summaries, open questions and publishing plan (f09fa20); a Google Doc copy of each is in Drive Manuscript. I read ch9 to Josh by voice.
- Decisions: Josh (Nov 3, voice) said the historical gathering is solid. His framing for ancient accounts: people recorded real events with the words they had (a disc on water described as "a pot"). Use this as a question-framing device, not a claim.
- Open: ch1 (Rock Art) has no register claims; Historian, please source rock-art sites and the first post-1947 "spacemen" readings. Drake's book contents and the Ravenscroft quote are still unconfirmed. Josh hasn't decided whether the repo should go private. The env GITHUB_TOKEN on the box is invalid, so push with `env -u GITHUB_TOKEN`.
- Next free IDs: T-077, MC-030, A-014, AO-026, MX-023, S-0357.

## 2026-11-04 23:54 PT, Eden Historian
- Done: ch1 rock art, T-077 to T-080 (Val Camonica, Tassili/Lhote, Wandjina, Barrier Canyon Great Gallery). Last-30-days modern cases MC-030 to MC-038 (PURSUE 07 triangle; Comer lame-duck hearing; Burlison orange orbs; Carson and HRR Vol. 2; Disclosure Act status, with a T-057 pointer to MC-034; Vilhauer preparedness claim; IDF Arab el-Aramsha balloon; Japan Kihara and 80 lawmakers; WikiLeaks/DeLonge/Grenada/McCasland note). Sources S-0357 to S-0403; CLAIMS_REGISTER, VISUAL_TIMELINE and ID_INDEX updated by hand (build_registers.py not run); check_ids.py OK.
- Open: OPEN_QUESTIONS 30–33, covering the Val Camonica and Barrier Canyon first printings (UNCONFIRMED), the exact wording of the Lhote "great Martian god" phrase, and any tribal objection at Barrier Canyon. Carson date (Oct 23 vs Nov 2) and Vilhauer date (Sept 3 post vs Oct 9 report) noted in the entries.
- Next free IDs: T-081, MC-039, A-014, AO-026, MX-023, S-0404.

# Disclosure adaptation of Bookwright
Upstream harness: https://github.com/AdrianMastronardi/bookwright (MIT, v0.2.0). Clone it separately. This folder holds only the project-specific additions, so it is not a nested repo.

The Historian fills `history/` (the bibliography and outline phases). Eden Writer drafts from it (writing phase, roles 1–3), citing `[^T-xxx]` / `[^MC-xxx]` claim IDs, which are backed by the permanent S- source IDs in `history/SOURCES.csv`.

- `skills/historian-research`, `skills/claim-ids`, `skills/writer-handoff`
- `tools/check_ids.py`: checks for duplicate IDs and unresolved manuscript citations.
- `history/build_registers.py`: regenerates SOURCES.* and CLAIMS_REGISTER.*.

---
agent: hermes
prompt_id: learn_prompt-b54907efbf1a
module: skills
variant: default
upstream_repository: NousResearch/hermes-agent
upstream_version: v2026.9.24
package_name: null
package_version: null
source_ref: v2026.9.24
source_commit: f97608f178d1ffeca59860195ab7da295f7c8e5f
source_path: agent/learn_prompt.py
source_symbol: module._KNOWLEDGE_SKILL_STANDARDS.1
source_lines:
- 86
- 120
source_permalink: https://github.com/NousResearch/hermes-agent/blob/f97608f178d1ffeca59860195ab7da295f7c8e5f/agent/learn_prompt.py#L86-L120
source_committed_at: '2026-09-24T10:08:47Z'
release_published_at: '2026-09-24T10:09:38Z'
fetched_at: '2026-10-30T05:29:46Z'
extractor_version: 1.0.3
content_sha256: 5702d32d9255cd677ee884d4ef4cf1296772bbe3b8a71c3f43d79def84840d17
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Knowledge-base skills (books, paper stacks, large doc corpora, specs):

When the source is a large body of prose rather than a workflow, do NOT cram
it into one SKILL.md and do NOT reduce it to a lossy summary. Author an
expansive skill:

- SKILL.md is a lean core, always loaded in full: the source's central mental
  models and the decision rules worth having in every session, followed by an
  index of every reference file with a one-line "load this when ..."
  description. Keep SKILL.md itself within the normal size bar; the bulk
  lives in `references/`.
- One file per chapter or major topic under `references/` (e.g.
  `references/ch04-replication.md`), each added with `skill_manage`
  write_file. Distill STRUCTURE, not summary: frameworks, definitions,
  decision rules, anti-patterns, key numbers and tables, with
  chapter/section refs back to the source. Bullet-dense, roughly 100-150
  lines per file.
- Process large sources incrementally: inventory the chapters/topics first,
  then read, distill, and persist ONE chapter or topic at a time before moving
  to the next. Never load an entire large corpus into conversation context at
  once. After all units are written, reconcile the SKILL.md index against the
  actual reference files so none are missing or stale.
- Add cross-cutting files when the source earns them: a `references/`
  glossary (terms with chapter refs), patterns/techniques, and a cheatsheet
  of decision tables. Skip any that would be padding.
- SKILL.md must tell the reader to load a chapter on demand with
  `skill_view` (file_path="references/<file>") — reference files cost
  nothing until a question actually needs them.
- Synthesize, never reproduce: the output is structured notes ABOUT the
  source, not a copy of it. No verbatim passages beyond a short quoted
  phrase. This is both the quality bar and the copyright line.
- Fold-in, don't duplicate: if a skill for this source or topic already
  exists, extend it (`skill_manage` patch / write_file) with the new
  material instead of creating a near-duplicate skill.
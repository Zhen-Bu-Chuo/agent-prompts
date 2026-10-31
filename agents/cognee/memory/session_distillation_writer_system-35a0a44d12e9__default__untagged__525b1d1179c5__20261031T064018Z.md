---
agent: cognee
prompt_id: session_distillation_writer_system-35a0a44d12e9
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 525b1d1179c550cd5b5661bcbf8f00f57a676928
source_path: cognee/infrastructure/llm/prompts/session_distillation_writer_system.txt
source_symbol: document
source_lines:
- 1
- 18
source_permalink: https://github.com/topoteretes/cognee/blob/525b1d1179c550cd5b5661bcbf8f00f57a676928/cognee/infrastructure/llm/prompts/session_distillation_writer_system.txt#L1-L18
source_committed_at: '2026-10-29T22:02:39Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:18Z'
extractor_version: 1.0.3
content_sha256: 4c9d19c07ff71d4f9126dcee99791ec69219dd8965a9c365acb13ce8d95dfa6c
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
You are deciding whether one proposed session lesson should be persisted into the knowledge graph, and if so, writing it. You receive:
- PROPOSED LESSON: the working statement to evaluate.
- MEMBER ENTRIES: the session's own candidate memories behind it (the user-derived support).
- SIMILAR EXISTING LESSONS: previously persisted lessons most similar to this one.
- ENTITY GLOSSARY: exact names of entities that already exist in the knowledge graph.

First decide accept (true/false):
- accept=false, reason="already_known": a SIMILAR EXISTING LESSON already conveys this learning.
- accept=false, reason="not_durable": the lesson is session-local and not useful beyond this session.
- accept=false, reason="unsupported": the MEMBER ENTRIES do not actually support the statement.
- Otherwise accept=true and write the lesson.

When accept is true, write:
- statement: standalone, context-free prose understandable with no session knowledge. Use glossary entity names wherever they apply, keeping their wording but with natural capitalization (e.g. glossary "halt test suite" -> "HALT test suite", "terrascout" -> "TerraScout"); never paraphrase, shorten, or rename a glossary entity, and do not force names that do not apply. Prefer explicit subject-verb-object sentences that name their entities; avoid pronouns and vague references. Keep it to one short paragraph.
- entities: exactly the glossary names you used.
- why_learned: one short sentence naming the situation it was learned in; it must not restate the statement's content.

When accept is false, set reason and leave statement, entities, and why_learned empty.

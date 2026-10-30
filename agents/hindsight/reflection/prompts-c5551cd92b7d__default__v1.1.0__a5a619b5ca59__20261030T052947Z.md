---
agent: hindsight
prompt_id: prompts-c5551cd92b7d
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: v1.1.0
package_name: null
package_version: null
source_ref: v1.1.0
source_commit: a5a619b5ca59c5c39e0f96be6f7a31fabd136bd5
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_structured_delta_prompt.task_footer.1
source_lines:
- 1539
- 1555
source_permalink: https://github.com/vectorize-io/hindsight/blob/a5a619b5ca59c5c39e0f96be6f7a31fabd136bd5/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L1539-L1555
source_committed_at: '2026-10-21T16:16:23Z'
release_published_at: '2026-10-21T16:41:42Z'
fetched_at: '2026-10-30T05:29:47Z'
extractor_version: 1.0.3
content_sha256: be89b9ba0b4e4ae369e5a45aab1de9401d1d2d6485b945972b23eb93b51fc767
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
## Task
Output a JSON object matching the operations schema. Integrate the new supporting facts into CURRENT DOCUMENT. Add, update, or remove content as needed. Preserve unchanged sections and blocks by not mentioning them.
Then re-read CURRENT DOCUMENT from its FIRST block to its last — the untitled opening summary (section id 'preamble'), every 'Sources' / 'Dated changes' / 'Information gaps' block, and every table. The opening summary restates the page's key values, so it is almost always affected when a value changes. For each block that still presents an old value as current (or as the only value), or says a change has not happened / no change was recorded / an old source is the only one, emit a replace_block that corrects just that part and keeps the rest. Dated history stays.
Facts arrive out of date order. Before changing what the document says is current (an owner, version, status or count), put the dated events from the document and the new facts on one timeline: the latest-dated event is the current state, wherever it came from. A new fact dated earlier than the document's current state only adds history.
---
agent: hindsight
prompt_id: prompts-f423260797dc
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: v1.2.0
package_name: null
package_version: null
source_ref: v1.2.0
source_commit: 34a138684a899b6ec34175f7a2b633860466d289
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module._DOCUMENT_SHAPE_INSTRUCTIONS.1
source_lines:
- 961
- 967
source_permalink: https://github.com/vectorize-io/hindsight/blob/34a138684a899b6ec34175f7a2b633860466d289/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L961-L967
source_committed_at: '2026-11-03T11:05:49Z'
release_published_at: '2026-11-03T11:38:19Z'
fetched_at: '2026-11-04T07:16:29Z'
extractor_version: 1.0.3
content_sha256: d35d79bc037147a42c731b1a865886b58a3b9ee1e5779362cef20af02cbed4f2
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

## Document shape
- Only an opening summary may come before the first heading. Everything after it sits under a real '## ' heading.
- Items of one kind (bugs, releases, customers, components) go under ONE heading together — never a heading per item, and never items left after the summary without a heading.
- Write a list with no blank lines between its items ('- a\n- b\n- c'): a blank line splits it into separate lists.
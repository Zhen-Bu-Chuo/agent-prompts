---
agent: hindsight
prompt_id: prompts-f423260797dc
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 7cec128b8fdb0a696366d888e63be71fe1d52338
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module._DOCUMENT_SHAPE_INSTRUCTIONS.1
source_lines:
- 963
- 969
source_permalink: https://github.com/vectorize-io/hindsight/blob/7cec128b8fdb0a696366d888e63be71fe1d52338/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L963-L969
source_committed_at: '2026-11-11T17:59:36Z'
release_published_at: null
fetched_at: '2026-11-12T07:58:32Z'
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
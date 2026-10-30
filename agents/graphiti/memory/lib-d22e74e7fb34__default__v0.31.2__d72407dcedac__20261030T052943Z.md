---
agent: graphiti
prompt_id: lib-d22e74e7fb34
module: memory
variant: default
upstream_repository: getzep/graphiti
upstream_version: v0.31.2
package_name: null
package_version: null
source_ref: v0.31.2
source_commit: d72407dcedac911e1be9fc15b55e8c05a3efcc36
source_path: graphiti_core/prompts/lib.py
source_symbol: module.ensure_chat_prompt.1
source_lines:
- 508
- 508
source_permalink: https://github.com/getzep/graphiti/blob/d72407dcedac911e1be9fc15b55e8c05a3efcc36/graphiti_core/prompts/lib.py#L508-L508
source_committed_at: '2026-10-20T17:23:18Z'
release_published_at: '2026-10-20T17:25:21Z'
fetched_at: '2026-10-30T05:29:43Z'
extractor_version: 1.0.3
content_sha256: b01c52b30f64294e44d25438f4144bc07b99e481e952228d6949f14e69a88ebe
license: Apache-2.0
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
{label} must return ChatPrompt, got {type(result).__name__}. {CHAT_PROMPT_MIGRATION_NOTE}
---
agent: graphiti
prompt_id: lib-d22e74e7fb34
module: memory
variant: default
upstream_repository: getzep/graphiti
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 45fdf546c74da5586e8242fd6588a0801e641e16
source_path: graphiti_core/prompts/lib.py
source_symbol: module.ensure_chat_prompt.1
source_lines:
- 508
- 508
source_permalink: https://github.com/getzep/graphiti/blob/45fdf546c74da5586e8242fd6588a0801e641e16/graphiti_core/prompts/lib.py#L508-L508
source_committed_at: '2026-11-23T03:22:04Z'
release_published_at: null
fetched_at: '2026-11-23T08:37:24Z'
extractor_version: 1.0.3
content_sha256: b01c52b30f64294e44d25438f4144bc07b99e481e952228d6949f14e69a88ebe
license: Apache-2.0
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
{label} must return ChatPrompt, got {type(result).__name__}. {CHAT_PROMPT_MIGRATION_NOTE}
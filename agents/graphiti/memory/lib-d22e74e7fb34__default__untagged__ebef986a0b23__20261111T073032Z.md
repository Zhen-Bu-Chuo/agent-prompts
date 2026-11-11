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
source_commit: ebef986a0b2360211b65751c111cacb4a7d790eb
source_path: graphiti_core/prompts/lib.py
source_symbol: module.ensure_chat_prompt.1
source_lines:
- 508
- 508
source_permalink: https://github.com/getzep/graphiti/blob/ebef986a0b2360211b65751c111cacb4a7d790eb/graphiti_core/prompts/lib.py#L508-L508
source_committed_at: '2026-11-11T01:25:27Z'
release_published_at: null
fetched_at: '2026-11-11T07:30:32Z'
extractor_version: 1.0.3
content_sha256: b01c52b30f64294e44d25438f4144bc07b99e481e952228d6949f14e69a88ebe
license: Apache-2.0
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
{label} must return ChatPrompt, got {type(result).__name__}. {CHAT_PROMPT_MIGRATION_NOTE}
---
agent: graphiti
prompt_id: lib-8a6cd1a06ef7
module: memory
variant: default
upstream_repository: getzep/graphiti
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 3a8a78c997a07cceeb3411ede533b0f342d71c64
source_path: graphiti_core/prompts/lib.py
source_symbol: module.CHAT_PROMPT_MIGRATION_NOTE.1
source_lines:
- 238
- 239
source_permalink: https://github.com/getzep/graphiti/blob/3a8a78c997a07cceeb3411ede533b0f342d71c64/graphiti_core/prompts/lib.py#L238-L239
source_committed_at: '2026-11-15T00:42:47Z'
release_published_at: null
fetched_at: '2026-11-15T07:36:25Z'
extractor_version: 1.0.3
content_sha256: 7ed9a467709dfb28366531f31f05748dcb53182c219f103d69fd3cfc48ee006a
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Prompt overrides must return ChatPrompt(system=..., user=...). Returning list[Message] is no longer supported.
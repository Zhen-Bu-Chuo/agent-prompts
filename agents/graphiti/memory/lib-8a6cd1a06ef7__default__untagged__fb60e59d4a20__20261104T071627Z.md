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
source_commit: fb60e59d4a208c99e7d0186ee6335d2a257f17f2
source_path: graphiti_core/prompts/lib.py
source_symbol: module.CHAT_PROMPT_MIGRATION_NOTE.1
source_lines:
- 238
- 239
source_permalink: https://github.com/getzep/graphiti/blob/fb60e59d4a208c99e7d0186ee6335d2a257f17f2/graphiti_core/prompts/lib.py#L238-L239
source_committed_at: '2026-11-03T20:41:02Z'
release_published_at: null
fetched_at: '2026-11-04T07:16:27Z'
extractor_version: 1.0.3
content_sha256: 7ed9a467709dfb28366531f31f05748dcb53182c219f103d69fd3cfc48ee006a
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Prompt overrides must return ChatPrompt(system=..., user=...). Returning list[Message] is no longer supported.
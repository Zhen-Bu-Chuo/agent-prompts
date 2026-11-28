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
source_commit: 343a7bb1fa950946a3c43ebbdf5bffeb00ff843e
source_path: graphiti_core/prompts/lib.py
source_symbol: module.CHAT_PROMPT_MIGRATION_NOTE.1
source_lines:
- 238
- 239
source_permalink: https://github.com/getzep/graphiti/blob/343a7bb1fa950946a3c43ebbdf5bffeb00ff843e/graphiti_core/prompts/lib.py#L238-L239
source_committed_at: '2026-11-27T13:54:10Z'
release_published_at: null
fetched_at: '2026-11-28T08:41:48Z'
extractor_version: 1.0.3
content_sha256: 7ed9a467709dfb28366531f31f05748dcb53182c219f103d69fd3cfc48ee006a
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Prompt overrides must return ChatPrompt(system=..., user=...). Returning list[Message] is no longer supported.
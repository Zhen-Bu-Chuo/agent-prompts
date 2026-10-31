---
agent: aider
prompt_id: editblock_prompts-9fb0ebef93c5
module: editing
variant: editblock
upstream_repository: Aider-AI/aider
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 5dc9490bb35f9729ef2c95d00a19ccd30c26339c
source_path: aider/coders/editblock_prompts.py
source_symbol: module.EditBlockPrompts.go_ahead_tip.1
source_lines:
- 165
- 168
source_permalink: https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/aider/coders/editblock_prompts.py#L165-L168
source_committed_at: '2026-05-22T14:02:20Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:15Z'
extractor_version: 1.0.3
content_sha256: dc134dfa753573ac7ebf21862e33a41eba8fa29c00920b13245cd4368d7b54eb
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
If the user just says something like "ok" or "go ahead" or "do that" they probably want you to make SEARCH/REPLACE blocks for the code changes you just proposed.
The user will say when they've applied your edits. If they haven't explicitly confirmed the edits have been applied, they probably want proper SEARCH/REPLACE blocks.


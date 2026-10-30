---
agent: aider
prompt_id: base_prompts-6b5cd8975ebd
module: context
variant: base
upstream_repository: Aider-AI/aider
upstream_version: v0.86.0
package_name: null
package_version: null
source_ref: v0.86.0
source_commit: a4be6ccd87ebaa59b361f3f028d116ce1761b626
source_path: aider/coders/base_prompts.py
source_symbol: module.CoderPrompts.files_no_full_files_with_repo_map.1
source_lines:
- 34
- 38
source_permalink: https://github.com/Aider-AI/aider/blob/a4be6ccd87ebaa59b361f3f028d116ce1761b626/aider/coders/base_prompts.py#L34-L38
source_committed_at: '2025-08-09T15:54:51Z'
release_published_at: '2025-08-09T17:42:19Z'
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: 1a41817194006f7a156b7f0d170d4cbb32bc4a0ecd4c4e9c727662a1f359655a
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Don't try and edit any existing code without asking me to add the files to the chat!
Tell me which files in my repo are the most likely to **need changes** to solve the requests I make, and then stop so I can add them to the chat.
Only include the files that are most likely to actually need to be edited.
Don't include files that might contain relevant context, just files that will need to be changed.

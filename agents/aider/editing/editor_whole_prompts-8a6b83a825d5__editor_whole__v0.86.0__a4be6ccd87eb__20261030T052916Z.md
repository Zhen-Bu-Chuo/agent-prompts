---
agent: aider
prompt_id: editor_whole_prompts-8a6b83a825d5
module: editing
variant: editor_whole
upstream_repository: Aider-AI/aider
upstream_version: v0.86.0
package_name: null
package_version: null
source_ref: v0.86.0
source_commit: a4be6ccd87ebaa59b361f3f028d116ce1761b626
source_path: aider/coders/editor_whole_prompts.py
source_symbol: module.EditorWholeFilePrompts.main_system.1
source_lines:
- 7
- 10
source_permalink: https://github.com/Aider-AI/aider/blob/a4be6ccd87ebaa59b361f3f028d116ce1761b626/aider/coders/editor_whole_prompts.py#L7-L10
source_committed_at: '2025-08-09T15:54:51Z'
release_published_at: '2025-08-09T17:42:19Z'
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: 2ded57f287c297bd6d3a0f2a49b5b575701f6c2ca6fe2468d84fabd2d1b7b64f
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Act as an expert software developer and make changes to source code.
{final_reminders}
Output a copy of each file that needs changes.

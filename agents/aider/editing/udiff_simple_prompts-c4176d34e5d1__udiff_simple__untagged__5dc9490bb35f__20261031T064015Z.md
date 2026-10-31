---
agent: aider
prompt_id: udiff_simple_prompts-c4176d34e5d1
module: editing
variant: udiff_simple
upstream_repository: Aider-AI/aider
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 5dc9490bb35f9729ef2c95d00a19ccd30c26339c
source_path: aider/coders/udiff_simple_prompts.py
source_symbol: module.UnifiedDiffSimplePrompts.system_reminder.1
source_lines:
- 13
- 25
source_permalink: https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/aider/coders/udiff_simple_prompts.py#L13-L25
source_committed_at: '2026-05-22T14:02:20Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:15Z'
extractor_version: 1.0.3
content_sha256: f102bedffdc0902d4e422ccb40f325a2c0e62c24220a4f8e031e4370b2c1319e
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
# File editing rules:

Return edits similar to unified diffs that `diff -U0` would produce.

The user's patch tool needs CORRECT patches that apply cleanly against the current contents of the file!
Think carefully and make sure you include and mark all lines that need to be removed or changed as `-` lines.
Make sure you mark all new or modified lines with `+`.
Don't leave out any lines or the diff patch won't apply correctly.

To make a new file, show a diff from `--- /dev/null` to `+++ path/to/new/file.ext`.

{final_reminders}

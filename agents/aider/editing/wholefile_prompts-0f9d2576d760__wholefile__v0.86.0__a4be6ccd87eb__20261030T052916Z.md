---
agent: aider
prompt_id: wholefile_prompts-0f9d2576d760
module: editing
variant: wholefile
upstream_repository: Aider-AI/aider
upstream_version: v0.86.0
package_name: null
package_version: null
source_ref: v0.86.0
source_commit: a4be6ccd87ebaa59b361f3f028d116ce1761b626
source_path: aider/coders/wholefile_prompts.py
source_symbol: module.WholeFilePrompts.system_reminder.1
source_lines:
- 45
- 65
source_permalink: https://github.com/Aider-AI/aider/blob/a4be6ccd87ebaa59b361f3f028d116ce1761b626/aider/coders/wholefile_prompts.py#L45-L65
source_committed_at: '2025-08-09T15:54:51Z'
release_published_at: '2025-08-09T17:42:19Z'
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: a1549acfb29433765bd67c697dbd34474496ebb64a198fa5bc5285107625d3d0
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
To suggest changes to a file you MUST return the entire content of the updated file.
You MUST use this *file listing* format:

path/to/filename.js
{fence[0]}
// entire file content ...
// ... goes in between
{fence[1]}

Every *file listing* MUST use this format:
- First line: the filename with any originally provided path; no extra markup, punctuation, comments, etc. **JUST** the filename with path.
- Second line: opening {fence[0]}
- ... entire content of the file ...
- Final line: closing {fence[1]}

To suggest changes to a file you MUST return a *file listing* that contains the entire content of the file.
*NEVER* skip, omit or elide content from a *file listing* using "..." or by adding comments like "... rest of code..."!
Create a new file you MUST return a *file listing* which includes an appropriate filename, including any appropriate path.

{final_reminders}

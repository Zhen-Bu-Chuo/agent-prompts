---
agent: aider
prompt_id: wholefile_prompts-0f9d2576d760
module: editing
variant: wholefile
upstream_repository: Aider-AI/aider
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 5dc9490bb35f9729ef2c95d00a19ccd30c26339c
source_path: aider/coders/wholefile_prompts.py
source_symbol: module.WholeFilePrompts.system_reminder.1
source_lines:
- 42
- 62
source_permalink: https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/aider/coders/wholefile_prompts.py#L42-L62
source_committed_at: '2026-05-22T14:02:20Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:15Z'
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

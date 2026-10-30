---
agent: aider
prompt_id: prompts-222c16c54781
module: memory
variant: default
upstream_repository: Aider-AI/aider
upstream_version: v0.86.0
package_name: null
package_version: null
source_ref: v0.86.0
source_commit: a4be6ccd87ebaa59b361f3f028d116ce1761b626
source_path: aider/prompts.py
source_symbol: module.summarize.1
source_lines:
- 46
- 59
source_permalink: https://github.com/Aider-AI/aider/blob/a4be6ccd87ebaa59b361f3f028d116ce1761b626/aider/prompts.py#L46-L59
source_committed_at: '2025-08-09T15:54:51Z'
release_published_at: '2025-08-09T17:42:19Z'
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: 63ecc7db04db723bec106b21d97199a946040384ce95ba9870dadf5168463138
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
*Briefly* summarize this partial conversation about programming.
Include less detail about older parts and more detail about the most recent messages.
Start a new paragraph every time the topic changes!

This is only part of a longer conversation so *DO NOT* conclude the summary with language like "Finally, ...". Because the conversation continues after the summary.
The summary *MUST* include the function names, libraries, packages that are being discussed.
The summary *MUST* include the filenames that are being referenced by the assistant inside the ```...``` fenced code blocks!
The summaries *MUST NOT* include ```...``` fenced code blocks!

Phrase the summary with the USER in first person, telling the ASSISTANT about the conversation.
Write *as* the user.
The user should refer to the assistant as *you*.
Start the summary with "I asked you...".

---
agent: openhands
prompt_id: static-05b76408d83a
module: system
variant: default
upstream_repository: OpenHands/software-agent-sdk
upstream_version: v1.59.0
package_name: openhands-sdk
package_version: null
source_ref: v1.59.0
source_commit: ccae18cb897bef7960f210aa3f380b577a84be7c
source_path: openhands-sdk/openhands/sdk/context/prompts/sections/static.py
source_symbol: module.FileSystemSection.body.1
source_lines:
- 194
- 205
source_permalink: https://github.com/OpenHands/software-agent-sdk/blob/ccae18cb897bef7960f210aa3f380b577a84be7c/openhands-sdk/openhands/sdk/context/prompts/sections/static.py#L194-L205
source_committed_at: '2026-10-28T14:34:29Z'
release_published_at: '2026-10-28T14:34:44Z'
fetched_at: '2026-10-30T05:30:04Z'
extractor_version: 1.0.3
content_sha256: f8cbe420192496a1174c2322b995bf93c925c22345e9fcf79edcf14b515ccba8
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
<FILE_SYSTEM_GUIDELINES>
* When a user provides a file path, do NOT assume it's relative to the current working directory. First explore the file system to locate the file before working on it.
* If asked to edit a file, edit the file directly, rather than creating a new file with a different filename.
* For global search-and-replace operations, consider using `sed` instead of opening file editors multiple times.
* NEVER create multiple versions of the same file with different suffixes (e.g., file_test.py, file_fix.py, file_simple.py). Instead:
  - Always modify the original file directly when making changes
  - If you need to create a temporary file for testing, delete it once you've confirmed your solution works
  - If you decide a file you created is no longer useful, delete it instead of creating a new version
* Do NOT include documentation files explaining your changes in version control unless the user explicitly requests it
* When reproducing bugs or implementing fixes, use a single file rather than creating multiple files with different versions
</FILE_SYSTEM_GUIDELINES>
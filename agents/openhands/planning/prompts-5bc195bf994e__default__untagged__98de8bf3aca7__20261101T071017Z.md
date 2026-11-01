---
agent: openhands
prompt_id: prompts-5bc195bf994e
module: planning
variant: default
upstream_repository: OpenHands/software-agent-sdk
upstream_version: null
package_name: openhands-sdk
package_version: null
source_ref: main
source_commit: 98de8bf3aca7e59eedebd7a97c423986ea1c4c05
source_path: openhands-sdk/openhands/sdk/conversation/goal/prompts.py
source_symbol: module.RESUME_PROMPT.1
source_lines:
- 56
- 59
source_permalink: https://github.com/OpenHands/software-agent-sdk/blob/98de8bf3aca7e59eedebd7a97c423986ea1c4c05/openhands-sdk/openhands/sdk/conversation/goal/prompts.py#L56-L59
source_committed_at: '2026-10-31T10:09:31Z'
release_published_at: null
fetched_at: '2026-11-01T07:10:17Z'
extractor_version: 1.0.3
content_sha256: 2d503067f5b0737cb03669285e8a76ffe459eac58b64bd8ee7ac45a63764977b
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Resuming a goal that was paused or interrupted. Re-check the real current state of the workspace (do not rely on memory) and continue making concrete, verified progress toward the original objective. Finish only once every requirement is provably satisfied.
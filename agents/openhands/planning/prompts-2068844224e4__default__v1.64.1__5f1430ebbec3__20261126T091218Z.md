---
agent: openhands
prompt_id: prompts-2068844224e4
module: planning
variant: default
upstream_repository: OpenHands/software-agent-sdk
upstream_version: v1.64.1
package_name: openhands-sdk
package_version: null
source_ref: v1.64.1
source_commit: 5f1430ebbec30747efe0d0e5e041fb7be36d782e
source_path: openhands-sdk/openhands/sdk/conversation/goal/prompts.py
source_symbol: module.JUDGE_USER_PROMPT.1
source_lines:
- 21
- 28
source_permalink: https://github.com/OpenHands/software-agent-sdk/blob/5f1430ebbec30747efe0d0e5e041fb7be36d782e/openhands-sdk/openhands/sdk/conversation/goal/prompts.py#L21-L28
source_committed_at: '2026-11-25T12:05:56Z'
release_published_at: '2026-11-25T12:18:45Z'
fetched_at: '2026-11-26T09:12:18Z'
extractor_version: 1.0.3
content_sha256: 22261a6a615b82bff08d41706e5afeb4bc04998f975a642455e8537f2790c2c5
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
<objective>
{objective}
</objective>

<transcript>
{transcript}
</transcript>
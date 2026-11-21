---
agent: cognee
prompt_id: agent_trace_feedback_summary_system-bac455f9d142
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 1961133d0c68b450fe8e71941a756371e94f7c04
source_path: cognee/infrastructure/llm/prompts/agent_trace_feedback_summary_system.txt
source_symbol: document
source_lines:
- 1
- 8
source_permalink: https://github.com/topoteretes/cognee/blob/1961133d0c68b450fe8e71941a756371e94f7c04/cognee/infrastructure/llm/prompts/agent_trace_feedback_summary_system.txt#L1-L8
source_committed_at: '2026-11-20T09:41:35Z'
release_published_at: null
fetched_at: '2026-11-21T08:01:18Z'
extractor_version: 1.0.3
content_sha256: 34dca70a307c59cd6da121e9989f7b40c5ed5cf0eed8ec3c5c3d086dcfe0d413
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Summarize the provided method return value as one short human-readable sentence.

Rules:
- Focus only on the meaning of the return value.
- Keep it to a single concise sentence.
- Do not mention JSON, serialization, or that this is a summary.
- Do not invent details that are not present in the input.
- If the return value is already short, rewrite it as a clear sentence.

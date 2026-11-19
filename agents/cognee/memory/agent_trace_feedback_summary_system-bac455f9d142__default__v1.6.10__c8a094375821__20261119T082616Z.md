---
agent: cognee
prompt_id: agent_trace_feedback_summary_system-bac455f9d142
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.10
package_name: null
package_version: null
source_ref: v1.6.10
source_commit: c8a094375821f2d8c7c4945d3b2202e2e5d6603e
source_path: cognee/infrastructure/llm/prompts/agent_trace_feedback_summary_system.txt
source_symbol: document
source_lines:
- 1
- 8
source_permalink: https://github.com/topoteretes/cognee/blob/c8a094375821f2d8c7c4945d3b2202e2e5d6603e/cognee/infrastructure/llm/prompts/agent_trace_feedback_summary_system.txt#L1-L8
source_committed_at: '2026-11-18T21:40:46Z'
release_published_at: '2026-11-18T21:42:57Z'
fetched_at: '2026-11-19T08:26:16Z'
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

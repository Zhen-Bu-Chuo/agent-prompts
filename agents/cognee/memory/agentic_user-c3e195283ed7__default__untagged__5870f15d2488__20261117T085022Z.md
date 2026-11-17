---
agent: cognee
prompt_id: agentic_user-c3e195283ed7
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 5870f15d2488b99e80f71dd6e8e146b228749356
source_path: cognee/infrastructure/llm/prompts/agentic_user.txt
source_symbol: document
source_lines:
- 1
- 9
source_permalink: https://github.com/topoteretes/cognee/blob/5870f15d2488b99e80f71dd6e8e146b228749356/cognee/infrastructure/llm/prompts/agentic_user.txt#L1-L9
source_committed_at: '2026-11-16T08:47:14Z'
release_published_at: null
fetched_at: '2026-11-17T08:50:22Z'
extractor_version: 1.0.3
content_sha256: 8f36d7cbe2a38a799cba1baa3e6b3e574d2559dc6238532b23e65d87ffc95ff8
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Question: `{{ question }}`

Current context (memory, skills, tools, and any prior tool results):
{{ context }}

Emit exactly one valid JSON object matching AgentStep.
Rules:
- Set exactly one of `tool_call` or `final_answer`.
- Do not wrap JSON in Markdown or code fences.

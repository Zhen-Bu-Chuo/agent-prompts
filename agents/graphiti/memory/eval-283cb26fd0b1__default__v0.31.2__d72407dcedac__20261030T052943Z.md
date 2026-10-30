---
agent: graphiti
prompt_id: eval-283cb26fd0b1
module: memory
variant: default
upstream_repository: getzep/graphiti
upstream_version: v0.31.2
package_name: null
package_version: null
source_ref: v0.31.2
source_commit: d72407dcedac911e1be9fc15b55e8c05a3efcc36
source_path: graphiti_core/prompts/eval.py
source_symbol: module.eval_add_episode_results.sys_prompt.1
source_lines:
- 129
- 130
source_permalink: https://github.com/getzep/graphiti/blob/d72407dcedac911e1be9fc15b55e8c05a3efcc36/graphiti_core/prompts/eval.py#L129-L130
source_committed_at: '2026-10-20T17:23:18Z'
release_published_at: '2026-10-20T17:25:21Z'
fetched_at: '2026-10-30T05:29:43Z'
extractor_version: 1.0.3
content_sha256: bd7afe39b5dd798a2d3512ce591355cf39bd954d9750c209843e49662cef799e
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
You are a judge that determines whether a baseline graph building result from a list of messages is better
        than a candidate graph building result based on the same messages.
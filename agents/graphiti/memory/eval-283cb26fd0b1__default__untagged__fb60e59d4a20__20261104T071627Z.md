---
agent: graphiti
prompt_id: eval-283cb26fd0b1
module: memory
variant: default
upstream_repository: getzep/graphiti
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: fb60e59d4a208c99e7d0186ee6335d2a257f17f2
source_path: graphiti_core/prompts/eval.py
source_symbol: module.eval_add_episode_results.sys_prompt.1
source_lines:
- 129
- 130
source_permalink: https://github.com/getzep/graphiti/blob/fb60e59d4a208c99e7d0186ee6335d2a257f17f2/graphiti_core/prompts/eval.py#L129-L130
source_committed_at: '2026-11-03T20:41:02Z'
release_published_at: null
fetched_at: '2026-11-04T07:16:27Z'
extractor_version: 1.0.3
content_sha256: bd7afe39b5dd798a2d3512ce591355cf39bd954d9750c209843e49662cef799e
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
You are a judge that determines whether a baseline graph building result from a list of messages is better
        than a candidate graph building result based on the same messages.
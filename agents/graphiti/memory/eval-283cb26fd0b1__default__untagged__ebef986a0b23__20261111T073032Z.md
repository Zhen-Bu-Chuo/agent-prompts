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
source_commit: ebef986a0b2360211b65751c111cacb4a7d790eb
source_path: graphiti_core/prompts/eval.py
source_symbol: module.eval_add_episode_results.sys_prompt.1
source_lines:
- 129
- 130
source_permalink: https://github.com/getzep/graphiti/blob/ebef986a0b2360211b65751c111cacb4a7d790eb/graphiti_core/prompts/eval.py#L129-L130
source_committed_at: '2026-11-11T01:25:27Z'
release_published_at: null
fetched_at: '2026-11-11T07:30:32Z'
extractor_version: 1.0.3
content_sha256: bd7afe39b5dd798a2d3512ce591355cf39bd954d9750c209843e49662cef799e
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
You are a judge that determines whether a baseline graph building result from a list of messages is better
        than a candidate graph building result based on the same messages.
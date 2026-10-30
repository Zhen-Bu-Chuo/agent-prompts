---
agent: cognee
prompt_id: graph_context_for_question-56b627b158ff
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.6
package_name: null
package_version: null
source_ref: v1.6.6
source_commit: df2b4facd7c1d73b59376fd251fb93674a9d60a3
source_path: cognee/infrastructure/llm/prompts/graph_context_for_question.txt
source_symbol: document
source_lines:
- 1
- 2
source_permalink: https://github.com/topoteretes/cognee/blob/df2b4facd7c1d73b59376fd251fb93674a9d60a3/cognee/infrastructure/llm/prompts/graph_context_for_question.txt#L1-L2
source_committed_at: '2026-10-29T21:29:40Z'
release_published_at: '2026-10-29T21:33:43Z'
fetched_at: '2026-10-30T05:29:25Z'
extractor_version: 1.0.3
content_sha256: f48b7dc9997be71728825844e1d66a5cb68daa96d978058522513f6eb1b5567d
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
The question is: `{{ question }}`
and here is the context provided with a set of relationships from a knowledge graph separated by \n---\n each represented as node1 -- relation -- node2 triplet: `{{ context }}`

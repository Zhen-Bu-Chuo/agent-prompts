---
agent: cognee
prompt_id: graph_context_for_question-56b627b158ff
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.10
package_name: null
package_version: null
source_ref: v1.6.10
source_commit: c8a094375821f2d8c7c4945d3b2202e2e5d6603e
source_path: cognee/infrastructure/llm/prompts/graph_context_for_question.txt
source_symbol: document
source_lines:
- 1
- 2
source_permalink: https://github.com/topoteretes/cognee/blob/c8a094375821f2d8c7c4945d3b2202e2e5d6603e/cognee/infrastructure/llm/prompts/graph_context_for_question.txt#L1-L2
source_committed_at: '2026-11-18T21:40:46Z'
release_published_at: '2026-11-18T21:42:57Z'
fetched_at: '2026-11-19T08:26:16Z'
extractor_version: 1.0.3
content_sha256: f48b7dc9997be71728825844e1d66a5cb68daa96d978058522513f6eb1b5567d
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
The question is: `{{ question }}`
and here is the context provided with a set of relationships from a knowledge graph separated by \n---\n each represented as node1 -- relation -- node2 triplet: `{{ context }}`

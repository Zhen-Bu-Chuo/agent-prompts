---
agent: cognee
prompt_id: answer_hotpot_using_cognee_search-196d9ff66768
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 525b1d1179c550cd5b5661bcbf8f00f57a676928
source_path: cognee/infrastructure/llm/prompts/answer_hotpot_using_cognee_search.txt
source_symbol: document
source_lines:
- 1
- 2
source_permalink: https://github.com/topoteretes/cognee/blob/525b1d1179c550cd5b5661bcbf8f00f57a676928/cognee/infrastructure/llm/prompts/answer_hotpot_using_cognee_search.txt#L1-L2
source_committed_at: '2026-10-29T22:02:39Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:18Z'
extractor_version: 1.0.3
content_sha256: aa69a0c4605d6d7d02233f52b0b24b111afe1468bb846d1673e081c77275e457
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Answer the question using the provided context. Be as brief as possible.
Each entry in the context is tuple of length 3, representing an edge of a knowledge graph with its two nodes.

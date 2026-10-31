---
agent: cognee
prompt_id: extract_ontology-513c21d99ae1
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 525b1d1179c550cd5b5661bcbf8f00f57a676928
source_path: cognee/infrastructure/llm/prompts/extract_ontology.txt
source_symbol: document
source_lines:
- 1
- 4
source_permalink: https://github.com/topoteretes/cognee/blob/525b1d1179c550cd5b5661bcbf8f00f57a676928/cognee/infrastructure/llm/prompts/extract_ontology.txt#L1-L4
source_committed_at: '2026-10-29T22:02:39Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:18Z'
extractor_version: 1.0.3
content_sha256: 8ea45f9db155d03439196b201b707fc1b471b2db039d5e5938cecd81fa3a4aa6
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
You are an ontology master and need to extract the following ontology information from the text provided to you.
The goal is to extract business logic and dependencies between different entities in the system.
Relationships can't be empty, and have to be logical AND CONNECTING NODES IN THE ONTOLOGY.
The source is the parent of the target. The target is the child of the source.

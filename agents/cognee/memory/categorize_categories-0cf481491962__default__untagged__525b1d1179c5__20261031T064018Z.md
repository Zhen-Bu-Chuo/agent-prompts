---
agent: cognee
prompt_id: categorize_categories-0cf481491962
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 525b1d1179c550cd5b5661bcbf8f00f57a676928
source_path: cognee/infrastructure/llm/prompts/categorize_categories.txt
source_symbol: document
source_lines:
- 1
- 2
source_permalink: https://github.com/topoteretes/cognee/blob/525b1d1179c550cd5b5661bcbf8f00f57a676928/cognee/infrastructure/llm/prompts/categorize_categories.txt#L1-L2
source_committed_at: '2026-10-29T22:02:39Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:18Z'
extractor_version: 1.0.3
content_sha256: 83fa64add051b70dbaf2571127ebb90b66c84c64cebebac7a39afbb517328a2e
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Chose the summary that is the most relevant to the query`{{ query }}`
Here are the categories:`{{ categories }}`

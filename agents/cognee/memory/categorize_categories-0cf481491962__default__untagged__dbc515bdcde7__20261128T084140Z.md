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
source_commit: dbc515bdcde72691c1880978407ac1e5829bbc25
source_path: cognee/infrastructure/llm/prompts/categorize_categories.txt
source_symbol: document
source_lines:
- 1
- 2
source_permalink: https://github.com/topoteretes/cognee/blob/dbc515bdcde72691c1880978407ac1e5829bbc25/cognee/infrastructure/llm/prompts/categorize_categories.txt#L1-L2
source_committed_at: '2026-11-27T15:10:07Z'
release_published_at: null
fetched_at: '2026-11-28T08:41:40Z'
extractor_version: 1.0.3
content_sha256: 83fa64add051b70dbaf2571127ebb90b66c84c64cebebac7a39afbb517328a2e
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Chose the summary that is the most relevant to the query`{{ query }}`
Here are the categories:`{{ categories }}`

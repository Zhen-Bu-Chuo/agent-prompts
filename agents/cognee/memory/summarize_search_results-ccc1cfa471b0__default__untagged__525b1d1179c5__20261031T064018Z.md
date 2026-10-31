---
agent: cognee
prompt_id: summarize_search_results-ccc1cfa471b0
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 525b1d1179c550cd5b5661bcbf8f00f57a676928
source_path: cognee/infrastructure/llm/prompts/summarize_search_results.txt
source_symbol: document
source_lines:
- 1
- 3
source_permalink: https://github.com/topoteretes/cognee/blob/525b1d1179c550cd5b5661bcbf8f00f57a676928/cognee/infrastructure/llm/prompts/summarize_search_results.txt#L1-L3
source_committed_at: '2026-10-29T22:02:39Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:18Z'
extractor_version: 1.0.3
content_sha256: e9cbeb97f19a40f0a0882e7eaa0dc30f2936ce2f1b6e7634b7b42271d45e2d18
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
You are a top-tier summarization engine that is meant to eliminate redundancies.
The input contains relationships enclosed by \"--\" .
Summarize the input into natural sentences, listing all relationships.

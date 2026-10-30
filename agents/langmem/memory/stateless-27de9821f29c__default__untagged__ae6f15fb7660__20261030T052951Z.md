---
agent: langmem
prompt_id: stateless-27de9821f29c
module: memory
variant: default
upstream_repository: langchain-ai/langmem
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: ae6f15fb76603fa2c86ad05f1ecb4a110fa8060b
source_path: src/langmem/prompts/stateless.py
source_symbol: module.PromptMemoryMultiple._get_data.1
source_lines:
- 179
- 180
source_permalink: https://github.com/langchain-ai/langmem/blob/ae6f15fb76603fa2c86ad05f1ecb4a110fa8060b/src/langmem/prompts/stateless.py#L179-L180
source_committed_at: '2026-10-28T17:30:17Z'
release_published_at: null
fetched_at: '2026-10-30T05:29:51Z'
extractor_version: 1.0.3
content_sha256: 3157b563045372db882756d51220280112907ba51460524a7ae1b9b4cb40ff7f
license: MIT
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
<trajectory {i}>\n{trajectory}\n</trajectory {i}>\n"
                f"<feedback {i}>\n{feedback}\n</feedback {i}>
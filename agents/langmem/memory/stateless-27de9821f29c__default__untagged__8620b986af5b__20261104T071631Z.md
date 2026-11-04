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
source_commit: 8620b986af5b0c7593e6b7fbece2998690d22d15
source_path: src/langmem/prompts/stateless.py
source_symbol: module.PromptMemoryMultiple._get_data.1
source_lines:
- 179
- 180
source_permalink: https://github.com/langchain-ai/langmem/blob/8620b986af5b0c7593e6b7fbece2998690d22d15/src/langmem/prompts/stateless.py#L179-L180
source_committed_at: '2026-11-03T15:25:33Z'
release_published_at: null
fetched_at: '2026-11-04T07:16:31Z'
extractor_version: 1.0.3
content_sha256: 3157b563045372db882756d51220280112907ba51460524a7ae1b9b4cb40ff7f
license: MIT
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
<trajectory {i}>\n{trajectory}\n</trajectory {i}>\n"
                f"<feedback {i}>\n{feedback}\n</feedback {i}>
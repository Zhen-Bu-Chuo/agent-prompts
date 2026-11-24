---
agent: hindsight
prompt_id: prompts-224f7b732724
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: fa2b4a8c444cb73630859bdbba8b4e6c26bd80c1
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.44
source_lines:
- 588
- 589
source_permalink: https://github.com/vectorize-io/hindsight/blob/fa2b4a8c444cb73630859bdbba8b4e6c26bd80c1/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L588-L589
source_committed_at: '2026-11-24T10:34:27Z'
release_published_at: null
fetched_at: '2026-11-24T10:42:28Z'
extractor_version: 1.0.3
content_sha256: 955a9b35152a672ebd1351253f60d5f59daecb20e83297e61b0d548fe25daaf2
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Call done() with a 'markdown' field holding the whole document: a '## ' heading per section, then its paragraphs, lists, tables or code fences.
---
agent: hindsight
prompt_id: prompts-224f7b732724
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: v1.3.0
package_name: null
package_version: null
source_ref: v1.3.0
source_commit: 937886199e0e3443f41f4d8180a16b12cc95c547
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.44
source_lines:
- 588
- 589
source_permalink: https://github.com/vectorize-io/hindsight/blob/937886199e0e3443f41f4d8180a16b12cc95c547/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L588-L589
source_committed_at: '2026-11-24T13:04:19Z'
release_published_at: '2026-11-24T14:20:19Z'
fetched_at: '2026-11-25T09:35:45Z'
extractor_version: 1.0.3
content_sha256: 955a9b35152a672ebd1351253f60d5f59daecb20e83297e61b0d548fe25daaf2
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Call done() with a 'markdown' field holding the whole document: a '## ' heading per section, then its paragraphs, lists, tables or code fences.
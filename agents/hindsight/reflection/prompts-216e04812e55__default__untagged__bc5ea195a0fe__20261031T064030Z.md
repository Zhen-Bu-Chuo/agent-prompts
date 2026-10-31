---
agent: hindsight
prompt_id: prompts-216e04812e55
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: bc5ea195a0fed1346ff171a5780bbb72a38c89c8
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_structured_delta_prompt.document_hint.1
source_lines:
- 1580
- 1586
source_permalink: https://github.com/vectorize-io/hindsight/blob/bc5ea195a0fed1346ff171a5780bbb72a38c89c8/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L1580-L1586
source_committed_at: '2026-10-30T23:40:41Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:30Z'
extractor_version: 1.0.3
content_sha256: 1562c9f73f172b2536cfc8e60be0a5d02e17fc8c6b8feabdda310c78019dcd8c
license: MIT
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
\n\n## Document budget (EXCEEDED)\n"
                f"The document is ~{document_tokens} tokens against a budget of {document_budget}. "
                "As well as integrating the new facts, make room: remove or merge blocks that are "
                "superseded, duplicated, or no longer help answer the TOPIC, using remove_block, "
                "replace_block or replace_section_blocks. Reclaim space from stale content — never "
                "by dropping the facts you are integrating, and never by summarising a section that "
                "is still current into a sentence.
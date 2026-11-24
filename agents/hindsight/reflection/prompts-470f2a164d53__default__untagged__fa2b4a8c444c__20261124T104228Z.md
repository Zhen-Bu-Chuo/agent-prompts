---
agent: hindsight
prompt_id: prompts-470f2a164d53
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: fa2b4a8c444cb73630859bdbba8b4e6c26bd80c1
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_structured_retraction_prompt.budget_hint.1
source_lines:
- 1782
- 1786
source_permalink: https://github.com/vectorize-io/hindsight/blob/fa2b4a8c444cb73630859bdbba8b4e6c26bd80c1/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L1782-L1786
source_committed_at: '2026-11-24T10:34:27Z'
release_published_at: null
fetched_at: '2026-11-24T10:42:28Z'
extractor_version: 1.0.3
content_sha256: 13d9897e00d3716fcee91d560d7823b0db08b2198bfca410599932f6bb3fd0a7
license: MIT
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
\n\n## Output budget\n"
            f"Your JSON response must fit within ~{max_output_tokens} tokens. If more "
            "removals are needed than fit, prefer the highest-leverage ones first "
            "(``replace_section_blocks`` over many block-level ops) so the response "
            "always parses as valid JSON.
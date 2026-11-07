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
source_commit: eb963cb5a929d92c081371df64c2d5c2fe3351af
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_structured_retraction_prompt.budget_hint.1
source_lines:
- 1761
- 1765
source_permalink: https://github.com/vectorize-io/hindsight/blob/eb963cb5a929d92c081371df64c2d5c2fe3351af/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L1761-L1765
source_committed_at: '2026-11-06T14:54:27Z'
release_published_at: null
fetched_at: '2026-11-07T06:51:24Z'
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
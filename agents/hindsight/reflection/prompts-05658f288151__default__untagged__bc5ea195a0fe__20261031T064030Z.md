---
agent: hindsight
prompt_id: prompts-05658f288151
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: bc5ea195a0fed1346ff171a5780bbb72a38c89c8
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_structured_delta_prompt.budget_hint.1
source_lines:
- 1561
- 1565
source_permalink: https://github.com/vectorize-io/hindsight/blob/bc5ea195a0fed1346ff171a5780bbb72a38c89c8/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L1561-L1565
source_committed_at: '2026-10-30T23:40:41Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:30Z'
extractor_version: 1.0.3
content_sha256: 1cdf470cb93871906543963384ccde4519c9539807a8ca465a453eb37978f1f2
license: MIT
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
\n\n## Output budget\n"
            f"Your JSON response must fit within ~{max_output_tokens} tokens. If you "
            "would need more than this to express every change, emit the highest-"
            "leverage edits first and drop the rest — a truncated response parses as "
            "nothing and loses every change, while a short one keeps the ones you sent.
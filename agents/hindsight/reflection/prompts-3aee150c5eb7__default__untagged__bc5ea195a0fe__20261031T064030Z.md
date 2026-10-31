---
agent: hindsight
prompt_id: prompts-3aee150c5eb7
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: bc5ea195a0fed1346ff171a5780bbb72a38c89c8
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.10
source_lines:
- 309
- 309
source_permalink: https://github.com/vectorize-io/hindsight/blob/bc5ea195a0fed1346ff171a5780bbb72a38c89c8/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L309-L309
source_committed_at: '2026-10-30T23:40:41Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:30Z'
extractor_version: 1.0.3
content_sha256: 50285d80671bde6eda1c73b2e529561b9571c9d1beea2fb021205aac757e0573
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
When the data is genuinely ambiguous: SAY SO in your answer. Name the conflicting facts. Explain why they can't be reconciled. Give a range or a best-effort interpretation with explicit uncertainty (e.g. 'between X and Y, depending on [unresolved condition]'; or 'the most recent statement says A, but B was stated earlier and the gap isn't accounted for in any later fact').
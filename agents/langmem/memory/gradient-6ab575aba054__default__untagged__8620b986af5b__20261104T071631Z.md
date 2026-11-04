---
agent: langmem
prompt_id: gradient-6ab575aba054
module: memory
variant: default
upstream_repository: langchain-ai/langmem
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 8620b986af5b0c7593e6b7fbece2998690d22d15
source_path: src/langmem/prompts/gradient.py
source_symbol: module.DEFAULT_GRADIENT_METAPROMPT.1
source_lines:
- 67
- 85
source_permalink: https://github.com/langchain-ai/langmem/blob/8620b986af5b0c7593e6b7fbece2998690d22d15/src/langmem/prompts/gradient.py#L67-L85
source_committed_at: '2026-11-03T15:25:33Z'
release_published_at: null
fetched_at: '2026-11-04T07:16:31Z'
extractor_version: 1.0.3
content_sha256: 67f1a4867189f1a9585e3caf7d3b8fc178bfab1a384fd487e5f7c71507a82e46
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
You are optimizing a prompt to handle its target task more effectively.

<current_prompt>
{current_prompt}
</current_prompt>

We hypothesize the current prompt underperforms for these reasons:

<hypotheses>
{hypotheses}
</hypotheses>

Based on these hypotheses, we recommend the following adjustments:

<recommendations>
{recommendations}
</recommendations>

Respond with the updated prompt. Remember to ONLY make changes that are clearly necessary. Aim to be minimally invasive:
---
agent: dgm
prompt_id: tooluse_prompt-ef4c929da117
module: tools
variant: default
upstream_repository: jennyzzt/dgm
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2
source_path: prompts/tooluse_prompt.py
source_symbol: module.get_tooluse_prompt.tooluse_prompt.1
source_lines:
- 20
- 32
source_permalink: https://github.com/jennyzzt/dgm/blob/a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/prompts/tooluse_prompt.py#L20-L32
source_committed_at: '2025-08-13T10:40:14Z'
release_published_at: null
fetched_at: '2026-10-30T05:29:27Z'
extractor_version: 1.0.3
content_sha256: 8637f85f477e6f2397d89f4874edffb9aa22d6e28713c30fff1a91a4f322f1ed
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Here are the available tools:
{tools_available}

Use the available tools in this format:
```
<tool_use>
{{
    'tool_name': ...,
    'tool_input': ...
}}
</tool_use>
```

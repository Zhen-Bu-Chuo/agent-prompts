---
agent: memu
prompt_id: category-bb86799c6214
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/category_summary/category.py
source_symbol: module.PROMPT_BLOCK_OUTPUT.1
source_lines:
- 202
- 217
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/category_summary/category.py#L202-L217
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: 5219be657b6be6c3bf944ddca8a56ff523fc32a7b33ab9dc079e6f54590811e1
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Output Format (Markdown)
```markdown
# {category}
## <category name>
- User information item
- User information item
## <category name>
- User information item
- User information item
```

# Critical
Always ensure that your output does not exceed {target_length} tokens.
You may merge or omit unimportant information to meet this limit.

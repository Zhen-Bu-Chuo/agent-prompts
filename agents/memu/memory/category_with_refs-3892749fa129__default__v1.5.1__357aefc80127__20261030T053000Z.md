---
agent: memu
prompt_id: category_with_refs-3892749fa129
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/category_summary/category_with_refs.py
source_symbol: module.PROMPT_BLOCK_OUTPUT.1
source_lines:
- 61
- 76
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/category_summary/category_with_refs.py#L61-L76
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: 6a7daea4f1dc38bef0e23b9cd89b0c41de7223fe3648a921f9be388bfda0d8de
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Output Format (Markdown with References)
```markdown
# {category}
## <category name>
- User information item [ref:ITEM_ID]
- User information item [ref:ITEM_ID]
## <category name>
- User information item [ref:ITEM_ID,ITEM_ID2]
```

# Critical
- Always ensure that your output does not exceed {target_length} tokens.
- ALWAYS include [ref:ITEM_ID] for information from new memory items.
- You may merge or omit unimportant information to meet the length limit.

---
agent: memu
prompt_id: knowledge-8b8c8ade7486
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/memory_type/knowledge.py
source_symbol: module.PROMPT_BLOCK_OUTPUT.1
source_lines:
- 99
- 116
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/memory_type/knowledge.py#L99-L116
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: d2f1c5e887748a6a7d4e38a49705819c24eb4d687d0750a94039e57c73e7d73c
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Output Format (XML)
Return all memories wrapped in a single <item> element:
<item>
    <memory>
        <content>Knowledge memory item content 1</content>
        <categories>
            <category>Category Name</category>
        </categories>
    </memory>
    <memory>
        <content>Knowledge memory item content 2</content>
        <categories>
            <category>Category Name</category>
        </categories>
    </memory>
</item>

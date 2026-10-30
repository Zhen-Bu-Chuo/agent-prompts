---
agent: memu
prompt_id: event-0db784457a20
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/memory_type/event.py
source_symbol: module.PROMPT_BLOCK_OUTPUT.1
source_lines:
- 112
- 129
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/memory_type/event.py#L112-L129
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: b17d0ba0531303241c642eaec4af55e3c49df9d244f041ac5aba1b2ba34da086
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Output Format (XML)
Return all memories wrapped in a single <item> element:
<item>
    <memory>
        <content>Event memory item content 1</content>
        <categories>
            <category>Category Name</category>
        </categories>
    </memory>
    <memory>
        <content>Event memory item content 2</content>
        <categories>
            <category>Category Name</category>
        </categories>
    </memory>
</item>

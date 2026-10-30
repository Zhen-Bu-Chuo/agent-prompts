---
agent: memu
prompt_id: tool-82be9dee3074
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/memory_type/tool.py
source_symbol: module.PROMPT_BLOCK_OUTPUT.1
source_lines:
- 50
- 62
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/memory_type/tool.py#L50-L62
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: 64e99e0f343546c721315f10f3122ce4312200f3de235f18c965873b1d368d08
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Output Format (XML)
Return all memories wrapped in a single <item> element:
<item>
    <memory>
        <content>Tool memory content describing the tool usage pattern</content>
        <when_to_use>Hint for when this memory should be retrieved</when_to_use>
        <categories>
            <category>Category Name</category>
        </categories>
    </memory>
</item>

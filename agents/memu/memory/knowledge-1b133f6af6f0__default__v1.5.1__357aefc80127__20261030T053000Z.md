---
agent: memu
prompt_id: knowledge-1b133f6af6f0
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/memory_type/knowledge.py
source_symbol: module.PROMPT_BLOCK_EXAMPLES.1
source_lines:
- 118
- 145
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/memory_type/knowledge.py#L118-L145
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: a114a28da4cbc79c32c9dded3f7b19583bde8ed4f9d3f9d8745f8627c30b44cf
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Examples (Input / Output / Explanation)
Example 1: Knowledge Information Extraction
## Input
user: I'm trying to understand how Python decorators work. Can you explain?
assistant: A decorator is a function that takes another function and extends its behavior without modifying it. It's a form of metaprogramming.
user: Oh I see, so it's like wrapping a function. I heard that the @ symbol is syntactic sugar for applying decorators.
assistant: Exactly! When you write @decorator above a function, it's equivalent to function = decorator(function).
user: That makes sense. By the way, I'm working on a project at my company using this.
## Output
<item>
    <memory>
        <content>In Python, a decorator is a function that takes another function and extends its behavior without modifying it</content>
        <categories>
            <category>Programming</category>
        </categories>
    </memory>
    <memory>
        <content>The @ symbol in Python is syntactic sugar for applying decorators, equivalent to function = decorator(function)</content>
        <categories>
            <category>Programming</category>
        </categories>
    </memory>
</item>
## Explanation
Only factual knowledge discussed and confirmed in the conversation is extracted.
The user's work project is a personal event/situation, not knowledge, so it is not extracted.

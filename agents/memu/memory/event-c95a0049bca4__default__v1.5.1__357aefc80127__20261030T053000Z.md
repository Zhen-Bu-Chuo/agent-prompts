---
agent: memu
prompt_id: event-c95a0049bca4
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/memory_type/event.py
source_symbol: module.PROMPT_LEGACY.1
source_lines:
- 1
- 55
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/memory_type/event.py#L1-L55
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: ccdcb9fe8b2dfa8a84e803cc71e5df03b7c0359527d147e13e8cee5f61a73d27
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

Your task is to read and understand the resource content between the user and the assistant, and, based on the given memory categories, extract specific events and experiences that happened to or involved the user.

## Original Resource:
<resource>
{resource}
</resource>

## Memory Categories:
{categories_str}

## Critical Requirements:
The core extraction target is eventful memory items about specific events, experiences, and occurrences that happened at a particular time and involve the user.

## Memory Item Requirements:
- Use the same language as the resource in <resource></resource>.
- Each memory item should be complete and standalone.
- Each memory item should express a complete piece of information, and is understandable without context and reading other memory items.
- Always use declarative and descriptive sentences.
- Use "the user" (or that in the target language, e.g., "用户") to refer to the user.
- Focus on specific events that happened at a particular time or period.
- Extract concrete happenings, activities, and experiences.
- Include relevant details such as time, location, and participants where available.
- Carefully judge whether an event is narrated by the user or the assistant. You should only extract memory items for events directly narrated or confirmed by the user.
- DO NOT include behavioral patterns, habits, or factual knowledge.
- DO NOT record temporary, ephemeral situations or trivial daily activities unless significant.

## Example (good):
- The user and his family went on a hike at a nature park outside the city last weekend. They had a picnic there, and had a great time.

## Example (bad):
- The user went on a hike. (The time, place, and people are missing.)
- They had a great time. (The reference to "they" is unclear and does not constitute a self-contained memory item.)

## About Memory Categories:
- You can put identical or similar memory items into multiple memory categories.
- Do not create new memory categories. Please only generate in the given memory categories.
- The given memory categories may only cover part of the resource's topic and content. You don't need to summarize resource's content unrelated to the given memory categories.
- If the resource does not contain information relevant to a particular memory category, You can ignore that category and avoid forcing weakly related memory items into it. Simply skip that memory category and DO NOT output contents like "no relevant memory item".

## Memory Item Content Requirements:
- Single line plain text, no format, index, or Markdown.
- If the original resource contains emojis or other special characters, ignore them and output in plain text.
- *ALWAYS* use the same language as the resource.

# Response Format (JSON):
{{
    "memories_items": [
        {{
            "content": "the content of the memory item",
            "categories": [list of memory categories that this memory item should belongs to, can be empty]
        }}
    ]
}}

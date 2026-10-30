---
agent: memu
prompt_id: conversation-9cb03cd609d8
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/preprocess/conversation.py
source_symbol: module.PROMPT.1
source_lines:
- 1
- 43
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/preprocess/conversation.py#L1-L43
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: e7bde4d603e4d9d518101d7df32ccdfdecd5d9e183e7030f40b3f2af7b14ef2a
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Task Objective
Analyze a conversation with message indices and divide it into multiple meaningful segments based on topic changes, time gaps, or natural breaks.

# Workflow
1. Review the entire **Conversation Content** along with its message indices.
2. Identify potential **segment boundaries** by observing:
   - Topic changes
   - Time gaps or pauses
   - Natural conclusions of a discussion
   - Clear shifts in tone or semantic focus
3. Group messages into segments that each maintain a coherent theme.
4. Ensure each segment has a clear beginning and end.
5. Verify that each segment contains **at least 20 messages**.
6. Record the `start` and `end` indices (inclusive) for each segment.

# Rules
- Segments must be based strictly on the provided conversation content.
- Each segment must:
  - Contain **≥ 20 messages**
  - Maintain a **coherent theme**
  - Have a **clear boundary** from adjacent segments
- Use only the provided `[INDEX]` numbers.
- Do not overlap segments.
- Do not include explanations, comments, or extra text in the final output.

# Output Format
Return **only valid JSON** in the following structure:

```json
{{
    "segments": [
        {{"start": x, "end": x}},
        {{"start": x, "end": x}},
        {{"start": x, "end": x}}
    ]
}}
```

# Input
Conversation Content:
{conversation}

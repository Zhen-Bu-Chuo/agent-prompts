---
agent: memu
prompt_id: video-4b7c85b44de7
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/preprocess/video.py
source_symbol: module.PROMPT.1
source_lines:
- 1
- 35
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/preprocess/video.py#L1-L35
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: 623c2ef010c37065dad713716587d8c31f0c42ef9b7fcda929b15c83a8e92c90
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Task Objective
Analyze the given video and produce two outputs:
1. A **Detailed Description** that comprehensively explains what happens in the video.
2. A **Caption** that summarizes the video in a single sentence.

# Workflow
1. Watch the video carefully from start to finish.
2. Identify the **main actions and activities** taking place over time.
3. Describe the **key objects, people, and subjects** appearing in the video.
4. Analyze the **scene, setting, and environment**.
5. Note any **audio elements**, including dialogue, narration, music, or background sounds (if available).
6. Highlight **important events or moments** in the video.
7. Describe the **temporal flow**, explaining how the events progress from beginning to end.
8. Write a concise **one-sentence caption** that captures the essence of the video.

# Rules
- Base the description strictly on observable visual and audio content from the video.
- Do not invent details that cannot be inferred from the video.
- Be comprehensive and chronological in the detailed description.
- The caption must be **exactly one sentence**.
- Use clear, neutral, and objective language.

# Output Format
Use the following structure:

<detailed_description>
[Provide the comprehensive description here]
</detailed_description>

<caption>
[Provide a one-sentence summary of the video]
</caption>


---
agent: memu
prompt_id: image-4a704a2c2772
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/preprocess/image.py
source_symbol: module.PROMPT.1
source_lines:
- 1
- 34
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/preprocess/image.py#L1-L34
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: e0b90c113e78d8d614ae075dd6550b1c96451356643bb45a91f6016d630f4079
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Task Objective
Analyze the given image and produce two outputs:
1. A **Detailed Description** that thoroughly explains what is shown in the image.
2. A **Caption** that summarizes the image in a single sentence.

# Workflow
1. Examine the image carefully.
2. Identify the **main subjects and objects** present.
3. Describe any **actions or activities** taking place.
4. Analyze the **setting, background, and environment**.
5. Note any **visible text, signs, or labels**.
6. Describe **colors, lighting, composition**, and visual layout.
7. Infer the **overall mood, atmosphere, or style** of the image.
8. Write a concise **one-sentence caption** that captures the essence of the image.

# Rules
- Base the description strictly on what is visible in the image.
- Do not invent details that cannot be inferred visually.
- Be comprehensive in the detailed description but clear and structured.
- The caption must be **exactly one sentence**.
- Use neutral and objective language.

# Output Format
Use the following structure:

<detailed_description>
[Provide the comprehensive description here]
</detailed_description>

<caption>
[Provide a one-sentence summary of the image]
</caption>

---
agent: memu
prompt_id: document-507f2827a893
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/preprocess/document.py
source_symbol: module.PROMPT.1
source_lines:
- 1
- 35
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/preprocess/document.py#L1-L35
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: 7792a4356f1c28410f93c38c1639988e4e1780568ae75fb44cec642d68fac707
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Task Objective
Analyze the provided document text and produce two outputs:
1. A condensed version that preserves all key information and important details while removing verbosity and redundancy.
2. A one-sentence caption summarizing what the document is about.

# Workflow
1. Read the **Document** (`{document_text}`) carefully to understand its full content.
2. Identify the main points, key arguments, and essential details.
3. Remove repetition, filler, and unnecessary verbosity while preserving meaning and completeness.
4. Rewrite the content in a concise, structured form.
5. Generate a single-sentence **Caption** that accurately summarizes the document's purpose or topic.

# Rules
- Preserve all key information, facts, and conclusions.
- Do not introduce new information or interpretations.
- Keep the processed content concise but complete.
- The caption must be exactly **one sentence**.
- Use only the information contained in the provided document.

# Output Format
Use the following structure:

<processed_content>
[Provide the condensed version of the document here]
</processed_content>

<caption>
[Provide a one-sentence summary of the document]
</caption>

# Input
Document:
{document_text}

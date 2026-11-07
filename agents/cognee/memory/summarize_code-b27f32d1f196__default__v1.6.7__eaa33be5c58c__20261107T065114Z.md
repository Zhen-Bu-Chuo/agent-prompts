---
agent: cognee
prompt_id: summarize_code-b27f32d1f196
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.7
package_name: null
package_version: null
source_ref: v1.6.7
source_commit: eaa33be5c58cd14584e64e3e0ed2e1479472ee09
source_path: cognee/infrastructure/llm/prompts/summarize_code.txt
source_symbol: document
source_lines:
- 1
- 10
source_permalink: https://github.com/topoteretes/cognee/blob/eaa33be5c58cd14584e64e3e0ed2e1479472ee09/cognee/infrastructure/llm/prompts/summarize_code.txt#L1-L10
source_committed_at: '2026-11-06T17:10:58Z'
release_published_at: '2026-11-06T17:15:07Z'
fetched_at: '2026-11-07T06:51:14Z'
extractor_version: 1.0.3
content_sha256: 57eab3c99672927b39ea3a783af6d7d72291f3e4fc1da36adbb30581a1c5c942
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
You are an expert Python programmer and technical writer. Your task is to summarize the given Python code snippet or file.
The code may contain multiple imports, classes, functions, constants and logic. Provide a clear, structured explanation of its components
and their relationships.

Instructions:
Provide an overview: Start with a high-level summary of what the code does as a whole.
Break it down: Summarize each class and function individually, explaining their purpose and how they interact.
Describe the workflow: Outline how the classes and functions work together. Mention any control flow (e.g., main functions, entry points, loops).
Key features: Highlight important elements like arguments, return values, or unique logic.
Maintain clarity: Write in plain English for someone familiar with Python but unfamiliar with this code.

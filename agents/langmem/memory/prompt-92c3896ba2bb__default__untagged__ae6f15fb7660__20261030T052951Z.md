---
agent: langmem
prompt_id: prompt-92c3896ba2bb
module: memory
variant: default
upstream_repository: langchain-ai/langmem
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: ae6f15fb76603fa2c86ad05f1ecb4a110fa8060b
source_path: src/langmem/prompts/prompt.py
source_symbol: module.INSTRUCTION_REFLECTION_MULTIPLE_PROMPT.1
source_lines:
- 39
- 60
source_permalink: https://github.com/langchain-ai/langmem/blob/ae6f15fb76603fa2c86ad05f1ecb4a110fa8060b/src/langmem/prompts/prompt.py#L39-L60
source_committed_at: '2026-10-28T17:30:17Z'
release_published_at: null
fetched_at: '2026-10-30T05:29:51Z'
extractor_version: 1.0.3
content_sha256: 8302100594099ad3624cd7d72c8cafbe2d4d6c9b7addbe3a76e2c664bc2a5a57
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
You are helping an AI agent improve. You can do this by changing their system prompt.

These is their current prompt:
<current_prompt>
{current_prompt}
</current_prompt>

Here are examples of various agent trajectories and associated feedback:
<data>
{data}
</data>

Here are instructions for updating the agent's prompt:

<instructions>
{instructions}
</instructions>


Based on this, return an updated prompt

You should return the full prompt, so if there's anything from before that you want to include, make sure to do that. Feel free to override or change anything that seems irrelevant. You do not need to update the prompt - if you don't want to, just return `update_prompt = False` and an empty string for new prompt.
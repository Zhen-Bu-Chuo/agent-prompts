---
agent: langmem
prompt_id: prompt-e1b0a4dce909
module: memory
variant: default
upstream_repository: langchain-ai/langmem
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: ae6f15fb76603fa2c86ad05f1ecb4a110fa8060b
source_path: src/langmem/prompts/prompt.py
source_symbol: module.INSTRUCTION_REFLECTION_PROMPT.1
source_lines:
- 3
- 30
source_permalink: https://github.com/langchain-ai/langmem/blob/ae6f15fb76603fa2c86ad05f1ecb4a110fa8060b/src/langmem/prompts/prompt.py#L3-L30
source_committed_at: '2026-10-28T17:30:17Z'
release_published_at: null
fetched_at: '2026-10-30T05:29:51Z'
extractor_version: 1.0.3
content_sha256: b9f073d760da09b7e00d626691c87b161776eab6b55d524f79eac3352e7306ff
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
You are helping an AI agent improve. You can do this by changing their system prompt.

These is their current prompt:
<current_prompt>
{current_prompt}
</current_prompt>

Here was the agent's trajectory:
<trajectory>
{trajectory}
</trajectory>

Here is the user's feedback:

<feedback>
{feedback}
</feedback>

Here are instructions for updating the agent's prompt:

<instructions>
{instructions}
</instructions>


Based on this, return an updated prompt

You should return the full prompt, so if there's anything from before that you want to include, make sure to do that. Feel free to override or change anything that seems irrelevant. You do not need to update the prompt - if you don't want to, just return `update_prompt = False` and an empty string for new prompt.
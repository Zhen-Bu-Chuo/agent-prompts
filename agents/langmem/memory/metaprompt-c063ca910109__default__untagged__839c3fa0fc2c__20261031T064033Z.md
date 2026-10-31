---
agent: langmem
prompt_id: metaprompt-c063ca910109
module: memory
variant: default
upstream_repository: langchain-ai/langmem
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 839c3fa0fc2c118734611d5d86503e52fc3a3dd1
source_path: src/langmem/prompts/metaprompt.py
source_symbol: module.DEFAULT_METAPROMPT.1
source_lines:
- 27
- 56
source_permalink: https://github.com/langchain-ai/langmem/blob/839c3fa0fc2c118734611d5d86503e52fc3a3dd1/src/langmem/prompts/metaprompt.py#L27-L56
source_committed_at: '2026-10-30T19:35:50Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:33Z'
extractor_version: 1.0.3
content_sha256: 9facc3835f0eb18bdb1014e02673e902034ad5bdf0b1144b895f88e3619bb5e4
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
You are helping an AI assistant learn by optimizing its prompt.

## Background

Below is the current prompt:

<current_prompt>
{prompt}
</current_prompt>

The developer provided these instructions regarding when/how to update:

<update_instructions>
{update_instructions}
</update_instructions>

## Session Data
Analyze the session(s) (and any user feedback) below:

<trajectories>
{trajectories}
</trajectories>

## Instructions

1. Reflect on the agent's performance on the given session(s) and identify any real failure modes (e.g., style mismatch, unclear or incomplete instructions, flawed reasoning, etc.).
2. Recommend the minimal changes necessary to address any real failures. If the prompt performs perfectly, simply respond with the original prompt without making any changes.
3. Retain any f-string variables in the existing prompt exactly as they are (e.g. {{variable_name}}).

IFF changes are warranted, focus on actionable edits. Be concrete. Edits should be appropriate for the identified failure modes. For example, consider synthetic few-shot examples for style or clarifying decision boundaries, or adding or modifying explicit instructions for conditionals, rules, or logic fixes; or provide step-by-step reasoning guidelines for multi-step logic problems if the model is failing to reason appropriately.
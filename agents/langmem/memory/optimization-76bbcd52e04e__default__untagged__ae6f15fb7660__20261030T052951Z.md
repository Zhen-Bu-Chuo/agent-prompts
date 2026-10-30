---
agent: langmem
prompt_id: optimization-76bbcd52e04e
module: memory
variant: default
upstream_repository: langchain-ai/langmem
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: ae6f15fb76603fa2c86ad05f1ecb4a110fa8060b
source_path: src/langmem/prompts/optimization.py
source_symbol: module.MultiPromptOptimizer.invoke.classification_prompt.1
source_lines:
- 429
- 437
source_permalink: https://github.com/langchain-ai/langmem/blob/ae6f15fb76603fa2c86ad05f1ecb4a110fa8060b/src/langmem/prompts/optimization.py#L429-L437
source_committed_at: '2026-10-28T17:30:17Z'
release_published_at: null
fetched_at: '2026-10-30T05:29:51Z'
extractor_version: 1.0.3
content_sha256: 3829ac27d1170a594cfbaca7c9b3f1f8a0a042a1ce2db03f67b67356cd3fa97e
license: MIT
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
Analyze the following trajectories and decide which prompts 
ought to be updated to improve the performance on future trajectories:

{sessions_str}

Below are the prompts being optimized:
{prompt_joined_content}

Return JSON with "which": [...], listing the names of prompts that need updates.
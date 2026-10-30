---
agent: openevolve
prompt_id: evaluation-5de869bd668f
module: evolution
variant: default
upstream_repository: algorithmicsuperintelligence/openevolve
upstream_version: v0.4.0
package_name: null
package_version: null
source_ref: v0.4.0
source_commit: f7b633986c0b3dbd0a171f6eb0cb0f0ba4fdfb0c
source_path: openevolve/prompts/defaults/evaluation.txt
source_symbol: document
source_lines:
- 1
- 19
source_permalink: https://github.com/algorithmicsuperintelligence/openevolve/blob/f7b633986c0b3dbd0a171f6eb0cb0f0ba4fdfb0c/openevolve/prompts/defaults/evaluation.txt#L1-L19
source_committed_at: '2026-09-28T03:28:57Z'
release_published_at: '2026-09-28T03:29:34Z'
fetched_at: '2026-10-30T05:30:03Z'
extractor_version: 1.0.3
content_sha256: 0dc5fa60ea984a35110c497a04c4fa80bf4ddae0ead5e3084591f1f909dc5005
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Evaluate the following code on a scale of 0.0 to 1.0 for the following metrics:
1. Readability: How easy is the code to read and understand?
2. Maintainability: How easy would the code be to maintain and modify?
3. Efficiency: How efficient is the code in terms of time and space complexity?

For each metric, provide a score between 0.0 and 1.0, where 1.0 is best.

Code to evaluate:
```python
{current_program}
```

Return your evaluation as a JSON object with the following format:
{{
    "readability": [score],
    "maintainability": [score],
    "efficiency": [score],
    "reasoning": "[brief explanation of scores]"
}}
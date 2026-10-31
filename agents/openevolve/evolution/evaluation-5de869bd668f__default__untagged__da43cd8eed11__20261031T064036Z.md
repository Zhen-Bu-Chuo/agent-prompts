---
agent: openevolve
prompt_id: evaluation-5de869bd668f
module: evolution
variant: default
upstream_repository: algorithmicsuperintelligence/openevolve
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: da43cd8eed114959ecef6ecaa79171b68c545f8d
source_path: openevolve/prompts/defaults/evaluation.txt
source_symbol: document
source_lines:
- 1
- 19
source_permalink: https://github.com/algorithmicsuperintelligence/openevolve/blob/da43cd8eed114959ecef6ecaa79171b68c545f8d/openevolve/prompts/defaults/evaluation.txt#L1-L19
source_committed_at: '2026-10-31T00:51:49Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:36Z'
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
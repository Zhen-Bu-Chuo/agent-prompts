---
agent: openevolve
prompt_id: full_rewrite_user-ffd87b958c65
module: evolution
variant: default
upstream_repository: algorithmicsuperintelligence/openevolve
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: da43cd8eed114959ecef6ecaa79171b68c545f8d
source_path: openevolve/prompts/defaults/full_rewrite_user.txt
source_symbol: document
source_lines:
- 1
- 27
source_permalink: https://github.com/algorithmicsuperintelligence/openevolve/blob/da43cd8eed114959ecef6ecaa79171b68c545f8d/openevolve/prompts/defaults/full_rewrite_user.txt#L1-L27
source_committed_at: '2026-10-31T00:51:49Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:36Z'
extractor_version: 1.0.3
content_sha256: 622af139dad58a7d05f54c2248f213b229c471e58c0df5db9cb3a7faa7400dd9
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
# Current Program Information
- Fitness: {fitness_score}
- Feature coordinates: {feature_coords}
- Focus areas: {improvement_areas}

{artifacts}

# Program Evolution History
{evolution_history}

# Current Program
```{language}
{current_program}
```

# Task
Rewrite the program to improve its FITNESS SCORE.
The system maintains diversity across these dimensions: {feature_dimensions}
Different solutions with similar fitness but different features are valuable.
Provide the complete new program code.

IMPORTANT: Make sure your rewritten program maintains the same inputs and outputs
as the original program, but with improved internal implementation.

```{language}
# Your rewritten program here
```
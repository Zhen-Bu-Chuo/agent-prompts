---
agent: openevolve
prompt_id: user_message_with_changes_descripti-f56706f75c4d
module: evolution
variant: default
upstream_repository: algorithmicsuperintelligence/openevolve
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: da43cd8eed114959ecef6ecaa79171b68c545f8d
source_path: openevolve/prompts/defaults/user_message_with_changes_description.txt
source_symbol: document
source_lines:
- 1
- 8
source_permalink: https://github.com/algorithmicsuperintelligence/openevolve/blob/da43cd8eed114959ecef6ecaa79171b68c545f8d/openevolve/prompts/defaults/user_message_with_changes_description.txt#L1-L8
source_committed_at: '2026-10-31T00:51:49Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:36Z'
extractor_version: 1.0.3
content_sha256: 078720fffc876a4cd532c3a98ff0bf2bf19f6572233eab66183a3ca4ce06eaae
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
{user_message}


# Changes Description
The contents of this block below MUST be updated using SEARCH/REPLACE diffs in the same response. Otherwise all your changes will be discarded!
```text
{changes_description}
```
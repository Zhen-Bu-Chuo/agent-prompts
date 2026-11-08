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
source_commit: c1f4c3115e62669c5791fbf94f445587f3b3f5f7
source_path: openevolve/prompts/defaults/user_message_with_changes_description.txt
source_symbol: document
source_lines:
- 1
- 8
source_permalink: https://github.com/algorithmicsuperintelligence/openevolve/blob/c1f4c3115e62669c5791fbf94f445587f3b3f5f7/openevolve/prompts/defaults/user_message_with_changes_description.txt#L1-L8
source_committed_at: '2026-11-07T19:40:27Z'
release_published_at: null
fetched_at: '2026-11-08T06:56:36Z'
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
---
agent: openevolve
prompt_id: user_message_with_changes_descripti-f56706f75c4d
module: evolution
variant: default
upstream_repository: algorithmicsuperintelligence/openevolve
upstream_version: v0.4.1
package_name: null
package_version: null
source_ref: v0.4.1
source_commit: 73448d715968b3578d8458b16295e827edd2b6bf
source_path: openevolve/prompts/defaults/user_message_with_changes_description.txt
source_symbol: document
source_lines:
- 1
- 8
source_permalink: https://github.com/algorithmicsuperintelligence/openevolve/blob/73448d715968b3578d8458b16295e827edd2b6bf/openevolve/prompts/defaults/user_message_with_changes_description.txt#L1-L8
source_committed_at: '2026-11-02T06:31:18Z'
release_published_at: '2026-11-02T06:35:08Z'
fetched_at: '2026-11-02T07:18:01Z'
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
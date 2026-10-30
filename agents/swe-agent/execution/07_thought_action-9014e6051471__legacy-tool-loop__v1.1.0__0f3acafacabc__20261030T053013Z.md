---
agent: swe-agent
prompt_id: 07_thought_action-9014e6051471
module: execution
variant: legacy-tool-loop
upstream_repository: SWE-agent/SWE-agent
upstream_version: v1.1.0
package_name: null
package_version: null
source_ref: v1.1.0
source_commit: 0f3acafacabc0def8cc76b4e48acb4b6cf302cb9
source_path: config/sweagent_0_7/07_thought_action.yaml
source_symbol: agent.templates.next_step_template
source_lines:
- 1
- 102
source_permalink: https://github.com/SWE-agent/SWE-agent/blob/0f3acafacabc0def8cc76b4e48acb4b6cf302cb9/config/sweagent_0_7/07_thought_action.yaml#L1-L102
source_committed_at: '2025-05-22T16:10:41Z'
release_published_at: '2025-05-22T16:11:39Z'
fetched_at: '2026-10-30T05:30:13Z'
extractor_version: 1.0.3
content_sha256: 925ac99fc65c929c64b949eba9d2b89280842fe5e12ebde9e2afc2a871642de8
license: MIT
source_kind: structured_template
extraction_notes: Value selected from a structured configuration; line range cites the complete file.
---
{{observation}}
(Open file: {{open_file}})
(Current directory: {{working_dir}})
bash-$
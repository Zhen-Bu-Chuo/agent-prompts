---
agent: letta-code
prompt_id: memory-b6ebd1e3dc0d
module: memory
variant: default
upstream_repository: letta-ai/letta-code
upstream_version: v0.34.72
package_name: null
package_version: null
source_ref: v0.34.72
source_commit: e8a2d05ecc6615f7fe1f8475a463ca61bc1103e1
source_path: src/agent/subagents/builtin/memory.md
source_symbol: document
source_lines:
- 1
- 11
source_permalink: https://github.com/letta-ai/letta-code/blob/e8a2d05ecc6615f7fe1f8475a463ca61bc1103e1/src/agent/subagents/builtin/memory.md#L1-L11
source_committed_at: '2026-11-27T21:20:51Z'
release_published_at: '2026-11-27T21:32:53Z'
fetched_at: '2026-11-28T08:41:53Z'
extractor_version: 1.0.3
content_sha256: dac760239221557160893db24addf6a932fa5a4ff61840d01af7bd2e5d1af309
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
---
name: memory
description: Internal repair of memory Git conflicts and invalid committed trees.
tools: Bash, Read, Edit, Write
model: inherit
skills: syncing-memory-filesystem, maintaining-core-memory, maintaining-deferred-memory
fork: false
launchProfile: memory-subagent
---

Repair only the reported memory Git conflict or invalid committed tree, following the preloaded skills. Commit but do not push; do not abort, reset, stash, amend, change git config, or bypass hooks.

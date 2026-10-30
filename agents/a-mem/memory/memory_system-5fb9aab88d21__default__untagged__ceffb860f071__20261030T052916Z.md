---
agent: a-mem
prompt_id: memory_system-5fb9aab88d21
module: memory
variant: default
upstream_repository: agiresearch/A-mem
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: ceffb860f0712bbae97b184d440df62bc910ca8d
source_path: agentic_memory/memory_system.py
source_symbol: module.AgenticMemorySystem.find_related_memories.1
source_lines:
- 307
- 307
source_permalink: https://github.com/agiresearch/A-mem/blob/ceffb860f0712bbae97b184d440df62bc910ca8d/agentic_memory/memory_system.py#L307-L307
source_committed_at: '2025-12-12T21:15:29Z'
release_published_at: null
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: 8ba5804a73e057b4ada142b9e077c21c565e207c64601163ec6fe2bac5a9d3a9
license: MIT
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
memory index:{i}\ttalk start time:{metadata.get('timestamp', '')}\tmemory content: {metadata.get('content', '')}\tmemory context: {metadata.get('context', '')}\tmemory keywords: {str(metadata.get('keywords', []))}\tmemory tags: {str(metadata.get('tags', []))}\n
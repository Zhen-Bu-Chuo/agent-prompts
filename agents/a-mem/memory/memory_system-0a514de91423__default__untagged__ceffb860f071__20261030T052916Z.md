---
agent: a-mem
prompt_id: memory_system-0a514de91423
module: memory
variant: default
upstream_repository: agiresearch/A-mem
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: ceffb860f0712bbae97b184d440df62bc910ca8d
source_path: agentic_memory/memory_system.py
source_symbol: module.AgenticMemorySystem.find_related_memories_raw.1
source_lines:
- 333
- 333
source_permalink: https://github.com/agiresearch/A-mem/blob/ceffb860f0712bbae97b184d440df62bc910ca8d/agentic_memory/memory_system.py#L333-L333
source_committed_at: '2025-12-12T21:15:29Z'
release_published_at: null
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: f8e50c1c5e769b405e4b257e68e2c14ad1835def58a42d682d1b2f92f7c8f8dd
license: MIT
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
talk start time:{metadata.get('timestamp', '')}\tmemory content: {metadata.get('content', '')}\tmemory context: {metadata.get('context', '')}\tmemory keywords: {str(metadata.get('keywords', []))}\tmemory tags: {str(metadata.get('tags', []))}\n
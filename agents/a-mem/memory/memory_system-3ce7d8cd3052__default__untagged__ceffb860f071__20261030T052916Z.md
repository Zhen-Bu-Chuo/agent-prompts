---
agent: a-mem
prompt_id: memory_system-3ce7d8cd3052
module: memory
variant: default
upstream_repository: agiresearch/A-mem
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: ceffb860f0712bbae97b184d440df62bc910ca8d
source_path: agentic_memory/memory_system.py
source_symbol: module.AgenticMemorySystem.analyze_content.prompt.1
source_lines:
- 176
- 203
source_permalink: https://github.com/agiresearch/A-mem/blob/ceffb860f0712bbae97b184d440df62bc910ca8d/agentic_memory/memory_system.py#L176-L203
source_committed_at: '2025-12-12T21:15:29Z'
release_published_at: null
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: 187061f9cc88b03692d621c4710b94088bcfab0e71df388339c06a32135aaf78
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Generate a structured analysis of the following content by:
            1. Identifying the most salient keywords (focus on nouns, verbs, and key concepts)
            2. Extracting core themes and contextual elements
            3. Creating relevant categorical tags

            Format the response as a JSON object:
            {
                "keywords": [
                    // several specific, distinct keywords that capture key concepts and terminology
                    // Order from most to least important
                    // Don't include keywords that are the name of the speaker or time
                    // At least three keywords, but don't be too redundant.
                ],
                "context": 
                    // one sentence summarizing:
                    // - Main topic/domain
                    // - Key arguments/points
                    // - Intended audience/purpose
                ,
                "tags": [
                    // several broad categories/themes for classification
                    // Include domain, format, and type tags
                    // At least three tags, but don't be too redundant.
                ]
            }

            Content for analysis:
            
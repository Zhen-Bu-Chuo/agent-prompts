---
agent: memu
prompt_id: tool-3dc137c0fae5
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/memory_type/tool.py
source_symbol: module.PROMPT_BLOCK_EXAMPLES.1
source_lines:
- 64
- 93
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/memory_type/tool.py#L64-L93
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: f8cdbbc51d1628e877014a8607695ee5060fc2e5fa7b567b8de49115a9f015c5
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Examples (Input / Output / Explanation)
Example 1: Tool Memory Extraction
## Input
[Tool Call] file_reader(path="/data/config.json")
[Result] Success - Read 2048 bytes in 0.3s
[Tool Call] json_parser(content=<file_content>)
[Result] Success - Parsed config with 15 keys
[Tool Call] file_reader(path="/data/missing.json")
[Result] Error - FileNotFoundError: File does not exist
## Output
<item>
    <memory>
        <content>The file_reader tool successfully reads JSON config files from /data/ directory. Average read time is 0.3s for ~2KB files. Works well when chained with json_parser for config processing.</content>
        <when_to_use>When needing to read configuration files or JSON data from the filesystem</when_to_use>
        <categories>
            <category>file_operations</category>
        </categories>
    </memory>
    <memory>
        <content>The file_reader tool fails with FileNotFoundError when the target file doesn't exist. Should verify file existence before reading or handle the error gracefully.</content>
        <when_to_use>When handling file read errors or implementing robust file operations</when_to_use>
        <categories>
            <category>error_handling</category>
        </categories>
    </memory>
</item>
## Explanation
Two tool memories are extracted: one for successful usage pattern, one for error handling insight. Both include when_to_use hints for smart retrieval.

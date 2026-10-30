---
agent: aider
prompt_id: wholefile_prompts-4af778dfd449
module: editing
variant: wholefile
upstream_repository: Aider-AI/aider
upstream_version: v0.86.0
package_name: null
package_version: null
source_ref: v0.86.0
source_commit: a4be6ccd87ebaa59b361f3f028d116ce1761b626
source_path: aider/coders/wholefile_prompts.py
source_symbol: module.WholeFilePrompts.example_messages.1
source_lines:
- 27
- 41
source_permalink: https://github.com/Aider-AI/aider/blob/a4be6ccd87ebaa59b361f3f028d116ce1761b626/aider/coders/wholefile_prompts.py#L27-L41
source_committed_at: '2025-08-09T15:54:51Z'
release_published_at: '2025-08-09T17:42:19Z'
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: b7f2f6195e1ebe946208a9d383d3bad6563d1d6e56764d7716a179db752fe8e1
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Ok, I will:

1. Switch the greeting text from "Hello" to "Hey".

show_greeting.py
{fence[0]}
import sys

def greeting(name):
    print(f"Hey {{name}}")

if __name__ == '__main__':
    greeting(sys.argv[1])
{fence[1]}

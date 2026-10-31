---
agent: aider
prompt_id: editblock_fenced_prompts-21ad29848bfc
module: editing
variant: editblock_fenced
upstream_repository: Aider-AI/aider
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 5dc9490bb35f9729ef2c95d00a19ccd30c26339c
source_path: aider/coders/editblock_fenced_prompts.py
source_symbol: module.EditBlockFencedPrompts.example_messages.3
source_lines:
- 64
- 93
source_permalink: https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/aider/coders/editblock_fenced_prompts.py#L64-L93
source_committed_at: '2026-05-22T14:02:20Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:15Z'
extractor_version: 1.0.3
content_sha256: c8571e145ac85047b8446bcc5323ad8a1b4425d1280fc29fbc99b15d992b3a36
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
To make this change we need to modify `main.py` and make a new file `hello.py`:

1. Make a new hello.py file with hello() in it.
2. Remove hello() from main.py and replace it with an import.

Here are the *SEARCH/REPLACE* blocks:

{fence[0]}python
hello.py
<<<<<<< SEARCH
=======
def hello():
    "print a greeting"

    print("hello")
>>>>>>> REPLACE
{fence[1]}

{fence[0]}python
main.py
<<<<<<< SEARCH
def hello():
    "print a greeting"

    print("hello")
=======
from hello import hello
>>>>>>> REPLACE
{fence[1]}

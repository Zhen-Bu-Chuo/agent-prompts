---
agent: aider
prompt_id: patch_prompts-1815d7db6cd5
module: editing
variant: patch
upstream_repository: Aider-AI/aider
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 5dc9490bb35f9729ef2c95d00a19ccd30c26339c
source_path: aider/coders/patch_prompts.py
source_symbol: module.PatchPrompts.example_messages.3
source_lines:
- 87
- 109
source_permalink: https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/aider/coders/patch_prompts.py#L87-L109
source_committed_at: '2026-05-22T14:02:20Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:15Z'
extractor_version: 1.0.3
content_sha256: db47ddb0b6f469c478bd1b27e0bfd4d5d43ee9ce1780be1415ab15cc7bf72ff9
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
To make this change we need to modify `main.py` and create a new file `hello.py`:

1. Create `hello.py` with the `hello()` function.
2. Remove `hello()` from `main.py` and import it instead.

Here is the patch:

*** Begin Patch
*** Add File: hello.py
+# A simple function
+def hello():
+    "print a greeting"
+
+    print("hello")
*** Update File: main.py
@@
-def hello():
-    "print a greeting"
-
-    print("hello")
+from hello import hello
*** End Patch

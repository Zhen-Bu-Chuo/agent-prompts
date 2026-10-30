---
agent: aider
prompt_id: patch_prompts-1815d7db6cd5
module: editing
variant: patch
upstream_repository: Aider-AI/aider
upstream_version: v0.86.0
package_name: null
package_version: null
source_ref: v0.86.0
source_commit: a4be6ccd87ebaa59b361f3f028d116ce1761b626
source_path: aider/coders/patch_prompts.py
source_symbol: module.PatchPrompts.example_messages.3
source_lines:
- 89
- 111
source_permalink: https://github.com/Aider-AI/aider/blob/a4be6ccd87ebaa59b361f3f028d116ce1761b626/aider/coders/patch_prompts.py#L89-L111
source_committed_at: '2025-08-09T15:54:51Z'
release_published_at: '2025-08-09T17:42:19Z'
fetched_at: '2026-10-30T05:29:16Z'
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

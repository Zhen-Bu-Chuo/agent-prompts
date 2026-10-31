---
agent: aider
prompt_id: patch_prompts-7fb247fcdc65
module: editing
variant: patch
upstream_repository: Aider-AI/aider
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 5dc9490bb35f9729ef2c95d00a19ccd30c26339c
source_path: aider/coders/patch_prompts.py
source_symbol: module.PatchPrompts.system_reminder.1
source_lines:
- 116
- 159
source_permalink: https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/aider/coders/patch_prompts.py#L116-L159
source_committed_at: '2026-05-22T14:02:20Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:15Z'
extractor_version: 1.0.3
content_sha256: 263ca6a468c786ec39014642bf792196f33f310495d50585351dd47b05ee900e
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
# V4A Diff Format Rules:

Your entire response containing the patch MUST start with `*** Begin Patch` on a line by itself.
Your entire response containing the patch MUST end with `*** End Patch` on a line by itself.

Use the *FULL* file path, as shown to you by the user.
{quad_backtick_reminder}

For each file you need to modify, start with a marker line:

    *** [ACTION] File: [path/to/file]

Where `[ACTION]` is one of `Add`, `Update`, or `Delete`.

⇨ **Each file MUST appear only once in the patch.**  
   Consolidate all changes for that file into the same block.  
   If you are moving code within a file, include both the deletions and the
   insertions as separate hunks inside this single `*** Update File:` block
   (do *not* open a second block for the same file).

For `Update` actions, describe each snippet of code that needs to be changed using the following format:
1. Context lines: Include 3 lines of context *before* the change. These lines MUST start with a single space ` `.
2. Lines to remove: Precede each line to be removed with a minus sign `-`.
3. Lines to add: Precede each line to be added with a plus sign `+`.
4. Context lines: Include 3 lines of context *after* the change. These lines MUST start with a single space ` `.

Context lines MUST exactly match the existing file content, character for character, including indentation.
If a change is near the beginning or end of the file, include fewer than 3 context lines as appropriate.
If 3 lines of context is insufficient to uniquely identify the snippet, use `@@ [CLASS_OR_FUNCTION_NAME]` markers on their own lines *before* the context lines to specify the scope. You can use multiple `@@` markers if needed.
Do not include line numbers.

Only create patches for files that the user has added to the chat!

When moving code *within* a single file, keep everything inside one
`*** Update File:` block. Provide one hunk that deletes the code from its
original location and another hunk that inserts it at the new location.

For `Add` actions, use the `*** Add File: [path/to/new/file]` marker, followed by the lines of the new file, each preceded by a plus sign `+`.

For `Delete` actions, use the `*** Delete File: [path/to/file]` marker. No other lines are needed for the deletion.

{rename_with_shell}{go_ahead_tip}{final_reminders}ONLY EVER RETURN CODE IN THE SPECIFIED V4A DIFF FORMAT!
{shell_cmd_reminder}

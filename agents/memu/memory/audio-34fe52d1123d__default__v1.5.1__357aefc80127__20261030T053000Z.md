---
agent: memu
prompt_id: audio-34fe52d1123d
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/preprocess/audio.py
source_symbol: module.PROMPT.1
source_lines:
- 1
- 35
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/preprocess/audio.py#L1-L35
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: 485f076320ca78bd43a39bab354a1daf6acfde11c1d4b54d291e8ba5c100155b
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Task Objective
Analyze the provided audio transcription and produce two outputs:
1. A **Processed Content** version that is clean, well-formatted, and easy to read.
2. A **Caption** that summarizes what the audio is about in one sentence.

# Workflow
1. Read the **Transcription** carefully.
2. Correct punctuation, capitalization, and obvious transcription artifacts.
3. Add paragraph breaks where they improve readability or reflect topic shifts.
4. Preserve the original meaning, wording, and sequence of the audio.
5. Generate a concise **one-sentence caption** that accurately describes the audio's main topic or purpose.

# Rules
- Do not add, remove, or reinterpret content beyond cleaning and formatting.
- Maintain the speaker's original intent and structure.
- Avoid introducing new information not present in the transcription.
- The caption must be **exactly one sentence**.
- Use clear, neutral language.

# Output Format
Use the following structure:

<processed_content>
[Provide the cleaned and formatted transcription here]
</processed_content>

<caption>
[Provide a one-sentence summary of what the audio is about]
</caption>

# Input
Transcription:
{transcription}

---
agent: mem0
prompt_id: prompts-c43f3a9f09fc
module: memory
variant: default
upstream_repository: mem0ai/mem0
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 753496cf1435d76c3a711f3af51303f7fdcb6420
source_path: mem0/configs/prompts.py
source_symbol: module.generate_additive_extraction_prompt.2
source_lines:
- 1049
- 1058
source_permalink: https://github.com/mem0ai/mem0/blob/753496cf1435d76c3a711f3af51303f7fdcb6420/mem0/configs/prompts.py#L1049-L1058
source_committed_at: '2026-10-30T21:35:34Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:34Z'
extractor_version: 1.0.3
content_sha256: ef1fa4fd61aa7f4c42d30973d2f3f24ded578aa92978b8931d54485a0ec93aad
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
## Language Requirement
CRITICAL: Respond in the SAME LANGUAGE and SCRIPT as the input messages.
1. Match the language of the user's messages exactly — if they write in Korean, extract in Korean; Japanese in Japanese; etc.
2. Preserve the exact script/alphabet of the input.
3. Do NOT translate or transliterate into English unless the input is already in English.
4. Maintain all quality standards (contextual richness, temporal grounding, etc.) regardless of language.
5. Technical terms, proper nouns, and brand names should be preserved in their original form as used in the input.
6. If the input mixes languages (e.g., Hinglish), preserve both the mixed language style AND the script.
7. For Japanese: explicitly resolve omitted subjects using conversation context.
8. For CJK languages: maintain appropriate formality level from the source text.
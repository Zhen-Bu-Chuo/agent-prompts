---
agent: memu
prompt_id: profile-75da12beeb17
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/memory_type/profile.py
source_symbol: module.PROMPT_BLOCK_EXAMPLES.1
source_lines:
- 128
- 163
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/memory_type/profile.py#L128-L163
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: 72e028cf476dc3c8026192ac119936451d854ce6e0eb6d3526ab411db8a6501a
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Examples (Input / Output / Explanation)
Example 1: User Information Extraction
## Input
user: Hi, are you busy? I just got off work and I'm going to the supermarket to buy some groceries.
assistant: Not busy. Are you cooking for yourself?
user: Yes. It's healthier. I work as a product manager in an internet company. I'm 30 this year. After work I like experimenting with cooking, I often figure out dishes by myself.
assistant: Being a PM is tough. You're so disciplined to cook at 30!
user: It's fine. Cooking relaxes me. It's better than takeout. Also I'm traveling next weekend.
assistant: You can check the weather ahead. Your sunscreen can finally be used.
user: I haven't started packing yet. It's annoying.
## Output
<item>
    <memory>
        <content>The user works as a product manager at an internet company</content>
        <categories>
            <category>Basic Information</category>
        </categories>
    </memory>
    <memory>
        <content>The user is 30 years old</content>
        <categories>
            <category>Basic Information</category>
        </categories>
    </memory>
    <memory>
        <content>The user likes experimenting with cooking after work</content>
        <categories>
            <category>Basic Information</category>
        </categories>
    </memory>
</item>
## Explanation
Only stable user facts explicitly stated by the user are extracted.
The travel plan and packing annoyance are events/temporary states, so they are not extracted as User Information.

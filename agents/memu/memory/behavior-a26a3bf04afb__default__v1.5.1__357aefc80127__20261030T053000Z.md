---
agent: memu
prompt_id: behavior-a26a3bf04afb
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/memory_type/behavior.py
source_symbol: module.PROMPT_BLOCK_EXAMPLES.1
source_lines:
- 119
- 149
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/memory_type/behavior.py#L119-L149
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: 04b2020328385a37367b14e9e72005f1023a7bdfbe2ef957ed71745a0c7dfe30
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Examples (Input / Output / Explanation)
Example 1: Behavior Information Extraction
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
        <content>The user typically cooks for themselves after work instead of ordering takeout</content>
        <categories>
            <category>Daily Routine</category>
        </categories>
    </memory>
    <memory>
        <content>The user often experiments with cooking and figures out dishes by themselves</content>
        <categories>
            <category>Daily Routine</category>
        </categories>
    </memory>
</item>
## Explanation
Only behavioral patterns explicitly stated by the user are extracted.
Cooking after work and experimenting with dishes are recurring behaviors/routines.
User's job, age are stable traits (not behaviors). The travel plan is a one-time event, not a behavioral pattern.

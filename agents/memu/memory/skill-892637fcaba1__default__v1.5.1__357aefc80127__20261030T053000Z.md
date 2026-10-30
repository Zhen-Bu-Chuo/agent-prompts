---
agent: memu
prompt_id: skill-892637fcaba1
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/memory_type/skill.py
source_symbol: module.PROMPT_BLOCK_OUTPUT.1
source_lines:
- 434
- 484
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/memory_type/skill.py#L434-L484
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: ae6642b8a9654bfb0dea932d9c28d4f3fda4f40b627df3443b7e79964d211e57
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Output Format (XML)
Return all memories wrapped in a single <item> element:
<item>
    <memory>
        <content>
---
name: skill-name-in-kebab-case
description: One-line description of what this skill enables
category: primary-category
demonstrated-in: [context where this was shown]
---

[Brief introduction explaining the skill and its importance]

## Core Principles
- [Key concept 1]
- [Key concept 2]

## When to Use This Skill
- [Situation 1]
- [Situation 2]

## Implementation Guide
### Prerequisites
- [Required knowledge or setup]

### Techniques and Approaches
[Detailed explanation of how to apply this skill]

### Example from Resource
[Concrete example from the source material]

## Success Patterns
- [Pattern 1 with explanation]
- [Pattern 2 with explanation]

## Common Pitfalls
- [Pitfall 1]: [Why it's a problem and how to avoid it]
- [Pitfall 2]: [Why it's a problem and how to avoid it]

## Key Takeaways
- [Critical insight 1]
- [Critical insight 2]
        </content>
        <categories>
            <category>technical_skills</category>
        </categories>
    </memory>
</item>

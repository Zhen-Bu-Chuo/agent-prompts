---
agent: memu
prompt_id: skill-8fe4fedbfd35
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/memory_type/skill.py
source_symbol: module.PROMPT_BLOCK_EXAMPLES.1
source_lines:
- 486
- 553
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/memory_type/skill.py#L486-L553
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: b9571a1885aa496a81be4a8ae9ecdafdd4a5f0b0c0a91d8cbaf310e5886ccc91
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Examples (Input / Output / Explanation)
Example 1: Skill Extraction from Deployment Log
## Input
[2024-01-15 10:30:00] Starting canary deployment for Payment Service v2.3.1
[2024-01-15 10:30:15] Deployed new version alongside existing v2.3.0
[2024-01-15 10:30:30] Configured load balancer: 10% traffic to v2.3.1
[2024-01-15 10:35:30] Metrics check: Error rate 0.1% (baseline 0.1%), p95 latency 270ms (baseline 320ms)
[2024-01-15 10:35:45] Increasing traffic to 50%
[2024-01-15 10:40:45] Metrics stable, increasing to 100%
[2024-01-15 10:42:00] Deployment complete. Zero downtime achieved.
## Output
<item>
    <memory>
        <content>
---
name: canary-deployment-with-monitoring
description: Implement gradual traffic shifting deployment strategy with real-time monitoring
category: deployment
demonstrated-in: [Payment Service v2.3.1 deployment]
---

Canary deployment is a risk-mitigation strategy that gradually shifts production traffic from an old version to a new version while continuously monitoring key metrics. This approach enables early detection of issues with minimal user impact.

## Core Principles
- Gradual exposure: Start with a small percentage of traffic (typically 5-10%) to limit blast radius
- Continuous monitoring: Track error rates, response times in real-time
- Quick recovery: Maintain ability to instantly route traffic back to stable version

## When to Use This Skill
- Deploying critical services where downtime is unacceptable
- Rolling out changes with uncertain production behavior
- High-traffic services where testing production performance is valuable

## Implementation Guide
### Prerequisites
- Load balancer with traffic splitting capabilities
- Monitoring system with real-time metrics
- Automated deployment pipeline

### Techniques and Approaches
1. Initial Deployment (10% traffic): Deploy new version alongside existing, route 10% traffic, monitor 5 minutes
2. Monitoring Checkpoints: Error rate should not exceed baseline by more than 2%, response time within 20% of baseline
3. Gradual Rollout: If metrics stable, progress 10% to 25% to 50% to 100%

### Example from Resource
Payment Service v2.3.1 deployment achieved zero downtime during 12-minute deployment. Traffic progressed 10% to 50% to 100% with 5-minute pauses. Response time improved 15% (320ms to 270ms p95). Error rate remained stable at 0.1%.

## Success Patterns
- Small initial percentage: 5-10% catches most issues while limiting impact
- Metric-driven automation: Removes human error from rollback decisions

## Common Pitfalls
- Too aggressive progression: Rushing from 10% to 100% defeats the purpose
- Insufficient monitoring window: Need 5+ minutes at each stage to detect issues

## Key Takeaways
- Canary deployments trade deployment speed for safety
- Start small, progress gradually, monitor continuously
        </content>
        <categories>
            <category>technical_skills</category>
        </categories>
    </memory>
</item>
## Explanation
A comprehensive skill profile is extracted from the deployment log, capturing the approach, techniques, metrics, and outcomes. The profile includes all required sections and provides actionable guidance for replicating the skill.

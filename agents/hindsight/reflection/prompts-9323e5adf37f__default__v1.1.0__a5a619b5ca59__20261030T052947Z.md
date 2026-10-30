---
agent: hindsight
prompt_id: prompts-9323e5adf37f
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: v1.1.0
package_name: null
package_version: null
source_ref: v1.1.0
source_commit: a5a619b5ca59c5c39e0f96be6f7a31fabd136bd5
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.5
source_lines:
- 292
- 292
source_permalink: https://github.com/vectorize-io/hindsight/blob/a5a619b5ca59c5c39e0f96be6f7a31fabd136bd5/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L292-L292
source_committed_at: '2026-10-21T16:16:23Z'
release_published_at: '2026-10-21T16:41:42Z'
fetched_at: '2026-10-30T05:29:47Z'
extractor_version: 1.0.3
content_sha256: 9974a254c6caae892d35da4718cca183e6029b17febba8020b5b8aafe7526ba7
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
A DECISION is different from a state. When the record holds a decision with its rationale (what was decided and why) and a later record changes the same thing WITHOUT stating a reason that overturns that decision (a refactor, a 'simplification', a cleanup, a performance change), the later record does NOT supersede the decision: report the decision as the standing one, and report the later change as a departure from it. Only a later record that itself decides, with its own rationale, replaces an earlier decision. Example: 'Invoices are due net-30; finance chose it for cash flow' (March) and 'cleanup: simplify billing config, terms = net-45' (May) → the rule is net-30; the May cleanup is a change that departed from it, NOT the rule.
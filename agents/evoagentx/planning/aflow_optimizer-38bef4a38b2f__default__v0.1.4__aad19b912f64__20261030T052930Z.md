---
agent: evoagentx
prompt_id: aflow_optimizer-38bef4a38b2f
module: planning
variant: default
upstream_repository: ANative-Lab/EvoAgentX
upstream_version: v0.1.4
package_name: null
package_version: null
source_ref: v0.1.4
source_commit: aad19b912f640161ea07e8904d9237cd34fde5f1
source_path: evoagentx/prompts/optimizers/aflow_optimizer.py
source_symbol: module.WORKFLOW_TEMPLATE.1
source_lines:
- 54
- 61
source_permalink: https://github.com/ANative-Lab/EvoAgentX/blob/aad19b912f640161ea07e8904d9237cd34fde5f1/evoagentx/prompts/optimizers/aflow_optimizer.py#L54-L61
source_committed_at: '2026-06-28T10:20:05Z'
release_published_at: '2026-06-28T10:24:06Z'
fetched_at: '2026-10-30T05:29:30Z'
extractor_version: 1.0.3
content_sha256: 91ddf66d13f05bb652f1430c264c3dc545624322a7b880cbe91ef1f97b492206
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
import evoagentx.workflow.operators as operator
import examples.aflow.humaneval.prompt as prompt_custom
from evoagentx.models.model_configs import LLMConfig
from evoagentx.benchmark.benchmark import Benchmark
from evoagentx.models.model_utils import create_llm_instance

{graph}

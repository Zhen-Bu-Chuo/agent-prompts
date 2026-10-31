---
agent: evoagentx
prompt_id: aflow_optimizer-3325c4748c3f
module: evolution
variant: default
upstream_repository: ANative-Lab/EvoAgentX
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: e3df900662443e94dd92141be5633b040a69a70a
source_path: evoagentx/prompts/optimizers/aflow_optimizer.py
source_symbol: module.WORKFLOW_TEMPLATE.1
source_lines:
- 54
- 61
source_permalink: https://github.com/ANative-Lab/EvoAgentX/blob/e3df900662443e94dd92141be5633b040a69a70a/evoagentx/prompts/optimizers/aflow_optimizer.py#L54-L61
source_committed_at: '2026-10-31T01:49:52Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:23Z'
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

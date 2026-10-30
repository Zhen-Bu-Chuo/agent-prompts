# EvoAgentX prompt and mechanism sources

- Repository: [`ANative-Lab/EvoAgentX`](https://github.com/ANative-Lab/EvoAgentX)
- Selected release/branch: `v0.1.4`
- Commit: `aad19b912f640161ea07e8904d9237cd34fde5f1`
- SPDX metadata: `MIT`
- Collection status: `supported`

## Selected source files

| Module | Extractor | Pinned source |
| --- | --- | --- |
| `evolution` | `python` | [`evoagentx/optimizers/evoprompt_optimizer.py`](https://github.com/ANative-Lab/EvoAgentX/blob/aad19b912f640161ea07e8904d9237cd34fde5f1/evoagentx/optimizers/evoprompt_optimizer.py) |
| `planning` | `python` | [`evoagentx/prompts/memory/manager.py`](https://github.com/ANative-Lab/EvoAgentX/blob/aad19b912f640161ea07e8904d9237cd34fde5f1/evoagentx/prompts/memory/manager.py) |
| `evolution`, `planning` | `python` | [`evoagentx/prompts/optimizers/aflow_optimizer.py`](https://github.com/ANative-Lab/EvoAgentX/blob/aad19b912f640161ea07e8904d9237cd34fde5f1/evoagentx/prompts/optimizers/aflow_optimizer.py) |
| `evolution`, `planning` | `python` | [`evoagentx/prompts/optimizers/textgrad_optimizer.py`](https://github.com/ANative-Lab/EvoAgentX/blob/aad19b912f640161ea07e8904d9237cd34fde5f1/evoagentx/prompts/optimizers/textgrad_optimizer.py) |
| `planning` | `python` | [`evoagentx/prompts/rag/graph_extract.py`](https://github.com/ANative-Lab/EvoAgentX/blob/aad19b912f640161ea07e8904d9237cd34fde5f1/evoagentx/prompts/rag/graph_extract.py) |
| `planning` | `python` | [`evoagentx/prompts/rag/graph_synonym.py`](https://github.com/ANative-Lab/EvoAgentX/blob/aad19b912f640161ea07e8904d9237cd34fde5f1/evoagentx/prompts/rag/graph_synonym.py) |
| `planning` | `python` | [`evoagentx/prompts/rag/hyde.py`](https://github.com/ANative-Lab/EvoAgentX/blob/aad19b912f640161ea07e8904d9237cd34fde5f1/evoagentx/prompts/rag/hyde.py) |
| `planning` | `python` | [`evoagentx/prompts/workflow/multi_agent_debate.py`](https://github.com/ANative-Lab/EvoAgentX/blob/aad19b912f640161ea07e8904d9237cd34fde5f1/evoagentx/prompts/workflow/multi_agent_debate.py) |
| `planning` | `python` | [`evoagentx/prompts/workflow/sew_optimizer.py`](https://github.com/ANative-Lab/EvoAgentX/blob/aad19b912f640161ea07e8904d9237cd34fde5f1/evoagentx/prompts/workflow/sew_optimizer.py) |
| `planning` | `python` | [`evoagentx/prompts/workflow/workflow_editor.py`](https://github.com/ANative-Lab/EvoAgentX/blob/aad19b912f640161ea07e8904d9237cd34fde5f1/evoagentx/prompts/workflow/workflow_editor.py) |
| `planning` | `python` | [`evoagentx/prompts/workflow/workflow_manager.py`](https://github.com/ANative-Lab/EvoAgentX/blob/aad19b912f640161ea07e8904d9237cd34fde5f1/evoagentx/prompts/workflow/workflow_manager.py) |

## Current coverage

- Coverage: `supported`.
- Pinned upstream version: `v0.1.4` at commit `aad19b912f640161ea07e8904d9237cd34fde5f1`.
- 将候选 Prompt 生成、优化器反馈与 workflow 编辑提示单独归档；score、候选列表和模型响应属于运行时状态。

## Collection notes
The collector reads only these configured file paths from the pinned commit. It parses structured strings and templates as data and does not run the upstream agent. A source entry is a static template fragment; values supplied at runtime remain unresolved.

- 将候选 Prompt 生成、优化器反馈与 workflow 编辑提示单独归档；score、候选列表和模型响应属于运行时状态。

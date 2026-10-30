# SWE-agent prompt and mechanism sources

- Repository: [`SWE-agent/SWE-agent`](https://github.com/SWE-agent/SWE-agent)
- Selected release/branch: `v1.1.0`
- Commit: `0f3acafacabc0def8cc76b4e48acb4b6cf302cb9`
- SPDX metadata: `MIT`
- Collection status: `partial`

## Selected source files

| Module | Extractor | Pinned source |
| --- | --- | --- |
| `system` | `yaml` | [`config/default.yaml`](https://github.com/SWE-agent/SWE-agent/blob/0f3acafacabc0def8cc76b4e48acb4b6cf302cb9/config/default.yaml) |
| `system` | `yaml` | [`config/default_backticks.yaml`](https://github.com/SWE-agent/SWE-agent/blob/0f3acafacabc0def8cc76b4e48acb4b6cf302cb9/config/default_backticks.yaml) |
| `execution` | `yaml` | [`config/sweagent_0_7/07.yaml`](https://github.com/SWE-agent/SWE-agent/blob/0f3acafacabc0def8cc76b4e48acb4b6cf302cb9/config/sweagent_0_7/07.yaml) |
| `execution` | `yaml` | [`config/sweagent_0_7/07_fcalling.yaml`](https://github.com/SWE-agent/SWE-agent/blob/0f3acafacabc0def8cc76b4e48acb4b6cf302cb9/config/sweagent_0_7/07_fcalling.yaml) |
| `execution` | `yaml` | [`config/sweagent_0_7/07_from_url.yaml`](https://github.com/SWE-agent/SWE-agent/blob/0f3acafacabc0def8cc76b4e48acb4b6cf302cb9/config/sweagent_0_7/07_from_url.yaml) |
| `execution` | `yaml` | [`config/sweagent_0_7/07_thought_action.yaml`](https://github.com/SWE-agent/SWE-agent/blob/0f3acafacabc0def8cc76b4e48acb4b6cf302cb9/config/sweagent_0_7/07_thought_action.yaml) |
| `execution` | `yaml` | [`config/sweagent_0_7/07_thought_action_xml.yaml`](https://github.com/SWE-agent/SWE-agent/blob/0f3acafacabc0def8cc76b4e48acb4b6cf302cb9/config/sweagent_0_7/07_thought_action_xml.yaml) |

## Current coverage

- Coverage: `partial`.
- Pinned upstream version: `v1.1.0` at commit `0f3acafacabc0def8cc76b4e48acb4b6cf302cb9`.
- 当前公开稳定 v1.1.0 将运行提示模板保存在 YAML 配置中；本采集器只选取 default 与 sweagent_0_7 里可证实的 instruction/instance/next-step 模板，不采集 benchmark 与轨迹样本。
- agent loop 根据工具、环境、observation 和步骤状态插入占位符，静态文件不等同于最终的完整模型消息。

## Collection notes
The collector reads only these configured file paths from the pinned commit. It parses structured strings and templates as data and does not run the upstream agent. A source entry is a static template fragment; values supplied at runtime remain unresolved.

- 当前公开稳定 v1.1.0 将运行提示模板保存在 YAML 配置中；本采集器只选取 default 与 sweagent_0_7 里可证实的 instruction/instance/next-step 模板，不采集 benchmark 与轨迹样本。
- agent loop 根据工具、环境、observation 和步骤状态插入占位符，静态文件不等同于最终的完整模型消息。

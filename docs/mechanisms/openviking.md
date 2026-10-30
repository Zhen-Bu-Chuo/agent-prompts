# OpenViking prompt and mechanism sources

- Repository: [`volcengine/OpenViking`](https://github.com/volcengine/OpenViking)
- Selected release/branch: `v0.5.2.1`
- Commit: `f5e6203033a13469c3d9a937f2ca39492ea69c51`
- SPDX metadata: `AGPL-3.0-only`
- Collection status: `supported`

## Selected source files

| Module | Extractor | Pinned source |
| --- | --- | --- |
| `memory` | `raw` | [`agent-plugins/skills/openviking-memory/SKILL.md`](https://github.com/volcengine/OpenViking/blob/f5e6203033a13469c3d9a937f2ca39492ea69c51/agent-plugins/skills/openviking-memory/SKILL.md) |
| `evolution` | `raw` | [`agent-plugins/skills/ov-experience-memory/SKILL.md`](https://github.com/volcengine/OpenViking/blob/f5e6203033a13469c3d9a937f2ca39492ea69c51/agent-plugins/skills/ov-experience-memory/SKILL.md) |
| `memory` | `python` | [`openviking/session/memory/extraction_output_protocol/json_protocol.py`](https://github.com/volcengine/OpenViking/blob/f5e6203033a13469c3d9a937f2ca39492ea69c51/openviking/session/memory/extraction_output_protocol/json_protocol.py) |
| `memory` | `python` | [`openviking/session/memory/extraction_output_protocol/python_protocol.py`](https://github.com/volcengine/OpenViking/blob/f5e6203033a13469c3d9a937f2ca39492ea69c51/openviking/session/memory/extraction_output_protocol/python_protocol.py) |

## Current coverage

- Coverage: `supported`.
- Pinned upstream version: `v0.5.2.1` at commit `f5e6203033a13469c3d9a937f2ca39492ea69c51`.
- OpenViking 使用 AGPL-3.0；保存上游许可证和 commit 署名。基准测试中的第三方 Agent prompt 不作为 OpenViking 自有提示词采集。

## Collection notes
The collector reads only these configured file paths from the pinned commit. It parses structured strings and templates as data and does not run the upstream agent. A source entry is a static template fragment; values supplied at runtime remain unresolved.

- OpenViking 使用 AGPL-3.0；保存上游许可证和 commit 署名。基准测试中的第三方 Agent prompt 不作为 OpenViking 自有提示词采集。

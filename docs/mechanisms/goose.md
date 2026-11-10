# Goose prompt and mechanism sources

- Repository: [`aaif-goose/goose`](https://github.com/aaif-goose/goose)
- Selected release/branch: `v1.58.1`
- Commit: `c97af00bca96442611bb95155c56d6109afa42d6`
- SPDX metadata: `Apache-2.0`
- Collection status: `supported`

## Selected source files

| Module | Extractor | Pinned source |
| --- | --- | --- |
| `system` | `raw` | [`crates/goose/src/prompts/apps_create.md`](https://github.com/aaif-goose/goose/blob/c97af00bca96442611bb95155c56d6109afa42d6/crates/goose/src/prompts/apps_create.md) |
| `system` | `raw` | [`crates/goose/src/prompts/apps_iterate.md`](https://github.com/aaif-goose/goose/blob/c97af00bca96442611bb95155c56d6109afa42d6/crates/goose/src/prompts/apps_iterate.md) |
| `system` | `raw` | [`crates/goose/src/prompts/permission_judge.md`](https://github.com/aaif-goose/goose/blob/c97af00bca96442611bb95155c56d6109afa42d6/crates/goose/src/prompts/permission_judge.md) |
| `system` | `raw` | [`crates/goose/src/prompts/session_name.md`](https://github.com/aaif-goose/goose/blob/c97af00bca96442611bb95155c56d6109afa42d6/crates/goose/src/prompts/session_name.md) |
| `system` | `raw` | [`crates/goose/src/prompts/subagent_system.md`](https://github.com/aaif-goose/goose/blob/c97af00bca96442611bb95155c56d6109afa42d6/crates/goose/src/prompts/subagent_system.md) |
| `system` | `raw` | [`crates/goose/src/prompts/system.md`](https://github.com/aaif-goose/goose/blob/c97af00bca96442611bb95155c56d6109afa42d6/crates/goose/src/prompts/system.md) |
| `system` | `raw` | [`crates/goose/src/prompts/tiny_model_system.md`](https://github.com/aaif-goose/goose/blob/c97af00bca96442611bb95155c56d6109afa42d6/crates/goose/src/prompts/tiny_model_system.md) |

## Current coverage

- Coverage: `supported`.
- Pinned upstream version: `v1.58.1` at commit `c97af00bca96442611bb95155c56d6109afa42d6`.
- 仓库从 block/goose 迁移至 aaif-goose/goose；已跟随 canonical repository，保持原产品对应关系。
- 工具注册和 MCP 上下文由执行期间组装。

## Collection notes
The collector reads only these configured file paths from the pinned commit. It parses structured strings and templates as data and does not run the upstream agent. A source entry is a static template fragment; values supplied at runtime remain unresolved.

- 仓库从 block/goose 迁移至 aaif-goose/goose；已跟随 canonical repository，保持原产品对应关系。
- 工具注册和 MCP 上下文由执行期间组装。

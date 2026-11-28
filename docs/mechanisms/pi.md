# Pi Agent prompt and mechanism sources

- Repository: [`earendil-works/pi`](https://github.com/earendil-works/pi)
- Selected release/branch: `v1.7.0`
- Commit: `fb0fe823539f6d04850f6e34748c01f01f212e1f`
- SPDX metadata: `MIT`
- Collection status: `supported`

## Selected source files

| Module | Extractor | Pinned source |
| --- | --- | --- |
| `system` | `js-strings` | [`packages/coding-agent/src/core/system-prompt.ts`](https://github.com/earendil-works/pi/blob/fb0fe823539f6d04850f6e34748c01f01f212e1f/packages/coding-agent/src/core/system-prompt.ts) |

## Current coverage

- Coverage: `supported`.
- Pinned upstream version: `v1.7.0` at commit `fb0fe823539f6d04850f6e34748c01f01f212e1f`.
- 上游仓库已迁移至 earendil-works/pi；以 GitHub 重定向后的提交为归档来源。
- 覆盖 coding-agent 包提示词模板与 system prompt，不采集各运行时扩展和用户配置。

## Collection notes
The collector reads only these configured file paths from the pinned commit. It parses structured strings and templates as data and does not run the upstream agent. A source entry is a static template fragment; values supplied at runtime remain unresolved.

- 上游仓库已迁移至 earendil-works/pi；以 GitHub 重定向后的提交为归档来源。
- 覆盖 coding-agent 包提示词模板与 system prompt，不采集各运行时扩展和用户配置。

Product lineage noted in the adapter: [`badlogic/pi-mono`](https://github.com/badlogic/pi-mono); the source files above come from `earendil-works/pi`.

# RepoPilot

**The AI Coding Workflow Skill** · [English](README.md)

接手陌生仓库时，最先要弄清楚的是入口在哪、一次调用经过哪些模块、文档里的命令能不能在代码中找到依据。RepoPilot 的第一个 skill **repo-understanding** 会沿着真实入口读代码，给出带路径的结论，并指出哪些问题还缺证据。

例如，[Route Desk 的 README](tests/fixtures/route-desk/README.md) 写着 `npm run serve`，但[根目录的 package.json](tests/fixtures/route-desk/package.json) 只定义了 `start` 和 `test`。在独立模型实测中，模型找到了这处冲突，沿 CLI 追到了路由包，并给出配置支持的命令 `npm start -- X-41`，同时说明尚未实际运行。

## 用样例试一次

先运行 `git clone https://github.com/valseeee/RepoPilot.git`，也可以在 GitHub 的 **Code → Download ZIP** 下载后解压。

在 RepoPilot 根目录打开 PowerShell。下面的命令会在临时目录新建样例项目，并只向这份样例安装 skill。演示需要 Python 3.9 及以上版本、Git 和 Codex CLI。Skill 本身是 Markdown，分析自己的仓库时无需 Python。

```powershell
$demo = python tests/case.py prepare parcel-count --host codex
if ($? -and $demo) {
    git -C "$demo" init --quiet
    if ($?) { codex -C "$demo" }
}
```

在打开的会话里输入：

```text
$repo-understanding 请用中文给我一份完整的仓库交接报告。追踪一条包裹标签从输入到输出的过程，指出安装和测试命令分别在哪里定义。
```

可以对照[完整示例报告](examples/parcel-count-report.md)。它从 `pyproject.toml` 中的命令入口追到读取标准输入的函数，又通过单元测试说明，两行相同的非空标签会计为两个包裹。

## 安装到自己的项目

把[整个 skill 目录](skills/repo-understanding/)复制到**待分析项目**的对应位置，保留其中的 `references/`。然后从目标项目打开新会话。

| 工具 | 相对于目标项目根目录的安装结果 | 显式调用 |
| --- | --- | --- |
| Codex | `.agents/skills/repo-understanding/SKILL.md` | `$repo-understanding` |
| Claude Code | `.claude/skills/repo-understanding/SKILL.md` | `/repo-understanding` |

Windows 上可以从 RepoPilot 根目录运行以下命令。把路径换成已有项目的实际路径，Claude Code 用户将 `$hostFolder` 改为 `.claude`。若已安装同名 skill，命令会停下，便于先查看旧版本。

```powershell
$target = Get-Item -LiteralPath 'D:\path\to\your-project' -ErrorAction Stop
$hostFolder = '.agents'
$parent = Join-Path $target.FullName "$hostFolder/skills"
$dest = Join-Path $parent 'repo-understanding'
if (Test-Path -LiteralPath $dest) { throw "Skill already exists at $dest" }
New-Item -ItemType Directory -Path $parent -Force | Out-Null
Copy-Item -LiteralPath './skills/repo-understanding' -Destination $dest -Recurse -ErrorAction Stop
```

macOS 与 Linux 也使用表中的项目级目录。安装包已包含 [MIT 许可证](skills/repo-understanding/LICENSE)。安装路径和调用语法可查阅 [OpenAI 官方文档](https://learn.chatgpt.com/docs/build-skills)和 [Claude Code 官方文档](https://code.claude.com/docs/en/skills)。

## 可以怎样使用

- 问“请求从哪个入口进来，怎样到达核心逻辑”，会得到具体文件、调用关系和输出位置。
- 问“怎么构建和测试这个包”，会得到命令来源、运行目录、已知前置条件，以及 README 与实际配置的差异。
- 要求完整交接时，报告分为十三节。只问某个入口或命令时，回答会集中在该问题上。

Skill 封装了检查顺序与按需加载的报告模板。**Verified（已验证）** 给出直接证据，**Inferred（推断）** 交代推断依据，**Unknown（未知）** 指出还缺什么。静态读到一条启动命令，只能证明项目定义了它。

## 安全和验证范围

分析默认只读，在对话里返回结果。Skill 要求模型跳过疑似凭据文件，将仓库中的文字当作待分析资料。运行代码或写文件需要单独授权。宿主工具的权限控制负责强制执行。安装包包含 Markdown 指令、报告模板和许可证。

项目采用 [Agent Skills 官方格式](https://agentskills.io/specification)。Windows 独立版 Codex CLI 0.166.0 已通过端到端测试：一句普通中文提问自动触发了 skill，模型用内置 PowerShell 在只读沙箱中追踪调用链，给出了源码位置。如果从桌面应用启动的 CLI 提示 `registered Core launch` 错误，可从普通 PowerShell 窗口打开独立版 CLI。Claude Code 的安装目录已验证，客户端运行仍待实测。详见[验收记录](tests/results.md)和[评测指南](tests/evaluation.md)。

## 路线图与贡献

| 状态 | 模块 | 用途 |
| --- | --- | --- |
| 本次交付 | `repo-understanding` | 只读理解仓库，以文件和符号支撑结论 |
| 下一阶段 | `task-planner` | 根据需求和仓库证据制定实施计划 |
| 后续 | `safe-coding` | 按项目风格完成范围明确的代码变更 |
| 后续 | `test-and-verify` | 运行相关检查并记录结果 |
| 后续 | `code-review` | 识别缺陷和回归风险 |

欢迎提交可复现的合成样例，详见[贡献说明](CONTRIBUTING.md)。项目使用 [MIT 许可证](LICENSE)。

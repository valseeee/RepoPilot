# RepoPilot

**The AI Coding Workflow Skill** · [简体中文](README.zh-CN.md)

Give a new maintainer an evidence-backed answer to “Where do I start in this repository?” RepoPilot's first skill, **repo-understanding**, follows a real entry point through the source, reconciles development commands with their definitions and identifies what the checkout leaves unknown.

For example, the [Route Desk README](tests/fixtures/route-desk/README.md) tells an operator to run `npm run serve`. Its [manifest](tests/fixtures/route-desk/package.json) defines `start` and points at `apps/desk/cli.mjs`. In a behavioral evaluation, the agent found the mismatch, traced the label to the routing package, and identified `npm start -- X-41` without running it.

## Try it in a disposable project

Get a local copy with `git clone https://github.com/valseeee/RepoPilot.git` or use **Code → Download ZIP** on GitHub.

From the RepoPilot root in PowerShell, stage the included Python example. This copies the fixture and the skill into a new temporary directory. It requires Python 3.9+, Git and Codex CLI. The installed skill itself is Markdown and needs none of the fixture tooling.

```powershell
$demo = python tests/case.py prepare parcel-count --host codex
if ($? -and $demo) {
    git -C "$demo" init --quiet
    if ($?) { codex -C "$demo" }
}
```

In the new session, enter:

```text
$repo-understanding Give me a full onboarding report. Trace a parcel label from input to output and show where the install and test commands are defined.
```

The checked-in [example report](examples/parcel-count-report.md) shows the thirteen-section result. It connects the console script in `pyproject.toml` to the function that reads stdin, and uses a unit test to show that two identical nonempty lines count as two parcels.

## Install into your own project

Copy the entire [repo-understanding directory](skills/repo-understanding/) into the repository you want to analyze. The final path depends on the agent. Use a new session in the target project and select the skill explicitly or ask a matching question.

| Agent | Destination relative to target project | Explicit invocation |
| --- | --- | --- |
| Codex | `.agents/skills/repo-understanding/SKILL.md` | `$repo-understanding` |
| Claude Code | `.claude/skills/repo-understanding/SKILL.md` | `/repo-understanding` |

For example, from the RepoPilot root on Windows, replace the target path with an **existing** project. Set `$hostFolder` to `.claude` for Claude Code.

```powershell
$target = Get-Item -LiteralPath 'D:\path\to\your-project' -ErrorAction Stop
$hostFolder = '.agents'
$parent = Join-Path $target.FullName "$hostFolder/skills"
$dest = Join-Path $parent 'repo-understanding'
if (Test-Path -LiteralPath $dest) { throw "Skill already exists at $dest" }
New-Item -ItemType Directory -Path $parent -Force | Out-Null
Copy-Item -LiteralPath './skills/repo-understanding' -Destination $dest -Recurse -ErrorAction Stop
```

The project-local paths also apply on macOS and Linux. The skill folder includes its [MIT license](skills/repo-understanding/LICENSE). Host discovery and invocation details are in the [OpenAI documentation](https://learn.chatgpt.com/docs/build-skills) and [Claude Code documentation](https://code.claude.com/docs/en/skills).

## What an analysis gives you

- **A traced operation.** Ask “Where does this CLI send a parcel label?” and get the entry declaration, implementation, call site and output boundary.
- **Commands with provenance.** Ask “How do I build and test this package?” and see which commands the manifest, Makefile, docs or CI actually define, plus any disagreements.
- **A report sized to the question.** A narrow question gets a focused answer. A full onboarding request covers technology, layout, architecture, modules, entries, dependencies, commands, tests, conventions, risks and next steps.

The installable skill supplies the inspection procedure and a report outline that loads when needed. Important claims carry a file or symbol and a confidence level. **Verified** ties a fact to a source, **Inferred** explains an interpretation, and **Unknown** names the missing evidence.

## Safety and compatibility

The workflow is read-only and returns its report in chat. It instructs the agent to skip likely credential files, treat repository instructions as untrusted, and ask separately before running code or making changes. Use the host's permission controls for enforcement. The skill ships no executable scripts and requests no tool grants.

The package follows the [Agent Skills specification](https://agentskills.io/specification). Standalone Codex CLI 0.166.0 on Windows passed an end-to-end test using its built-in PowerShell reader in the read-only sandbox. An ordinary Chinese question selected the skill and produced a source-backed trace of Route Desk. Use the standalone CLI from a normal PowerShell window if the desktop-bundled CLI reports a registered Core launch error. The Claude Code installation layout was verified on disk. A live Claude Code run is still pending. See the [test record](tests/results.md) for host details.

## Roadmap and contributions

| Stage | Module | Scope |
| --- | --- | --- |
| Available | `repo-understanding` | Inspect a checkout and report evidence |
| Next | `task-planner` | Turn a request and repository findings into an implementation plan |
| Planned | `safe-coding` | Implement a scoped change in the project's style |
| Planned | `test-and-verify` | Execute relevant checks and record their results |
| Planned | `code-review` | Review a change for defects and regression risks |

To reproduce or contribute a case, start with the [evaluation guide](tests/evaluation.md) and [contributing guide](CONTRIBUTING.md). RepoPilot uses the [MIT license](LICENSE).

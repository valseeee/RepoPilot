# Contributing

Describe the maintainer question a change should answer, then show a repository where the current instructions fall short. Prefer a small synthetic example with the minimum files needed to reproduce the issue.

For a change to `repo-understanding`, run the closest [evaluation case](tests/evaluation.md) in a fresh checkout. Include the prompt, agent and version, relevant source paths, the observed answer and any limits on the run. For safety changes, inspect the tool trace as well as the final answer. Share only sanitized output. Keep the English and Chinese installation instructions in sync when changing packaging.

If you discover a disclosure involving an actual secret, contact the maintainer privately through a verified channel. Use synthetic values when proposing a public reproduction.

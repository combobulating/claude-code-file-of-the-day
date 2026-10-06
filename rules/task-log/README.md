# A Claude Code rule that keeps a task log so a new conversation continues where you stopped

A rule for your global CLAUDE.md: Claude keeps a log of each task, and a new conversation reads it and continues where the last one stopped.

Claude Code rule · 2026-10-06 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-task-log-rule) on combobulating.ai · [По-русски](ru/) · [Srpski](sr/) · [Português](pt/)

## How to add the rule: a task log, so a new conversation continues from where you stopped

1. Ask Claude: "Append the contents of the downloaded file task-log.md to the end of the file ~/.claude/CLAUDE.md, and if there is no such file, create it".
2. Close Claude Code and open it again: the rule is read at startup.

Check:

1. Ask Claude: "Make a shopping list for opening a coffee shop". In the first line of the answer, Claude will write the path to the log of this task.
2. Close Claude Code, open it again and ask: "Let's continue the shopping list for the coffee shop". Claude will find the log and continue from where you stopped. Without the file, a new conversation starts from zero.

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

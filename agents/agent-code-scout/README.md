# A Claude Code subagent that finds code without eating your context

A Claude Code subagent that searches unfamiliar code in its own context and hands back only paths and line numbers. One file, a minute to install.

Claude Code subagent · 2026-09-24 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-subagent-code-search) on combobulating.ai · [По-русски](ru/)

## How to install the code scout agent

The agent searches code in its own context and returns only addresses to the main session: the path and the line number. The main session does not spend its context on reading files, and the search itself runs on the model you assign to the agent.

Where to put it:
```
mkdir -p ~/.claude/agents
cp agent-code-scout.md ~/.claude/agents/
```

What to fill in: in the `model` line, the model the search will run on: `haiku`, `sonnet`, `opus`, `fable`, a full model ID or `inherit` (the main session's model). In the `effort` line, the effort level: `low`, `medium`, `high`, `xhigh` or `max`; which levels are available depends on the model.

How to check that it works: open a new Claude Code session and ask:
```
Using the code-scout agent, find where the function <name> is defined in this project
```

While the agent is running, the `/tasks` command shows its row and the model it runs on. The answer will come as lines like `path:line_number - what is there`, not as file contents.

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

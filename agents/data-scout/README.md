# A Claude Code subagent that collects data and leaves the conclusions to you

A Claude Code subagent that runs queries, appends each result with its source to a shared file and answers in a line or two. Conclusions stay with you.

Claude Code subagent · 2026-09-26 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-data-collection-subagent) on combobulating.ai · [По-русски](ru/)

## How to install the data collector

1. Put `data-scout.md` into the `~/.claude/agents/` folder.
2. In the `model` and `effort` lines set the model and effort level you give to data collection.
3. In the `tools` line keep only the tools that collection needs.
4. Restart Claude Code.

Check:

1. Type `@` and find `data-scout` in the suggestions.
2. Ask: "Call data-scout: have it put the number of files in the current folder into /tmp/test.md and return a status".
3. The collector's reply is one or two lines, and the number and the command that produced it are in `/tmp/test.md`.

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

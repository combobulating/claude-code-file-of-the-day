# A Claude Code rule that checks the result before it says done

Claude Code calls a task done only after it has looked at the result itself and tells you what it saw. A success message from a script no longer counts.

Claude Code rule · 2026-10-23 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-done-means-checked-rule) on combobulating.ai · [По-русски](ru/) · [Srpski](sr/) · [Português](pt/)

## How to make Claude stop saying "done" without checking

1. Ask Claude: "Add the contents of the downloaded file verified-done.md to the end of the file ~/.claude/CLAUDE.md, and if that file does not exist, create it".
2. Close Claude Code and open it again: the rules are read at startup.

Check:

1. Ask Claude: "Create a file hello.txt with the word hello in it".
2. The reply will have "done, checked:" and what Claude saw when it opened the file after writing it.

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

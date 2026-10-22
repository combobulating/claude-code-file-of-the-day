# A Claude Code rule that writes down an idea mid-work instead of starting on it

Claude Code writes an idea, mistake or task you mention mid-work as one line in plan.md and goes back to the work instead of starting on it.

Claude Code rule · 2026-10-22 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-note-for-later-rule) on combobulating.ai · [По-русски](ru/) · [Srpski](sr/) · [Português](pt/)

## How to stop losing ideas that come up on the go

1. Ask Claude: "Add the contents of the downloaded file note-for-later.md to the end of the file ~/.claude/CLAUDE.md, and if that file does not exist, create it".
2. Close Claude Code and open it again: the rules are read at startup.
3. In the middle of any work, say "note for later" and then the idea, mistake or task itself.

Check:

1. Ask Claude: "Note for later: add online booking to the website". Claude will reply in one line that it wrote it down, and won't start doing anything.
2. Ask Claude: "Show me the file plan.md". It will have a line with today's date, the word "idea" and your words.

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

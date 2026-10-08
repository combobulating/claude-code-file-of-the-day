# A Claude Code rule that turns three letters into a whole request

A rule for your CLAUDE.md: add jao, nch, awm or rbp to a request, and Claude only answers, changes nothing, sends a plan first or searches the web.

Claude Code rule · 2026-10-08 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-short-commands-rule) on combobulating.ai · [По-русски](ru/) · [Srpski](sr/) · [Português](pt/)

## How to add short commands: two or three letters instead of a whole request

1. Ask Claude: "Append the contents of the downloaded file short-commands.md to the end of the file ~/.claude/CLAUDE.md, and if there is no such file, create it".
2. Close Claude Code and open it again: the commands are read at startup.
3. You add your own abbreviation with the same kind of request. Ask Claude: "Add the line "stp - shorter and to the point" to the section "Short commands" of the file ~/.claude/CLAUDE.md".

Check:

1. Ask Claude: "Create the file menu.txt with the menu of my coffee shop jao". Claude does not create the file and only answers in words.
2. Ask Claude: "Create the file menu.txt with the menu of my coffee shop awm". Claude sends a plan and waits for your approval.

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

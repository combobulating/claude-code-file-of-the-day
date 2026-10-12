# A Claude Code rule that keeps work moving while you are away

Claude Code keeps working while you are away: it decides on its own instead of asking, then reports what was done and what was not.

Claude Code rule · 2026-10-12 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-work-without-me-rule) on combobulating.ai · [По-русски](ru/) · [Srpski](sr/) · [Português](pt/)

## How to keep work moving while you are away

1. Ask Claude: "Add the contents of the downloaded file work-without-me.md to the end of the file ~/.claude/CLAUDE.md, and if that file does not exist, create it".
2. Close Claude Code and open it again: the rules are read at startup.
3. When you leave, start your request with the words "work without me". The mode ends with your next message.

Check:

1. Ask Claude: "Work without me. Come up with a name for my coffee shop and write an opening announcement". Claude does not ask which name you like: it picks one itself, writes the announcement, and ends with a report with the parts "Done without you" and "Not done".
2. Send Claude any message without those words: the mode is off, and the reply has no two-part report.

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

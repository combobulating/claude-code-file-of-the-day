# A Claude Code rule that finds where the work will break before you hand it over

A rule for your global CLAUDE.md: at the end of every task and plan Claude imagines the work has failed and deals with the causes before the handover.

Claude Code rule · 2026-10-04 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-premortem-rule) on combobulating.ai · [По-русски](ru/) · [Srpski](sr/) · [Português](pt/)

## How to install the rule: find where the work will break, before handing it over

1. Ask Claude: "Append the contents of the downloaded file premortem.md to the end of the file ~/.claude/CLAUDE.md, and if that file does not exist, create it".
2. Close Claude Code and open it again: the rule is read at startup.

Check:

1. Ask Claude: "Make a plan for moving client bookings from a paper notebook into a Google Sheet".
2. At the end of the plan Claude writes a "What could go wrong" block: what it has already taken care of in the plan itself and what waits for your decision. Without the file there is no such block.

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

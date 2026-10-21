# A Claude Code rule that offers to put the work you keep giving it on a schedule

Claude Code spots the work you give it again and again, offers in one line to run it on a schedule, and on your yes sets it up and runs it once.

Claude Code rule · 2026-10-21 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-repeat-work-on-schedule-rule) on combobulating.ai · [По-русски](ru/) · [Srpski](sr/) · [Português](pt/)

## How Claude Code tells you which work is ready to run on a schedule without you

1. Ask Claude: "Append the contents of the downloaded file offer-a-schedule.md to the end of ~/.claude/CLAUDE.md, and if that file does not exist, create it".
2. Close Claude Code and open it again: rules are read at startup.

Check:

1. Ask Claude: "Look through the history of our past conversations: what work do I give you again and again, and which of it is worth putting on a schedule?" Claude Code names that work and what it will save you, or says there is nothing to schedule yet.
2. If you agree with the suggestion, reply "yes". Claude Code puts the work on a schedule by itself and runs it once right away so you see the result; if it asks permission to run a command, allow it.
3. From then on, when you give it a familiar task for the third time and it can be done without you, one line with a suggestion appears at the end of the reply.

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

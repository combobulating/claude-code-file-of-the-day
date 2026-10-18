# A Claude Code rule that shows you finished work instead of a path to a file

Claude Code prints short results in the reply and opens pages, images and spreadsheets on your screen itself, instead of giving you a path to a file.

Claude Code rule · 2026-10-18 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-show-finished-work-rule) on combobulating.ai · [По-русски](ru/) · [Srpski](sr/) · [Português](pt/)

## How to see finished work on your screen right away instead of hunting for a file

1. Ask Claude: "Append the contents of the downloaded file show-the-result.md to the end of ~/.claude/CLAUDE.md, and if that file does not exist, create it".
2. Close Claude Code and open it again: rules are read at startup.

Check:

1. Ask Claude: "Make a simple one-page business card for my business that I can open in a browser". If Claude Code asks permission to run the command that opens files, allow it. The page opens on your screen by itself, and the reply has no path to it.
2. Ask Claude: "Write three versions of a greeting for a new customer". The versions arrive right in the reply, with no separate file.

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

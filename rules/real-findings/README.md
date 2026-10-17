# A Claude Code rule that keeps only real findings in a review

Ask Claude Code to check a contract or a price list and the list keeps only what costs someone something, with who loses. An empty list is fine.

Claude Code rule · 2026-10-17 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-real-findings-rule) on combobulating.ai · [По-русски](ru/) · [Srpski](sr/) · [Português](pt/)

## How to keep only what is worth your time in a list of findings

1. Ask Claude: "Add the contents of the downloaded file real-findings.md to the end of the file ~/.claude/CLAUDE.md, and if that file does not exist, create it".
2. Close Claude Code and open it again: the rules are read at startup.

Check:

1. Ask Claude: "Find my latest contract, price list, or website text in the Downloads folder, review it, and give me a list of findings". The list has no "could be better" advice or remarks on taste, and under each item you can see who loses and what will change after the fix.
2. If there is nothing to fix in the file, Claude says so instead of making up items to fill the list.

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

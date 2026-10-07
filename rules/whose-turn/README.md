# A Claude Code rule that ends each answer with a mark showing whose turn it is

A rule for your global CLAUDE.md: every answer that hands work back to you ends with one mark, so you see at once whether Claude needs you.

Claude Code rule · 2026-10-07 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-whose-turn-mark-rule) on combobulating.ai · [По-русски](ru/) · [Srpski](sr/) · [Português](pt/)

## How to add the rule: a mark at the end of Claude's answer shows whose turn it is now

1. Ask Claude: "Append the contents of the downloaded file whose-turn.md to the end of the file ~/.claude/CLAUDE.md, and if there is no such file, create it".
2. Close Claude Code and open it again: the rule is read at startup.

Check:

1. Ask Claude: "Write a short notice that my coffee shop now opens at 8 a.m. and save it to notice.txt". The answer ends with the mark ✅: the work is done, nothing is needed from you.
2. Ask Claude: "Suggest two names for my new coffee shop, and I will decide which one to pick myself". The answer ends with the mark ✏️: your choice is needed next.
3. Without the file, there is no mark at the end of the answer.

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

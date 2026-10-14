# A Claude Code rule that tells you in a minute whether to take an order

Paste an order, a tender or an offer, and Claude Code answers bid now, not now or pass, with one reason and five scores.

Claude Code rule · 2026-10-14 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-bid-or-pass-rule) on combobulating.ai · [По-русски](ru/) · [Srpski](sr/) · [Português](pt/)

## How to know in a minute whether to take an order

1. Ask Claude: "Add the contents of the downloaded file bid-or-pass.md to the end of the file ~/.claude/CLAUDE.md, and if that file does not exist, create it".
2. Ask Claude: "In ~/.claude/CLAUDE.md, under the heading 'What I do' write: ..., and under the heading 'What I don't take on': ...". In place of the dots, describe your business in your own words.
3. Close Claude Code and open it again: the rules are read at startup.

Check:

1. Ask Claude: "Should I take this order?" and paste the text of an order, a tender, or an offer letter you got recently.
2. In the first line Claude writes "bid now", "not now", or "pass" with one sentence why, and below it a score for each of the five measures, if the order passed the first check.

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

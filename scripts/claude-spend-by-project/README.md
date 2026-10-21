# A Claude Code script that shows which work eats your money and limit

See which folders and conversations use up your Claude Code money or subscription limit, counted from the logs on your own computer.

Claude Code script · 2026-10-21 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-spend-by-project-script) on combobulating.ai · [По-русски](ru/) · [Srpski](sr/) · [Português](pt/)

## How to see which work eats your Claude Code money and limit

1. Ask Claude: "Put the downloaded file claude-spend-by-project.py in the folder ~/.claude/scripts, and if that folder does not exist, create it".
2. Ask Claude: "Run python3 ~/.claude/scripts/claude-spend-by-project.py. If there is a "No price" line at the bottom, open https://platform.claude.com/docs/en/about-claude/pricing, enter the prices of the models named there into PRICES in this file and run it again".

Check:

1. You will see a table: every folder where you worked with Claude Code, how many conversations it had, the amount and its share of the total. Below it are the five most expensive conversations with their first request.
2. The amount is counted at Anthropic token prices. On a subscription you do not pay it; it shows which work eats the most of your limit.
3. To see only the last week, ask Claude: "Run python3 ~/.claude/scripts/claude-spend-by-project.py 7".
4. Claude Code keeps conversation logs for 30 days, so the report does not see older work.

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

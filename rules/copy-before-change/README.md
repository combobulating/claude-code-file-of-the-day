# A Claude Code rule that saves a copy before every edit and deletes only on your word

Claude Code saves a copy before it changes your spreadsheets and documents, says how to get it back, and deletes only on your command, after asking again.

Claude Code rule · 2026-10-19 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-copy-before-change-rule) on combobulating.ai · [По-русски](ru/) · [Srpski](sr/) · [Português](pt/)

## How to make sure a Claude Code mistake doesn't cost you your data

1. Ask Claude: "Append the contents of the downloaded file copy-before-change.md to the end of ~/.claude/CLAUDE.md, and if that file does not exist, create it".
2. Close Claude Code and open it again: rules are read at startup.

Check:

1. Ask Claude: "Create a spreadsheet prices.csv with three products and their prices".
2. Close Claude Code and open it again, so that what follows is a new conversation.
3. Ask Claude: "Raise all prices in prices.csv by 10 percent". Before editing, Claude Code saves a copy and tells you how to ask for the old prices back.
4. Ask Claude: "Bring back the old prices". The spreadsheet goes back to how it was before the edit.
5. Ask Claude: "Delete the spreadsheet prices.csv". Claude Code first asks again what exactly to delete and deletes it only after your answer.

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

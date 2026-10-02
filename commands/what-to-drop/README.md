# A Claude Code command that finds one thing to stop each month

Once a month a Claude Code command reads your bank statement and names one thing to close, with the figure behind it. It cancels nothing by itself.

Claude Code command · 2026-10-02 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-monthly-what-to-drop-command) on combobulating.ai · [По-русски](ru/)

## How to install planned closing

1. Ask Claude: "Put the downloaded file what-to-drop.md into the folder ~/.claude/commands/, and if the folder does not exist, create it".
2. Restart Claude Code.
3. Save into the working folder a bank account or card statement for the last months or a table of your expenses.

Run:

1. Once a month write to Claude: /what-to-drop
2. If there is no statement in the folder, Claude asks for it in one line.

Check:

1. Write to Claude: /what-to-drop
2. Claude asks a few questions about the costs in the statement and brings one candidate for closing: what to close, what figure confirms it, what will be freed, who will be affected and how to bring it back. It cancels nothing by itself.

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

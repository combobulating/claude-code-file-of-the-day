# A Claude Code subagent that reads your text as the person it is for

A Claude Code subagent reads a letter, post or offer as the person it is addressed to before it goes out and splits its remarks into blocking and optional.

Claude Code subagent · 2026-09-28 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-picky-reader-subagent) on combobulating.ai · [По-русски](ru/)

## How to install the picky reader

1. Ask Claude: "Put the downloaded file picky-reader.md into the ~/.claude/agents/ folder, and if the folder does not exist, create it".
2. Ask Claude: "At the end of the file ~/.claude/agents/picky-reader.md, add a line: who my clients are and what matters most to them".
3. Ask Claude: "Write a rule into ~/.claude/CLAUDE.md: before sending any of my texts to people, call picky-reader and show me its report".
4. Restart Claude Code.

Check:

1. Ask Claude: "Call picky-reader: check the letter to a client 'Hello! The invoice is attached, it must be paid today by 18:00.' The letter has no attachment".
2. The first line of the report is the role, for example the client who received the letter.
3. The blocking list says that the letter promises an invoice that is not there.

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

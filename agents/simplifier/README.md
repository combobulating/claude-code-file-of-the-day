# A Claude Code subagent that rewrites an unclear answer in plain words

Write that you did not understand, and a Claude Code subagent rewrites the last answer shorter and simpler, with the same numbers, conclusions and questions.

Claude Code subagent · 2026-10-01 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-answer-simplifier-subagent) on combobulating.ai · [По-русски](ru/)

## How to install the answer simplifier

1. Ask Claude: "Put the downloaded file simplifier.md into the folder ~/.claude/agents/, and if there is no such folder, create it".
2. Ask Claude: "Write a rule into ~/.claude/CLAUDE.md: when I write that your answer is unclear or too long, call simplifier, pass it your last answer and my words word for word, and show me its text as it is".
3. Restart Claude Code.

Check:

1. Ask Claude: "Explain how a backup differs from file syncing".
2. Write: "I did not understand anything, too long".
3. Claude calls simplifier and shows the same answer shorter and simpler, with no new facts.

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

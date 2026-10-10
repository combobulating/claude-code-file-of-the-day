# A Claude Code rule that makes every question come with a ready decision

Decide in seconds: Claude Code suggests the best option with every question it asks, and one digit is enough.

Claude Code rule · 2026-10-10 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-questions-with-recommendation-rule) on combobulating.ai · [По-русски](ru/) · [Srpski](sr/) · [Português](pt/)

## How to make Claude give a ready decision with every question

1. Ask Claude: "Add the contents of the downloaded file questions-with-recommendation.md to the end of the file ~/.claude/CLAUDE.md, and if that file does not exist, create it".
2. Close Claude Code and open it again: the rules are read at startup.

Check:

1. Ask Claude: "Suggest a name for my coffee shop and ask me which option I like". The options come numbered, the recommended one is first, and next to it Claude says what it is based on.
2. Answer with a single digit, for example "2". Claude first repeats the second option word for word and only then continues the work.

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

# A Claude Code hook that skips permission questions while you are away

Leave Claude Code with a task and it no longer waits an hour at a permission question: the step that needs your yes is skipped, the rest gets done.

Claude Code hook · 2026-10-24 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-no-stops-while-away-hook) on combobulating.ai · [По-русски](ru/) · [Srpski](sr/) · [Português](pt/)

## How to keep a permission question from stopping work while you are away

1. Ask Claude: "Put the downloaded file deny-while-away.sh in the folder ~/.claude/hooks/ and make it executable."
2. Ask Claude: "Add ~/.claude/hooks/deny-while-away.sh to ~/.claude/settings.json as a PermissionRequest hook for all tools."
3. Close Claude Code and open it again: hooks are read at startup.
4. When you leave, start your request with the words "work without me". While that is your last message, any step Claude would ask permission for is skipped, and the rest of the work keeps going.
5. So that Claude can edit files without you, press Shift+Tab before you leave until "accept edits on" appears at the bottom. In this mode Claude also moves and deletes files in the working folder without asking.
6. Your next message brings back the usual permission questions. For Claude to ask about file edits again too, press Shift+Tab until "manual mode on" appears at the bottom.

Check:

1. Ask Claude: "Work without me. Run the command curl -sI https://claude.com and show the first line of the response."
2. There is no permission question: Claude writes that this step was skipped because there was no way to ask you.
3. Ask Claude the same thing without the words "work without me": the usual permission question appears; answer "No".

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

# A Claude Code hook that shows the start of every reply in a notification

When Claude Code finishes a reply, a notification with its first words pops up in the corner of the screen, so you can work in another window.

Claude Code hook · 2026-10-15 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-reply-notification-hook) on combobulating.ai · [По-русски](ru/) · [Srpski](sr/) · [Português](pt/)

## How to know Claude is done without sitting at the screen

1. Ask Claude: "Put the downloaded file notify-done.sh in the folder ~/.claude/hooks/ and make it executable."
2. Ask Claude: "Add ~/.claude/hooks/notify-done.sh to ~/.claude/settings.json as a Stop hook."
3. Ask Claude: "Check that jq is installed on this computer, and install it if it is not."
4. On a Mac, ask Claude: "Run the command osascript -e 'display notification "test"'."
5. Then open "System Settings", go to "Notifications", find "Script Editor" in the list and turn on "Allow Notifications".
6. If your computer is not a Mac, ask Claude: "In the file ~/.claude/hooks/notify-done.sh, replace osascript with my system's notification command."
7. Close Claude Code and open it again: hooks are read at startup.

Check:

1. Ask Claude: "Reply in one line: notifications work" and switch to another window right away.
2. A few seconds later, a "Claude Code" notification with the start of the reply pops up in the corner of the screen.

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

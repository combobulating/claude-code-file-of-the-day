# A Claude Code hook that tells you by sound whose move is next

A Claude Code Stop hook ends a reply with a short tone: a ringing one when the work is done, a lower one when your decision or action is needed.

Claude Code hook · 2026-09-29 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-sound-signal-hook) on combobulating.ai · [По-русски](ru/)

## How to install the sound signal

1. Ask Claude: "Put the downloaded file sound-signal.sh into the folder ~/.claude/hooks/ and make it executable".
2. Ask Claude: "Make two short sounds in the folder ~/.claude/sounds: done.wav from the system sound Glass and need.wav from the system sound Purr".
3. Ask Claude: "Connect ~/.claude/hooks/sound-signal.sh in ~/.claude/settings.json as a Stop hook".
4. Ask Claude: "Write a rule into ~/.claude/CLAUDE.md: when you hand over work, as the last action before the reply find the session number with the command echo $CLAUDE_CODE_SESSION_ID and write one word with the file writing tool into the file /tmp/claude_signal_<session number>: done if nothing is needed from me, or need if my decision, access or action is needed".
5. Ask Claude: "In ~/.claude/settings.json allow without confirmation writing to the files /tmp/claude_signal_* and /private/tmp/claude_signal_* and the command echo $CLAUDE_CODE_SESSION_ID, with the rules Edit(//tmp/claude_signal_*), Edit(//private/tmp/claude_signal_*) and Bash(echo $CLAUDE_CODE_SESSION_ID)".
6. Ask Claude: "Check that jq is on the computer, and if it is not, install it".
7. Ask Claude: "In the file ~/.claude/hooks/sound-signal.sh set my quiet hours: from 22 to 8".
8. If the computer is not a Mac, ask Claude: "In the file ~/.claude/hooks/sound-signal.sh replace afplay with the sound player of my system".
9. Restart Claude Code.

Check outside quiet hours:

1. Ask Claude: "Write the word need into the signal file of this session and reply with one line".
2. After the reply a low tone sounds.
3. Ask Claude the same with the word done.
4. After the reply a ringing tone sounds.

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

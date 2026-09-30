# A Claude Code hook that lets read-only commands run without asking

A PreToolUse hook that lets Claude Code run grep, cat, ls and git log without a permission prompt and leaves every other command to you. One script.

Claude Code hook · 2026-09-25 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-read-only-commands-hook) on combobulating.ai · [По-русски](ru/)

## How to install the "command only reads" check

The check splits a shell command into words and answers with code 0 only when every part of it only reads: `grep`, `cat`, `ls`, `git log` and similar ones from a closed list. Everything else, as well as any doubtful case, gets code 1. Below is how to install it as a hook: Claude Code will run read commands without asking for permission, the rest will go the usual way.

Where to put it:
```
mkdir -p ~/.claude/hooks
cp read_only.py ~/.claude/hooks/
```

What to fill in yourself: in `~/.claude/settings.json` add the hook below; if the file already has a `hooks` section, add only `PreToolUse` to it. The `jq` program is needed.
```
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r .tool_input.command | python3 ~/.claude/hooks/read_only.py && echo '{\"hookSpecificOutput\":{\"hookEventName\":\"PreToolUse\",\"permissionDecision\":\"allow\"}}' || true"
          }
        ]
      }
    ]
  }
}
```
Add your own read programs to the `READ_ONLY` list in the file, and git subcommands to `GIT_READ_ONLY`.

How to check that it works:
```
printf 'git log --oneline -3 | head -2' | python3 ~/.claude/hooks/read_only.py; echo $?
printf 'cat a.txt > b.txt' | python3 ~/.claude/hooks/read_only.py; echo $?
```
The first command prints 0, the second 1. Then open a new Claude Code session and ask it to show `git status`: the command will run without a permission question, and `git commit` will bring up the question.

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

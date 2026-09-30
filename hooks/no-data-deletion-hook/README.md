# A Claude Code hook that keeps the agent from wiping your database

A PreToolUse hook that stops Claude Code before it runs DROP TABLE, TRUNCATE or DELETE without WHERE. One script, a minute to install.

Claude Code hook · 2026-09-23 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-no-data-deletion-hook) on combobulating.ai · [По-русски](ru/)

## How to install the hook against data deletion

The hook fires before every command Claude runs in the terminal and blocks commands that destroy data in a database: DROP TABLE, TRUNCATE TABLE, DROP DATABASE, ALTER TABLE with DROP/RENAME/ALTER COLUMN and DELETE FROM without WHERE.

What you need: `jq` and `perl`. macOS already has perl, jq is installed with `brew install jq`. Without jq the hook blocks every terminal command.

Where to put it:
```
mkdir -p ~/.claude/hooks
cp no-data-deletion-hook.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/no-data-deletion-hook.sh
```

What to add to `~/.claude/settings.json` (if the `hooks` section already exists, add the block inside `PreToolUse`):

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          { "type": "command", "command": "$HOME/.claude/hooks/no-data-deletion-hook.sh" }
        ]
      }
    ]
  }
}
```

What to add yourself: a line in `~/.claude/CLAUDE.md` - "The CLAUDE_USER_APPROVED=1 prefix is added only after my direct permission in this conversation".

How to check that it works:
```
echo '{"tool_input":{"command":"psql -c \"DROP TABLE users\""}}' | ~/.claude/hooks/no-data-deletion-hook.sh
```

You will get a line with `"permissionDecision":"deny"`. Then, in a new Claude session, ask it to run `echo "DROP TABLE test"`: the command will not run, and Claude will show the reason for the block. The list of connected hooks is shown by the `/hooks` command.

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

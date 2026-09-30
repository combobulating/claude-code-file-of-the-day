#!/bin/bash
# PreToolUse hook: stops Claude from running a bash command that destroys data in a database.
# Blocks DROP TABLE, TRUNCATE TABLE, DROP DATABASE, destructive ALTER TABLE and DELETE FROM without WHERE.
# Allowed with the CLAUDE_USER_APPROVED=1 prefix in the command itself; DELETE FROM without WHERE never passes.

# Without jq the command cannot be read. The guard hook then never lets anything through silently:
# exit 2 blocks the call, and Claude sees the reason in stderr.
if ! command -v jq >/dev/null 2>&1; then
    echo "BLOCKED: the no-data-deletion hook needs jq (brew install jq)" >&2
    exit 2
fi

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

# Deny with a reason: the model gets permissionDecisionReason, understands why the command
# did not pass, and adjusts on its own.
hook_deny() {
    jq -cn --arg r "${1}" '{hookSpecificOutput:{hookEventName:"PreToolUse",permissionDecision:"deny",permissionDecisionReason:$r}}'
    exit 0
}

if [ -z "$COMMAND" ]; then
    exit 0
fi

# bash removes the "backslash + newline" pair when reading, while grep matches one
# physical line. So the check runs on two forms at once: joined and raw.
JOINED=$(printf '%s' "$COMMAND" | perl -0pe 's/\\\n//g')
[ -z "$JOINED" ] && JOINED=$COMMAND
COMMAND="$JOINED
$COMMAND"

approved() {
    echo "$COMMAND" | grep -q 'CLAUDE_USER_APPROVED=1'
}

# DROP TABLE / TRUNCATE TABLE
if echo "$COMMAND" | grep -qiE 'DROP\s+TABLE|TRUNCATE\s+TABLE'; then
    approved || hook_deny "BLOCKED: DROP TABLE/TRUNCATE are forbidden without CLAUDE_USER_APPROVED=1 (data loss)"
fi

# DROP DATABASE
if echo "$COMMAND" | grep -qiE 'DROP\s+DATABASE'; then
    approved || hook_deny "BLOCKED: DROP DATABASE is forbidden without CLAUDE_USER_APPROVED=1 (deletes the whole database)"
fi

# Destructive ALTER TABLE: DROP/RENAME/ALTER COLUMN. ADD COLUMN and ADD CONSTRAINT pass freely.
if echo "$COMMAND" | grep -qiE 'ALTER\s+TABLE'; then
    if echo "$COMMAND" | grep -qiE '\b(DROP\s+COLUMN|DROP\s+CONSTRAINT|RENAME\s+(TO|COLUMN)|ALTER\s+COLUMN)\b'; then
        approved || hook_deny "BLOCKED: destructive ALTER TABLE (DROP/RENAME/ALTER COLUMN) is forbidden without CLAUDE_USER_APPROVED=1. ADD COLUMN is allowed freely."
    fi
fi

# DELETE FROM without WHERE. Uses perl because grep on macOS cannot look ahead.
if echo "$COMMAND" | perl -ne 'BEGIN{$f=0} $f=1 if /DELETE\s+FROM(?!\s+.*WHERE)/i; END{exit !$f}'; then
    hook_deny "BLOCKED: DELETE FROM without WHERE is forbidden"
fi

exit 0

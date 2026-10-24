#!/bin/bash
# PermissionRequest hook: while you are away, Claude Code does not wait for your permission.
# If your last message starts with the words "work without me", the permission request
# is denied: the step is skipped and the work keeps going. At other times the permission prompt is as usual.
# Deny only through the decision object: exit code 2 is not honored for this event.
# Reference: https://code.claude.com/docs/en/hooks, section "PermissionRequest".

# --- input ---
INPUT=$(cat 2>/dev/null)
TRANSCRIPT=$(printf '%s' "$INPUT" | grep -o '"transcript_path" *: *"[^"]*"' | sed 's/.*: *"//; s/"$//; s/\\\\/\\/g')
[ -f "$TRANSCRIPT" ] || exit 0

# --- are you here? ---
LAST_PROMPT=$(grep -F '"origin":{"kind":"human"' "$TRANSCRIPT" | tail -n 1)
printf '%s' "$LAST_PROMPT" | grep -qE '"(content|text|prompt)":"(W|w)ork without me' || exit 0

# --- answer ---
printf '%s\n' '{"hookSpecificOutput":{"hookEventName":"PermissionRequest","decision":{"behavior":"deny","message":"There is no one to ask for permission: the last message starts with the words \"work without me\", and the person is unavailable until their next message. Do not do this step, do not repeat it and do not work around it another way. Finish the rest of the work in separate steps, and name the skipped step in your report."}}}'
exit 0

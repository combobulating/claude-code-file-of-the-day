#!/bin/bash
# Stop hook: when Claude Code finishes a reply, a Mac notification pops up
# with the start of that reply. The hook never stops Claude's work.
INPUT=$(cat)
# Leading dashes are dropped: a reply that starts with "-" would be read as an option of the notification command.
MSG=$(printf '%s' "$INPUT" | jq -r '(.last_assistant_message // "") | gsub("[*`#]"; "") | gsub("\\s+"; " ") | sub("^[ -]+"; "") | .[0:120]' 2>/dev/null)
[ -z "$MSG" ] && MSG="Work finished"
osascript - "$MSG" >/dev/null 2>&1 <<'EOF'
on run argv
display notification (item 1 of argv) with title "Claude Code" subtitle "Reply ready"
end run
EOF
exit 0

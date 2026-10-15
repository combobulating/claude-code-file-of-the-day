#!/bin/bash
# Stop hook: kada Claude Code završi odgovor, na Mac-u iskoči obaveštenje
# sa početkom tog odgovora. Hook nikada ne zaustavlja rad Claude-a.
INPUT=$(cat)
# Crtice na početku se uklanjaju: odgovor koji počinje sa „-“ komanda za obaveštenja bi pročitala kao svoju opciju.
MSG=$(printf '%s' "$INPUT" | jq -r '(.last_assistant_message // "") | gsub("[*`#]"; "") | gsub("\\s+"; " ") | sub("^[ -]+"; "") | .[0:120]' 2>/dev/null)
[ -z "$MSG" ] && MSG="Posao je završen"
osascript - "$MSG" >/dev/null 2>&1 <<'EOF'
on run argv
display notification (item 1 of argv) with title "Claude Code" subtitle "Odgovor je spreman"
end run
EOF
exit 0

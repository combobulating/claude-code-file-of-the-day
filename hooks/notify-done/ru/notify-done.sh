#!/bin/bash
# Stop-хук: когда Claude Code заканчивает ответ, на Mac всплывает уведомление
# с началом этого ответа. Хук никогда не останавливает работу Claude.
INPUT=$(cat)
# Тире в начале убираются: ответ, который начинается с «-», команда уведомления прочитала бы как свой параметр.
MSG=$(printf '%s' "$INPUT" | jq -r '(.last_assistant_message // "") | gsub("[*`#]"; "") | gsub("\\s+"; " ") | sub("^[ -]+"; "") | .[0:120]' 2>/dev/null)
[ -z "$MSG" ] && MSG="Работа закончена"
osascript - "$MSG" >/dev/null 2>&1 <<'EOF'
on run argv
display notification (item 1 of argv) with title "Claude Code" subtitle "Ответ готов"
end run
EOF
exit 0

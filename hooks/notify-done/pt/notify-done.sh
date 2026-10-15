#!/bin/bash
# Hook de Stop: quando o Claude Code termina uma resposta, aparece uma notificação no Mac
# com o começo dessa resposta. O hook nunca interrompe o trabalho do Claude.
INPUT=$(cat)
# Os traços do início são removidos: uma resposta que começa com “-” seria lida como uma opção do comando de notificação.
MSG=$(printf '%s' "$INPUT" | jq -r '(.last_assistant_message // "") | gsub("[*`#]"; "") | gsub("\\s+"; " ") | sub("^[ -]+"; "") | .[0:120]' 2>/dev/null)
[ -z "$MSG" ] && MSG="Trabalho concluído"
osascript - "$MSG" >/dev/null 2>&1 <<'EOF'
on run argv
display notification (item 1 of argv) with title "Claude Code" subtitle "Resposta pronta"
end run
EOF
exit 0

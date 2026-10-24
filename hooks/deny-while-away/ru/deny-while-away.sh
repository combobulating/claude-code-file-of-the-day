#!/bin/bash
# Хук PermissionRequest: пока вас нет, Claude Code не ждёт вашего разрешения.
# Если ваше последнее сообщение начинается со слов «работай без меня», запрос разрешения
# отклоняется: шаг пропускается, а работа идёт дальше. В остальное время запрос разрешения как обычно.
# Отклонять только через объект decision: код выхода 2 для этого события не учитывается.
# Справка: https://code.claude.com/docs/en/hooks, раздел «PermissionRequest».

# --- вход ---
INPUT=$(cat 2>/dev/null)
TRANSCRIPT=$(printf '%s' "$INPUT" | grep -o '"transcript_path" *: *"[^"]*"' | sed 's/.*: *"//; s/"$//; s/\\\\/\\/g')
[ -f "$TRANSCRIPT" ] || exit 0

# --- вы здесь? ---
LAST_PROMPT=$(grep -F '"origin":{"kind":"human"' "$TRANSCRIPT" | tail -n 1)
printf '%s' "$LAST_PROMPT" | grep -qE '"(content|text|prompt)":"(Р|р)аботай без меня' || exit 0

# --- ответ ---
printf '%s\n' '{"hookSpecificOutput":{"hookEventName":"PermissionRequest","decision":{"behavior":"deny","message":"Некого спросить о разрешении: последнее сообщение начинается со слов «работай без меня», и человек недоступен до своего следующего сообщения. Не делай этот шаг, не повторяй его и не обходи его другим способом. Доделай остальную работу отдельными шагами, а пропущенный шаг назови в отчёте."}}}'
exit 0

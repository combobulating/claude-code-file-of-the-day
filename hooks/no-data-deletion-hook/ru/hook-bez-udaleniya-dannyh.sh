#!/bin/bash
# PreToolUse hook: не даёт Claude выполнить в bash команду, которая уничтожает данные в базе.
# Отбивает DROP TABLE, TRUNCATE TABLE, DROP DATABASE, разрушающий ALTER TABLE и DELETE FROM без WHERE.
# Пропуск с префиксом CLAUDE_USER_APPROVED=1 в самой команде; DELETE FROM без WHERE не проходит никогда.

# Без jq команду не прочитать. Защитный хук тогда не пропускает ничего молча:
# exit 2 отбивает вызов, и Claude видит причину в stderr.
if ! command -v jq >/dev/null 2>&1; then
    echo "BLOCKED: хуку против удаления данных нужен jq (brew install jq)" >&2
    exit 2
fi

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

# Отказ с причиной: модель получает permissionDecisionReason, понимает, почему команда
# не прошла, и перестраивается сама.
hook_deny() {
    jq -cn --arg r "${1}" '{hookSpecificOutput:{hookEventName:"PreToolUse",permissionDecision:"deny",permissionDecisionReason:$r}}'
    exit 0
}

if [ -z "$COMMAND" ]; then
    exit 0
fi

# bash убирает пару «обратная косая + перевод строки» при чтении, а grep сверяет одну
# физическую строку. Поэтому сверка идёт по двум видам сразу: склеенному и сырому.
SKLEENO=$(printf '%s' "$COMMAND" | perl -0pe 's/\\\n//g')
[ -z "$SKLEENO" ] && SKLEENO=$COMMAND
COMMAND="$SKLEENO
$COMMAND"

approved() {
    echo "$COMMAND" | grep -q 'CLAUDE_USER_APPROVED=1'
}

# DROP TABLE / TRUNCATE TABLE
if echo "$COMMAND" | grep -qiE 'DROP\s+TABLE|TRUNCATE\s+TABLE'; then
    approved || hook_deny "BLOCKED: DROP TABLE/TRUNCATE запрещены без CLAUDE_USER_APPROVED=1 (потеря данных)"
fi

# DROP DATABASE
if echo "$COMMAND" | grep -qiE 'DROP\s+DATABASE'; then
    approved || hook_deny "BLOCKED: DROP DATABASE запрещён без CLAUDE_USER_APPROVED=1 (удаление базы целиком)"
fi

# Разрушающий ALTER TABLE: DROP/RENAME/ALTER COLUMN. ADD COLUMN и ADD CONSTRAINT проходят свободно.
if echo "$COMMAND" | grep -qiE 'ALTER\s+TABLE'; then
    if echo "$COMMAND" | grep -qiE '\b(DROP\s+COLUMN|DROP\s+CONSTRAINT|RENAME\s+(TO|COLUMN)|ALTER\s+COLUMN)\b'; then
        approved || hook_deny "BLOCKED: разрушающие ALTER TABLE (DROP/RENAME/ALTER COLUMN) запрещены без CLAUDE_USER_APPROVED=1. ADD COLUMN - разрешено свободно."
    fi
fi

# DELETE FROM без WHERE. Через perl, потому что grep на macOS не умеет заглядывать вперёд.
if echo "$COMMAND" | perl -ne 'BEGIN{$f=0} $f=1 if /DELETE\s+FROM(?!\s+.*WHERE)/i; END{exit !$f}'; then
    hook_deny "BLOCKED: DELETE FROM без WHERE запрещён"
fi

exit 0

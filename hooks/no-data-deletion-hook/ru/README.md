# Хук для Claude Code, который не даст агенту стереть базу данных

PreToolUse-хук, который останавливает Claude Code перед DROP TABLE, TRUNCATE и DELETE без WHERE. Один скрипт, ставится за минуту.

2026-09-23 · Слава Сажин  
[Статья целиком](https://combobulating.ai/ru/blog/claude-code-no-data-deletion-hook) на combobulating.ai · [English](../)

## Как поставить хук против удаления данных

Хук срабатывает перед каждой командой, которую Claude запускает в терминале, и не пускает команды, уничтожающие данные в базе: DROP TABLE, TRUNCATE TABLE, DROP DATABASE, ALTER TABLE с DROP/RENAME/ALTER COLUMN и DELETE FROM без WHERE.

Что нужно: `jq` и `perl`. На macOS perl уже есть, jq ставится через `brew install jq`. Без jq хук отбивает любую команду в терминале.

Куда положить:
```
mkdir -p ~/.claude/hooks
cp hook-bez-udaleniya-dannyh.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/hook-bez-udaleniya-dannyh.sh
```

Что вписать в `~/.claude/settings.json` (если раздел `hooks` уже есть, добавьте блок внутрь `PreToolUse`):

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          { "type": "command", "command": "$HOME/.claude/hooks/hook-bez-udaleniya-dannyh.sh" }
        ]
      }
    ]
  }
}
```

Что вписать своё: строку в `~/.claude/CLAUDE.md` - «Префикс CLAUDE_USER_APPROVED=1 ставится только после моего прямого разрешения в этом разговоре».

Как убедиться, что заработало:
```
echo '{"tool_input":{"command":"psql -c \"DROP TABLE users\""}}' | ~/.claude/hooks/hook-bez-udaleniya-dannyh.sh
```

В ответ придёт строка с `"permissionDecision":"deny"`. Потом в новой сессии Claude попросите выполнить `echo "DROP TABLE test"`: команда не пойдёт, Claude покажет причину отказа. Список подключённых хуков виден командой `/hooks`.

---

Из рубрики «Файл дня» на [combobulating.ai](https://combobulating.ai/ru/blog).

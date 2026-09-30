# Хук для Claude Code, который пропускает команды чтения без вопроса

PreToolUse-хук, который даёт Claude Code запускать grep, cat, ls и git log без вопроса о разрешении, а остальные команды оставляет вам. Один скрипт.

2026-09-25 · Слава Сажин  
[Статья целиком](https://combobulating.ai/ru/blog/claude-code-read-only-commands-hook) на combobulating.ai · [English](../)

## Как поставить проверку «команда только читает»

Проверка разбирает команду оболочки по словам и отвечает кодом 0 лишь тогда, когда каждая её часть только читает: `grep`, `cat`, `ls`, `git log` и подобные из закрытого списка. Всё остальное, как и любой сомнительный случай, получает код 1. Ниже показано, как поставить её хуком: команды чтения Claude Code будет запускать без вопроса о разрешении, остальные пойдут обычным порядком.

Куда положить:
```
mkdir -p ~/.claude/hooks
cp tolko_chtenie.py ~/.claude/hooks/
```

Что вписать у себя: в `~/.claude/settings.json` добавьте хук ниже; если раздел `hooks` в файле уже есть, допишите в него только `PreToolUse`. Нужна программа `jq`.
```
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r .tool_input.command | python3 ~/.claude/hooks/tolko_chtenie.py && echo '{\"hookSpecificOutput\":{\"hookEventName\":\"PreToolUse\",\"permissionDecision\":\"allow\"}}' || true"
          }
        ]
      }
    ]
  }
}
```
Свои программы для чтения допишите в список `CHTENIE` в файле, а подкоманды git - в `GIT_CHTENIE`.

Как проверить, что всё работает:
```
printf 'git log --oneline -3 | head -2' | python3 ~/.claude/hooks/tolko_chtenie.py; echo $?
printf 'cat a.txt > b.txt' | python3 ~/.claude/hooks/tolko_chtenie.py; echo $?
```
Первая команда печатает 0, вторая - 1. Потом откройте новую сессию Claude Code и попросите показать `git status`: команда пройдёт без вопроса о разрешении, а на `git commit` вопрос появится.

---

Из рубрики «Файл дня» на [combobulating.ai](https://combobulating.ai/ru/blog).

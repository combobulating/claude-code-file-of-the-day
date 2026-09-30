# Команда для Claude Code, которая отбирает для вас новинки недели

Раз в неделю команда для Claude Code разбирает новинки Claude Code, сверяет их с вашей работой и оставляет только подходящие советы с готовой просьбой.

2026-09-30 · Слава Сажин  
[Статья целиком](https://combobulating.ai/ru/blog/claude-code-weekly-news-advice) на combobulating.ai · [English](../)

## Как настроить новости Claude Code раз в неделю

1. Положите `novosti-claude-code.md` в папку `~/.claude/commands/`.
2. Попросите Claude: «Создай папку $HOME/claude-news».
3. Попросите Claude: «Поставь запуск каждый понедельник в 9:00 командой cd $HOME && claude -p '/novosti-claude-code' --add-dir $HOME/claude-news --allowedTools "WebSearch,WebFetch(domain:code.claude.com),WebFetch(domain:www.anthropic.com),Bash(claude --version),Edit(~/claude-news/**)"».
4. Попросите Claude: «Запусти эту задачу один раз через сам планировщик и проверь, что в папке $HOME/claude-news появился отчёт. Если запуск пишет, что вход не выполнен, помоги мне выполнить claude setup-token и добавь полученный ключ в запуск как CLAUDE_CODE_OAUTH_TOKEN».
5. В понедельник утром компьютер должен быть включён и не находиться в спящем режиме.
6. Чтобы прочитать свежий отчёт, попросите Claude: «Покажи последний отчёт из папки $HOME/claude-news».

Проверка:

1. Запустите в Claude Code `/novosti-claude-code`.
2. Claude ищет новости в интернете и печатает в чат отчёт «НОВОСТИ CLAUDE CODE»: абзац о главном за неделю и советы с просьбами «Попросите Claude: ...».
3. В папке `$HOME/claude-news` появляется файл отчёта с сегодняшней датой.
4. Запустите `/novosti-claude-code` ещё раз: Claude показывает тот же отчёт и новый поиск не начинает.

---

Из рубрики «Файл дня» на [combobulating.ai](https://combobulating.ai/ru/blog).

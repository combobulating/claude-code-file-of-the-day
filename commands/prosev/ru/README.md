# Команда для Claude Code, которая каждую ночь просеивает заметки в базу знаний

Команда для Claude Code ночью читает заметки за последние сутки и дописывает в базу знаний то, что пригодится через три месяца. Ничего не удаляет.

2026-09-27 · Слава Сажин  
[Статья целиком](https://combobulating.ai/ru/blog/claude-code-nightly-notes-to-knowledge-base) на combobulating.ai · [English](../)

## Как поставить ночной просев заметок

1. Положите `prosev.md` в папку `~/.claude/commands/`.
2. Попросите Claude: «Создай папки $HOME/notes и $HOME/knowledge».
3. Попросите Claude: «В конце каждой рабочей задачи коротко записывай узнанное в заметку в папке $HOME/notes».
4. Попросите Claude: «Поставь ежедневный запуск в 3:00 командой claude -p '/prosev' --permission-mode acceptEdits --add-dir $HOME/notes --add-dir $HOME/knowledge».
5. На ночь оставляйте компьютер включённым и не переводите его в режим сна.

Проверка:

1. Положите в папку `$HOME/notes` файл с одной строкой: «Отчёт для бухгалтерии собирается командой report --month».
2. Запустите в Claude Code `/prosev`.
3. Claude отвечает «Всё в порядке, всё сделано.», а в папке `$HOME/knowledge` появляется эта строка.
4. Запустите `/prosev` ещё раз: строка второй раз не дописывается.

---

Из рубрики «Файл дня» на [combobulating.ai](https://combobulating.ai/ru/blog).

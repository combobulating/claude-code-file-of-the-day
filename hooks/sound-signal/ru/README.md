# Хук для Claude Code, который звуком говорит, чей следующий ход

Stop-хук для Claude Code заканчивает ответ коротким тоном: звонким, когда работа сделана, и ниже, когда нужны ваше решение или действие.

2026-09-29 · Слава Сажин  
[Статья целиком](https://combobulating.ai/ru/blog/claude-code-sound-signal-hook) на combobulating.ai · [English](../)

## Как поставить звуковой сигнал

1. Попросите Claude: «Положи скачанный файл zvukovoy-signal.sh в папку ~/.claude/hooks/ и сделай его исполняемым».
2. Попросите Claude: «Сделай в папке ~/.claude/sounds два коротких звука: done.wav из системного звука Glass и need.wav из системного звука Purr».
3. Попросите Claude: «Подключи ~/.claude/hooks/zvukovoy-signal.sh в ~/.claude/settings.json как хук Stop».
4. Попросите Claude: «Запиши в ~/.claude/CLAUDE.md правило: когда сдаёшь работу, последним действием перед ответом узнай номер сессии командой echo $CLAUDE_CODE_SESSION_ID и запиши инструментом записи файлов одно слово в файл /tmp/claude_signal_<номер сессии>: done, если от меня ничего не нужно, или need, если нужны моё решение, доступ или действие».
5. Попросите Claude: «Разреши в ~/.claude/settings.json без подтверждения запись в файлы /tmp/claude_signal_* и /private/tmp/claude_signal_* и команду echo $CLAUDE_CODE_SESSION_ID правилами Edit(//tmp/claude_signal_*), Edit(//private/tmp/claude_signal_*) и Bash(echo $CLAUDE_CODE_SESSION_ID)».
6. Попросите Claude: «Проверь, что на компьютере есть jq, а если нет, поставь его».
7. Попросите Claude: «В файле ~/.claude/hooks/zvukovoy-signal.sh поставь мои часы тишины: с 22 до 8».
8. Если компьютер не Mac, попросите Claude: «В файле ~/.claude/hooks/zvukovoy-signal.sh замени afplay на проигрыватель звука моей системы».
9. Перезапустите Claude Code.

Проверка вне часов тишины:

1. Попросите Claude: «Запиши слово need в файл сигнала этой сессии и ответь одной строкой».
2. После ответа звучит низкий тон.
3. Попросите Claude то же самое со словом done.
4. После ответа звучит звонкий тон.

---

Из рубрики «Файл дня» на [combobulating.ai](https://combobulating.ai/ru/blog).

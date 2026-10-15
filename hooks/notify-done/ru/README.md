# Хук для Claude Code, который показывает начало каждого ответа в уведомлении

Когда Claude Code заканчивает ответ, в углу экрана всплывает уведомление с его первыми словами, и можно спокойно работать в другом окне.

2026-10-15 · Слава Сажин  
[Статья целиком](https://combobulating.ai/ru/blog/claude-code-reply-notification-hook) на combobulating.ai · [English](../)

## Как узнать, что Claude закончил, не сидя у экрана

1. Попросите Claude: «Положи скачанный файл notify-done.sh в папку ~/.claude/hooks/ и сделай его исполняемым».
2. Попросите Claude: «Добавь ~/.claude/hooks/notify-done.sh в ~/.claude/settings.json как Stop-хук».
3. Попросите Claude: «Проверь, что на этом компьютере установлен jq, и установи его, если нет».
4. На Mac попросите Claude: «Выполни команду osascript -e 'display notification "test"'».
5. Потом откройте «Системные настройки» (System Settings), перейдите в «Уведомления» (Notifications), найдите в списке «Редактор скриптов» (Script Editor) и включите «Разрешить уведомления» (Allow Notifications).
6. Если у вас не Mac, попросите Claude: «В файле ~/.claude/hooks/notify-done.sh замени osascript на команду уведомлений моей системы».
7. Закройте Claude Code и откройте снова: хуки читаются при запуске.

Проверка:

1. Попросите Claude: «Ответь одной строкой: уведомления работают» и сразу переключитесь в другое окно.
2. Через несколько секунд в углу экрана всплывёт уведомление «Claude Code» с началом ответа.

---

Из рубрики «Файл дня» на [combobulating.ai](https://combobulating.ai/ru/blog).

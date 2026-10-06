# Claude Code file of the day

Hooks, subagents, slash commands and `CLAUDE.md` rules for [Claude Code](https://code.claude.com/docs),
one ready-to-install file at a time. Each folder holds the file, where to put it, what to add to
`settings.json`, and a command that proves it works.

Published by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents: an always-on machine with Claude Code installed and kept up to
date for 2.99 EUR a month ([seven Claude Code machines compared, 22 September
2026](https://combobulating.ai/en/blog/claude-code-vps-hosting-compared)).

## The files

| Date | Kind | File | What it does | Write-up |
|---|---|---|---|---|
| 2026-10-06 | rule | [task-log.md](rules/task-log/) | keeps a task log so a new conversation continues where you stopped | [article](https://combobulating.ai/en/blog/claude-code-task-log-rule) |
| 2026-10-05 | rule | [urgency.md](rules/urgency/) | marks every task and problem by urgency | [article](https://combobulating.ai/en/blog/claude-code-urgency-marks-rule) |
| 2026-10-04 | rule | [premortem.md](rules/premortem/) | finds where the work will break before you hand it over | [article](https://combobulating.ai/en/blog/claude-code-premortem-rule) |
| 2026-10-03 | command | [business-ideas.md](commands/business-ideas/) | finds a business abroad you can repeat at home | [article](https://combobulating.ai/en/blog/claude-code-business-from-abroad-command) |
| 2026-10-02 | command | [what-to-drop.md](commands/what-to-drop/) | finds one thing to stop each month | [article](https://combobulating.ai/en/blog/claude-code-monthly-what-to-drop-command) |
| 2026-10-01 | subagent | [simplifier.md](agents/simplifier/) | rewrites an unclear answer in plain words | [article](https://combobulating.ai/en/blog/claude-code-answer-simplifier-subagent) |
| 2026-09-30 | command | [claude-code-news.md](commands/claude-code-news/) | picks the new features of the week for you | [article](https://combobulating.ai/en/blog/claude-code-weekly-news-advice) |
| 2026-09-29 | hook | [sound-signal.sh](hooks/sound-signal/) | tells you by sound whose move is next | [article](https://combobulating.ai/en/blog/claude-code-sound-signal-hook) |
| 2026-09-28 | subagent | [picky-reader.md](agents/picky-reader/) | reads your text as the person it is for | [article](https://combobulating.ai/en/blog/claude-code-picky-reader-subagent) |
| 2026-09-27 | command | [prosev.md](commands/prosev/) | sifts your notes into a knowledge base every night | [article](https://combobulating.ai/en/blog/claude-code-nightly-notes-to-knowledge-base) |
| 2026-09-26 | subagent | [data-scout.md](agents/data-scout/) | collects data and leaves the conclusions to you | [article](https://combobulating.ai/en/blog/claude-code-data-collection-subagent) |
| 2026-09-25 | hook | [read_only.py](hooks/read-only/) | lets read-only commands run without asking | [article](https://combobulating.ai/en/blog/claude-code-read-only-commands-hook) |
| 2026-09-24 | subagent | [agent-code-scout.md](agents/agent-code-scout/) | finds code without eating your context | [article](https://combobulating.ai/en/blog/claude-code-subagent-code-search) |
| 2026-09-23 | hook | [no-data-deletion-hook.sh](hooks/no-data-deletion-hook/) | keeps the agent from wiping your database | [article](https://combobulating.ai/en/blog/claude-code-no-data-deletion-hook) |

Every file is also in Russian, in the `ru/` folder beside it, and since 4 October 2026 in Serbian
(`sr/`) and Portuguese (`pt/`) too. Все файлы есть и на русском: папка `ru/` рядом с английской
версией.

## Where they go

| Kind | Folder | Turned on by |
|---|---|---|
| hook | `~/.claude/hooks/` | a block in `~/.claude/settings.json`, shown in the file's README |
| subagent | `~/.claude/agents/` | nothing: Claude Code picks it up in the next session |
| command | `~/.claude/commands/` | nothing: type `/` and its name |
| rule | `~/.claude/CLAUDE.md` (append it) | restarting Claude Code: the file is read at startup |

Put a file in the project's own `.claude/` instead of `~/.claude/` to have it in one project only.

## Keep them running when the laptop is closed

A hook guards a session only while there is a session, and a command that sifts your notes every
night needs a machine that is on every night. [combobulating](https://combobulating.ai/en) rents a
Linux machine with Claude Code installed, a browser terminal, a mailbox and Telegram for the
agent, so it keeps working when you are not. The Mini is 2.99 EUR a month; Claude itself stays
on your own Anthropic subscription or API account. [Prices and plans](https://combobulating.ai/en/pricing).

A new file most days: star or watch the repo to get the next one.

## License

MIT: copy them, change them, ship them. See [LICENSE](LICENSE).

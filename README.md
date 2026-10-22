# Claude Code file of the day

Hooks, subagents, slash commands, `CLAUDE.md` rules and scripts for [Claude Code](https://code.claude.com/docs),
one ready-to-install file at a time. Each folder holds the file, where to put it, what to add to
`settings.json`, and a command that proves it works.

Published by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents: an always-on machine with Claude Code installed and kept up to
date for 2.99 EUR a month ([seven Claude Code machines compared, 22 September
2026](https://combobulating.ai/en/blog/claude-code-vps-hosting-compared)).

## The files

| Date | Kind | File | What it does | Write-up |
|---|---|---|---|---|
| 2026-10-22 | rule | [note-for-later.md](rules/note-for-later/) | writes down an idea mid-work instead of starting on it | [article](https://combobulating.ai/en/blog/claude-code-note-for-later-rule) |
| 2026-10-21 | script | [claude-spend-by-project.py](scripts/claude-spend-by-project/) | shows which work eats your money and limit | [article](https://combobulating.ai/en/blog/claude-code-spend-by-project-script) |
| 2026-10-21 | rule | [offer-a-schedule.md](rules/offer-a-schedule/) | offers to put the work you keep giving it on a schedule | [article](https://combobulating.ai/en/blog/claude-code-repeat-work-on-schedule-rule) |
| 2026-10-19 | rule | [copy-before-change.md](rules/copy-before-change/) | saves a copy before every edit and deletes only on your word | [article](https://combobulating.ai/en/blog/claude-code-copy-before-change-rule) |
| 2026-10-18 | rule | [show-the-result.md](rules/show-the-result/) | shows you finished work instead of a path to a file | [article](https://combobulating.ai/en/blog/claude-code-show-finished-work-rule) |
| 2026-10-17 | rule | [real-findings.md](rules/real-findings/) | keeps only real findings in a review | [article](https://combobulating.ai/en/blog/claude-code-real-findings-rule) |
| 2026-10-16 | command | [competitors.md](commands/competitors/) | brings three to five signals about your competitors every week | [article](https://combobulating.ai/en/blog/claude-code-competitor-signals-command) |
| 2026-10-15 | hook | [notify-done.sh](hooks/notify-done/) | shows the start of every reply in a notification | [article](https://combobulating.ai/en/blog/claude-code-reply-notification-hook) |
| 2026-10-14 | rule | [bid-or-pass.md](rules/bid-or-pass/) | tells you in a minute whether to take an order | [article](https://combobulating.ai/en/blog/claude-code-bid-or-pass-rule) |
| 2026-10-13 | rule | [worst-case-preview.md](rules/worst-case-preview/) | shows where a page breaks before your customers see it | [article](https://combobulating.ai/en/blog/claude-code-worst-case-preview-rule) |
| 2026-10-12 | rule | [work-without-me.md](rules/work-without-me/) | keeps work moving while you are away | [article](https://combobulating.ai/en/blog/claude-code-work-without-me-rule) |
| 2026-10-11 | command | [idea.md](commands/idea/) | brings one growth idea for your business at a time | [article](https://combobulating.ai/en/blog/claude-code-one-growth-idea-command) |
| 2026-10-10 | rule | [questions-with-recommendation.md](rules/questions-with-recommendation/) | makes every question come with a ready decision | [article](https://combobulating.ai/en/blog/claude-code-questions-with-recommendation-rule) |
| 2026-10-09 | script | [find_secrets.py](scripts/find-secrets/) | finds passwords left in plain text in your files | [article](https://combobulating.ai/en/blog/claude-code-plain-text-passwords-script) |
| 2026-10-08 | rule | [short-commands.md](rules/short-commands/) | turns three letters into a whole request | [article](https://combobulating.ai/en/blog/claude-code-short-commands-rule) |
| 2026-10-07 | rule | [whose-turn.md](rules/whose-turn/) | ends each answer with a mark showing whose turn it is | [article](https://combobulating.ai/en/blog/claude-code-whose-turn-mark-rule) |
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
| script | `~/.claude/scripts/` | nothing: ask Claude to run it, the README has the request |

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

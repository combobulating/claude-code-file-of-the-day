# A Claude Code command that picks the new features of the week for you

Once a week a Claude Code command reads what is new in Claude Code, checks it against how you work and keeps only the advice that fits, with a ready request.

Claude Code command · 2026-09-30 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-weekly-news-advice) on combobulating.ai · [По-русски](ru/)

## How to set up Claude Code news once a week

1. Put `claude-code-news.md` into the folder `~/.claude/commands/`.
2. Ask Claude: "Create the folder $HOME/claude-news".
3. Ask Claude: "Schedule a run every Monday at 9:00 with the command cd $HOME && claude -p '/claude-code-news' --add-dir $HOME/claude-news --allowedTools "WebSearch,WebFetch(domain:code.claude.com),WebFetch(domain:www.anthropic.com),Bash(claude --version),Edit(~/claude-news/**)"".
4. Ask Claude: "Run this task once through the scheduler itself and check that a report appeared in the folder $HOME/claude-news. If the run says you are not logged in, help me run claude setup-token and add the resulting key to the run as CLAUDE_CODE_OAUTH_TOKEN".
5. On Monday morning the computer must be on and not asleep.
6. To read the fresh report, ask Claude: "Show the latest report from the folder $HOME/claude-news".

Check:

1. Run `/claude-code-news` in Claude Code.
2. Claude searches for news on the internet and prints the report "CLAUDE CODE NEWS" in the chat: a paragraph about the main things of the week and advice with requests "Ask Claude: ...".
3. A report file with today's date appears in the folder `$HOME/claude-news`.
4. Run `/claude-code-news` again: Claude shows the same report and does not start a new search.

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

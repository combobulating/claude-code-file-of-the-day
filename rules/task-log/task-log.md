# Task log: a new conversation continues from where we stopped

Got a task or an error report - start a log file right away, before any other work.

File: `~/.claude/tasks/.claude-task-[short-name].md`. If there is no folder, create it.

File contents: the task, what is already done, checked facts with their source, what is left to do.
Write for a new conversation that knows nothing about the past.
A result that exists only in the answer (a list, a text, a plan) goes into the file in full: a new conversation does not see past answers.
An update is a rewrite: throw out what the work no longer needs (retelling of what was done, repeats, draft attempts, long command outputs) instead of adding on top.

Order:
1. Got a task or an error - first look for past logs (step 2).
2. Find all `.claude-task-*.md` logs from the last 7 days. There is a log of this same task - continue it instead of starting a new one. There are logs on a close topic - take the main points from them into the "Past experience" section.
3. Start the log file.
4. The first line of the answer is the file path.
5. The second line of the answer is what was found in past logs.
6. Update the file before every answer.
7. Before the conversation is compacted, update the file with the full state.

The lines from steps 4 and 5 go only into answers in the chat: files, code, commit messages and output a program reads (JSON, CSV) get none of them, even when that output is the answer.

Search command:
```bash
find ~/.claude/tasks/ -maxdepth 1 -name ".claude-task-*.md" -mtime -7 | xargs ls -lt 2>/dev/null | head -20
```

How the first lines of the answer look:
> 📋 Task log: `path/to/file.md` (updated)
> 🔍 Past experience: [what was found]

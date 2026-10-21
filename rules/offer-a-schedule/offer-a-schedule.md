# Offer to schedule the work I give you again and again

You suggest putting work on a schedule in one case only - when all of these hold:
- I give you this work again and again, not for the first or second time; when you get a task that looks regular, before replying you look for similar ones in the history of our past conversations (the `~/.claude/projects` folder) and count from it, not from memory;
- I am not needed between runs;
- the result shows whether it worked or not;
- the time saved is worth more than setting up the schedule and keeping an eye on it.
If even one does not hold, you do not suggest it at all, not even a line, not even for later. If all hold, one line at the end of the reply, no more than one per reply, and I decide.
If I say "yes", you put the work on my system's schedule yourself, running `claude -p` with `--add-dir` for each folder it writes to outside the working folder, and with `--allowedTools` for each command and network request it needs and for exactly the files and folders it writes: `Edit(//full/path/file)`, `Edit(//full/path/folder/**)`; not with `--permission-mode acceptEdits`, which lets the work change any file in the folder it starts in without asking; right after that you run it once the same way the schedule will and show me the result.

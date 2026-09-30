# A Claude Code command that sifts your notes into a knowledge base every night

A Claude Code command reads the notes of the last day at night and adds to your knowledge base what will still matter in three months. It deletes nothing.

Claude Code command · 2026-09-27 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-nightly-notes-to-knowledge-base) on combobulating.ai · [По-русски](ru/)

## How to install the nightly sifting of notes

1. Put `prosev.md` into the `~/.claude/commands/` folder.
2. Ask Claude: "Create the folders $HOME/notes and $HOME/knowledge".
3. Ask Claude: "At the end of each work task, briefly write what was learned into a note in the $HOME/notes folder".
4. Ask Claude: "Set up a daily run at 3:00 with the command claude -p '/prosev' --permission-mode acceptEdits --add-dir $HOME/notes --add-dir $HOME/knowledge".
5. At night leave the computer on and do not put it to sleep.

Check:

1. Put a file with one line into the `$HOME/notes` folder: "The accounting report is built with the command report --month".
2. Run `/prosev` in Claude Code.
3. Claude replies "All good, all done.", and this line appears in the `$HOME/knowledge` folder.
4. Run `/prosev` again: the line is not added a second time.

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

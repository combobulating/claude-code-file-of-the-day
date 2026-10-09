# A Claude Code script that finds passwords left in plain text in your files

Protect your accounts and money: Claude Code finds files with your passwords in plain text, so you remove them in time.

Claude Code script · 2026-10-09 · by Slava Sazhin  
[Read the write-up](https://combobulating.ai/en/blog/claude-code-plain-text-passwords-script) on combobulating.ai · [По-русски](ru/) · [Srpski](sr/) · [Português](pt/)

## How to find passwords that sit in your files as plain text

1. Ask Claude: "Put the downloaded file find_secrets.py into the folder ~/.claude/scripts and check that python3 is on the computer; if it is not, install it".
2. Ask Claude: "Run ~/.claude/scripts/find_secrets.py on the folder $HOME/Documents and show me what it found". Instead of Documents, name the folder where your work files are.
3. The script prints the path of each file it found and what is in it: a password, an access key or a private key. It looks for a password next to the word password, and it will not find a password with no such word next to it. It also reads Word documents, Excel spreadsheets and CSV files. It does not show the passwords themselves and changes nothing in the files.

Check:

1. Ask Claude: "Create the folder $HOME/secrets-test, put a file note.txt in it with the line Email password: Kofe2026sad and run ~/.claude/scripts/find_secrets.py on this folder". The script prints the path of the file note.txt and the word "password", and does not show the password itself.
2. Ask Claude: "Delete the folder $HOME/secrets-test".

---

Part of [Claude Code file of the day](../../) by [combobulating](https://combobulating.ai/en), the cheapest hosting for Claude Code and other AI agents.

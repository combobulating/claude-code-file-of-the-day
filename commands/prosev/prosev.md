---
description: At night sifts fresh work notes with the filter "will this matter in three months" and moves what passes into the knowledge base. Deletes nothing.
---

# Prosev - nightly sifting of notes into the knowledge base

GOAL: what was learned at work and will outlive this week - how a place is set up, a working command, a trap found, an owner preference - must not get lost in old notes. Once a day the skill takes the notes changed in the last day, picks out what was learned, checks it against what the knowledge base already has, and adds what is missing.

MAIN: the skill deletes and shortens nothing - neither notes nor knowledge base entries. It only adds and fixes in place what is outdated in the knowledge base. An empty catch is a normal outcome: then nothing is written to the knowledge base.

## Step 1. Reading and selection

Read in full every note in the `$HOME/notes` folder changed in the last day. From each, write out candidates: one line per candidate - the essence and the source (note name).

There is one measure: picture a new conversation from a clean slate three months from now, doing a different task in the same place - will this entry save it even one step.

Not taken:
- the course and status of a task, what is done and what is left;
- one-off measurements and dates;
- what can be read from the code with one query;
- secrets in any form: password, token, key. Only a reference to an environment variable is allowed;
- anything personal, even if it turned up in a work note.

## Step 2. Checking the knowledge base BEFORE writing

For each candidate - a search in `$HOME/knowledge/*.md` by its distinctive words (path, command, service name, file name) and reading the found section in full, not one line. Three outcomes:
- already written - skip;
- written differently (outdated, differs from the note) - fix in place, with the observation date in the text of the fix;
- missing - add it to the section of a file that fits the topic.

A new file in the knowledge base is created only when none of the existing ones fits the topic.

## Step 3. Checking the write

After writing, check each change by reading that place: the text landed where named, the neighbouring text is intact. Does not match - put the file back as it was.

## Reply format

No errors - one line: "All good, all done." The same for an empty catch. There are errors - only them, one line each.

## Rules
- ⛔ Neither a bare secret nor anything personal is written to the knowledge base. Doubt is resolved as "do not write".
- The wording of an entry follows the neighbouring entries of the same file: the same language, the same order.

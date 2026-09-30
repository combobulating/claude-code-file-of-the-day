#!/usr/bin/env python3
"""A command that ONLY READS: parser for a shell command guard.

Splits the line into commands by separators (`;`, `&&`, `||`, `|`, `&`) and answers 0 only
when EVERY command is a read from a closed list of names. Anything else - 1. Parsing goes by
shell tokens (shlex): a separator INSIDE quotes (`grep "a|b"`) is not counted as a command.

Strictness: any doubt - answer 1. Not allowed: several lines, substitution `$(...)`,
back quotes, input from a file, heredoc, brackets, writing to a file, variable assignment,
a program by path and a command whose name is not in the read list.

Usage: command on stdin, exit code 0 - read only, 1 - not.
"""
import shlex
import sys

# Names that only read and print. The list is closed: not in it - not a read.
# Left out on purpose: `env`, `less`, `more`, `bat`, `awk`, `find`, `xargs`, `sed`, `sudo`,
# shells and python - they can run someone else's code.
READ_ONLY = {
    "grep", "egrep", "fgrep", "rg", "cat", "head", "tail", "ls", "wc",
    "sort", "uniq", "cut", "tr", "column", "echo", "printf", "comm", "nl", "tac", "which",
    "type", "file", "stat", "basename", "dirname", "realpath", "readlink", "pwd", "date",
    "diff", "md5sum", "sha256sum", "cksum", "true", "false", "test",
    "whoami", "id", "uptime", "df", "du", "jq", "git",
}

# Options with which a reading program writes a file or runs someone else's code. A long one
# is caught by abbreviation too (`--compress-prog`), a short one in a cluster (`-no`, `-Oless`).
DANGEROUS_OPTIONS = {
    "sort": ("--compress-program", "--output", "-o"),
    "rg": ("--pre", "--hostname-bin", "--search-zip", "-z"),
    "file": ("--compile", "-C"),
    "date": ("--set", "-s"),
    "git": ("-c", "--exec-path", "--upload-pack", "--receive-pack", "--ext-diff", "--output",
            "--open-files-in-pager", "-O", "--textconv", "--filters", "--config-env",
            "--attr-source", "--shallow-file"),
}

# git subcommands that only read. The rest (push, merge, commit, checkout) are actions.
GIT_READ_ONLY = {"log", "diff", "show", "status", "blame", "ls-files", "rev-parse", "cat-file",
                 "describe", "shortlog", "grep"}

SEPARATORS = {";", "&&", "||", "|", "&"}
SIGNS = set("();<>|&")


def read_only(line):
    line = line.strip()
    if not line or any(z in line for z in ("$(", "`", "<", "\n", "\r")):
        return False
    try:
        lex = shlex.shlex(line, posix=True, punctuation_chars=True)
        lex.whitespace_split = True
        lex.commenters = ""
        tokens = list(lex)
    except ValueError:
        return False

    command = []
    i = 0
    while i <= len(tokens):
        tok = tokens[i] if i < len(tokens) else None
        if tok is None or tok in SEPARATORS:
            if command and not command_is_read(command):
                return False
            command = []
            i += 1
            continue
        if tok in (">", ">>", "&>", ">&"):
            # Only /dev/null and joining streams `2>&1` pass, writing to a file does not.
            target = tokens[i + 1] if i + 1 < len(tokens) else None
            if target != "/dev/null" and not (tok == ">&" and target is not None and target.isdigit()):
                return False
            if command and command[-1].isdigit():
                command.pop()
            i += 2
            continue
        if set(tok) <= SIGNS:  # brackets and joined signs (`;(`, `>|`, `>(`)
            return False
        command.append(tok)
        i += 1
    return True


def command_is_read(words):
    name = words[0]
    # Assignment changes how the program behaves, a name with a path is someone else's program.
    if "=" in name or "/" in name or name not in READ_ONLY:
        return False
    # Braces, a mask and a variable are expanded by the shell after parsing: `{-o,f}`, `*`.
    extra = "*?[$" if name in DANGEROUS_OPTIONS or name == "uniq" else ""
    if any(z in s for s in words for z in "{}" + extra):
        return False
    for s in words[1:]:
        op = s.split("=", 1)[0]
        for o in DANGEROUS_OPTIONS.get(name, ()):
            if o.startswith("--"):
                if op.startswith("--") and len(op) > 2 and o.startswith(op):
                    return False
            elif s.startswith("-") and not s.startswith("--") and o[1] in s[1:]:
                return False
    # `-` is standard input, and after `--` a name is a file: `uniq - out` writes `out`.
    operands = [s for s in words[1:] if s == "-" or not s.startswith("-")]
    if name == "uniq" and ("--" in words or len(operands) > 1):
        return False
    if name == "git":
        sub, j = None, 1
        while j < len(words):
            s = words[j]
            if s.startswith("-"):  # options of git itself, -C and similar carry their own word
                j += 2 if s in ("-C", "--git-dir", "--work-tree", "--namespace") else 1
                continue
            sub = s
            break
        if sub not in GIT_READ_ONLY:
            return False
    return True


if __name__ == "__main__":
    sys.exit(0 if read_only(sys.stdin.read()) else 1)

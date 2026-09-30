#!/usr/bin/env python3
"""Команда, которая ТОЛЬКО ЧИТАЕТ: разбор для сторожа команд оболочки.

Делит строку на команды по разделителям (`;`, `&&`, `||`, `|`, `&`) и отвечает 0, только
когда КАЖДАЯ команда - чтение из закрытого списка имён. Всё прочее - 1. Разбор идёт по
лексемам оболочки (shlex): разделитель ВНУТРИ кавычек (`grep "a|b"`) командой не считается.

Строгость: любое сомнение - ответ 1. Не освобождаются: несколько строк, подстановка `$(...)`,
обратные кавычки, ввод из файла, heredoc, скобки, запись в файл, присваивание переменной,
программа по пути и команда, чьё имя в список чтения не входит.

Запуск: команда на stdin, код возврата 0 - только чтение, 1 - нет.
"""
import shlex
import sys

# Имена, которые только читают и печатают. Список закрытый: нет в нём - значит не чтение.
# Нет намеренно: `env`, `less`, `more`, `bat`, `awk`, `find`, `xargs`, `sed`, `sudo`,
# оболочки и питон - они умеют запускать чужое.
CHTENIE = {
    "grep", "egrep", "fgrep", "rg", "cat", "head", "tail", "ls", "wc",
    "sort", "uniq", "cut", "tr", "column", "echo", "printf", "comm", "nl", "tac", "which",
    "type", "file", "stat", "basename", "dirname", "realpath", "readlink", "pwd", "date",
    "diff", "md5sum", "sha256sum", "cksum", "true", "false", "test",
    "whoami", "id", "uptime", "df", "du", "jq", "git",
}

# Опции, которыми читающая программа пишет файл или запускает чужое. Длинная ловится и по
# сокращению (`--compress-prog`), короткая - и в склейке (`-no`, `-Oless`).
OPASNYE_OPCII = {
    "sort": ("--compress-program", "--output", "-o"),
    "rg": ("--pre", "--hostname-bin", "--search-zip", "-z"),
    "file": ("--compile", "-C"),
    "date": ("--set", "-s"),
    "git": ("-c", "--exec-path", "--upload-pack", "--receive-pack", "--ext-diff", "--output",
            "--open-files-in-pager", "-O", "--textconv", "--filters", "--config-env",
            "--attr-source", "--shallow-file"),
}

# Подкоманды git, которые только читают. Остальные (push, merge, commit, checkout) - действия.
GIT_CHTENIE = {"log", "diff", "show", "status", "blame", "ls-files", "rev-parse", "cat-file",
               "describe", "shortlog", "grep"}

RAZDELITELI = {";", "&&", "||", "|", "&"}
ZNAKI = set("();<>|&")


def tolko_chtenie(stroka):
    stroka = stroka.strip()
    if not stroka or any(z in stroka for z in ("$(", "`", "<", "\n", "\r")):
        return False
    try:
        lex = shlex.shlex(stroka, posix=True, punctuation_chars=True)
        lex.whitespace_split = True
        lex.commenters = ""
        leksemy = list(lex)
    except ValueError:
        return False

    komanda = []
    i = 0
    while i <= len(leksemy):
        lek = leksemy[i] if i < len(leksemy) else None
        if lek is None or lek in RAZDELITELI:
            if komanda and not komanda_chtenie(komanda):
                return False
            komanda = []
            i += 1
            continue
        if lek in (">", ">>", "&>", ">&"):
            # Пускаем только /dev/null и склейку потоков `2>&1`, запись в файл - нет.
            cel = leksemy[i + 1] if i + 1 < len(leksemy) else None
            if cel != "/dev/null" and not (lek == ">&" and cel is not None and cel.isdigit()):
                return False
            if komanda and komanda[-1].isdigit():
                komanda.pop()
            i += 2
            continue
        if set(lek) <= ZNAKI:  # скобки и склейки знаков (`;(`, `>|`, `>(`)
            return False
        komanda.append(lek)
        i += 1
    return True


def komanda_chtenie(slova):
    imya = slova[0]
    # Присваивание меняет поведение программы, имя по пути - чужая программа.
    if "=" in imya or "/" in imya or imya not in CHTENIE:
        return False
    # Фигурные скобки, маска и переменная раскрываются оболочкой после разбора: `{-o,f}`, `*`.
    dop = "*?[$" if imya in OPASNYE_OPCII or imya == "uniq" else ""
    if any(z in s for s in slova for z in "{}" + dop):
        return False
    for s in slova[1:]:
        op = s.split("=", 1)[0]
        for o in OPASNYE_OPCII.get(imya, ()):
            if o.startswith("--"):
                if op.startswith("--") and len(op) > 2 and o.startswith(op):
                    return False
            elif s.startswith("-") and not s.startswith("--") and o[1] in s[1:]:
                return False
    # `-` - это стандартный ввод, а после `--` имя - файл: `uniq - out` пишет `out`.
    operandy = [s for s in slova[1:] if s == "-" or not s.startswith("-")]
    if imya == "uniq" and ("--" in slova or len(operandy) > 1):
        return False
    if imya == "git":
        pod, j = None, 1
        while j < len(slova):
            s = slova[j]
            if s.startswith("-"):  # опции самой git, -C и подобные несут своё слово
                j += 2 if s in ("-C", "--git-dir", "--work-tree", "--namespace") else 1
                continue
            pod = s
            break
        if pod not in GIT_CHTENIE:
            return False
    return True


if __name__ == "__main__":
    sys.exit(0 if tolko_chtenie(sys.stdin.read()) else 1)

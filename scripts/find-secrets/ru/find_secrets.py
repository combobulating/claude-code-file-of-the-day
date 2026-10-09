#!/usr/bin/env python3
"""Находит в папке файлы, где пароль или ключ доступа записан открытым текстом.

Запуск: python3 find_secrets.py <папка>
Выводит путь к файлу и что в нём найдено. Сами пароли не выводит никогда.
Ничего не меняет, только читает. Читает и документы Word, и таблицы Excel.
"""
import html
import os
import re
import sys
import zipfile

# Сколько читать из одного файла: у большого файла читается только начало.
READ_MAX = 2_000_000
# Папки, в которые проверка не заходит.
SKIP_DIRS = {'.git', 'node_modules', '__pycache__', '.venv', 'venv'}
# Слово «пароль» по-английски, по-русски, по-португальски и по-черногорски.
LABELS = r'password|passwd|pwd|db_pass|\u043f\u0430\u0440\u043e\u043b|senha|lozink'

# Сильные признаки: такой текст бывает только у настоящего ключа.
STRONG = [
    ('закрытый ключ', re.compile(r'-----BEGIN [A-Z ]*PRIVATE KEY-----')),
    ('токен JWT', re.compile(r'\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.')),
    ('ключ сервисного аккаунта Google', re.compile(r'"type"\s*:\s*"service_account"')),
    ('токен GitLab', re.compile(r'glpat-[A-Za-z0-9_-]{15,}')),
    ('ключ AWS', re.compile(r'\bAKIA[0-9A-Z]{16}\b')),
    ('слово «пароль» в отдельной строке или ячейке', re.compile(r'(?im)^[ \t"]*(?:' + LABELS + r')\w{0,30}(?:[ \t]+\w{1,30}){0,2}[ \t"\r]*$')),
]
# Слабые признаки: слово вроде «пароль», secret или api_key и значение после него.
SOFT = [
    ('пароль', re.compile(r'(?i)\b(?:' + LABELS + r')[\w \t"\'-]{0,60}[=:]\s*(["\']?)(\S{6,})')),
    ('пароль', re.compile(r'(?i)\b(?:' + LABELS + r')\w{0,30}(?:[ \t]+\S{1,30}){0,6}?'
                          r'(?:[ \t]*[-\u2013\u2014:=][ \t]*|[ \t]+)(["\']?)((?=\S{0,200}?[\d!@#$%^&*?_+])\S{6,200})')),
    ('секрет', re.compile(r'(?i)\b[A-Z0-9_]*secret[A-Z0-9_]*["\']?\s*[=:]\s*(["\']?)(\S{8,})')),
    ('ключ доступа', re.compile(r'(?i)\b[A-Z0-9_]*(?:api[_-]?key|apikey|access[_-]?key|auth[_-]?'
                                r'token|bot[_-]?token)[A-Z0-9_]*["\']?\s*[=:]\s*(["\']?)(\S{8,})')),
    ('пароль в строке подключения', re.compile(r'(?i)(?:Password|Pwd)\s*=\s*([^;\s]{4,});')),
]
# Значение - это ссылка на переменную или настройку, а не сам пароль.
REFERENCE = re.compile(r"""(?ix)^(
   os\.environ|os\.getenv|environ|getenv|process\.env|System\.|Environment\.|configuration|
   config\.|self\.|this\.|cfg\.|settings\.|require\(|import\b|input\(|prompt
)""")
BRACKET = re.compile(r'^(\$\{?[A-Za-z_]|%\(|\{\{|\{[A-Za-z_]|<[A-Za-z_]|@[A-Za-z_]|\[)')
# Значение - заглушка из примера, а не пароль. Сравнивается целиком.
DUMMY = re.compile(r'(?ix)^(None|null|nil|true|false|undefined|x{3,}|y{3,}|\*+|\.{3,}|'
                   r'change_?me|your_?\w*|test|password|secret|dummy|example|sample|'
                   r'placeholder|\d{1,4}|["\'`]*)$')


def value(m):
    g = [x for x in m.groups() if x is not None]
    return (g[-1] if g else '').strip('"\'`,;)')


def is_secret(v):
    if not v or len(v) < 6:
        return False
    if REFERENCE.match(v) or BRACKET.match(v):
        return False
    if DUMMY.fullmatch(v):
        return False
    return True


def read_text(path):
    """Текст файла. У документа Word или таблицы Excel - текст из их частей, по абзацу или ячейке на строку."""
    low = path.lower()
    if low.endswith(('.docx', '.xlsx')):
        with zipfile.ZipFile(path) as z:
            parts = [z.open(n).read(READ_MAX) for n in z.namelist() if n.endswith('.xml')]
        text = b'\n'.join(parts).decode('utf-8', 'ignore')
        text = re.sub(r'</(?:w:p|w:tc|si|c|row)>', '\n', text)
        return html.unescape(re.sub(r'<[^>]+>', '', text))
    with open(path, 'rb') as fh:
        text = fh.read(READ_MAX).decode('utf-8', 'ignore')
    # В таблице CSV каждое поле идёт на отдельную строку.
    return re.sub(r'[,;\t]', '\n', text) if low.endswith(('.csv', '.tsv')) else text


def signs(path):
    """Что найдено в файле. Сами значения не возвращаются никогда."""
    try:
        data = read_text(path)
    except Exception:
        return []
    found = [name for name, rx in STRONG if rx.search(data)]
    for name, rx in SOFT:
        for m in rx.finditer(data):
            if is_secret(value(m)):
                found.append(name)
                break
    return sorted(set(found))


def main():
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    if not os.path.isdir(root):
        sys.exit(f'Нет такой папки: {root}')
    total = 0
    for folder, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            path = os.path.join(folder, f)
            if os.path.islink(path) or not os.path.isfile(path):
                continue
            found = signs(path)
            if found:
                total += 1
                print(f'{path}: {", ".join(found)}')
    print(f'Файлов с открытым паролем или ключом: {total}')


if __name__ == '__main__':
    main()

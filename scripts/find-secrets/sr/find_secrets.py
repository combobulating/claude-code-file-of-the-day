#!/usr/bin/env python3
"""Pronalazi u fascikli fajlove u kojima je lozinka ili ključ za pristup zapisan kao običan tekst.

Pokretanje: python3 find_secrets.py <fascikla>
Ispisuje putanju do fajla i šta je u njemu pronađeno. Same lozinke nikad ne ispisuje.
Ništa ne menja, samo čita. Čita i Word dokumente i Excel tabele.
"""
import html
import os
import re
import sys
import zipfile

# Koliko se čita iz jednog fajla: kod velikog fajla čita se samo početak.
READ_MAX = 2_000_000
# Fascikle u koje provera ne ulazi.
SKIP_DIRS = {'.git', 'node_modules', '__pycache__', '.venv', 'venv'}
# Reč „lozinka“ na engleskom, ruskom, portugalskom i crnogorskom.
LABELS = r'password|passwd|pwd|db_pass|\u043f\u0430\u0440\u043e\u043b|senha|lozink'

# Jaki znaci: ovakav tekst ima samo pravi ključ.
STRONG = [
    ('privatni ključ', re.compile(r'-----BEGIN [A-Z ]*PRIVATE KEY-----')),
    ('JWT token', re.compile(r'\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.')),
    ('ključ servisnog naloga Google', re.compile(r'"type"\s*:\s*"service_account"')),
    ('GitLab token', re.compile(r'glpat-[A-Za-z0-9_-]{15,}')),
    ('AWS ključ', re.compile(r'\bAKIA[0-9A-Z]{16}\b')),
    ('reč „lozinka“ sama u redu ili ćeliji', re.compile(r'(?im)^[ \t"]*(?:' + LABELS + r')\w{0,30}(?:[ \t]+\w{1,30}){0,2}[ \t"\r]*$')),
]
# Slabi znaci: reč kao „lozinka“, secret ili api_key i vrednost posle nje.
SOFT = [
    ('lozinka', re.compile(r'(?i)\b(?:' + LABELS + r')[\w \t"\'-]{0,60}[=:]\s*(["\']?)(\S{6,})')),
    ('lozinka', re.compile(r'(?i)\b(?:' + LABELS + r')\w{0,30}(?:[ \t]+\S{1,30}){0,6}?'
                          r'(?:[ \t]*[-\u2013\u2014:=][ \t]*|[ \t]+)(["\']?)((?=\S{0,200}?[\d!@#$%^&*?_+])\S{6,200})')),
    ('tajna', re.compile(r'(?i)\b[A-Z0-9_]*secret[A-Z0-9_]*["\']?\s*[=:]\s*(["\']?)(\S{8,})')),
    ('ključ za pristup', re.compile(r'(?i)\b[A-Z0-9_]*(?:api[_-]?key|apikey|access[_-]?key|auth[_-]?'
                                r'token|bot[_-]?token)[A-Z0-9_]*["\']?\s*[=:]\s*(["\']?)(\S{8,})')),
    ('lozinka u konekcionom stringu', re.compile(r'(?i)(?:Password|Pwd)\s*=\s*([^;\s]{4,});')),
]
# Vrednost je referenca na promenljivu ili podešavanje, a ne sama lozinka.
REFERENCE = re.compile(r"""(?ix)^(
   os\.environ|os\.getenv|environ|getenv|process\.env|System\.|Environment\.|configuration|
   config\.|self\.|this\.|cfg\.|settings\.|require\(|import\b|input\(|prompt
)""")
BRACKET = re.compile(r'^(\$\{?[A-Za-z_]|%\(|\{\{|\{[A-Za-z_]|<[A-Za-z_]|@[A-Za-z_]|\[)')
# Vrednost je šablon iz primera, a ne lozinka. Poredi se u celini.
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
    """Tekst fajla. Kod Word dokumenta ili Excel tabele, tekst iz njihovih delova, po jedan pasus ili ćelija u redu."""
    low = path.lower()
    if low.endswith(('.docx', '.xlsx')):
        with zipfile.ZipFile(path) as z:
            parts = [z.open(n).read(READ_MAX) for n in z.namelist() if n.endswith('.xml')]
        text = b'\n'.join(parts).decode('utf-8', 'ignore')
        text = re.sub(r'</(?:w:p|w:tc|si|c|row)>', '\n', text)
        return html.unescape(re.sub(r'<[^>]+>', '', text))
    with open(path, 'rb') as fh:
        text = fh.read(READ_MAX).decode('utf-8', 'ignore')
    # U CSV tabeli svako polje ide u poseban red.
    return re.sub(r'[,;\t]', '\n', text) if low.endswith(('.csv', '.tsv')) else text


def signs(path):
    """Šta je pronađeno u fajlu. Same vrednosti se nikad ne vraćaju."""
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
        sys.exit(f'Nema takve fascikle: {root}')
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
    print(f'Fajlova sa otvorenom lozinkom ili ključem: {total}')


if __name__ == '__main__':
    main()

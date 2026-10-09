#!/usr/bin/env python3
"""Encontra numa pasta os arquivos em que uma senha ou uma chave de acesso está escrita como texto aberto.

Uso: python3 find_secrets.py <pasta>
Mostra o caminho do arquivo e o tipo do que encontrou. Nunca mostra as senhas em si.
Não muda nada, só lê. Também lê documentos do Word e planilhas do Excel.
"""
import html
import os
import re
import sys
import zipfile

# Quanto ler de um arquivo: de um arquivo grande só se lê o começo.
READ_MAX = 2_000_000
# Pastas em que a verificação não entra.
SKIP_DIRS = {'.git', 'node_modules', '__pycache__', '.venv', 'venv'}
# A palavra “senha” em inglês, russo, português e montenegrino.
LABELS = r'password|passwd|pwd|db_pass|\u043f\u0430\u0440\u043e\u043b|senha|lozink'

# Sinais fortes: só uma chave de verdade tem um texto assim.
STRONG = [
    ('chave privada', re.compile(r'-----BEGIN [A-Z ]*PRIVATE KEY-----')),
    ('token JWT', re.compile(r'\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.')),
    ('chave de conta de serviço do Google', re.compile(r'"type"\s*:\s*"service_account"')),
    ('token do GitLab', re.compile(r'glpat-[A-Za-z0-9_-]{15,}')),
    ('chave da AWS', re.compile(r'\bAKIA[0-9A-Z]{16}\b')),
    ('a palavra “senha” sozinha numa linha ou célula', re.compile(r'(?im)^[ \t"]*(?:' + LABELS + r')\w{0,30}(?:[ \t]+\w{1,30}){0,2}[ \t"\r]*$')),
]
# Sinais fracos: uma palavra como “senha”, secret ou api_key e o valor depois dela.
SOFT = [
    ('senha', re.compile(r'(?i)\b(?:' + LABELS + r')[\w \t"\'-]{0,60}[=:]\s*(["\']?)(\S{6,})')),
    ('senha', re.compile(r'(?i)\b(?:' + LABELS + r')\w{0,30}(?:[ \t]+\S{1,30}){0,6}?'
                          r'(?:[ \t]*[-\u2013\u2014:=][ \t]*|[ \t]+)(["\']?)((?=\S{0,200}?[\d!@#$%^&*?_+])\S{6,200})')),
    ('segredo', re.compile(r'(?i)\b[A-Z0-9_]*secret[A-Z0-9_]*["\']?\s*[=:]\s*(["\']?)(\S{8,})')),
    ('chave de acesso', re.compile(r'(?i)\b[A-Z0-9_]*(?:api[_-]?key|apikey|access[_-]?key|auth[_-]?'
                                r'token|bot[_-]?token)[A-Z0-9_]*["\']?\s*[=:]\s*(["\']?)(\S{8,})')),
    ('senha numa string de conexão', re.compile(r'(?i)(?:Password|Pwd)\s*=\s*([^;\s]{4,});')),
]
# O valor é uma referência a uma variável ou configuração, não a senha em si.
REFERENCE = re.compile(r"""(?ix)^(
   os\.environ|os\.getenv|environ|getenv|process\.env|System\.|Environment\.|configuration|
   config\.|self\.|this\.|cfg\.|settings\.|require\(|import\b|input\(|prompt
)""")
BRACKET = re.compile(r'^(\$\{?[A-Za-z_]|%\(|\{\{|\{[A-Za-z_]|<[A-Za-z_]|@[A-Za-z_]|\[)')
# O valor é um exemplo de preenchimento, não uma senha. É comparado por inteiro.
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
    """Texto do arquivo. Para um documento do Word ou uma planilha do Excel, o texto das suas partes, um parágrafo ou célula por linha."""
    low = path.lower()
    if low.endswith(('.docx', '.xlsx')):
        with zipfile.ZipFile(path) as z:
            parts = [z.open(n).read(READ_MAX) for n in z.namelist() if n.endswith('.xml')]
        text = b'\n'.join(parts).decode('utf-8', 'ignore')
        text = re.sub(r'</(?:w:p|w:tc|si|c|row)>', '\n', text)
        return html.unescape(re.sub(r'<[^>]+>', '', text))
    with open(path, 'rb') as fh:
        text = fh.read(READ_MAX).decode('utf-8', 'ignore')
    # Numa tabela CSV, cada campo vai para uma linha própria.
    return re.sub(r'[,;\t]', '\n', text) if low.endswith(('.csv', '.tsv')) else text


def signs(path):
    """Tipos do que foi encontrado no arquivo. Os valores em si nunca são devolvidos."""
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
        sys.exit(f'Pasta não encontrada: {root}')
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
    print(f'Arquivos com senha ou chave em texto aberto: {total}')


if __name__ == '__main__':
    main()

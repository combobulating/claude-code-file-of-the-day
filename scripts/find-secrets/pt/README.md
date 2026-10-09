# Um script para o Claude Code que encontra senhas deixadas em texto aberto nos seus arquivos

Proteja suas contas e seu dinheiro: o Claude Code encontra arquivos com suas senhas em texto aberto, para você tirá-las a tempo.

2026-10-09 · Slava Sazhin  
[Texto completo](https://combobulating.ai/pt/blog/claude-code-plain-text-passwords-script) no combobulating.ai · [English](../)

## Como encontrar senhas que estão nos seus arquivos como texto aberto

1. Peça ao Claude: “Coloque o arquivo baixado find_secrets.py na pasta ~/.claude/scripts e verifique se o python3 está no computador; se não estiver, instale”.
2. Peça ao Claude: “Rode ~/.claude/scripts/find_secrets.py na pasta $HOME/Documents e me mostre o que ele encontrou”. Em vez de Documents, indique a pasta onde ficam os seus arquivos de trabalho.
3. O script mostra o caminho de cada arquivo encontrado e o que há nele: uma senha, uma chave de acesso ou uma chave privada. Ele procura a senha ao lado da palavra “senha” ou password, e uma senha sem essa palavra ao lado ele não encontra. Ele também lê documentos do Word, planilhas do Excel e arquivos CSV. Ele não mostra as senhas em si e não muda nada nos arquivos.

Verificação:

1. Peça ao Claude: “Crie a pasta $HOME/secrets-test, coloque nela um arquivo note.txt com a linha Senha do e-mail: Kofe2026sad e rode ~/.claude/scripts/find_secrets.py nessa pasta”. O script mostra o caminho do arquivo note.txt e a palavra “senha”, e não mostra a senha em si.
2. Peça ao Claude: “Apague a pasta $HOME/secrets-test”.

---

Da série “Arquivo do dia” no [combobulating.ai](https://combobulating.ai/pt/blog).

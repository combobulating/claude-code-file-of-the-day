# Um hook para o Claude Code que pula os pedidos de permissão enquanto você está fora

Deixe o Claude Code com uma tarefa e ele não espera mais uma hora num pedido de permissão: o passo que precisa do seu “sim” é pulado, o resto é feito.

2026-10-24 · Slava Sazhin  
[Texto completo](https://combobulating.ai/pt/blog/claude-code-no-stops-while-away-hook) no combobulating.ai · [English](../)

## Como evitar que um pedido de permissão pare o trabalho enquanto você está fora

1. Peça ao Claude: “Coloque o arquivo baixado deny-while-away.sh na pasta ~/.claude/hooks/ e torne-o executável.”
2. Peça ao Claude: “Adicione ~/.claude/hooks/deny-while-away.sh ao ~/.claude/settings.json como um hook PermissionRequest para todas as ferramentas.”
3. Feche o Claude Code e abra de novo: os hooks são lidos na inicialização.
4. Quando sair, comece o seu pedido com as palavras “trabalhe sem mim”. Enquanto essa for a sua última mensagem, qualquer passo para o qual o Claude pediria permissão é pulado, e o resto do trabalho continua.
5. Para que o Claude possa editar arquivos sem você, antes de sair aperte Shift+Tab até aparecer “accept edits on” embaixo. Nesse modo o Claude também move e apaga arquivos na pasta de trabalho sem perguntar.
6. A sua próxima mensagem traz de volta os pedidos de permissão de sempre. Para o Claude voltar a perguntar também sobre edições de arquivos, aperte Shift+Tab até aparecer “manual mode on” embaixo.

Verificação:

1. Peça ao Claude: “Trabalhe sem mim. Rode o comando curl -sI https://claude.com e mostre a primeira linha da resposta.”
2. Não aparece pedido de permissão: o Claude escreve que esse passo foi pulado porque não havia como perguntar a você.
3. Peça ao Claude a mesma coisa sem as palavras “trabalhe sem mim”: aparece o pedido de permissão de sempre; responda “No”.

---

Da série “Arquivo do dia” no [combobulating.ai](https://combobulating.ai/pt/blog).

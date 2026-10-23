# Uma regra para o Claude Code que verifica o resultado antes de dizer “feito”

O Claude Code só chama uma tarefa de feita depois de olhar o resultado ele mesmo e conta o que viu. Uma mensagem de sucesso do script não conta mais.

2026-10-23 · Slava Sazhin  
[Texto completo](https://combobulating.ai/pt/blog/claude-code-done-means-checked-rule) no combobulating.ai · [English](../)

## Como fazer o Claude parar de dizer “feito” sem verificar

1. Peça ao Claude: “Acrescente o conteúdo do arquivo baixado verified-done.md ao final do arquivo ~/.claude/CLAUDE.md e, se esse arquivo não existir, crie-o”.
2. Feche o Claude Code e abra de novo: as regras são lidas na inicialização.

Verificação:

1. Peça ao Claude: “Crie um arquivo hello.txt com a palavra hello”.
2. Na resposta haverá “feito, verificado:” e o que o Claude viu quando abriu o arquivo depois de gravá-lo.

---

Da série “Arquivo do dia” no [combobulating.ai](https://combobulating.ai/pt/blog).

# Uma regra para o Claude Code que mantém um registro da tarefa para a próxima conversa continuar dali

Uma regra para o seu CLAUDE.md: o Claude mantém um registro de cada tarefa, e uma conversa nova o lê e continua de onde a anterior parou.

2026-10-06 · Slava Sazhin  
[Texto completo](https://combobulating.ai/pt/blog/claude-code-task-log-rule) no combobulating.ai · [English](../)

## Como adicionar a regra: um registro da tarefa, para uma conversa nova continuar de onde você parou

1. Peça ao Claude: “Acrescente o conteúdo do arquivo baixado task-log.md ao final do arquivo ~/.claude/CLAUDE.md e, se esse arquivo não existir, crie-o”.
2. Feche o Claude Code e abra de novo: a regra é lida na inicialização.

Verificação:

1. Peça ao Claude: “Faça uma lista de compras para abrir uma cafeteria”. Na primeira linha da resposta, o Claude vai escrever o caminho do registro desta tarefa.
2. Feche o Claude Code, abra de novo e peça: “Vamos continuar a lista de compras da cafeteria”. O Claude vai encontrar o registro e continuar de onde você parou. Sem o arquivo, uma conversa nova começa do zero.

---

Da série “Arquivo do dia” no [combobulating.ai](https://combobulating.ai/pt/blog).

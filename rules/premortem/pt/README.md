# Uma regra para o Claude Code que descobre onde o trabalho vai quebrar antes da entrega

Uma regra para o seu CLAUDE.md: no fim de cada tarefa e plano, o Claude imagina que o trabalho falhou e trata das causas antes da entrega.

2026-10-04 · Slava Sazhin  
[Texto completo](https://combobulating.ai/pt/blog/claude-code-premortem-rule) no combobulating.ai · [English](../)

## Como instalar a regra: descobrir onde o trabalho vai quebrar, antes da entrega

1. Peça ao Claude: “Acrescente o conteúdo do arquivo baixado premortem.md ao final do arquivo ~/.claude/CLAUDE.md e, se esse arquivo não existir, crie-o”.
2. Feche o Claude Code e abra de novo: a regra é lida na inicialização.

Verificação:

1. Peça ao Claude: “Monte um plano para passar a agenda dos clientes de um caderno de papel para uma planilha do Google”.
2. No fim do plano, o Claude escreve o bloco “O que pode dar errado”: o que ele já levou em conta no próprio plano e o que espera a sua decisão. Sem o arquivo, esse bloco não aparece.

---

Da série “Arquivo do dia” no [combobulating.ai](https://combobulating.ai/pt/blog).

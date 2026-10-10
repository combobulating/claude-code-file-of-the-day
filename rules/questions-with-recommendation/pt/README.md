# Uma regra para o Claude Code que traz uma decisão pronta em cada pergunta

Decida em segundos: o Claude Code sugere a melhor opção em cada pergunta que faz, e um dígito basta para responder.

2026-10-10 · Slava Sazhin  
[Texto completo](https://combobulating.ai/pt/blog/claude-code-questions-with-recommendation-rule) no combobulating.ai · [English](../)

## Como fazer o Claude dar uma decisão pronta em cada pergunta

1. Peça ao Claude: “Acrescente o conteúdo do arquivo baixado questions-with-recommendation.md ao final do arquivo ~/.claude/CLAUDE.md e, se esse arquivo não existir, crie-o”.
2. Feche o Claude Code e abra de novo: as regras são lidas na inicialização.

Verificação:

1. Peça ao Claude: “Sugira um nome para a minha cafeteria e me pergunte qual opção eu prefiro”. As opções vêm numeradas, a recomendada vem primeiro, e ao lado dela o Claude diz em que se baseia.
2. Responda com um único dígito, por exemplo “2”. O Claude primeiro repete a segunda opção palavra por palavra e só depois continua o trabalho.

---

Da série “Arquivo do dia” no [combobulating.ai](https://combobulating.ai/pt/blog).

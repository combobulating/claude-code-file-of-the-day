# Uma regra para o Claude Code que diz em um minuto se vale aceitar um trabalho

Cole um pedido, uma licitação ou uma proposta, e o Claude Code responde: enviar proposta agora, agora não ou recusar, com um motivo e cinco notas.

2026-10-14 · Slava Sazhin  
[Texto completo](https://combobulating.ai/pt/blog/claude-code-bid-or-pass-rule) no combobulating.ai · [English](../)

## Como saber em um minuto se vale aceitar um trabalho

1. Peça ao Claude: “Acrescente o conteúdo do arquivo baixado bid-or-pass.md ao final do arquivo ~/.claude/CLAUDE.md e, se esse arquivo não existir, crie-o”.
2. Peça ao Claude: “No ~/.claude/CLAUDE.md, embaixo do título ‘O que eu faço’ escreva: ..., e embaixo do título ‘O que eu não aceito’: ...”. No lugar dos pontos, descreva o seu negócio com as suas palavras.
3. Feche o Claude Code e abra de novo: as regras são lidas na inicialização.

Verificação:

1. Pergunte ao Claude: “Devo aceitar este trabalho?” e cole o texto de um pedido, de uma licitação ou de uma carta com uma proposta que você recebeu recentemente.
2. Na primeira linha o Claude escreve “Enviar proposta agora”, “Agora não” ou “Recusar” com uma frase dizendo por quê e, abaixo, uma nota para cada um dos cinco critérios, se o trabalho passou na primeira verificação.

---

Da série “Arquivo do dia” no [combobulating.ai](https://combobulating.ai/pt/blog).

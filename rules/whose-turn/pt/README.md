# Uma regra para o Claude Code que termina cada resposta com uma marca de quem é a vez

Uma regra para o seu CLAUDE.md: cada resposta que passa o trabalho para você termina com uma marca, e você vê na hora se o Claude precisa de você.

2026-10-07 · Slava Sazhin  
[Texto completo](https://combobulating.ai/pt/blog/claude-code-whose-turn-mark-rule) no combobulating.ai · [English](../)

## Como adicionar a regra: uma marca no fim da resposta do Claude mostra de quem é a vez agora

1. Peça ao Claude: “Acrescente o conteúdo do arquivo baixado whose-turn.md ao final do arquivo ~/.claude/CLAUDE.md e, se esse arquivo não existir, crie-o”.
2. Feche o Claude Code e abra de novo: a regra é lida na inicialização.

Verificação:

1. Peça ao Claude: “Escreva um aviso curto de que a minha cafeteria agora abre às 8 da manhã e salve em notice.txt”. A resposta termina com a marca ✅: o trabalho está feito, não precisa de nada de você.
2. Peça ao Claude: “Sugira dois nomes para a minha nova cafeteria, e eu mesmo decido qual escolher”. A resposta termina com a marca ✏️: agora é preciso a sua escolha.
3. Sem o arquivo, não há marca no fim da resposta.

---

Da série “Arquivo do dia” no [combobulating.ai](https://combobulating.ai/pt/blog).

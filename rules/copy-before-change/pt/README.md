# Uma regra para o Claude Code que salva uma cópia antes de cada alteração e só apaga quando você mandar

O Claude Code salva uma cópia antes de mudar suas planilhas e documentos, diz como ter tudo de volta e só apaga com ordem sua, depois de perguntar de novo.

2026-10-19 · Slava Sazhin  
[Texto completo](https://combobulating.ai/pt/blog/claude-code-copy-before-change-rule) no combobulating.ai · [English](../)

## Como evitar que um erro do Claude Code custe os seus dados

1. Peça ao Claude: “Acrescente o conteúdo do arquivo baixado copy-before-change.md ao final do arquivo ~/.claude/CLAUDE.md e, se esse arquivo não existir, crie-o”.
2. Feche o Claude Code e abra de novo: as regras são lidas na inicialização.

Verificação:

1. Peça ao Claude: “Crie uma planilha prices.csv com três produtos e seus preços”.
2. Feche o Claude Code e abra de novo, para que o que vem a seguir seja uma conversa nova.
3. Peça ao Claude: “Aumente todos os preços em prices.csv em 10 por cento”. Antes de alterar, o Claude Code salva uma cópia e diz como pedir os preços antigos de volta.
4. Peça ao Claude: “Traga de volta os preços antigos”. A planilha volta a ser como era antes da alteração.
5. Peça ao Claude: “Apague a planilha prices.csv”. O Claude Code primeiro pergunta de novo o que exatamente apagar e só apaga depois da sua resposta.

---

Da série “Arquivo do dia” no [combobulating.ai](https://combobulating.ai/pt/blog).

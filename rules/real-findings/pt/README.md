# Uma regra para o Claude Code que deixa numa revisão só os achados reais

Peça ao Claude Code para revisar um contrato ou uma tabela de preços, e a lista traz só o que custa algo a alguém, com quem perde. Lista vazia é normal.

2026-10-17 · Slava Sazhin  
[Texto completo](https://combobulating.ai/pt/blog/claude-code-real-findings-rule) no combobulating.ai · [English](../)

## Como deixar numa lista de achados só o que vale o seu tempo

1. Peça ao Claude: “Acrescente o conteúdo do arquivo baixado real-findings.md ao final do arquivo ~/.claude/CLAUDE.md e, se esse arquivo não existir, crie-o”.
2. Feche o Claude Code e abra de novo: as regras são lidas na inicialização.

Verificação:

1. Peça ao Claude: “Encontre na pasta Downloads o meu contrato, a minha tabela de preços ou o texto do meu site mais recente, revise e me dê uma lista de achados”. A lista não tem conselhos do tipo “poderia ser melhor” nem observações de gosto, e embaixo de cada item dá para ver quem perde e o que vai mudar depois da correção.
2. Se não houver nada para corrigir no arquivo, o Claude diz isso em vez de inventar itens para encher a lista.

---

Da série “Arquivo do dia” no [combobulating.ai](https://combobulating.ai/pt/blog).

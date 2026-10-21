# Um script para o Claude Code que mostra qual trabalho consome o seu dinheiro e o seu limite

Veja quais pastas e conversas consomem o seu dinheiro ou o limite da assinatura do Claude Code, contado pelos registros no seu computador.

2026-10-21 · Slava Sazhin  
[Texto completo](https://combobulating.ai/pt/blog/claude-code-spend-by-project-script) no combobulating.ai · [English](../)

## Como ver qual trabalho consome o seu dinheiro e o seu limite no Claude Code

1. Peça ao Claude: “Coloque o arquivo baixado claude-spend-by-project.py na pasta ~/.claude/scripts e, se essa pasta não existir, crie a pasta”.
2. Peça ao Claude: “Rode python3 ~/.claude/scripts/claude-spend-by-project.py. Se no final houver uma linha ‘Sem preço’, abra https://platform.claude.com/docs/en/about-claude/pricing, coloque os preços dos modelos citados nela em PRICES neste arquivo e rode de novo”.

Verificação:

1. Você verá uma tabela: cada pasta onde você trabalhou com o Claude Code, quantas conversas ela teve, o valor e a parte dele no total. Abaixo dela estão as cinco conversas mais caras com o primeiro pedido de cada uma.
2. O valor é calculado pelos preços de tokens da Anthropic. Na assinatura você não paga esse valor; ele mostra qual trabalho consome mais do seu limite.
3. Para ver só a última semana, peça ao Claude: “Rode python3 ~/.claude/scripts/claude-spend-by-project.py 7”.
4. O Claude Code guarda os registros das conversas por 30 dias, então o relatório não vê trabalhos mais antigos.

---

Da série “Arquivo do dia” no [combobulating.ai](https://combobulating.ai/pt/blog).

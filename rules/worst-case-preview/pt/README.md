# Uma regra para o Claude Code que mostra onde uma página quebra antes dos seus clientes

O Claude Code preenche cada prévia com os seus nomes reais mais longos e os maiores números, e você vê o card quebrado antes dos clientes.

2026-10-13 · Slava Sazhin  
[Texto completo](https://combobulating.ai/pt/blog/claude-code-worst-case-preview-rule) no combobulating.ai · [English](../)

## Como ver onde uma página quebra antes dos seus clientes

1. Peça ao Claude: “Acrescente o conteúdo do arquivo baixado worst-case-preview.md ao final do arquivo ~/.claude/CLAUDE.md e, se esse arquivo não existir, crie-o”.
2. Feche o Claude Code e abra de novo: as regras são lidas na inicialização.

Verificação:

1. Peça ao Claude: “Faça um card de produto para o meu site e me mostre. Meus produtos: Café; Chá verde; kit presente ‘Manhã na Montanha’: duas canecas, um bule de café e café moído de três blends”.
2. O Claude mostra cards lado a lado com o nome mais longo, um comum e o mais curto, e não inventa o que você não passou: preços, fotos, descrições. No card longo dá para ver na hora se o nome cabe.

---

Da série “Arquivo do dia” no [combobulating.ai](https://combobulating.ai/pt/blog).

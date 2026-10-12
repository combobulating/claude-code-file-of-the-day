# Uma regra para o Claude Code que mantém o trabalho andando enquanto você está fora

O Claude Code continua trabalhando enquanto você está fora: decide sozinho em vez de esperar resposta e no fim diz o que foi feito e o que não foi.

2026-10-12 · Slava Sazhin  
[Texto completo](https://combobulating.ai/pt/blog/claude-code-work-without-me-rule) no combobulating.ai · [English](../)

## Como manter o trabalho andando enquanto você está fora

1. Peça ao Claude: “Acrescente o conteúdo do arquivo baixado work-without-me.md ao final do arquivo ~/.claude/CLAUDE.md e, se esse arquivo não existir, crie-o”.
2. Feche o Claude Code e abra de novo: as regras são lidas na inicialização.
3. Quando sair, comece o seu pedido com as palavras “trabalhe sem mim”. O modo termina com a sua próxima mensagem.

Verificação:

1. Peça ao Claude: “Trabalhe sem mim. Invente um nome para a minha cafeteria e escreva um anúncio de inauguração”. O Claude não pergunta qual nome você prefere: ele mesmo escolhe um, escreve o anúncio e termina com um relatório com as partes “Feito sem você” e “Não feito”.
2. Mande ao Claude qualquer mensagem sem essas palavras: o modo está desligado, e a resposta não tem o relatório em duas partes.

---

Da série “Arquivo do dia” no [combobulating.ai](https://combobulating.ai/pt/blog).

# Uma regra para o Claude Code que oferece agendar o trabalho que você passa a ele de novo e de novo

O Claude Code nota o trabalho que você passa a ele de novo e de novo, oferece numa linha agendá-lo e, com o seu sim, configura e roda uma vez.

2026-10-21 · Slava Sazhin  
[Texto completo](https://combobulating.ai/pt/blog/claude-code-repeat-work-on-schedule-rule) no combobulating.ai · [English](../)

## Como o Claude Code mostra qual trabalho já pode rodar num agendamento sem você

1. Peça ao Claude: “Acrescente o conteúdo do arquivo baixado offer-a-schedule.md ao final do arquivo ~/.claude/CLAUDE.md e, se esse arquivo não existir, crie-o”.
2. Feche o Claude Code e abra de novo: as regras são lidas na inicialização.

Verificação:

1. Pergunte ao Claude: “Olhe o histórico das nossas conversas anteriores: que trabalho eu te passo de novo e de novo, e o que dele vale a pena colocar num agendamento?” O Claude Code diz qual é esse trabalho e o que ele vai economizar para você, ou diz que ainda não há nada para agendar.
2. Se você concordar com a sugestão, responda “sim”. O Claude Code coloca o trabalho no agendamento sozinho e roda uma vez na hora, para você ver o resultado; se ele pedir permissão para rodar um comando, permita.
3. A partir daí, quando você der a ele uma tarefa conhecida pela terceira vez e ela puder ser feita sem você, aparece uma linha com uma sugestão no fim da resposta.

---

Da série “Arquivo do dia” no [combobulating.ai](https://combobulating.ai/pt/blog).

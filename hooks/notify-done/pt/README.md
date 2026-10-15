# Um hook para o Claude Code que mostra o começo de cada resposta em uma notificação

Quando o Claude Code termina uma resposta, aparece no canto da tela uma notificação com as primeiras palavras, e você pode trabalhar em outra janela.

2026-10-15 · Slava Sazhin  
[Texto completo](https://combobulating.ai/pt/blog/claude-code-reply-notification-hook) no combobulating.ai · [English](../)

## Como saber que o Claude terminou sem ficar olhando para a tela

1. Peça ao Claude: “Coloque o arquivo baixado notify-done.sh na pasta ~/.claude/hooks/ e torne-o executável.”
2. Peça ao Claude: “Adicione ~/.claude/hooks/notify-done.sh ao ~/.claude/settings.json como um hook de Stop.”
3. Peça ao Claude: “Verifique se o jq está instalado neste computador e instale-o se não estiver.”
4. No Mac, peça ao Claude: “Execute o comando osascript -e 'display notification "test"'.”
5. Depois abra os “Ajustes do Sistema” (System Settings), vá em “Notificações” (Notifications), encontre o “Editor de Script” (Script Editor) na lista e ative “Permitir Notificações” (Allow Notifications).
6. Se o seu computador não for um Mac, peça ao Claude: “No arquivo ~/.claude/hooks/notify-done.sh, substitua o osascript pelo comando de notificação do meu sistema.”
7. Feche o Claude Code e abra de novo: os hooks são lidos na inicialização.

Verificação:

1. Peça ao Claude: “Responda em uma linha com o texto: notificações funcionam” e mude logo para outra janela.
2. Alguns segundos depois, aparece no canto da tela uma notificação “Claude Code” com o começo da resposta.

---

Da série “Arquivo do dia” no [combobulating.ai](https://combobulating.ai/pt/blog).

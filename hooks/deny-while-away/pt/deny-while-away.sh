#!/bin/bash
# Hook PermissionRequest: enquanto você está fora, o Claude Code não espera a sua permissão.
# Se a sua última mensagem começa com as palavras “trabalhe sem mim”, o pedido de permissão
# é negado: o passo é pulado e o trabalho continua. No resto do tempo, o pedido de permissão aparece como sempre.
# Negar só pelo objeto decision: o código de saída 2 não é levado em conta neste evento.
# Referência: https://code.claude.com/docs/en/hooks, seção “PermissionRequest”.

# --- entrada ---
INPUT=$(cat 2>/dev/null)
TRANSCRIPT=$(printf '%s' "$INPUT" | grep -o '"transcript_path" *: *"[^"]*"' | sed 's/.*: *"//; s/"$//; s/\\\\/\\/g')
[ -f "$TRANSCRIPT" ] || exit 0

# --- você está aqui? ---
LAST_PROMPT=$(grep -F '"origin":{"kind":"human"' "$TRANSCRIPT" | tail -n 1)
printf '%s' "$LAST_PROMPT" | grep -qE '"(content|text|prompt)":"(T|t)rabalhe sem mim' || exit 0

# --- resposta ---
printf '%s\n' '{"hookSpecificOutput":{"hookEventName":"PermissionRequest","decision":{"behavior":"deny","message":"Não há a quem pedir permissão: a última mensagem começa com as palavras “trabalhe sem mim”, e a pessoa não está disponível até a próxima mensagem dela. Não faça este passo, não o repita e não o contorne de outro jeito. Termine o resto do trabalho em passos separados e cite o passo pulado no seu relatório."}}}'
exit 0

#!/bin/bash
# Hook PermissionRequest: dok vas nema, Claude Code ne čeka vašu dozvolu.
# Ako vaša poslednja poruka počinje rečima „radi bez mene“, zahtev za dozvolu
# se odbija: korak se preskače, a posao ide dalje. U ostalo vreme pitanje za dozvolu je kao i obično.
# Odbijati samo preko objekta decision: izlazni kod 2 se za ovaj događaj ne uzima u obzir.
# Referenca: https://code.claude.com/docs/en/hooks, odeljak „PermissionRequest“.

# --- ulaz ---
INPUT=$(cat 2>/dev/null)
TRANSCRIPT=$(printf '%s' "$INPUT" | grep -o '"transcript_path" *: *"[^"]*"' | sed 's/.*: *"//; s/"$//; s/\\\\/\\/g')
[ -f "$TRANSCRIPT" ] || exit 0

# --- da li ste tu? ---
LAST_PROMPT=$(grep -F '"origin":{"kind":"human"' "$TRANSCRIPT" | tail -n 1)
printf '%s' "$LAST_PROMPT" | grep -qE '"(content|text|prompt)":"(R|r)adi bez mene' || exit 0

# --- odgovor ---
printf '%s\n' '{"hookSpecificOutput":{"hookEventName":"PermissionRequest","decision":{"behavior":"deny","message":"Nema koga da se pita za dozvolu: poslednja poruka počinje rečima „radi bez mene“, i osoba nije dostupna do svoje sledeće poruke. Ne radi ovaj korak, ne ponavljaj ga i ne zaobilazi ga na drugi način. Ostatak posla završi u odvojenim koracima, a preskočeni korak navedi u izveštaju."}}}'
exit 0

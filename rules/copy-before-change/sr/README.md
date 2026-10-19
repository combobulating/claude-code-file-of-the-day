# Pravilo za Claude Code koje čuva kopiju pre svake izmene i briše samo na vašu reč

Claude Code čuva kopiju pre nego što menja vaše tabele i dokumente, kaže kako da sve vratite i briše samo na vašu komandu, pošto još jednom pita.

2026-10-19 · Slava Sazhin  
[Ceo tekst](https://combobulating.ai/sr/blog/claude-code-copy-before-change-rule) na combobulating.ai · [English](../)

## Kako da vas greška Claude Code-a ne košta podataka

1. Zamolite Claude-a: „Dopiši sadržaj preuzetog fajla copy-before-change.md na kraj fajla ~/.claude/CLAUDE.md, a ako takvog fajla nema, napravi ga“.
2. Zatvorite Claude Code i ponovo ga otvorite: pravila se čitaju pri pokretanju.

Provera:

1. Zamolite Claude-a: „Napravi tabelu prices.csv sa tri proizvoda i njihovim cenama“.
2. Zatvorite Claude Code i ponovo ga otvorite, da bi ono što sledi bio novi razgovor.
3. Zamolite Claude-a: „Podigni sve cene u prices.csv za 10 procenata“. Pre izmene Claude Code čuva kopiju i kaže vam kako da tražite stare cene nazad.
4. Zamolite Claude-a: „Vrati stare cene“. Tabela je ponovo onakva kakva je bila pre izmene.
5. Zamolite Claude-a: „Obriši tabelu prices.csv“. Claude Code prvo ponovo pita šta tačno da obriše i briše tek posle vašeg odgovora.

---

Iz rubrike „Fajl dana“ na [combobulating.ai](https://combobulating.ai/sr/blog).

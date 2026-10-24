# Hook za Claude Code koji preskače pitanja za dozvolu dok vas nema

Ostavite Claude Code sa zadatkom i on više ne čeka sat vremena na pitanju za dozvolu: korak kome treba vaše „da“ se preskače, ostalo se radi.

2026-10-24 · Slava Sazhin  
[Ceo tekst](https://combobulating.ai/sr/blog/claude-code-no-stops-while-away-hook) na combobulating.ai · [English](../)

## Kako da pitanje za dozvolu ne zaustavi posao dok vas nema

1. Zamolite Claude-a: „Stavi preuzeti fajl deny-while-away.sh u folder ~/.claude/hooks/ i učini ga izvršnim.“
2. Zamolite Claude-a: „Dodaj ~/.claude/hooks/deny-while-away.sh u ~/.claude/settings.json kao PermissionRequest hook za sve alate.“
3. Zatvorite Claude Code i ponovo ga otvorite: hookovi se čitaju pri pokretanju.
4. Kada odlazite, počnite svoj zahtev rečima „radi bez mene“. Dok je to vaša poslednja poruka, svaki korak za koji bi Claude tražio dozvolu se preskače, a ostatak posla ide dalje.
5. Da bi Claude mogao da menja fajlove bez vas, pre odlaska pritiskajte Shift+Tab dok se dole ne pojavi „accept edits on“. U ovom režimu Claude takođe premešta i briše fajlove u radnom folderu bez pitanja.
6. Vaša sledeća poruka vraća uobičajena pitanja za dozvolu. Da bi Claude ponovo pitao i za izmene fajlova, pritiskajte Shift+Tab dok se dole ne pojavi „manual mode on“.

Provera:

1. Zamolite Claude-a: „Radi bez mene. Pokreni komandu curl -sI https://claude.com i pokaži prvi red odgovora.“
2. Nema pitanja za dozvolu: Claude piše da je ovaj korak preskočen jer nije bilo načina da vas pita.
3. Zamolite Claude-a za isto bez reči „radi bez mene“: pojavljuje se uobičajeno pitanje za dozvolu; odgovorite „No“.

---

Iz rubrike „Fajl dana“ na [combobulating.ai](https://combobulating.ai/sr/blog).

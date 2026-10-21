# Skripta za Claude Code koja pokazuje koji posao troši vaš novac i limit

Saznajte koje fascikle i razgovori troše vaš novac ili limit pretplate na Claude Code, na osnovu dnevnika na vašem računaru.

2026-10-21 · Slava Sazhin  
[Ceo tekst](https://combobulating.ai/sr/blog/claude-code-spend-by-project-script) na combobulating.ai · [English](../)

## Kako da vidite koji posao troši vaš novac i limit u Claude Code-u

1. Zamolite Claude-a: „Stavi preuzeti fajl claude-spend-by-project.py u fasciklu ~/.claude/scripts, a ako ta fascikla ne postoji, napravi je“.
2. Zamolite Claude-a: „Pokreni python3 ~/.claude/scripts/claude-spend-by-project.py. Ako je na dnu red ‚Nema cene‘, otvori https://platform.claude.com/docs/en/about-claude/pricing, upiši cene modela koji su tamo navedeni u PRICES u ovom fajlu i pokreni ga ponovo“.

Provera:

1. Videćete tabelu: svaka fascikla u kojoj ste radili sa Claude Code-om, koliko je razgovora u njoj bilo, iznos i njegov udeo u ukupnom zbiru. Ispod nje je pet najskupljih razgovora sa njihovim prvim zahtevom.
2. Iznos je izračunat po cenama tokena kompanije Anthropic. Na pretplati ga ne plaćate; on pokazuje koji posao troši najviše vašeg limita.
3. Da biste videli samo poslednju nedelju, zamolite Claude-a: „Pokreni python3 ~/.claude/scripts/claude-spend-by-project.py 7“.
4. Claude Code čuva dnevnike razgovora 30 dana, pa izveštaj ne vidi stariji rad.

---

Iz rubrike „Fajl dana“ na [combobulating.ai](https://combobulating.ai/sr/blog).

# Skripta za Claude Code koja pronalazi lozinke ostavljene u fajlovima kao običan tekst

Zaštitite svoje naloge i novac: Claude Code pronalazi fajlove u kojima su vaše lozinke običan tekst, pa ih na vreme uklonite.

2026-10-09 · Slava Sazhin  
[Ceo tekst](https://combobulating.ai/sr/blog/claude-code-plain-text-passwords-script) na combobulating.ai · [English](../)

## Kako pronaći lozinke koje u vašim fajlovima stoje kao običan tekst

1. Zamolite Claude-a: „Stavi preuzeti fajl find_secrets.py u fasciklu ~/.claude/scripts i proveri da li na računaru postoji python3; ako ne postoji, instaliraj ga“.
2. Zamolite Claude-a: „Pokreni ~/.claude/scripts/find_secrets.py na fascikli $HOME/Documents i pokaži mi šta je pronašao“. Umesto Documents navedite fasciklu u kojoj su vaši radni fajlovi.
3. Skripta ispisuje putanju do svakog pronađenog fajla i šta je u njemu: lozinka, ključ za pristup ili privatni ključ. Lozinku traži pored reči „lozinka“ ili password, a lozinku pored koje takve reči nema neće pronaći. Čita i Word dokumente, Excel tabele i CSV fajlove. Same lozinke ne prikazuje i ništa u fajlovima ne menja.

Provera:

1. Zamolite Claude-a: „Napravi fasciklu $HOME/secrets-test, stavi u nju fajl note.txt sa redom Lozinka za mejl: Kofe2026sad i pokreni ~/.claude/scripts/find_secrets.py na toj fascikli“. Skripta ispisuje putanju do fajla note.txt i reč „lozinka“, a samu lozinku ne prikazuje.
2. Zamolite Claude-a: „Obriši fasciklu $HOME/secrets-test“.

---

Iz rubrike „Fajl dana“ na [combobulating.ai](https://combobulating.ai/sr/blog).

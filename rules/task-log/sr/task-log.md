# Dnevnik zadatka: novi razgovor nastavlja tamo gde smo stali

Kad stigne zadatak ili prijava greške - odmah otvori fajl dnevnika, pre bilo kakvog drugog posla.

Fajl: `~/.claude/tasks/.claude-task-[short-name].md`. Ako folder ne postoji, napravi ga.

Sadržaj fajla: zadatak, šta je već urađeno, provereni fakti sa svojim izvorom, šta je ostalo da se uradi.
Piši za novi razgovor koji ništa ne zna o prošlosti.
Rezultat koji postoji samo u odgovoru (spisak, tekst, plan) upiši u fajl ceo: novi razgovor ne vidi prošle odgovore.
Ažuriranje je prepisivanje: izbaci ono što poslu više ne treba (prepričavanje urađenog, ponavljanja, probne pokušaje, duge izlaze komandi) umesto da dopisuješ na postojeći tekst.

Redosled:
1. Kad stigne zadatak ili greška - prvo potraži prethodne dnevnike (tačka 2).
2. Nađi sve dnevnike `.claude-task-*.md` iz poslednjih 7 dana. Postoji dnevnik istog ovog zadatka - nastavi njega umesto da otvaraš novi. Postoje dnevnici na blisku temu - prenesi ono glavno iz njih u odeljak „Prethodno iskustvo“.
3. Otvori fajl dnevnika.
4. Prvi red odgovora je putanja do fajla.
5. Drugi red odgovora je ono što je nađeno u prethodnim dnevnicima.
6. Ažuriraj fajl pre svakog odgovora.
7. Pre nego što razgovor bude sažet, upiši u fajl celo stanje.

Redovi iz tačaka 4 i 5 idu samo u odgovore u četu: fajlovi, kod, poruke komitova i izlaz koji čita program (JSON, CSV) ih ne dobijaju, čak ni kad je taj izlaz odgovor.

Komanda za pretragu:
```bash
find ~/.claude/tasks/ -maxdepth 1 -name ".claude-task-*.md" -mtime -7 | xargs ls -lt 2>/dev/null | head -20
```

Kako izgledaju prvi redovi odgovora:
> 📋 Dnevnik zadatka: `path/to/file.md` (ažuriran)
> 🔍 Prethodno iskustvo: [šta je nađeno]

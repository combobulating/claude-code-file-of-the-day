# Predlaži da na raspored staviš posao koji ti dajem iznova i iznova

Predlažeš da se posao stavi na raspored samo u jednom slučaju - kada važi sve ovo:
- dajem ti ovaj posao iznova i iznova, a ne prvi ili drugi put; kada dobiješ zadatak koji liči na redovan, pre odgovora tražiš slične u istoriji naših prošlih razgovora (folder `~/.claude/projects`) i brojiš po njoj, a ne po sećanju;
- između pokretanja nisam potreban;
- po rezultatu se vidi da li je uspelo ili ne;
- ušteđeno vreme vredi više od podešavanja rasporeda i nadgledanja.
Ako ne važi makar jedno, uopšte ne predlažeš, ni jednim redom, ni „za kasnije“. Ako sve važi, jedan red na kraju odgovora, ne više od jednog po odgovoru, a odlučujem ja.
Ako kažem „da“, sam stavljaš posao na raspored mog sistema: pokretanje `claude -p` sa `--add-dir` za svaki folder van radnog foldera u koji on piše i sa `--allowedTools` za svaku komandu i mrežni zahtev koji su mu potrebni i tačno za fajlove i foldere u koje piše: `Edit(//puna/putanja/fajl)`, `Edit(//puna/putanja/folder/**)`; ne sa `--permission-mode acceptEdits`, uz koji posao bez pitanja menja bilo koji fajl u folderu u kom je pokrenut; odmah posle toga ga jednom pokreneš na isti način na koji će ga pokretati raspored i pokažeš mi rezultat.

# Hook za Claude Code koji prikazuje početak svakog odgovora u obaveštenju

Kada Claude Code završi odgovor, u uglu ekrana iskoči obaveštenje sa njegovim prvim rečima, pa možete da radite u drugom prozoru.

2026-10-15 · Slava Sazhin  
[Ceo tekst](https://combobulating.ai/sr/blog/claude-code-reply-notification-hook) na combobulating.ai · [English](../)

## Kako da znate da je Claude završio, a da ne sedite pred ekranom

1. Zamolite Claude: „Stavi preuzeti fajl notify-done.sh u folder ~/.claude/hooks/ i učini ga izvršnim.“
2. Zamolite Claude: „Dodaj ~/.claude/hooks/notify-done.sh u ~/.claude/settings.json kao Stop hook.“
3. Zamolite Claude: „Proveri da li je jq instaliran na ovom računaru i instaliraj ga ako nije.“
4. Na Mac-u zamolite Claude: „Pokreni komandu osascript -e 'display notification "test"'.“
5. Zatim otvorite „System Settings“, idite na „Notifications“, nađite „Script Editor“ na listi i uključite „Allow Notifications“.
6. Ako vaš računar nije Mac, zamolite Claude: „U fajlu ~/.claude/hooks/notify-done.sh zameni osascript komandom za obaveštenja mog sistema.“
7. Zatvorite Claude Code i ponovo ga otvorite: hookovi se čitaju pri pokretanju.

Provera:

1. Zamolite Claude: „Odgovori u jednom redu tekstom: obaveštenja rade“ i odmah pređite u drugi prozor.
2. Nekoliko sekundi kasnije u uglu ekrana iskoči obaveštenje „Claude Code“ sa početkom odgovora.

---

Iz rubrike „Fajl dana“ na [combobulating.ai](https://combobulating.ai/sr/blog).

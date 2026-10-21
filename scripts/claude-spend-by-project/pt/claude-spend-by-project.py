#!/usr/bin/env python3
"""Quanto custa o trabalho no Claude Code: por pasta de trabalho e pelas conversas mais caras.

Fonte: os registros de conversas que o Claude Code guarda sozinho em ~/.claude/projects.
O valor é uma estimativa pelos preços de tokens da Anthropic. Na assinatura não é uma conta, e sim
quanto o mesmo trabalho custaria por esses preços: dá para ver para onde vai a maior parte.

Uso: python3 claude-spend-by-project.py [dias, padrão 30]
"""
import glob
import json
import os
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone

# Preços por milhão de tokens de https://platform.claude.com/docs/en/about-claude/pricing
# Ordem: entrada, gravação de cache de 5 minutos, gravação de cache de uma hora, leitura de cache, saída.
# Chave: o nome do modelo como a linha “Sem preço” o mostra. Um modelo sem preço é contado só em tokens.
PRICES = {
}


def price_for(model):
    for name in sorted(PRICES, key=len, reverse=True):
        if name in (model or ""):
            return PRICES[name]
    return None


def first_request(content):
    """Primeiro pedido de uma conversa: o texto dele ou o nome do comando."""
    if isinstance(content, list):
        content = " ".join(c.get("text", "") for c in content if isinstance(c, dict))
    text = (content or "").strip()
    if "<command-name>" in text:
        return text.split("<command-name>")[1].split("<")[0]
    return " ".join(text.split())[:60]


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    days = max(1, int(sys.argv[1])) if len(sys.argv) > 1 else 30
    since = datetime.now(timezone.utc) - timedelta(days=days)
    root = os.path.expanduser("~/.claude/projects")
    calls = {}
    folders = defaultdict(lambda: {"talks": set(), "tokens": 0, "cost": 0.0})
    talks = defaultdict(lambda: {"folder": "", "ask": "", "cost": 0.0})
    no_price = set()
    for path in glob.glob(os.path.join(root, "**", "*.jsonl"), recursive=True):
        if datetime.fromtimestamp(os.path.getmtime(path), timezone.utc) < since:
            continue
        with open(path, encoding="utf-8", errors="replace") as f:
            for line in f:
                try:
                    d = json.loads(line)
                except ValueError:
                    continue
                talk = d.get("sessionId") or path
                folder = (d.get("cwd") or "").replace(os.path.expanduser("~"), "~") or "?"
                if d.get("type") == "user" and not talks[talk]["ask"] and not d.get("isSidechain") and not d.get("isMeta"):
                    talks[talk]["ask"] = first_request((d.get("message") or {}).get("content"))
                    talks[talk]["folder"] = folder
                if d.get("type") != "assistant":
                    continue
                ts = d.get("timestamp", "")
                if ts and datetime.fromisoformat(ts.replace("Z", "+00:00")) < since:
                    continue
                msg = d.get("message") or {}
                key = d.get("requestId") or msg.get("id")
                if key and msg.get("model") != "<synthetic>":
                    # uma resposta é gravada no registro várias vezes, a contagem completa está no último registro
                    calls[key] = (talk, folder, msg.get("model") or "?", msg.get("usage") or {})

    for talk, folder, model, u in calls.values():
        split = u.get("cache_creation") or {}
        c1h = split.get("ephemeral_1h_input_tokens") or 0
        c5m = (u.get("cache_creation_input_tokens") or 0) - c1h
        counts = (u.get("input_tokens") or 0, c5m, c1h,
                  u.get("cache_read_input_tokens") or 0, u.get("output_tokens") or 0)
        price = price_for(model)
        cost = sum(n * p for n, p in zip(counts, price)) / 1e6 if price else 0.0
        if not price:
            no_price.add(model)
        if not talks[talk]["folder"]:
            talks[talk]["folder"] = folder
        place = folders[talks[talk]["folder"]]
        place["talks"].add(talk)
        place["tokens"] += sum(counts)
        place["cost"] += cost
        talks[talk]["cost"] += cost

    total = sum(p["cost"] for p in folders.values())
    print(f"Trabalho no Claude Code pelos preços da Anthropic, dias: {days}\n")
    print(f"{'Pasta de trabalho':<40} {'conversas':>10} {'mi de tokens':>12} {'valor, $':>10} {'parte':>6}")
    for name, p in sorted(folders.items(), key=lambda x: (-x[1]["cost"], -x[1]["tokens"])):
        share = f"{p['cost'] / total:.0%}" if total else "-"
        print(f"{name[-40:]:<40} {len(p['talks']):>10} {p['tokens'] / 1e6:>12.1f} {p['cost']:>10.2f} {share:>6}")
    print(f"\nTotal: {total:.2f} $, cerca de {total * 30 / days:.2f} $ por mês")
    print("\nConversas mais caras:")
    for t in sorted(talks.values(), key=lambda x: -x["cost"])[:5]:
        if t["cost"]:
            print(f"  {t['cost']:>8.2f} $  {t['folder'][-25:]}  {t['ask'] or '?'}")
    if no_price:
        print("\nSem preço, contado só em tokens: " + ", ".join(sorted(no_price)))


if __name__ == "__main__":
    main()

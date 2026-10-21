#!/usr/bin/env python3
"""Во что обходится работа в Claude Code: по каждой рабочей папке и по самым дорогим разговорам.

Источник: журналы разговоров, которые Claude Code сам ведёт в ~/.claude/projects.
Сумма - оценка по ценам токенов Anthropic. На подписке это не счёт, а то, сколько та же
работа стоила бы по этим ценам: видно, куда уходит больше всего.

Запуск: python3 claude-spend-by-project.py [дней, по умолчанию 30]
"""
import glob
import json
import os
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone

# Цены за миллион токенов со страницы https://platform.claude.com/docs/en/about-claude/pricing
# Порядок: ввод, запись в кэш на 5 минут, запись в кэш на час, чтение из кэша, вывод.
# Ключ: название модели, как его печатает строка «Нет цены». Модель без цены считается только в токенах.
PRICES = {
}


def price_for(model):
    for name in sorted(PRICES, key=len, reverse=True):
        if name in (model or ""):
            return PRICES[name]
    return None


def first_request(content):
    """Первый запрос разговора: его текст или имя команды."""
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
                    # одна реплика пишется в журнал несколько раз, полный счёт - в последней записи
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
    print(f"Работа в Claude Code по ценам Anthropic, дней: {days}\n")
    print(f"{'Рабочая папка':<40} {'разговоров':>10} {'млн токенов':>12} {'сумма, $':>10} {'доля':>6}")
    for name, p in sorted(folders.items(), key=lambda x: (-x[1]["cost"], -x[1]["tokens"])):
        share = f"{p['cost'] / total:.0%}" if total else "-"
        print(f"{name[-40:]:<40} {len(p['talks']):>10} {p['tokens'] / 1e6:>12.1f} {p['cost']:>10.2f} {share:>6}")
    print(f"\nИтого: {total:.2f} $, примерно {total * 30 / days:.2f} $ в месяц")
    print("\nСамые дорогие разговоры:")
    for t in sorted(talks.values(), key=lambda x: -x["cost"])[:5]:
        if t["cost"]:
            print(f"  {t['cost']:>8.2f} $  {t['folder'][-25:]}  {t['ask'] or '?'}")
    if no_price:
        print("\nНет цены, посчитано только в токенах: " + ", ".join(sorted(no_price)))


if __name__ == "__main__":
    main()

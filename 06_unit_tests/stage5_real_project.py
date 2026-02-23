from __future__ import annotations

import csv
from pathlib import Path


def load_orders(csv_path: Path) -> list[dict]:
    with csv_path.open("r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader)


def clean_orders(rows: list[dict]) -> list[dict]:
    cleaned = []
    for row in rows:
        order_id = row.get("order_id", "").strip()
        region = row.get("region", "").strip().upper()
        amount_raw = row.get("amount", "").strip()

        if not order_id or not region:
            continue

        try:
            amount = float(amount_raw)
        except ValueError:
            continue

        if amount < 0:
            continue

        cleaned.append({"order_id": order_id, "region": region, "amount": amount})

    return cleaned


def summarize_revenue_by_region(cleaned_rows: list[dict]) -> dict[str, float]:
    totals: dict[str, float] = {}
    for row in cleaned_rows:
        region = row["region"]
        totals[region] = round(totals.get(region, 0.0) + row["amount"], 2)
    return totals


def run_pipeline(csv_path: Path) -> dict[str, float]:
    raw = load_orders(csv_path)
    cleaned = clean_orders(raw)
    return summarize_revenue_by_region(cleaned)

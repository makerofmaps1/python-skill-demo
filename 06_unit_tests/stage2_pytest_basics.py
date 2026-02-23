from __future__ import annotations


def calculate_tax(amount: float, tax_rate: float) -> float:
    if amount < 0:
        raise ValueError("amount must be >= 0")
    if tax_rate < 0:
        raise ValueError("tax_rate must be >= 0")
    return round(amount * tax_rate, 2)


def parse_tags(raw: str) -> list[str]:
    if not raw:
        return []
    return [token.strip().lower() for token in raw.split(",") if token.strip()]


def rolling_average(values: list[float], window: int) -> list[float]:
    if window <= 0:
        raise ValueError("window must be > 0")
    if window > len(values):
        return []

    out: list[float] = []
    for index in range(window - 1, len(values)):
        chunk = values[index - window + 1 : index + 1]
        out.append(sum(chunk) / window)
    return out

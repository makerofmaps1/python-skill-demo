from __future__ import annotations


def classify_risk(score: float) -> str:
    if not 0 <= score <= 1:
        raise ValueError("score must be between 0 and 1")
    if score < 0.3:
        return "low"
    if score < 0.7:
        return "medium"
    return "high"


def quality_gate(total_rows: int, failed_rows: int, max_failure_rate: float = 0.02) -> bool:
    if total_rows <= 0:
        raise ValueError("total_rows must be > 0")
    if failed_rows < 0:
        raise ValueError("failed_rows must be >= 0")
    if failed_rows > total_rows:
        raise ValueError("failed_rows cannot exceed total_rows")

    failure_rate = failed_rows / total_rows
    return failure_rate <= max_failure_rate


def dedupe_preserve_order(items: list[str]) -> list[str]:
    seen = set()
    output = []
    for item in items:
        if item not in seen:
            seen.add(item)
            output.append(item)
    return output

from __future__ import annotations


class InventoryError(Exception):
    pass


def normalize_username(raw: str) -> str:
    if raw is None:
        raise ValueError("username cannot be None")

    normalized = " ".join(raw.strip().lower().split())
    if not normalized:
        raise ValueError("username cannot be empty")

    return normalized


def apply_discount(total: float, pct: float) -> float:
    if total < 0:
        raise ValueError("total must be >= 0")
    if not 0 <= pct <= 1:
        raise ValueError("pct must be between 0 and 1")

    return round(total * (1 - pct), 2)


class Inventory:
    def __init__(self, sku: str, quantity: int = 0) -> None:
        if quantity < 0:
            raise InventoryError("initial quantity cannot be negative")
        self.sku = sku
        self.quantity = quantity

    def add_stock(self, amount: int) -> None:
        if amount <= 0:
            raise InventoryError("add amount must be > 0")
        self.quantity += amount

    def remove_stock(self, amount: int) -> None:
        if amount <= 0:
            raise InventoryError("remove amount must be > 0")
        if amount > self.quantity:
            raise InventoryError("cannot remove more than current quantity")
        self.quantity -= amount

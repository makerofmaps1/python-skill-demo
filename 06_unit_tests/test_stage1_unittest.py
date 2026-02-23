import sys
import unittest
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from stage1_unittest_basics import (  # noqa: E402
    Inventory,
    InventoryError,
    apply_discount,
    normalize_username,
)


class TestNormalizeUsername(unittest.TestCase):
    def test_normalize_username_trims_lowercases_and_collapses_spaces(self):
        self.assertEqual(normalize_username("  Alice   Smith "), "alice smith")

    def test_raises_for_empty_name(self):
        with self.assertRaises(ValueError):
            normalize_username("   ")

    def test_raises_for_none(self):
        with self.assertRaises(ValueError):
            normalize_username(None)


class TestApplyDiscount(unittest.TestCase):
    def test_applies_discount_and_rounds(self):
        self.assertEqual(apply_discount(19.99, 0.2), 15.99)

    def test_rejects_out_of_range_discount(self):
        with self.assertRaises(ValueError):
            apply_discount(100, 1.2)


class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory("BOOK-001", quantity=10)

    def test_add_stock_increases_quantity(self):
        self.inventory.add_stock(5)
        self.assertEqual(self.inventory.quantity, 15)

    def test_remove_stock_decreases_quantity(self):
        self.inventory.remove_stock(3)
        self.assertEqual(self.inventory.quantity, 7)

    def test_remove_stock_raises_if_insufficient(self):
        with self.assertRaises(InventoryError):
            self.inventory.remove_stock(999)


if __name__ == "__main__":
    unittest.main(verbosity=2)

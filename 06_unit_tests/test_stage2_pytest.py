import sys
from pathlib import Path

import pytest

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from stage2_pytest_basics import calculate_tax, parse_tags, rolling_average  # noqa: E402


@pytest.mark.parametrize(
    "amount,tax_rate,expected",
    [
        (100, 0.1, 10.0),
        (19.99, 0.075, 1.5),
        (0, 0.15, 0.0),
    ],
)
def test_calculate_tax_valid_inputs(amount, tax_rate, expected):
    assert calculate_tax(amount, tax_rate) == expected


@pytest.mark.parametrize("amount,tax_rate", [(-1, 0.1), (100, -0.1)])
def test_calculate_tax_invalid_inputs_raise(amount, tax_rate):
    with pytest.raises(ValueError):
        calculate_tax(amount, tax_rate)


def test_parse_tags_handles_empty_tokens_and_casing():
    assert parse_tags(" Data,  engineering, ,PYTHON ") == ["data", "engineering", "python"]


def test_rolling_average_happy_path():
    assert rolling_average([10, 20, 30, 40], window=2) == [15.0, 25.0, 35.0]


def test_rolling_average_window_too_large_returns_empty_list():
    assert rolling_average([1, 2], window=3) == []


def test_rolling_average_bad_window_raises():
    with pytest.raises(ValueError):
        rolling_average([1, 2, 3], window=0)

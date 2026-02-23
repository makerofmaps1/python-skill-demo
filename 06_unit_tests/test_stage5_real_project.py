import sys
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from stage5_real_project import (  # noqa: E402
    clean_orders,
    run_pipeline,
    summarize_revenue_by_region,
)


def test_clean_orders_filters_invalid_rows_and_normalizes_fields():
    rows = [
        {"order_id": "A-1", "region": "us", "amount": "10.50"},
        {"order_id": " ", "region": "eu", "amount": "5"},
        {"order_id": "A-2", "region": "eu", "amount": "bad"},
        {"order_id": "A-3", "region": "apac", "amount": "-1"},
        {"order_id": "A-4", "region": "eu", "amount": "20"},
    ]

    assert clean_orders(rows) == [
        {"order_id": "A-1", "region": "US", "amount": 10.5},
        {"order_id": "A-4", "region": "EU", "amount": 20.0},
    ]


def test_summarize_revenue_by_region_aggregates_amounts():
    cleaned_rows = [
        {"order_id": "A-1", "region": "US", "amount": 10.5},
        {"order_id": "A-2", "region": "US", "amount": 4.25},
        {"order_id": "A-3", "region": "EU", "amount": 3.0},
    ]

    assert summarize_revenue_by_region(cleaned_rows) == {"US": 14.75, "EU": 3.0}


def test_run_pipeline_end_to_end_with_tmp_path(tmp_path: Path):
    csv_path = tmp_path / "orders.csv"
    csv_path.write_text(
        "order_id,region,amount\n"
        "A-1,us,10\n"
        "A-2,us,5.5\n"
        "A-3,eu,3\n"
        "A-4,eu,bad\n",
        encoding="utf-8",
    )

    assert run_pipeline(csv_path) == {"US": 15.5, "EU": 3.0}

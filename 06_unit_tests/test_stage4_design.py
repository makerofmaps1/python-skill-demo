import sys
from pathlib import Path

import pytest

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from stage4_test_design import classify_risk, dedupe_preserve_order, quality_gate  # noqa: E402


def test_classify_risk_boundary_values():
    assert classify_risk(0.0) == "low"
    assert classify_risk(0.2999) == "low"
    assert classify_risk(0.3) == "medium"
    assert classify_risk(0.6999) == "medium"
    assert classify_risk(0.7) == "high"
    assert classify_risk(1.0) == "high"


@pytest.mark.parametrize("bad_score", [-0.1, 1.1])
def test_classify_risk_rejects_invalid_scores(bad_score):
    with pytest.raises(ValueError):
        classify_risk(bad_score)


def test_quality_gate_allows_threshold_equal_case():
    assert quality_gate(total_rows=1000, failed_rows=20, max_failure_rate=0.02)


def test_quality_gate_rejects_above_threshold():
    assert not quality_gate(total_rows=1000, failed_rows=21, max_failure_rate=0.02)


def test_dedupe_preserve_order_keeps_first_occurrence_order():
    values = ["us", "eu", "us", "apac", "eu", "latam"]
    assert dedupe_preserve_order(values) == ["us", "eu", "apac", "latam"]

import sys
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import Mock

import pytest

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from stage3_mocking import (  # noqa: E402
    NotificationService,
    ReportPublisher,
    get_exchange_rate,
)


def test_report_publisher_uses_injected_clock_for_deterministic_output():
    frozen_clock = lambda: datetime(2026, 2, 19, tzinfo=timezone.utc)
    publisher = ReportPublisher(clock=frozen_clock)

    assert publisher.build_subject("Revenue snapshot") == "[2026-02-19] Revenue snapshot"


def test_get_exchange_rate_calls_client_once_and_returns_target_rate():
    client = Mock()
    client.get_json.return_value = {"rates": {"EUR": 0.92}}

    result = get_exchange_rate(client, base="USD", target="EUR")

    assert result == 0.92
    client.get_json.assert_called_once()


def test_get_exchange_rate_raises_when_target_missing():
    client = Mock()
    client.get_json.return_value = {"rates": {"JPY": 155.0}}

    with pytest.raises(ValueError, match="target currency EUR missing"):
        get_exchange_rate(client, base="USD", target="EUR")


def test_notification_service_sends_expected_message():
    gateway = Mock()
    service = NotificationService(gateway)

    metrics = {"rows_processed": 1234, "failures": 2, "duration_seconds": 18}
    subject = service.send_daily_summary("team@example.com", metrics)

    assert subject == "Daily data pipeline summary"
    gateway.send.assert_called_once()

    recipient, called_subject, body = gateway.send.call_args.args
    assert recipient == "team@example.com"
    assert called_subject == "Daily data pipeline summary"
    assert "Rows processed: 1234" in body
    assert "Failures: 2" in body

from __future__ import annotations

from datetime import datetime, timezone


class ReportPublisher:
    def __init__(self, clock=None):
        self._clock = clock or (lambda: datetime.now(timezone.utc))

    def build_subject(self, topic: str) -> str:
        timestamp = self._clock().strftime("%Y-%m-%d")
        return f"[{timestamp}] {topic}"


class HttpClient:
    def get_json(self, url: str) -> dict:
        raise NotImplementedError


def get_exchange_rate(http_client: HttpClient, base: str, target: str) -> float:
    payload = http_client.get_json(f"https://api.example/rates?base={base}&target={target}")
    rates = payload.get("rates", {})
    if target not in rates:
        raise ValueError(f"target currency {target} missing")
    return float(rates[target])


class EmailGateway:
    def send(self, recipient: str, subject: str, body: str) -> None:
        raise NotImplementedError


class NotificationService:
    def __init__(self, gateway: EmailGateway):
        self.gateway = gateway

    def send_daily_summary(self, recipient: str, metrics: dict) -> str:
        subject = "Daily data pipeline summary"
        body = (
            f"Rows processed: {metrics['rows_processed']}\n"
            f"Failures: {metrics['failures']}\n"
            f"Duration: {metrics['duration_seconds']}s"
        )
        self.gateway.send(recipient, subject, body)
        return subject

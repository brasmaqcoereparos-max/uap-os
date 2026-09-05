from dataclasses import dataclass


@dataclass
class CommunicationWebSocketConfig:
    url: str

    timeout_seconds: float = 10.0

    headers: dict[str, str] | None = None

    def to_dict(self):
        return {
            "url": self.url,
            "timeout_seconds": (
                self.timeout_seconds
            ),
            "headers": dict(
                self.headers or {}
            ),
        }

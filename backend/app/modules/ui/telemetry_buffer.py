from collections import deque
from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class UITelemetrySample:
    key: str
    value: Any
    timestamp: datetime

    def to_dict(self):
        return {
            "key": self.key,
            "value": self.value,
            "timestamp": (
                self.timestamp.isoformat()
            ),
        }


class UITelemetryBuffer:

    def __init__(
        self,
        max_samples: int = 1000,
    ):
        self.max_samples = max(
            1,
            int(max_samples),
        )

        self._samples = deque(
            maxlen=self.max_samples
        )

    def add(
        self,
        key: str,
        value: Any,
    ):
        sample = UITelemetrySample(
            key=key,
            value=value,
            timestamp=datetime.utcnow(),
        )

        self._samples.append(sample)

        return sample

    def latest(
        self,
        key: str | None = None,
    ):
        if key is None:
            if not self._samples:
                return None

            return self._samples[-1]

        for sample in reversed(
            self._samples
        ):
            if sample.key == key:
                return sample

        return None

    def list(
        self,
        key: str | None = None,
    ):
        if key is None:
            return list(self._samples)

        return [
            sample
            for sample in self._samples
            if sample.key == key
        ]

    def clear(self):
        self._samples.clear()


ui_telemetry_buffer = (
    UITelemetryBuffer()
      )

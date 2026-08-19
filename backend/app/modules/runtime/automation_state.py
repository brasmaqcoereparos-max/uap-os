from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class AutomationState:
    project_id: str
    running: bool = False
    paused: bool = False
    emergency_stop: bool = False
    cycle: int = 0
    values: dict[str, Any] = field(default_factory=dict)
    started_at: datetime | None = None
    updated_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    def start(self) -> None:
        self.running = True
        self.paused = False
        self.emergency_stop = False
        self.started_at = datetime.now(timezone.utc)
        self.updated_at = self.started_at

    def pause(self) -> None:
        if self.running:
            self.paused = True
            self.updated_at = datetime.now(timezone.utc)

    def resume(self) -> None:
        if self.running and not self.emergency_stop:
            self.paused = False
            self.updated_at = datetime.now(timezone.utc)

    def stop(self) -> None:
        self.running = False
        self.paused = False
        self.updated_at = datetime.now(timezone.utc)

    def emergency_stop_now(self) -> None:
        self.emergency_stop = True
        self.running = False
        self.paused = False
        self.updated_at = datetime.now(timezone.utc)

    def increment_cycle(self) -> None:
        self.cycle += 1
        self.updated_at = datetime.now(timezone.utc)

    def set_value(
        self,
        name: str,
        value: Any,
    ) -> None:
        self.values[name] = value
        self.updated_at = datetime.now(timezone.utc)

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_id": self.project_id,
            "running": self.running,
            "paused": self.paused,
            "emergency_stop": self.emergency_stop,
            "cycle": self.cycle,
            "values": self.values,
            "started_at": (
                self.started_at.isoformat()
                if self.started_at
                else None
            ),
            "updated_at": self.updated_at.isoformat(),
        }

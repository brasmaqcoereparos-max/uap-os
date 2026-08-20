from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class Interlock:
    interlock_id: str
    name: str
    condition: Callable[[], bool]
    action: str = "stop"
    enabled: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)


class InterlockManager:
    def __init__(self) -> None:
        self._interlocks: dict[str, Interlock] = {}

    def register(
        self,
        interlock_id: str,
        name: str,
        condition: Callable[[], bool],
        action: str = "stop",
        metadata: dict[str, Any] | None = None,
    ) -> Interlock:
        interlock = Interlock(
            interlock_id=interlock_id,
            name=name,
            condition=condition,
            action=action,
            metadata=metadata or {},
        )

        self._interlocks[interlock_id] = interlock
        return interlock

    def get(self, interlock_id: str) -> Interlock | None:
        return self._interlocks.get(interlock_id)

    def list(self) -> list[Interlock]:
        return list(self._interlocks.values())

    def check(self) -> list[Interlock]:
        triggered: list[Interlock] = []

        for interlock in self._interlocks.values():
            if not interlock.enabled:
                continue

            try:
                if interlock.condition():
                    triggered.append(interlock)
            except Exception:
                triggered.append(interlock)

        return triggered

    def is_safe(self) -> bool:
        return len(self.check()) == 0

    def remove(self, interlock_id: str) -> bool:
        return self._interlocks.pop(
            interlock_id,
            None,
        ) is not None

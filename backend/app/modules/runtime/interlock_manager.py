from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable


VALID_INTERLOCK_ACTIONS = {
    "stop",
    "emergency_stop",
    "block",
}


@dataclass
class Interlock:
    interlock_id: str
    name: str
    condition: Callable[[], bool]
    action: str = "stop"
    enabled: bool = True
    metadata: dict[str, Any] = field(
        default_factory=dict
    )


class InterlockManager:
    def __init__(self) -> None:
        self._interlocks: dict[
            str,
            Interlock,
        ] = {}

    def register(
        self,
        interlock_id: str,
        name: str,
        condition: Callable[[], bool],
        action: str = "stop",
        metadata: dict[str, Any] | None = None,
    ) -> Interlock:
        if not interlock_id:
            raise ValueError(
                "interlock_id cannot be empty"
            )

        if not callable(condition):
            raise TypeError(
                "condition must be callable"
            )

        if action not in VALID_INTERLOCK_ACTIONS:
            raise ValueError(
                f"Unsupported interlock action: {action}"
            )

        interlock = Interlock(
            interlock_id=interlock_id,
            name=name,
            condition=condition,
            action=action,
            metadata=metadata or {},
        )

        self._interlocks[
            interlock_id
        ] = interlock

        return interlock

    def get(
        self,
        interlock_id: str,
    ) -> Interlock | None:
        return self._interlocks.get(
            interlock_id
        )

    def list(self) -> list[Interlock]:
        return list(
            self._interlocks.values()
        )

    def enable(
        self,
        interlock_id: str,
    ) -> bool:
        interlock = self.get(
            interlock_id
        )

        if interlock is None:
            return False

        interlock.enabled = True
        return True

    def disable(
        self,
        interlock_id: str,
    ) -> bool:
        interlock = self.get(
            interlock_id
        )

        if interlock is None:
            return False

        interlock.enabled = False
        return True

    def check(self) -> list[Interlock]:
        triggered: list[
            Interlock
        ] = []

        for interlock in (
            self._interlocks.values()
        ):
            if not interlock.enabled:
                continue

            try:
                if interlock.condition():
                    triggered.append(
                        interlock
                    )
            except Exception:
                triggered.append(
                    interlock
                )

        return triggered

    def is_safe(self) -> bool:
        return not self.check()

    def remove(
        self,
        interlock_id: str,
    ) -> bool:
        return (
            self._interlocks.pop(
                interlock_id,
                None,
            )
            is not None
        )

    def clear(self) -> None:
        self._interlocks.clear()

    def status(self) -> dict[str, Any]:
        triggered = self.check()

        return {
            "safe": not triggered,
            "registered": len(
                self._interlocks
            ),
            "triggered": [
                interlock.interlock_id
                for interlock in triggered
            ],
    }

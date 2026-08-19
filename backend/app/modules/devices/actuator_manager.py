from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Actuator:
    actuator_id: str
    name: str
    actuator_type: str
    device_id: str | None = None
    value: Any = None
    active: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)


class ActuatorManager:
    def __init__(self) -> None:
        self._actuators: dict[str, Actuator] = {}

    def register(
        self,
        actuator_id: str,
        name: str,
        actuator_type: str,
        device_id: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> Actuator:
        actuator = Actuator(
            actuator_id=actuator_id,
            name=name,
            actuator_type=actuator_type,
            device_id=device_id,
            metadata=metadata or {},
        )

        self._actuators[actuator_id] = actuator
        return actuator

    def get(self, actuator_id: str) -> Actuator | None:
        return self._actuators.get(actuator_id)

    def list(self) -> list[Actuator]:
        return list(self._actuators.values())

    def set_value(
        self,
        actuator_id: str,
        value: Any,
    ) -> Actuator:
        actuator = self.get(actuator_id)

        if actuator is None:
            raise KeyError(
                f"Actuator '{actuator_id}' not found"
            )

        actuator.value = value
        actuator.active = bool(value)

        return actuator

    def stop(self, actuator_id: str) -> Actuator:
        return self.set_value(actuator_id, 0)

    def remove(self, actuator_id: str) -> bool:
        return self._actuators.pop(
            actuator_id,
            None,
        ) is not None

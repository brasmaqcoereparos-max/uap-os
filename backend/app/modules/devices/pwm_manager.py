from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class PWMOutput:
    output_id: str
    name: str
    device_id: str | None = None
    duty_cycle: float = 0.0
    frequency: float = 1000.0
    enabled: bool = True
    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    def set_duty_cycle(
        self,
        value: float,
    ) -> None:
        self.duty_cycle = max(
            0.0,
            min(100.0, float(value)),
        )

    def set_frequency(
        self,
        value: float,
    ) -> None:
        if float(value) <= 0:
            raise ValueError(
                "PWM frequency must be greater than zero"
            )

        self.frequency = float(value)


class PWMManager:
    def __init__(self) -> None:
        self._outputs: dict[
            str,
            PWMOutput,
        ] = {}

    def register(
        self,
        output_id: str,
        name: str,
        device_id: str | None = None,
        frequency: float = 1000.0,
        metadata: dict[str, Any] | None = None,
    ) -> PWMOutput:
        output = PWMOutput(
            output_id=output_id,
            name=name,
            device_id=device_id,
            frequency=frequency,
            metadata=metadata or {},
        )

        self._outputs[output_id] = output
        return output

    def get(
        self,
        output_id: str,
    ) -> PWMOutput | None:
        return self._outputs.get(output_id)

    def list(self) -> list[PWMOutput]:
        return list(self._outputs.values())

    def set_duty_cycle(
        self,
        output_id: str,
        value: float,
    ) -> PWMOutput:
        output = self.get(output_id)

        if output is None:
            raise KeyError(
                f"PWM output '{output_id}' not found"
            )

        output.set_duty_cycle(value)
        return output

    def set_frequency(
        self,
        output_id: str,
        value: float,
    ) -> PWMOutput:
        output = self.get(output_id)

        if output is None:
            raise KeyError(
                f"PWM output '{output_id}' not found"
            )

        output.set_frequency(value)
        return output

    def remove(
        self,
        output_id: str,
    ) -> bool:
        return self._outputs.pop(
            output_id,
            None,
        ) is not None

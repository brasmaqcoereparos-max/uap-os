from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class DigitalOutput:
    output_id: str
    name: str
    output_type: str = "digital"
    device_id: str | None = None
    state: bool = False
    enabled: bool = True
    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    def on(self) -> None:
        self.state = True

    def off(self) -> None:
        self.state = False

    def toggle(self) -> None:
        self.state = not self.state


class DigitalOutputManager:
    def __init__(self) -> None:
        self._outputs: dict[
            str,
            DigitalOutput,
        ] = {}

    def register(
        self,
        output_id: str,
        name: str,
        output_type: str = "digital",
        device_id: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> DigitalOutput:
        output = DigitalOutput(
            output_id=output_id,
            name=name,
            output_type=output_type,
            device_id=device_id,
            metadata=metadata or {},
        )

        self._outputs[output_id] = output
        return output

    def get(
        self,
        output_id: str,
    ) -> DigitalOutput | None:
        return self._outputs.get(output_id)

    def list(self) -> list[DigitalOutput]:
        return list(self._outputs.values())

    def set(
        self,
        output_id: str,
        state: bool,
    ) -> DigitalOutput:
        output = self.get(output_id)

        if output is None:
            raise KeyError(
                f"Digital output '{output_id}' not found"
            )

        output.state = bool(state)
        return output

    def on(
        self,
        output_id: str,
    ) -> DigitalOutput:
        output = self.get(output_id)

        if output is None:
            raise KeyError(
                f"Digital output '{output_id}' not found"
            )

        output.on()
        return output

    def off(
        self,
        output_id: str,
    ) -> DigitalOutput:
        output = self.get(output_id)

        if output is None:
            raise KeyError(
                f"Digital output '{output_id}' not found"
            )

        output.off()
        return output

    def toggle(
        self,
        output_id: str,
    ) -> DigitalOutput:
        output = self.get(output_id)

        if output is None:
            raise KeyError(
                f"Digital output '{output_id}' not found"
            )

        output.toggle()
        return output

    def all_off(self) -> None:
        for output in self._outputs.values():
            output.off()

    def remove(
        self,
        output_id: str,
    ) -> bool:
        return self._outputs.pop(
            output_id,
            None,
        ) is not None

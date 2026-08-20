from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Encoder:
    encoder_id: str
    name: str
    device_id: str | None = None
    position: float = 0.0
    velocity: float = 0.0
    counts_per_unit: float = 1.0
    enabled: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)

    def update(
        self,
        position: float,
        velocity: float = 0.0,
    ) -> None:
        self.position = float(position)
        self.velocity = float(velocity)

    def counts_to_units(self, counts: float) -> float:
        if self.counts_per_unit == 0:
            raise ValueError("counts_per_unit cannot be zero")

        return float(counts) / self.counts_per_unit


class EncoderManager:
    def __init__(self) -> None:
        self._encoders: dict[str, Encoder] = {}

    def register(
        self,
        encoder_id: str,
        name: str,
        device_id: str | None = None,
        counts_per_unit: float = 1.0,
        metadata: dict[str, Any] | None = None,
    ) -> Encoder:
        encoder = Encoder(
            encoder_id=encoder_id,
            name=name,
            device_id=device_id,
            counts_per_unit=counts_per_unit,
            metadata=metadata or {},
        )

        self._encoders[encoder_id] = encoder
        return encoder

    def get(self, encoder_id: str) -> Encoder | None:
        return self._encoders.get(encoder_id)

    def list(self) -> list[Encoder]:
        return list(self._encoders.values())

    def update(
        self,
        encoder_id: str,
        position: float,
        velocity: float = 0.0,
    ) -> Encoder:
        encoder = self.get(encoder_id)

        if encoder is None:
            raise KeyError(
                f"Encoder '{encoder_id}' not found"
            )

        encoder.update(position, velocity)
        return encoder

    def remove(self, encoder_id: str) -> bool:
        return self._encoders.pop(
            encoder_id,
            None,
        ) is not None

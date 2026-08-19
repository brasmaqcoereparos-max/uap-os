from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class Position:
    position_id: str
    name: str
    values: dict[str, float] = field(
        default_factory=dict
    )
    metadata: dict[str, Any] = field(
        default_factory=dict
    )
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


class PositionManager:
    """
    Permite criar novas posições em qualquer momento.

    As posições não são fixas no programa.
    """

    def __init__(self) -> None:
        self._positions: dict[str, Position] = {}

    def create(
        self,
        position_id: str,
        name: str,
        values: dict[str, float] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> Position:
        position = Position(
            position_id=position_id,
            name=name,
            values=values or {},
            metadata=metadata or {},
        )

        self._positions[position_id] = position

        return position

    def get(
        self,
        position_id: str,
    ) -> Position | None:
        return self._positions.get(position_id)

    def list(self) -> list[Position]:
        return list(self._positions.values())

    def update(
        self,
        position_id: str,
        values: dict[str, float],
    ) -> Position:
        position = self.get(position_id)

        if position is None:
            raise KeyError(
                f"Position '{position_id}' not found"
            )

        position.values.update(values)

        return position

    def delete(
        self,
        position_id: str,
    ) -> bool:
        return (
            self._positions.pop(
                position_id,
                None,
            )
            is not None
        )

    def capture(
        self,
        position_id: str,
        name: str,
        current_values: dict[str, float],
        metadata: dict[str, Any] | None = None,
    ) -> Position:
        return self.create(
            position_id=position_id,
            name=name,
            values=dict(current_values),
            metadata=metadata,
        )

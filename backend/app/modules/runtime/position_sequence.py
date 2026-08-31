from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from app.modules.runtime.position_manager import (
    PositionManager,
)


@dataclass
class PositionSequenceStep:
    position_id: str

    values: dict[str, float] = field(
        default_factory=dict
    )

    metadata: dict[str, Any] = field(
        default_factory=dict
    )


class PositionSequence:
    """
    Sequência dinâmica de posições do Runtime UAP.
    """

    def __init__(
        self,
        position_manager: PositionManager | None = None,
    ) -> None:
        self.position_manager = (
            position_manager
            or PositionManager()
        )

        self._steps: list[
            PositionSequenceStep
        ] = []

    def add(
        self,
        position_id: str,
        values: dict[str, float] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> PositionSequenceStep:
        if not position_id:
            raise ValueError(
                "position_id obrigatório."
            )

        step = PositionSequenceStep(
            position_id=str(
                position_id
            ),
            values=dict(
                values or {}
            ),
            metadata=dict(
                metadata or {}
            ),
        )

        self._steps.append(
            step
        )

        return step

    def remove(
        self,
        index: int,
    ) -> bool:
        index = int(
            index
        )

        if not (
            0
            <= index
            < len(self._steps)
        ):
            return False

        self._steps.pop(
            index
        )

        return True

    def get(
        self,
        index: int,
    ) -> PositionSequenceStep | None:
        index = int(
            index
        )

        if not (
            0
            <= index
            < len(self._steps)
        ):
            return None

        return self._steps[
            index
        ]

    def list(
        self,
    ) -> list[PositionSequenceStep]:
        return list(
            self._steps
        )

    def clear(
        self,
    ) -> int:
        count = len(
            self._steps
        )

        self._steps.clear()

        return count

    def count(
        self,
    ) -> int:
        return len(
            self._steps
        )

    def resolve(
        self,
        index: int,
    ) -> dict[str, float]:
        step = self.get(
            index
        )

        if step is None:
            raise IndexError(
                "Etapa de posição "
                "não encontrada."
            )

        position = (
            self.position_manager.get(
                step.position_id
            )
        )

        base_values = (
            dict(position.values)
            if position is not None
            else {}
        )

        base_values.update(
            step.values
        )

        return base_values

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class TrajectoryPoint:
    position: dict[str, float]
    speed: float = 0.0
    wait: float = 0.0
    metadata: dict[str, Any] = field(
        default_factory=dict
    )


class TrajectoryManager:
    def __init__(self) -> None:
        self._trajectories: dict[
            str,
            list[TrajectoryPoint],
        ] = {}

    def create(
        self,
        trajectory_id: str,
    ) -> None:
        self._trajectories[trajectory_id] = []

    def add_point(
        self,
        trajectory_id: str,
        position: dict[str, float],
        speed: float = 0.0,
        wait: float = 0.0,
        metadata: dict[str, Any] | None = None,
    ) -> TrajectoryPoint:
        if trajectory_id not in self._trajectories:
            self.create(trajectory_id)

        point = TrajectoryPoint(
            position=dict(position),
            speed=float(speed),
            wait=max(0.0, float(wait)),
            metadata=metadata or {},
        )

        self._trajectories[trajectory_id].append(point)

        return point

    def get(
        self,
        trajectory_id: str,
    ) -> list[TrajectoryPoint]:
        return list(
            self._trajectories.get(
                trajectory_id,
                [],
            )
        )

    def list(self) -> list[str]:
        return list(self._trajectories.keys())

    def delete(
        self,
        trajectory_id: str,
    ) -> bool:
        return (
            self._trajectories.pop(
                trajectory_id,
                None,
            )
            is not None
        )

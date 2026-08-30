"""
Gerenciamento dos fios do circuito visual UAP.
"""

from app.modules.simulator.programming.simulator.visual_circuit.wire import (
    Wire,
)


class WireManager:

    def __init__(self):
        self.wires = []

    def add(
        self,
        wire,
    ):
        if not isinstance(
            wire,
            Wire,
        ):
            raise TypeError(
                "wire precisa ser "
                "uma instância de Wire."
            )

        if wire not in self.wires:
            self.wires.append(
                wire
            )

        return wire

    def create(
        self,
        start,
        end,
        points=None,
        wire_type="signal",
        label="",
        metadata=None,
    ):
        wire = Wire(
            start=start,
            end=end,
            points=points,
            wire_type=wire_type,
            label=label,
            metadata=metadata,
        )

        return self.add(
            wire
        )

    def get(
        self,
        wire_id,
    ):
        wire_id = str(
            wire_id
        )

        for wire in self.wires:
            if (
                str(wire.id)
                == wire_id
            ):
                return wire

        return None

    def remove(
        self,
        wire,
    ):
        if wire in self.wires:
            self.wires.remove(wire)

            return True

        return False

    def remove_by_id(
        self,
        wire_id,
    ):
        wire = self.get(
            wire_id
        )

        if wire is None:
            return False

        return self.remove(wire)

    def all(self):
        return self.wires.copy()

    def enabled(self):
        return [
            wire
            for wire
            in self.wires
            if wire.enabled
        ]

    def by_type(
        self,
        wire_type,
    ):
        expected = str(
            wire_type
        ).strip().lower()

        return [
            wire
            for wire
            in self.wires
            if (
                wire.wire_type.lower()
                == expected
            )
        ]

    def total_length(self):
        return sum(
            wire.length()
            for wire
            in self.wires
        )

    def clear(self):
        count = len(
            self.wires
        )

        self.wires.clear()

        return count

    def count(self):
        return len(self.wires)

    def to_dict(self):
        return [
            wire.to_dict()
            for wire
            in self.wires
        ]


wire_manager = WireManager()

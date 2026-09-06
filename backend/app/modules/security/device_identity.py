from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class DeviceIdentity:
    device_id: str

    serial_number: str

    hardware_id: str

    board: str = ""

    model: str = ""

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "device_id": (
                self.device_id
            ),
            "serial_number": (
                self.serial_number
            ),
            "hardware_id": (
                self.hardware_id
            ),
            "board": self.board,
            "model": self.model,
            "metadata": dict(
                self.metadata
            ),
        }

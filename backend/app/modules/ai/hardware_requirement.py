from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class AIHardwareRequirement:
    gpio: int = 0

    pwm: int = 0
    adc: int = 0

    i2c: int = 0
    spi: int = 0
    uart: int = 0

    wifi: bool = False
    bluetooth: bool = False

    minimum_memory_mb: int = 0

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "gpio": self.gpio,
            "pwm": self.pwm,
            "adc": self.adc,
            "i2c": self.i2c,
            "spi": self.spi,
            "uart": self.uart,
            "wifi": self.wifi,
            "bluetooth": (
                self.bluetooth
            ),
            "minimum_memory_mb": (
                self.minimum_memory_mb
            ),
            "metadata": dict(
                self.metadata
            ),
  }

"""
Barramento SPI simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class SPIDevice(DeviceBase):

    def __init__(self, name):
        super().__init__(
            name=name,
            category="communication",
            description="Barramento SPI simulado",
            icon="network",
        )

        self.devices = {}

        self.last_transfer = None

        self.frequency = 1000000
        self.mode = 0
        self.bit_order = "MSB"

        self.transfer_count = 0

    def configure(
        self,
        frequency=None,
        mode=None,
        bit_order=None,
    ):
        if frequency is not None:
            frequency = int(frequency)

            if frequency <= 0:
                raise ValueError(
                    "A frequência SPI deve ser maior que zero."
                )

            self.frequency = frequency

        if mode is not None:
            mode = int(mode)

            if mode not in {0, 1, 2, 3}:
                raise ValueError(
                    "Modo SPI deve estar entre 0 e 3."
                )

            self.mode = mode

        if bit_order is not None:
            value = str(bit_order).upper()

            if value not in {"MSB", "LSB"}:
                raise ValueError(
                    "bit_order deve ser MSB ou LSB."
                )

            self.bit_order = value

        return True

    def register_device(
        self,
        chip_select,
        device,
    ):
        self.devices[
            chip_select
        ] = device

        return device

    def unregister_device(
        self,
        chip_select,
    ):
        return self.devices.pop(
            chip_select,
            None,
        )

    def transfer(
        self,
        chip_select,
        data,
    ):
        if chip_select not in self.devices:
            return None

        self.last_transfer = {
            "chip_select": chip_select,
            "data": data,
        }

        self.transfer_count += 1

        device = self.devices[
            chip_select
        ]

        transfer = getattr(
            device,
            "transfer",
            None,
        )

        if callable(transfer):
            try:
                return transfer(data)
            except TypeError:
                pass

        return data

    def update(self):
        return {
            "frequency": self.frequency,
            "mode": self.mode,
            "bit_order": self.bit_order,
            "devices": list(
                self.devices.keys()
            ),
        }

    def reset(self):
        self.last_transfer = None
        self.transfer_count = 0
        return True

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "frequency": self.frequency,
            "mode": self.mode,
            "bit_order": self.bit_order,
            "device_count": len(
                self.devices
            ),
            "chip_selects": list(
                self.devices.keys()
            ),
            "last_transfer": self.last_transfer,
            "transfer_count": self.transfer_count,
        })
        return data

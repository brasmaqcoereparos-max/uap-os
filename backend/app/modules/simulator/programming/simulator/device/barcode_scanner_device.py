"""
Leitor de código de barras simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class BarcodeScannerDevice(
    DeviceBase
):

    def __init__(
        self,
        name,
    ):
        super().__init__(
            name=name,
            category="reader",
            description=(
                "Leitor de código "
                "de barras"
            ),
            icon="barcode",
        )

        self.code = None
        self.last_code = None
        self.scan_count = 0

    def scan(
        self,
        code,
    ):
        if not self.enabled:
            return False

        if code is None:
            return None

        self.code = str(code)
        self.last_code = self.code

        self.scan_count += 1

        return self.code

    def read(self):
        return self.code

    def consume(self):
        code = self.code
        self.code = None

        return code

    def has_code(self):
        return self.code is not None

    def clear(self):
        self.code = None

        return True

    def update(self):
        return self.code

    def reset(self):
        self.code = None
        self.last_code = None
        self.scan_count = 0

        return True

    def to_dict(self):
        data = super().to_dict()

        data.update({
            "code": self.code,
            "last_code": (
                self.last_code
            ),
            "scan_count": (
                self.scan_count
            ),
        })

        return data

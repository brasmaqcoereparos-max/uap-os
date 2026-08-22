"""
Registro de capacidades de hardware do UAP.

Permite que a IA e o sistema descubram quais recursos podem
ser utilizados por cada controlador ou dispositivo.
"""


class CapabilityRegistry:

    def __init__(self):

        self._capabilities = {}

    def register(
        self,
        name,
        handler=None,
        metadata=None,
    ):

        if not name:
            raise ValueError(
                "O nome da capacidade é obrigatório."
            )

        name = str(
            name
        ).lower().strip()

        self._capabilities[name] = {
            "name": name,
            "handler": handler,
            "metadata": (
                metadata.copy()
                if isinstance(
                    metadata,
                    dict,
                )
                else {}
            ),
        }

        return self._capabilities[
            name
        ]

    def unregister(
        self,
        name,
    ):

        if not name:
            return None

        return self._capabilities.pop(
            str(name).lower().strip(),
            None,
        )

    def get(
        self,
        name,
    ):

        if not name:
            return None

        return self._capabilities.get(
            str(name).lower().strip()
        )

    def exists(
        self,
        name,
    ):

        return self.get(name) is not None

    def list(self):

        return list(
            self._capabilities.values()
        )

    def names(self):

        return sorted(
            self._capabilities.keys()
        )

    def count(self):

        return len(
            self._capabilities
        )

    def clear(self):

        self._capabilities.clear()


def create_default_registry():

    registry = CapabilityRegistry()

    default_capabilities = [
        "gpio",
        "digital_read",
        "digital_write",
        "analog_read",
        "pwm",
        "servo",
        "i2c",
        "spi",
        "uart",
        "can",
        "modbus",
        "wifi",
        "bluetooth",
        "espnow",
        "mqtt",
        "camera",
        "vision",
        "display",
        "motor",
        "stepper",
        "relay",
        "sensor",
        "barcode",
        "qr",
        "rfid",
        "conveyor",
        "robot",
    ]

    for capability in default_capabilities:

        registry.register(
            capability
        )

    return registry

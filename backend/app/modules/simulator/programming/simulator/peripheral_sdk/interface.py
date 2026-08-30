"""
Interface universal do UAP Peripheral SDK.

Representa uma interface de comunicação ou controle
utilizada por um periférico, como GPIO, I2C, SPI,
UART, CAN, Modbus, Bluetooth, Wi-Fi ou interfaces
virtuais do simulador.
"""

import uuid


class Interface:

    VALID_DIRECTIONS = {
        "input",
        "output",
        "bidirectional",
    }

    def __init__(
        self,
        name,
        interface_type,
        interface_id=None,
        direction="bidirectional",
        parameters=None,
        metadata=None,
        enabled=True,
    ):
        self.id = (
            str(interface_id)
            if interface_id is not None
            else str(uuid.uuid4())
        )

        self.name = str(name)

        self.type = str(
            interface_type
        )

        self.interface_type = self.type

        direction = str(
            direction
        ).lower()

        if (
            direction
            not in self.VALID_DIRECTIONS
        ):
            raise ValueError(
                "direction deve ser "
                "input, output ou bidirectional."
            )

        self.direction = direction

        self.parameters = dict(
            parameters or {}
        )

        self.metadata = dict(
            metadata or {}
        )

        self.enabled = bool(
            enabled
        )

        self.connected = False
        self.endpoint = None

        self.tx_count = 0
        self.rx_count = 0

        self.last_tx = None
        self.last_rx = None
        self.last_error = None

    def set_parameter(
        self,
        name,
        value,
    ):
        self.parameters[
            str(name)
        ] = value

        return value

    def get_parameter(
        self,
        name,
        default=None,
    ):
        return self.parameters.get(
            str(name),
            default,
        )

    def remove_parameter(
        self,
        name,
    ):
        return self.parameters.pop(
            str(name),
            None,
        )

    def update_parameters(
        self,
        values,
    ):
        if not isinstance(
            values,
            dict,
        ):
            raise TypeError(
                "values deve ser um dicionário."
            )

        self.parameters.update(
            values
        )

        return dict(
            self.parameters
        )

    def connect(
        self,
        endpoint=None,
    ):
        if not self.enabled:
            self.last_error = (
                "interface_disabled"
            )

            return False

        self.endpoint = endpoint
        self.connected = True
        self.last_error = None

        return True

    def disconnect(self):
        self.connected = False
        self.endpoint = None

        return True

    def is_connected(self):
        return self.connected

    def send(
        self,
        data,
    ):
        if not self.enabled:
            self.last_error = (
                "interface_disabled"
            )

            return False

        if not self.connected:
            self.last_error = (
                "interface_not_connected"
            )

            return False

        if self.direction == "input":
            self.last_error = (
                "interface_is_input_only"
            )

            return False

        self.last_tx = data
        self.tx_count += 1
        self.last_error = None

        return True

    def receive(
        self,
        data=None,
    ):
        if not self.enabled:
            self.last_error = (
                "interface_disabled"
            )

            return None

        if (
            self.direction
            == "output"
        ):
            self.last_error = (
                "interface_is_output_only"
            )

            return None

        if data is not None:
            self.last_rx = data

        self.rx_count += 1
        self.last_error = None

        return self.last_rx

    def enable(self):
        self.enabled = True
        return True

    def disable(self):
        self.enabled = False
        return True

    def reset(self):
        self.disconnect()

        self.tx_count = 0
        self.rx_count = 0

        self.last_tx = None
        self.last_rx = None
        self.last_error = None

        return True

    def status(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "direction": (
                self.direction
            ),
            "enabled": (
                self.enabled
            ),
            "connected": (
                self.connected
            ),
            "endpoint": (
                self.endpoint
            ),
            "tx_count": (
                self.tx_count
            ),
            "rx_count": (
                self.rx_count
            ),
            "last_error": (
                self.last_error
            ),
        }

    def to_dict(self):
        return {
            **self.status(),
            "parameters": dict(
                self.parameters
            ),
            "metadata": dict(
                self.metadata
            ),
            "last_tx": (
                self.last_tx
            ),
            "last_rx": (
                self.last_rx
            ),
        }

    @classmethod
    def from_dict(
        cls,
        data,
    ):
        if not isinstance(
            data,
            dict,
        ):
            raise TypeError(
                "data deve ser um dicionário."
            )

        interface = cls(
            name=data.get(
                "name",
                "Interface",
            ),
            interface_type=data.get(
                "type",
                data.get(
                    "interface_type",
                    "generic",
                ),
            ),
            interface_id=data.get(
                "id"
            ),
            direction=data.get(
                "direction",
                "bidirectional",
            ),
            parameters=data.get(
                "parameters",
                {},
            ),
            metadata=data.get(
                "metadata",
                {},
            ),
            enabled=data.get(
                "enabled",
                True,
            ),
        )

        return interface

"""
Base universal das placas virtuais do UAP.

Esta classe representa o contrato mínimo de uma placa
eletrônica utilizada pelo simulador, mantendo compatibilidade
com as placas simples já existentes.
"""

import uuid


class BoardBase:

    name = "Board"
    manufacturer = ""

    gpio_count = 0
    pwm_count = 0
    adc_count = 0

    flash_size = 0
    ram_size = 0

    cpu = ""
    frequency = 0

    architecture = ""
    voltage = 0.0

    def __init__(
        self,
        board_id=None,
        name=None,
        metadata=None,
    ):
        self.id = (
            str(board_id)
            if board_id is not None
            else str(uuid.uuid4())
        )

        if name is not None:
            self.name = str(name)

        self.metadata = dict(
            metadata or {}
        )

        self.properties = {}

        self.initialized = False
        self.enabled = True

        self.running = False

        self.pins = {}
        self.peripherals = {}

        self.errors = []

        self.initialization_count = 0
        self.update_count = 0

    @property
    def board_id(self):
        return self.id

    def initialize(self):
        if not self.enabled:
            return False

        self.initialized = True
        self.running = True

        self.initialization_count += 1

        return True

    def shutdown(self):
        self.running = False
        self.initialized = False

        return True

    def start(self):
        if not self.initialized:
            self.initialize()

        if not self.enabled:
            return False

        self.running = True

        return True

    def stop(self):
        self.running = False

        return True

    def reset(self):
        self.running = False

        self.properties.clear()
        self.errors.clear()

        self.update_count = 0

        return True

    def update(self):
        if (
            not self.initialized
            or not self.enabled
            or not self.running
        ):
            return None

        self.update_count += 1

        return self.status()

    def enable(self):
        self.enabled = True

        return True

    def disable(self):
        self.enabled = False
        self.running = False

        return True

    def set_property(
        self,
        name,
        value,
    ):
        self.properties[
            str(name)
        ] = value

        return value

    def get_property(
        self,
        name,
        default=None,
    ):
        return self.properties.get(
            str(name),
            default,
        )

    def remove_property(
        self,
        name,
    ):
        return self.properties.pop(
            str(name),
            None,
        )

    def register_pin(
        self,
        pin,
        key=None,
    ):
        if pin is None:
            raise ValueError(
                "Pino não informado."
            )

        pin_key = (
            key
            if key is not None
            else getattr(
                pin,
                "number",
                getattr(
                    pin,
                    "name",
                    None,
                ),
            )
        )

        if pin_key is None:
            raise ValueError(
                "Não foi possível determinar "
                "a identificação do pino."
            )

        self.pins[
            pin_key
        ] = pin

        return pin

    def get_pin(
        self,
        key,
    ):
        return self.pins.get(
            key
        )

    def remove_pin(
        self,
        key,
    ):
        return self.pins.pop(
            key,
            None,
        )

    def register_peripheral(
        self,
        peripheral,
        name=None,
    ):
        if peripheral is None:
            raise ValueError(
                "Periférico não informado."
            )

        key = str(
            name
            or getattr(
                peripheral,
                "name",
                type(
                    peripheral
                ).__name__,
            )
        )

        self.peripherals[
            key
        ] = peripheral

        return peripheral

    def get_peripheral(
        self,
        name,
    ):
        return self.peripherals.get(
            str(name)
        )

    def remove_peripheral(
        self,
        name,
    ):
        return self.peripherals.pop(
            str(name),
            None,
        )

    def add_error(
        self,
        error,
    ):
        self.errors.append(
            str(error)
        )

        return error

    def clear_errors(self):
        self.errors.clear()

    def capabilities(self):
        return {
            "gpio": int(
                self.gpio_count
            ),
            "pwm": int(
                self.pwm_count
            ),
            "adc": int(
                self.adc_count
            ),
            "flash_size": int(
                self.flash_size
            ),
            "ram_size": int(
                self.ram_size
            ),
            "frequency": int(
                self.frequency
            ),
        }

    def status(self):
        return {
            "id": self.id,
            "name": self.name,
            "manufacturer": (
                self.manufacturer
            ),
            "cpu": self.cpu,
            "architecture": (
                self.architecture
            ),
            "frequency": (
                self.frequency
            ),
            "gpio_count": (
                self.gpio_count
            ),
            "pwm_count": (
                self.pwm_count
            ),
            "adc_count": (
                self.adc_count
            ),
            "flash_size": (
                self.flash_size
            ),
            "ram_size": (
                self.ram_size
            ),
            "voltage": (
                self.voltage
            ),
            "initialized": (
                self.initialized
            ),
            "enabled": (
                self.enabled
            ),
            "running": (
                self.running
            ),
            "update_count": (
                self.update_count
            ),
            "errors": list(
                self.errors
            ),
        }

    def to_dict(self):
        return {
            **self.status(),
            "properties": dict(
                self.properties
            ),
            "metadata": dict(
                self.metadata
            ),
            "pins": {
                str(key): (
                    value.to_dict()
                    if hasattr(
                        value,
                        "to_dict",
                    )
                    else str(value)
                )
                for key, value
                in self.pins.items()
            },
            "peripherals": {
                str(key): (
                    value.to_dict()
                    if hasattr(
                        value,
                        "to_dict",
                    )
                    else str(value)
                )
                for key, value
                in self.peripherals.items()
            },
        }

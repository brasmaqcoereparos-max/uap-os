from app.modules.uhal.hardware_registry import (
    hardware_registry,
)

from app.modules.uhal.drivers.simulator import (
    SimulatorDriver,
)

from app.modules.uhal.drivers.esp32 import (
    ESP32Driver,
)

from app.modules.uhal.drivers.arduino_uno import (
    ArduinoUnoDriver,
)

from app.modules.uhal.drivers.raspberry_pi import (
    RaspberryPiDriver,
)


def register_builtin_drivers():

    drivers = {
        "simulator": SimulatorDriver(),
        "esp32": ESP32Driver(),
        "arduino_uno": ArduinoUnoDriver(),
        "raspberry_pi": RaspberryPiDriver(),
    }

    for name, driver in drivers.items():

        if hardware_registry.get(
            name
        ) is None:

            hardware_registry.register(
                name,
                driver,
            )

    return hardware_registry.all()

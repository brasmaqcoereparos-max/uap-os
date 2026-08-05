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

    hardware_registry.register(

        "simulator",

        SimulatorDriver(),

    )

    hardware_registry.register(

        "esp32",

        ESP32Driver(),

    )

    hardware_registry.register(

        "arduino_uno",

        ArduinoUnoDriver(),

    )

    hardware_registry.register(

        "raspberry_pi",

        RaspberryPiDriver(),

  )

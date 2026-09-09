from app.modules.uhal.hardware_registry import (
    hardware_registry,
)

from app.modules.uhal.drivers.simulator import (
    SimulatorDriver,
)

from app.modules.uhal.drivers.esp32 import (
    ESP32Driver,
)

from app.modules.uhal.drivers.esp32_c3 import (
    ESP32C3Driver,
)

from app.modules.uhal.drivers.esp32_s3 import (
    ESP32S3Driver,
)

from app.modules.uhal.drivers.esp8266 import (
    ESP8266Driver,
)

from app.modules.uhal.drivers.arduino_uno import (
    ArduinoUnoDriver,
)

from app.modules.uhal.drivers.arduino_nano import (
    ArduinoNanoDriver,
)

from app.modules.uhal.drivers.arduino_mega import (
    ArduinoMegaDriver,
)

from app.modules.uhal.drivers.raspberry_pi import (
    RaspberryPiDriver,
)

from app.modules.uhal.drivers.raspberry_pico import (
    RaspberryPicoDriver,
)

from app.modules.uhal.drivers.stm32 import (
    STM32Driver,
)

from app.modules.uhal.drivers.teensy import (
    TeensyDriver,
)

from app.modules.uhal.drivers.beaglebone import (
    BeagleBoneDriver,
)


def register_builtin_drivers():

    drivers = {
        "simulator": (
            SimulatorDriver()
        ),
        "esp32": (
            ESP32Driver()
        ),
        "esp32_c3": (
            ESP32C3Driver()
        ),
        "esp32_s3": (
            ESP32S3Driver()
        ),
        "esp8266": (
            ESP8266Driver()
        ),
        "arduino_uno": (
            ArduinoUnoDriver()
        ),
        "arduino_nano": (
            ArduinoNanoDriver()
        ),
        "arduino_mega": (
            ArduinoMegaDriver()
        ),
        "raspberry_pi": (
            RaspberryPiDriver()
        ),
        "raspberry_pico": (
            RaspberryPicoDriver()
        ),
        "stm32": (
            STM32Driver()
        ),
        "teensy": (
            TeensyDriver()
        ),
        "beaglebone": (
            BeagleBoneDriver()
        ),
    }

    for (
        name,
        driver,
    ) in drivers.items():

        if hardware_registry.get(
            name
        ) is None:

            hardware_registry.register(
                name,
                driver,
            )

    return hardware_registry.all()

from app.modules.simulator.programming.compiler.backends.arduino_backend import (
    ArduinoBackend,
)


class ESP32Backend(ArduinoBackend):

    name = "esp32"

    def generate(
        self,
        ir,
    ):

        source = super().generate(ir)

        source = source.replace(

            "#include <Arduino.h>",

            "#include <Arduino.h>\n#include <WiFi.h>",

        )

        return source


esp32_backend = ESP32Backend()

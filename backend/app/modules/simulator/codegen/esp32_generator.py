from app.modules.simulator.codegen.arduino_generator import (
    ArduinoGenerator,
)


class ESP32Generator(ArduinoGenerator):

    LANGUAGE = "ESP32"

    def header(self):

        return """// UAP OS
// ESP32 Arduino Framework

void setup() {

}

void loop() {
"""

    def footer(self):

        return """
}
"""

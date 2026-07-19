from app.modules.simulator.programming.compiler.backends.arduino_backend import (
    ArduinoBackend,
)


class RP2040Backend(ArduinoBackend):

    name = "rp2040"

    def generate(
        self,
        ir,
    ):

        return super().generate(ir)


rp2040_backend = RP2040Backend()

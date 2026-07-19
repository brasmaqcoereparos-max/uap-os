from app.modules.simulator.programming.compiler.backends.arduino_backend import (
    ArduinoBackend,
)


class STM32Backend(ArduinoBackend):

    name = "stm32"

    def generate(
        self,
        ir,
    ):

        return super().generate(ir)


stm32_backend = STM32Backend()

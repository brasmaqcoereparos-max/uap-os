from app.modules.uhal.hardware_controller import (
    hardware_controller,
)


class RuntimeHardwareBridge:

    def initialize(self, board):
        return hardware_controller.initialize(
            board
        )

    def shutdown(self):
        return hardware_controller.shutdown()

    def status(self):
        return hardware_controller.status()

    def write(
        self,
        pin,
        value,
    ):
        return hardware_controller.write(
            pin,
            value,
        )

    def read(self, pin):
        return hardware_controller.read(
            pin
        )

    def execute(self, command):
        if not isinstance(
            command,
            dict,
        ):
            raise TypeError(
                "Comando de hardware inválido."
            )

        action = str(
            command.get(
                "action",
                "",
            )
        ).strip().lower()

        if action == "hardware.initialize":
            return self.initialize(
                command.get(
                    "board",
                    "raspberry_pi",
                )
            )

        if action == "hardware.shutdown":
            return self.shutdown()

        if action == "hardware.status":
            return self.status()

        if action == "gpio.write":
            return self.write(
                command.get("pin"),
                command.get("value"),
            )

        if action == "gpio.read":
            return self.read(
                command.get("pin")
            )

        raise ValueError(
            f"Ação desconhecida: {action}"
        )


runtime_hardware_bridge = (
    RuntimeHardwareBridge()
      )

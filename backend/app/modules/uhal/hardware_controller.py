from app.modules.uhal.hardware_service import (
    hardware_service,
)


class HardwareController:

    def execute(self, command):

        if not isinstance(command, dict):
            raise TypeError(
                "Comando de hardware inválido."
            )

        action = str(
            command.get("action", "")
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

        if action == "hardware.available":
            return self.available()

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

        if action == "gpio.pwm":
            return self.pwm(
                command.get("pin"),
                command.get("duty"),
            )

        raise ValueError(
            f"Ação desconhecida: {action}"
        )

    def initialize(self, board):
        hardware_service.load(
            board
        )

        return hardware_service.status()

    def shutdown(self):
        hardware_service.unload()

        return {
            "success": True
        }

    def available(self):
        return hardware_service.available()

    def status(self):
        return hardware_service.status()

    def write(self, pin, value):
        return hardware_service.write(
            pin,
            value,
        )

    def read(self, pin):
        return hardware_service.read(
            pin
        )

    def pwm(self, pin, duty):
        return hardware_service.pwm(
            pin,
            duty,
        )


hardware_controller = HardwareController()

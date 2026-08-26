from app.modules.uhal.hardware_service import (
    hardware_service,
)


class HardwareController:

    def initialize(self, board):
        hardware_service.load(
            board
        )

        return hardware_service.status()

    def shutdown(self):
        hardware_service.unload()

        return {
            "success": True,
        }

    def status(self):
        return hardware_service.status()

    def write(
        self,
        pin,
        value,
    ):
        return hardware_service.write(
            pin,
            value,
        )

    def read(self, pin):
        return hardware_service.read(
            pin
        )


hardware_controller = HardwareController()

from app.modules.uhal.hal_manager import (
    hal_manager,
)


class HardwareService:

    def load(self, board):
        return hal_manager.load(
            board
        )

    def unload(self):
        return hal_manager.unload()

    def status(self):
        driver = hal_manager.current()

        if driver is None:
            return {
                "loaded": False,
                "board": None,
            }

        method = getattr(
            driver,
            "status",
            None,
        )

        if callable(method):
            result = method()

        else:
            result = {}

        return {
            "loaded": True,
            "board": hal_manager.current_board(),
            "driver": result,
        }

    def write(
        self,
        pin,
        value,
    ):
        return hal_manager.digital_write(
            pin,
            value,
        )

    def read(self, pin):
        return hal_manager.digital_read(
            pin
        )


hardware_service = HardwareService()

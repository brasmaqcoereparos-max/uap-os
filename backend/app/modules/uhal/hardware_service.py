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

    def available(self):
        return hal_manager.available()

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

        return {
            "loaded": True,
            "board": hal_manager.current_board(),
            "driver": (
                method()
                if callable(method)
                else {}
            ),
        }

    def write(self, pin, value):
        return hal_manager.digital_write(
            pin,
            value,
        )

    def read(self, pin):
        return hal_manager.digital_read(
            pin
        )

    def pwm(self, pin, duty):
        return hal_manager.pwm_write(
            pin,
            duty,
        )


hardware_service = HardwareService()

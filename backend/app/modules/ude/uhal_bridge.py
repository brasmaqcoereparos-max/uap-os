from app.modules.uhal.hal_manager import (
    hal_manager,
)


class UHALBridge:

    def current_driver(self):
        return hal_manager.current()

    def current_board(self):
        return hal_manager.current_board()

    def available_drivers(self):
        return hal_manager.available()

    def load_driver(
        self,
        board,
    ):
        return hal_manager.load(
            board
        )

    def unload_driver(self):
        return hal_manager.unload()

    def digital_write(
        self,
        pin,
        value,
    ):
        return hal_manager.digital_write(
            pin,
            value,
        )

    def digital_read(
        self,
        pin,
    ):
        return hal_manager.digital_read(
            pin
        )

    def analog_write(
        self,
        pin,
        value,
    ):
        return hal_manager.analog_write(
            pin,
            value,
        )

    def analog_read(
        self,
        pin,
    ):
        return hal_manager.analog_read(
            pin
        )


uhal_bridge = UHALBridge()

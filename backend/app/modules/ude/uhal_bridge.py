from app.modules.uhal.hal_manager import (
    hal_manager,
)


class UHALBridge:

    def current_driver(self):

        return hal_manager.current()

    def available_drivers(self):

        return hal_manager.available()


uhal_bridge = UHALBridge()

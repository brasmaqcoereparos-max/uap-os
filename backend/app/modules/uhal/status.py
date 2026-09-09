from app.modules.uhal.health import (
    uhal_health,
)


class UHALStatus:

    def snapshot(self):
        health = (
            uhal_health
            .check()
        )

        return {
            "service": "uhal",
            "healthy": (
                health["healthy"]
            ),
            "health": health,
            "components": {
                "hal_manager": True,
                "hardware_registry": True,
                "driver_loader": True,
                "gpio": True,
                "port_manager": True,
                "board_detector": True,
            },
        }


uhal_status = UHALStatus()

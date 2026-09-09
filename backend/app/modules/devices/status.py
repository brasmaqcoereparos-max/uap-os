from app.modules.devices.health import (
    devices_health,
)


class DevicesStatus:

    def snapshot(self):
        health = (
            devices_health
            .check()
        )

        return {
            "service": "devices",
            "healthy": (
                health["healthy"]
            ),
            "health": health,
            "components": {
                "device_manager": True,
                "device_registry": True,
                "device_service": True,
                "hardware_gateway": True,
                "sensor_manager": True,
                "motor_manager": True,
                "relay_manager": True,
                "gpio_device": True,
            },
        }


devices_status = DevicesStatus()

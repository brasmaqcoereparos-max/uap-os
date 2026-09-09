from app.modules.ude.health import (
    ude_health,
)


class UDEStatus:

    def snapshot(self):
        health = (
            ude_health
            .check()
        )

        return {
            "service": "ude",
            "healthy": (
                health.get(
                    "healthy",
                    True,
                )
            ),
            "health": health,
            "components": {
                "ude_manager": True,
                "device_manager": True,
                "device_registry": True,
                "device_controller": True,
                "uhal_bridge": True,
                "motion_bridge": True,
                "simulator": True,
            },
        }


ude_status = UDEStatus()

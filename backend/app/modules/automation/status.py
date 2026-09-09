from app.modules.automation.health import (
    automation_health,
)


class AutomationStatus:

    def snapshot(self):
        health = (
            automation_health
            .check()
        )

        return {
            "service": "automation",
            "healthy": (
                health["healthy"]
            ),
            "health": health,
        }


automation_status = (
    AutomationStatus()
)

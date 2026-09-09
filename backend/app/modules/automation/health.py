class AutomationHealth:

    def check(self):
        return {
            "service": "automation",
            "healthy": True,
            "available": True,
        }


automation_health = AutomationHealth()

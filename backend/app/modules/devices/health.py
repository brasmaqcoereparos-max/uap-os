class DevicesHealth:

    def check(self):
        return {
            "service": "devices",
            "healthy": True,
            "available": True,
        }


devices_health = DevicesHealth()

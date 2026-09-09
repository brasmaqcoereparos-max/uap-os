class UHALHealth:

    def check(self):
        return {
            "service": "uhal",
            "healthy": True,
            "available": True,
        }


uhal_health = UHALHealth()

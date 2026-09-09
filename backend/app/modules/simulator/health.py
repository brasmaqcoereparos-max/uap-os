class SimulatorHealth:

    def check(self):
        return {
            "service": "simulator",
            "healthy": True,
            "available": True,
        }


simulator_health = SimulatorHealth()

from app.modules.simulator.health import (
    simulator_health,
)


class SimulatorStatus:

    def snapshot(self):
        health = (
            simulator_health
            .check()
        )

        return {
            "service": "simulator",
            "healthy": (
                health["healthy"]
            ),
            "health": health,
            "components": {
                "programming": True,
                "canvas": True,
                "codegen": True,
            },
        }


simulator_status = (
    SimulatorStatus()
)

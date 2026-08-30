"""
Motor principal de simulação de hardware do UAP.
"""

from app.modules.simulator.programming.simulator.hardware_engine.loop import (
    SimulationLoop,
)


class SimulationEngine:

    def __init__(self):
        self.running = False
        self.loop = SimulationLoop()

        self.tick_count = 0
        self.start_count = 0

        self.last_error = None

    def start(self):
        if self.running:
            return True

        try:
            self.loop.start()

            self.running = True
            self.start_count += 1

            self.last_error = None

            return True

        except Exception as exc:
            self.running = False
            self.last_error = str(exc)

            raise

    def stop(self):
        if not self.running:
            return True

        try:
            self.loop.stop()

            self.running = False
            self.last_error = None

            return True

        except Exception as exc:
            self.last_error = str(exc)

            raise

    def tick(self):
        if not self.running:
            return None

        try:
            result = self.loop.tick()

            self.tick_count += 1
            self.last_error = None

            return result

        except Exception as exc:
            self.last_error = str(exc)

            raise

    def reset(self):
        result = self.loop.reset()

        self.running = False
        self.tick_count = 0
        self.last_error = None

        return result

    def is_running(self):
        return self.running

    def status(self):
        loop_status = getattr(
            self.loop,
            "status",
            None,
        )

        return {
            "running": self.running,
            "tick_count": (
                self.tick_count
            ),
            "start_count": (
                self.start_count
            ),
            "last_error": (
                self.last_error
            ),
            "loop": (
                loop_status()
                if callable(loop_status)
                else None
            ),
        }

    def to_dict(self):
        return self.status()


simulation_engine = SimulationEngine()

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

    def start(self):

        if self.running:
            return

        self.running = True
        self.loop.start()

    def stop(self):

        if not self.running:
            return

        self.loop.stop()
        self.running = False

    def tick(self):

        if not self.running:
            return

        self.loop.tick()

    def reset(self):

        self.loop.reset()
        self.running = False

    def is_running(self):

        return self.running

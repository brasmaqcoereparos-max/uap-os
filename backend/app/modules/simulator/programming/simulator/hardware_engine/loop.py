"""
Loop principal do motor de simulação UAP.
"""

from app.modules.simulator.programming.simulator.hardware_engine.device_runner import (
    DeviceRunner,
)


class SimulationLoop:

    def __init__(self):

        self.running = False
        self.device_runner = DeviceRunner()

    def start(self):

        self.running = True
        self.device_runner.start()

    def stop(self):

        self.running = False
        self.device_runner.stop()

    def tick(self):

        if not self.running:
            return

        self.device_runner.update()

    def reset(self):

        self.device_runner.reset()
        self.running = False

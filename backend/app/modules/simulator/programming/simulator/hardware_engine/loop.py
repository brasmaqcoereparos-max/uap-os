"""
Loop principal do motor UAP.

Integra:
    Runtime
    Devices
    Timers
    Hardware Engine
"""

from app.modules.simulator.programming.simulator.hardware_engine.device_runner import (
    DeviceRunner,
)

from app.modules.simulator.programming.simulator.runtime.runtime_engine import (
    runtime_engine,
)


class SimulationLoop:

    def __init__(self):

        self.running = False
        self.device_runner = DeviceRunner()

    def start(self):

        if self.running:
            return

        self.device_runner.start()
        runtime_engine.start()

        self.running = True

    def stop(self):

        runtime_engine.stop()
        self.device_runner.stop()

        self.running = False

    def tick(self):

        if not self.running:
            return

        self.device_runner.update()
        runtime_engine.update()

    def reset(self):

        runtime_engine.reset()
        self.device_runner.reset()

        self.running = False

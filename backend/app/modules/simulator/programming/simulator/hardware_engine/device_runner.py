"""
Executor dos dispositivos físicos/virtuais do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_manager import (
    device_manager,
)

from app.modules.simulator.programming.simulator.device.device_initializer import (
    DeviceInitializer,
)


class DeviceRunner:

    def __init__(self):

        self.running = False

    def initialize(self):

        DeviceInitializer.initialize()

    def start(self):

        self.initialize()

        self.running = True

    def stop(self):

        self.running = False

    def update(self):

        if not self.running:
            return

        device_manager.update_all()

    def reset(self):

        device_manager.reset_all()

        self.running = False

    def device_count(self):

        return device_manager.count()

    def devices(self):

        return device_manager.all()

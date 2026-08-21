"""
Executor central dos dispositivos do simulador UAP.
"""

from app.modules.simulator.programming.simulator.device.device_manager import (
    device_manager,
)


class DeviceRunner:

    def __init__(self):

        self.running = False

    def start(self):

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

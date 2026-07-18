from app.modules.simulator.programming.canvas.device_manager import (
    device_manager,
)


class DeviceMonitor:

    def status(self):

        return device_manager.all()

    def connected(self):

        return {

            name: data

            for name, data

            in device_manager.all().items()

            if data["connected"]

        }

    def disconnected(self):

        return {

            name: data

            for name, data

            in device_manager.all().items()

            if not data["connected"]

        }


device_monitor = DeviceMonitor()

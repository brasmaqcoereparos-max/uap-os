from app.modules.simulator.programming.canvas.device_persistence import (
    device_persistence,
)


class DeviceWorkspace:

    def save_workspace(
        self,
        filename="devices.json",
    ):

        device_persistence.save(filename)

    def load_workspace(
        self,
        filename="devices.json",
    ):

        device_persistence.load(filename)

    def workspace_exists(
        self,
        filename="devices.json",
    ):

        return device_persistence.exists(filename)


device_workspace = DeviceWorkspace()

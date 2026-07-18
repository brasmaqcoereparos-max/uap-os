import json

from app.modules.simulator.programming.canvas.device_serializer import (
    device_serializer,
)
from app.modules.simulator.programming.canvas.device_manager import (
    device_manager,
)


class DeviceImport:

    def import_json(
        self,
        content,
    ):

        devices = json.loads(content)

        for _, data in devices.items():

            device = device_serializer.deserialize(data)

            device_manager.register(device)

    def import_dict(
        self,
        devices,
    ):

        for _, data in devices.items():

            device = device_serializer.deserialize(data)

            device_manager.register(device)


device_import = DeviceImport()

import json

from app.modules.simulator.programming.canvas.device_manager import (
    device_manager,
)


class DeviceExport:

    def export(self):

        return json.dumps(

            device_manager.all(),

            indent=4,

        )

    def export_dict(self):

        return device_manager.all()


device_export = DeviceExport()

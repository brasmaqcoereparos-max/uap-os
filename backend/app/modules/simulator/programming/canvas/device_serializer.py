from app.modules.simulator.programming.canvas.device_base import (
    DeviceBase,
)


class DeviceSerializer:

    def serialize(
        self,
        device: DeviceBase,
    ):

        return device.status()

    def deserialize(
        self,
        data,
    ):

        device = DeviceBase(
            data["name"]
        )

        if data.get("enabled", True):

            device.enable()

        else:

            device.disable()

        if data.get("connected", False):

            device.connect()

        return device


device_serializer = DeviceSerializer()

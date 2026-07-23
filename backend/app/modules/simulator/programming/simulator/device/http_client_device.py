from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)


class HTTPClientDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

    def get(
        self,
        url,
    ):
        return {
            "status": 200,
            "url": url,
        }

    def post(
        self,
        url,
        payload,
    ):
        return {
            "status": 200,
            "url": url,
            "payload": payload,
        }

    def update(self):
        pass

    def reset(self):
        pass

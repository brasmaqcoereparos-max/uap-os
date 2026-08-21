"""
Cliente HTTP simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class HTTPClientDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.connected = False
        self.last_request = None
        self.last_response = None

    def connect(self):
        self.connected = True

    def disconnect(self):
        self.connected = False

    def request(
        self,
        method,
        url,
        data=None,
    ):

        self.last_request = {
            "method": method,
            "url": url,
            "data": data,
        }

        if not self.connected:
            self.connect()

        self.last_response = {
            "status": 200,
            "data": None,
        }

        return self.last_response

    def get(
        self,
        url,
    ):
        return self.request(
            "GET",
            url,
        )

    def post(
        self,
        url,
        data=None,
    ):
        return self.request(
            "POST",
            url,
            data,
        )

    def update(self):
        pass

    def reset(self):

        self.last_request = None
        self.last_response = None
        self.disconnect()

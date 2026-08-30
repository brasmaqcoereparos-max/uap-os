"""
Cliente HTTP simulado do UAP.

Este dispositivo não realiza acesso real à Internet.
Ele representa o comportamento de um cliente HTTP
dentro do ambiente de simulação.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class HTTPClientDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(
            name=name,
            category="communication",
            description=(
                "Cliente HTTP simulado"
            ),
            icon="network",
        )

        self.connected = False

        self.last_request = None
        self.last_response = None

        self.request_count = 0

        self.default_headers = {}

    def connect(self):
        if not self.enabled:
            return False

        self.connected = True

        return True

    def disconnect(self):
        self.connected = False

        return True

    def set_header(
        self,
        name,
        value,
    ):
        self.default_headers[
            str(name)
        ] = str(value)

        return value

    def remove_header(
        self,
        name,
    ):
        return self.default_headers.pop(
            str(name),
            None,
        )

    def clear_headers(self):
        self.default_headers.clear()

        return True

    def request(
        self,
        method,
        url,
        data=None,
        headers=None,
    ):
        if not self.enabled:
            return {
                "status": 0,
                "data": None,
                "error": (
                    "device_disabled"
                ),
            }

        if not self.connected:
            self.connect()

        method = str(
            method
        ).strip().upper()

        request_headers = dict(
            self.default_headers
        )

        request_headers.update(
            dict(headers or {})
        )

        self.last_request = {
            "method": method,
            "url": str(url),
            "data": data,
            "headers": (
                request_headers
            ),
        }

        self.request_count += 1

        self.last_response = {
            "status": 200,
            "data": None,
            "headers": {},
            "simulated": True,
        }

        return dict(
            self.last_response
        )

    def get(
        self,
        url,
        headers=None,
    ):
        return self.request(
            "GET",
            url,
            headers=headers,
        )

    def post(
        self,
        url,
        data=None,
        headers=None,
    ):
        return self.request(
            "POST",
            url,
            data,
            headers,
        )

    def put(
        self,
        url,
        data=None,
        headers=None,
    ):
        return self.request(
            "PUT",
            url,
            data,
            headers,
        )

    def delete(
        self,
        url,
        headers=None,
    ):
        return self.request(
            "DELETE",
            url,
            headers=headers,
        )

    def update(self):
        return self.last_response

    def reset(self):
        self.last_request = None
        self.last_response = None

        self.request_count = 0

        self.default_headers.clear()

        self.disconnect()

        return True

    def to_dict(self):
        data = super().to_dict()

        data.update({
            "connected": (
                self.connected
            ),
            "last_request": (
                self.last_request
            ),
            "last_response": (
                self.last_response
            ),
            "request_count": (
                self.request_count
            ),
            "default_headers": dict(
                self.default_headers
            ),
        })

        return data

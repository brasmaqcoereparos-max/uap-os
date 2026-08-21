"""
Dispositivo virtual do UDE.

Usado para simulação, testes e desenvolvimento
sem necessidade de hardware físico.
"""

from uuid import uuid4


class VirtualDevice:

    def __init__(
        self,
        name,
        device_type="virtual",
        device_id=None,
    ):
        self.id = (
            device_id
            or str(uuid4())
        )

        self.name = name
        self.device_type = device_type

        self.connected = False
        self.enabled = True

        self.inputs = {}
        self.outputs = {}
        self.properties = {}

    def connect(self):
        self.connected = True
        return True

    def disconnect(self):
        self.connected = False
        return True

    def enable(self):
        self.enabled = True
        return True

    def disable(self):
        self.enabled = False
        return True

    def set_input(
        self,
        name,
        value,
    ):
        self.inputs[name] = value

    def get_input(
        self,
        name,
        default=None,
    ):
        return self.inputs.get(
            name,
            default,
        )

    def set_output(
        self,
        name,
        value,
    ):
        self.outputs[name] = value

    def get_output(
        self,
        name,
        default=None,
    ):
        return self.outputs.get(
            name,
            default,
        )

    def set_property(
        self,
        name,
        value,
    ):
        self.properties[name] = value

    def get_property(
        self,
        name,
        default=None,
    ):
        return self.properties.get(
            name,
            default,
        )

    def is_available(self):
        return (
            self.enabled
            and self.connected
        )

    def status(self):
        return {
            "id": self.id,
            "name": self.name,
            "device_type": self.device_type,
            "connected": self.connected,
            "enabled": self.enabled,
            "available": self.is_available(),
            "inputs": dict(self.inputs),
            "outputs": dict(self.outputs),
            "properties": dict(
                self.properties
            ),
        }

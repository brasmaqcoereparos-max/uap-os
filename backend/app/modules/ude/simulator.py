"""
Simulador básico de dispositivos UDE.

Permite testar projetos sem hardware físico.
"""


class SimulatedDevice:

    def __init__(
        self,
        device_id,
        name,
        device_type="virtual",
    ):
        self.device_id = device_id
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

    def disable(self):
        self.enabled = False

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

    def status(self):
        return {
            "device_id": self.device_id,
            "name": self.name,
            "device_type": self.device_type,
            "connected": self.connected,
            "enabled": self.enabled,
            "inputs": dict(self.inputs),
            "outputs": dict(self.outputs),
            "properties": dict(
                self.properties
            ),
        }


class DeviceSimulator:

    def __init__(self):
        self.devices = {}

    def create(
        self,
        device_id,
        name,
        device_type="virtual",
    ):
        device = SimulatedDevice(
            device_id=device_id,
            name=name,
            device_type=device_type,
        )

        self.devices[device_id] = device

        return device

    def get(
        self,
        device_id,
    ):
        return self.devices.get(
            device_id
        )

    def remove(
        self,
        device_id,
    ):
        return self.devices.pop(
            device_id,
            None,
        )

    def list(self):
        return list(
            self.devices.values()
        )

    def clear(self):
        self.devices.clear()

    def status(self):
        return {
            device.device_id:
                device.status()
            for device in self.devices.values()
        }


simulator = DeviceSimulator()

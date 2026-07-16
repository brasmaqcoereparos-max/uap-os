from app.modules.simulator.devices.virtual_led import VirtualLED
from app.modules.simulator.devices.virtual_button import VirtualButton
from app.modules.simulator.devices.virtual_relay import VirtualRelay

from app.modules.simulator.components.virtual_temperature import (
    VirtualTemperature,
)
from app.modules.simulator.components.virtual_humidity import (
    VirtualHumidity,
)
from app.modules.simulator.components.virtual_ultrasonic import (
    VirtualUltrasonic,
)


class SimulatorService:

    def __init__(self):
        self.devices = {}

    def add(self, device):
        self.devices[device.id] = device

    # --------------------
    # Atuadores
    # --------------------

    def create_led(self, device_id: str, name: str):
        device = VirtualLED(device_id, name)
        self.add(device)
        return device.status()

    def create_button(self, device_id: str, name: str):
        device = VirtualButton(device_id, name)
        self.add(device)
        return device.status()

    def create_relay(self, device_id: str, name: str):
        device = VirtualRelay(device_id, name)
        self.add(device)
        return device.status()

    # --------------------
    # Sensores
    # --------------------

    def create_temperature(self, device_id: str, name: str):
        sensor = VirtualTemperature(device_id, name)
        self.add(sensor)
        return sensor.status()

    def create_humidity(self, device_id: str, name: str):
        sensor = VirtualHumidity(device_id, name)
        self.add(sensor)
        return sensor.status()

    def create_ultrasonic(self, device_id: str, name: str):
        sensor = VirtualUltrasonic(device_id, name)
        self.add(sensor)
        return sensor.status()

    # --------------------

    def update(self):
        for device in self.devices.values():
            if hasattr(device, "update"):
                device.update()

    def list(self):
        self.update()

        return [
            device.status()
            for device in self.devices.values()
        ]

    def get(self, device_id):
        device = self.devices.get(device_id)

        if device:
            if hasattr(device, "update"):
                device.update()

            return device.status()

        return None

    def remove(self, device_id):
        if device_id in self.devices:
            del self.devices[device_id]

    def turn_on(self, device_id):
        device = self.devices.get(device_id)

        if device and hasattr(device, "on"):
            device.on()

        return self.get(device_id)

    def turn_off(self, device_id):
        device = self.devices.get(device_id)

        if device and hasattr(device, "off"):
            device.off()

        return self.get(device_id)

    def toggle(self, device_id):
        device = self.devices.get(device_id)

        if device and hasattr(device, "toggle"):
            device.toggle()

        return self.get(device_id)


simulator_service = SimulatorService()

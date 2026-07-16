from app.modules.simulator.devices.virtual_led import VirtualLED
from app.modules.simulator.devices.virtual_button import VirtualButton
from app.modules.simulator.devices.virtual_relay import VirtualRelay


class SimulatorService:

    def __init__(self):
        self.devices = {}

    def add(self, device):
        self.devices[device.id] = device

    def create_led(self, device_id: str, name: str):
        led = VirtualLED(device_id, name)
        self.add(led)
        return led.status()

    def create_button(self, device_id: str, name: str):
        button = VirtualButton(device_id, name)
        self.add(button)
        return button.status()

    def create_relay(self, device_id: str, name: str):
        relay = VirtualRelay(device_id, name)
        self.add(relay)
        return relay.status()

    def list(self):
        return [
            device.status()
            for device in self.devices.values()
        ]

    def get(self, device_id):
        device = self.devices.get(device_id)

        if device:
            return device.status()

        return None

    def remove(self, device_id):
        if device_id in self.devices:
            del self.devices[device_id]

    def turn_on(self, device_id):
        device = self.devices.get(device_id)

        if device:
            device.on()
            return device.status()

        return None

    def turn_off(self, device_id):
        device = self.devices.get(device_id)

        if device:
            device.off()
            return device.status()

        return None

    def toggle(self, device_id):
        device = self.devices.get(device_id)

        if device:
            device.toggle()
            return device.status()

        return None


simulator_service = SimulatorService()

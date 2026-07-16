class SimulatorService:

    def __init__(self):
        self.devices = {}

    def add(self, device):
        self.devices[device["id"]] = device

    def list(self):
        return list(self.devices.values())

    def get(self, device_id):
        return self.devices.get(device_id)

    def remove(self, device_id):
        self.devices.pop(device_id, None)


simulator_service = SimulatorService()

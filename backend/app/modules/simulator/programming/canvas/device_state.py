from enum import Enum


class DeviceState(Enum):

    OFFLINE = "offline"
    ONLINE = "online"
    BUSY = "busy"
    ERROR = "error"


class DeviceStateManager:

    def __init__(self):

        self.states = {}

    def set(self, device, state: DeviceState):

        self.states[device] = state

    def get(self, device):

        return self.states.get(
            device,
            DeviceState.OFFLINE,
        )

    def clear(self):

        self.states.clear()

    def all(self):

        return {
            device: state.value
            for device, state in self.states.items()
        }


device_state = DeviceStateManager()

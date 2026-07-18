from copy import deepcopy


class DeviceSnapshot:

    def __init__(self):

        self.snapshots = {}

    def save(
        self,
        device,
        state,
    ):

        self.snapshots[device] = deepcopy(state)

    def load(
        self,
        device,
    ):

        return deepcopy(

            self.snapshots.get(device)

        )

    def remove(
        self,
        device,
    ):

        self.snapshots.pop(
            device,
            None,
        )

    def clear(self):

        self.snapshots.clear()

    def all(self):

        return deepcopy(self.snapshots)


device_snapshot = DeviceSnapshot()

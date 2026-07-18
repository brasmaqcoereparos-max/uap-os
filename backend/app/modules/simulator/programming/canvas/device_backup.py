from datetime import datetime


class DeviceBackup:

    def __init__(self):

        self.backups = []

    def create(
        self,
        device,
        state,
    ):

        self.backups.append(

            {

                "device": device,

                "created": datetime.now().isoformat(),

                "state": state,

            }

        )

    def latest(self):

        if not self.backups:

            return None

        return self.backups[-1]

    def clear(self):

        self.backups.clear()

    def all(self):

        return self.backups.copy()


device_backup = DeviceBackup()

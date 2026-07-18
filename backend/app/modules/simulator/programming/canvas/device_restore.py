from app.modules.simulator.programming.canvas.device_backup import (
    device_backup,
)


class DeviceRestore:

    def restore_last(self):

        backup = device_backup.latest()

        if backup is None:

            return None

        return backup

    def available(self):

        return len(

            device_backup.all()

        )

    def clear(self):

        device_backup.clear()


device_restore = DeviceRestore()

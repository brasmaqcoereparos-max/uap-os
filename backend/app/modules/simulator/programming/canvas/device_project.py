from datetime import datetime


class DeviceProject:

    def __init__(self):

        self.name = "New Project"

        self.created = datetime.now()

        self.modified = datetime.now()

    def rename(
        self,
        name,
    ):

        self.name = name

        self.modified = datetime.now()

    def info(self):

        return {

            "name": self.name,

            "created": self.created.isoformat(),

            "modified": self.modified.isoformat(),

        }


device_project = DeviceProject()

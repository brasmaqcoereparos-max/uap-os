from app.modules.ude.device_command import (
    DeviceCommand,
)


class DeviceController:

    def __init__(self):

        self.device = None

    def attach(
        self,
        device,
    ):

        self.device = device

    def execute(
        self,
        command,
    ):

        if self.device is None:
            return False

        action = command.action

        method = getattr(
            self.device,
            action,
            None,
        )

        if method is None:
            return False

        method(
            **command.parameters
        )

        return True

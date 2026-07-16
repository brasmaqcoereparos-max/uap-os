from app.modules.simulator.devices.virtual_device import VirtualDevice


class VirtualButton(VirtualDevice):

    def __init__(
        self,
        device_id,
        name,
    ):
        super().__init__(
            device_id,
            name,
            "BUTTON",
        )

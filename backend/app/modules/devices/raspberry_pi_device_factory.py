from app.modules.devices.raspberry_pi_device import (
    RaspberryPiDevice,
)


class RaspberryPiDeviceFactory:

    @staticmethod
    def create(
        device_id,
        pin,
        mode="output",
    ):

        return RaspberryPiDevice(
            device_id=device_id,
            pin=pin,
            mode=mode,
        )


raspberry_pi_device_factory = (
    RaspberryPiDeviceFactory()
)

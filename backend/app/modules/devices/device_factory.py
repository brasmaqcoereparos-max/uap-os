from app.modules.devices.raspberry_pi_device import (
    RaspberryPiDevice,
)


class DeviceFactory:

    def create(
        self,
        device_type,
        device_id,
        **config,
    ):

        device_type = str(
            device_type
        ).strip().lower()

        if device_type in {
            "gpio",
            "raspberry_pi_gpio",
            "digital_output",
            "digital_input",
        }:

            return RaspberryPiDevice(
                device_id=device_id,
                pin=config.get("pin"),
                mode=config.get(
                    "mode",
                    "output",
                ),
            )

        raise ValueError(
            f"Tipo de dispositivo desconhecido: "
            f"{device_type}"
        )


device_factory = DeviceFactory()

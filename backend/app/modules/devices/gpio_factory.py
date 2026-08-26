from app.modules.devices.inputs.digital_input import (
    DigitalInput,
)

from app.modules.devices.outputs.digital_output import (
    DigitalOutput,
)


class GPIOFactory:

    @staticmethod
    def create_input(
        device_id,
        pin,
        pull_up=False,
    ):

        return DigitalInput(
            device_id=device_id,
            pin=pin,
            pull_up=pull_up,
        )

    @staticmethod
    def create_output(
        device_id,
        pin,
        initial=False,
    ):

        return DigitalOutput(
            device_id=device_id,
            pin=pin,
            initial=initial,
        )


gpio_factory = GPIOFactory()

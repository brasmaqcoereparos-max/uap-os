from app.modules.simulator.programming.simulator.devices.device_manager import (
    device_manager,
)

from app.modules.simulator.programming.simulator.devices.led_device import (
    LEDDevice,
)

from app.modules.simulator.programming.simulator.devices.button_device import (
    ButtonDevice,
)

from app.modules.simulator.programming.simulator.devices.potentiometer_device import (
    PotentiometerDevice,
)

from app.modules.simulator.programming.simulator.devices.relay_device import (
    RelayDevice,
)

from app.modules.simulator.programming.simulator.devices.buzzer_device import (
    BuzzerDevice,
)

from app.modules.simulator.programming.simulator.devices.servo_device import (
    ServoDevice,
)


class DeviceInitializer:

    initialized = False

    @classmethod
    def initialize(cls):

        if cls.initialized:

            return

        device_manager.add(

            LEDDevice(

                "LED",

                13,

            )

        )

        device_manager.add(

            ButtonDevice(

                "BUTTON",

                2,

            )

        )

        device_manager.add(

            PotentiometerDevice(

                "POT",

                34,

            )

        )

        device_manager.add(

            RelayDevice(

                "RELAY",

                5,

            )

        )

        device_manager.add(

            BuzzerDevice(

                "BUZZER",

                18,

            )

        )

        device_manager.add(

            ServoDevice(

                "SERVO",

                19,

            )

        )

        cls.initialized = True

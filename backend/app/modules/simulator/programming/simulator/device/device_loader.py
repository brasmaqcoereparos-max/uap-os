from app.modules.simulator.programming.simulator.devices.device_catalog import (
    device_catalog,
)

from app.modules.simulator.programming.simulator.devices.led_device import LEDDevice
from app.modules.simulator.programming.simulator.devices.button_device import ButtonDevice
from app.modules.simulator.programming.simulator.devices.relay_device import RelayDevice
from app.modules.simulator.programming.simulator.devices.buzzer_device import BuzzerDevice
from app.modules.simulator.programming.simulator.devices.servo_device import ServoDevice
from app.modules.simulator.programming.simulator.devices.potentiometer_device import (
    PotentiometerDevice,
)


class DeviceLoader:

    loaded = False

    @classmethod
    def load(cls):

        if cls.loaded:

            return

        device_catalog.register(

            "LED",

            LEDDevice,

        )

        device_catalog.register(

            "BUTTON",

            ButtonDevice,

        )

        device_catalog.register(

            "RELAY",

            RelayDevice,

        )

        device_catalog.register(

            "BUZZER",

            BuzzerDevice,

        )

        device_catalog.register(

            "SERVO",

            ServoDevice,

        )

        device_catalog.register(

            "POT",

            PotentiometerDevice,

        )

        cls.loaded = True

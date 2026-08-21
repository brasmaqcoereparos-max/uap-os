"""
Carregador central dos dispositivos disponíveis no UAP.
"""

from app.modules.simulator.programming.simulator.device.device_catalog import (
    device_catalog,
)

from app.modules.simulator.programming.simulator.device.led_device import (
    LEDDevice,
)
from app.modules.simulator.programming.simulator.device.button_device import (
    ButtonDevice,
)
from app.modules.simulator.programming.simulator.device.relay_device import (
    RelayDevice,
)
from app.modules.simulator.programming.simulator.device.buzzer_device import (
    BuzzerDevice,
)
from app.modules.simulator.programming.simulator.device.servo_device import (
    ServoDevice,
)
from app.modules.simulator.programming.simulator.device.potentiometer_device import (
    PotentiometerDevice,
)
from app.modules.simulator.programming.simulator.device.lora_device import (
    LoRaDevice,
)
from app.modules.simulator.programming.simulator.device.espnow_device import (
    ESPNowDevice,
)
from app.modules.simulator.programming.simulator.device.wifi_device import (
    WiFiDevice,
)
from app.modules.simulator.programming.simulator.device.bluetooth_device import (
    BluetoothDevice,
)
from app.modules.simulator.programming.simulator.device.mqtt_device import (
    MQTTDevice,
)
from app.modules.simulator.programming.simulator.device.can_device import (
    CANDevice,
)


class DeviceLoader:

    loaded = False

    @classmethod
    def load(cls):

        if cls.loaded:
            return

        devices = {
            "LED": LEDDevice,
            "BUTTON": ButtonDevice,
            "RELAY": RelayDevice,
            "BUZZER": BuzzerDevice,
            "SERVO": ServoDevice,
            "POT": PotentiometerDevice,
            "LORA": LoRaDevice,
            "ESPNOW": ESPNowDevice,
            "WIFI": WiFiDevice,
            "BLUETOOTH": BluetoothDevice,
            "MQTT": MQTTDevice,
            "CAN": CANDevice,
        }

        for name, device_class in devices.items():

            device_catalog.register(
                name,
                device_class,
            )

        cls.loaded = True

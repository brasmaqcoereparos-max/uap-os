"""
Carregamento do catálogo básico de dispositivos UAP.
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

    DEVICES = (
        (
            "LED",
            LEDDevice,
            "output",
            "LED digital",
            "lightbulb",
        ),
        (
            "BUTTON",
            ButtonDevice,
            "input",
            "Botão digital",
            "button",
        ),
        (
            "RELAY",
            RelayDevice,
            "output",
            "Relé digital",
            "relay",
        ),
        (
            "BUZZER",
            BuzzerDevice,
            "output",
            "Buzzer",
            "volume",
        ),
        (
            "SERVO",
            ServoDevice,
            "motion",
            "Servo motor",
            "servo",
        ),
        (
            "POT",
            PotentiometerDevice,
            "input",
            "Potenciômetro",
            "sliders",
        ),
        (
            "LORA",
            LoRaDevice,
            "communication",
            "Comunicação LoRa",
            "radio",
        ),
        (
            "ESPNOW",
            ESPNowDevice,
            "communication",
            "Comunicação ESP-NOW",
            "wifi",
        ),
        (
            "WIFI",
            WiFiDevice,
            "communication",
            "Wi-Fi",
            "wifi",
        ),
        (
            "BLUETOOTH",
            BluetoothDevice,
            "communication",
            "Bluetooth",
            "bluetooth",
        ),
        (
            "MQTT",
            MQTTDevice,
            "communication",
            "Cliente MQTT",
            "message",
        ),
        (
            "CAN",
            CANDevice,
            "communication",
            "Barramento CAN",
            "network",
        ),
    )

    @classmethod
    def load(
        cls,
        force=False,
    ):
        if cls.loaded and not force:
            return device_catalog.count()

        for (
            name,
            device_class,
            category,
            description,
            icon,
        ) in cls.DEVICES:
            device_catalog.register(
                name=name,
                device_class=device_class,
                category=category,
                description=description,
                icon=icon,
                replace=True,
            )

        cls.loaded = True

        return device_catalog.count()

    @classmethod
    def reload(cls):
        cls.loaded = False
        return cls.load(force=True)

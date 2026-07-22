from app.modules.simulator.programming.simulator.devices.device_manager import device_manager

from app.modules.simulator.programming.simulator.devices.led_device import LEDDevice
from app.modules.simulator.programming.simulator.devices.button_device import ButtonDevice
from app.modules.simulator.programming.simulator.devices.potentiometer_device import PotentiometerDevice
from app.modules.simulator.programming.simulator.devices.relay_device import RelayDevice
from app.modules.simulator.programming.simulator.devices.buzzer_device import BuzzerDevice
from app.modules.simulator.programming.simulator.devices.servo_device import ServoDevice
from app.modules.simulator.programming.simulator.devices.lcd16x2_device import LCD16x2Device
from app.modules.simulator.programming.simulator.devices.oled_device import OLEDDevice
from app.modules.simulator.programming.simulator.devices.seven_segment_device import SevenSegmentDevice
from app.modules.simulator.programming.simulator.devices.temperature_sensor_device import TemperatureSensorDevice


class DeviceInitializer:

    initialized = False

    @classmethod
    def initialize(cls):

        if cls.initialized:
            return

        device_manager.add(LEDDevice("LED", 13))
        device_manager.add(ButtonDevice("BUTTON", 2))
        device_manager.add(PotentiometerDevice("POT", 34))
        device_manager.add(RelayDevice("RELAY", 5))
        device_manager.add(BuzzerDevice("BUZZER", 18))
        device_manager.add(ServoDevice("SERVO", 19))

        device_manager.add(LCD16x2Device("LCD16X2"))
        device_manager.add(OLEDDevice("OLED"))
        device_manager.add(SevenSegmentDevice("DISPLAY7"))
        device_manager.add(TemperatureSensorDevice("TEMP"))

        cls.initialized = True

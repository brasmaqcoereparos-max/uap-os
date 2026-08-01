from app.modules.simulator.programming.simulator.devices.device_manager import device_manager

# GPIO
from app.modules.simulator.programming.simulator.devices.led_device import LEDDevice
from app.modules.simulator.programming.simulator.devices.button_device import ButtonDevice
from app.modules.simulator.programming.simulator.devices.potentiometer_device import PotentiometerDevice
from app.modules.simulator.programming.simulator.devices.relay_device import RelayDevice
from app.modules.simulator.programming.simulator.devices.buzzer_device import BuzzerDevice
from app.modules.simulator.programming.simulator.devices.servo_device import ServoDevice

# Displays
from app.modules.simulator.programming.simulator.devices.lcd16x2_device import LCD16x2Device
from app.modules.simulator.programming.simulator.devices.oled_device import OLEDDevice
from app.modules.simulator.programming.simulator.devices.seven_segment_device import SevenSegmentDevice

# Sensores
from app.modules.simulator.programming.simulator.devices.temperature_sensor_device import TemperatureSensorDevice
from app.modules.simulator.programming.simulator.devices.ultrasonic_sensor_device import UltrasonicSensorDevice
from app.modules.simulator.programming.simulator.devices.humidity_sensor_device import HumiditySensorDevice
from app.modules.simulator.programming.simulator.devices.pressure_sensor_device import PressureSensorDevice
from app.modules.simulator.programming.simulator.devices.light_sensor_device import LightSensorDevice
from app.modules.simulator.programming.simulator.devices.load_cell_device import LoadCellDevice

# Identificação
from app.modules.simulator.programming.simulator.devices.rfid_reader_device import RFIDReaderDevice
from app.modules.simulator.programming.simulator.devices.barcode_scanner_device import BarcodeScannerDevice
from app.modules.simulator.programming.simulator.devices.qr_reader_device import QRReaderDevice

# Atuadores
from app.modules.simulator.programming.simulator.devices.dc_motor_device import DCMotorDevice
from app.modules.simulator.programming.simulator.devices.stepper_motor_device import StepperMotorDevice
from app.modules.simulator.programming.simulator.devices.conveyor_device import ConveyorDevice
from app.modules.simulator.programming.simulator.devices.elevator_device import ElevatorDevice

# Comunicação
from app.modules.simulator.programming.simulator.devices.wifi_device import WiFiDevice
from app.modules.simulator.programming.simulator.devices.bluetooth_device import BluetoothDevice
from app.modules.simulator.programming.simulator.devices.mqtt_device import MQTTDevice
from app.modules.simulator.programming.simulator.devices.http_client_device import HTTPClientDevice

# Barramentos
from app.modules.simulator.programming.simulator.devices.i2c_device import I2CDevice
from app.modules.simulator.programming.simulator.devices.spi_device import SPIDevice
from app.modules.simulator.programming.simulator.devices.uart_device import UARTDevice
from app.modules.simulator.programming.simulator.devices.can_device import CANDevice

# Protocolos
from app.modules.simulator.programming.simulator.devices.modbus_rtu_device import ModbusRTUDevice
from app.modules.simulator.programming.simulator.devices.modbus_tcp_device import ModbusTCPDevice
from app.modules.simulator.programming.simulator.devices.lora_device import LoRaDevice
from app.modules.simulator.programming.simulator.devices.espnow_device import ESPNowDevice


class DeviceInitializer:

    initialized = False

    @classmethod
    def initialize(cls):

        if cls.initialized:
            return

        device_manager.add(LEDDevice("LED", 13))
        device_manager.add(ButtonDevice("BUTTON", 2))
        device_manager.add(RelayDevice("RELAY", 5))
        device_manager.add(BuzzerDevice("BUZZER", 18))
        device_manager.add(ServoDevice("SERVO", 19))
        device_manager.add(PotentiometerDevice("POT", 34))

        device_manager.add(LCD16x2Device("LCD16X2"))
        device_manager.add(OLEDDevice("OLED"))
        device_manager.add(SevenSegmentDevice("DISPLAY7"))

        device_manager.add(TemperatureSensorDevice("TEMP"))
        device_manager.add(UltrasonicSensorDevice("ULTRASONIC"))
        device_manager.add(HumiditySensorDevice("HUMIDITY"))
        device_manager.add(PressureSensorDevice("PRESSURE"))
        device_manager.add(LightSensorDevice("LIGHT"))
        device_manager.add(LoadCellDevice("LOAD_CELL"))

        device_manager.add(RFIDReaderDevice("RFID"))
        device_manager.add(BarcodeScannerDevice("BARCODE"))
        device_manager.add(QRReaderDevice("QR"))

        device_manager.add(DCMotorDevice("DC_MOTOR", 25))
        device_manager.add(StepperMotorDevice("STEPPER"))
        device_manager.add(ConveyorDevice("CONVEYOR"))
        device_manager.add(ElevatorDevice("ELEVATOR"))

        device_manager.add(WiFiDevice("WIFI"))
        device_manager.add(BluetoothDevice("BLUETOOTH"))
        device_manager.add(MQTTDevice("MQTT"))
        device_manager.add(HTTPClientDevice("HTTP"))

        device_manager.add(I2CDevice("I2C"))
        device_manager.add(SPIDevice("SPI"))
        device_manager.add(UARTDevice("UART"))
        device_manager.add(CANDevice("CAN"))

        device_manager.add(ModbusRTUDevice("MODBUS_RTU"))
        device_manager.add(ModbusTCPDevice("MODBUS_TCP"))
        device_manager.add(LoRaDevice("LORA"))
        device_manager.add(ESPNowDevice("ESPNOW"))

        cls.initialized = True

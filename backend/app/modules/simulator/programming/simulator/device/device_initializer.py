from app.modules.simulator.programming.simulator.device.device_manager import (
    device_manager,
)

from app.modules.simulator.programming.simulator.device.device_loader import (
    DeviceLoader,
)

from app.modules.simulator.programming.simulator.device.led_device import (
    LEDDevice,
)

from app.modules.simulator.programming.simulator.device.button_device import (
    ButtonDevice,
)

from app.modules.simulator.programming.simulator.device.potentiometer_device import (
    PotentiometerDevice,
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

from app.modules.simulator.programming.simulator.device.lcd16x2_device import (
    LCD16x2Device,
)

from app.modules.simulator.programming.simulator.device.oled_device import (
    OLEDDevice,
)

from app.modules.simulator.programming.simulator.device.seven_segment_device import (
    SevenSegmentDevice,
)

from app.modules.simulator.programming.simulator.device.temperature_sensor_device import (
    TemperatureSensorDevice,
)

from app.modules.simulator.programming.simulator.device.ultrasonic_sensor_device import (
    UltrasonicSensorDevice,
)

from app.modules.simulator.programming.simulator.device.humidity_sensor_device import (
    HumiditySensorDevice,
)

from app.modules.simulator.programming.simulator.device.pressure_sensor_device import (
    PressureSensorDevice,
)

from app.modules.simulator.programming.simulator.device.light_sensor_device import (
    LightSensorDevice,
)

from app.modules.simulator.programming.simulator.device.load_cell_device import (
    LoadCellDevice,
)

from app.modules.simulator.programming.simulator.device.barcode_scanner_device import (
    BarcodeScannerDevice,
)

from app.modules.simulator.programming.simulator.device.rfid_reader_device import (
    RFIDReaderDevice,
)

from app.modules.simulator.programming.simulator.device.qr_reader_device import (
    QRReaderDevice,
)

from app.modules.simulator.programming.simulator.device.dc_motor_device import (
    DCMotorDevice,
)

from app.modules.simulator.programming.simulator.device.stepper_motor_device import (
    StepperMotorDevice,
)

from app.modules.simulator.programming.simulator.device.conveyor_device import (
    ConveyorDevice,
)

from app.modules.simulator.programming.simulator.device.elevator_device import (
    ElevatorDevice,
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

from app.modules.simulator.programming.simulator.device.http_client_device import (
    HTTPClientDevice,
)

from app.modules.simulator.programming.simulator.device.i2c_device import (
    I2CDevice,
)

from app.modules.simulator.programming.simulator.device.spi_device import (
    SPIDevice,
)

from app.modules.simulator.programming.simulator.device.uart_device import (
    UARTDevice,
)

from app.modules.simulator.programming.simulator.device.can_device import (
    CANDevice,
)

from app.modules.simulator.programming.simulator.device.modbus_rtu_device import (
    ModbusRTUDevice,
)

from app.modules.simulator.programming.simulator.device.modbus_tcp_device import (
    ModbusTCPDevice,
)

from app.modules.simulator.programming.simulator.device.lora_device import (
    LoRaDevice,
)

from app.modules.simulator.programming.simulator.device.espnow_device import (
    ESPNowDevice,
)


class DeviceInitializer:

    initialized = False

    @classmethod
    def initialize(cls):
        if cls.initialized:
            return device_manager.count()

        DeviceLoader.load()

        devices = [
            LEDDevice(
                "LED",
                13,
            ),
            ButtonDevice(
                "BUTTON",
                2,
            ),
            RelayDevice(
                "RELAY",
                5,
            ),
            BuzzerDevice(
                "BUZZER",
                18,
            ),
            ServoDevice(
                "SERVO",
                19,
            ),
            PotentiometerDevice(
                "POT",
                34,
            ),
            LCD16x2Device(
                "LCD16X2"
            ),
            OLEDDevice(
                "OLED"
            ),
            SevenSegmentDevice(
                "DISPLAY7"
            ),
            TemperatureSensorDevice(
                "TEMP"
            ),
            UltrasonicSensorDevice(
                "ULTRASONIC"
            ),
            HumiditySensorDevice(
                "HUMIDITY"
            ),
            PressureSensorDevice(
                "PRESSURE"
            ),
            LightSensorDevice(
                "LIGHT"
            ),
            LoadCellDevice(
                "LOAD_CELL"
            ),
            BarcodeScannerDevice(
                "BARCODE"
            ),
            RFIDReaderDevice(
                "RFID"
            ),
            QRReaderDevice(
                "QR"
            ),
            DCMotorDevice(
                "DC_MOTOR",
                25,
            ),
            StepperMotorDevice(
                "STEPPER"
            ),
            ConveyorDevice(
                "CONVEYOR"
            ),
            ElevatorDevice(
                "ELEVATOR"
            ),
            WiFiDevice(
                "WIFI"
            ),
            BluetoothDevice(
                "BLUETOOTH"
            ),
            MQTTDevice(
                "MQTT"
            ),
            HTTPClientDevice(
                "HTTP"
            ),
            I2CDevice(
                "I2C"
            ),
            SPIDevice(
                "SPI"
            ),
            UARTDevice(
                "UART"
            ),
            CANDevice(
                "CAN"
            ),
            ModbusRTUDevice(
                "MODBUS_RTU"
            ),
            ModbusTCPDevice(
                "MODBUS_TCP"
            ),
            LoRaDevice(
                "LORA"
            ),
            ESPNowDevice(
                "ESPNOW"
            ),
        ]

        for device in devices:
            device_manager.add(
                device,
                replace=True,
            )

        cls.initialized = True

        return device_manager.count()

    @classmethod
    def reset(cls):
        device_manager.reset_all()
        device_manager.clear()

        cls.initialized = False

        return True

from app.modules.uhal.drivers.simulator import (
    SimulatorDriver,
)


class RaspberryPiDriver(SimulatorDriver):

    def __init__(self):

        super().__init__()

        self.board.name = "Raspberry Pi"
        self.board.manufacturer = (
            "Raspberry Pi Foundation"
        )

        self.board.capabilities.gpio = 40
        self.board.capabilities.pwm = 4
        self.board.capabilities.uart = 6
        self.board.capabilities.i2c = 7
        self.board.capabilities.spi = 6
        self.board.capabilities.ethernet = True
        self.board.capabilities.wifi = True
        self.board.capabilities.bluetooth = True

        self.hardware_mode = False
        self._gpio = None

    def initialize(self):

        if self.initialized:
            return True

        try:

            from gpiozero import Device
            from gpiozero.pins.lgpio import (
                LGPIOFactory,
            )

            Device.pin_factory = (
                LGPIOFactory()
            )

            self._gpio = Device
            self.hardware_mode = True

        except Exception:

            self._gpio = None
            self.hardware_mode = False

        self.initialized = True

        return True

    def shutdown(self):

        self._gpio = None
        self.hardware_mode = False
        self.initialized = False

        return True

    def connect(self):

        return self.initialize()

    def disconnect(self):

        return self.shutdown()

    def update(self):

        return True

    def digital_write(
        self,
        pin,
        value,
    ):

        if not self.initialized:
            self.initialize()

        if not self.hardware_mode:

            return super().digital_write(
                pin,
                value,
            )

        from gpiozero import DigitalOutputDevice

        output = DigitalOutputDevice(
            pin
        )

        try:

            if bool(value):
                output.on()
            else:
                output.off()

        finally:

            output.close()

        return True

    def digital_read(
        self,
        pin,
    ):

        if not self.initialized:
            self.initialize()

        if not self.hardware_mode:

            return super().digital_read(
                pin
            )

        from gpiozero import DigitalInputDevice

        input_device = DigitalInputDevice(
            pin
        )

        try:

            return int(
                bool(
                    input_device.value
                )
            )

        finally:

            input_device.close()

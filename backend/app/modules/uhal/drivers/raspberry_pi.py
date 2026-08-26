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
        self._gpiozero_device = None

    def initialize(self):
        if self.initialized:
            return True

        try:
            from gpiozero import Device
            from gpiozero.pins.lgpio import (
                LGPIOFactory,
            )

            Device.pin_factory = LGPIOFactory()

            self._gpiozero_device = Device
            self.hardware_mode = True

        except Exception:
            self._gpiozero_device = None
            self.hardware_mode = False

        self.initialized = True

        return True

    def shutdown(self):
        self._gpiozero_device = None
        self.hardware_mode = False

        return super().shutdown()

    def pin_mode(self, pin, mode):
        if not self.hardware_mode:
            return super().pin_mode(
                pin,
                mode,
            )

        mode = str(mode).lower()

        if mode in {
            "output",
            "out",
        }:
            self.pins[pin] = {
                "mode": "output",
                "value": 0,
            }

        elif mode in {
            "input",
            "in",
            "input_pullup",
        }:
            self.pins[pin] = {
                "mode": "input",
                "value": 0,
            }

        else:
            raise ValueError(
                f"Modo GPIO inválido: {mode}"
            )

        return True

    def digital_write(self, pin, value):
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

    def digital_read(self, pin):
        if not self.initialized:
            self.initialize()

        if not self.hardware_mode:
            return super().digital_read(pin)

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

    def analog_write(self, pin, value):
        return self.digital_write(
            pin,
            value,
        )

    def analog_read(self, pin):
        return self.digital_read(pin)

    def pwm_write(self, pin, duty):
        if not self.hardware_mode:
            return super().pwm_write(
                pin,
                duty,
            )

        from gpiozero import PWMOutputDevice

        output = PWMOutputDevice(
            pin
        )

        try:
            output.value = max(
                0.0,
                min(
                    1.0,
                    float(duty),
                ),
            )

        finally:
            output.close()

        return True

    def pwm_frequency(
        self,
        pin,
        frequency,
    ):
        return True

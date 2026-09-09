class BoardCapabilities:

    _FIELDS = (
        "gpio",
        "pwm",
        "adc",
        "dac",
        "uart",
        "i2c",
        "spi",
        "can",
        "ethernet",
        "wifi",
        "bluetooth",
        "usb",
        "sd_card",
        "display",
        "camera",
    )

    def __init__(self):

        self.gpio = 0

        self.pwm = 0

        self.adc = 0

        self.dac = 0

        self.uart = 0

        self.i2c = 0

        self.spi = 0

        self.can = False

        self.ethernet = False

        self.wifi = False

        self.bluetooth = False

        self.usb = False

        self.sd_card = False

        self.display = False

        self.camera = False

    def get(
        self,
        name,
        default=None,
    ):

        key = str(
            name or ""
        ).strip().lower()

        if key not in self._FIELDS:
            return default

        return getattr(
            self,
            key,
        )

    def supports(
        self,
        name,
    ):

        value = self.get(
            name,
            None,
        )

        if value is None:
            return False

        if isinstance(
            value,
            bool,
        ):
            return value

        if isinstance(
            value,
            (
                int,
                float,
            ),
        ):
            return value > 0

        return bool(
            value
        )

    def available(self):

        return [
            name
            for name in self._FIELDS
            if self.supports(name)
        ]

    def to_dict(self):

        return {
            name: getattr(
                self,
                name,
            )
            for name in self._FIELDS
        }

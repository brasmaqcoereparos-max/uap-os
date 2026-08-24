"""
Targets suportados pelo compilador UAP.
"""


class CompilerTarget:

    ARDUINO = "arduino"
    ESP32 = "esp32"
    RP2040 = "rp2040"
    STM32 = "stm32"
    PYTHON = "python"
    MICROPYTHON = "micropython"
    RASPBERRY = "raspberry"
    JSON = "json"
    TEXT = "text"

    @classmethod
    def all(cls):

        return [
            cls.ARDUINO,
            cls.ESP32,
            cls.RP2040,
            cls.STM32,
            cls.PYTHON,
            cls.MICROPYTHON,
            cls.RASPBERRY,
            cls.JSON,
            cls.TEXT,
        ]

    @classmethod
    def normalize(
        cls,
        target,
    ):

        if target is None:
            raise ValueError(
                "Target do compilador não informado."
            )

        value = str(
            target
        ).strip().lower()

        aliases = {
            "arduino": cls.ARDUINO,
            "uno": cls.ARDUINO,
            "arduino_uno": cls.ARDUINO,

            "esp32": cls.ESP32,

            "rp2040": cls.RP2040,
            "raspberry_pi_pico": cls.RP2040,
            "pico": cls.RP2040,

            "stm32": cls.STM32,

            "python": cls.PYTHON,

            "micropython": cls.MICROPYTHON,

            "raspberry": cls.RASPBERRY,
            "raspberry_pi": cls.RASPBERRY,
            "raspberrypi": cls.RASPBERRY,

            "json": cls.JSON,

            "text": cls.TEXT,
        }

        normalized = aliases.get(
            value
        )

        if normalized is None:
            raise ValueError(
                f"Target não suportado: {target}"
            )

        return normalized

    @classmethod
    def is_supported(
        cls,
        target,
    ):

        try:
            cls.normalize(
                target
            )
            return True

        except ValueError:
            return False

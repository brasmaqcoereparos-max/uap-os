import os
import platform

from pathlib import Path


class BoardDetector:

    ENVIRONMENT_KEYS = (
        "UAP_BOARD",
        "UAP_BOARD_TYPE",
    )

    ALIASES = {
        "sim": "simulator",
        "simulation": "simulator",
        "simulator": "simulator",

        "esp32": "esp32",

        "esp32-c3": "esp32_c3",
        "esp32_c3": "esp32_c3",

        "esp32-s3": "esp32_s3",
        "esp32_s3": "esp32_s3",

        "esp8266": "esp8266",

        "arduino": "arduino_uno",
        "arduino-uno": "arduino_uno",
        "arduino_uno": "arduino_uno",
        "uno": "arduino_uno",

        "arduino-nano": (
            "arduino_nano"
        ),
        "arduino_nano": (
            "arduino_nano"
        ),
        "nano": "arduino_nano",

        "arduino-mega": (
            "arduino_mega"
        ),
        "arduino_mega": (
            "arduino_mega"
        ),
        "mega": "arduino_mega",

        "raspberry-pi": (
            "raspberry_pi"
        ),
        "raspberry_pi": (
            "raspberry_pi"
        ),
        "rpi": "raspberry_pi",

        "raspberry-pi-pico": (
            "raspberry_pico"
        ),
        "raspberry_pico": (
            "raspberry_pico"
        ),
        "pico": (
            "raspberry_pico"
        ),

        "stm32": "stm32",

        "teensy": "teensy",

        "beaglebone": (
            "beaglebone"
        ),
        "beaglebone-black": (
            "beaglebone"
        ),
    }

    def normalize(
        self,
        name,
    ):

        if name is None:
            return None

        key = str(
            name
        ).strip().lower()

        key = key.replace(
            " ",
            "-",
        )

        return self.ALIASES.get(
            key,
            key.replace(
                "-",
                "_",
            ),
        )

    def _environment_board(
        self,
    ):

        for key in self.ENVIRONMENT_KEYS:

            value = os.getenv(
                key
            )

            if (
                value
                and value.strip()
            ):
                return self.normalize(
                    value
                )

        return None

    def _raspberry_pi_model(
        self,
    ):

        if (
            platform.system()
            .lower()
            != "linux"
        ):
            return False

        model_path = Path(
            "/proc/device-tree/model"
        )

        try:

            model = (
                model_path
                .read_text(
                    encoding="utf-8",
                    errors="ignore",
                )
            )

        except (
            OSError,
            UnicodeError,
        ):
            return False

        return (
            "raspberry pi"
            in model.lower()
        )

    def detect(
        self,
        preferred=None,
    ):

        if preferred is not None:

            return self.normalize(
                preferred
            )

        environment_board = (
            self._environment_board()
        )

        if (
            environment_board
            is not None
        ):
            return environment_board

        if self._raspberry_pi_model():

            return "raspberry_pi"

        return "simulator"


board_detector = BoardDetector()

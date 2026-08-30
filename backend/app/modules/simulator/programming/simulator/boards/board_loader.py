"""
Loader das placas padrão do simulador UAP.
"""

from app.modules.simulator.programming.simulator.boards.board_manager import (
    board_manager,
)

from app.modules.simulator.programming.simulator.boards.arduino_uno import (
    ArduinoUNO,
)

from app.modules.simulator.programming.simulator.boards.arduino_mega2560 import (
    ArduinoMega2560,
)

from app.modules.simulator.programming.simulator.boards.esp32_devkit import (
    ESP32DevKit,
)

from app.modules.simulator.programming.simulator.boards.esp8266 import (
    ESP8266,
)

from app.modules.simulator.programming.simulator.boards.raspberry_pi_pico import (
    RaspberryPiPico,
)


class BoardLoader:

    loaded = False

    boards = {
        "arduino_uno": (
            ArduinoUNO
        ),
        "arduino_mega2560": (
            ArduinoMega2560
        ),
        "esp32_devkit": (
            ESP32DevKit
        ),
        "esp8266": ESP8266,
        "raspberry_pi_pico": (
            RaspberryPiPico
        ),
    }

    aliases = {
        "uno": "arduino_uno",
        "mega": (
            "arduino_mega2560"
        ),
        "mega2560": (
            "arduino_mega2560"
        ),
        "esp32": (
            "esp32_devkit"
        ),
        "pico": (
            "raspberry_pi_pico"
        ),
        "rp2040": (
            "raspberry_pi_pico"
        ),
    }

    @classmethod
    def resolve(
        cls,
        board_name,
    ):
        key = str(
            board_name
        ).strip()

        if key in cls.boards:
            return key

        if key in cls.aliases:
            return cls.aliases[
                key
            ]

        lowered = key.lower()

        for name in cls.boards:
            if (
                name.lower()
                == lowered
            ):
                return name

        for alias, target in (
            cls.aliases.items()
        ):
            if (
                alias.lower()
                == lowered
            ):
                return target

        return None

    @classmethod
    def load(
        cls,
        default_board="arduino_uno",
    ):
        if cls.loaded:
            return (
                board_manager.get_board()
            )

        board = cls.create(
            default_board
        )

        board_manager.set_board(
            board
        )

        cls.loaded = True

        return board

    @classmethod
    def create(
        cls,
        board_name,
        *args,
        **kwargs,
    ):
        key = cls.resolve(
            board_name
        )

        if key is None:
            raise ValueError(
                f"Placa '{board_name}' "
                "não encontrada."
            )

        board_class = (
            cls.boards[key]
        )

        return board_class(
            *args,
            **kwargs,
        )

    @classmethod
    def register(
        cls,
        name,
        board_class,
        aliases=None,
        replace=True,
    ):
        name = str(name)

        if (
            name in cls.boards
            and not replace
        ):
            raise ValueError(
                f"Placa já registrada: {name}"
            )

        cls.boards[
            name
        ] = board_class

        for alias in (
            aliases or []
        ):
            cls.aliases[
                str(alias)
            ] = name

        return board_class

    @classmethod
    def unregister(
        cls,
        name,
    ):
        key = cls.resolve(
            name
        )

        if key is None:
            return None

        board_class = (
            cls.boards.pop(
                key,
                None,
            )
        )

        for alias, target in list(
            cls.aliases.items()
        ):
            if target == key:
                cls.aliases.pop(
                    alias,
                    None,
                )

        return board_class

    @classmethod
    def available(cls):
        return list(
            cls.boards.keys()
        )

    @classmethod
    def classes(cls):
        return cls.boards.copy()

    @classmethod
    def reset(cls):
        cls.loaded = False

        board_manager.clear_current()

        return True

    @classmethod
    def status(cls):
        return {
            "loaded": cls.loaded,
            "available": (
                cls.available()
            ),
            "current": (
                getattr(
                    board_manager.get_board(),
                    "name",
                    None,
                )
            ),
                }

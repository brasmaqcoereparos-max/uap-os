"""
Serviço público do simulador UAP.

Esta camada conecta:
- API REST;
- placas virtuais;
- atuadores virtuais;
- sensores virtuais.

Contratos existentes preservados.
"""

from app.modules.simulator.devices.virtual_led import (
    VirtualLED,
)
from app.modules.simulator.devices.virtual_button import (
    VirtualButton,
)
from app.modules.simulator.devices.virtual_relay import (
    VirtualRelay,
)

from app.modules.simulator.components.virtual_temperature import (
    VirtualTemperature,
)
from app.modules.simulator.components.virtual_humidity import (
    VirtualHumidity,
)
from app.modules.simulator.components.virtual_ultrasonic import (
    VirtualUltrasonic,
)

from app.modules.simulator.boards.arduino_uno import (
    ArduinoUNO,
)
from app.modules.simulator.boards.esp32 import (
    ESP32Board,
)
from app.modules.simulator.boards.raspberry_pi import (
    RaspberryPiBoard,
)


class SimulatorService:

    def __init__(self):
        self.devices = {}
        self.boards = {}

        self.update_count = 0
        self.error_count = 0

        self.last_error = None

    # =====================================================
    # REGISTRO
    # =====================================================

    def add(
        self,
        device,
        replace=True,
    ):
        if device is None:
            return None

        device_id = getattr(
            device,
            "id",
            None,
        )

        if device_id is None:
            raise ValueError(
                "Dispositivo precisa possuir id."
            )

        if (
            device_id in self.devices
            and not replace
        ):
            return self.devices[
                device_id
            ]

        self.devices[
            device_id
        ] = device

        return device

    def add_board(
        self,
        board,
        replace=True,
    ):
        if board is None:
            return None

        board_id = getattr(
            board,
            "id",
            None,
        )

        if board_id is None:
            raise ValueError(
                "Placa precisa possuir id."
            )

        if (
            board_id in self.boards
            and not replace
        ):
            return self.boards[
                board_id
            ]

        self.boards[
            board_id
        ] = board

        return board

    # =====================================================
    # PLACAS
    # =====================================================

    def create_arduino(
        self,
        board_id: str,
        name: str,
    ):
        board = ArduinoUNO(
            board_id,
            name,
        )

        self.add_board(
            board
        )

        return board.status()

    def create_esp32(
        self,
        board_id: str,
        name: str,
    ):
        board = ESP32Board(
            board_id,
            name,
        )

        self.add_board(
            board
        )

        return board.status()

    def create_raspberry(
        self,
        board_id: str,
        name: str,
    ):
        board = RaspberryPiBoard(
            board_id,
            name,
        )

        self.add_board(
            board
        )

        return board.status()

    def list_boards(self):
        return [
            board.status()
            for board
            in self.boards.values()
        ]

    def get_board(
        self,
        board_id,
    ):
        board = self.boards.get(
            board_id
        )

        if board is None:
            return None

        return board.status()

    def remove_board(
        self,
        board_id,
    ):
        board = self.boards.pop(
            board_id,
            None,
        )

        return (
            board is not None
        )

    def clear_boards(self):
        count = len(
            self.boards
        )

        self.boards.clear()

        return count

    # =====================================================
    # ATUADORES
    # =====================================================

    def create_led(
        self,
        device_id,
        name,
    ):
        obj = VirtualLED(
            device_id,
            name,
        )

        self.add(obj)

        return obj.status()

    def create_button(
        self,
        device_id,
        name,
    ):
        obj = VirtualButton(
            device_id,
            name,
        )

        self.add(obj)

        return obj.status()

    def create_relay(
        self,
        device_id,
        name,
    ):
        obj = VirtualRelay(
            device_id,
            name,
        )

        self.add(obj)

        return obj.status()

    # =====================================================
    # SENSORES
    # =====================================================

    def create_temperature(
        self,
        device_id,
        name,
    ):
        obj = VirtualTemperature(
            device_id,
            name,
        )

        self.add(obj)

        return obj.status()

    def create_humidity(
        self,
        device_id,
        name,
    ):
        obj = VirtualHumidity(
            device_id,
            name,
        )

        self.add(obj)

        return obj.status()

    def create_ultrasonic(
        self,
        device_id,
        name,
    ):
        obj = VirtualUltrasonic(
            device_id,
            name,
        )

        self.add(obj)

        return obj.status()

    # =====================================================
    # EXECUÇÃO
    # =====================================================

    def update(self):
        results = {}

        try:
            for device_id, device in list(
                self.devices.items()
            ):
                update = getattr(
                    device,
                    "update",
                    None,
                )

                if callable(update):
                    results[
                        device_id
                    ] = update()

            self.update_count += 1

            self.last_error = None

            return results

        except Exception as exc:
            self.error_count += 1
            self.last_error = str(exc)

            raise

    def list(self):
        self.update()

        return [
            device.status()
            for device
            in self.devices.values()
        ]

    def get(
        self,
        device_id,
    ):
        device = self.devices.get(
            device_id
        )

        if device is None:
            return None

        update = getattr(
            device,
            "update",
            None,
        )

        if callable(update):
            update()

        return device.status()

    def remove(
        self,
        device_id,
    ):
        device = self.devices.pop(
            device_id,
            None,
        )

        return (
            device is not None
        )

    def clear(self):
        count = len(
            self.devices
        )

        self.devices.clear()

        return count

    # =====================================================
    # CONTROLE
    # =====================================================

    def turn_on(
        self,
        device_id,
    ):
        device = self.devices.get(
            device_id
        )

        if (
            device is not None
            and hasattr(
                device,
                "on",
            )
        ):
            device.on()

        return self.get(
            device_id
        )

    def turn_off(
        self,
        device_id,
    ):
        device = self.devices.get(
            device_id
        )

        if (
            device is not None
            and hasattr(
                device,
                "off",
            )
        ):
            device.off()

        return self.get(
            device_id
        )

    def toggle(
        self,
        device_id,
    ):
        device = self.devices.get(
            device_id
        )

        if (
            device is not None
            and hasattr(
                device,
                "toggle",
            )
        ):
            device.toggle()

        return self.get(
            device_id
        )

    # =====================================================
    # DIAGNÓSTICO
    # =====================================================

    def device_count(self):
        return len(
            self.devices
        )

    def board_count(self):
        return len(
            self.boards
        )

    def reset(self):
        for device in (
            self.devices.values()
        ):
            reset = getattr(
                device,
                "reset",
                None,
            )

            if callable(reset):
                reset()

        for board in (
            self.boards.values()
        ):
            reset = getattr(
                board,
                "reset",
                None,
            )

            if callable(reset):
                reset()

        self.update_count = 0
        self.error_count = 0
        self.last_error = None

        return True

    def status(self):
        return {
            "device_count": (
                self.device_count()
            ),
            "board_count": (
                self.board_count()
            ),
            "update_count": (
                self.update_count
            ),
            "error_count": (
                self.error_count
            ),
            "last_error": (
                self.last_error
            ),
        }


simulator_service = SimulatorService()

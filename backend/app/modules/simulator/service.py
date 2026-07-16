from app.modules.simulator.devices.virtual_led import VirtualLED
from app.modules.simulator.devices.virtual_button import VirtualButton
from app.modules.simulator.devices.virtual_relay import VirtualRelay

from app.modules.simulator.components.virtual_temperature import (
    VirtualTemperature,
)
from app.modules.simulator.components.virtual_humidity import (
    VirtualHumidity,
)
from app.modules.simulator.components.virtual_ultrasonic import (
    VirtualUltrasonic,
)

from app.modules.simulator.boards.arduino_uno import ArduinoUNO
from app.modules.simulator.boards.esp32 import ESP32Board
from app.modules.simulator.boards.raspberry_pi import RaspberryPiBoard


class SimulatorService:

    def __init__(self):
        self.devices = {}
        self.boards = {}

    # ------------------------
    # Registro
    # ------------------------

    def add(self, device):
        self.devices[device.id] = device

    def add_board(self, board):
        self.boards[board.id] = board

    # ------------------------
    # Placas
    # ------------------------

    def create_arduino(
        self,
        board_id: str,
        name: str,
    ):
        board = ArduinoUNO(board_id, name)
        self.add_board(board)
        return board.status()

    def create_esp32(
        self,
        board_id: str,
        name: str,
    ):
        board = ESP32Board(board_id, name)
        self.add_board(board)
        return board.status()

    def create_raspberry(
        self,
        board_id: str,
        name: str,
    ):
        board = RaspberryPiBoard(board_id, name)
        self.add_board(board)
        return board.status()

    def list_boards(self):
        return [
            board.status()
            for board in self.boards.values()
        ]

    def get_board(self, board_id):
        board = self.boards.get(board_id)

        if board:
            return board.status()

        return None

    # ------------------------
    # Atuadores
    # ------------------------

    def create_led(self, device_id, name):
        obj = VirtualLED(device_id, name)
        self.add(obj)
        return obj.status()

    def create_button(self, device_id, name):
        obj = VirtualButton(device_id, name)
        self.add(obj)
        return obj.status()

    def create_relay(self, device_id, name):
        obj = VirtualRelay(device_id, name)
        self.add(obj)
        return obj.status()

    # ------------------------
    # Sensores
    # ------------------------

    def create_temperature(self, device_id, name):
        obj = VirtualTemperature(device_id, name)
        self.add(obj)
        return obj.status()

    def create_humidity(self, device_id, name):
        obj = VirtualHumidity(device_id, name)
        self.add(obj)
        return obj.status()

    def create_ultrasonic(self, device_id, name):
        obj = VirtualUltrasonic(device_id, name)
        self.add(obj)
        return obj.status()

    # ------------------------

    def update(self):
        for device in self.devices.values():
            if hasattr(device, "update"):
                device.update()

    def list(self):
        self.update()

        return [
            device.status()
            for device in self.devices.values()
        ]

    def get(self, device_id):
        device = self.devices.get(device_id)

        if device:
            if hasattr(device, "update"):
                device.update()

            return device.status()

        return None

    def remove(self, device_id):
        if device_id in self.devices:
            del self.devices[device_id]

    def turn_on(self, device_id):
        device = self.devices.get(device_id)

        if device and hasattr(device, "on"):
            device.on()

        return self.get(device_id)

    def turn_off(self, device_id):
        device = self.devices.get(device_id)

        if device and hasattr(device, "off"):
            device.off()

        return self.get(device_id)

    def toggle(self, device_id):
        device = self.devices.get(device_id)

        if device and hasattr(device, "toggle"):
            device.toggle()

        return self.get(device_id)


simulator_service = SimulatorService()

class BlockLibrary:

    def __init__(self):

        self.blocks = {

            # =====================================================
            # CONTROLE
            # =====================================================

            "start": {
                "name": "Start",
                "category": "Control",
                "color": "#2ecc71",
                "icon": "play",
                "inputs": 0,
                "outputs": 1,
                "properties": {},
            },

            "delay": {
                "name": "Delay",
                "category": "Control",
                "color": "#f39c12",
                "icon": "clock",
                "inputs": 1,
                "outputs": 1,
                "properties": {
                    "milliseconds": 1000,
                },
            },

            "if": {
                "name": "If",
                "category": "Logic",
                "color": "#3498db",
                "icon": "git-branch",
                "inputs": 1,
                "outputs": 2,
                "properties": {
                    "variable": "",
                    "value": 0,
                },
            },

            "loop": {
                "name": "Loop",
                "category": "Logic",
                "color": "#9b59b6",
                "icon": "repeat",
                "inputs": 1,
                "outputs": 1,
                "properties": {
                    "count": 10,
                },
            },

            # =====================================================
            # GPIO
            # =====================================================

            "digital_write": {
                "name": "Digital Write",
                "category": "GPIO",
                "color": "#e74c3c",
                "icon": "toggle-right",
                "inputs": 1,
                "outputs": 1,
                "properties": {
                    "pin": 13,
                    "value": 1,
                },
            },

            "digital_read": {
                "name": "Digital Read",
                "category": "GPIO",
                "color": "#16a085",
                "icon": "radio",
                "inputs": 1,
                "outputs": 1,
                "properties": {
                    "pin": 2,
                },
            },

            "analog_write": {
                "name": "Analog Write",
                "category": "GPIO",
                "color": "#d35400",
                "icon": "sliders",
                "inputs": 1,
                "outputs": 1,
                "properties": {
                    "pin": 5,
                    "value": 255,
                },
            },

            "analog_read": {
                "name": "Analog Read",
                "category": "GPIO",
                "color": "#2980b9",
                "icon": "activity",
                "inputs": 1,
                "outputs": 1,
                "properties": {
                    "pin": 34,
                },
            },

            # =====================================================
            # SENSORES
            # =====================================================

            "temperature": {
                "name": "Temperature",
                "category": "Sensors",
                "color": "#ff6b6b",
                "icon": "thermometer",
                "inputs": 0,
                "outputs": 1,
                "properties": {},
            },

            "humidity": {
                "name": "Humidity",
                "category": "Sensors",
                "color": "#3498db",
                "icon": "droplets",
                "inputs": 0,
                "outputs": 1,
                "properties": {},
            },

            "ultrasonic": {
                "name": "Ultrasonic",
                "category": "Sensors",
                "color": "#8e44ad",
                "icon": "wifi",
                "inputs": 0,
                "outputs": 1,
                "properties": {},
            },

            # =====================================================
            # ATUADORES
            # =====================================================

            "led": {
                "name": "LED",
                "category": "Actuators",
                "color": "#f1c40f",
                "icon": "lightbulb",
                "inputs": 1,
                "outputs": 0,
                "properties": {},
            },

            "relay": {
                "name": "Relay",
                "category": "Actuators",
                "color": "#34495e",
                "icon": "cpu",
                "inputs": 1,
                "outputs": 0,
                "properties": {},
            },

            "button": {
                "name": "Button",
                "category": "Inputs",
                "color": "#27ae60",
                "icon": "mouse-pointer",
                "inputs": 0,
                "outputs": 1,
                "properties": {},
            },
        }

    def all(self):
        return self.blocks

    def get(self, block_type):
        return self.blocks.get(block_type)


block_library = BlockLibrary()

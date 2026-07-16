class BlockLibrary:

    def __init__(self):

        self.blocks = {
            "start": {
                "name": "Start",
                "category": "Control",
                "color": "#2ecc71",
                "inputs": [],
                "outputs": 1,
            },
            "delay": {
                "name": "Delay",
                "category": "Control",
                "color": "#f39c12",
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
                "inputs": 1,
                "outputs": 1,
                "properties": {
                    "count": 10,
                },
            },
            "digital_write": {
                "name": "Digital Write",
                "category": "GPIO",
                "color": "#e74c3c",
                "inputs": 1,
                "outputs": 1,
                "properties": {
                    "pin": 0,
                    "value": 1,
                },
            },
            "digital_read": {
                "name": "Digital Read",
                "category": "GPIO",
                "color": "#16a085",
                "inputs": 1,
                "outputs": 1,
                "properties": {
                    "pin": 0,
                },
            },
            "analog_write": {
                "name": "Analog Write",
                "category": "GPIO",
                "color": "#d35400",
                "inputs": 1,
                "outputs": 1,
                "properties": {
                    "pin": 0,
                    "value": 0,
                },
            },
            "analog_read": {
                "name": "Analog Read",
                "category": "GPIO",
                "color": "#2980b9",
                "inputs": 1,
                "outputs": 1,
                "properties": {
                    "pin": 0,
                },
            },
        }

    def all(self):
        return self.blocks

    def get(self, block_type):
        return self.blocks.get(block_type)


block_library = BlockLibrary()

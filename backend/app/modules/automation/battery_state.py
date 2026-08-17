class BatteryState:

    def __init__(self):

        self.level = 100
        self.voltage = 0
        self.charging = False

    def update(
        self,
        level,
        voltage=None,
    ):

        self.level = max(
            0,
            min(100, level),
        )

        if voltage is not None:
            self.voltage = voltage

    def set_charging(self, charging):

        self.charging = charging

    def get(self):

        return {
            "level": self.level,
            "voltage": self.voltage,
            "charging": self.charging,
        }

    def is_low(self, threshold=20):

        return self.level <= threshold

    def is_critical(self, threshold=10):

        return self.level <= threshold

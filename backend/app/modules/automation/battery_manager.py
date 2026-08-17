from app.modules.automation.battery_state import (
    BatteryState,
)


class BatteryManager:

    def __init__(self):

        self.state = BatteryState()

    def update(
        self,
        level,
        voltage=None,
    ):

        self.state.update(
            level,
            voltage,
        )

    def get_state(self):

        return self.state.get()

    def is_low(self):

        return self.state.is_low()

    def is_critical(self):

        return self.state.is_critical()

    def set_charging(self, charging):

        self.state.set_charging(
            charging
        )


battery_manager = BatteryManager()

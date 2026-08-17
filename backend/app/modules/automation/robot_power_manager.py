class RobotPowerManager:

    def __init__(
        self,
        battery,
        return_to_base,
        docking,
    ):

        self.battery = battery
        self.return_to_base = return_to_base
        self.docking = docking

    def update(self):

        if self.battery.is_critical():

            self.return_to_base.start()

            return "critical_return"

        if self.battery.is_low():

            self.return_to_base.start()

            return "low_battery_return"

        return "normal"

    def get_status(self):

        return {
            "battery":
                self.battery.get_state(),
            "returning":
                self.return_to_base.is_active(),
            "docking":
                self.docking.is_active(),
        }

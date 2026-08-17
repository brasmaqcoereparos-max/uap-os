class AutoChargeController:

    def __init__(
        self,
        battery,
        docking,
    ):

        self.battery = battery
        self.docking = docking

    def should_return(self):

        return (
            self.battery.is_low()
            or self.battery.is_critical()
        )

    def start_docking(self):

        return self.docking.start()

    def is_charging(self):

        return (
            self.battery.get_state()
            ["charging"]
        )

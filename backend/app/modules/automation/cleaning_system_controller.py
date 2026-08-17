class CleaningSystemController:

    def __init__(
        self,
        brush=None,
        vacuum=None,
        pump=None,
        dryer=None,
    ):

        self.brush = brush
        self.vacuum = vacuum
        self.pump = pump
        self.dryer = dryer

    def start_vacuum_cleaning(
        self,
        power=70,
    ):

        if self.brush is not None:

            self.brush.enable()
            self.brush.set_power(50)

        if self.vacuum is not None:

            self.vacuum.enable()
            self.vacuum.set_power(power)

    def start_wet_cleaning(
        self,
        water_power=50,
        detergent_power=30,
    ):

        if self.pump is not None:

            self.pump.water_on(
                water_power
            )

            self.pump.detergent_on(
                detergent_power
            )

        if self.brush is not None:

            self.brush.enable()
            self.brush.set_power(50)

    def stop_cleaning(self):

        if self.brush is not None:
            self.brush.disable()

        if self.vacuum is not None:
            self.vacuum.disable()

        if self.pump is not None:

            self.pump.water_off()
            self.pump.detergent_off()

        if self.dryer is not None:
            self.dryer.disable()

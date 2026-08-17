class CleaningPumpController:

    def __init__(self, water=None, detergent=None):

        self.water = water
        self.detergent = detergent

    def water_on(self, power=50):

        if self.water is None:
            return False

        self.water.enable()
        self.water.set_power(power)

        return True

    def water_off(self):

        if self.water is None:
            return False

        self.water.disable()

        return True

    def detergent_on(self, power=30):

        if self.detergent is None:
            return False

        self.detergent.enable()
        self.detergent.set_power(power)

        return True

    def detergent_off(self):

        if self.detergent is None:
            return False

        self.detergent.disable()

        return True

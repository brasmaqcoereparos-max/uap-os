class CleaningBrushController:

    def __init__(self, actuator):

        self.actuator = actuator

    def start(self, power=50):

        self.actuator.enable()
        self.actuator.set_power(power)

    def stop(self):

        self.actuator.disable()

    def set_power(self, power):

        self.actuator.set_power(power)

    def get_power(self):

        return self.actuator.get_power()

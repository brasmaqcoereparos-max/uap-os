class CleaningVacuumController:

    def __init__(self, actuator):

        self.actuator = actuator

    def start(self, power=70):

        self.actuator.enable()
        self.actuator.set_power(power)

    def stop(self):

        self.actuator.disable()

    def set_power(self, power):

        self.actuator.set_power(power)

    def is_running(self):

        return self.actuator.is_enabled()

class CleaningActuatorManager:

    def __init__(self):

        self.actuators = {}

    def add(self, actuator):

        self.actuators[
            actuator.actuator_id
        ] = actuator

        return actuator

    def remove(self, actuator_id):

        if actuator_id not in self.actuators:
            return False

        self.actuators.pop(actuator_id)

        return True

    def get(self, actuator_id):

        return self.actuators.get(
            actuator_id
        )

    def enable(self, actuator_id):

        actuator = self.get(actuator_id)

        if actuator is None:
            return False

        actuator.enable()

        return True

    def disable(self, actuator_id):

        actuator = self.get(actuator_id)

        if actuator is None:
            return False

        actuator.disable()

        return True

    def get_all(self):

        return dict(self.actuators)

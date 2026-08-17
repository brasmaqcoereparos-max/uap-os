class SensorState:

    def __init__(self):

        self.states = {}

    def update(
        self,
        sensor_id,
        value,
    ):

        self.states[sensor_id] = {
            "value": value,
            "active": True,
        }

    def deactivate(
        self,
        sensor_id,
    ):

        if sensor_id not in self.states:

            return False

        self.states[
            sensor_id
        ]["active"] = False

        return True

    def get(
        self,
        sensor_id,
    ):

        return self.states.get(
            sensor_id
        )

    def get_all(self):

        return dict(
            self.states
        )

    def clear(self):

        self.states.clear()


sensor_state = SensorState()

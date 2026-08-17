class SensorRegistry:

    def __init__(self):

        self.sensors = {}

    def register(
        self,
        sensor_id,
        sensor,
    ):

        self.sensors[sensor_id] = sensor

        return sensor

    def unregister(
        self,
        sensor_id,
    ):

        if sensor_id not in self.sensors:

            return False

        self.sensors.pop(
            sensor_id
        )

        return True

    def get(
        self,
        sensor_id,
    ):

        return self.sensors.get(
            sensor_id
        )

    def exists(
        self,
        sensor_id,
    ):

        return sensor_id in self.sensors

    def get_all(self):

        return dict(
            self.sensors
        )

    def clear(self):

        self.sensors.clear()


sensor_registry = SensorRegistry()

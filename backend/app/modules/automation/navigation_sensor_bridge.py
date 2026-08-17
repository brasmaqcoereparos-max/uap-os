class NavigationSensorBridge:

    def __init__(self, sensors):

        self.sensors = sensors

    def get_distance(
        self,
        sensor_id,
    ):

        sensor = self.sensors.get(
            sensor_id
        )

        if sensor is None:
            return None

        return sensor.get_value()

    def obstacle_detected(
        self,
        sensor_id,
    ):

        sensor = self.sensors.get(
            sensor_id
        )

        if sensor is None:
            return False

        if hasattr(
            sensor,
            "is_detected",
        ):

            return sensor.is_detected()

        return False

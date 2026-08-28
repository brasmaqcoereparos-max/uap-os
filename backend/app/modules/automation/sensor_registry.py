class SensorRegistry:
    def __init__(self):
        self.sensors = {}

    def register(
        self,
        sensor_id,
        sensor=None,
        replace=True,
    ):
        if sensor is None:
            sensor = sensor_id

            sensor_id = getattr(
                sensor,
                "sensor_id",
                getattr(
                    sensor,
                    "id",
                    None,
                ),
            )

        if sensor_id is None:
            raise ValueError(
                "Sensor sem identificador."
            )

        sensor_id = str(sensor_id)

        if (
            sensor_id in self.sensors
            and not replace
        ):
            raise ValueError(
                "Sensor já registrado: "
                f"{sensor_id}"
            )

        self.sensors[
            sensor_id
        ] = sensor

        return sensor

    def unregister(self, sensor_id):
        return self.sensors.pop(
            str(sensor_id),
            None,
        )

    def get(self, sensor_id):
        return self.sensors.get(
            str(sensor_id)
        )

    def exists(self, sensor_id):
        return (
            str(sensor_id)
            in self.sensors
        )

    def get_all(self):
        return dict(
            self.sensors
        )

    def all(self):
        return list(
            self.sensors.values()
        )

    def ids(self):
        return list(
            self.sensors.keys()
        )

    def by_type(self, sensor_type):
        sensor_type = str(
            sensor_type
        ).strip().lower()

        return [
            sensor
            for sensor
            in self.sensors.values()
            if str(
                getattr(
                    sensor,
                    "sensor_type",
                    "",
                )
            ).lower()
            == sensor_type
        ]

    def clear(self):
        count = len(self.sensors)
        self.sensors.clear()

        return count

    def count(self):
        return len(self.sensors)


sensor_registry = SensorRegistry()

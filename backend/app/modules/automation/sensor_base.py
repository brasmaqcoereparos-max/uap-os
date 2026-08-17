class SensorBase:

    def __init__(
        self,
        sensor_id,
        name=None,
    ):

        self.sensor_id = sensor_id
        self.name = name or sensor_id

        self.enabled = False
        self.value = None
        self.status = "unknown"

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False

    def update(
        self,
        value,
    ):

        self.value = value
        self.status = "active"

    def get_value(self):

        return self.value

    def get_status(self):

        return self.status

    def is_enabled(self):

        return self.enabled

    def to_dict(self):

        return {
            "id": self.sensor_id,
            "name": self.name,
            "enabled": self.enabled,
            "value": self.value,
            "status": self.status,
        }

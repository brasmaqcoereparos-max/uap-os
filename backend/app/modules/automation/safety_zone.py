class SafetyZone:

    def __init__(
        self,
        name,
        minimum_distance=0,
    ):

        self.name = name
        self.minimum_distance = (
            minimum_distance
        )

        self.active = True

    def set_distance(
        self,
        distance,
    ):

        self.minimum_distance = max(
            0,
            distance,
        )

    def enable(self):

        self.active = True

    def disable(self):

        self.active = False

    def is_safe(
        self,
        distance,
    ):

        if not self.active:
            return True

        return distance >= (
            self.minimum_distance
        )

    def to_dict(self):

        return {
            "name": self.name,
            "minimum_distance":
                self.minimum_distance,
            "active": self.active,
        }

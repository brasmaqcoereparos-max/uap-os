from app.modules.automation.safety_zone import (
    SafetyZone,
)


class SafetyManager:

    def __init__(self):

        self.zones = {}

    def create_zone(
        self,
        name,
        minimum_distance=0,
    ):

        zone = SafetyZone(
            name,
            minimum_distance,
        )

        self.zones[name] = zone

        return zone

    def get_zone(
        self,
        name,
    ):

        return self.zones.get(name)

    def remove_zone(
        self,
        name,
    ):

        if name not in self.zones:
            return False

        self.zones.pop(name)

        return True

    def check_distance(
        self,
        distance,
    ):

        for zone in self.zones.values():

            if not zone.is_safe(distance):

                return False

        return True

    def get_zones(self):

        return dict(self.zones)


safety_manager = SafetyManager()

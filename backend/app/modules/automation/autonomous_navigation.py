class AutonomousNavigation:

    def __init__(
        self,
        localization,
        planner,
    ):

        self.localization = localization
        self.planner = planner

        self.active = False

    def start(self):

        self.active = True

    def stop(self):

        self.active = False

    def is_active(self):

        return self.active

    def get_next_target(self):

        if not self.active:

            return None

        return self.planner.next_point()

    def get_position(self):

        return self.localization.get_position()


autonomous_navigation = None

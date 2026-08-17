class DockingController:

    def __init__(
        self,
        station,
    ):

        self.station = station
        self.active = False

    def start(self):

        if not self.station.is_available():

            return False

        self.active = True

        return True

    def stop(self):

        self.active = False

    def is_active(self):

        return self.active

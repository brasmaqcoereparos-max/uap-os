class ChargingStation:

    def __init__(self):

        self.available = True
        self.robot_connected = False

    def set_available(
        self,
        available,
    ):

        self.available = available

    def connect_robot(self):

        if not self.available:

            return False

        self.robot_connected = True

        return True

    def disconnect_robot(self):

        self.robot_connected = False

    def is_available(self):

        return self.available

    def is_connected(self):

        return self.robot_connected


charging_station = ChargingStation()

class CartesianPose:

    def __init__(
        self,
        x=0,
        y=0,
        z=0,
        rx=0,
        ry=0,
        rz=0,
    ):

        self.x = x
        self.y = y
        self.z = z

        self.rx = rx
        self.ry = ry
        self.rz = rz

    def set_position(
        self,
        x,
        y,
        z,
    ):

        self.x = x
        self.y = y
        self.z = z

    def set_rotation(
        self,
        rx,
        ry,
        rz,
    ):

        self.rx = rx
        self.ry = ry
        self.rz = rz

    def get_position(self):

        return {
            "x": self.x,
            "y": self.y,
            "z": self.z,
        }

    def get_rotation(self):

        return {
            "rx": self.rx,
            "ry": self.ry,
            "rz": self.rz,
        }

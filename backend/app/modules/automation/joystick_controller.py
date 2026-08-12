class JoystickController:

    def __init__(self):

        self.x = 0
        self.y = 0
        self.z = 0

        self.rx = 0
        self.ry = 0
        self.rz = 0

        self.buttons = {}

    def set_axis(
        self,
        axis,
        value,
    ):

        value = max(
            -1.0,
            min(1.0, value),
        )

        if axis == "x":
            self.x = value
        elif axis == "y":
            self.y = value
        elif axis == "z":
            self.z = value
        elif axis == "rx":
            self.rx = value
        elif axis == "ry":
            self.ry = value
        elif axis == "rz":
            self.rz = value

    def set_button(
        self,
        button,
        pressed,
    ):

        self.buttons[button] = pressed

    def get_axes(self):

        return {
            "x": self.x,
            "y": self.y,
            "z": self.z,
            "rx": self.rx,
            "ry": self.ry,
            "rz": self.rz,
        }

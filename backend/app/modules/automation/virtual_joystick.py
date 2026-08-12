class VirtualJoystick:

    def __init__(self):

        self.x = 0
        self.y = 0
        self.speed = 0

    def move(self, x, y):

        self.x = max(-1.0, min(1.0, x))
        self.y = max(-1.0, min(1.0, y))

    def set_speed(self, speed):

        self.speed = max(
            0,
            min(100, speed),
        )

    def center(self):

        self.x = 0
        self.y = 0

    def get_state(self):

        return {
            "x": self.x,
            "y": self.y,
            "speed": self.speed,
        }

class MotionDevice:

    def __init__(self, name):

        self.name = name
        self.position = 0
        self.speed = 0
        self.direction = 1
        self.enabled = False

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False
        self.speed = 0

    def set_speed(self, speed):

        self.speed = max(0, speed)

    def set_direction(self, direction):

        if direction not in (-1, 1):
            raise ValueError(
                "Direction must be -1 or 1"
            )

        self.direction = direction

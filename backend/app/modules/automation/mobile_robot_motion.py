class MobileRobotMotion:

    def __init__(self):

        self.left_speed = 0
        self.right_speed = 0

    def set_speed(
        self,
        left,
        right,
    ):

        self.left_speed = left
        self.right_speed = right

    def stop(self):

        self.left_speed = 0
        self.right_speed = 0

    def forward(self, speed):

        self.set_speed(
            speed,
            speed,
        )

    def backward(self, speed):

        self.set_speed(
            -speed,
            -speed,
        )

    def turn_left(self, speed):

        self.set_speed(
            -speed,
            speed,
        )

    def turn_right(self, speed):

        self.set_speed(
            speed,
            -speed,
        )

    def get_speed(self):

        return {
            "left": self.left_speed,
            "right": self.right_speed,
        }

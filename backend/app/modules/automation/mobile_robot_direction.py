class MobileRobotDirection:

    FORWARD = "forward"
    BACKWARD = "backward"
    LEFT = "left"
    RIGHT = "right"
    STOP = "stop"

    @classmethod
    def all(cls):

        return [
            cls.FORWARD,
            cls.BACKWARD,
            cls.LEFT,
            cls.RIGHT,
            cls.STOP,
        ]

class MotionSegment:

    def __init__(
        self,
        start,
        end,
        speed=0,
        wait=0,
    ):

        self.start = start
        self.end = end
        self.speed = speed
        self.wait = wait

    def set_speed(self, speed):

        self.speed = max(
            0,
            speed,
        )

    def set_wait(self, wait):

        self.wait = max(
            0,
            wait,
        )

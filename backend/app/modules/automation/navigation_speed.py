class NavigationSpeed:

    def __init__(self):

        self.speed = 0

    def set(self, speed):

        self.speed = max(
            0,
            min(100, speed),
        )

    def increase(self, value=5):

        self.set(
            self.speed + value
        )

    def decrease(self, value=5):

        self.set(
            self.speed - value
        )

    def get(self):

        return self.speed

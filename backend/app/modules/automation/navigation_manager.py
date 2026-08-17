from app.modules.automation.navigation_speed import (
    NavigationSpeed,
)

from app.modules.automation.navigation_mode import (
    NavigationMode,
)

from app.modules.automation.trajectory import (
    Trajectory,
)


class NavigationManager:

    def __init__(self):

        self.speed = NavigationSpeed()
        self.mode = NavigationMode()
        self.trajectory = Trajectory()

    def set_speed(self, speed):

        self.speed.set(speed)

    def get_speed(self):

        return self.speed.get()

    def set_mode(self, mode):

        self.mode.set(mode)

    def get_mode(self):

        return self.mode.get()

    def add_point(self, point):

        return self.trajectory.add(point)

    def get_trajectory(self):

        return self.trajectory.get_all()

    def clear_trajectory(self):

        self.trajectory.clear()


navigation_manager = NavigationManager()

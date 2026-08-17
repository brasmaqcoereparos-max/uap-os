class PathPlanner:

    def __init__(self):

        self.path = []

    def set_path(
        self,
        points,
    ):

        self.path = list(points)

    def add_point(
        self,
        point,
    ):

        self.path.append(point)

    def clear(self):

        self.path.clear()

    def get_path(self):

        return list(self.path)

    def next_point(self):

        if not self.path:

            return None

        return self.path.pop(0)

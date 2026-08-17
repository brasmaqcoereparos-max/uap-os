class Trajectory:

    def __init__(self):

        self.points = []

    def add(self, point):

        self.points.append(point)

        return len(self.points) - 1

    def insert(
        self,
        index,
        point,
    ):

        index = max(
            0,
            min(index, len(self.points)),
        )

        self.points.insert(
            index,
            point,
        )

    def remove(self, index):

        if not (
            0 <= index < len(self.points)
        ):
            return False

        self.points.pop(index)

        return True

    def clear(self):

        self.points.clear()

    def get_all(self):

        return list(self.points)

    def to_dict(self):

        return {
            "points": [
                point.to_dict()
                for point in self.points
            ]
        }

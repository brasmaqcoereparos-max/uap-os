class RobotPositionView:

    def __init__(self):

        self.position = {}

    def update(self, positions):

        self.position = dict(positions)

    def get(self):

        return dict(self.position)

    def get_axis(self, axis_id):

        return self.position.get(axis_id)

class MultiAxisController:

    def __init__(self, robot):

        self.robot = robot

    def set_positions(self, positions):

        for axis_id, position in positions.items():

            self.robot.set_position(
                axis_id,
                position,
            )

    def get_positions(self):

        return self.robot.get_positions()

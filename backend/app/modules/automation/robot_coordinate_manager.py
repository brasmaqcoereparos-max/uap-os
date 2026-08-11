from app.modules.automation.cartesian_pose import (
    CartesianPose,
)

from app.modules.automation.coordinate_system import (
    CoordinateSystem,
)

from app.modules.automation.tool_frame import (
    ToolFrame,
)

from app.modules.automation.work_frame import (
    WorkFrame,
)


class RobotCoordinateManager:

    def __init__(self):

        self.world = CoordinateSystem()

        self.tool = ToolFrame()

        self.work = WorkFrame()

    def create_pose(
        self,
        x=0,
        y=0,
        z=0,
        rx=0,
        ry=0,
        rz=0,
    ):

        return CartesianPose(
            x,
            y,
            z,
            rx,
            ry,
            rz,
        )

    def get_world(self):

        return self.world

    def get_tool(self):

        return self.tool

    def get_work(self):

        return self.work


robot_coordinate_manager = (
    RobotCoordinateManager()
)

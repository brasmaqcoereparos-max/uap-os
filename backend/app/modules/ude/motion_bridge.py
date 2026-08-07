from app.modules.motion.axis_manager import (
    axis_manager,
)

from app.modules.motion.motion_manager import (
    motion_manager,
)


class MotionBridge:

    def axes(self):

        return axis_manager.list()

    def sequences(self):

        return motion_manager.list_sequences()


motion_bridge = MotionBridge()

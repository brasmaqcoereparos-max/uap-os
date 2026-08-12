from app.modules.automation.robot_sequence_executor import (
    RobotSequenceExecutor,
)

from app.modules.automation.robot_repeat_controller import (
    RobotRepeatController,
)

from app.modules.automation.robot_execution_position import (
    RobotExecutionPosition,
)


class RobotSequenceRunner:

    def __init__(self):

        self.executor = RobotSequenceExecutor()

        self.repeat = RobotRepeatController()

        self.position = RobotExecutionPosition()

    def load(self, poses, repeat=1):

        self.executor.load(poses)

        self.repeat.set_repeat(repeat)

    def start(self):

        self.repeat.start()

        return self.executor.start()

    def next(self):

        pose = self.executor.next()

        if pose is not None:

            self.position.set_target(pose)

            return pose

        if not self.repeat.finished():

            if self.repeat.next_cycle():

                self.executor.load(
                    self.executor.sequence
                )

                return self.executor.next()

        return None

    def stop(self):

        self.executor.stop()

    def get_position(self):

        return self.position.get_target()


robot_sequence_runner = RobotSequenceRunner()

from app.modules.automation.robot_sequence_runner import (
    robot_sequence_runner,
)


class RobotProgramExecutor:

    def load_program(self, program):

        poses = []

        for segment in program.segments:

            poses.append(
                {
                    "start": segment.start,
                    "end": segment.end,
                    "speed": segment.speed,
                    "wait": segment.wait,
                }
            )

        robot_sequence_runner.load(
            poses,
            program.repeat,
        )

    def start(self):

        return robot_sequence_runner.start()

    def next(self):

        return robot_sequence_runner.next()

    def stop(self):

        robot_sequence_runner.stop()

    def get_current_position(self):

        return robot_sequence_runner.get_position()


robot_program_executor = RobotProgramExecutor()

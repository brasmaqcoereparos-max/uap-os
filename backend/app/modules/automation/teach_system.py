from app.modules.automation.teach_record_service import (
    TeachRecordService,
)

from app.modules.automation.robot_position_view import (
    RobotPositionView,
)


class TeachSystem:

    def __init__(self):

        self.recorder = TeachRecordService()

        self.position_view = (
            RobotPositionView()
        )

    def start_recording(self):

        self.recorder.start()

    def record_position(self, pose):

        return self.recorder.record(
            pose
        )

    def stop_recording(self):

        self.recorder.stop()

    def update_position(self, positions):

        self.position_view.update(
            positions
        )

    def get_current_position(self):

        return self.position_view.get()

    def get_recorded_positions(self):

        return self.recorder.get()


teach_system = TeachSystem()

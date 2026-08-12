from app.modules.automation.pose_editor import (
    PoseEditor,
)


class PoseEditorService:

    def __init__(self):

        self.editor = PoseEditor()

    def update_position(
        self,
        pose,
        axis_id,
        position,
    ):

        self.editor.update_axis(
            pose,
            axis_id,
            position,
        )

        return pose

    def update_speed(
        self,
        pose,
        speed,
    ):

        self.editor.set_speed(
            pose,
            speed,
        )

        return pose

    def update_wait(
        self,
        pose,
        wait,
    ):

        self.editor.set_wait(
            pose,
            wait,
        )

        return pose


pose_editor_service = (
    PoseEditorService()
)

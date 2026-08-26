from app.modules.vision.vision_state import vision_state


class VisionStateManager:

    def start(self):
        vision_state.enabled = True
        vision_state.running = True

        return vision_state.to_dict()

    def stop(self):
        vision_state.running = False
        vision_state.cameras_active = 0

        return vision_state.to_dict()

    def enable(self):
        vision_state.enabled = True
        return vision_state.to_dict()

    def disable(self):
        vision_state.enabled = False
        vision_state.running = False

        return vision_state.to_dict()

    def set_cameras_active(self, count):
        vision_state.cameras_active = max(
            0,
            int(count),
        )

        return vision_state.cameras_active

    def record_frame(self):
        vision_state.record_frame()

    def record_analysis(self):
        vision_state.record_analysis()

    def record_detection(self, count=1):
        vision_state.record_detection(
            count
        )

    def record_motion(self):
        vision_state.record_motion()

    def record_person(self):
        vision_state.record_person()

    def set_event(self, event):
        vision_state.set_event(event)

    def set_analysis(self, analysis):
        vision_state.set_analysis(
            analysis
        )

    def status(self):
        return vision_state.to_dict()


vision_state_manager = VisionStateManager()

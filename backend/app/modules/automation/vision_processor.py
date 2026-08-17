from app.modules.automation.vision_result import (
    VisionResult,
)


class VisionProcessor:

    def __init__(self):

        self.enabled = False

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False

    def process(self, frame):

        if not self.enabled:
            return None

        result = VisionResult()

        # A implementação específica
        # de câmera/IA será conectada
        # posteriormente.

        return result

    def is_enabled(self):

        return self.enabled


vision_processor = VisionProcessor()

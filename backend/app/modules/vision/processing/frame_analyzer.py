from typing import Any

from app.modules.vision.processing.frame_processor import (
    frame_processor,
)


class FrameAnalyzer:

    def dimensions(self, frame: Any):

        if frame is None:
            return {
                "width": 0,
                "height": 0,
                "channels": 0,
            }

        shape = getattr(
            frame,
            "shape",
            (),
        )

        if len(shape) < 2:
            return {
                "width": 0,
                "height": 0,
                "channels": 0,
            }

        return {
            "width": int(shape[1]),
            "height": int(shape[0]),
            "channels": (
                int(shape[2])
                if len(shape) > 2
                else 1
            ),
        }

    def brightness(self, frame: Any):

        if frame is None:
            return 0.0

        gray = frame_processor.grayscale(
            frame
        )

        return float(
            gray.mean()
        )

    def analyze(self, frame: Any):

        dimensions = self.dimensions(
            frame
        )

        brightness = self.brightness(
            frame
        )

        return {
            "dimensions": dimensions,
            "brightness": brightness,
            "available": frame is not None,
        }


frame_analyzer = FrameAnalyzer()

from typing import Any


class MotionDetector:

    def __init__(self):
        self._previous_frame = None

    def reset(self):
        self._previous_frame = None

    def detect(
        self,
        frame: Any,
    ):

        if frame is None:
            return {
                "motion": False,
                "difference": 0.0,
            }

        if self._previous_frame is None:
            self._previous_frame = frame

            return {
                "motion": False,
                "difference": 0.0,
            }

        difference = self._difference(
            self._previous_frame,
            frame,
        )

        self._previous_frame = frame

        return {
            "motion": difference > 0.0,
            "difference": difference,
        }

    def _difference(
        self,
        previous,
        current,
    ):

        try:
            previous_array = previous.astype(
                "float32"
            )

            current_array = current.astype(
                "float32"
            )

            if previous_array.shape != current_array.shape:
                return 1.0

            difference = (
                abs(
                    previous_array
                    - current_array
                ).mean()
            )

            return float(difference)

        except Exception:
            return 1.0


motion_detector = MotionDetector()

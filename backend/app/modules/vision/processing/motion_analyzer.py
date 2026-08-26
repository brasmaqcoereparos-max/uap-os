from typing import Any


class MotionAnalyzer:

    def __init__(
        self,
        threshold: float = 8.0,
    ):
        self.threshold = float(
            threshold
        )

    def compare(
        self,
        previous: Any,
        current: Any,
    ):

        if previous is None or current is None:
            return {
                "motion": False,
                "difference": 0.0,
            }

        try:
            import cv2
        except ImportError as exc:
            raise RuntimeError(
                "OpenCV não está instalado."
            ) from exc

        if (
            previous.shape
            != current.shape
        ):
            return {
                "motion": True,
                "difference": 255.0,
            }

        previous_gray = cv2.cvtColor(
            previous,
            cv2.COLOR_BGR2GRAY,
        )

        current_gray = cv2.cvtColor(
            current,
            cv2.COLOR_BGR2GRAY,
        )

        difference = cv2.absdiff(
            previous_gray,
            current_gray,
        )

        value = float(
            difference.mean()
        )

        return {
            "motion": value
            >= self.threshold,
            "difference": value,
            "threshold": self.threshold,
        }


motion_analyzer = MotionAnalyzer()

from typing import Any


class FrameProcessor:

    def resize(
        self,
        frame: Any,
        width: int,
        height: int,
    ):

        if frame is None:
            return None

        try:
            import cv2
        except ImportError as exc:
            raise RuntimeError(
                "OpenCV não está instalado."
            ) from exc

        return cv2.resize(
            frame,
            (int(width), int(height)),
        )

    def grayscale(self, frame: Any):

        if frame is None:
            return None

        try:
            import cv2
        except ImportError as exc:
            raise RuntimeError(
                "OpenCV não está instalado."
            ) from exc

        return cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY,
        )

    def blur(
        self,
        frame: Any,
        kernel_size: int = 5,
    ):

        if frame is None:
            return None

        try:
            import cv2
        except ImportError as exc:
            raise RuntimeError(
                "OpenCV não está instalado."
            ) from exc

        kernel_size = max(
            1,
            int(kernel_size),
        )

        if kernel_size % 2 == 0:
            kernel_size += 1

        return cv2.GaussianBlur(
            frame,
            (
                kernel_size,
                kernel_size,
            ),
            0,
        )


frame_processor = FrameProcessor()

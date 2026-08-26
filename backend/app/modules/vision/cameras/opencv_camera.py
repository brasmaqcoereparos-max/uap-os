from typing import Any


class OpenCVCamera:

    def __init__(
        self,
        camera_id: str,
        source: Any = 0,
        width: int = 640,
        height: int = 480,
        fps: int = 15,
    ):
        self.camera_id = str(camera_id)
        self.source = source
        self.width = int(width)
        self.height = int(height)
        self.fps = int(fps)

        self._capture = None
        self._running = False

    def start(self):

        if self._running:
            return True

        try:
            import cv2
        except ImportError as exc:
            raise RuntimeError(
                "OpenCV não está instalado."
            ) from exc

        self._capture = cv2.VideoCapture(
            self.source
        )

        if not self._capture.isOpened():
            self._capture.release()
            self._capture = None

            raise RuntimeError(
                f"Não foi possível abrir "
                f"a câmera '{self.camera_id}'."
            )

        self._capture.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            self.width,
        )

        self._capture.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            self.height,
        )

        self._capture.set(
            cv2.CAP_PROP_FPS,
            self.fps,
        )

        self._running = True

        return True

    def stop(self):

        if self._capture is not None:
            self._capture.release()

        self._capture = None
        self._running = False

        return True

    def capture(self):

        if not self._running:
            self.start()

        if self._capture is None:
            return None

        success, frame = (
            self._capture.read()
        )

        if not success:
            return None

        return frame

    def status(self):

        return {
            "id": self.camera_id,
            "source": self.source,
            "width": self.width,
            "height": self.height,
            "fps": self.fps,
            "running": self._running,
            "available": (
                self._capture is not None
                and self._capture.isOpened()
            ),
        }

    def is_running(self):
        return self._running

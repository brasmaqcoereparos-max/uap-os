from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Camera:
    camera_id: str
    name: str
    device_id: str | None = None
    source: str | int | None = None
    width: int = 640
    height: int = 480
    fps: int = 30
    enabled: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)


class CameraManager:
    def __init__(self) -> None:
        self._cameras: dict[str, Camera] = {}

    def register(
        self,
        camera_id: str,
        name: str,
        device_id: str | None = None,
        source: str | int | None = None,
        width: int = 640,
        height: int = 480,
        fps: int = 30,
        metadata: dict[str, Any] | None = None,
    ) -> Camera:
        camera = Camera(
            camera_id=camera_id,
            name=name,
            device_id=device_id,
            source=source,
            width=width,
            height=height,
            fps=fps,
            metadata=metadata or {},
        )

        self._cameras[camera_id] = camera
        return camera

    def get(self, camera_id: str) -> Camera | None:
        return self._cameras.get(camera_id)

    def list(self) -> list[Camera]:
        return list(self._cameras.values())

    def configure(
        self,
        camera_id: str,
        width: int | None = None,
        height: int | None = None,
        fps: int | None = None,
    ) -> Camera:
        camera = self.get(camera_id)

        if camera is None:
            raise KeyError(
                f"Camera '{camera_id}' not found"
            )

        if width is not None:
            camera.width = width

        if height is not None:
            camera.height = height

        if fps is not None:
            camera.fps = fps

        return camera

    def remove(self, camera_id: str) -> bool:
        return self._cameras.pop(
            camera_id,
            None,
        ) is not None

from __future__ import annotations

from app.modules.vision.cameras.camera_service import (
    camera_service,
)
from app.modules.vision.pipeline.pipeline_runner import (
    pipeline_runner,
)
from app.modules.vision.pipeline.vision_pipeline import (
    vision_pipeline,
)


class PipelineService:

    def process(
        self,
        camera_id,
        frame,
        metadata=None,
    ):
        result = pipeline_runner.run(
            camera_id,
            frame,
            metadata,
        )

        return result.to_dict()

    def capture_and_process(
        self,
        camera_id: str,
        metadata=None,
    ):
        if not camera_id:
            raise ValueError(
                "camera_id obrigatório."
            )

        camera = camera_service.get(
            camera_id
        )

        frame = camera.capture()

        if frame is None:
            return {
                "camera_id": camera_id,
                "analysis": {},
                "events": [],
                "decisions": [],
                "actions": [],
                "success": False,
                "error": (
                    "Não foi possível "
                    "capturar frame da câmera."
                ),
            }

        pipeline_metadata = dict(
            metadata or {}
        )

        pipeline_metadata.setdefault(
            "camera_status",
            camera.status(),
        )

        result = pipeline_runner.run(
            camera_id=camera_id,
            frame=frame,
            metadata=pipeline_metadata,
        )

        return result.to_dict()

    def capture_frame(
        self,
        camera_id: str,
    ):
        if not camera_id:
            raise ValueError(
                "camera_id obrigatório."
            )

        return camera_service.capture(
            camera_id
        )

    def camera_status(
        self,
        camera_id: str,
    ):
        return camera_service.status(
            camera_id
        )

    def execute_flow(
        self,
        flow_name,
        context,
    ):
        return vision_pipeline.execute_flow(
            flow_name,
            context,
        )


pipeline_service = PipelineService()

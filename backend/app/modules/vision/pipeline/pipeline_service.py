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

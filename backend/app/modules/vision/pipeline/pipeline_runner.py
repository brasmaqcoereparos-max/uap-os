from app.modules.vision.pipeline.pipeline_context import (
    PipelineContext,
)

from app.modules.vision.pipeline.pipeline_result import (
    PipelineResult,
)

from app.modules.vision.pipeline.vision_pipeline import (
    vision_pipeline,
)


class PipelineRunner:

    def run(
        self,
        camera_id,
        frame,
        metadata=None,
    ):

        context = PipelineContext(
            camera_id=camera_id,
            frame=frame,
            metadata=metadata or {},
        )

        try:

            result = vision_pipeline.process(
                camera_id,
                frame,
            )

            context.update(
                analysis=result.get(
                    "analysis",
                    {},
                ),
                events=result.get(
                    "events",
                    [],
                ),
                decisions=result.get(
                    "decisions",
                    [],
                ),
                actions=result.get(
                    "actions",
                    [],
                ),
            )

            return PipelineResult(
                camera_id=camera_id,
                analysis=context.analysis,
                events=context.events,
                decisions=context.decisions,
                actions=context.actions,
            )

        except Exception as exc:

            return PipelineResult(
                camera_id=camera_id,
                success=False,
                error=str(exc),
            )


pipeline_runner = PipelineRunner()

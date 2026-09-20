from __future__ import annotations

from app.modules.vision.pipeline.pipeline_service import (
    pipeline_service,
)


class PipelineController:

    def execute(
        self,
        command,
    ):
        if not isinstance(
            command,
            dict,
        ):
            raise TypeError(
                "Comando de pipeline inválido."
            )

        action = str(
            command.get(
                "action",
                "",
            )
        ).strip().lower()

        if (
            action
            == "vision.pipeline.process"
        ):
            return (
                pipeline_service.process(
                    camera_id=(
                        command.get(
                            "camera_id"
                        )
                    ),
                    frame=(
                        command.get(
                            "frame"
                        )
                    ),
                    metadata=(
                        command.get(
                            "metadata",
                            {},
                        )
                    ),
                )
            )

        if (
            action
            == "vision.pipeline.capture"
        ):
            camera_id = (
                command.get(
                    "camera_id"
                )
            )

            if not camera_id:
                raise ValueError(
                    "camera_id obrigatório."
                )

            return (
                pipeline_service
                .capture_frame(
                    camera_id
                )
            )

        if (
            action
            == "vision.pipeline.capture_process"
        ):
            camera_id = (
                command.get(
                    "camera_id"
                )
            )

            if not camera_id:
                raise ValueError(
                    "camera_id obrigatório."
                )

            return (
                pipeline_service
                .capture_and_process(
                    camera_id=(
                        camera_id
                    ),
                    metadata=(
                        command.get(
                            "metadata",
                            {},
                        )
                    ),
                )
            )

        if (
            action
            == "vision.pipeline.camera_status"
        ):
            camera_id = (
                command.get(
                    "camera_id"
                )
            )

            if not camera_id:
                raise ValueError(
                    "camera_id obrigatório."
                )

            return (
                pipeline_service
                .camera_status(
                    camera_id
                )
            )

        if (
            action
            == "vision.pipeline.flow"
        ):
            flow_name = (
                command.get(
                    "flow_name"
                )
            )

            if not flow_name:
                raise ValueError(
                    "flow_name obrigatório."
                )

            return (
                pipeline_service
                .execute_flow(
                    flow_name=(
                        flow_name
                    ),
                    context=(
                        command.get(
                            "context",
                            {},
                        )
                    ),
                )
            )

        raise ValueError(
            "Ação de pipeline desconhecida: "
            f"{action}"
        )


pipeline_controller = (
    PipelineController()
)

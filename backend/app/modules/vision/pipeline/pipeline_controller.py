from app.modules.vision.pipeline.pipeline_service import (
    pipeline_service,
)


class PipelineController:

    def execute(self, command):

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

        if action == "vision.pipeline.process":

            return pipeline_service.process(
                camera_id=command.get(
                    "camera_id"
                ),
                frame=command.get(
                    "frame"
                ),
                metadata=command.get(
                    "metadata",
                    {},
                ),
            )

        if action == "vision.pipeline.flow":

            return pipeline_service.execute_flow(
                flow_name=command.get(
                    "flow_name"
                ),
                context=command.get(
                    "context",
                    {},
                ),
            )

        raise ValueError(
            f"Ação de pipeline desconhecida: "
            f"{action}"
        )


pipeline_controller = PipelineController()

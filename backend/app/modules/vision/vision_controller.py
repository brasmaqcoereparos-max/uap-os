from app.modules.vision.vision_manager import (
    vision_manager,
)

from app.modules.vision.vision_pipeline import (
    vision_pipeline,
)


class VisionController:

    def execute(
        self,
        command,
    ):

        if not isinstance(
            command,
            dict,
        ):
            raise TypeError(
                "Comando Vision inválido."
            )

        action = str(
            command.get(
                "action",
                "",
            )
        ).strip().lower()

        camera_id = command.get(
            "camera_id"
        )

        if action == "vision.camera.list":
            return [
                {
                    "id": camera_id,
                    "status": vision_manager.status(
                        camera_id
                    ),
                }
                for camera_id in vision_manager.cameras()
            ]

        if action == "vision.camera.count":
            return {
                "count": vision_manager.camera_count()
            }

        if not camera_id:
            raise ValueError(
                "camera_id obrigatório."
            )

        if action == "vision.camera.start":
            return vision_manager.start(
                camera_id
            )

        if action == "vision.camera.stop":
            return vision_manager.stop(
                camera_id
            )

        if action == "vision.camera.capture":
            return vision_manager.capture(
                camera_id
            )

        if action == "vision.camera.status":
            return vision_manager.status(
                camera_id
            )

        if action == "vision.analyze":
            return vision_pipeline.process(
                camera_id
            )

        raise ValueError(
            f"Ação Vision desconhecida: {action}"
        )


vision_controller = VisionController()

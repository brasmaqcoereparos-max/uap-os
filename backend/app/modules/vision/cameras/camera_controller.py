from app.modules.vision.cameras.camera_service import (
    camera_service,
)


class CameraController:

    def execute(self, command):

        if not isinstance(
            command,
            dict,
        ):
            raise TypeError(
                "Comando de câmera inválido."
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

        if action == "camera.register":

            if not camera_id:
                raise ValueError(
                    "camera_id obrigatório."
                )

            return camera_service.register(
                camera_id=camera_id,
                source=command.get(
                    "source",
                    0,
                ),
                width=command.get(
                    "width",
                    640,
                ),
                height=command.get(
                    "height",
                    480,
                ),
                fps=command.get(
                    "fps",
                    15,
                ),
                metadata=command.get(
                    "metadata"
                ),
            ).status()

        if action == "camera.list":
            return camera_service.status_all()

        if not camera_id:
            raise ValueError(
                "camera_id obrigatório."
            )

        if action == "camera.remove":
            return bool(
                camera_service.remove(
                    camera_id
                )
            )

        if action == "camera.start":
            return camera_service.start(
                camera_id
            )

        if action == "camera.stop":
            return camera_service.stop(
                camera_id
            )

        if action == "camera.capture":
            return camera_service.capture(
                camera_id
            )

        if action == "camera.status":
            return camera_service.status(
                camera_id
            )

        raise ValueError(
            f"Ação de câmera desconhecida: {action}"
        )


camera_controller = CameraController()

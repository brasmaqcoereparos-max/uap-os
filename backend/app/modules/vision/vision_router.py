from app.modules.vision.vision_controller import (
    vision_controller,
)


class VisionRouter:

    def route(self, command):

        if not isinstance(command, dict):
            raise TypeError(
                "Comando Vision inválido."
            )

        return vision_controller.execute(
            command
        )


vision_router = VisionRouter()

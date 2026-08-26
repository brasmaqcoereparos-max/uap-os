from app.modules.vision.events.vision_event_service import (
    vision_event_service,
)


class VisionEventController:

    def execute(self, command):

        if not isinstance(
            command,
            dict,
        ):
            raise TypeError(
                "Comando de evento inválido."
            )

        action = str(
            command.get(
                "action",
                "",
            )
        ).strip().lower()

        if action == "vision.event.process":

            return vision_event_service.process(
                camera_id=command.get(
                    "camera_id"
                ),
                analysis=command.get(
                    "analysis",
                    {},
                ),
            )

        if action == "vision.event.latest":

            return vision_event_service.latest()

        if action == "vision.event.list":

            return vision_event_service.list()

        if action == "vision.event.count":

            return vision_event_service.count()

        raise ValueError(
            f"Ação de evento desconhecida: "
            f"{action}"
        )


vision_event_controller = (
    VisionEventController()
      )

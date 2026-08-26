from app.modules.vision.ai.local.local_ai_service import (
    local_ai_service,
)


class LocalAIController:

    def execute(self, command):

        if not isinstance(
            command,
            dict,
        ):
            raise TypeError(
                "Comando de IA local inválido."
            )

        action = str(
            command.get(
                "action",
                "",
            )
        ).strip().lower()

        if action == "ai.local.load":

            return local_ai_service.load_onnx(
                name=command.get(
                    "name"
                ),
                path=command.get(
                    "path"
                ),
                providers=command.get(
                    "providers"
                ),
            )

        if action == "ai.local.remove":

            return bool(
                local_ai_service.remove(
                    command.get(
                        "name"
                    )
                )
            )

        if action == "ai.local.status":

            return local_ai_service.status()

        raise ValueError(
            f"Ação IA local desconhecida: "
            f"{action}"
        )


local_ai_controller = (
    LocalAIController()
      )

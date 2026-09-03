from app.modules.voice.response import (
    VoiceResponse,
)


class VoiceResponseBuilder:

    def from_dispatch(
        self,
        dispatch: dict | None,
    ):
        if not dispatch:
            return VoiceResponse(
                text=(
                    "Não foi possível "
                    "processar o comando."
                ),
                level="error",
            )

        status = dispatch.get(
            "status"
        )

        if status == "ready":
            return VoiceResponse(
                text=(
                    "Comando pronto "
                    "para execução."
                ),
                level="success",
            )

        if (
            status
            == "confirmation_required"
        ):
            return VoiceResponse(
                text=(
                    "Confirme para "
                    "continuar."
                ),
                level="warning",
            )

        if status == "rejected":
            errors = dispatch.get(
                "errors",
                [],
            )

            text = (
                errors[0]
                if errors
                else (
                    "Comando rejeitado."
                )
            )

            return VoiceResponse(
                text=text,
                level="error",
            )

        return VoiceResponse(
            text="Comando processado."
        )

    def from_execution(
        self,
        execution: dict | None,
    ):
        if not execution:
            return VoiceResponse(
                text=(
                    "Aguardando ação."
                ),
                speak=False,
            )

        if execution.get(
            "executed"
        ):
            return VoiceResponse(
                text=(
                    "Comando executado."
                ),
                level="success",
            )

        errors = execution.get(
            "errors",
            [],
        )

        return VoiceResponse(
            text=(
                errors[0]
                if errors
                else (
                    "Falha na execução."
                )
            ),
            level="error",
        )


voice_response_builder = (
    VoiceResponseBuilder()
          )

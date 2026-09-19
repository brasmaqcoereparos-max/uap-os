from __future__ import annotations

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
                metadata={
                    "confirmation_id": (
                        dispatch.get(
                            "confirmation_id"
                        )
                    ),
                },
            )

        if status == "rejected":
            errors = dispatch.get(
                "errors",
                [],
            )

            text = (
                errors[0]
                if errors
                else "Comando rejeitado."
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
                text="Aguardando ação.",
                speak=False,
            )

        if execution.get(
            "executed"
        ):
            return VoiceResponse(
                text="Comando executado.",
                level="success",
                metadata={
                    "status": (
                        execution.get(
                            "status"
                        )
                    ),
                },
            )

        errors = execution.get(
            "errors",
            [],
        )

        return VoiceResponse(
            text=(
                errors[0]
                if errors
                else "Falha na execução."
            ),
            level="error",
        )

    def from_result(
        self,
        result: dict | None,
    ):
        if not result:
            return VoiceResponse(
                text=(
                    "Não foi possível "
                    "processar a solicitação."
                ),
                level="error",
            )

        error = result.get(
            "error"
        )

        if error:
            return VoiceResponse(
                text=str(
                    error
                ),
                level="error",
            )

        execution = result.get(
            "execution"
        )

        if execution is not None:
            return self.from_execution(
                execution
            )

        dispatch = result.get(
            "dispatch"
        )

        if dispatch is not None:
            return self.from_dispatch(
                dispatch
            )

        if result.get(
            "command"
        ) is None:
            return VoiceResponse(
                text=(
                    "Não identifiquei "
                    "um comando."
                ),
                level="warning",
            )

        return VoiceResponse(
            text="Comando processado.",
            level="success",
        )


voice_response_builder = (
    VoiceResponseBuilder()
)

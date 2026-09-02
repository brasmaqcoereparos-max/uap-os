from app.modules.voice.enums import (
    VoiceIntentType,
)
from app.modules.voice.intent import (
    VoiceIntent,
)
from app.modules.voice.transcript import (
    VoiceTranscript,
)


class VoiceIntentResolver:

    NAVIGATION = {
        "início": "/home",
        "inicio": "/home",
        "home": "/home",
        "painel": "/dashboard",
        "dashboard": "/dashboard",
    }

    CONFIRMATIONS = {
        "sim",
        "confirmar",
        "confirma",
        "confirmo",
        "ok",
    }

    CANCELLATIONS = {
        "não",
        "nao",
        "cancelar",
        "cancela",
        "pare",
    }

    def resolve(
        self,
        transcript: VoiceTranscript,
    ):
        text = (
            transcript
            .normalized_text()
            .lower()
        )

        if not text:
            return VoiceIntent(
                name="unknown",
                source_text=text,
            )

        if text in self.CONFIRMATIONS:
            return VoiceIntent(
                name="confirm",
                intent_type=(
                    VoiceIntentType
                    .CONFIRMATION
                ),
                confidence=1.0,
                source_text=text,
            )

        if text in self.CANCELLATIONS:
            return VoiceIntent(
                name="cancel",
                intent_type=(
                    VoiceIntentType
                    .CANCELLATION
                ),
                confidence=1.0,
                source_text=text,
            )

        navigation = (
            self._navigation(
                text
            )
        )

        if navigation:
            return navigation

        return VoiceIntent(
            name="command",
            intent_type=(
                VoiceIntentType.COMMAND
            ),
            confidence=0.5,
            parameters={
                "text": text,
            },
            source_text=text,
        )

    def _navigation(
        self,
        text: str,
    ):
        prefixes = (
            "abrir ",
            "abra ",
            "ir para ",
            "vá para ",
            "va para ",
            "mostrar ",
            "mostre ",
        )

        target = text

        for prefix in prefixes:
            if text.startswith(
                prefix
            ):
                target = text[
                    len(prefix):
                ].strip()

                break

        route = self.NAVIGATION.get(
            target
        )

        if not route:
            return None

        return VoiceIntent(
            name="navigate",
            intent_type=(
                VoiceIntentType
                .NAVIGATION
            ),
            confidence=0.95,
            parameters={
                "route": route,
            },
            source_text=text,
        )


voice_intent_resolver = (
    VoiceIntentResolver()
      )

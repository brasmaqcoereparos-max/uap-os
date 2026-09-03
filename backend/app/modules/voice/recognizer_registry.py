from app.modules.voice.recognizer import (
    VoiceRecognizer,
)


class VoiceRecognizerRegistry:

    def __init__(self):
        self._recognizers: dict[
            str,
            VoiceRecognizer,
        ] = {}

        self._default: (
            str | None
        ) = None

    def register(
        self,
        recognizer: VoiceRecognizer,
        default: bool = False,
    ):
        self._recognizers[
            recognizer.name
        ] = recognizer

        if (
            default
            or self._default is None
        ):
            self._default = (
                recognizer.name
            )

        return recognizer

    def get(
        self,
        name: str,
    ):
        return self._recognizers.get(
            name
        )

    def default(self):
        if self._default is None:
            return None

        return self.get(
            self._default
        )

    def set_default(
        self,
        name: str,
    ):
        if (
            name
            not in self._recognizers
        ):
            raise ValueError(
                "Voice recognizer "
                "not found"
            )

        self._default = name

        return self.get(name)

    def available(self):
        return [
            recognizer
            for recognizer
            in self._recognizers.values()
            if recognizer.available()
        ]

    def list_all(self):
        return list(
            self._recognizers.values()
        )


voice_recognizer_registry = (
    VoiceRecognizerRegistry()
)

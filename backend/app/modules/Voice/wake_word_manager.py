from app.modules.voice.wake_word import (
    VoiceWakeWord,
)


class VoiceWakeWordManager:

    def __init__(self):
        self._wake_words: list[
            VoiceWakeWord
        ] = [
            VoiceWakeWord(
                phrase="uap"
            )
        ]

    def register(
        self,
        wake_word: VoiceWakeWord,
    ):
        self._wake_words.append(
            wake_word
        )

        return wake_word

    def list_all(self):
        return list(
            self._wake_words
        )

    def detect(
        self,
        text: str,
    ):
        for wake_word in (
            self._wake_words
        ):
            if wake_word.matches(text):
                return wake_word

        return None

    def strip(
        self,
        text: str,
    ):
        wake_word = self.detect(
            text
        )

        if not wake_word:
            return {
                "detected": False,
                "text": text.strip(),
                "wake_word": None,
            }

        return {
            "detected": True,
            "text": wake_word.strip(
                text
            ),
            "wake_word": (
                wake_word.phrase
            ),
        }


voice_wake_word_manager = (
    VoiceWakeWordManager()
)

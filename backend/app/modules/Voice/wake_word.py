from dataclasses import dataclass


@dataclass
class VoiceWakeWord:
    phrase: str = "uap"

    enabled: bool = True

    case_sensitive: bool = False

    def matches(
        self,
        text: str,
    ):
        if not self.enabled:
            return False

        source = text.strip()
        target = self.phrase.strip()

        if not self.case_sensitive:
            source = source.lower()
            target = target.lower()

        return (
            source == target
            or source.startswith(
                f"{target} "
            )
        )

    def strip(
        self,
        text: str,
    ):
        if not self.matches(text):
            return text.strip()

        source = text.strip()

        length = len(
            self.phrase
        )

        return source[
            length:
        ].strip()

from app.modules.voice.context_buffer import (
    VoiceContextBuffer,
)
from app.modules.voice.context_item import (
    VoiceContextItem,
)


class VoiceSessionContext:

    def __init__(
        self,
        session_id: str,
    ):
        self.session_id = session_id

        self.buffer = (
            VoiceContextBuffer()
        )

    def add_user(
        self,
        text: str,
    ):
        return self.buffer.add(
            VoiceContextItem.create(
                role="user",
                content=text,
            )
        )

    def add_system(
        self,
        text: str,
    ):
        return self.buffer.add(
            VoiceContextItem.create(
                role="system",
                content=text,
            )
        )

    def add_assistant(
        self,
        text: str,
    ):
        return self.buffer.add(
            VoiceContextItem.create(
                role="assistant",
                content=text,
            )
        )

    def history(self):
        return self.buffer.to_dict()

    def clear(self):
        self.buffer.clear()

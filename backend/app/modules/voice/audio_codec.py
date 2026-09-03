import base64


class VoiceAudioCodec:

    @staticmethod
    def decode_base64(
        value: str,
    ):
        try:
            return base64.b64decode(
                value,
                validate=True,
            )

        except Exception as exc:
            raise ValueError(
                "Invalid base64 audio data"
            ) from exc

    @staticmethod
    def encode_base64(
        value: bytes,
    ):
        return (
            base64.b64encode(
                value
            )
            .decode("ascii")
        )


voice_audio_codec = (
    VoiceAudioCodec()
)

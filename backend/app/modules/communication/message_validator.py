from app.modules.communication.message_envelope import (
    CommunicationMessageEnvelope,
)
from app.modules.communication.message_validation import (
    CommunicationMessageValidation,
)


class CommunicationMessageValidator:

    def validate(
        self,
        envelope: (
            CommunicationMessageEnvelope
        ),
    ):
        result = (
            CommunicationMessageValidation(
                valid=True
            )
        )

        if not envelope.id.strip():
            result.add_error(
                "Message id is empty"
            )

        if not envelope.topic.strip():
            result.add_error(
                "Message topic is empty"
            )

        if not envelope.source.strip():
            result.add_error(
                "Message source is empty"
            )

        if not isinstance(
            envelope.payload,
            dict,
        ):
            result.add_error(
                "Message payload "
                "must be a dictionary"
            )

        return result


communication_message_validator = (
    CommunicationMessageValidator()
)

import uuid

from app.modules.security.key_record import (
    SecurityKeyRecord,
)
from app.modules.security.key_registry import (
    security_key_registry,
)


class SecurityKeyRotationService:

    def create_initial(self):
        key_id = str(
            uuid.uuid4()
        )

        key = SecurityKeyRecord(
            key_id=key_id
        )

        security_key_registry.register(
            key
        )

        return key

    def rotate(
        self,
        current_key_id: str,
    ):
        current = (
            security_key_registry
            .get(
                current_key_id
            )
        )

        if not current:
            raise ValueError(
                "Security key not found"
            )

        current.active = False

        new_key = SecurityKeyRecord(
            key_id=str(
                uuid.uuid4()
            ),
            rotated_from=(
                current_key_id
            ),
        )

        security_key_registry.register(
            new_key
        )

        return new_key


security_key_rotation_service = (
    SecurityKeyRotationService()
)

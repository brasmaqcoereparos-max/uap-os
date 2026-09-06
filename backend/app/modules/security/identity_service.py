import hashlib
import platform
import uuid

from app.modules.security.device_identity import (
    DeviceIdentity,
)


class DeviceIdentityService:

    def generate(
        self,
        serial_number: str | None = None,
        board: str = "",
        model: str = "",
    ):
        machine = (
            platform.machine()
        )

        node = str(
            uuid.getnode()
        )

        base = (
            serial_number
            or f"{machine}:{node}"
        )

        hardware_id = (
            hashlib.sha256(
                base.encode(
                    "utf-8"
                )
            )
            .hexdigest()
        )

        device_id = (
            hardware_id[:24]
        )

        return DeviceIdentity(
            device_id=device_id,
            serial_number=(
                serial_number
                or node
            ),
            hardware_id=(
                hardware_id
            ),
            board=board,
            model=model,
        )


device_identity_service = (
    DeviceIdentityService()
      )
